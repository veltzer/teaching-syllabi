---
tags:
  - languages:java
  - security:security
  - security:secure-coding
  - security:owasp
level: advanced
category: language
duration_hours: 16
audience:
  - audiences:developers
  - audiences:security-professionals
---
<!-- course: java_security -->
# `Java` Security

## Description
This course provides a comprehensive overview of security in `Java` applications. Participants
will learn the `Java` security architecture, cryptography APIs, secure coding practices, and
how to defend against the `OWASP` `Top` 10 vulnerabilities. The course covers input validation,
authentication and authorization mechanisms, secure communications with `TLS`/`SSL`,
dependency vulnerability scanning, and serialization security.

## Duration
16 hours / 2 days

## Intended Audience
* `Java` developers who want to write more secure applications.
* Security professionals working with `Java`-based systems.

## Prerequisites
* `Solid` experience in `Java` programming.
* Basic understanding of security concepts.

## Objectives
* Participants will gain the ability to
    * Understand the `Java` security architecture and its components.
    * Use `Java` cryptography APIs for encryption, hashing, and signing.
    * Apply secure coding practices to prevent common vulnerabilities.
    * Defend against the `OWASP` `Top` 10 threats in `Java` applications.
    * Implement secure authentication and authorization.
    * Configure secure communications using `TLS`/`SSL`.

## Outline
<!-- chapter: java-security-architecture, duration: 1h -->
* `Java` Security Architecture
    * Security model overview
    * SecurityManager and policy files
    * Permissions and protection domains
    * Code signing and verification
    * Security providers framework
<!-- chapter: cryptography-apis, duration: 2h -->
* Cryptography APIs
    * `Java` Cryptography Architecture (JCA)
    * `Java` Cryptography Extension (JCE)
    * Symmetric encryption (`AES`, DES)
    * Asymmetric encryption (`RSA`, EC)
    * Message digests and hashing
    * Digital signatures
    * Key management and keystores
<!-- chapter: secure-coding-practices, duration: 2h -->
* Secure Coding Practices
    * Defensive programming principles
    * Immutable objects and thread safety
    * Least privilege principle
    * Fail-safe defaults
    * Secure exception handling
    * Logging security considerations
<!-- chapter: owasp-top-10-for-java, duration: 3h -->
* `OWASP` `Top` 10 for `Java`
    * Injection attacks and prevention
    * Broken authentication
    * Sensitive data exposure
    * `XML` External Entities (XXE)
    * Broken access control
    * Security misconfiguration
    * Cross-Site Scripting (`XSS`)
    * Insecure deserialization
    * Using components with known vulnerabilities
    * Insufficient logging and monitoring
<!-- chapter: input-validation, duration: 2h -->
* Input Validation
    * Validation strategies and frameworks
    * Whitelisting vs blacklisting
    * Regular expression based validation
    * Bean Validation (JSR 380)
    * Sanitization techniques
    * Preventing `SQL` injection
<!-- chapter: authentication-and-authorization, duration: 1h -->
* Authentication and Authorization
    * JAAS — `Java` Authentication and Authorization Service
    * Token-based authentication
    * `OAuth` 2.0 and `OpenID Connect`
    * Role-based access control
    * Attribute-based access control
<!-- chapter: secure-communications, duration: 2h -->
* Secure Communications
    * `TLS`/`SSL` fundamentals
    * Configuring `HTTPS` in `Java`
    * Certificate management
    * Trust stores and key stores
    * Certificate pinning
    * Mutual `TLS` authentication
<!-- chapter: dependency-vulnerability-scanning, duration: 2h -->
* Dependency Vulnerability Scanning
    * Supply chain security risks
    * `OWASP` Dependency-`Check`
    * `Snyk` and other scanning tools
    * CVE databases and vulnerability tracking
    * Automated scanning in `CI/CD` pipelines
    * Dependency update strategies
<!-- chapter: serialization-security, duration: 1h -->
* Serialization Security
    * Risks of `Java` serialization
    * Deserialization attacks
    * Filtering and whitelisting classes
    * Alternatives to native serialization
    * `JSON` and `XML` serialization security

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
