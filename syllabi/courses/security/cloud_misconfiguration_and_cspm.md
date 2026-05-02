---
tags:
  - concepts:security
  - concepts:identity
  - concepts:operations
  - concepts:best-practices
  - concepts:cloud-economics
  - concepts:gitops
level: intermediate
category: security
duration_hours: 40
audience:
  - audiences:security-engineers
  - audiences:devops
  - audiences:sres
  - audiences:senior-developers
  - audiences:architects
---
<!-- course: cloud_misconfiguration_and_cspm -->
# Cloud Misconfiguration and `CSPM`

## Description
Most cloud breaches are not novel exploits. They are public buckets, over-permissive `IAM`, exposed
management interfaces, forgotten compute instances, and snapshots accessible to the world. The cloud
security course in the catalog is a broader treatment; this course is the focused, hands-on companion on
finding, fixing, and preventing the misconfigurations that account for the majority of real-world cloud
incidents.

This five day course covers the top cloud-misconfiguration classes across `AWS`, `GCP` and `Azure`, the
discipline of `IAM` least privilege, the `CSPM` (cloud security posture management) tooling landscape
(`Wiz`, `Prisma Cloud`, Lacework, Orca, `Snyk Cloud`, native cloud CSPMs), the `IaC`-side
prevention story (`tfsec`, Checkov, KICS, `Snyk IaC`, `Terrascan`), runtime drift detection, and the
remediation playbooks. Examples are drawn from public breach disclosures and `CSPM` benchmark reports.
Participants leave able to assess a cloud environment, prioritize fixes, and build the prevention
program that keeps a fixed environment fixed.

## Duration
40 hours / 5 days

## Intended Audience
* security engineers responsible for cloud security posture
* `DevOps` and `SRE` engineers operating cloud infrastructure
* developers writing `IaC` for production cloud workloads
* engineers responding to cloud-security audit findings
* architects evaluating `CSPM` tooling

## Prerequisites
* working knowledge of at least one cloud platform
* basic familiarity with `IaC` (`Terraform`, `CloudFormation`, `Pulumi`)
* exposure to `IAM` and at least one cloud's identity model
* exposure to the broader cloud-security material is helpful

## Objectives
* enumerate the top cloud-misconfiguration classes
* design `IAM` least privilege correctly across `AWS`, `GCP`, `Azure`
* operate `CSPM` tooling effectively and prioritize findings
* prevent misconfiguration at the `IaC` layer
* detect and remediate runtime drift
* build a misconfiguration-prevention program with appropriate metrics
* avoid the noise-and-fatigue trap that kills `CSPM` programs

## Outline
<!-- chapter: the-misconfiguration-threat-landscape, duration: 2h -->
* The misconfiguration threat landscape
    * the public breach pattern: misconfig, not zero-day
    * the `Capital One`, Twitch, Uber, `Equifax` cloud-misconfig lessons
    * the `OWASP Cloud Top 10` style frameworks
    * `CIS` benchmarks
    * `MITRE ATT&CK` for cloud
    * cross-reference to the Threat Hunting course
<!-- chapter: iam-the-most-important-control, duration: 4h -->
* `IAM`: the most important control
    * `AWS IAM`, `GCP IAM`, `Azure RBAC`
    * principals, roles, policies, conditions
    * resource-based vs identity-based policies
    * `AWS` `SCPs` and permission boundaries
    * `GCP` organization policies
    * `Azure` management groups
    * the `*:*:*` policy and its variants
    * cross-account / cross-project access
<!-- chapter: iam-least-privilege-in-practice, duration: 3h -->
* `IAM` least privilege in practice
    * starting from observed access vs starting from policy
    * `AWS Access Analyzer`, `GCP Policy Analyzer`, `Azure PIM`
    * just-in-time elevation
    * service control policies as the safety net
    * the human vs machine identity split
    * cross-reference to the Zero Trust Networking course
<!-- chapter: storage-misconfigurations, duration: 3h -->
* Storage misconfigurations
    * public `S3` buckets, `GCS` buckets, `Azure` blob containers
    * pre-signed `URLs` and the long-lived link
    * encryption at `rest` and key-policy mistakes
    * snapshot and image public exposure
    * cross-account snapshot sharing
    * `S3` `Block Public Access` and equivalents
<!-- chapter: network-misconfigurations, duration: 3h -->
* Network misconfigurations
    * security groups and `NACLs`
    * the `0.0.0.0/0` problem
    * `VPC` peering and the transitive-trust mistake
    * `Cloud Run`/`App Service` public endpoints
    * exposed `RDS`/`Cloud SQL`/`Azure SQL` instances
    * `Kubernetes` `LoadBalancer` services accidentally public
    * cross-reference to the Edge Computing course
<!-- chapter: management-interface-and-credential-exposure, duration: 2h -->
* Management interface and credential exposure
    * exposed `kubectl` apiserver, `Jenkins`, `Argo`
    * `IMDS` v1 and `SSRF`
    * key-`vault` and parameter-store mistakes
    * `Git`-leaked cloud credentials
    * cross-reference to the Secrets Management course
    * the `MFA`-not-enforced root account
<!-- chapter: kubernetes-cloud-misconfigurations, duration: 3h -->
* `Kubernetes` cloud misconfigurations
    * `EKS`/`GKE`/`AKS` cluster public endpoints
    * permissive `pod` security
    * `IRSA`/`GKE` `Workload Identity` mistakes
    * cluster `IAM` and the node role
    * `RBAC` overprivilege
    * cross-reference to the existing `Kubernetes` Security course
<!-- chapter: cspm-tooling-landscape, duration: 3h -->
* `CSPM` tooling landscape
    * `Wiz`, `Prisma Cloud`, Lacework, Orca, `Snyk Cloud`
    * native cloud: `Security Hub`, `Security Command Center`, `Defender for Cloud`
    * `CIEM` (cloud identity entitlement management) tools
    * agentless vs agent-based scanning
    * `CNAPP` and the bundled-platform trend
    * choosing tooling from real requirements
<!-- chapter: prioritizing-cspm-findings, duration: 3h -->
* Prioritizing `CSPM` findings
    * the alert-fatigue problem
    * severity vs reachability vs business impact
    * the "internet-exposed plus privileged" combination
    * the attack-path graph
    * triage queues and ownership routing
    * post-mortem analysis of dropped findings
<!-- chapter: iac-prevention, duration: 3h -->
* `IaC` prevention
    * `tfsec`, Checkov, KICS, `Snyk IaC`, `Terrascan`
    * `OPA`/`Conftest` for policy as code
    * `Sentinel` for `Terraform Cloud`
    * pre-commit, `PR`, and pipeline gates
    * the false-positive economics in `IaC` scanning
    * custom rules for organization-specific policy
<!-- chapter: drift-detection-and-runtime-config, duration: 2h -->
* Drift detection and runtime config
    * `Terraform` drift detection
    * `AWS Config`, `Cloud Asset Inventory`, `Azure Resource Graph`
    * detecting click-ops changes
    * remediation back to `IaC`
    * the "console-disabled" pattern
<!-- chapter: forgotten-and-shadow-resources, duration: 2h -->
* Forgotten and shadow resources
    * the unowned account and the unmanaged subscription
    * forgotten `EC2` instances and `RDS` databases
    * old `IAM` keys and service accounts
    * shadow `SaaS` and the corporate `IT` boundary
    * inventory as a security control
<!-- chapter: remediation-playbooks, duration: 2h -->
* Remediation playbooks
    * the public-bucket playbook
    * the over-permissive `IAM` playbook
    * the leaked-credential playbook
    * cross-reference to the Security Incident Response course
    * automated remediation and its dangers
<!-- chapter: program-design-and-metrics, duration: 3h -->
* Program design and metrics
    * the maturity model: visibility, prevention, response, hardening
    * `MTTR` for misconfigurations
    * coverage metrics
    * accountability and ownership routing
    * the executive dashboard that drives action
    * the developer-facing portal
    * cross-reference to the Engineering Metrics and `DORA` course
<!-- chapter: workshop-and-wrap-up, duration: 2h -->
* Workshop and wrap up
    * audit walkthrough of a sample cloud account
    * prioritization exercise on real `CSPM` findings
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
