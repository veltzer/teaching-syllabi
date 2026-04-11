---
tags:
  - security:security
  - concepts:architecture
level: intermediate
category: security
duration_hours: 24
audience:
  - audiences:security-professionals
  - audiences:developers
  - audiences:architects
---
<!-- course: identity_and_access_management -->
# Identity and Access Management

## Description
This course provides a comprehensive exploration of identity and access management (`IAM`) concepts, protocols, and implementations. Participants will learn how modern authentication and authorization systems work, from foundational protocols like `LDAP` and `Kerberos` to contemporary standards such as `OAuth2` and `OpenID Connect`. The course covers directory services, identity federation, authorization models, `API` security, cloud `IAM`, and identity governance, equipping teams to design and implement robust identity solutions.

## Duration
24 hours / 3 days

## Intended Audience
* Security engineers and architects designing identity solutions
* Software developers implementing authentication and authorization
* System administrators managing directory services and access controls
* Cloud architects configuring `IAM` across cloud platforms
* Technical leads evaluating identity-as-a-service solutions
* Compliance officers overseeing access governance

## Prerequisites
* Basic understanding of web technologies (`HTTP`/`HTTPS`, `REST APIs`)
* Familiarity with networking concepts (`DNS`, `TCP`/`IP`, `TLS`)
* Basic knowledge of security principles (authentication vs authorization)
* Experience with at least one cloud platform is helpful but not required
* Understanding of `JSON` and `XML` data formats

## Objectives
* Understand and compare authentication protocols including `SAML`, `OIDC`, `OAuth2`, `LDAP`, and `Kerberos`
* Design and implement single sign-on and multi-factor authentication solutions
* Configure and manage directory services such as `Active Directory` and `LDAP`
* Apply authorization models including `RBAC`, `ABAC`, and ReBAC appropriately
* Secure APIs using `JWT`, `OAuth2` scopes, and `API` key management
* Implement identity solutions across `AWS`, `Azure`, and `GCP` cloud platforms
* Evaluate and integrate identity-as-a-service platforms like `Okta`, `Auth0`, and `Keycloak`
* Address compliance and governance requirements in identity management

## Outline
<!-- chapter: iam-fundamentals-and-authentication-protocols, duration: 4h -->
* `IAM` Fundamentals and Authentication Protocols
    * Identity and access management core concepts and terminology
    * The identity lifecycle: provisioning, management, and deprovisioning
    * Authentication factors: knowledge, possession, and inherence
    * `LDAP` protocol: directory structure, `bind` operations, and search queries
    * `Kerberos` authentication: tickets, KDC, and mutual authentication
    * `SAML` protocol: assertions, identity providers, and service providers
    * `OpenID Connect`: `ID` tokens, discovery, and user info endpoint
    * `OAuth2` framework: grant types, scopes, and token management
    * Comparing protocols: use cases and selection criteria
<!-- chapter: single-sign-on-and-multi-factor-authentication, duration: 3h -->
* Single Sign-On and Multi-Factor Authentication
    * Single sign-on (SSO) architecture and benefits
    * Implementing SSO with `SAML` and `OIDC`
    * Desktop SSO and `Kerberos` integration
    * SSO session management and token lifecycle
    * Multi-factor authentication (MFA) methods and technologies
    * TOTP, `FIDO2`/`WebAuthn`, and push notification-based MFA
    * Adaptive and risk-based authentication
    * Passwordless authentication strategies
<!-- chapter: directory-services-and-identity-federation, duration: 3h -->
* Directory Services and Identity Federation
    * `Active Directory` architecture: domains, forests, trusts, and group policies
    * `LDAP` directory design and schema management
    * Directory synchronization and replication
    * Identity federation concepts and trust relationships
    * Cross-domain and cross-organization federation
    * SCIM protocol for identity provisioning
    * Just-in-time provisioning and account linking
    * Hybrid identity: bridging on-premises and cloud directories
<!-- chapter: authorization-models, duration: 3h -->
* Authorization Models
    * Role-based access control (`RBAC`): roles, permissions, and hierarchies
    * Attribute-based access control (`ABAC`): policies, attributes, and evaluation
    * Relationship-based access control (ReBAC): graph-based authorization
    * Policy engines and policy-as-code
    * Fine-grained vs coarse-grained authorization
    * Authorization in `microservices` architectures
    * Implementing least privilege and separation of duties
    * Auditing and reviewing access decisions
<!-- chapter: api-security-and-token-management, duration: 3h -->
* `API` Security and Token Management
    * `API` authentication patterns and best practices
    * `API` keys: generation, rotation, and scope limitation
    * `JWT` structure, signing algorithms, and validation
    * `OAuth2` scopes and consent management
    * Token introspection and revocation
    * Short-lived tokens and refresh token strategies
    * Securing machine-to-machine communication
    * `API gateway` integration for authentication and rate limiting
<!-- chapter: cloud-iam-and-identity-as-a-service, duration: 4h -->
* Cloud `IAM` and Identity as a Service
    * `AWS IAM`: users, roles, policies, and identity federation
    * `Azure AD` (now `Entra ID`): tenants, app registrations, and conditional access
    * `GCP IAM`: service accounts, roles, and workload identity
    * Cross-cloud identity strategies
    * Identity-as-a-service platforms: `Okta`, `Auth0`, and `Keycloak`
    * Evaluating and selecting identity providers
    * Migration strategies between identity platforms
    * Zero trust identity: continuous verification and device trust
<!-- chapter: identity-governance-and-compliance, duration: 4h -->
* Identity Governance and Compliance
    * Identity governance framework and processes
    * Access certification and periodic reviews
    * Privileged access management (`PAM`) and just-in-time access
    * Segregation of duties enforcement
    * Compliance requirements: `GDPR`, SOX, `HIPAA`, and `PCI DSS`
    * Audit logging and reporting for identity events
    * Orphaned accounts and access drift detection
    * Building an identity governance program

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
