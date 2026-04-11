---
tags:
  - security:security
  - security:authentication
  - concepts:api
  - networking:web
level: intermediate
category: security
duration_hours: 16
audience:
  - audiences:developers
  - audiences:architects
  - audiences:security-professionals
---
<!-- course: api_security -->
# `API` Security

## Description
This course provides comprehensive coverage of `API` security principles, protocols, and best practices. Participants will gain deep understanding of `OAuth 2.0` grant types, `OpenID Connect`, and `JWT` security considerations. The course also addresses `API` key management, rate limiting, the `OWASP` `API` Security `Top` 10, input validation, CORS, `CSRF` protection for APIs, `API gateway` security, and mutual `TLS` authentication.

## Duration
16 hours / 2 days

## Intended Audience
* Backend developers building and securing APIs
* Software architects designing authentication and authorization systems
* Security professionals assessing `API` security posture
* Engineers responsible for `API gateway` configuration and management
* Development teams adopting `OAuth 2.0` and `OpenID Connect`

## Prerequisites
* Experience with building or consuming `REST` APIs
* Basic understanding of `HTTP` protocol and web security concepts
* Familiarity with `JSON` and common web development patterns

## Objectives
* Implement `OAuth 2.0` flows for various application types using the appropriate grant types
* Configure `OpenID Connect` for federated identity and single sign-on
* Apply `JWT` best practices for signing, encryption, and claims management
* Design and implement `API` key management strategies
* Protect APIs against the `OWASP` `API` Security `Top` 10 threats
* Implement rate limiting, throttling, and abuse prevention mechanisms
* Configure CORS policies and `CSRF` protection for APIs
* Secure `API` gateways and implement mutual `TLS`

## Outline
<!-- chapter: api-security-fundamentals, duration: 1h -->
* `API` Security Fundamentals
    * The `API` threat landscape
    * Authentication vs authorization in `API` contexts
    * Transport layer security for APIs
    * `API` security architecture patterns
    * Defense in depth for APIs
<!-- chapter: oauth-2-0-deep-dive, duration: 2h -->
* `OAuth 2.0` Deep Dive
    * `OAuth 2.0` architecture and roles
    * Authorization code grant with `PKCE`
    * Client credentials grant for service-to-service communication
    * Resource owner password credentials grant (and why to avoid it)
    * Device authorization grant
    * Token introspection and revocation
    * Scopes and fine-grained permissions
    * `OAuth 2.0` security considerations and common vulnerabilities
    * Token storage and lifecycle management
<!-- chapter: openid-connect, duration: 2h -->
* `OpenID Connect`
    * `OpenID Connect` layered on `OAuth 2.0`
    * `ID` tokens and user info endpoint
    * Discovery and dynamic client registration
    * Session management and logout
    * Claims and claim types
    * `OpenID Connect` flows for web, mobile, and single-page applications
    * Federated identity and identity provider selection
<!-- chapter: jwt-best-practices, duration: 2h -->
* `JWT` Best Practices
    * `JWT` structure: header, payload, and signature
    * Signing algorithms: `HMAC`, `RSA`, and `ECDSA`
    * JWE (`JSON` Web Encryption) for confidential claims
    * Claims best practices: iss, aud, exp, nbf, iat, and custom claims
    * Token size considerations and claim minimization
    * `JWT` validation checklist
    * Common `JWT` vulnerabilities: algorithm confusion, key leakage, and none algorithm attacks
    * Refresh token rotation and token families
<!-- chapter: api-keys-management, duration: 1h -->
* `API` Keys Management
    * `API` key generation and entropy
    * Key rotation strategies
    * Key scoping and permissions
    * Secure key storage and transmission
    * `API` key vs `OAuth` token: choosing the right approach
    * Key revocation and auditing
<!-- chapter: rate-limiting-and-throttling, duration: 1h -->
* Rate Limiting and Throttling
    * Rate limiting algorithms: token bucket, leaky bucket, fixed window, sliding window
    * Per-client, per-endpoint, and global rate limits
    * Rate limit headers and client communication
    * Distributed rate limiting across multiple `API` instances
    * Throttling vs rate limiting vs quotas
    * Abuse detection and adaptive rate limiting
<!-- chapter: owasp-api-security-top-10, duration: 2h -->
* `OWASP` `API` Security `Top` 10
    * Broken object-level authorization (BOLA)
    * Broken authentication
    * Broken object property-level authorization
    * Unrestricted resource consumption
    * Broken function-level authorization
    * Unrestricted access to sensitive business flows
    * Server-side request forgery (SSRF)
    * Security misconfiguration
    * Improper inventory management
    * Unsafe consumption of APIs
    * Mitigation strategies for each category
<!-- chapter: input-validation, duration: 1h -->
* Input Validation
    * Input validation strategies for APIs
    * Schema validation with `JSON Schema` and `OpenAPI`
    * Content type validation and enforcement
    * Parameter pollution and injection prevention
    * `File` upload security
    * Request size limits and payload validation
<!-- chapter: cors-and-csrf-for-apis, duration: 1h -->
* CORS and `CSRF` for APIs
    * CORS mechanism and preflight requests
    * Configuring CORS policies: origins, methods, headers, and credentials
    * Common CORS misconfigurations and their security impact
    * `CSRF` attack vectors against APIs
    * `CSRF` protection techniques: tokens, SameSite cookies, and custom headers
    * CORS and `CSRF` in single-page application architectures
<!-- chapter: api-gateway-security, duration: 1h -->
* `API Gateway` Security
    * `API gateway` as a security enforcement point
    * Authentication and authorization at the gateway
    * Request transformation and validation
    * Logging, monitoring, and anomaly detection
    * Web application `firewall` integration
    * Gateway high availability and failover
<!-- chapter: mutual-tls-mtls, duration: 2h -->
* Mutual `TLS` (mTLS)
    * `TLS` fundamentals and certificate-based authentication
    * mTLS handshake and certificate verification
    * Certificate management: issuance, rotation, and revocation
    * mTLS in service-to-service communication
    * Certificate pinning and trust store management
    * mTLS with `API` gateways and service meshes

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
