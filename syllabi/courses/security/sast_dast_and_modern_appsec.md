---
tags:
  - concepts:security
  - concepts:testing
  - concepts:best-practices
  - concepts:operations
  - concepts:developer-experience
level: intermediate
category: security
duration_hours: 40
audience:
  - audiences:security-engineers
  - audiences:developers
  - audiences:senior-developers
  - audiences:devops
  - audiences:architects
---
<!-- course: sast_dast_and_modern_appsec -->
# `SAST`, `DAST` and Modern AppSec

## Description
The `OWASP` course in the catalog covers the vulnerability classes; this course covers the engineering
discipline of finding them at scale. Modern application security is a tooling and workflow problem more than
a knowledge problem. Most organizations buy `SAST`, `DAST`, `SCA` and secrets-scanning tools, integrate them
shallowly, drown in noise, and end up worse off than before they started.

This five day course covers the modern AppSec pipeline as an engineering discipline. It covers the families
of automated security testing (`SAST`, `DAST`, IAST, `SCA`, secrets, container scanning, `IaC` scanning),
the integration into developer workflows, the false-positive economics that determine whether a program
succeeds or fails, the prioritization story (reachability, exploitability, asset value), the tooling
landscape (`Snyk`, `Semgrep`, Checkmarx, Veracode, Sonatype, `GitHub Advanced Security`, `GitLab Ultimate`),
and the program-level practices that `make` AppSec a developer-friendly discipline rather than a security-team
gatekeeping function. Participants leave able to design, run, and tune an AppSec program without burning out
the developers it is supposed to help.

## Duration
40 hours / 5 days

## Intended Audience
* security engineers responsible for application security tooling
* `DevOps` and platform engineers integrating security into CI/`CD`
* developers leading a team's AppSec story
* architects evaluating AppSec tooling
* engineers responding to an AppSec audit finding

## Prerequisites
* working knowledge of at least one mainstream programming language
* basic familiarity with `CI`/`CD` and pull-request workflows
* exposure to the `OWASP Top 10` material is helpful

## Objectives
* describe the families of automated security testing and pick the right one
* integrate AppSec scanning into developer workflows without grinding them to a halt
* manage the false-positive economics of an AppSec program
* prioritize findings by reachability and exploitability
* operate the major AppSec tooling effectively
* build a developer-friendly AppSec program with appropriate metrics

## Outline
<!-- chapter: the-modern-appsec-landscape, duration: 2h -->
* The modern AppSec landscape
    * AppSec as a tooling and workflow problem
    * the gap between vulnerability knowledge and program effectiveness
    * the developer-team-vs-security-team dynamic
    * the shift-left, shift-right, shift-everywhere debate
    * what good looks like
<!-- chapter: sast-static-application-security-testing, duration: 3h -->
* `SAST`: static application security testing
    * what `SAST` actually does
    * pattern matching vs taint analysis vs symbolic execution
    * the false-positive economics of `SAST`
    * `Semgrep`, `CodeQL`, `Snyk Code`, Checkmarx, Veracode, `SonarQube`
    * custom rules and the team-specific ruleset
    * `SAST` in the IDE vs `SAST` in `CI`
<!-- chapter: dast-dynamic-application-security-testing, duration: 3h -->
* `DAST`: dynamic application security testing
    * what `DAST` actually does
    * authenticated scanning and its complications
    * `OWASP ZAP`, `Burp Suite`, Nuclei, Acunetix, `Detectify`
    * `DAST` in CI vs `DAST` against staging
    * the `API`-aware `DAST` evolution
    * `DAST` and modern `SPAs`
<!-- chapter: iast-and-rasp, duration: 2h -->
* `IAST` and `RASP`
    * interactive application security testing
    * runtime application self-protection
    * the agent-based model
    * the cases where `IAST` actually pays off
    * `Contrast`, `HCL AppScan`, others
    * the `RASP` debate
<!-- chapter: sca-and-dependency-scanning, duration: 3h -->
* `SCA` and dependency scanning
    * the `Log4Shell` lesson
    * the `SBOM` requirement
    * direct vs transitive dependencies
    * `Snyk`, Sonatype, Mend, `Dependabot`, Renovate, `OSV-Scanner`, `Trivy`
    * vulnerability databases: `NVD`, OSV, `GHSA`
    * cross-reference to the existing Supply Chain Security course
    * version-pinning and patch policy
<!-- chapter: secrets-scanning, duration: 2h -->
* Secrets scanning
    * cross-reference to the Secrets Management course's secret-scanning chapter
    * pre-commit, push-protection, `CI`, retroactive
    * `gitleaks`, trufflehog, `detect-secrets`, GitGuardian, `GitHub` push protection
    * triaging detection alerts
    * the "rotate first, investigate after" rule
<!-- chapter: container-and-image-scanning, duration: 2h -->
* Container and image scanning
    * `OS`-package vulnerabilities vs application vulnerabilities
    * `Trivy`, `Grype`, `Clair`, `Snyk Container`, `Anchore`
    * registry-side scanning
    * runtime image attestation
    * the base-image upgrade story
<!-- chapter: iac-scanning, duration: 2h -->
* `IaC` scanning
    * cross-reference to the Cloud Misconfiguration and `CSPM` course
    * `Checkov`, tfsec, KICS, Terrascan, `Snyk IaC`
    * `OPA`/`Conftest` for custom policy
    * `IaC` scanning in `PR` vs in pipeline
    * the false-positive economics in `IaC` scanning
<!-- chapter: false-positives-the-economics, duration: 3h -->
* False positives: the economics
    * the cost of one false positive in developer minutes
    * the false-positive budget per detection
    * the noise-induced bypass: developers stop looking
    * tuning at the rule, repo, and project layers
    * suppression and exception workflows
    * the recurring-false-positive metric
<!-- chapter: prioritization-reachability-and-exploitability, duration: 3h -->
* Prioritization: reachability and exploitability
    * `CVSS` and its limitations
    * `EPSS` (exploit prediction scoring system)
    * `KEV` (known exploited vulnerabilities) catalog
    * reachability analysis
    * the "internet-exposed plus privileged" combination revisited
    * triage queues and ownership routing
<!-- chapter: integrating-into-developer-workflow, duration: 3h -->
* Integrating into developer workflow
    * the `IDE`, `pre-commit`, `PR`, pipeline, scheduled-scan layers
    * blocking vs warning gates
    * the "fix in this `PR`" vs "create a ticket" decision
    * triage `SLA`s and review queues
    * giving developers ownership of their findings
    * cross-reference to the Code Review course
<!-- chapter: github-advanced-security-and-platform-tools, duration: 2h -->
* `GitHub Advanced Security` and platform tools
    * `CodeQL` and `GitHub Advanced Security`
    * `GitLab Ultimate` security pipelines
    * `Bitbucket` and `Azure DevOps` equivalents
    * the cost story of platform-bundled AppSec
    * choosing platform tools vs best-of-breed
<!-- chapter: vulnerability-management-program, duration: 3h -->
* Vulnerability management program
    * inventory: applications, services, repos, ownership
    * the queue: triage, ownership, deadline
    * `SLAs` by severity
    * the patch deadline model
    * `risk acceptance` and the exception process
    * the executive dashboard for AppSec
<!-- chapter: bug-bounty-and-responsible-disclosure, duration: 2h -->
* Bug bounty and responsible disclosure
    * `HackerOne`, Bugcrowd, `Intigriti`, self-hosted
    * scope and rules of engagement
    * triage workflow for inbound reports
    * the public `security.txt` file
    * working with researchers
    * cross-reference to the `Web3` and Blockchain Security course's bounty chapter
<!-- chapter: appsec-and-llm-and-genai-applications, duration: 2h -->
* AppSec and `LLM` and GenAI applications
    * the `OWASP Top 10` for `LLMs`
    * prompt injection from the AppSec lens
    * cross-reference to the `AI` Safety and Alignment course
    * dependency security for `AI`-driven code
    * the `AI`-generated-code review angle
<!-- chapter: program-metrics-and-maturity, duration: 2h -->
* Program metrics and maturity
    * coverage metrics
    * mean time to remediate
    * recurrence rate by category
    * developer satisfaction with AppSec
    * the `BSIMM` and `OpenSAMM` maturity models
    * cross-reference to the Engineering Metrics and `DORA` course
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * audit a sample team's AppSec pipeline
    * triage a real `SAST`/`DAST` finding queue
    * recommended reading: `OWASP` cheat sheets, `BSIMM`, `OpenSAMM`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
