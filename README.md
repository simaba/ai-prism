# PRISM — AI Governance Resource Hub

> Practical Resources for Intelligent Systems Management — a curated collection
> of frameworks, tools, regulations, papers, and open-source projects for
> responsible and trustworthy AI deployment in regulated industries.

Maintained by [Sima Bagheri](https://github.com/simaba) · [LinkedIn](https://www.linkedin.com/in/simaba/) · [Medium](https://medium.com/@bagheri.sima)

**Focus areas:** Enterprise AI governance · LLM deployment safety · Risk management · Regulatory compliance (NIST AI RMF, EU AI Act, ISO 42001) · Release readiness · Incident response

---

## Curation standard

This is a curated resource hub, not a link dump. Resources should be practical, credible, and relevant to AI governance, evaluation, risk management, release readiness, or incident response.

See [`CURATION.md`](CURATION.md) for:

- inclusion and exclusion criteria
- source preference rules
- freshness review cadence
- description-quality standards
- contribution review checklist

A blocking link-check workflow runs on pull requests and monthly. `REVIEW_STATUS.md` tracks manual content freshness separately from URL availability.

---

## Contents

- [Regulatory Frameworks](#regulatory-frameworks)
- [Risk Management Frameworks](#risk-management-frameworks)
- [Governance Tools & Platforms](#governance-tools--platforms)
- [AI Testing & Evaluation](#ai-testing--evaluation)
- [Incident Management](#incident-management)
- [Model Cards & Documentation](#model-cards--documentation)
- [Academic Papers](#academic-papers)
- [Datasets & Benchmarks](#datasets--benchmarks)
- [Communities & Organizations](#communities--organizations)
- [Courses & Learning](#courses--learning)
- [My Open-Source Frameworks](#my-open-source-frameworks)

---

## Regulatory Frameworks

### United States

- **[NIST AI Risk Management Framework](https://airc.nist.gov/home)** — NIST’s official hub for the voluntary framework organized around Govern, Map, Measure, and Manage.
- **[NIST AI Program and Center for AI Standards and Innovation](https://www.nist.gov/artificial-intelligence)** — NIST’s official AI hub covering AI RMF resources, measurement science, standards, evaluations, and related federal AI programs.
- **[OMB AI Governance Policy M-24-10](https://www.whitehouse.gov/wp-content/uploads/2024/03/M-24-10-Advancing-Governance-Innovation-and-Risk-Management-for-Agency-Use-of-Artificial-Intelligence.pdf)** — U.S. federal agency governance and risk-management requirements for AI use.

### European Union

- **[EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)** — Official risk-based legal framework for AI in the European Union.
- **[EU AI Act Summary](https://artificialintelligenceact.eu/)** — Secondary plain-language guide to provisions and timelines; confirm legal interpretation against the official text.

### International Standards

- **[ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html)** — International standard for AI management systems.
- **[ISO/IEC 23894:2023](https://www.iso.org/standard/77304.html)** — Guidance on risk management for AI systems.
- **[IEEE 7000 Series](https://standards.ieee.org/initiatives/artificial-intelligence-systems/standards/)** — Standards for ethically aligned AI design.
- **[OECD AI Principles](https://oecd.ai/en/ai-principles)** — International principles for trustworthy AI.

---

## Risk Management Frameworks

- **[NIST AI RMF Core](https://airc.nist.gov/home)** — Interactive starting point for NIST AI RMF categories and subcategories.
- **[Microsoft Responsible AI Standard](https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-Responsible-AI-Standard-v2-General-Requirements-3.pdf)** — Public responsible-AI standard and requirements guide.
- **[Google PAIR Guidebook](https://pair.withgoogle.com/guidebook/)** — People + AI Research guidebook for human-centered AI design.
- **[MITRE ATLAS](https://atlas.mitre.org/)** — Knowledge base of AI-specific adversarial tactics and techniques.
- **[OWASP Top 10 for LLMs and GenAI Apps](https://genai.owasp.org/llm-top-10/)** — Current OWASP GenAI Security Project page for LLM and generative-AI application risks and mitigations.

---

## Governance Tools & Platforms

- **[Microsoft Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/responsible-ai-toolbox?style=social) — Tools for error analysis, fairness, causal inference, and counterfactual analysis.
- **[Giskard](https://github.com/Giskard-AI/giskard)** ![GitHub stars](https://img.shields.io/github/stars/Giskard-AI/giskard?style=social) — Open-source AI quality testing platform.
- **[Evidently AI](https://github.com/evidentlyai/evidently)** ![GitHub stars](https://img.shields.io/github/stars/evidentlyai/evidently?style=social) — Evaluation, testing, and monitoring for ML and LLM systems.
- **[WhyLabs](https://whylabs.ai/)** — AI observability and model monitoring platform.
- **[Fiddler AI](https://www.fiddler.ai/)** — Explainability and model-performance monitoring platform.
- **[Microsoft PyRIT](https://github.com/Azure/PyRIT)** ![GitHub stars](https://img.shields.io/github/stars/Azure/PyRIT?style=social) — Python toolkit for generative-AI red teaming.
- **[LangFuse](https://github.com/langfuse/langfuse)** ![GitHub stars](https://img.shields.io/github/stars/langfuse/langfuse?style=social) — Open-source LLM observability and analytics.

---

## AI Testing & Evaluation

- **[Holistic Evaluation of Language Models (HELM)](https://crfm.stanford.edu/helm/)** — Comprehensive LLM evaluation across scenarios, metrics, and models.
- **[EleutherAI LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness)** ![GitHub stars](https://img.shields.io/github/stars/EleutherAI/lm-evaluation-harness?style=social) — Unified framework for evaluating language models.
- **[DeepEval](https://github.com/confident-ai/deepeval)** ![GitHub stars](https://img.shields.io/github/stars/confident-ai/deepeval?style=social) — LLM evaluation metrics for RAG, hallucination, and safety.
- **[TruLens](https://github.com/truera/trulens)** ![GitHub stars](https://img.shields.io/github/stars/truera/trulens?style=social) — Evaluation and tracking for LLM-based applications.
- **[RAGAS](https://github.com/explodinggradients/ragas)** ![GitHub stars](https://img.shields.io/github/stars/explodinggradients/ragas?style=social) — Evaluation framework for retrieval-augmented generation.
- **[MLflow Model Evaluation](https://mlflow.org/docs/latest/model-evaluation/index.html)** — Model evaluation with LLM and custom-metric support.

---

## Incident Management

- **[AI Incident Database](https://incidentdatabase.ai/)** — Crowd-sourced database of AI incidents and failures.
- **[AI Vulnerability Database (AVID)](https://avidml.org/)** — Taxonomy of AI failure modes, biases, and vulnerabilities.
- **[NIST AI RMF Core](https://airc.nist.gov/home)** — Official NIST source for risk-management resources and supporting materials.
- **[Weights & Biases Incident Retrospectives](https://wandb.ai/site/articles)** — Practitioner incident and operations retrospectives.

---

## Model Cards & Documentation

- **[Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993)** — Foundational paper introducing model cards as a transparency mechanism.
- **[Hugging Face Model Cards](https://huggingface.co/docs/hub/model-cards)** — Standardized model-card format and documentation.
- **[Datasheets for Datasets](https://arxiv.org/abs/1803.09010)** — Framework for documenting dataset provenance, composition, and intended use.

---

## Academic Papers

- **[Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565)** — Foundational paper on practical AI safety problems.
- **[Stochastic Parrots](https://dl.acm.org/doi/10.1145/3442188.3445922)** — Influential paper on risks of large language models.
- **[Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993)** — Introduced model cards as a documentation standard.
- **[The Alignment Problem](https://arxiv.org/abs/2009.01148)** — Survey of specification gaming in AI systems.
- **[Trustworthy AI](https://www.ibm.com/watson/assets/duo/pdf/Trustworthy_AI.pdf)** — Practical guide to trustworthy machine-learning systems.
- **[Governing AI for Humanity](https://www.un.org/sites/un2.un.org/files/governing_ai_for_humanity_final_report_en.pdf)** — UN report on global AI governance.

---

## Datasets & Benchmarks

- **[BIG-bench](https://github.com/google/BIG-bench)** ![GitHub stars](https://img.shields.io/github/stars/google/BIG-bench?style=social) — Collaborative benchmark for large-language-model evaluation.
- **[TruthfulQA](https://github.com/sylinrl/TruthfulQA)** — Benchmark for truthfulness in language-model outputs.
- **[HarmBench](https://github.com/centerforaisafety/HarmBench)** — Standardized evaluation framework for automated red teaming.
- **[MMLU](https://github.com/hendrycks/test)** — Multitask benchmark across 57 subjects.

---

## Communities & Organizations

- **[Partnership on AI](https://partnershiponai.org/)** — Multi-stakeholder organization advancing responsible-AI practice.
- **[MLCommons](https://mlcommons.org/)** — Engineering consortium for ML benchmarks and safety evaluation.
- **[Montreal AI Ethics Institute](https://montrealethics.ai/)** — AI ethics research and practitioner community.
- **[Center for AI Safety](https://www.safe.ai/)** — Research organization focused on societal AI risk.
- **[FINOS](https://www.finos.org/ai-readiness)** — AI-readiness resources for financial services.
- **[NIST National AI Initiative](https://www.nist.gov/artificial-intelligence)** — U.S. AI standards and research coordination.
- **[Future of Life Institute](https://futureoflife.org/cause-area/artificial-intelligence/)** — Research on catastrophic and long-term AI risks.

---

## Courses & Learning

- **[Responsible AI practices](https://ai.google/responsibility/responsible-ai-practices/)** — Google’s practical responsible-AI guidance.
- **[AI Ethics](https://ethics.fast.ai/)** — Free course on AI and data ethics.
- **[Trustworthy AI](https://www.ibm.com/training/badge/trustworthy-ai-foundations)** — IBM trustworthy-AI learning resource.
- **[NIST AI RMF Core](https://airc.nist.gov/home)** — Official NIST entry point for learning and implementation resources.
- **[Human-Centered AI](https://hai.stanford.edu/education)** — Stanford HAI educational resources.

---

## My Open-Source Frameworks

Frameworks I have built for AI governance and release readiness in regulated industries:

| Repository | Description | Stars |
|---|---|---|
| [governance-playbook](https://github.com/simaba/governance-playbook) | End-to-end AI governance playbook with practitioner NIST AI RMF mapping | ![stars](https://img.shields.io/github/stars/simaba/governance-playbook?style=social) |
| [release-checklist](https://github.com/simaba/release-checklist) | Risk-tiered release gate checklist for AI/ML deployments with a CLI validator | ![stars](https://img.shields.io/github/stars/simaba/release-checklist?style=social) |
| [nist-rmf-guide](https://github.com/simaba/nist-rmf-guide) | Practitioner guide to implementing NIST AI RMF | ![stars](https://img.shields.io/github/stars/simaba/nist-rmf-guide?style=social) |
| [release-governance](https://github.com/simaba/release-governance) | Release lifecycle framework with governance gates | ![stars](https://img.shields.io/github/stars/simaba/release-governance?style=social) |
| [accountability-patterns](https://github.com/simaba/accountability-patterns) | Design patterns for human accountability in AI systems | ![stars](https://img.shields.io/github/stars/simaba/accountability-patterns?style=social) |
| [regulated-ai](https://github.com/simaba/regulated-ai) | Starter kit for governance and release-readiness structure | ![stars](https://img.shields.io/github/stars/simaba/regulated-ai?style=social) |
| [multi-agent-governance](https://github.com/simaba/multi-agent-governance) | Governance framework for multi-agent AI systems | ![stars](https://img.shields.io/github/stars/simaba/multi-agent-governance?style=social) |
| [agent-eval](https://github.com/simaba/agent-eval) | Framework for evaluating AI-agent performance, safety, and reliability | ![stars](https://img.shields.io/github/stars/simaba/agent-eval?style=social) |

---

## Contributing

Contributions are welcome. Read the [Contributing Guidelines](CONTRIBUTING.md) and open an issue before submitting a PR.

When adding a resource:

1. Read the [Curation Policy](CURATION.md).
2. Verify the source is public, accessible, and maintained.
3. Add a specific one-line description.
4. Use a GitHub stars badge only for GitHub projects.
5. Update [`REVIEW_STATUS.md`](REVIEW_STATUS.md) when a section receives a substantive manual review.

---

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, Sima Bagheri has waived all copyright and related or neighboring rights to this work.