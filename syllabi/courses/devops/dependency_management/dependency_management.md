---
tags:
  - practices:devops
  - security:security
  - practices:automation
level: intermediate
category: devops
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
  - audiences:security-professionals
---
<!-- course: dependency_management -->
# Dependency Management

## Description
This course covers the principles and practices of managing software dependencies effectively
and securely. Participants will learn about versioning strategies, vulnerability scanning,
automated dependency updates, supply chain security, and license compliance. The course
provides practical guidance on configuring tools like `Dependabot`, `Renovate`, and `Snyk`,
and addresses the growing importance of software supply chain security.

## Duration
16 hours / 1 day

## Intended Audience
* developers responsible for maintaining project dependencies.
* `devops` engineers managing build pipelines and security scanning.
* security-minded engineers focused on supply chain integrity.

## Prerequisites
* experience with at least one package manager (`npm`, `pip`, `Maven`, `Go modules`, etc.).
* basic understanding of `CI/CD` pipelines.
* familiarity with `Git` and pull request workflows.

## Required Knowledge
* `Go` Programming (or equivalent experience)

## Objectives
* understand dependency management fundamentals and versioning strategies.
* configure automated dependency update tools.
* implement vulnerability scanning and supply chain security practices.
* manage license compliance and software bill of materials.

## Outline
<!-- chapter: dependency-management-fundamentals, duration: 1h -->
* Dependency management fundamentals
    * why dependency management matters
    * direct vs transitive dependencies
    * dependency trees and graphs
    * dependency hell and resolution conflicts
<!-- chapter: semantic-versioning, duration: 1h -->
* Semantic versioning
    * major, minor, and patch versions
    * pre-release and build metadata
    * version ranges and constraints
    * breaking changes and compatibility
<!-- chapter: lock-files, duration: 1h -->
* Lock files
    * purpose of lock files
    * lock files across ecosystems (package-lock.`json`, Pipfile.lock, `go`.sum)
    * deterministic builds
    * `when` to commit lock files
<!-- chapter: dependency-resolution, duration: 1h -->
* Dependency resolution
    * resolution algorithms
    * conflict resolution strategies
    * peer dependencies
    * platform-specific dependencies
<!-- chapter: vulnerability-scanning, duration: 1h -->
* Vulnerability scanning
    * `Dependabot` security alerts
    * `Snyk` vulnerability scanning
    * `npm audit`, `pip`-audit, and similar tools
    * interpreting vulnerability reports
    * prioritizing and remediating vulnerabilities
<!-- chapter: automated-dependency-updates, duration: 1h -->
* Automated dependency updates
    * `Renovate` configuration and setup
    * `Dependabot` configuration and setup
    * custom update rules and schedules
    * auto-merge policies
<!-- chapter: update-strategies, duration: 2h -->
* Update strategies
    * grouping related updates
    * scheduling update `windows`
    * automerge criteria
    * handling breaking updates
    * staged rollouts
<!-- chapter: security-advisories-and-cves, duration: 1h -->
* Security advisories and CVEs
    * understanding CVE identifiers
    * security advisory databases
    * responsible disclosure
    * patching strategies and timelines
<!-- chapter: sbom-software-bill-of-materials, duration: 1h -->
* `SBOM` (Software Bill of Materials)
    * what is an `SBOM`
    * `SBOM` formats (`SPDX`, `CycloneDX`)
    * generating SBOMs
    * `SBOM` in procurement and compliance
<!-- chapter: license-compliance, duration: 1h -->
* License compliance
    * open-source license types (MIT, `Apache`, GPL, etc.)
    * license compatibility
    * license scanning tools
    * organizational license policies
<!-- chapter: supply-chain-security, duration: 1h -->
* Supply chain security
    * `Sigstore` and code signing
    * `SLSA` framework and build provenance
    * dependency pinning and verification
    * typosquatting and dependency confusion attacks
<!-- chapter: private-registries, duration: 1h -->
* Private registries
    * setting up private package registries
    * proxying and caching public registries
    * access control and authentication
    * common solutions (Artifactory, `Nexus`, `GitHub Packages`)
<!-- chapter: monorepo-dependency-management, duration: 1h -->
* Monorepo dependency management
    * shared dependencies in monorepos
    * workspace protocols
    * version consistency across packages
    * tools for monorepo dependency management
<!-- chapter: best-practices, duration: 2h -->
* Best practices
    * dependency review in pull requests
    * keeping dependencies current
    * evaluating new dependencies
    * deprecation and removal strategies
    * organizational policies and governance

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
