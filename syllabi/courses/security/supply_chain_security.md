---
tags:
  - security:supply-chain
  - security:sbom
  - tools:sigstore
  - concepts:slsa
  - practices:devops
level: intermediate
category: security
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
  - audiences:security-engineers
---
<!-- course: supply_chain_security -->
# Software Supply Chain Security

## Description
Software supply chain attacks have become one of the most significant threats facing modern organizations, as demonstrated by incidents like `SolarWinds`, `Codecov`, and the `XZ Utils` backdoor. This course provides a thorough grounding in the threats, frameworks, and tools used to secure the software supply chain from source code through to deployment. Participants will learn to apply the `SLSA` framework, generate and consume `SBOM`s, sign artifacts with `Sigstore` and `Cosign`, and enforce supply chain policies using `OPA` and `Kyverno`. By the end of the course, attendees will be able to evaluate their organization's supply chain risk posture and implement concrete controls at every stage of the build and delivery pipeline.

## Duration
16 hours / 2 days

## Intended Audience
* Software developers concerned with open-source dependency risk and build integrity
* `DevOps` and platform engineers responsible for `CI/CD` pipeline security
* Security engineers assessing and hardening software delivery pipelines

## Prerequisites
* Hands-on experience with `CI/CD` platforms (`GitHub Actions`, `GitLab CI`, `Jenkins`, or similar)
* Familiarity with `Docker` and container image builds
* Basic understanding of `Git` workflows and version control concepts
* Working knowledge of `Linux` command-line tools
* Awareness of common supply chain attack patterns is helpful but not required

## Objectives
* Identify the major categories of software supply chain threats and historical attack vectors
* Apply the `SLSA` framework to evaluate and improve build provenance and integrity levels
* Generate, validate, and consume `SBOM`s in `SPDX` and `CycloneDX` formats
* Sign container images and binary artifacts using `Sigstore`, `Cosign`, and `Fulcio`
* Perform dependency vulnerability scanning with `SCA` tools and act on findings
* Harden `CI/CD` pipeline configurations to prevent injection and tampering
* Establish container image provenance chains and verify them at deployment time
* Enforce supply chain policy using `OPA` and `Kyverno` in `Kubernetes` environments

## Outline
<!-- chapter: introduction-to-software-supply-chain-threats, duration: 2h -->
* Introduction to Software Supply Chain Threats
    * Defining the software supply chain: source, build, dependencies, delivery
    * Taxonomy of supply chain attacks: dependency confusion, typosquatting, build tampering, insider threat
    * Case studies: `SolarWinds` SUNBURST, `Codecov` script injection, `event-stream` malicious package, `XZ Utils` backdoor
    * The expanding attack surface in open-source ecosystems
    * Why traditional security controls are insufficient for supply chain threats
    * Industry response: `OpenSSF`, `CNCF` supply chain working groups, executive orders
    * Mapping threats to controls using the `SLSA` and `NIST SSDF` frameworks

<!-- chapter: slsa-framework-levels, duration: 2h -->
* `SLSA` Framework Levels
    * What is `SLSA` (Supply-chain Levels for Software Artifacts)?
    * The four `SLSA` levels: requirements and guarantees at each level
    * Provenance: what it is, what it contains, and how it is generated
    * Build platform requirements for `SLSA` level 2 and above
    * Hermetic, reproducible, and isolated builds
    * Generating `SLSA` provenance with `slsa-github-generator` and `slsa-verifier`
    * Achieving `SLSA` level 3 in practice: challenges and tooling
    * Verifying provenance in downstream consumers and deployment systems

<!-- chapter: software-bill-of-materials-sbom, duration: 2h -->
* Software Bill of Materials (`SBOM`)
    * What is an `SBOM` and why it is mandated by US executive orders and emerging regulation
    * `SBOM` formats: `SPDX` vs `CycloneDX` — structure, tooling, and ecosystem support
    * Generating `SBOM`s for container images, `npm`, `pip`, `Maven`, and `Go` modules
    * Tools: `Syft`, `cdxgen`, `Trivy`, and language ecosystem native tools
    * `SBOM` signing, attestation, and embedding in `OCI` images
    * Consuming and querying `SBOM`s for vulnerability correlation (`Grype`, `OSV`)
    * `SBOM` management at scale: storage, lifecycle, and tooling integration

<!-- chapter: sigstore-and-cosign-for-artifact-signing, duration: 2h -->
* `Sigstore` and `Cosign` for Artifact Signing
    * Why artifact signing matters: preventing tampering and establishing provenance
    * The `Sigstore` project: `Cosign`, `Fulcio`, `Rekor` — architecture and trust model
    * Keyless signing with `OIDC` identity tokens and the `Fulcio` certificate authority
    * Signing container images with `Cosign`: push, verify, and inspect attestations
    * The `Rekor` transparency log: tamper-evident append-only ledger
    * Signing arbitrary blobs, `SBOM`s, and build provenance documents
    * Integrating `Cosign` signing and verification into `CI/CD` pipelines
    * Policy enforcement: requiring verified signatures before deployment

<!-- chapter: dependency-security-and-sca, duration: 2h -->
* Dependency Security and `SCA`
    * Open-source dependency risk: direct vs transitive dependencies
    * Software Composition Analysis (`SCA`) tools: `Snyk`, `Dependabot`, `OWASP Dependency-Check`, `Socket`
    * `OSV` (Open Source Vulnerabilities) database and `osv-scanner`
    * Package repository security features: `npm` audit, `pip-audit`, `go mod verify`
    * Dependency pinning, lockfiles, and integrity verification (`hash pinning`)
    * Detecting malicious packages: behavioral analysis and `Socket`'s static analysis
    * Automating dependency updates with `Renovate` and `Dependabot`

<!-- chapter: securing-build-pipelines, duration: 2h -->
* Securing Build Pipelines
    * `CI/CD` as a high-value attack target: pipeline injection and credential theft
    * `GitHub Actions` security: pinning actions by `SHA`, avoiding `pull_request_target` misuse
    * Securing `GitLab CI`, `Jenkins`, and `Tekton` pipelines against injection attacks
    * Principle of least privilege for pipeline service accounts and tokens
    * Ephemeral, isolated build environments: preventing build poisoning
    * `OIDC`-based cloud authentication from `CI/CD` — eliminating long-lived credentials
    * Auditing pipeline configurations for common misconfigurations

<!-- chapter: container-image-provenance, duration: 2h -->
* Container Image Provenance
    * Container image layers and the provenance challenge
    * Reproducible and deterministic image builds
    * Generating provenance attestations for container images with `Buildkit` and `GitHub Actions`
    * `OCI` Image Manifest and Referrers `API` for attaching attestations
    * Verifying image provenance in admission controllers
    * Minimal base images: `distroless`, `scratch`, and `Wolfi` to reduce attack surface
    * Image tagging vs `digest` pinning: why tags are mutable and digests are not

<!-- chapter: policy-enforcement-with-opa-and-kyverno, duration: 2h -->
* Policy Enforcement with `OPA` and `Kyverno`
    * Policy as code: enforcing supply chain controls at cluster admission time
    * `OPA` (`Open Policy Agent`) architecture: `Rego` language and policy evaluation model
    * `Gatekeeper`: `OPA` as a `Kubernetes` admission controller
    * `Kyverno` policies: simpler `YAML`-native policy authoring for `Kubernetes`
    * Writing policies to `require` signed images, verified `SBOM` attestations, and `SLSA` provenance
    * Audit mode vs enforce mode: incremental policy rollout strategies
    * Integrating policy enforcement into `GitOps` workflows with `Flux` and `ArgoCD`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
