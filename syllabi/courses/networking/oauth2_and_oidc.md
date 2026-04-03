---
tags:
  - networking:security
  - networking:authentication
  - protocols:oauth2
  - protocols:oidc
  - concepts:identity
level: intermediate
category: networking
duration_hours: 16
audience:
  - audiences:developers
  - audiences:architects
  - audiences:security-engineers
---
<!-- course: oauth2_and_oidc -->
# `OAuth2` and `OpenID Connect`

## Description
`OAuth2` and `OpenID Connect` (`OIDC`) are the foundation of modern identity and access management, enabling secure delegated authorization and federated authentication across web, mobile, and service-to-service applications. Together they define how applications obtain access tokens, verify user identity, and integrate with external identity providers such as `Keycloak`, `Auth0`, and `Okta` without handling user credentials directly. This course provides a thorough technical understanding of both specifications, exploring every grant type, token format, and security consideration that practitioners encounter in real-world deployments. Participants will implement and secure `OAuth2` flows, deeply understand `JWT` structure and validation, and learn how to avoid common vulnerabilities and pitfalls that lead to authentication bypasses and privilege escalation.

## Duration
16 hours / 2 days

## Intended Audience
* Backend and full-stack developers building applications that use third-party login, `API` authorization, or service-to-service authentication.
* Software architects designing identity and access management strategies for distributed systems and `microservices`.
* Security engineers performing threat modeling, code review, or penetration testing of `OAuth2`/`OIDC` implementations.

## Prerequisites
* `Solid` understanding of `HTTP`: requests, responses, redirects, cookies, and headers.
* Experience with at least one server-side programming language (`Python`, `Node.js`, `Java`, `Go`).
* Familiarity with `JSON` and basic cryptography concepts (symmetric vs asymmetric encryption) is helpful.
* Basic knowledge of web application security (same-origin policy, `HTTPS`, `CORS`).

## Required Knowledge
* `HTTP` protocol fundamentals
* Web application development experience

## Objectives
* Distinguish between authentication and authorization and understand `when` each is needed
* Explain the `OAuth2` authorization framework: roles, token types, and grant types
* Implement the Authorization Code flow with `PKCE` for web and native applications
* Understand the use cases and security trade-offs of all `OAuth2` grant types
* Differentiate access tokens, refresh tokens, and `ID` tokens and handle them correctly
* Understand the `OpenID Connect` layer and how it adds identity to `OAuth2`
* Decode, validate, and work with `JWT` tokens including signature verification
* Apply security best practices to avoid common `OAuth2` vulnerabilities
* Integrate with real-world identity providers: `Keycloak`, `Auth0`, and `Okta`

## Outline
<!-- chapter: introduction-to-authn-and-authz, duration: 1h -->
* Introduction to Authentication and Authorization
    * Defining authentication (AuthN) and authorization (AuthZ)
    * The problem of delegated access: the password anti-pattern
    * Evolution from `HTTP` Basic Auth to token-based systems
    * The role of identity providers and single sign-on (SSO)
    * Overview of `OAuth2`, `OIDC`, `SAML`, and `LDAP` in the identity landscape
    * Threat model: what can `go` wrong without proper auth standards
<!-- chapter: oauth2-fundamentals, duration: 2h -->
* `OAuth2` Fundamentals
    * `OAuth2` roles: resource owner, client, authorization server, resource server
    * The concept of scopes and delegated permissions
    * `OAuth2` token endpoint and authorization endpoint
    * Client types: confidential vs public clients
    * Client credentials and registration
    * The `OAuth2` token response structure
    * Bearer tokens and how resource servers validate them
    * Token introspection endpoint (`RFC 7662`)
<!-- chapter: authorization-code-flow, duration: 2h -->
* Authorization Code Flow
    * Step-by-step walkthrough of the Authorization Code grant
    * The authorization request: `response_type`, `client_id`, `redirect_uri`, `scope`, `state`
    * The authorization code exchange for tokens
    * The `state` parameter and `CSRF` protection
    * `PKCE` (Proof Key for Code Exchange): motivation and implementation
    * Silent token refresh using `prompt=none` and iframes
    * Implementing Authorization Code with `PKCE` for SPAs and mobile apps
    * Hands-on: building a complete Authorization Code flow
<!-- chapter: other-grant-types, duration: 2h -->
* Other Grant Types
    * Client Credentials grant for machine-to-machine authorization
    * Resource Owner Password Credentials grant: use cases and why to avoid it
    * Device Authorization grant (`RFC 8628`) for `CLI` tools and `IoT`
    * Token Exchange (`RFC 8693`) for service impersonation and delegation
    * Refresh Token grant: obtaining new access tokens without user interaction
    * Choosing the right grant type for different application scenarios
<!-- chapter: token-types, duration: 2h -->
* Token Types: Access, Refresh, and `ID` Tokens
    * Access token: purpose, lifetime, and storage best practices
    * Opaque tokens vs `JWT`-formatted access tokens
    * Token scopes and audience (`aud`) claim validation
    * Refresh token: rotation, absolute expiry, and revocation
    * `ID` token: what it represents and how it differs from access tokens
    * Token storage: secure cookies vs in-memory vs `localStorage` trade-offs
    * Token revocation endpoint (`RFC 7009`)
<!-- chapter: openid-connect, duration: 2h -->
* `OpenID Connect` (`OIDC`)
    * How `OIDC` extends `OAuth2` for authentication
    * The `openid` scope and `ID` token issuance
    * Standard `OIDC` claims: `sub`, `iss`, `aud`, `exp`, `iat`, `nonce`
    * The `nonce` parameter and replay attack prevention
    * `OIDC` Discovery document and `JWKS` endpoint
    * UserInfo endpoint for additional claims
    * `OIDC` hybrid flow and implicit flow (legacy)
    * Single Log-Out (`SLO`): front-channel and back-channel logout
<!-- chapter: jwt-deep-dive, duration: 2h -->
* `JWT` Deep Dive
    * `JWT` structure: header, payload, and signature
    * Signing algorithms: `RS256`, `ES256`, `HS256` — trade-offs and recommendations
    * Validating a `JWT`: signature, issuer, audience, expiry
    * The `JWKS` endpoint and key rotation
    * `JWE` (`JSON` Web Encryption) for encrypted tokens
    * Common `JWT` vulnerabilities: `alg:none`, key confusion attacks, weak secrets
    * Libraries and tooling for `JWT` across languages
<!-- chapter: implementing-oauth2-securely, duration: 2h -->
* Implementing `OAuth2` Securely
    * `OAuth2` Security Best Current Practice (`RFC 9700`)
    * Redirect URI validation and open redirect vulnerabilities
    * Authorization Code injection attacks and `PKCE` mitigation
    * `CSRF` protection for server-side applications
    * Token leakage via `Referer` headers and browser history
    * `CORS` configuration for token endpoints
    * Threat modeling an `OAuth2` deployment
    * Security checklist for `OAuth2` and `OIDC` implementations
<!-- chapter: oauth2-in-practice, duration: 1h -->
* `OAuth2` in Practice: `Keycloak`, `Auth0`, and `Okta`
    * Setting up `Keycloak` as an open-source identity provider
    * Configuring realms, clients, and scopes in `Keycloak`
    * `Auth0` tenant configuration and application types
    * `Okta` developer setup and `OIDC` application registration
    * Comparing capabilities, pricing, and operational complexity
    * Federated identity: connecting identity providers together

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
