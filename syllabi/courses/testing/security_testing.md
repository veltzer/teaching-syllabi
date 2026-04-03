---
tags:
  - practices:testing
  - security:security
  - security:owasp
  - security:sast
  - security:dast
level: intermediate
category: testing
duration_hours: 16
audience:
  - audiences:developers
  - audiences:security-professionals
  - audiences:devops
  - audiences:testers
---
<!-- course: security_testing -->
# Security Testing

## Description
This two day course provides a practical, hands-on approach to security testing throughout the software development lifecycle. Participants will learn to use industry-standard tools for static and dynamic analysis, dependency scanning, fuzzing, secret detection, and container image scanning, all integrated into `CI/CD` pipelines.

## Duration
16 hours / 2 days

## Intended Audience
* Developers looking to shift security testing left
* Security professionals seeking practical tooling skills
* `DevOps` engineers responsible for pipeline security

## Prerequisites
* Experience developing or deploying software applications
* Basic understanding of application security concepts
* Familiarity with `CI/CD` pipelines and version control

## Objectives
* Apply `SAST` and `DAST` tools to identify vulnerabilities in code and running applications.
* Integrate dependency scanning and secret detection into development workflows.
* Use fuzzing techniques to discover edge-case vulnerabilities.
* Scan container images for known vulnerabilities.
* Build a comprehensive security testing strategy within `CI/CD` pipelines.
* Manage and prioritize vulnerabilities effectively.

## Outline
<!-- chapter: introduction-to-security-testing, duration: 1h -->
* Introduction to Security Testing
    * Security testing in the `SDLC`
    * Shift-left security principles
    * Threat modeling as a testing input
    * Security testing taxonomy
<!-- chapter: static-application-security-testing-sast, duration: 1h -->
* Static Application Security Testing (`SAST`)
    * How `SAST` tools analyze source code
    * Configuring and tuning `SAST` scanners
    * Interpreting and triaging `SAST` findings
    * Reducing false positives
<!-- chapter: dynamic-application-security-testing-dast, duration: 2h -->
* Dynamic Application Security Testing (`DAST`)
    * Setting up `DAST` scans with `OWASP ZAP`
    * Authenticated and unauthenticated scanning
    * `API` security testing with `DAST`
    * Analyzing and validating `DAST` results
<!-- chapter: dependency-scanning, duration: 2h -->
* Dependency Scanning
    * Software composition analysis concepts
    * Scanning dependencies for known CVEs
    * Monitoring and alerting on new vulnerabilities
    * License compliance considerations
<!-- chapter: fuzzing-for-developers, duration: 2h -->
* Fuzzing for Developers
    * Fuzzing fundamentals and techniques
    * Coverage-guided fuzzing
    * Protocol and `API` fuzzing
    * Interpreting fuzzing results and reproducing crashes
<!-- chapter: secret-scanning, duration: 2h -->
* Secret Scanning
    * Detecting secrets in source code and history
    * Pre-commit hooks for secret prevention
    * Remediating leaked secrets
    * Secret management best practices
<!-- chapter: container-image-scanning, duration: 2h -->
* Container Image Scanning
    * Scanning base images and layers
    * Integrating image scanning into build pipelines
    * Policy enforcement and admission control
    * Maintaining minimal and secure base images
<!-- chapter: ci-cd-integration, duration: 2h -->
* `CI/CD` Integration
    * Building security gates into pipelines
    * Orchestrating multiple scanning tools
    * Configuring quality gates and break conditions
    * Reporting and dashboarding security metrics
<!-- chapter: vulnerability-management, duration: 2h -->
* Vulnerability Management
    * Prioritizing vulnerabilities by risk
    * Tracking remediation across teams
    * SLA-based vulnerability management
    * Continuous improvement and metrics

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
