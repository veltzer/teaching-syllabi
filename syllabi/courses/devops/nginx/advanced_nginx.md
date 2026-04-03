---
tags:
  - tools:nginx
  - practices:devops
  - networking:web
  - practices:performance
level: advanced
category: devops
duration_hours: 16
audience:
  - audiences:devops
  - audiences:sres
  - audiences:sysadmins
---
<!-- course: advanced_nginx -->
# Advanced `Nginx`

## Description
This course covers advanced `Nginx` topics for experienced engineers who want to master `Nginx` as a high-performance reverse proxy, load balancer, and web server. Topics include reverse proxy configuration, load balancing algorithms, caching strategies, rate limiting, `SSL/TLS` termination, Lua scripting with OpenResty, performance tuning, and high availability setups. Students will gain the skills needed to architect and manage production-grade `Nginx` deployments.

## Duration
16 hours / 2 days

## Intended Audience
* `DevOps` engineers and site reliability engineers
* System administrators managing web infrastructure
* Backend engineers responsible for deployment and scaling

## Prerequisites
* Basic experience with `Nginx` configuration and operation.
* Familiarity with `Linux` system administration.
* Understanding of `HTTP`/`HTTPS` protocols and networking fundamentals.

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Configure `Nginx` as a reverse proxy for complex application architectures.
* Implement and tune load balancing algorithms for different workloads.
* Design and deploy caching strategies to improve application performance.
* Set up rate limiting and request throttling to protect backend services.
* Configure `SSL/TLS` termination and hardened security settings.
* Extend `Nginx` functionality using Lua scripting with OpenResty.
* Tune `Nginx` for high performance under heavy traffic loads.
* Architect high availability `Nginx` deployments.

## Outline
<!-- chapter: reverse-proxy-configuration, duration: 2h -->
* Reverse Proxy Configuration:
    * Proxy pass directives and upstream blocks.
    * Header manipulation and request rewriting.
    * `WebSocket` proxying.
    * Buffering and timeout configuration.
<!-- chapter: load-balancing-algorithms, duration: 2h -->
* Load Balancing Algorithms:
    * Round-robin, least connections, and `IP` hash.
    * Weighted load balancing.
    * Health checks and failover strategies.
    * Session persistence and sticky sessions.
<!-- chapter: caching-strategies, duration: 2h -->
* Caching Strategies:
    * Proxy cache configuration.
    * Cache keys and cache zones.
    * Cache invalidation and purging.
    * Microcaching for dynamic content.
<!-- chapter: rate-limiting, duration: 2h -->
* Rate Limiting:
    * Request rate limiting with limit_req.
    * Connection limiting with limit_conn.
    * Burst handling and delay configuration.
    * Per-client and per-URI rate limiting.
<!-- chapter: ssl-tls-termination, duration: 2h -->
* `SSL/TLS` Termination:
    * Certificate management and configuration.
    * `TLS` protocol and cipher suite selection.
    * OCSP stapling and session resumption.
    * `HTTP`/2 and `HTTP`/3 configuration.
<!-- chapter: lua-scripting-with-openresty, duration: 2h -->
* Lua Scripting with OpenResty:
    * Introduction to OpenResty and the Lua module.
    * Request and response manipulation with Lua.
    * Accessing external services from Lua.
    * Authentication and authorization logic.
<!-- chapter: performance-tuning, duration: 2h -->
* Performance Tuning:
    * Worker processes and connection handling.
    * Buffer sizes and timeout optimization.
    * `File` `I/O` and sendfile configuration.
    * Monitoring and profiling `Nginx` performance.
<!-- chapter: high-availability, duration: 2h -->
* High Availability:
    * Active-passive and active-active configurations.
    * Keepalived and virtual `IP` failover.
    * Configuration management and deployment strategies.
    * Logging, monitoring, and alerting.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
