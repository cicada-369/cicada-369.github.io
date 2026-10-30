---
title: "OWASP Top 10 directory"
description: "A directory of OWASP Top 10 projects verified as of October 27, 2026."
layout: page
permalink: /atlas/owasp-top-10-all/
---

Here is a **GitHub** directory of OWASP Top 10 projects I could verify as of October 27, 2026. I’m listing the projects themselves—not the ten individual risks within each project.

OWASP’s Top 10 family includes separate lists for web applications, APIs, mobile, AI, infrastructure, and other domains. Not every project has a finalized, year-numbered release; some are drafts or historical repositories. [owasp](https://owasp.org/www-project-developer-guide/assets/exports/OWASP_Developer_Guide.pdf)

## Application security and secure development

| Project | GitHub repository | Latest edition or status verified |
|---|---|---|
| OWASP Top 10 — Web Application Security Risks | [OWASP/Top10](https://github.com/OWASP/Top10) | 2025 final; supersedes 2021.  [github](https://github.com/owasp/top10) |
| API Security Top 10 | [OWASP/API-Security](https://github.com/OWASP/API-Security) | 2023 edition located.  [github](https://github.com/OWASP/API-Security/blob/master/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows.md?ref=blog.hackingclub.com) |
| Mobile Top 10 | [OWASP/www-project-mobile-top-10](https://github.com/OWASP/www-project-mobile-top-10) | 2024 final.  [github](https://github.com/OWASP/www-project-mobile-top-10/releases) |
| Desktop App Security Top 10 | [OWASP/www-project-desktop-app-security-top-10](https://github.com/OWASP/www-project-desktop-app-security-top-10) | 2021 edition.  [github](https://github.com/OWASP/www-project-desktop-app-security-top-10) |
| Top 10 Proactive Controls | [OWASP/www-project-proactive-controls](https://github.com/OWASP/www-project-proactive-controls) | 2024 tagged release verified; repository also contains current working content. This is a controls list rather than a vulnerability ranking.  [github](https://github.com/OWASP/www-project-proactive-controls/releases) |
| Top 10 for Business Logic Abuse | [OWASP/www-project-top-10-for-business-logic-abuse](https://github.com/OWASP/www-project-top-10-for-business-logic-abuse) | Repository and risk documentation available; final edition year not verified.  [github](https://github.com/owasp/www-project-top-10-for-business-logic-abuse) |
| Low-Code/No-Code Top 10 / Citizen Development Top 10 Security Risks | [OWASP/www-project-citizen-development-top10-security-risks](https://github.com/OWASP/www-project-citizen-development-top10-security-risks) | OWASP lists the Low-Code/No-Code project; its repository includes discussion of renaming it for citizen development. Treat these as one project lineage, not two independent lists.  [owasp](https://owasp.org/projects/low-codeno-code-top-10) |
| Smart Contract Top 10 | [OWASP/www-project-smart-contract-top-10](https://github.com/OWASP/www-project-smart-contract-top-10) | 2026 edition; its forward-looking ranking uses incidents and survey data from 2025.  [github](https://github.com/owasp/www-project-smart-contract-top-10) |

## AI, LLM, and agent security

| Project | GitHub repository | Latest edition or status verified |
|---|---|---|
| GenAI / LLM Top 10 | [GenAI-Security-Project/GenAI-LLM-Top10](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10) | 2026, published August 4, 2026. The previous OWASP repository explicitly redirects active development here.  [genai.owasp](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) |
| Machine Learning Security Top 10 | [OWASP/www-project-machine-learning-security-top-10](https://github.com/OWASP/www-project-machine-learning-security-top-10) | OWASP describes the current work as a frequently modified draft.  [owasp](https://owasp.org/projects/machine-learning-security-top-ten) |
| MCP Top 10 | [OWASP/www-project-mcp-top-10](https://github.com/OWASP/www-project-mcp-top-10) | Repository contains 2025-numbered risks; no packaged GitHub release was listed.  [github](https://github.com/OWASP/www-project-mcp-top-10) |
| Agentic Skills Top 10 | [OWASP/www-project-agentic-skills-top-10](https://github.com/OWASP/www-project-agentic-skills-top-10) | Available framework focused specifically on AI-agent skills and their tools-layer risks.  [github](https://github.com/OWASP/www-project-agentic-skills-top-10) |

There is also an OWASP Top 10 for Agentic Applications 2026, covering autonomous agents at the application/system level. I verified its official publication, but not a dedicated canonical GitHub repository for the Top 10 document itself, so I have not substituted an unofficial mirror in the table. It is distinct from the Agentic Skills Top 10. [github](https://github.com/OWASP/www-project-agentic-skills-top-10)

The older [OWASP LLM repository](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications) remains useful for historical editions and translations, but it is now a legacy entry point—not the current development repository. [github](https://github.com/owasp/www-project-top-10-for-large-language-model-applications)

## Cloud, DevSecOps, infrastructure, and IoT

| Project | GitHub repository | Latest edition or status verified |
|---|---|---|
| Top 10 CI/CD Security Risks | [OWASP/www-project-top-10-ci-cd-security-risks](https://github.com/OWASP/www-project-top-10-ci-cd-security-risks) | Published framework and risk documents available; a newer year-numbered edition was not verified.  [github](https://github.com/OWASP/www-project-top-10-ci-cd-security-risks) |
| Kubernetes Top Ten | [OWASP/www-project-kubernetes-top-ten](https://github.com/OWASP/www-project-kubernetes-top-ten) | 2025 risk list available in the repository.  [github](https://github.com/OWASP/www-project-kubernetes-top-ten) |
| Cloud-Native Application Security Top 10 | [OWASP/www-project-cloud-native-application-security-top-10](https://github.com/OWASP/www-project-cloud-native-application-security-top-10) | Interim / under-review material, including a 2022 content tree. The separate older source repository is archived.  [github](https://github.com/OWASP/www-project-cloud-native-application-security-top-10/blob/master/2022/en/src/0x05_insecure_secrets.md) |
| Top 10 Infrastructure Security Risks | [OWASP/www-project-top-10-infrastructure-security-risks](https://github.com/OWASP/www-project-top-10-infrastructure-security-risks) | Repository located; finalized edition/version not verified.  [github](https://github.com/OWASP/www-project-top-10-infrastructure-security-risks/issues/views) |
| IoT Top 10 | [OWASP/www-project-internet-of-things](https://github.com/OWASP/www-project-internet-of-things) | 2018 list remains available within the broader IoT project.  [github](https://github.com/OWASP/www-project-internet-of-things/blob/master/tab_seek_and_understand.md) |
| Subtractive Hardening / Subtractive Security Top 10 | [OWASP/OWASP-Subtractive-Hardening-Top-10](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10) | Repository provides attack-path-removal guidance and platform-specific Top 10 documents, including IoT.  [github](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10) |
| Top 10 Neocloud and AI Data Center Security Risks | [OWASP/OWASP-Top-10-Neocloud-and-AI-Data-Center-Security-Risks](https://github.com/OWASP/OWASP-Top-10-Neocloud-and-AI-Data-Center-Security-Risks) | Repository located; finalized edition/version not verified.  [github](https://github.com/OWASP/OWASP-Top-10-Neocloud-and-AI-Data-Center-Security-Risks/security) |

OWASP also maintains the Serverless Top 10 project. Its official page currently provides the Serverless Interpretation report and describes further work toward an official Serverless Top 10 report. I did not verify the canonical source-repository URL, so I’m not guessing one. [owasp](https://owasp.org/projects/serverless-top-10)

## Data, privacy, and industry-specific projects

| Project | GitHub repository | Latest edition or status verified |
|---|---|---|
| Data Security Top 10 | [OWASP/www-project-data-security-top-10](https://github.com/OWASP/www-project-data-security-top-10) | Repository available; finalized latest edition not verified.  [github](https://github.com/OWASP/www-project-data-security-top-10/commits) |
| Top 10 Privacy Risks | [OWASP/www-project-top-10-privacy-risks](https://github.com/OWASP/www-project-top-10-privacy-risks) | Version 2.0 / 2021. Repository archived March 15, 2025.  [github](https://github.com/OWASP/www-project-top-10-privacy-risks/blob/master/index.md) |
| Top 10 for Maritime Security | [OWASP/www-project-top-10-for-maritime-security](https://github.com/OWASP/www-project-top-10-for-maritime-security) | Development-stage initiative; repository describes the roadmap rather than establishing a verified final edition.  [github](https://github.com/OWASP/www-project-top-10-for-maritime-security) |

## Scope and completeness

This is a verified directory, not a guaranteed exhaustive count of every newly created OWASP repository. It separates released editions from working drafts, archived material, and repositories whose release status could not be confirmed. OWASP’s project inventory is broader and changes over time; a repository’s existence or recent commit date alone does not establish a new finalized Top 10 edition. [owasp](https://owasp.org/projects/machine-learning-security-top-ten)
