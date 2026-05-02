---
tags:
  - infrastructure:gcp
  - infrastructure:cloud
  - security:security
  - security:iam
level: intermediate
category: cloud
duration_hours: 16
audience:
  - audiences:security-professionals
  - audiences:devops
  - audiences:sres
---
<!-- course: gcp_security -->
# `GCP` Security

## Description
This course provides a comprehensive look at security on `Google Cloud Platform`.
Participants will gain deep understanding of `GCP` identity and access management,
network security, data protection, and threat detection. The course covers
key services such as `VPC Service Controls`, `Security Command Center`,
`Cloud KMS`, `Cloud Armor`, and `Binary Authorization`, along with best practices
for audit logging, compliance, and incident response.

## Duration
16 hours / 2 days

## Intended Audience
* Security professionals responsible for securing `GCP` environments.
* `DevOps` engineers implementing security controls on `GCP`.
* Site reliability engineers managing secure infrastructure on `Google Cloud`.

## Prerequisites
* Basic familiarity with `GCP` core services.
* Understanding of general cloud security concepts.
* Basic knowledge of networking and identity management.

## Objectives
* Design and implement `IAM` policies and organizational hierarchies on `GCP`.
* Configure `VPC Service Controls` to protect sensitive data.
* Use `Security Command Center` for threat detection and vulnerability management.
* Manage encryption keys and secrets with `Cloud KMS` and `Secret Manager`.
* Implement network security using `Cloud Armor` and `firewall` policies.
* Establish audit logging, compliance controls, and incident response procedures.

## Outline
<!-- chapter: gcp-security-foundations, duration: 1h -->
* `GCP` Security Foundations
    * Shared responsibility model
    * `GCP` resource hierarchy and organization policies
    * Security best practices overview
<!-- chapter: iam-deep-dive, duration: 2h -->
* `IAM` Deep Dive
    * Users, groups, and service accounts
    * Roles and custom roles
    * `IAM` conditions and policy bindings
    * Workload identity federation
    * Least privilege and role recommendations
<!-- chapter: vpc-service-controls, duration: 1h -->
* `VPC Service Controls`
    * Service perimeters and access levels
    * Protecting sensitive APIs and data
    * Dry-run mode and troubleshooting
    * Ingress and egress policies
<!-- chapter: security-command-center, duration: 2h -->
* `Security Command Center`
    * Security Health Analytics
    * Event Threat Detection
    * Container Threat Detection
    * Web Security Scanner
    * Findings and notifications
<!-- chapter: cloud-kms-and-data-protection, duration: 2h -->
* `Cloud KMS` and Data Protection
    * Key management concepts and key rings
    * Encryption at `rest` and in transit
    * Customer-managed vs. customer-supplied encryption keys
    * `Secret Manager` for secrets management
    * Data Loss Prevention `API`
<!-- chapter: cloud-armor, duration: 2h -->
* `Cloud Armor`
    * Web application `firewall` policies
    * `DDoS` protection
    * Adaptive protection
    * Security policies and rules
    * Integration with load balancers
<!-- chapter: binary-authorization, duration: 2h -->
* `Binary Authorization`
    * Container image attestation
    * Policy enforcement for `GKE`
    * Integration with `CI/CD` pipelines
    * Continuous validation
<!-- chapter: audit-logging-and-compliance, duration: 2h -->
* Audit Logging and Compliance
    * Admin activity and data access audit logs
    * Log sinks and centralized logging
    * Compliance standards and `Assured Workloads`
    * Access Transparency
<!-- chapter: incident-response, duration: 2h -->
* Incident Response
    * Incident response planning on `GCP`
    * Forensics and evidence collection
    * Automated response with `Cloud Functions`
    * Integration with `SIEM` and SOAR tools

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
