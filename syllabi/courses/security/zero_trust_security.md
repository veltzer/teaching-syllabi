---
tags:
  - security:zero-trust
  - security:architecture
  - concepts:identity
  - concepts:network-security
level: intermediate
category: security
duration_hours: 16
audience:
  - audiences:architects
  - audiences:security-engineers
  - audiences:devops
  - audiences:managers
---
<!-- course: zero_trust_security -->
# Zero Trust Security

## Description
Zero Trust is a security model built on the principle of "never trust, always verify," eliminating implicit trust granted by network location or user credentials alone. This course provides a comprehensive understanding of Zero Trust architecture, covering its core principles, practical implementation patterns, and the tooling and frameworks used to enforce it at scale. Participants will learn how to apply Zero Trust controls across identity, devices, networks, applications, and data, with reference to real-world deployments such as `BeyondCorp` and the `NIST SP 800-207` standard. By the end of the course, attendees will be able to assess their organization's current security posture and chart a roadmap toward a Zero Trust architecture.

## Duration
16 hours / 2 days

## Intended Audience
* Security architects and enterprise architects designing modern security frameworks
* Security engineers responsible for access control and network security
* `DevOps` and platform engineers building secure infrastructure
* Security managers and CISOs evaluating Zero Trust adoption strategies

## Prerequisites
* `Solid` understanding of networking fundamentals (```TCP``/``IP```, `DNS`, `VPN`, firewalls)
* Familiarity with identity and access management concepts (`LDAP`, `Active Directory`, `OAuth 2.0`)
* Experience with cloud infrastructure (`AWS`, `Azure`, or `GCP`) is beneficial
* Basic knowledge of `PKI` and `TLS` certificate management
* Understanding of enterprise IT architecture and traditional perimeter security models

## Objectives
* Explain the limitations of traditional perimeter-based security and the business case for Zero Trust
* Articulate the core principles and pillars of Zero Trust as defined by `NIST SP 800-207` and `BeyondCorp`
* Design identity-centric access control strategies using `MFA`, conditional access, and `IAM` policies
* Implement device trust evaluation using endpoint detection and posture assessment tools
* Apply network micro-segmentation to limit lateral movement and blast `radius`
* Enforce least-privilege access policies at the application and `API` layer
* Classify data and apply Zero Trust controls for data protection in transit and at `rest`
* Develop a phased Zero Trust implementation roadmap aligned with organizational maturity

## Outline
<!-- chapter: traditional-perimeter-security-vs-zero-trust, duration: 2h -->
* Traditional Perimeter Security vs Zero Trust
    * The castle-and-moat model and its assumptions
    * How cloud adoption, remote work, and `SaaS` broke the perimeter
    * High-profile breaches enabled by implicit trust (`SolarWinds`, lateral movement attacks)
    * What Zero Trust is — and what it is not
    * Zero Trust as an architecture philosophy, not a product
    * Overview of `NIST SP 800-207` and the `BeyondCorp` reference model
    * Business drivers: risk reduction, compliance, and operational agility

<!-- chapter: zero-trust-principles-and-pillars, duration: 2h -->
* Zero Trust Principles and Pillars
    * The three core principles: verify explicitly, use least privilege, assume breach
    * The five pillars: identity, devices, networks, applications, data
    * Continuous verification vs point-in-time trust decisions
    * Policy Decision Points (`PDP`) and Policy Enforcement Points (`PEP`)
    * `NIST SP 800-207` logical architecture components
    * Threat modeling within a Zero Trust context
    * Mapping Zero Trust controls to compliance frameworks (`SOC 2`, `ISO 27001`, `FedRAMP`)

<!-- chapter: identity-as-the-new-perimeter, duration: 2h -->
* Identity as the New Perimeter
    * Why identity is the primary control plane in Zero Trust
    * Strong authentication: `MFA`, `FIDO2`/`WebAuthn`, and passwordless strategies
    * Conditional access policies based on user risk and context
    * `OAuth 2.0`, `OpenID Connect`, and `SAML` in a Zero Trust architecture
    * Identity providers: `Okta`, `Azure AD`, `Google Workspace`
    * Privileged access management (`PAM`) and just-in-time access
    * Service account and workload identity (`SPIFFE`/`SPIRE`)

<!-- chapter: device-trust-and-endpoint-security, duration: 2h -->
* Device Trust and Endpoint Security
    * Device posture assessment: what constitutes a trusted device
    * `MDM` and endpoint management with `Microsoft Intune`, `Jamf`, `Google Endpoint Management`
    * Endpoint detection and response (`EDR`) and its role in continuous trust evaluation
    * Certificate-based device authentication
    * Managed vs unmanaged device policies (`BYOD` considerations)
    * Device health signals integrated with access decisions
    * Responding to anomalous device behavior in real time

<!-- chapter: network-micro-segmentation, duration: 2h -->
* Network Micro-Segmentation
    * Flat networks and the lateral movement problem
    * Principles of micro-segmentation and software-defined perimeters (`SDP`)
    * `VLAN`s, `SDN`, and overlay networks for segmentation
    * Service mesh security with `Istio` and `Linkerd`
    * East-west traffic inspection and enforcement
    * `eBPF`-based network policy enforcement with `Cilium`
    * Implementing micro-segmentation in cloud environments (`AWS Security Groups`, `Azure NSGs`)

<!-- chapter: application-access-control, duration: 2h -->
* Application Access Control
    * Moving from `VPN`-based access to application-level access proxies
    * `BeyondCorp`-style access proxies and context-aware access
    * Zero Trust Network Access (`ZTNA`) solutions: `Cloudflare Access`, `Zscaler`, `Tailscale`
    * `API` gateway enforcement and token validation
    * Role-based and attribute-based access control (`RBAC`/`ABAC`)
    * Continuous session verification and re-authentication triggers
    * Audit logging and non-repudiation for application access

<!-- chapter: data-protection-in-zero-trust, duration: 2h -->
* Data Protection in Zero Trust
    * Data classification frameworks and their role in access policy
    * Encryption at `rest` and in transit as a foundational control
    * Data Loss Prevention (`DLP`) in a Zero Trust context
    * Rights management and `IRM` for sensitive documents
    * Secrets management with `HashiCorp Vault` and cloud-native secret stores
    * Tokenization and masking for sensitive data exposure reduction
    * Monitoring data access patterns for anomaly detection

<!-- chapter: implementing-zero-trust-with-beyondcorp-and-nist-sp-800-207, duration: 2h -->
* Implementing Zero Trust with `BeyondCorp` and `NIST SP 800-207`
    * Google's `BeyondCorp` journey: lessons and principles
    * `NIST SP 800-207` implementation steps and deployment models
    * Assessing organizational Zero Trust maturity (`CISA` Zero Trust Maturity Model)
    * Building a phased Zero Trust roadmap: quick wins and long-term investments
    * Change management, stakeholder buy-in, and user experience considerations
    * Metrics and KPIs for measuring Zero Trust effectiveness
    * Common pitfalls and anti-patterns in Zero Trust deployments

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
