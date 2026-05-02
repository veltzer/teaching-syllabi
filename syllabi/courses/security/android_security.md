---
tags:
  - security:security
  - infrastructure:android
  - security:secure-coding
  - security:vulnerabilities
level: advanced
category: security
duration_hours: 16
audience:
  - audiences:developers
  - audiences:security-professionals
  - audiences:testers
---
<!-- course: android_security -->
# `Android` Security

## Description
This course provides an in-depth exploration of `Android` platform security, covering the security model,
application sandboxing, secure coding practices, and defenses against reverse engineering and malware.
Participants will learn how to build secure `Android` applications and assess the security posture of
existing apps.

## Duration
16 hours / 2 days

## Intended Audience
* `Android` developers who want to build more secure applications
* Security professionals assessing `Android` application security
* Testers performing security testing on `Android` apps

## Prerequisites
* Experience with `Android` application development
* Familiarity with `Java` or `Kotlin`
* Basic understanding of security concepts

## Required Knowledge
* `Kotlin` Programming (or equivalent experience)

## Objectives
* Understand the `Android` security model and its layered architecture
* Implement proper permission handling and app sandboxing
* Apply secure storage and network communication techniques
* Defend applications against reverse engineering and tampering
* Integrate biometric authentication securely
* Identify and mitigate common `Android` vulnerabilities

## Outline
<!-- chapter: android-security-model, duration: 1h -->
* `Android` Security Model
    * `Android` platform architecture and security layers
    * `Linux` kernel security features
    * Security-Enhanced `Linux` (`SELinux`) on `Android`
    * Verified boot and trusted execution environment
    * Application signing and trust model
<!-- chapter: permissions-framework, duration: 1h -->
* Permissions Framework
    * Permission types and protection levels
    * Runtime permissions model
    * Custom permissions and permission groups
    * Inter-app permission enforcement
    * Least privilege principle in practice
<!-- chapter: application-sandboxing, duration: 1h -->
* Application Sandboxing
    * Process isolation and UID assignment
    * `File` system permissions and private storage
    * Intent security and component exposure
    * Content provider security
    * Broadcast receiver protection
<!-- chapter: secure-storage, duration: 1h -->
* Secure Storage
    * `Android` Keystore system
    * Encrypted shared preferences
    * SQLCipher for database encryption
    * Secure file storage patterns
    * Key management best practices
<!-- chapter: network-security-configuration, duration: 1h -->
* Network Security Configuration
    * Network security config file
    * Cleartext traffic restrictions
    * Custom trust anchors
    * Certificate pinning via network security config
    * `TLS` configuration and cipher suites
<!-- chapter: certificate-pinning, duration: 1h -->
* Certificate Pinning
    * Pinning strategies and implementation
    * OkHttp certificate pinner
    * Handling pin rotation and backup pins
    * Detecting pin bypass attempts
<!-- chapter: code-obfuscation, duration: 2h -->
* Code Obfuscation
    * ProGuard configuration and rules
    * R8 compiler optimizations
    * Resource shrinking and obfuscation
    * String encryption techniques
    * Native code protection with `NDK`
<!-- chapter: reverse-engineering-defenses, duration: 2h -->
* Reverse Engineering Defenses
    * Understanding attacker methodologies
    * Anti-debugging techniques
    * Root detection and emulator detection
    * Integrity verification of application package
    * Dynamic analysis countermeasures
<!-- chapter: malware-analysis, duration: 2h -->
* Malware Analysis
    * Common `Android` malware families and techniques
    * Static analysis of suspicious applications
    * Dynamic analysis and behavioral monitoring
    * Identifying malicious permissions and behaviors
    * Threat intelligence for `Android`
<!-- chapter: runtime-integrity-checks, duration: 2h -->
* Runtime Integrity Checks
    * SafetyNet and `Play Integrity API`
    * Runtime application self-protection (RASP)
    * Tamper detection mechanisms
    * Environment trust verification
    * Responding to integrity failures
<!-- chapter: biometric-authentication, duration: 2h -->
* Biometric Authentication
    * `BiometricPrompt API`
    * Cryptographic authentication with biometrics
    * Fallback and error handling strategies
    * Secure user authentication flows
    * Biometric security considerations and limitations

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
