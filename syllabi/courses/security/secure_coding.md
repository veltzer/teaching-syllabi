---
tags:
  - security:secure-coding
  - security:owasp
  - security:encryption
  - security:compliance
  - security:application-security
  - languages:c
  - languages:c++
  - languages:python
  - practices:ci-cd
  - practices:devops
  - data-and-ai:ai
  - hardware-and-embedded:embedded
level: intermediate
category: security
duration_hours: 8
audience:
  - audiences:developers
  - audiences:embedded-engineers
  - audiences:devops
  - audiences:security-professionals
---

<!-- course: secure_coding -->
# Secure Coding

## Description
This course covers the principles and practices of writing secure code across multiple languages and platforms.
It addresses the full spectrum of secure development, from supply chain security and `CI/CD` pipeline hardening
to hardware-based security mechanisms like secure boot and secure elements. The course also covers encryption
fundamentals, industry standards such as `OWASP` and `NIST`, and the emerging field of secure `AI` development.
Examples and demonstrations are given in `Linux`, C, `C++`, and `Python`.

Please note that this is just a review course and we will not have to deal with each topic in depth.

## Duration
8 hours / 1 day

## Intended Audience
* Embedded and systems developers working with C and `C++`
* `Python` developers building backend or infrastructure services
* `DevOps` and `CI/CD` engineers responsible for build pipeline security
* Security engineers and architects designing secure systems
* Developers working with hardware security and secure boot processes

## Prerequisites
* Working knowledge of at least one of: C, `C++`, or `Python`
* Basic familiarity with `Linux`
* General understanding of software development workflows

## Objectives
* Understand supply chain security risks and mitigations.
* Design secure protocols using hardware-backed mechanisms.
* Apply cryptography correctly across C, `C++`, and `Python`.
* Apply `OWASP` and `NIST` guidelines to real code.
* Harden `CI/CD` pipelines, secure boot chains, and secure elements.
* Understand security risks specific to `AI`/`ML` development.

## Outline
<!-- chapter: supply-chain-security, duration: 1h -->
* Supply Chain Security
    * Understanding software supply chain attacks
    * Dependency management and verification
    * Software Bill of Materials (`SBOM`)
    * Package integrity and signing
    * Vendor and third-party risk assessment
    * Software configuration management and secure change management
    * Separation of duties (e.g. developers and `DevOps` shall not be the ones deploying to production)
<!-- chapter: designing-secure-protocols-with-hardware, duration: 1h -->
* Designing Secure Protocols with Hardware
    * Hardware security fundamentals
    * Hardware-software trust boundaries
    * Secure communication protocols
    * Attestation and authentication mechanisms
    * Key management with hardware support
<!-- chapter: encryption, duration: 1h -->
* Encryption
    * Symmetric vs asymmetric encryption
    * Hashing and message authentication codes
    * `TLS`/`SSL` and secure transport
    * Key generation, storage, and rotation
    * Common cryptographic pitfalls in C, `C++`, and `Python`
<!-- chapter: owasp-and-nist, duration: 1h -->
* `OWASP` and `NIST`
    * `OWASP` `Top` 10 overview
    * Secure coding guidelines per language
    * `NIST` Cybersecurity Framework
    * `NIST` Secure Software Development Framework (`SSDF`)
    * Applying standards to real-world codebases
<!-- chapter: cicd-security, duration: 1h -->
* `CI/CD` Security
    * Securing the build pipeline
    * Secrets management in `CI/CD`
    * Static and dynamic analysis integration
    * Container image scanning and signing
    * Artifact integrity and provenance
<!-- chapter: secure-boot, duration: 1h -->
* Secure Boot
    * The boot chain of trust
    * `UEFI` Secure Boot
    * Bootloader verification
    * Kernel and module signing
    * Measured boot and trusted platform modules
<!-- chapter: secure-element, duration: 1h -->
* Secure Element
    * What is a secure element
    * Trusted Platform Module (`TPM`)
    * Hardware Security Modules (`HSM`)
    * Secure enclaves and trusted execution environments
    * Integrating secure elements into applications
<!-- chapter: secure-ai-development, duration: 1h -->
* Secure `AI` Development
    * Security risks in `AI`/`ML` pipelines
    * Training data integrity and poisoning
    * Model security and intellectual property protection
    * Adversarial attacks and defenses
    * Secure deployment of `AI` models
    * `NIST` SP 800-218A - Secure Software Development Practices for Generative `AI` and Dual-Use Foundation Models
    * `OWASP` guidelines for `AI`/`ML` security

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
