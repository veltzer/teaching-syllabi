---
tags:
  - tools:vault
  - security:security
  - practices:devops
level: intermediate
category: devops
duration_hours: 16
audience:
  - audiences:developers
  - audiences:security-professionals
  - audiences:devops
---
<!-- course: hashicorp_vault -->
# HashiCorp `Vault`

## Description
This course covers HashiCorp `Vault`, the industry-standard tool for secrets management,
encryption as a service, and identity-based access. Students will learn how to deploy,
configure, and operate `Vault` in production environments.

The course progresses from secrets management fundamentals through `Vault` architecture,
secret engines, authentication methods, and policies. Students will gain practical experience
with dynamic secrets, the transit engine, `Vault` Agent, and integrations with `Kubernetes`
and `Terraform`.

## Duration
16 hours / 2 days

## Intended Audience
* Developers, `DevOps` engineers, and security professionals who need to manage secrets and sensitive data in their infrastructure.
* Teams adopting zero-trust security models and looking to centralize secrets management.

## Prerequisites
* Basic understanding of security concepts (encryption, authentication, authorization).
* Familiarity with command-line tools.
* Experience with `Linux` systems administration is helpful.

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Understand secrets management challenges and how `Vault` addresses them.
* Install, configure, and unseal a `Vault` server.
* Use multiple secret engines for different use cases.
* Configure authentication methods and write access policies.
* Generate and manage dynamic secrets.
* Integrate `Vault` with `Kubernetes` and `Terraform`.
* Design highly available and disaster-recoverable `Vault` deployments.

## Outline
<!-- chapter: secrets-management-concepts, duration: 1h -->
* Secrets Management Concepts
    * The secrets sprawl problem
    * Static vs dynamic secrets
    * Zero-trust security model
    * Secrets lifecycle management
<!-- chapter: vault-architecture, duration: 1h -->
* `Vault` Architecture
    * `Vault` server components
    * Storage backends (`Consul`, Raft, filesystem)
    * Seal and unseal process
    * Shamir secret sharing
    * Auto-unseal with `cloud KMS`
    * `Vault` `API` overview
<!-- chapter: secret-engines, duration: 2h -->
* Secret Engines
    * KV secrets engine (v1 and v2)
    * Versioning and soft deletes
    * Database secrets engine (dynamic credentials)
    * `PKI` secrets engine (certificate authority)
    * Transit secrets engine (encryption as a service)
    * `AWS` secrets engine
    * `SSH` secrets engine
    * Enabling and configuring engines
<!-- chapter: authentication-methods, duration: 2h -->
* Authentication Methods
    * Token authentication
    * AppRole authentication
    * `LDAP` authentication
    * `OIDC` authentication
    * `Kubernetes` authentication
    * Token types and lifecycle
    * Choosing the right auth method
<!-- chapter: policies-and-acls, duration: 2h -->
* Policies and `ACLs`
    * HCL policy syntax
    * Path-based access control
    * Capabilities (create, read, update, delete, list)
    * Policy templating
    * Sentinel policies (Enterprise)
    * Root and default policies
<!-- chapter: dynamic-secrets, duration: 1h -->
* Dynamic Secrets
    * How dynamic secrets work
    * Database dynamic credentials
    * Cloud provider dynamic credentials
    * Lease management and renewal
    * Revocation strategies
<!-- chapter: encryption-as-a-service, duration: 1h -->
* Encryption as a Service
    * Transit engine operations (encrypt, decrypt, rewrap)
    * Key rotation
    * Convergent encryption
    * Data masking
<!-- chapter: vault-agent, duration: 1h -->
* `Vault` Agent
    * Auto-auth configuration
    * Template rendering
    * Caching
    * Process supervisor mode
    * Sidecar pattern with `Kubernetes`
<!-- chapter: namespaces-and-multi-tenancy, duration: 1h -->
* Namespaces and Multi-Tenancy
    * Namespace isolation
    * Delegated administration
    * Cross-namespace policies
<!-- chapter: audit-logging, duration: 1h -->
* Audit Logging
    * Audit device configuration
    * Log formats and filtering
    * Compliance and forensics
<!-- chapter: high-availability-and-disaster-recovery, duration: 1h -->
* High Availability and Disaster Recovery
    * HA architecture with Raft
    * Active/standby nodes
    * Performance replication (Enterprise)
    * Disaster recovery replication (Enterprise)
    * Backup and restore
<!-- chapter: terraform-integration, duration: 1h -->
* `Terraform` Integration
    * `Vault` provider for `Terraform`
    * Managing `Vault` configuration as code
    * Dynamic credentials for `Terraform` runs
<!-- chapter: kubernetes-integration, duration: 1h -->
* `Kubernetes` Integration
    * `Vault` sidecar injector
    * CSI provider
    * `Vault` Secrets Operator
    * Pod identity and authentication

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
