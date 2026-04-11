---
tags:
  - tools:nginx
  - networking:web
  - practices:performance
level: intermediate
category: devops
duration_hours: 24
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
  - audiences:security-professionals
---
<!-- course: nginx -->
# `Nginx`

## Description
This course provides comprehensive training on `Nginx`, one of the most widely used web
servers and reverse proxies. Students will learn how to configure `Nginx` for serving static
content, reverse proxying, load balancing, `SSL`/`TLS` termination, and `API gateway` use cases.

The course covers `Nginx` architecture, configuration best practices, performance tuning,
and security hardening. Students will gain hands-on experience with real-world deployment
scenarios and learn how to monitor and troubleshoot `Nginx` in production environments.

## Duration
24 hours / 2 days

## Intended Audience
* Developers, system administrators, and `DevOps` engineers who deploy and manage web applications and APIs.
* Teams looking to improve the performance, security, and reliability of their web infrastructure.

## Prerequisites
* Basic understanding of `HTTP` protocol and web server concepts.
* Familiarity with `Linux` command-line administration.
* Basic understanding of networking concepts (`DNS`, `TCP`/`IP`, `TLS`).

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Understand `Nginx` architecture and its event-driven model.
* Configure `Nginx` for serving static content and virtual hosting.
* Set up reverse proxy and load balancing configurations.
* Implement `SSL`/`TLS` termination and security hardening.
* Use `Nginx` as an `API gateway`.
* Tune `Nginx` for high-performance production workloads.

## Outline
<!-- chapter: nginx-architecture, duration: 1h -->
* `Nginx` Architecture
    * `Event-driven architecture` overview
    * Master and worker processes
    * Connection handling model
    * Comparison with `Apache` and `HAProxy`
    * `Nginx` vs `Nginx` Plus
<!-- chapter: installation-and-configuration, duration: 1h -->
* Installation and Configuration
    * Installing from packages and source
    * Configuration `file` structure
    * Main, events, and `http` contexts
    * Include directives and modular configuration
    * Configuration testing and reloading
<!-- chapter: serving-static-content, duration: 2h -->
* Serving Static Content
    * Root and alias directives
    * Index files and directory listings
    * MIME types and content negotiation
    * Gzip compression
    * Sendfile and direct `I/O`
    * Byte-range requests
<!-- chapter: virtual-hosts-server-blocks, duration: 1h -->
* Virtual Hosts (Server Blocks)
    * Server block configuration
    * Name-based virtual hosting
    * `IP`-based virtual hosting
    * Default server behavior
    * Server name matching rules
<!-- chapter: reverse-proxy-configuration, duration: 2h -->
* Reverse Proxy Configuration
    * proxy_pass directive
    * Upstream configuration
    * Proxy headers and X-Forwarded-For
    * Buffering and timeouts
    * `WebSocket` proxying
    * `gRPC` proxying
<!-- chapter: load-balancing, duration: 2h -->
* Load Balancing
    * Round-robin distribution
    * Least connections method
    * `IP` hash method
    * Weighted load balancing
    * Health checks (passive and active)
    * Session persistence
    * Upstream failure handling
<!-- chapter: ssl-tls-termination, duration: 2h -->
* `SSL`/`TLS` Termination
    * Certificate and key configuration
    * `SSL` protocols and cipher suites
    * `OCSP` stapling
    * `SSL` session caching
    * `HTTP` to `HTTPS` redirection
    * Client certificate authentication
<!-- chapter: http-2-and-http-3, duration: 1h -->
* `HTTP`/2 and `HTTP`/3
    * Enabling `HTTP`/2
    * `HTTP`/2 push (deprecated considerations)
    * `HTTP`/3 and QUIC support
    * Protocol negotiation
<!-- chapter: caching, duration: 1h -->
* Caching
    * Proxy cache configuration
    * Cache key and zone setup
    * Cache purging
    * Cache bypass and conditional caching
    * Microcaching strategies
<!-- chapter: rate-limiting, duration: 1h -->
* Rate Limiting
    * limit_req module
    * limit_conn module
    * Burst handling
    * Rate limiting by different keys
    * Custom error responses for limited requests
<!-- chapter: access-control, duration: 1h -->
* Access Control
    * `IP`-based allow/deny rules
    * Basic authentication
    * Subrequest authentication
    * GeoIP-based access control
<!-- chapter: logging, duration: 1h -->
* Logging
    * Access log configuration
    * Error log levels
    * Custom log formats
    * Conditional logging
    * Log rotation
<!-- chapter: rewrite-rules, duration: 1h -->
* Rewrite Rules
    * rewrite directive
    * return directive
    * try_files directive
    * Regular expressions in locations
    * Map directive for variable mapping
<!-- chapter: security-headers, duration: 2h -->
* Security Headers
    * Content Security Policy
    * X-Frame-Options
    * X-Content-Type-Options
    * Strict-Transport-Security
    * Referrer-Policy
    * Permissions-Policy
<!-- chapter: nginx-as-api-gateway, duration: 2h -->
* `Nginx` as `API Gateway`
    * `API` routing configuration
    * Rate limiting per `API` endpoint
    * Request and response transformation
    * `API` versioning with `Nginx`
    * `JWT` validation
    * CORS configuration
<!-- chapter: performance-tuning, duration: 2h -->
* Performance Tuning
    * Worker process and connection tuning
    * Buffer sizes optimization
    * Keepalive connections
    * Open `file` cache
    * Kernel parameter tuning
    * Benchmarking with wrk and ab
<!-- chapter: monitoring, duration: 1h -->
* Monitoring
    * Stub status module
    * Logging-based monitoring
    * Integration with `Prometheus` and `Grafana`
    * Error tracking and alerting

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
