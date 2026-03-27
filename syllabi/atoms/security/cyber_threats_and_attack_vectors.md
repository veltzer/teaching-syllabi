---
tags:
  - security
  - cyber-threats
  - web-security
  - penetration-testing
level: intermediate
category: security
audience:
  - security-professionals
  - developers
---
# Cyber Threats and Attack Vectors

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This course surveys and demonstrates many of the prevalent attack threats, methods and vectors used by today's
hackers. The course starts with introductory material that is needed to understand the technical aspects of
the following chapters and then goes into the various attack vectors. Each attack method is explained, analyzed
and demonstrated.

## Duration
48 hours / 6 days

## Intended Audience
* Anyone who wishes to understand the current security landscape of threats and attack vectors.

## Prerequisites
* Tech affinity
* Programming background is not required but may add to participants understanding

## Outline
* Hacking landscape overview
    * Who are the hackers?
    * What are the hackers motivations?
    * What are the hackers goals?
    * What are the hackers targets?
        * Data theft
        * Password theft
        * Credit card data
        * `DNS`
        * Client takeover
        * CDN
        * Firewall
        * Load Balancer
        * Application (regular and mobile)
        * Web server
        * Operating system
        * Database
    * Attack life-cycle
    * Forensics introduction
* Basic OS security
    * Admin/root vs regular user
    * Password hashing
    * Reverse hashing
    * `sudo` and other tools.
    * Containers and security (e.g. `docker`)
* Networking background
    * IP addresses
    * Geo IP, ISP, ASN, CIDR
    * Routers
    * Firewalls
    * Base 64
    * URL encoding
    * NAT
    * `SSL` (symmetric and asymmetric encryption)
* `DNS` background
    * The protocol and it's versions
    * The `DNS` network
    * Why is `DNS` important for security?
    * The types of `DNS` servers
        * Recursive resolvers
        * root name-servers
        * TLD name-servers
        * authoritative name-servers
* `DNS` hacking
    * Zero-Day-Attack
    * Cache Poisoning
    * `DNS` Denial of Service
    * `DNS` Distributes Denial of Service
    * `DNS` Amplification
    * Fast-Flux `DNS`
* Web/HTTP background
    * What is a webserver?
    * What is a webclient?
    * `HTTP` protocol and it's versions
    * Method headers
    * User-Agent
    * Referrer
    * Body, content-length
    * Dynamic vs static pages
    * `JavaScript`
    * Single page applications
    * `HTTP` parameters
    * Keep-alive/close connection
    * Cookies
    * Server headers
    * CRLF
    * HSTS
    * `HTTP` Error codes
    * Local Storage/Session storage
    * Robots.txt
    * CDN
    * Proxies and caching.
    * TOR
    * X-Forward-For
    * Certificates for server and client (symmetric and non symmetric)
    * CORS
* Web server security
    * `SSL`
    * `SSL` Certificates
    * Access control lists (ACLs)
    * X-Forwarded-For security
* Web application authentication methods
    * Basic Auth
    * Cookies and cookie expiration
    * `HTTP` only cookies
    * Signed cookies
    * JWT and JWT validation
    * Signing requests and validating them.
    * One time passwords
    * Certificate based authentication
    * Bio-metric authentication
    * Multi-factor authentication
    * oauth and oauth2
    * Captcha
* Hacking Web applications
    * Tools to brute-force web forms and applications
    * What is broken authentication
    * Using mechanical Turks and `AI` to break Captcha and other mechanisms.
    * What is form-jacking?
    * What is denial of inventory?
    * Hacking New Gen Bots
    * Data scraping
    * Hacking headless browsers
* Web application security
    * What is an account takeover?
    * How to fight account takeovers?
* Browser hacking
    * Basic browser security
    * Man in the Middle
    * Hacking other tabs in the browser
        * Local storage events
        * Broadcast channels
        * Service worker `postMessage`
        * Window `postMessage`
    * Stealing data from browser local storage, session storage and SQLite databases
    * Stealing browser auto-complete, browsing history, cookies and more
    * Stealing browser stored usernames and passwords
    * Breaking out of the browser to the operating system outside.
    * Fake browser parts by using canvas
    * Client side form-jacking
* Search engines
    * Robots.txt
    * How can search engines be used for hacking?
* Tools
    * F12
    * Burp
    * NMAP
* Web hacking
    * Google hacking
    * 500/fingerprinting hacking
    * X-Forward-For L7 IP spoofing
* Catching hackers
    * What are honey pots and how they are used
    * Various honey pots:
        * robots.txt as honeypot
        * known hacking URLs
        * `chroot` jails
        * containers (`docker` etc)
        * fake applications
* Secure coding
    * code review as a tool for security
    * application logic
    * logic flow
    * parameter specification
    * parameter validation
    * covering all entry points to your application.
    * defensive programming
    * preventing injection
    * The difference between different platforms and languages
    * Security oriented code scanning tools
    * Testing your codes security
* Databases and hacking
    * Basic database security
    * `SQL` injection
    * Stored procedure hacking.
* Denial of Service networking attacks (DOS)
    * L3
        * Ping flood
        * Smurf attack
        * Ping of death
        * Connection flood
        * SYN flood attack
    * L7
        * Basic `HTTP` Floods
        * Randomized `HTTP` Floods
        * Get flood
        * Post Flood
        * Slowloris Attacks
            * Slow Header
            * Slow Body
            * Slow read
        * WordPress `XML`-`RPC` Floods
* Securing large scale web `APIs`
    * Managed `APIs`
        * Swagger
        * `AWS` `API` gateway
        * `GCP` web functions
    * Serverless and applications and web security
    * Managed WAFs
* CDN features
    * Caching
    * Application load balancing
    * Origin shield
    * Network security
    * DDOS protection
    * WAF
    * Rate limiting
    * `SSL` support
    * Certificate support
    * Video and audio streaming support
    * Compression
    * `TCP` multiplexing
    * Anti-spoofing and X-Forwarded-For
* CDN hacking
    * Data Breach
    * DDOS attacks
    * Malware and Virus distribution
    * Domain high-jacking
    * Insider threat
* Standard attack vectors and OWASP
    * OS injection / Shell injection
    * Filesystem attacks
        * Remote File Inclusion (RFI) and Local File Inclusion (LFI)
        * Unrestricted File Download
        * Directory Traversal / File Path Traversal
        * Directory listing
    * Web attacks
        * Open Redirect
        * Bypassing authentication
        * Server Side Request Forgery (SSRF)
            * Routing based
        * Cookies manipulation
        * `HTTP` Host header attacks
        * CSRF
            * How does it work?
            * `JSON` high-jacking
            * `XML` high-jacking
    * `XML` external entity (XXE) injection
    * XSS (Cross-Site-Scripting) and CSP (Content-Security-Policy)
    * X-Frame-Option (click-jacking)
    * Predictable resource location
    * `SSL`-stripping
    * Sensitive Data exposure
    * Broken access control
    * App attacks
        * Deprecated endpoint attack
    * Virtual host brute forcing
    * Null byte injection
    * Connection state attacks
    * Authorization header attacks
    * Broken Object Level Authorization (BOLA) attack
    * Data exposure
    * Mass assignment

## References
* [Google Hacking](https://en.wikipedia.org/wiki/Google_hacking)
* [burp](https://portswigger.net/burp)
* [NMAP](https://nmap.org)
* [Web Development Tools](https://en.wikipedia.org/wiki/Web_development_tools)

## Copyright
Mark Veltzer, © 2026
