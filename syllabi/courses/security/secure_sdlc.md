---
tags:
  - security:security
  - practices:methodology
  - concepts:best-practices
level: intermediate
category: security
duration_hours: 16
audience:
  - audiences:developers
  - audiences:security-professionals
  - audiences:managers
  - audiences:devops
---
<!-- course: secure_sdlc -->
# Secure `SDLC`

## Description
The Secure Software Development Lifecycle (Secure `SDLC`) integrates security practices into every phase of software development. This course covers security requirements gathering, threat modeling in design, secure coding guidelines, static and dynamic analysis, software composition analysis, secrets scanning, penetration testing, and `DevSecOps` practices. Participants will also learn about vulnerability management, security champions programs, compliance frameworks, and maturity models.

## Duration
16 hours / 2 days

## Intended Audience
* Software developers building secure applications
* Security engineers and application security professionals
* Engineering managers leading development teams
* `DevOps` and `DevSecOps` engineers
* Quality assurance engineers
* Technical leaders defining development processes

## Prerequisites
* Experience with software development in at least one programming language
* Basic understanding of software development lifecycle models (`Agile`, Waterfall)
* Familiarity with version control (`Git`) and `CI/CD` concepts
* Basic knowledge of common security vulnerabilities (`OWASP Top 10`)
* Understanding of web application architecture

## Objectives
* Integrate security into every phase of the software development lifecycle
* Gather and define security requirements alongside functional requirements
* Apply threat modeling during the design phase
* Follow secure coding guidelines from `OWASP` and CERT
* Use `SAST`, `DAST`, and `SCA` tools effectively in development workflows
* Implement secrets scanning and security code review processes
* Build `DevSecOps` pipelines with automated security testing
* Establish a vulnerability management program
* Launch and maintain a security champions program
* Understand compliance frameworks (`PCI`-DSS, SOC2, `ISO 27001`) and maturity models (BSIMM, `OWASP SAMM`)

## Outline
<!-- chapter: secure-sdlc-overview, duration: 1h -->
* Secure `SDLC` Overview
    * Traditional `SDLC` vs Secure `SDLC`
    * Security as a shared responsibility
    * Cost of fixing vulnerabilities at each phase
    * Secure `SDLC` frameworks and models
    * Building a security culture in development teams
<!-- chapter: security-requirements-gathering, duration: 1h -->
* Security Requirements Gathering
    * Identifying security requirements from business needs
    * Abuse cases and misuse cases
    * Security user stories and acceptance criteria
    * Regulatory and compliance requirements
    * Security requirements traceability
    * Prioritizing security requirements
<!-- chapter: threat-modeling-in-design, duration: 1h -->
* Threat Modeling in Design
    * `When` and how to perform threat modeling
    * Data flow diagrams and trust boundaries
    * STRIDE methodology for threat identification
    * Risk rating and prioritization
    * Documenting and tracking threats
    * Lightweight threat modeling for `agile` teams
<!-- chapter: secure-coding-guidelines, duration: 1h -->
* Secure Coding Guidelines
    * `OWASP` secure coding practices
    * CERT secure coding standards
    * Input validation and output encoding
    * Authentication and session management best practices
    * Error handling and logging guidelines
    * Cryptographic best practices
    * Language-specific secure coding patterns
<!-- chapter: static-application-security-testing-sast, duration: 1h -->
* Static Application Security Testing (`SAST`)
    * How `SAST` tools work (abstract syntax tree analysis, data flow analysis)
    * Popular `SAST` tools (`SonarQube`, `Semgrep`, Checkmarx, `CodeQL`)
    * Integrating `SAST` into IDE and `CI/CD` pipelines
    * Tuning rules and managing false positives
    * Interpreting and triaging `SAST` results
<!-- chapter: dynamic-application-security-testing-dast, duration: 1h -->
* Dynamic Application Security Testing (`DAST`)
    * How `DAST` tools work (black-box scanning)
    * Popular `DAST` tools (`OWASP ZAP`, `Burp Suite`, Nuclei)
    * Configuring scan profiles and authentication
    * Integrating `DAST` into `CI/CD` pipelines
    * Interpreting and triaging `DAST` results
    * Interactive Application Security Testing (IAST) overview
<!-- chapter: software-composition-analysis-sca, duration: 1h -->
* Software Composition Analysis (`SCA`)
    * Open-source risk and supply chain security
    * Popular `SCA` tools (Snyk, `Dependabot`, Renovate, `OWASP Dependency-Check`)
    * Vulnerability databases (CVE, NVD, OSV)
    * License compliance checking
    * `SBOM` (Software Bill of Materials) generation and management
    * Dependency update strategies
<!-- chapter: secrets-scanning, duration: 1h -->
* Secrets Scanning
    * Common secret exposure patterns
    * Secrets scanning tools (GitLeaks, TruffleHog, detect-secrets)
    * Pre-commit hooks for secret prevention
    * Integrating secrets scanning into `CI/CD`
    * Remediating exposed secrets
    * Secrets management solutions (`HashiCorp Vault`, `cloud KMS`)
<!-- chapter: security-code-review, duration: 1h -->
* Security Code Review
    * Security-focused code review checklist
    * Manual code review techniques for security
    * Combining manual review with automated tools
    * Review prioritization and risk-based approach
    * Training developers on security code review
<!-- chapter: penetration-testing, duration: 1h -->
* Penetration Testing
    * Types of penetration testing (black-box, gray-box, white-box)
    * Penetration testing methodology and phases
    * Scope definition and rules of engagement
    * Interpreting penetration test reports
    * Remediation tracking and retesting
    * Bug bounty programs as a complement
<!-- chapter: security-testing-in-ci-cd, duration: 1h -->
* Security Testing in `CI/CD`
    * Building a security testing pipeline
    * Gate criteria and quality gates for security
    * Orchestrating `SAST`, `DAST`, `SCA`, and secrets scanning
    * Balancing speed and security in `CI/CD`
    * Notification and escalation workflows
    * Security dashboard and reporting
<!-- chapter: devsecops-practices, duration: 1h -->
* `DevSecOps` Practices
    * `DevSecOps` principles and culture
    * Infrastructure as code security scanning
    * Container image scanning and hardening
    * `Kubernetes` security policies
    * Cloud security posture management
    * Shift-left and shift-right security approaches
<!-- chapter: vulnerability-management, duration: 1h -->
* Vulnerability Management
    * Vulnerability lifecycle (discovery, triage, remediation, verification)
    * Severity scoring with CVSS
    * Vulnerability tracking and SLA management
    * Risk acceptance and exception processes
    * Vulnerability metrics and reporting
    * Coordinated vulnerability disclosure
<!-- chapter: security-champions-program, duration: 1h -->
* Security Champions Program
    * What is a security champions program
    * Identifying and recruiting security champions
    * Training and empowering champions
    * Champion responsibilities and activities
    * Measuring program effectiveness
    * Sustaining the program over time
<!-- chapter: compliance-frameworks, duration: 1h -->
* Compliance Frameworks
    * `PCI`-DSS requirements for secure development
    * SOC2 trust service criteria and development controls
    * `ISO 27001` Annex A controls for development
    * Mapping secure `SDLC` practices to compliance requirements
    * Audit preparation and evidence collection
<!-- chapter: maturity-models, duration: 1h -->
* Maturity Models
    * BSIMM (Building Security In Maturity Model) framework
    * `OWASP SAMM` (Software Assurance Maturity Model)
    * Assessing current maturity level
    * Building a roadmap for improvement
    * Benchmarking against industry peers

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
