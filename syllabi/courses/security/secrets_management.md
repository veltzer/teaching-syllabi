---
tags:
  - concepts:security
  - concepts:cryptography
  - concepts:identity
  - concepts:certificates
  - concepts:pki
  - concepts:best-practices
level: intermediate
category: security
duration_hours: 40
audience:
  - audiences:developers
  - audiences:devops
  - audiences:sres
  - audiences:security-engineers
  - audiences:architects
---
<!-- course: secrets_management -->
# Secrets Management

## Description
Almost every breach disclosure mentions a leaked or mismanaged secret. `API keys` committed to repositories, long-lived
database passwords copied between systems, certificates that nobody knows how to rotate, and `.env` files passed around
in chat. Secrets are everywhere, and most organizations manage them poorly.

This five day course is dedicated entirely to the engineering and operational discipline of secrets management.
It covers the threat model around secrets, the cryptographic primitives that `make` modern secret stores work, the
architecture and operation of Vault, cloud `KMS` services, sealed and external secrets in `Kubernetes`, secret
rotation, runtime secret injection, and the full lifecycle of credentials from issuance to retirement.
The course is implementation-focused but vendor-neutral: the same patterns apply whether you run `HashiCorp Vault`,
`AWS KMS`/`Secrets Manager`, `Google Cloud KMS`, `Azure Key Vault`, or a combination.

## Duration
40 hours / 5 days

## Intended Audience
* developers writing applications that depend on secrets
* `DevOps` and `SRE` engineers operating secret infrastructure
* security engineers responsible for credential hygiene
* architects designing systems with strong identity and credential boundaries
* engineers responding to a secret leak incident or building defenses against the next one

## Prerequisites
* working knowledge of `Linux` and at least one cloud platform
* basic familiarity with `Kubernetes` and containers
* basic understanding of `TLS`, public key cryptography and `JWT`
* some experience with at least one configuration system (`env` vars, config files)

## Objectives
* enumerate the kinds of secrets a typical organization holds and the threats against them
* design systems with the smallest possible secret surface area
* operate Vault and equivalent secret stores
* use cloud `KMS` services correctly: envelope encryption, key policies, audit
* manage secrets in `Kubernetes` without committing them to `git`
* implement short-lived credentials and dynamic secrets
* rotate secrets safely without downtime
* respond to a leaked secret with confidence
* build a secrets program with policies, audit and compliance

## Outline
<!-- chapter: the-secrets-problem, duration: 2h -->
* The secrets problem
    * what counts as a secret
    * the typical inventory: `API keys`, passwords, certificates, tokens, signing keys
    * how secrets leak in the real world
    * secret sprawl and why it grows on its own
    * the cost of a leaked secret
    * threat model for secrets at `rest` and in transit
<!-- chapter: cryptographic-foundations-for-secrets, duration: 3h -->
* Cryptographic foundations for secrets
    * symmetric vs asymmetric encryption
    * authenticated encryption (`AES-GCM`, `ChaCha20-Poly1305`)
    * key derivation functions
    * envelope encryption and the data-key pattern
    * `HMAC` and message authentication
    * digital signatures and what they guarantee
    * what cryptographic primitives do not solve on their own
<!-- chapter: identity-as-the-foundation-of-secrets, duration: 2h -->
* Identity as the foundation of secrets
    * the principle "every workload has an identity"
    * machine identity vs human identity
    * `SPIFFE`/`SPIRE` and workload identity
    * cloud workload identity (`AWS IAM`, `GCP service accounts`, `Azure managed identity`)
    * identity-bound credentials replace shared secrets
<!-- chapter: anti-patterns-and-where-secrets-go-wrong, duration: 2h -->
* Anti-patterns and where secrets `go` wrong
    * `.env` files in repositories
    * secrets in `Dockerfile` `RUN` commands
    * secrets in image layers and image metadata
    * secrets in `CI` logs and build artifacts
    * long-lived shared admin credentials
    * the "wiki page of passwords"
    * detection and remediation of each anti-pattern
<!-- chapter: hashicorp-vault-fundamentals, duration: 3h -->
* `HashiCorp Vault` fundamentals
    * Vault architecture and the storage backend
    * seal and unseal: `Shamir`, auto-unseal with `KMS`
    * authentication methods: `AppRole`, `Kubernetes`, cloud, `OIDC`
    * policies and path-based authorization
    * audit devices
    * high-availability deployment
<!-- chapter: vault-secret-engines-and-dynamic-secrets, duration: 3h -->
* Vault secret engines and dynamic secrets
    * the `KV` v1 vs `KV` v2 secret engine
    * database dynamic secrets
    * cloud dynamic secrets (`AWS`, `GCP`, `Azure`)
    * `PKI` secret engine for short-lived certificates
    * `SSH` secret engine
    * `Transit` engine for encryption-as-a-service
    * leases, renewals and revocation
<!-- chapter: cloud-kms-services, duration: 3h -->
* Cloud `KMS` services
    * `AWS KMS`, `Google Cloud KMS`, `Azure Key Vault`
    * key hierarchies: `CMK`, data keys, customer-managed keys
    * envelope encryption in practice
    * key rotation and key versioning
    * key policies and grants
    * `KMS` audit and CloudTrail/`Cloud Audit Logs`
    * `KMS` cost models
<!-- chapter: cloud-secrets-managers, duration: 2h -->
* Cloud secrets managers
    * `AWS Secrets Manager` vs `SSM Parameter Store`
    * `Google Secret Manager`
    * `Azure Key Vault` secrets
    * pricing and quotas
    * cross-account and cross-project secret sharing
    * choosing between `KMS`, `parameter store` and `secrets manager`
<!-- chapter: kubernetes-secrets-and-its-limits, duration: 2h -->
* `Kubernetes` secrets and its limits
    * native `Kubernetes` `Secret` objects
    * what `Kubernetes` does and does not give you
    * `etcd` encryption at `rest`
    * `RBAC` for secrets
    * common misconceptions about `Kubernetes` secret security
<!-- chapter: secrets-in-gitops-and-kubernetes, duration: 3h -->
* Secrets in `GitOps` and `Kubernetes`
    * `Sealed Secrets` (Bitnami)
    * `External Secrets Operator`
    * Vault agent injector and `CSI` driver
    * `SOPS` with `KMS` backends
    * `age` and `git-crypt`
    * comparing approaches: trust model, operations, ergonomics
<!-- chapter: secret-rotation, duration: 3h -->
* Secret rotation
    * why rotation matters and when it does not
    * automated rotation patterns
    * rotating database passwords without downtime
    * rotating `API keys` with grace periods
    * rotating signing keys and key roll-over
    * rotation monitoring and alerting on stale secrets
<!-- chapter: certificate-lifecycle-management, duration: 2h -->
* Certificate lifecycle management
    * `X.509` certificates as a special class of secret
    * private `CA` design
    * `cert-manager` and automated issuance
    * short-lived certificates as the modern default
    * certificate transparency and monitoring
    * outage stories from expired certificates
<!-- chapter: ci-cd-and-build-time-secrets, duration: 2h -->
* `CI`/`CD` and build-time secrets
    * `OIDC` federation between `CI` and cloud providers
    * `GitHub Actions` `OIDC`, `GitLab CI` `OIDC`
    * `BuildKit` secret mounts
    * scoping secrets to specific jobs and branches
    * preventing secrets from appearing in logs and artifacts
<!-- chapter: detecting-leaks-and-secret-scanning, duration: 2h -->
* Detecting leaks and secret scanning
    * `gitleaks`, trufflehog, `detect-secrets`, `Gitguardian`
    * pre-commit hooks for secret detection
    * server-side push protection
    * scanning historical `git` history
    * scanning images, binaries and logs
    * triaging detection alerts
<!-- chapter: incident-response-for-leaked-secrets, duration: 2h -->
* Incident response for leaked secrets
    * the leak runbook
    * rotate first, investigate after
    * scope of compromise: what could the secret access
    * forensic timelines from audit logs
    * communication with affected parties
    * post-incident hardening
<!-- chapter: governance-policy-and-compliance, duration: 2h -->
* Governance, policy and compliance
    * a secrets policy worth following
    * separation of duties around secrets
    * audit and access reviews
    * compliance angles: `SOC2`, `PCI-DSS`, `HIPAA`, `GDPR`
    * metrics for a secrets program: time-to-rotate, leak rate, coverage
<!-- chapter: workshop-and-wrap-up, duration: 2h -->
* Workshop and wrap up
    * end-to-end design walkthrough on a real-world scenario
    * tabletop exercise: simulated secret leak
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
