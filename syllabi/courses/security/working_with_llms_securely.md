---
tags:
  - security:security
  - data-and-ai:ai
  - data-and-ai:llm
  - security:owasp
level: intermediate
category: security
duration_days: 1
audience:
  - audiences:developers
  - audiences:security-professionals
---
# Working with `LLMs` Securely

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This one day course covers the OWASP Top 10 for Large Language Model Applications, providing a comprehensive understanding of the most critical security risks when building and deploying `LLM`-based systems. Students will learn to identify, exploit, and mitigate each vulnerability category through practical examples and hands-on exercises.

## Duration
8 hours / 1 day

## Intended Audience
* Software developers integrating `LLMs` into applications
* Security engineers evaluating `LLM` deployments
* `DevOps` engineers deploying `LLM`-based systems

## Prerequisites
* Basic understanding of `LLMs` and their `APIs`
* Familiarity with web application security concepts
* Programming experience in `Python` or similar language

## Objectives
* Understand the OWASP Top 10 for `LLM` Applications.
* Identify and exploit common `LLM` vulnerabilities.
* Implement mitigations for each vulnerability category.
* Design secure `LLM` integration architectures.

## Outline
* Introduction to OWASP Top 10 for `LLMs`
    * Overview of OWASP `LLM` project
    * Threat modeling for `LLM` applications
    * Attack surface analysis
* LLM01: Prompt Injection
    * Direct prompt injection techniques
    * Indirect prompt injection via external data
    * Mitigation strategies and input validation
* LLM02: Insecure Output Handling
    * Cross-site scripting via `LLM` outputs
    * Server-side request forgery
    * Output encoding and sanitization
* LLM03: Training Data Poisoning
    * Data poisoning attack vectors
    * Supply chain risks in training data
    * Data validation and provenance tracking
* LLM04: Model Denial of Service
    * Resource exhaustion attacks
    * Query complexity exploitation
    * Rate limiting and resource management
* LLM05: Supply Chain Vulnerabilities
    * Third-party model risks
    * Plugin and extension security
    * Dependency management and verification
* LLM06: Sensitive Information Disclosure
    * Training data extraction attacks
    * PII leakage through outputs
    * Data sanitization and filtering
* LLM07: Insecure Plugin Design
    * Plugin permission models
    * Input validation for plugins
    * Sandboxing and least privilege
* LLM08: Excessive Agency
    * Autonomous action risks
    * Human-in-the-loop controls
    * Permission boundaries and approval workflows
* LLM09: Overreliance
    * Hallucination and misinformation risks
    * Verification and fact-checking strategies
    * User education and trust calibration
* LLM10: Model Theft
    * Model extraction attacks
    * `API` abuse for model replication
    * Access controls and monitoring

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
