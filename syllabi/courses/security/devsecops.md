---
tags:
  - security:devsecops
  - practices:devops
  - security:sast
  - security:dast
  - practices:shift-left
level: intermediate
category: security
duration_hours: 24
audience:
  - audiences:developers
  - audiences:devops
  - audiences:security-engineers
---
<!-- course: devsecops -->
# `DevSecOps`

## Description
`DevSecOps` integrates security practices directly into the software development lifecycle, shifting responsibility for security left toward developers and making it a shared, continuous concern across engineering teams. This course teaches the principles, tooling, and cultural changes needed to embed security gates, automated scanning, and threat awareness into modern `CI/CD` pipelines. Participants will gain hands-on experience with industry-standard tools including `Semgrep`, `SonarQube`, `CodeQL`, `OWASP ZAP`, `Trivy`, and secrets management systems, learning how to identify and remediate vulnerabilities early without slowing down delivery. By the end of this course, attendees will be equipped to build and operate a mature `DevSecOps` program that reduces risk while maintaining engineering velocity.

## Duration
24 hours / 3 days

## Intended Audience
* Software developers wanting to take ownership of application security
* `DevOps` and platform engineers responsible for `CI/CD` pipeline design
* Security engineers embedding security into engineering workflows
* Development leads and architects designing secure-by-default systems

## Prerequisites
* Proficiency in at least one programming language (`Python`, `Java`, Go, `JavaScript`, or similar)
* Hands-on experience with `CI/CD` tools such as `GitHub Actions`, `GitLab CI`, or `Jenkins`
* Familiarity with `Docker` and container-based deployments
* Basic understanding of common web vulnerabilities (`OWASP Top 10`)
* Working knowledge of `Git` and version-control workflows
* Basic `Linux` command-line skills

## Objectives
* Articulate the `DevSecOps` philosophy and the cultural shift required for shift-left security
* Apply threat modeling techniques during design and sprint planning phases
* Configure and integrate `SAST` tools (`Semgrep`, `SonarQube`, `CodeQL`) into `CI/CD` pipelines
* Deploy `DAST` tools (`OWASP ZAP`, `Burp Suite`) for automated security testing in pipelines
* Implement Software Composition Analysis (`SCA`) to manage third-party dependency risk
* Prevent secrets leakage using scanning tools and centralized secrets management (`HashiCorp Vault`, `AWS Secrets Manager`)
* Scan container images for vulnerabilities with `Trivy`, `Grype`, and registry-level policies
* Define and enforce security quality gates that block insecure code from progressing to production
* Establish security metrics and reporting dashboards for continuous improvement
* Build an organizational `DevSecOps` program with defined roles, processes, and tooling

## Outline
<!-- chapter: introduction-to-devsecops, duration: 2h -->
* Introduction to `DevSecOps`
    * The evolution from `DevOps` to `DevSecOps`
    * Why traditional security processes fail in `agile` and cloud-native environments
    * Security as a shared responsibility: developers, operations, and security teams
    * The cost of finding vulnerabilities late in the `SDLC`
    * Overview of the `DevSecOps` toolchain landscape
    * Key principles: automation, visibility, feedback loops, and continuous improvement
    * Real-world `DevSecOps` transformation case studies

<!-- chapter: shift-left-security-principles, duration: 2h -->
* Shift-Left Security Principles
    * Defining "shift-left" and its impact on vulnerability remediation cost
    * Secure coding standards and developer security training
    * Security requirements gathering during sprint planning
    * Pre-commit hooks and `IDE` security plugins
    * Security-focused code review checklists
    * Building a security champions program within engineering teams
    * Measuring shift-left maturity and developer security adoption

<!-- chapter: threat-modeling-in-the-sdlc, duration: 2h -->
* Threat Modeling in the `SDLC`
    * What is threat modeling and why it matters at design time
    * STRIDE methodology: Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation
    * PASTA and attack tree methodologies
    * Data Flow Diagrams (`DFD`) as the foundation for threat analysis
    * Identifying trust boundaries and attack surfaces
    * Threat modeling tools: `OWASP Threat Dragon`, `Microsoft Threat Modeling Tool`
    * Integrating threat model outputs into backlog and acceptance criteria

<!-- chapter: sast-tools-semgrep-sonarqube-codeql, duration: 3h -->
* `SAST` Tools — `Semgrep`, `SonarQube`, `CodeQL`
    * How Static Application Security Testing (`SAST`) works and its limitations
    * Writing and customizing `Semgrep` rules for language-specific vulnerability patterns
    * Configuring `SonarQube` quality gates and security hotspot review workflows
    * `CodeQL` query language: writing custom security queries for `GitHub Advanced Security`
    * Tuning `SAST` tools to minimize false positives while maximizing signal
    * Integrating `SAST` scan results into pull request workflows and developer feedback loops
    * Comparing and combining multiple `SAST` tools for comprehensive coverage

<!-- chapter: dast-tools-owasp-zap-burp-suite-in-pipelines, duration: 2h -->
* `DAST` Tools — `OWASP ZAP`, `Burp Suite` in Pipelines
    * How Dynamic Application Security Testing (`DAST`) complements `SAST`
    * `OWASP ZAP` baseline scan and full scan modes for automated pipelines
    * `Burp Suite Enterprise Edition` for automated crawling and scanning
    * `API` security scanning with `OWASP ZAP` against `OpenAPI` specifications
    * Authenticated scanning: managing session tokens and login flows in `DAST`
    * Interpreting `DAST` scan reports and triaging findings
    * Deploying staging environments for safe automated `DAST` testing

<!-- chapter: software-composition-analysis, duration: 2h -->
* Software Composition Analysis (`SCA`)
    * The open-source dependency risk landscape (`Log4Shell`, `event-stream`, `XZ Utils`)
    * How `SCA` tools detect vulnerable and malicious dependencies
    * Tools: `Dependabot`, `Snyk`, `OWASP Dependency-Check`, Renovate
    * License compliance scanning alongside vulnerability detection
    * Establishing dependency update policies and automated PR workflows
    * Responding to zero-day vulnerabilities in production dependencies
    * Combining `SCA` with `SBOM` generation for supply chain visibility

<!-- chapter: secrets-management-in-ci-cd, duration: 2h -->
* Secrets Management in `CI/CD`
    * The problem of secrets sprawl: hardcoded credentials, leaked `.env` files
    * Scanning for secrets with `truffleHog`, gitleaks, and `git-secrets`
    * Pre-commit and pre-push hooks for secrets detection
    * `HashiCorp Vault`: dynamic secrets, secret leasing, and `CI/CD` integration
    * Cloud-native secrets stores: `AWS Secrets Manager`, `Azure Key Vault`, `GCP Secret Manager`
    * `CI/CD` platform secret management best practices (`GitHub Actions`, `GitLab CI`)
    * Secrets rotation strategies and emergency revocation procedures

<!-- chapter: container-and-image-scanning, duration: 2h -->
* Container and Image Scanning
    * Container image attack surface: base images, installed packages, application layers
    * Vulnerability scanning with `Trivy`, `Grype`, and `Clair`
    * Scanning images at build time, registry ingestion, and runtime
    * `Dockerfile` best practices: minimal base images, non-root users, multi-stage builds
    * Image signing and attestation with `Cosign` and `Notary v2`
    * Registry policy enforcement with Harbor and cloud registry security features
    * Runtime container security monitoring with `Falco`

<!-- chapter: security-gates-in-ci-cd-pipelines, duration: 3h -->
* Security Gates in `CI/CD` Pipelines
    * Designing pipeline security stages: build, test, scan, deploy, monitor
    * Defining pass/fail thresholds for vulnerability severity (`CVSS` scoring)
    * Implementing break-the-build policies for critical and high findings
    * Managing exceptions and risk acceptance workflows
    * Integrating security tool output into unified dashboards (`Defect Dojo`, `Jira`)
    * Pipeline as code security: protecting `CI/CD` configuration files
    * Practical pipeline design workshop: building an end-to-end secure pipeline

<!-- chapter: security-metrics-and-reporting, duration: 2h -->
* Security Metrics and Reporting
    * Defining meaningful `DevSecOps` metrics: MTTR, vulnerability density, escape rate
    * Tracking mean time to remediate (`MTTR`) by severity and team
    * Building security dashboards for engineering teams and leadership
    * Vulnerability aging and SLA enforcement
    * Integrating findings into engineering planning and OKRs
    * Communicating security risk in business terms
    * Using `DORA` metrics in conjunction with security metrics

<!-- chapter: building-a-devsecops-program, duration: 2h -->
* Building a `DevSecOps` Program
    * Assessing current state: security maturity models (`BSIMM`, `OWASP SAMM`)
    * Defining roles and responsibilities across development, operations, and security
    * Toolchain selection and total cost of ownership considerations
    * Scaling `DevSecOps` across multiple teams and technology stacks
    * Governance: policies, standards, and exception management processes
    * Building developer security enablement: training, documentation, and feedback
    * Roadmap planning and executive sponsorship for `DevSecOps` transformation

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
