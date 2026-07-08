# Core Authoritative-Source Review — 2026-07-07

## Scope

This was a limited first-pass content review of the core authoritative sources that anchor PRISM's regulatory and security sections. It did **not** validate every linked tool, benchmark, community, course, or secondary guide.

## Reviewed sources and findings

| Resource | Result | README description check | Follow-up |
|---|---|---|---|
| NIST AI program hub | Official NIST page identifies the AI RMF, Center for AI Standards and Innovation, AI Resource Center, standards work, evaluations, and NIST's nonregulatory measurement-science role. | Updated the U.S. entry to point to the broader current NIST AI hub rather than an older executive-order page. | Review the AI RMF and supporting resources separately, including current profiles and implementation guidance. |
| ISO/IEC 42001:2023 | Official ISO page identifies it as a published international standard for an AI management system. | Accurate. | Keep the existing ISO link and review on the normal standards cadence. |
| OECD AI Principles | Official OECD page states that the principles promote innovative, trustworthy AI and were updated in May 2024. | Accurate but could eventually note the 2024 update. | Keep the existing link. |
| OWASP Top 10 for LLM Applications | Official OWASP page states that the original Top 10 is now part of the broader OWASP GenAI Security Project and directs readers to the current dedicated LLM Top 10 location. | Updated the README destination and label to the current GenAI Security Project LLM Top 10 page. | Review OWASP's agentic-app and GenAI governance resources separately. |
| EU AI Act | The README links directly to the official EUR-Lex text for Regulation (EU) 2024/1689. | Accurate as a source classification. | Review implementation dates and related secondary guidance separately; do not rely on the hub's one-line entry for legal interpretation. |
| MITRE ATLAS | The README links to the official MITRE ATLAS site. | Accurate as a source classification. | Perform a separate content review of ATLAS technique coverage and release/versioning. |

## Review discipline

- A source was recorded as reviewed only where the source owner and high-level description could be checked directly.
- This review did not certify legal currency, implementation completeness, safety sufficiency, or applicability to any organization.
- Secondary summaries remain secondary. The EU AI Act summary entry should continue to direct readers back to EUR-Lex for legal interpretation.

## Next review priorities

1. Review NIST AI RMF and related implementation resources separately, including current supporting profiles and resources.
2. Review OWASP's agentic-app security, AI security governance checklist, and GenAI Security Project resources beyond the LLM Top 10.
3. Complete the first manual review of open-source tools, benchmarks, and communities using the criteria in `CURATION.md`.
