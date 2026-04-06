# Awesome AI Governance [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of frameworks, tools, regulations, papers, and resources for
> responsible and trustworthy AI deployment in regulated industries.

Maintained by [Sima Bagheri](https://github.com/simaba) · [LinkedIn](https://www.linkedin.com/in/simabagheri) · [Medium](https://medium.com/@simabagheri)

**Focus areas:** Enterprise AI governance · LLM deployment safety · Risk management · Regulatory compliance (NIST AI RMF, EU AI Act, ISO 42001) · Release readiness · Incident response

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
- **[NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)** — The U.S. government's voluntary framework for managing risks in the design, development, deployment, and use of AI systems. Organized around four functions: Govern, Map, Measure, Manage.
- **[NIST AI RMF Playbook](https://airc.nist.gov/Docs/2)** — Practical guidance for implementing the AI RMF, with suggested actions for each subcategory.
- **[Executive Order on Safe, Secure, and Trustworthy AI](https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/)** — U.S. Executive Order (Oct 2023) establishing new standards for AI safety and security.
- **[NIST AI Safety Institute (AISI)](https://www.nist.gov/artificial-intelligence/executive-order-safe-secure-and-trustworthy-artificial-intelligence)** — Federal body coordinating AI safety research and standards.
- **[OMB AI Governance Policy M-24-10](https://www.whitehouse.gov/wp-content/uploads/2024/03/M-24-10-Advancing-Governance-Innovation-and-Risk-Management-for-Agency-Use-of-Artificial-Intelligence.pdf)** — Governance and risk management requirements for federal agency AI use.

### European Union
- **[EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)** — The world's first comprehensive legal framework for AI, using a risk-based tiered approach (unacceptable, high, limited, minimal risk).
- **[EU AI Act Summary](https://artificialintelligenceact.eu/)** — Plain-language guide to the EU AI Act provisions and timelines.
- **[GDPR & AI](https://edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-032021-virtual-voice-assistants_en)** — European Data Protection Board guidance on AI and GDPR intersection.

### International Standards
- **[ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html)** — International standard for AI management systems. Provides requirements and guidance for establishing, implementing, maintaining, and improving an AI management system.
- **[ISO/IEC 23894:2023](https://www.iso.org/standard/77304.html)** — Guidance on risk management for AI systems.
- **[IEEE 7000 Series](https://standards.ieee.org/initiatives/artificial-intelligence-systems/standards/)** — IEEE standards for ethically aligned AI design.
- **[OECD AI Principles](https://oecd.ai/en/ai-principles)** — International principles on trustworthy AI adopted by 46 countries.

---

## Risk Management Frameworks

- **[NIST AI RMF Core](https://airc.nist.gov/home)** — Interactive version of the AI RMF with searchable categories and subcategories.
- **[Microsoft Responsible AI Standard](https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-Responsible-AI-Standard-v2-General-Requirements-3.pdf)** — Microsoft's internal responsible AI framework, publicly shared.
- **[Google PAIR Guidebook](https://pair.withgoogle.com/guidebook/)** — People + AI Research guidebook for designing human-centered AI.
- **[IBM AI Fairness 360](https://aif360.mybluemix.net/)** — Open-source toolkit for examining, reporting, and mitigating discrimination in ML models.
- **[MITRE ATLAS](https://atlas.mitre.org/)** — Adversarial Threat Landscape for AI Systems — knowledge base of AI-specific adversarial tactics.
- **[OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/)** — The 10 most critical security risks for LLM applications.

---

## Governance Tools & Platforms

- **[Microsoft Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox)** ![GitHub stars](https://img.shields.io/github/stars/microsoft/responsible-ai-toolbox?style=social) — Integrated suite for responsible AI assessment including error analysis, fairness, causal inference, and counterfactual analysis.
- **[Giskard](https://github.com/Giskard-AI/giskard)** ![GitHub stars](https://img.shields.io/github/stars/Giskard-AI/giskard?style=social) — Open-source AI quality testing platform for detecting biases, vulnerabilities, and performance issues.
- **[verifywise](https://github.com/verifywise/verifywise)** ![GitHub stars](https://img.shields.io/github/stars/verifywise/verifywise?style=social) — AI compliance platform with direct NIST AI RMF and EU AI Act mappings.
- **[Evidently AI](https://github.com/evidentlyai/evidently)** ![GitHub stars](https://img.shields.io/github/stars/evidentlyai/evidently?style=social) — Evaluate, test, and monitor ML and LLM models in production.
- **[WhyLabs](https://whylabs.ai/)** — AI observability platform for model monitoring and drift detection.
- **[Fiddler AI](https://www.fiddler.ai/)** — Explainable AI and model performance monitoring for enterprises.
- **[Microsoft PyRIT](https://github.com/Azure/PyRIT)** ![GitHub stars](https://img.shields.io/github/stars/Azure/PyRIT?style=social) — Python Risk Identification Toolkit for generative AI red teaming.
- **[LangFuse](https://github.com/langfuse/langfuse)** ![GitHub stars](https://img.shields.io/github/stars/langfuse/langfuse?style=social) — Open-source LLM observability and analytics.

---

## AI Testing & Evaluation

- **[Holistic Evaluation of Language Models (HELM)](https://crfm.stanford.edu/helm/)** — Stanford's comprehensive LLM evaluation framework across scenarios, metrics, and models.
- **[EleutherAI LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness)** ![GitHub stars](https://img.shields.io/github/stars/EleutherAI/lm-evaluation-harness?style=social) — Unified framework for evaluating language models across 200+ tasks.
- **[DeepEval](https://github.com/confident-ai/deepeval)** ![GitHub stars](https://img.shields.io/github/stars/confident-ai/deepeval?style=social) — LLM evaluation framework with metrics for RAG, hallucination, and safety.
- **[TruLens](https://github.com/truera/trulens)** ![GitHub stars](https://img.shields.io/github/stars/truera/trulens?style=social) — Evaluation and tracking for LLM-based applications.
- **[RAGAS](https://github.com/explodinggradients/ragas)** ![GitHub stars](https://img.shields.io/github/stars/explodinggradients/ragas?style=social) — Evaluation framework for Retrieval Augmented Generation pipelines.
- **[MLflow Model Evaluation](https://mlflow.org/docs/latest/model-evaluation/index.html)** — Built-in model evaluation with support for LLMs and custom metrics.

---

## Incident Management

- **[AI Incident Database](https://incidentdatabase.ai/)** — Crowdsourced database of AI incidents and failures across industries.
- **[AI Vulnerability Database (AVID)](https://avidml.org/)** — Taxonomy of AI failure modes, biases, and vulnerabilities.
- **[NIST AI Incident Tracking](https://airc.nist.gov/Docs/2)** — NIST guidance on AI incident classification and response.
- **[Weights & Biases Incident Retrospectives](https://wandb.ai/site/articles)** — Real-world ML incident retrospectives from practitioners.

---

## Model Cards & Documentation

- **[Model Cards for Model Reporting (Google)](https://arxiv.org/abs/1810.03993)** — Original paper introducing model cards as a transparency mechanism.
- **[Hugging Face Model Card Toolkit](https://huggingface.co/docs/hub/model-cards)** — Standardized model card format with template and auto-generation.
- **[Google Model Card Toolkit](https://github.com/google/model-card-toolkit)** — Python toolkit for generating model cards programmatically.
- **[Datasheets for Datasets](https://arxiv.org/abs/1803.09010)** — Framework for documenting datasets with provenance, composition, and intended use.

---

## Academic Papers

- **[Concrete Problems in AI Safety (Amodei et al., 2016)](https://arxiv.org/abs/1606.06565)** — Foundational paper defining five practical AI safety problems.
- **[Stochastic Parrots (Bender et al., 2021)](https://dl.acm.org/doi/10.1145/3442188.3445922)** — Seminal paper on risks of large language models.
- **[Model Cards for Model Reporting (Mitchell et al., 2019)](https://arxiv.org/abs/1810.03993)** — Introduced model cards as a documentation standard.
- **[The Alignment Problem (Krakovna et al., 2020)](https://arxiv.org/abs/2009.01148)** — Survey of specification gaming in AI systems.
- **[Trustworthy AI (Varshney, 2022)](https://www.ibm.com/watson/assets/duo/pdf/Trustworthy_AI.pdf)** — Practical guide to building trustworthy ML systems.
- **[Governing AI for Humanity (UN Advisory Body, 2024)](https://www.un.org/sites/un2.un.org/files/governing_ai_for_humanity_final_report_en.pdf)** — UN report on global AI governance frameworks.

---

## Datasets & Benchmarks

- **[BigBench](https://github.com/google/BIG-bench)** ![GitHub stars](https://img.shields.io/github/stars/google/BIG-bench?style=social) — Collaborative benchmark for large language model evaluation beyond current capabilities.
- **[TruthfulQA](https://github.com/sylinrl/TruthfulQA)** — Benchmark measuring whether LLMs generate truthful answers.
- **[HarmBench](https://github.com/centerforaisafety/HarmBench)** — Standardized evaluation framework for automated red teaming.
- **[MMLU](https://github.com/hendrycks/test)** — Massive Multitask Language Understanding benchmark across 57 subjects.

---

## Communities & Organizations

- **[Partnership on AI](https://partnershiponai.org/)** — Multi-stakeholder organization advancing responsible AI practices.
- **[MLCommons](https://mlcommons.org/)** — Open engineering consortium for ML benchmarks and safety evaluations.
- **[Montreal AI Ethics Institute (MAIEI)](https://montrealethics.ai/)** — Research institute for AI ethics with practitioner community.
- **[Center for AI Safety (CAIS)](https://www.safe.ai/)** — Research organization focused on reducing societal risks from AI.
- **[FINOS (Fintech Open Source Foundation)](https://www.finos.org/ai-readiness)** — AI readiness resources for financial services industry.
- **[NIST National AI Initiative](https://www.nist.gov/artificial-intelligence)** — U.S. government AI standards and research coordination.
- **[Future of Life Institute](https://futureoflife.org/cause-area/artificial-intelligence/)** — Research on existential and catastrophic AI risks.

---

## Courses & Learning

- **[Responsible AI practices (Google)](https://ai.google/responsibility/responsible-ai-practices/)** — Google's practical guidance on responsible AI development.
- **[AI Ethics (fast.ai)](https://ethics.fast.ai/)** — Free course on AI ethics and data ethics.
- **[Trustworthy AI (IBM)](https://www.ibm.com/training/badge/trustworthy-ai-foundations)** — IBM's trustworthy AI foundations certification.
- **[NIST AI RMF Workshop Videos](https://www.nist.gov/artificial-intelligence/ai-risk-management-framework)** — Free workshop recordings on implementing the AI RMF.
- **[Human-Centered AI (Stanford HAI)](https://hai.stanford.edu/education)** — Stanford's human-centered AI educational resources.

---

## My Open-Source Frameworks

Frameworks I have built for AI governance and release readiness in regulated industries:

| Repository | Description | Stars |
|---|---|---|
| [enterprise-ai-governance-playbook](https://github.com/simaba/enterprise-ai-governance-playbook) | End-to-end AI governance playbook aligned with NIST AI RMF | ![stars](https://img.shields.io/github/stars/simaba/enterprise-ai-governance-playbook?style=social) |
| [ai-release-readiness-checklist](https://github.com/simaba/ai-release-readiness-checklist) | YAML-based release gate checklist for LLM/ML deployments | ![stars](https://img.shields.io/github/stars/simaba/ai-release-readiness-checklist?style=social) |
| [ai-risk-taxonomy](https://github.com/simaba/ai-risk-taxonomy) | Structured taxonomy of AI risks mapped to NIST AI RMF | ![stars](https://img.shields.io/github/stars/simaba/ai-risk-taxonomy?style=social) |
| [llm-governance-readiness-framework](https://github.com/simaba/llm-governance-readiness-framework) | LLM-specific governance maturity framework | ![stars](https://img.shields.io/github/stars/simaba/llm-governance-readiness-framework?style=social) |
| [regulated-ai-use-case-library](https://github.com/simaba/regulated-ai-use-case-library) | AI use cases with governance context for regulated industries | ![stars](https://img.shields.io/github/stars/simaba/regulated-ai-use-case-library?style=social) |
| [nist-ai-rmf-implementation-guide](https://github.com/simaba/nist-ai-rmf-implementation-guide) | Practitioner guide to implementing NIST AI RMF | ![stars](https://img.shields.io/github/stars/simaba/nist-ai-rmf-implementation-guide?style=social) |

---

## Contributing

Contributions are welcome! Please read the [Contributing Guidelines](CONTRIBUTING.md)
and open an issue before submitting a PR.

**How to add a resource:**
1. Verify the resource is publicly accessible and actively maintained
2. Add it to the appropriate section with a one-line description
3. For GitHub repos: add a stars badge using `![stars](https://img.shields.io/github/stars/owner/repo?style=social)`
4. Open a PR with the title `Add: [Resource Name]`

---

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, Sima Bagheri has waived all copyright and
related or neighboring rights to this work.
