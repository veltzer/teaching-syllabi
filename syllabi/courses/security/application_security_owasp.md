---
tags:
  - security:security
  - security:owasp
  - security:application-security
  - security:sast
  - security:dast
  - security:secure-sdlc
level: intermediate
category: security
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
  - audiences:architects
  - audiences:managers
  - audiences:security-professionals
---
<!-- course: application_security_owasp -->
# Application Security (`OWASP`)

## Description
Application security is essential for building resilient software that withstands modern attack vectors. This course provides a comprehensive understanding of the `OWASP Top 10` vulnerabilities, threat modeling methodologies, static and dynamic application security testing, secrets management, secure software development lifecycle practices, and dependency scanning. Participants will learn how to integrate security into every phase of the development process.

## Duration
16 hours / 2 days

## Intended Audience
* Software developers and engineers
* `DevOps` and `DevSecOps` engineers
* Security engineers and architects
* Technical leads and team managers
* Quality assurance engineers
* Anyone responsible for application security in their organization

## Prerequisites
* `Solid` experience with at least one programming language
* Understanding of web application architecture and `REST APIs`
* Familiarity with `HTTP`/`HTTPS` protocols
* Basic knowledge of version control systems (`Git`)
* Understanding of `CI/CD` pipeline concepts
* Basic command-line interface usage

## Objectives
* Identify and mitigate all `OWASP Top 10` vulnerabilities in real-world applications
* Apply threat modeling techniques such as `STRIDE` and DREAD to assess application risks
* Integrate `SAST` and `DAST` tools into the development workflow
* Implement secure secrets management practices using tools like `HashiCorp Vault`
* Design and adopt a secure `SDLC` framework across development teams
* Perform dependency scanning and manage software supply chain risks
* Establish security gates within `CI/CD` pipelines
* Develop security champions programs and foster security-aware culture

## Outline
<!-- chapter: introduction-to-application-security, duration: 2h -->
* Introduction to Application Security
    * The evolving application threat landscape
    * Cost of security breaches and business impact
    * Security as a shared responsibility
    * Overview of `OWASP` and its mission
    * Application security vs network security
    * Compliance requirements and industry standards
<!-- chapter: owasp-top-10-deep-dive, duration: 2h -->
* `OWASP Top 10` Deep Dive
    * Broken Access Control: identification and prevention
    * Cryptographic Failures: common mistakes and best practices
    * Injection attacks: `SQL`, `NoSQL`, `OS command`, and `LDAP` injection
    * Insecure Design: secure `design patterns` and principles
    * Security Misconfiguration: hardening and default settings
    * Vulnerable and Outdated Components: detection and remediation
    * Identification and Authentication Failures: secure authentication patterns
    * Software and Data Integrity Failures: `CI/CD` pipeline protection
    * Security Logging and Monitoring Failures: effective logging strategies
    * Server-Side Request Forgery (SSRF): attack vectors and defenses
<!-- chapter: threat-modeling, duration: 2h -->
* Threat Modeling
    * Introduction to threat modeling methodologies
    * `STRIDE` model: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege
    * DREAD risk assessment model
    * Creating data flow diagrams for threat analysis
    * Identifying trust boundaries and attack surfaces
    * Prioritizing threats and defining mitigations
    * Threat modeling tools and automation
    * Integrating threat modeling into the design phase
<!-- chapter: static-application-security-testing-sast, duration: 2h -->
* Static Application Security Testing (`SAST`)
    * Principles of static code analysis for security
    * Popular `SAST` tools: `SonarQube`, Checkmarx, `Semgrep`
    * Configuring and tuning `SAST` rules to reduce false positives
    * Integrating `SAST` into IDE and `CI/CD` pipelines
    * Interpreting `SAST` results and prioritizing findings
    * Custom rule creation for organization-specific patterns
    * Limitations of `SAST` and complementary approaches
<!-- chapter: dynamic-application-security-testing-dast, duration: 2h -->
* Dynamic Application Security Testing (`DAST`)
    * Principles of runtime security testing
    * Popular `DAST` tools: `OWASP ZAP`, `Burp Suite`
    * Configuring `DAST` scans for web applications and APIs
    * Authenticated scanning and crawling strategies
    * Integrating `DAST` into `CI/CD` pipelines
    * Interpreting `DAST` results and correlating with `SAST` findings
    * Interactive Application Security Testing (IAST) overview
<!-- chapter: secrets-management, duration: 2h -->
* Secrets Management
    * Risks of hardcoded secrets and credential leakage
    * Secrets management solutions: `HashiCorp Vault`, `AWS Secrets Manager`, `Azure Key Vault`
    * Secret rotation policies and automation
    * Environment variable management and secure configuration
    * Detecting leaked secrets with tools like GitLeaks and `TruffleHog`
    * Secrets in containerized environments and `Kubernetes`
    * Encryption at `rest` and in transit for sensitive data
<!-- chapter: secure-software-development-lifecycle-sdlc, duration: 2h -->
* Secure Software Development Lifecycle (`SDLC`)
    * Phases of a secure `SDLC`
    * Security requirements gathering and abuse case development
    * Secure coding guidelines and standards
    * Security code review processes and checklists
    * Security testing strategies at each `SDLC` phase
    * Security sign-off and release management
    * Building a security champions program
    * Maturity models: `OWASP SAMM` and `BSIMM`
<!-- chapter: dependency-scanning-and-supply-chain-security, duration: 2h -->
* Dependency Scanning and Supply Chain Security
    * Software composition analysis (`SCA`) principles
    * Dependency scanning tools: `Snyk`, `Dependabot`, `OWASP Dependency-Check`
    * Managing vulnerability disclosures and CVE databases
    * Software Bill of Materials (`SBOM`) generation and management
    * Lock `file` integrity and dependency pinning
    * Private registry security and artifact verification
    * Responding to zero-day vulnerabilities in dependencies

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
