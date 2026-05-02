---
tags:
  - networking:web
  - practices:devops
  - networking:http
  - practices:sysadmin
level: intermediate
category: devops
duration_hours: 16
audience:
  - audiences:sysadmins
  - audiences:devops
  - audiences:developers
---
<!-- course: apache_http_server -->
# Apache `HTTP` Server

## Description
This course covers the installation, configuration, and administration of the Apache `HTTP` Server, one of the most widely deployed web servers in the world. Participants will learn how to configure virtual hosts, manage modules, set up `SSL/TLS`, implement reverse proxying, and tune performance. The course also addresses security hardening and operational best practices for running Apache in production environments.

## Duration
16 hours / 1 day

## Intended Audience
* System administrators managing web server infrastructure.
* `DevOps` engineers deploying and maintaining web applications.
* Developers who need to configure and troubleshoot Apache for their applications.

## Prerequisites
* Basic `Linux` system administration skills.
* Familiarity with `HTTP` fundamentals (request/response, status codes, headers).
* Comfort working with the command line and text editors.

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Install and configure Apache `HTTP` Server on `Linux`.
* Understand the structure of httpd.conf and related configuration files.
* Configure name-based and `IP`-based virtual hosts.
* Enable and configure commonly used modules (mod_rewrite, mod_ssl, mod_proxy, mod_security).
* Use .htaccess files for directory-level configuration.
* Write URL rewriting rules with mod_rewrite.
* Set up `SSL/TLS` certificates for secure connections.
* Configure Apache as a reverse proxy.
* Tune Apache performance using MPM workers and caching strategies.
* Implement security hardening measures.
* Configure and analyze Apache access and error logs.

## Outline
<!-- chapter: installation-and-basic-configuration, duration: 1h -->
* Installation and Basic Configuration
    * Installing Apache on major `Linux` distributions
    * Starting, stopping, and restarting the service
    * Directory layout and default configuration
<!-- chapter: httpd-conf-structure, duration: 1h -->
* httpd.conf Structure
    * Global settings, directives, and contexts
    * Server-level vs. directory-level configuration
    * Include and IncludeOptional directives
    * Configuration syntax and best practices
<!-- chapter: virtual-hosts, duration: 1h -->
* Virtual Hosts
    * Name-based virtual hosts
    * `IP`-based virtual hosts
    * Default virtual host and catch-all configuration
    * Managing multiple sites
<!-- chapter: apache-modules, duration: 2h -->
* Apache Modules
    * Module architecture and loading modules
    * mod_rewrite for URL manipulation
    * mod_ssl for `TLS` termination
    * mod_proxy for reverse proxying and load balancing
    * mod_security for web application `firewall` capabilities
    * Other useful modules
<!-- chapter: htaccess-files, duration: 1h -->
* .htaccess Files
    * Use cases and limitations
    * AllowOverride directives
    * Performance implications
    * Migrating .htaccess rules to main configuration
<!-- chapter: url-rewriting, duration: 1h -->
* URL Rewriting
    * RewriteRule and RewriteCond syntax
    * Common rewriting patterns (redirects, `clean` URLs, forced `HTTPS`)
    * Debugging rewrite rules with RewriteLog
<!-- chapter: ssl-tls-configuration, duration: 1h -->
* `SSL/TLS` Configuration
    * Obtaining and installing certificates
    * Configuring SSLCertificateFile and SSLCertificateKeyFile
    * Cipher suite selection and protocol versions
    * `HSTS` and `OCSP` stapling
<!-- chapter: reverse-proxy, duration: 2h -->
* Reverse Proxy
    * ProxyPass and ProxyPassReverse directives
    * Load balancing with mod_proxy_balancer
    * `WebSocket` proxying
    * Proxy timeouts and connection pooling
<!-- chapter: performance-tuning, duration: 2h -->
* Performance Tuning
    * MPM models (prefork, worker, event)
    * Choosing and configuring the right MPM
    * Caching strategies (mod_cache, mod_expires)
    * KeepAlive settings and connection management
    * Compression with mod_deflate
<!-- chapter: logging, duration: 2h -->
* Logging
    * Access log formats and CustomLog directives
    * Error log levels and ErrorLog configuration
    * Log rotation with `logrotate`
    * Analyzing logs for troubleshooting
<!-- chapter: security-hardening, duration: 2h -->
* Security Hardening
    * Hiding server version and signature
    * Restricting directory listings and access
    * Preventing clickjacking, `XSS`, and MIME-sniffing
    * Rate limiting and connection limits
    * Security headers (Content-Security-Policy, X-Frame-Options)

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
