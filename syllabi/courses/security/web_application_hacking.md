---
tags:
  - security:security
  - security:web-security
  - security:penetration-testing
  - security:owasp
level: advanced
category: security
duration_hours_short: 16
duration_hours_long: 40
audience:
  - audiences:security-professionals
  - audiences:developers
  - audiences:testers
duration_hours: 40
---
<!-- course: web_application_hacking -->
# Web Application Hacking

## Description
This course is a practical guide to discovering and exploiting security flaws in web applications. By "web applications" we mean those that are accessed using a web browser to communicate with a web server. We examine a wide variety of different technologies, such as databases, `file` systems, and `web services`, but only in the context in which these are employed by web applications. Throughout the course, we spell out the specific steps you need to follow to detect each type of vulnerability, and how to exploit it to perform unauthorized actions.

## Duration
* Short: 16 hours / 2 days
* Long: 40 hours / 5 days

## Intended Audience
* Penetration testers
* Web application developers
* Security vendors and service providers (`IPS`, `WAF`, Browser security)
* Web-focused QA with aspirations in security

## Prerequisites
* Hands-on familiarity with web technologies (`HTML`, `JavaScript`, `SQL`, server-code)
* Good system skills (`Linux` or `Windows`, preferably both)
* Good coding skills (any of these will do: `Java`, `Python`, `C#`, `JavaScript`, `PHP`, ...)
* Good understanding in networking technologies (`IP`, `TCP`, `DNS`, `HTTP`, `HTTPS`)

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Improve your understanding of web vulnerabilities and security
* Manual and automated application mapping
* Anatomy of server attacks; from injection to root
* Learn how to attack Authentication and Session
* Learn how to attack and exploit data-stores (`SQL`, `NoSQL`)
* Learn Client attack techniques (`XSS`, `CSRF`)
* Learn how to attack Access Controls
* Learn how to attacking Back-End Components and Application Logic
* Gain better understanding in OS & service hardening
* Gain understanding in input sanitation and data validation
* Learn about web application filters and firewalls

## Exercises
We will use common hacking practice sites to exercise (see below)
These are the exercises that we will do:

* `SQL` Injection hack
* Cross-Site Scripting (`XSS`)
* Broken Authentication
* Sensitive Data Exposure
* Security Misconfiguration

## Outline
<!-- chapter: web-application-in-security, duration: 3h -->
* Web application (in)security
    * Server OS platforms
    * Web servers (`Apache`, `nginx`, weblogic, `IIS` etc.)
    * Server-side application frameworks and programming languages
    * Data-stores; Relational (`SQL`), non-relational (`NoSQL`) and document-based
    * Client-side technologies (Browsers, Browser plugins, `HTML`, HTML5, `CSS`, `JavaScript` etc.)
    * Offensive toolset and practice targets
<!-- chapter: mapping-web-applications, duration: 6h -->
* Mapping web applications
    * Web spidering (automated and user directed)
    * Discovering Hidden Content
    * Application Pages Versus Functional Paths
    * Discovering Hidden Parameters
    * Identifying Entry Points for User Input
    * Identifying Server-Side Technologies and Functionality
    * Mapping the Attack Surface
    * Transmitting Data Via the Client [long]
    * Capturing User Data: `HTML` Forms [long]
    * Capturing User Data: Browser Extensions [long]
<!-- chapter: authentication-and-session-attacks, duration: 5h -->
* Authentication and session attacks
    * Authentication Technologies
    * Design Flaws in Authentication Mechanisms
    * Brute-forcing logins
    * Implementation Flaws in Authentication
    * Securing Authentication
    * The Need for State
    * Weaknesses in Token Generation [long]
    * Weaknesses in Session Token Handling [long]
    * Securing Session Management [long]
<!-- chapter: attacking-data-stores, duration: 8h -->
* Attacking data stores
    * Exploiting a Basic Vulnerability
    * Injecting into Different Statement Types
    * Finding `SQL` Injection Bugs
    * Fingerprinting the Database
    * Extracting Data with UNION
    * Performing Blind injections
    * Automating SQLi testing with sqlmap
    * Advanced Exploitation (FS interaction, and code execution)
    * Bypassing Filters
    * Second-Order `SQL` Injection
    * Beyond `SQL` Injection: Escalating the Database Attack [long]
    * Using `SQL` Exploitation Tools [long]
    * `SQL` Syntax and Error Reference [long]
    * Preventing `SQL` Injection [long]
<!-- chapter: attacking-users-cross-site-scripting, duration: 4h -->
* Attacking Users: Cross-Site Scripting
    * Varieties of `XSS`
    * Real-World `XSS` Attacks
    * Payloads for `XSS` Attacks
    * Delivery Mechanisms for `XSS` Attacks
    * Finding and Exploiting `XSS` Vulnerabilities [long]
    * Preventing Reflected and Stored `XSS` [long]
    * Evading security filters and browser checks [long]
<!-- chapter: attacking-back-end-components-and-application-logic, duration: 5h -->
* Attacking Back-End Components and Application Logic
    * Injecting OS Commands
    * Manipulating `File` Paths
    * Injecting objects and (de)serializers
    * The Nature of Logic Flaws
    * Real-World Logic Flaws
    * Avoiding Logic Flaws [long]
    * Hardening OS networking stacks [long]
    * Implement host-based firewalls and "good" logging [long]
    * Hardening web application servers (`Apache`, `IIS`) [long]
<!-- chapter: boot2root-attack-scenario-against-a-server-long, duration: 6h -->
* boot2root attack scenario against a server [long]
    * Scanning, enumeration and resource mapping
    * Testing for possible injections
    * Detect vulnerable parser at other side
    * Inject code
    * Gather system information
    * Establish control connection
    * Enumerate attack surface (resources, services, users, permissions, execution paths etc)
    * Escalate privileges
    * Establish persistence
    * Pivot
<!-- chapter: boot2root-now-it-s-your-turn-optional-long, duration: 3h -->
* boot2root: now it's your turn (optional) [long]
    * Final CTF
    * Students work on their own and submit reports
    * Workshop summary

## References
* [TryHackMe](`https`://tryhackme.com/dashboard)
* [HackThisSite](`https`://www.hackthissite.org)
* [CTFlearn](`https`://ctflearn.com)

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
