---
tags:
  - infrastructure:azure
  - infrastructure:cloud
  - concepts:security
level: intermediate
category: cloud
duration_hours: 24
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:architects
---
<!-- course: azure_security -->
# `Azure` Security

## Description
This course provides a comprehensive exploration of security in `Microsoft Azure`, covering identity management, network protection, data security, and compliance. Participants will learn how to design and implement security controls across `Azure` environments using services such as `Microsoft Entra ID`, `Azure Key Vault`, `Microsoft Defender for Cloud`, and `Azure Sentinel`. The course emphasizes practical, defense-in-depth strategies that align with industry best practices and `Azure` security benchmarks.

## Duration
24 hours / 3 days

## Intended Audience
* Developers building secure applications on `Azure`
* System administrators responsible for `Azure` infrastructure security
* Architects designing secure cloud solutions

## Prerequisites
* Basic understanding of `Azure` services and the `Azure` portal
* Familiarity with networking fundamentals (`IP` addressing, firewalls, `DNS`)
* Basic understanding of identity and authentication concepts

## Objectives
* Implement identity and access management with `Microsoft Entra ID`
* Configure role-based and conditional access controls
* Protect data using encryption and `Azure Key Vault`
* Secure network infrastructure with firewalls, `Network Security Groups`, and private endpoints
* Monitor and respond to security threats using `Microsoft Defender for Cloud` and `Azure Sentinel`
* Enforce organizational compliance with `Azure Policy` and `Microsoft Purview`

## Outline
<!-- chapter: microsoft-entra-id-deep-dive, duration: 2h -->
* `Microsoft Entra ID` Deep Dive
    * Tenant and directory architecture
    * Users, groups, and external identities
    * Authentication methods and passwordless options
    * `Entra ID` Privileged Identity Management (PIM)
    * Application registrations and service principals
<!-- chapter: role-based-access-control-and-custom-roles, duration: 2h -->
* Role-Based Access Control and Custom Roles
    * Built-in roles and role assignments
    * Creating and managing custom roles
    * Scope hierarchy (management groups, subscriptions, resource groups)
    * Least-privilege access strategies
<!-- chapter: conditional-access-policies, duration: 2h -->
* Conditional Access Policies
    * Policy components (assignments, conditions, controls)
    * Multi-factor authentication enforcement
    * Device compliance and trusted locations
    * Named locations and risk-based policies
    * Report-only mode and troubleshooting
<!-- chapter: managed-identities, duration: 2h -->
* `Managed Identities`
    * System-assigned vs. user-assigned identities
    * Accessing `Azure` resources without credentials
    * Integration with `Azure Key Vault`, `Storage`, and `SQL`
<!-- chapter: azure-key-vault, duration: 2h -->
* `Azure Key Vault`
    * Keys, secrets, and certificates management
    * Access policies and `RBAC` for `Key Vault`
    * Key rotation and versioning
    * Hardware security modules (`HSM`) support
    * Integration with application code and `DevOps` pipelines
<!-- chapter: microsoft-defender-for-cloud, duration: 2h -->
* `Microsoft Defender for Cloud`
    * Security posture management
    * Secure Score and recommendations
    * Defender plans for various workloads
    * Vulnerability assessment and remediation
    * Just-in-time VM access
<!-- chapter: azure-sentinel-siem, duration: 2h -->
* `Azure Sentinel` (`SIEM`)
    * Workspace setup and data connectors
    * Analytics rules and incident management
    * Threat hunting with KQL queries
    * Automated response with playbooks
    * Workbooks and dashboards
<!-- chapter: network-security, duration: 3h -->
* Network Security
    * `Network Security Groups` and rule evaluation
    * `Application Security Groups`
    * `Azure Firewall` and `Firewall Manager`
    * `Azure DDoS Protection` (basic and standard)
    * `Azure Private Link` and private endpoints
    * Service endpoints vs. private endpoints
<!-- chapter: data-encryption, duration: 2h -->
* Data Encryption
    * Encryption at `rest` (storage service encryption, disk encryption)
    * Encryption in transit (`TLS`, `VPN`, `ExpressRoute`)
    * Customer-managed keys and `Bring Your Own Key`
    * `Azure` Confidential Computing overview
<!-- chapter: azure-policy-and-compliance, duration: 2h -->
* `Azure Policy` and Compliance
    * Policy definitions and initiatives
    * Compliance dashboard and remediation tasks
    * Regulatory compliance standards (ISO, `SOC`, `GDPR`)
    * `Microsoft Purview` for data governance and classification
    * Data loss prevention and sensitivity labels
<!-- chapter: security-monitoring-and-incident-response, duration: 3h -->
* Security Monitoring and Incident Response
    * `Azure Monitor` and diagnostic logging
    * Activity log analysis
    * Security alerts and automated remediation
    * Incident response planning and execution
    * Integration with third-party `SIEM` tools

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
