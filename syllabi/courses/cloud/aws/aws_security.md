---
tags:
  - infrastructure:aws
  - infrastructure:cloud
  - security:security
  - security:iam
  - security:compliance
level: intermediate
category: cloud
duration_hours: 24
audience:
  - audiences:sysadmins
  - audiences:security-professionals
  - audiences:devops
---
<!-- course: aws_security -->
<!-- Track gaps: AWS Organization and Landing Zone, interfacing other identity systems, AWS SSO (Identity Center) deep dive -->
# `AWS` Security

## Description
This course provides a comprehensive deep dive into securing workloads on `AWS`. It covers identity and access management, threat detection, data protection, network security, and compliance automation. Students will learn how to design and implement a robust security posture on `AWS` using native services and best practices, and how to respond effectively to security incidents in cloud environments.

## Duration
24 hours / 3 days

## Intended Audience
* Cloud engineers responsible for securing `AWS` environments.
* Security professionals transitioning to cloud security.
* `DevOps` engineers looking to integrate security into their pipelines.

## Prerequisites
* Working knowledge of `AWS` core services (`EC2`, `S3`, `VPC`, `Lambda`).
* Basic understanding of networking and security concepts.
* Familiarity with the `AWS` Management Console and `CLI`.

## Objectives
* Design and implement fine-grained access control using `IAM`.
* Configure threat detection and continuous monitoring across `AWS` accounts.
* Protect data at `rest` and in transit using `AWS` encryption services.
* Implement network security controls using `WAF` and Shield.
* Automate compliance checks and remediation.
* Plan and execute incident response procedures on `AWS`.

## Outline
<!-- chapter: identity-and-access-management-deep-dive, duration: 3h -->
* Identity and Access Management Deep Dive
    * `IAM` users, groups, and roles
    * Policy language and evaluation logic
    * Permission boundaries and service control policies
    * Cross-account access patterns
    * `IAM` Access Analyzer
    * Federation and SSO with `AWS IAM Identity Center`
    * Best practices for least privilege
<!-- chapter: aws-cloudtrail-and-logging, duration: 3h -->
* `AWS CloudTrail` and Logging
    * Configuring CloudTrail for multi-region and multi-account
    * Log integrity validation
    * Integration with `CloudWatch Logs`
    * Querying trails with Athena
    * `VPC` Flow Logs and `S3` access logs
<!-- chapter: threat-detection-with-amazon-guardduty, duration: 3h -->
* Threat Detection with `Amazon GuardDuty`
    * Enabling and configuring GuardDuty
    * Understanding finding types and severity
    * Multi-account management with `AWS Organizations`
    * Automated response with EventBridge and `Lambda`
    * Suppression rules and trusted `IP` lists
<!-- chapter: aws-security-hub, duration: 3h -->
* `AWS Security Hub`
    * Aggregating findings across services
    * Security standards and controls
    * CIS `AWS` Foundations Benchmark
    * Custom actions and automated remediation
    * Integration with third-party tools
<!-- chapter: aws-config-and-compliance, duration: 3h -->
* `AWS Config` and Compliance
    * Config rules and conformance packs
    * Custom rules with `Lambda`
    * Remediation actions
    * Multi-account compliance with aggregators
    * Mapping to compliance frameworks (`SOC` 2, `PCI` DSS, `HIPAA`)
<!-- chapter: network-security, duration: 3h -->
* Network Security
    * `AWS WAF` rules and web `ACLs`
    * Rate-based rules and bot control
    * `AWS Shield` Standard and Advanced
    * `DDoS` response best practices
    * Security groups and network `ACLs` hardening
    * `AWS Network Firewall`
<!-- chapter: data-protection-and-encryption, duration: 3h -->
* Data Protection and Encryption
    * `AWS KMS` key types and key policies
    * Envelope encryption
    * Customer managed keys vs `AWS` managed keys
    * `KMS` grants and cross-account key sharing
    * `AWS Certificate Manager`
    * `S3` encryption options and bucket policies
    * `Secrets Manager` and `Parameter Store`
<!-- chapter: incident-response-on-aws, duration: 3h -->
* Incident Response on `AWS`
    * Building an incident response plan for cloud
    * Forensic investigation with `EC2` snapshots
    * Isolating compromised resources
    * Automating containment with `Lambda` and `Step Functions`
    * Post-incident analysis and lessons learned
    * `AWS` support and abuse reporting

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
