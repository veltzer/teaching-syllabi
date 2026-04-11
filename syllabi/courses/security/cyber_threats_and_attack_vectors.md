---
tags:
  - security:security
  - security:cyber-threats
  - security:web-security
  - security:penetration-testing
level: intermediate
category: security
duration_hours_short: 24
duration_hours_long: 48
audience:
  - audiences:security-professionals
  - audiences:developers
duration_hours: 56
---
<!-- course: cyber_threats_and_attack_vectors -->
# Cyber Threats and Attack Vectors

## Description
This course surveys and demonstrates many of the prevalent attack threats, methods and vectors used by today's
hackers. The course starts with introductory material that is needed to understand the technical aspects of
the following chapters and then goes into the various attack vectors. Each attack method is explained, analyzed
and demonstrated.

## Duration
* Short: 24 hours / 3 days
* Long: 48 hours / 6 days

## Intended Audience
* Anyone who wishes to understand the current security landscape of threats and attack vectors.

## Prerequisites
* Tech affinity
* Programming background is not required but may add to participants understanding

## Objectives
* understand the core concepts and principles of Cyber Threats and Attack Vectors
* gain practical knowledge of Hacking landscape overview
* gain practical knowledge of Basic OS security
* gain practical knowledge of Networking background

## Outline
<!-- chapter: hacking-landscape-overview, duration: 5h -->
* Hacking landscape overview
    * Who are the hackers?
    * What are the hackers motivations?
    * What are the hackers goals?
    * What are the hackers targets?
        * Data theft [long]
        * Password theft [long]
        * Credit card data [long]
        * `DNS` [long]
        * Client takeover [long]
        * CDN [long]
        * `Firewall` [long]
        * Load Balancer [long]
        * Application (regular and mobile) [long]
        * Web server [long]
        * Operating system [long]
        * Database [long]
    * Attack life-cycle
    * Forensics introduction
<!-- chapter: basic-os-security, duration: 1h -->
* Basic OS security
    * Admin/root vs regular user
    * Password hashing
    * Reverse hashing
    * `sudo` and other tools.
    * Containers and security (e.g. `docker`)
<!-- chapter: injections, duration: 1h -->
* Injections
    * `SQL` Injection
    * Shell injection
<!-- chapter: networking-background-long, duration: 2h -->
* Networking background [long]
    * `IP` addresses
    * Geo `IP`, ISP, ASN, `CIDR`
    * Routers
    * Firewalls
    * Base 64
    * URL encoding
    * `NAT`
    * `SSL` (symmetric and asymmetric encryption)
<!-- chapter: dns-background-long, duration: 2h -->
* `DNS` background [long]
    * The protocol and it's versions
    * The `DNS` network
    * Why is `DNS` important for security?
    * The types of `DNS` servers
        * Recursive resolvers
        * root name-servers
        * TLD name-servers
        * authoritative name-servers
<!-- chapter: dns-hacking, duration: 1h -->
* `DNS` hacking
    * Zero-Day-Attack
    * Cache Poisoning
    * `DNS` Denial of Service
    * `DNS` Distributed Denial of Service
    * `DNS` Amplification
    * Fast-`Flux` `DNS`
<!-- chapter: web-http-background-long, duration: 5h -->
* Web/`HTTP` background [long]
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
    * `HSTS`
    * `HTTP` Error codes
    * Local Storage/Session storage
    * Robots.txt
    * CDN
    * Proxies and caching.
    * TOR
    * X-Forward-For
    * Certificates for server and client (symmetric and non symmetric)
    * CORS
<!-- chapter: web-server-security-long, duration: 1h -->
* Web server security [long]
    * `SSL`
    * `SSL` Certificates
    * Access control lists (`ACLs`)
    * X-Forwarded-For security
<!-- chapter: web-application-authentication-methods-long, duration: 3h -->
* Web application authentication methods [long]
    * Basic Auth
    * Cookies and cookie expiration
    * `HTTP` only cookies
    * Signed cookies
    * `JWT` and `JWT` validation
    * Signing requests and validating them.
    * One time passwords
    * Certificate based authentication
    * Bio-metric authentication
    * Multi-factor authentication
    * `oauth` and `oauth2`
    * Captcha
<!-- chapter: hacking-web-applications, duration: 2h -->
* Hacking Web applications
    * Tools to brute-force web forms and applications
    * What is broken authentication
    * Using mechanical Turks and `AI` to break Captcha and other mechanisms.
    * What is form-jacking?
    * What is denial of inventory?
    * Hacking New Gen Bots
    * Data scraping
    * Hacking headless browsers [long]
<!-- chapter: web-application-security-long, duration: 1h -->
* Web application security [long]
    * What is an account takeover?
    * How to fight account takeovers?
<!-- chapter: browser-hacking, duration: 4h -->
* Browser hacking
    * Man in the Middle
    * Local store attack
    * Basic browser security [long]
    * Hacking other tabs in the browser [long]
        * Local storage events [long]
        * Broadcast channels [long]
        * Service worker postMessage [long]
        * Window postMessage [long]
    * Stealing data from browser local storage, session storage and `SQLite` databases [long]
    * Stealing browser auto-complete, browsing history, cookies and more [long]
    * Stealing browser stored usernames and passwords [long]
    * Breaking out of the browser to the operating system outside. [long]
    * Fake browser parts by using canvas [long]
    * Client side form-jacking [long]
<!-- chapter: search-engines-long, duration: 1h -->
* Search engines [long]
    * Robots.txt
    * How can search engines be used for hacking?
<!-- chapter: tools, duration: 1h -->
* Tools
    * F12 [long]
    * Burp [long]
    * `NMAP`
<!-- chapter: web-hacking, duration: 1h -->
* Web hacking
    * Google hacking
    * `500`/fingerprinting hacking
    * X-Forward-For L7 `IP` spoofing
<!-- chapter: catching-hackers, duration: 2h -->
* Catching hackers
    * What are honey pots and how they are used
    * Various honey pots: [long]
        * robots.txt as honeypot [long]
        * known hacking URLs [long]
        * chroot jails [long]
        * containers (`docker` etc) [long]
        * fake applications [long]
<!-- chapter: secure-coding-long, duration: 3h -->
* Secure coding [long]
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
<!-- chapter: databases-and-hacking-long, duration: 1h -->
* Databases and hacking [long]
    * Basic database security
    * `SQL` injection
    * Stored procedure hacking.
<!-- chapter: denial-of-service-networking-attacks-dos, duration: 4h -->
* Denial of Service networking attacks (DOS)
    * L3
        * `Ping` flood
        * Smurf attack
        * `Ping` of death
        * Connection flood
        * SYN flood attack
    * L7
        * Basic `HTTP` Floods (Get, POST, Randomized)
        * Slowloris Attacks
            * Slow Header [long]
            * Slow Body [long]
            * Slow read [long]
        * WordPress `XML`-RPC Floods [long]
<!-- chapter: securing-large-scale-web-apis-long, duration: 2h -->
* Securing large scale web APIs [long]
    * Managed APIs
        * Swagger
        * `AWS` `API` gateway
        * `GCP` web functions
    * Serverless and applications and web security
    * Managed WAFs
<!-- chapter: cdn-features-long, duration: 3h -->
* CDN features [long]
    * Caching
    * Application load balancing
    * Origin shield
    * Network security
    * `DDOS` protection
    * `WAF`
    * Rate limiting
    * `SSL` support
    * Certificate support
    * Video and audio streaming support
    * Compression
    * `TCP` multiplexing
    * Anti-spoofing and X-Forwarded-For
<!-- chapter: cdn-hacking, duration: 1h -->
* CDN hacking
    * Data Breach [long]
    * `DDOS` attacks [long]
    * Malware and Virus distribution [long]
    * Domain high-jacking
    * Insider threat
<!-- chapter: standard-attack-vectors-and-owasp-long, duration: 9h -->
* Standard attack vectors and `OWASP` [long]
    * OS injection / Shell injection
    * Filesystem attacks
        * Remote `File` Inclusion (RFI) and Local `File` Inclusion (LFI)
        * Unrestricted `File` Download
        * Directory Traversal / `File` Path Traversal
        * Directory listing
    * Web attacks
        * Open Redirect
        * Bypassing authentication
        * Server Side Request Forgery (SSRF)
            * Routing based
        * Cookies manipulation
        * `HTTP` Host header attacks
        * `CSRF`
            * How does it work?
            * `JSON` high-jacking
            * `XML` high-jacking
    * `XML` external entity (XXE) injection
    * `XSS` (Cross-Site-Scripting) and CSP (Content-Security-Policy)
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
* [Google Hacking](`https`://en.wikipedia.org/wiki/Google_hacking)
* [burp](`https`://portswigger.net/burp)
* [`NMAP`](`https`://`nmap`.org)
* [Web Development Tools](`https`://en.wikipedia.org/wiki/Web_development_tools)

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
