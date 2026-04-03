---
tags:
  - security:penetration-testing
  - security:web-security
  - security:owasp
  - security:vulnerabilities
level: advanced
category: security
duration_hours: 24
audience:
  - audiences:security-professionals
  - audiences:developers
  - audiences:testers
---
<!-- course: web_application_penetration_testing -->
# Web Application Penetration Testing

## Description
This advanced course provides hands-on training in web application penetration testing, covering the full pentesting lifecycle from reconnaissance through exploitation and reporting. Participants will learn to use industry-standard tools such as `Burp Suite` and `OWASP ZAP` to identify and exploit common web application vulnerabilities. The course follows the `OWASP` Testing Guide methodology and emphasizes responsible disclosure practices.

The course covers both manual and automated testing techniques, equipping participants with the skills needed to assess the security posture of modern web applications and APIs.

## Duration
24 hours / 3 days

## Intended Audience
* Security professionals conducting web application assessments
* Developers seeking to understand attacker techniques
* Penetration testers expanding their web application testing skills
* QA testers transitioning into security testing roles

## Prerequisites
* `Solid` understanding of `HTTP` protocol and web technologies
* Familiarity with `HTML`, `JavaScript`, and `SQL`
* Basic networking knowledge (`TCP`/`IP`, `DNS`)
* Experience with `Linux` command line
* Understanding of common web application architectures

## Required Knowledge
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Apply a structured pentesting methodology to web application assessments
* Perform thorough reconnaissance and information gathering
* Use `Burp Suite` and `OWASP ZAP` for vulnerability discovery and exploitation
* Identify and exploit `SQL` injection, `XSS`, and `CSRF` vulnerabilities
* Test authentication and session management mechanisms
* Conduct `API` penetration testing
* Produce professional penetration testing reports
* Practice responsible disclosure procedures

## Outline
<!-- chapter: pentesting-methodology, duration: 2h -->
* Pentesting Methodology
    * Penetration testing standards and frameworks
    * Scoping and rules of engagement
    * Testing phases overview
    * Legal and ethical considerations
    * Setting up the testing environment
<!-- chapter: reconnaissance-and-information-gathering, duration: 2h -->
* Reconnaissance and Information Gathering
    * Passive reconnaissance techniques
    * Active reconnaissance techniques
    * Subdomain enumeration
    * Technology fingerprinting
    * Directory and `file` discovery
    * Gathering information from public sources
<!-- chapter: owasp-testing-guide, duration: 1h -->
* `OWASP` Testing Guide
    * `OWASP` Testing Guide overview
    * `OWASP` `Top` 10 vulnerabilities
    * Testing methodology and checklists
    * Risk rating and severity classification
<!-- chapter: burp-suite, duration: 2h -->
* `Burp Suite`
    * Configuring `Burp Suite` proxy
    * Intercepting and modifying requests
    * Using the scanner
    * Intruder and Repeater tools
    * Sequencer for session token analysis
    * Extensions and BApp Store
<!-- chapter: owasp-zap, duration: 2h -->
* `OWASP ZAP`
    * ZAP configuration and setup
    * Automated scanning
    * Active and passive scanning modes
    * Fuzzing with ZAP
    * Scripting and automation
<!-- chapter: sql-injection-exploitation, duration: 2h -->
* `SQL` Injection Exploitation
    * Types of `SQL` injection (in-band, blind, out-of-band)
    * Manual detection and exploitation
    * Union-based extraction techniques
    * Boolean-based and time-based blind injection
    * Using sqlmap for automated exploitation
    * Second-order `SQL` injection
    * Bypassing `WAF` and filters
<!-- chapter: xss-exploitation, duration: 2h -->
* `XSS` Exploitation
    * Reflected `XSS`
    * Stored `XSS`
    * DOM-based `XSS`
    * `XSS` filter evasion techniques
    * Cookie stealing and session hijacking via `XSS`
    * `XSS` in modern frameworks
<!-- chapter: csrf-attacks, duration: 2h -->
* `CSRF` Attacks
    * Understanding `CSRF` attack flow
    * Crafting `CSRF` payloads
    * Token-based defenses and their weaknesses
    * SameSite cookie attribute bypass
    * `CSRF` in `JSON` and `XML` requests
<!-- chapter: authentication-bypass, duration: 2h -->
* Authentication Bypass
    * Brute-force and credential stuffing
    * Default credentials testing
    * Password reset flaws
    * Multi-factor authentication bypass
    * `OAuth` and SSO vulnerabilities
    * `JWT` attacks (algorithm confusion, token manipulation)
<!-- chapter: session-management-testing, duration: 2h -->
* Session Management Testing
    * Session token analysis
    * Session fixation
    * Session hijacking
    * Cookie attribute testing
    * Concurrent session handling
    * Session timeout and logout testing
<!-- chapter: api-penetration-testing, duration: 2h -->
* `API` Penetration Testing
    * `REST API` security testing
    * `GraphQL` security testing
    * Authentication and authorization testing in APIs
    * Rate limiting and resource exhaustion
    * Mass assignment and BOLA vulnerabilities
    * `API` documentation analysis
<!-- chapter: reporting-and-documentation, duration: 2h -->
* Reporting and Documentation
    * Structuring a penetration test report
    * Writing effective vulnerability descriptions
    * Risk rating and prioritization
    * Remediation recommendations
    * Executive summary writing
<!-- chapter: responsible-disclosure, duration: 1h -->
* Responsible Disclosure
    * Disclosure policies and frameworks
    * Bug bounty programs
    * Coordinated vulnerability disclosure
    * Communication with stakeholders

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
