---
tags:
  - networking:http
  - networking:protocols
  - networking:web
level: intermediate
category: networking
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
---
<!-- course: http2_and_http3 -->
# `HTTP`/2 and `HTTP`/3

## Description
`HTTP`/2 and `HTTP`/3 represent major evolutions of the web's foundational protocol, addressing performance limitations of `HTTP`/1.1 through binary framing, multiplexing, header compression, and the move to QUIC and `UDP`. This course provides a thorough understanding of both protocols, their performance benefits, server configuration, client support, and practical migration strategies. Participants will learn how these protocols work under the hood and how to take full advantage of them in production environments.

## Duration
16 hours / 1 day

## Intended Audience
* Web developers optimizing application performance
* Backend developers configuring web servers and APIs
* `DevOps` engineers managing web infrastructure
* Network engineers working with web protocols
* Technical leads evaluating protocol migration

## Prerequisites
* `Solid` understanding of `HTTP`/1.1 protocol (methods, headers, status codes)
* Familiarity with `TCP` and `UDP` networking fundamentals
* Basic understanding of `TLS` and `HTTPS`
* Experience with web server configuration (`Nginx`, Apache, or similar)
* Familiarity with browser developer tools

## Required Knowledge
* `Nginx` (or equivalent experience)

## Objectives
* Understand the limitations of `HTTP`/1.1 and the motivations for `HTTP`/2 and `HTTP`/3
* Explain `HTTP`/2 features: binary framing, multiplexing, HPACK header compression, server push, and stream prioritization
* Understand `HTTP`/3 and QUIC: `UDP`-based transport, 0-RTT, and connection migration
* Configure `HTTP`/2 and `HTTP`/3 on popular web servers
* Measure and analyze performance improvements
* Debug protocol-level issues with `Wireshark` and `Chrome DevTools`
* Plan and execute migration from `HTTP`/1.1 to `HTTP`/2 and `HTTP`/3

## Outline
<!-- chapter: http-1-1-limitations, duration: 1h -->
* `HTTP`/1.1 Limitations
    * Head-of-line blocking in `HTTP`/1.1
    * Connection overhead and the cost of multiple `TCP` connections
    * Workarounds: domain sharding, sprite sheets, concatenation, inlining
    * Redundant headers and text-based protocol inefficiency
    * The need for a modern `HTTP` protocol
    * Timeline of `HTTP` evolution: `HTTP`/0.9 to `HTTP`/3
<!-- chapter: http-2-fundamentals, duration: 2h -->
* `HTTP`/2 Fundamentals
    * `HTTP`/2 overview and `RFC 7540`
    * Binary framing layer: frames, messages, and streams
    * Multiplexing: multiple concurrent streams on a single connection
    * Stream prioritization and dependency trees
    * HPACK header compression algorithm
    * Server push: proactively sending resources
    * Connection management and GOAWAY frames
    * `HTTP`/2 and `TLS` (ALPN negotiation)
    * Cleartext `HTTP`/2 (h2c) vs encrypted `HTTP`/2 (h2)
<!-- chapter: http-2-performance-benefits, duration: 1h -->
* `HTTP`/2 Performance Benefits
    * Reduced latency through multiplexing
    * Eliminating domain sharding and concatenation
    * Header compression impact on repeated requests
    * Server push for critical resources
    * Real-world performance measurements and case studies
    * `When` `HTTP`/2 does not help: common misconceptions
    * Optimizing applications for `HTTP`/2
<!-- chapter: http-3-and-quic, duration: 2h -->
* `HTTP`/3 and QUIC
    * Why `HTTP`/3: `TCP` head-of-line blocking at the transport layer
    * QUIC protocol overview: `UDP`-based transport
    * QUIC connection establishment: 0-RTT and 1-RTT handshakes
    * Connection migration across network changes
    * Stream-level flow control and independent streams
    * Built-in encryption with `TLS 1.3`
    * QPACK header compression
    * `HTTP`/3 `RFC 9114` and QUIC `RFC 9000`
<!-- chapter: http-3-vs-http-2-vs-http-1-1, duration: 1h -->
* `HTTP`/3 vs `HTTP`/2 vs `HTTP`/1.1
    * Transport layer differences: `TCP` vs QUIC vs `UDP`
    * Head-of-line blocking comparison across versions
    * Connection setup latency comparison
    * Performance on lossy and high-latency networks
    * Mobile and network-switching scenarios
    * Feature comparison table
    * Choosing the right protocol for your use case
<!-- chapter: tls-1-3-integration, duration: 1h -->
* `TLS 1.3` Integration
    * `TLS 1.3` overview and improvements over `TLS 1.2`
    * Reduced handshake round trips
    * 0-RTT resumption and security considerations
    * `TLS 1.3` as mandatory for `HTTP`/3
    * Certificate and cipher suite configuration
<!-- chapter: server-configuration, duration: 2h -->
* Server Configuration
    * Enabling `HTTP`/2 in `Nginx`
    * Enabling `HTTP`/2 in Apache (mod_http2)
    * Caddy with automatic `HTTP`/2 and `HTTP`/3
    * Enabling `HTTP`/3 with `Nginx` (QUIC module)
    * LiteSpeed and `HTTP`/3 support
    * Load balancer configuration for `HTTP`/2 and `HTTP`/3
    * Backend connection protocols: `HTTP`/2 to origin servers
    * Configuration testing and validation
<!-- chapter: cdn-and-client-support, duration: 1h -->
* CDN and Client Support
    * CDN support for `HTTP`/2 and `HTTP`/3 (Cloudflare, Akamai, Fastly, `AWS CloudFront`)
    * Browser support status for `HTTP`/2 and `HTTP`/3
    * `curl` support for `HTTP`/2 (--http2) and `HTTP`/3 (--http3)
    * Programming language library support
    * Mobile app and native client support
    * Graceful fallback and protocol negotiation
<!-- chapter: debugging-and-analysis, duration: 1h -->
* Debugging and Analysis
    * `Chrome DevTools` protocol column and timing analysis
    * Firefox developer tools for `HTTP`/2 and `HTTP`/3
    * `Wireshark` for `HTTP`/2 frame inspection
    * `Wireshark` QUIC and `HTTP`/3 decryption with SSLKEYLOGFILE
    * nghttp2 tools: nghttp, nghttpd, h2load
    * `curl` verbose output for protocol debugging
    * QUIC connection logging and diagnostics
<!-- chapter: performance-measurement, duration: 2h -->
* Performance Measurement
    * Benchmarking tools: h2load, wrk, hey
    * Measuring time to first byte (TTFB) improvement
    * Page load performance comparison
    * Waterfall analysis with `HTTP`/2 multiplexing
    * Real user monitoring (RUM) metrics
    * Synthetic testing across protocol versions
    * Load testing considerations for `HTTP`/2 and `HTTP`/3
<!-- chapter: migration-considerations, duration: 2h -->
* Migration Considerations
    * Assessing readiness for `HTTP`/2 and `HTTP`/3 migration
    * Enabling `HTTP`/2 without breaking `HTTP`/1.1 clients
    * Gradual rollout strategies
    * Updating application optimization patterns for `HTTP`/2
    * Removing `HTTP`/1.1 workarounds (domain sharding, concatenation)
    * Monitoring and validating after migration
    * Planning for `HTTP`/3 adoption
    * `Firewall` and network considerations for QUIC (`UDP` port 443)

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
