# PRISM Review Status

This ledger distinguishes automated link health from manual content freshness. A working URL does not confirm that a regulation, standard, tool, or description remains current.

**Tracking baseline established:** 2026-06-24  
**Review owner:** Repository maintainer  
**Rule:** Record a dated content review only after checking the linked primary source and the description in `README.md`.

See [`docs/source-reviews/2026-07-core-authoritative-sources.md`](docs/source-reviews/2026-07-core-authoritative-sources.md) for the scope and limits of the first documented source review.

## Regulatory Frameworks

| Section | Last confirmed content review | Next review due | Status |
|---|---:|---:|---|
| United States | 2026-07-07 | 2026-10-07 | Initial NIST AI hub source classification reviewed; OMB source remains pending |
| European Union | 2026-07-07 | 2026-10-07 | Initial source classification reviewed; legal-timeline interpretation remains out of scope |
| International Standards | 2026-07-07 | 2026-10-07 | Initial ISO/OECD source and description review completed; IEEE and ISO/IEC 23894 remain pending |

## Other active resources

| Section | Last confirmed content review | Next review due | Status |
|---|---:|---:|---|
| Open-source tools and platforms | Not yet recorded | 2026-09-24 | Requires initial manual review |
| Benchmarks and evaluation frameworks | Not yet recorded | 2026-09-24 | Requires initial manual review |
| Communities and courses | Not yet recorded | 2026-12-24 | Requires initial manual review |
| LLM security guidance | 2026-07-07 | 2026-10-07 | OWASP source reviewed and README destination refreshed to the current GenAI Security Project page |
| Adversarial-AI knowledge bases | 2026-07-07 | 2026-10-07 | MITRE ATLAS source classification reviewed; technique coverage review remains pending |

## Update procedure

When completing a manual review:

1. Check the source remains maintained or authoritative.
2. Confirm whether a newer version or replacement exists.
3. Validate that the one-sentence README description remains accurate.
4. Replace the `Last confirmed content review` and `Next review due` values.
5. Note material removals or replacements in the pull request description.
