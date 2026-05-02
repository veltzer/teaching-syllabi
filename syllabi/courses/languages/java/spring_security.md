---
tags:
  - languages:java
  - tools:spring
  - tools:spring-security
  - concepts:security
  - concepts:web-development
level: intermediate
category: language
duration_hours: 16
audience:
  - audiences:developers
  - audiences:architects
  - audiences:security-professionals
---
<!-- course: spring_security -->
# `Spring Security`

## Description
This course provides an in-depth exploration of `Spring Security` for building secure `Java` applications. Covering authentication and authorization mechanisms, `OAuth2` and `OpenID Connect` integration, `JWT`-based stateless authentication, method-level security, and protection against common web vulnerabilities, the course equips developers with the knowledge to implement robust security in `Spring Boot` applications.

## Duration
16 hours / 2 days

## Intended Audience
* `Java` developers building secure backend applications
* `Spring Boot` developers who need to implement authentication and authorization
* Software engineers responsible for application security
* Backend developers integrating with identity providers and `OAuth2` services
* Architects designing secure `microservices` architectures

## Prerequisites
* Intermediate proficiency in `Java` programming (classes, interfaces, annotations)
* Working knowledge of `Spring Boot` and the Spring ecosystem
* Understanding of `HTTP` protocol, `REST API` concepts, and web application architecture
* Basic familiarity with relational databases and `SQL`
* Awareness of common web security concepts (authentication vs. authorization)
* Experience with an IDE such as `IntelliJ IDEA` or Eclipse

## Objectives
* Understand the `Spring Security` architecture, filter chain, and request processing pipeline
* Implement authentication using in-memory, database-backed, and custom authentication providers
* Configure role-based and permission-based authorization at URL and method levels
* Integrate `OAuth2` and `OpenID Connect` for delegated authentication with external identity providers
* Implement `JWT`-based stateless authentication for `REST APIs`
* Apply method-level security with @PreAuthorize, @PostAuthorize, and @Secured annotations
* Configure CORS policies and `CSRF` protection for web applications
* Customize security filters and build custom authentication mechanisms

## Outline
<!-- chapter: spring-security-architecture, duration: 2h -->
* `Spring Security` Architecture
    * Overview of `Spring Security` and its role in the Spring ecosystem
    * The security filter chain and how requests are processed
    * SecurityContext and the Authentication object
    * SecurityFilterChain bean configuration
    * Auto-configuration in `Spring Boot`
    * Debugging and logging security events
<!-- chapter: authentication, duration: 2h -->
* Authentication
    * Authentication providers and the AuthenticationManager
    * In-memory user details configuration
    * Database-backed authentication with UserDetailsService
    * Password encoding with BCrypt, SCrypt, and Argon2
    * Custom authentication providers
    * Authentication events and listeners
    * Remember-me authentication
    * Multi-factor authentication strategies
<!-- chapter: authorization, duration: 2h -->
* Authorization
    * Role-based access control (`RBAC`)
    * URL-based authorization with request matchers
    * Authority vs. role distinction in `Spring Security`
    * Hierarchical roles
    * Access decision managers and voters
    * Expression-based access control
    * Dynamic authorization with custom logic
<!-- chapter: method-level-security, duration: 2h -->
* Method-Level Security
    * Enabling method security with @EnableMethodSecurity
    * @PreAuthorize and @PostAuthorize annotations
    * @Secured and @RolesAllowed annotations
    * @PreFilter and @PostFilter for collection filtering
    * Custom security expressions
    * Method security with SpEL (Spring Expression Language)
<!-- chapter: oauth2-and-openid-connect, duration: 2h -->
* `OAuth2` and `OpenID Connect`
    * Introduction to `OAuth2` flows and grant types
    * `OpenID Connect` concepts and `ID` tokens
    * Configuring `Spring Security` as an `OAuth2` client
    * Integration with identity providers (Google, `GitHub`, `Keycloak`, `Okta`)
    * `OAuth2` login and user info mapping
    * `OAuth2` resource server configuration
    * Token relay in `microservices`
    * Customizing the `OAuth2` login flow
<!-- chapter: jwt-authentication, duration: 2h -->
* `JWT` Authentication
    * Introduction to `JSON Web Tokens` and their structure
    * `JWT` generation, signing, and validation
    * Configuring `Spring Security` as a `JWT`-based resource server
    * Symmetric vs. asymmetric key signing
    * Token expiration, refresh tokens, and revocation strategies
    * Custom claims and authorities extraction
    * Stateless session management with `JWT`
<!-- chapter: cors-and-csrf-protection, duration: 2h -->
* CORS and `CSRF` Protection
    * Understanding `Cross-Origin Resource Sharing` (CORS)
    * Configuring CORS policies in `Spring Security`
    * Global and per-endpoint CORS configuration
    * Understanding `Cross-Site Request Forgery` (`CSRF`)
    * `CSRF` token handling in traditional and SPA applications
    * `When` to disable `CSRF` protection
    * SameSite cookie attribute and its security implications
<!-- chapter: security-filters-and-customization, duration: 2h -->
* Security Filters and Customization
    * The `Spring Security` filter chain in detail
    * Adding custom filters to the security chain
    * Filter ordering and registration
    * Custom AuthenticationEntryPoint and AccessDeniedHandler
    * Security headers configuration (X-Frame-Options, CSP, `HSTS`)
    * Session management and concurrency control
    * Security best practices and common vulnerabilities

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
