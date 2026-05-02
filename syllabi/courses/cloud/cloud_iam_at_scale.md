---
tags:
  - concepts:security
  - concepts:identity
  - concepts:operations
  - concepts:best-practices
level: advanced
category: cloud
duration_hours: 24
audience:
  - audiences:devops
  - audiences:security-engineers
  - audiences:architects
  - audiences:senior-developers
---
<!-- course: cloud_iam_at_scale -->
# Cloud `IAM` at Scale

## Description
The catalog has `Identity and Access Management`, `Cloud Security`, and the per-cloud security courses
(`AWS Security`, `Azure Security`, `GCP Security`), all of which touch `IAM`. None of them is the
focused course on operating cloud identity at scale: hundreds of accounts, thousands of roles, multi-account
or multi-subscription topologies, the human-and-workload identity-pipeline question, federation from
`SSO`, the tension between developer velocity and least privilege, and the audit-and-compliance reality.

This three day course covers cloud `IAM` as practiced at organizational scale. It covers the
multi-account topology (`AWS Organizations`, `Azure Management Groups`, `GCP Organizations`), the
identity-source question (`Okta`, `Entra ID`, `Google Workspace` as the source of truth), the
federation pattern (`SAML`, `OIDC`, SCIM), the per-cloud `IAM` model (`AWS IAM`, `Azure RBAC` plus
`Entra`, `GCP IAM` plus the resource hierarchy), the workload-identity story (no long-lived keys), the
permission-boundaries / `SCPs` / org-policies tier, the access-review and certification workflow, the
emergency-access pattern, the just-in-time access pattern, the privileged-access management tier, and
the migration of an organization that grew up with sprawled `IAM` to a managed program. Examples are
drawn from public engineering writing of `Square`, Netflix, Airbnb, and the `AWS` Well-Architected
Security Pillar. Participants leave able to design and run `IAM` for an organization that is bigger
than one team.

## Duration
24 hours / 3 days

## Intended Audience
* `DevOps` engineers running multi-account cloud environments
* security engineers operating identity programs
* architects designing the cloud landing zone
* senior developers facing the "we have `500` roles" reality

## Prerequisites
* working experience with at least one major cloud provider's `IAM`
* exposure to the Identity and Access Management course
* familiarity with at least one identity provider (`Okta`, `Entra ID`, `Google Workspace`)
* basic understanding of `SSO`

## Objectives
* design a multi-account cloud topology
* federate identity from a single source of truth
* enforce permission boundaries across the organization
* eliminate long-lived workload credentials
* run access reviews and certifications
* operate emergency-access and just-in-time access
* migrate sprawled `IAM` to a managed program

## Outline
<!-- chapter: why-iam-breaks-at-scale, duration: 1h -->
* Why `IAM` breaks at scale
    * the canonical sprawl: `500` roles, no clear ownership
    * the "we cannot tell who has access to what" reality
    * the "we cannot prove least privilege" audit failure
    * cross-reference to the Identity and Access Management course
    * the cost of doing nothing
<!-- chapter: multi-account-topology, duration: 3h -->
* Multi-account topology
    * `AWS Organizations` and `OU` design
    * `Azure Management Groups` and subscriptions
    * `GCP Organizations` and folders
    * the per-environment-per-team model
    * the per-team model
    * the "we have 5000 accounts" reality at large companies
<!-- chapter: identity-source-of-truth, duration: 2h -->
* Identity source of truth
    * `Okta`, `Entra ID`, `Google Workspace` as the canonical source
    * the user lifecycle (joiner, mover, leaver)
    * the group-based access model
    * `SCIM` provisioning into the cloud
    * the "we managed users in three places and they drifted" failure
<!-- chapter: federation, duration: 2h -->
* Federation
    * `SAML` and `OIDC` to the cloud
    * `AWS IAM Identity Center` (formerly `SSO`)
    * `Entra ID` and `Azure RBAC`
    * `GCP Workforce Identity Federation`
    * the no-`IAM`-users rule
<!-- chapter: aws-iam-at-scale, duration: 2h -->
* `AWS IAM` at scale
    * `IAM Identity Center` permission sets
    * `Service Control Policies` (`SCPs`)
    * `Permission Boundaries`
    * `IAM Access Analyzer`
    * the "we used the root user once" disaster
<!-- chapter: azure-rbac-at-scale, duration: 2h -->
* `Azure RBAC` at scale
    * `Entra ID` plus `Azure RBAC`
    * management-group-level policies
    * `Privileged Identity Management` (`PIM`)
    * `Azure Policy`
    * the gotchas in the cross-tenant case
<!-- chapter: gcp-iam-at-scale, duration: 2h -->
* `GCP IAM` at scale
    * the resource-hierarchy inheritance
    * `Organization Policy`
    * `IAM Recommender`
    * `IAM Conditions`
    * the per-folder permission strategy
<!-- chapter: workload-identity, duration: 2h -->
* Workload identity
    * the no-long-lived-keys rule
    * `IAM Roles for Service Accounts` (IRSA) for `EKS`
    * `EKS Pod Identity`
    * `Workload Identity` for `GKE`
    * `Managed Identities` for `Azure`
    * the `OIDC` from `GitHub Actions`
    * the "the secret was in Slack" disaster
<!-- chapter: access-review-and-certification, duration: 2h -->
* Access review and certification
    * the periodic access review
    * the certification campaign
    * the "we approved everything because the meeting was long" failure
    * the access-review tooling
    * the "the auditor found unused roles from 2019" reality
<!-- chapter: emergency-access, duration: 1h -->
* Emergency access
    * the break-glass account
    * the alarm-when-used policy
    * the "we never tested break-glass" reality
    * the post-incident review
    * the rotation of break-glass credentials
<!-- chapter: just-in-time-access, duration: 2h -->
* Just-in-time access
    * the request-and-approve flow
    * `AWS IAM Identity Center` JIT, `Azure PIM`, `GCP` `IAM` Conditions with time
    * `ConductorOne`, Sym, Indent, `Opal` as third-party tools
    * the "we made `JIT` so painful nobody used it" failure
    * the developer-velocity trade-off
<!-- chapter: migrating-from-sprawl-to-program, duration: 2h -->
* Migrating from sprawl to program
    * the inventory step
    * the per-account ownership step
    * the federation cutover
    * the role consolidation
    * the "we tried to fix everything at once and gave up" reality
    * the staged plan
<!-- chapter: audit-and-compliance, duration: 1h -->
* Audit and compliance
    * the `SOC 2` access-control evidence
    * the `ISO 27001` requirements
    * the per-jurisdiction questions
    * cross-reference to the `GDPR` and Compliance course
    * the audit-friendly logging story

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
