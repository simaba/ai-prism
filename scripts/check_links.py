#!/usr/bin/env python3
"""Create a JSON report of local and external Markdown link health.

This script is diagnostic only. The Lychee workflow remains the blocking link check.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen


MARKDOWN_LINK = re.compile(r'!?(?:\[[^\]]*\])\(([^)\s]+)(?:\s+"[^"]*")?\)')
HTTP_SUCCESS = set(range(200, 400)) | {403, 429}
SKIPPED_PREFIXES = ("mailto:", "tel:", "#")
MAX_WORKERS = 8


def _iter_urls(paths: Iterable[Path]) -> Iterable[Tuple[Path, int, str]]:
    for path in paths:
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for target in MARKDOWN_LINK.findall(line):
                yield path, line_number, target.strip("<>")


def _check_external(url: str) -> Dict[str, object]:
    request = Request(
        url,
        headers={"User-Agent": "simaba-ai-prism-link-check/1.0"},
        method="HEAD",
    )
    try:
        with urlopen(request, timeout=12) as response:
            status = response.getcode()
            return {"status": status, "ok": status in HTTP_SUCCESS}
    except HTTPError as exc:
        if exc.code == 405:
            get_request = Request(
                url,
                headers={"User-Agent": "simaba-ai-prism-link-check/1.0"},
            )
            try:
                with urlopen(get_request, timeout=12) as response:
                    status = response.getcode()
                    return {"status": status, "ok": status in HTTP_SUCCESS}
            except HTTPError as get_error:
                return {"status": get_error.code, "ok": get_error.code in HTTP_SUCCESS}
            except URLError as get_error:
                return {"status": None, "ok": False, "error": str(get_error.reason)}
        return {"status": exc.code, "ok": exc.code in HTTP_SUCCESS}
    except URLError as exc:
        return {"status": None, "ok": False, "error": str(exc.reason)}


def _check_local(url: str, source: Path) -> Dict[str, object]:
    target = unquote(url.split("#", 1)[0])
    if not target:
        return {"status": "anchor", "ok": True}
    path = (source.parent / target).resolve()
    return {"status": "local", "ok": path.exists(), "resolved_path": str(path)}


def _check_entry(entry: Tuple[Path, int, str]) -> Dict[str, object]:
    source, line_number, url = entry
    parsed = urlparse(url)
    if parsed.scheme in {"http", "https"}:
        outcome = _check_external(url)
    else:
        outcome = _check_local(url, source)
    return {
        "source": str(source),
        "line": line_number,
        "url": url,
        **outcome,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a diagnostic Markdown link report.")
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    checked: Set[str] = set()
    entries: List[Tuple[Path, int, str]] = []
    for source, line_number, url in _iter_urls(args.paths):
        if url.startswith(SKIPPED_PREFIXES) or "img.shields.io" in url:
            continue
        cache_key = "{}:{}".format(source, url)
        if cache_key in checked:
            continue
        checked.add(cache_key)
        entries.append((source, line_number, url))

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = list(executor.map(_check_entry, entries))

    failures = [result for result in results if not result["ok"]]
    report = {"checked": len(results), "failures": failures, "results": results}
    args.report.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("checked={} failures={}".format(len(results), len(failures)))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
