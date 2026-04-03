---
tags:
  - tools:github
  - practices:devops
  - security:security
level: intermediate
category: devops
duration_hours: 16
audience:
  - audiences:devops
  - audiences:sysadmins
  - audiences:team-leads
  - audiences:security-professionals
---
<!-- course: github_administration -->
# `GitHub` Administration

## Description
This course covers the administration and governance of `GitHub` organizations. Participants will learn how to manage teams and permissions, configure branch protection rules and required reviews, set up self-hosted Actions runners, manage secrets, and leverage `GitHub` Advanced Security features including `Dependabot`, code scanning, and audit logging. The course also provides an overview of `GitHub` Enterprise Server (GHES) for on-premise deployments.

## Duration
16 hours / 1 day

## Intended Audience
* `DevOps` engineers responsible for managing `GitHub` organizations and repositories.
* System administrators overseeing `GitHub` infrastructure and access control.
* Team leads managing development workflows and repository policies.
* Security professionals implementing code security and compliance on `GitHub`.

## Prerequisites
* Basic familiarity with `Git` and version control concepts.
* Experience working in software development teams.

## Objectives
* Configure and manage `GitHub` organizations, teams, and permissions.
* Set up branch protection rules and enforce code review policies.
* Deploy and manage Actions self-hosted runners.
* Implement secret management best practices.
* Enable and configure `GitHub` Advanced Security features.
* Monitor organizational activity with audit logging.
* Understand `GitHub` Enterprise Server deployment options.

## Outline
<!-- chapter: organization-management, duration: 1h -->
* Organization Management
    * Creating and configuring organizations
    * Organization settings and policies
    * Repository creation rules
    * Default repository permissions
    * Organization-level templates
<!-- chapter: teams-and-permissions, duration: 1h -->
* Teams and Permissions
    * Team structure and hierarchy
    * Repository access levels
    * Team synchronization with identity providers
    * Custom repository roles
    * CODEOWNERS files
<!-- chapter: branch-protection-rules, duration: 2h -->
* Branch Protection Rules
    * Configuring branch protection
    * Required status checks
    * Required reviews and approvals
    * Signed commits enforcement
    * Restricting push access
    * Rulesets
<!-- chapter: actions-self-hosted-runners, duration: 1h -->
* Actions Self-Hosted Runners
    * Self-hosted runner architecture
    * Installing and configuring runners
    * Runner groups and labels
    * Scaling runners with auto-scaling solutions
    * Security considerations for self-hosted runners
<!-- chapter: secret-management, duration: 1h -->
* Secret Management
    * Organization, repository, and environment secrets
    * Actions secrets and variables
    * Using `OIDC` for cloud authentication
    * Secret scanning and alerts
    * Best practices for credential management
<!-- chapter: github-apps, duration: 1h -->
* `GitHub` Apps
    * `GitHub` Apps vs `OAuth` Apps
    * Creating and installing `GitHub` Apps
    * App permissions and events
    * Managing `GitHub` App installations
<!-- chapter: audit-logging, duration: 2h -->
* Audit Logging
    * Organization audit log
    * Streaming audit logs
    * Monitoring user and repository activity
    * Compliance and regulatory requirements
    * `API`-based audit log access
<!-- chapter: github-advanced-security-ghas, duration: 1h -->
* `GitHub` Advanced Security (GHAS)
    * Overview of GHAS features
    * Enabling GHAS for organizations
    * Licensing and seat management
<!-- chapter: dependabot, duration: 2h -->
* `Dependabot`
    * `Dependabot` alerts
    * `Dependabot` security updates
    * `Dependabot` version updates
    * Configuring `Dependabot` with `dependabot`.yml
    * Reviewing and merging `Dependabot` pull requests
<!-- chapter: code-scanning, duration: 2h -->
* Code Scanning
    * `CodeQL` analysis
    * Setting up code scanning workflows
    * Custom queries and configurations
    * Third-party scanning tool integration
    * Managing code scanning alerts
<!-- chapter: github-enterprise-server-ghes-overview, duration: 2h -->
* `GitHub` Enterprise Server (GHES) Overview
    * GHES vs `GitHub`.com
    * Deployment options and requirements
    * High availability and disaster recovery
    * Authentication and `LDAP`/`SAML` integration
    * Migrating between GHES and `GitHub`.com

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
