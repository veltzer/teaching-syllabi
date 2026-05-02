---
tags:
  - tools:argo-cd
  - tools:kubernetes
  - concepts:gitops
  - practices:devops
level: advanced
category: devops
duration_hours: 16
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: advanced_argo_cd -->
# Advanced `Argo CD`

## Description
This advanced course takes students deep into `Argo CD`, the declarative `GitOps` continuous
delivery tool for `Kubernetes`. The course goes beyond basic application deployment to cover
enterprise-grade patterns, multi-cluster management, and advanced deployment strategies.

Students will learn how to scale `Argo CD` for large organizations using ApplicationSets,
the App of Apps pattern, and `Argo Rollouts` for progressive delivery. The course also
covers high availability, security, notifications, and operational best practices for
running `Argo CD` at scale.

## Duration
16 hours / 2 days

## Intended Audience
* `DevOps` engineers who are already using `Argo CD` and want to deepen their expertise for enterprise-scale deployments.
* Teams adopting `GitOps` practices across multiple clusters and environments.

## Prerequisites
* Working experience with `Argo CD` (basic application creation and sync).
* Strong understanding of `Kubernetes` (deployments, services, `RBAC`, CRDs).
* Familiarity with Helm and/or `Kustomize`.
* Understanding of `Git` workflows and branching strategies.

## Required Knowledge
* Introduction to `Kubernetes` (or equivalent experience)
* Introduction to `Git` (or equivalent experience)
* Helm (or equivalent experience)

## Objectives
* Design and implement advanced `Argo CD` deployment patterns.
* Use ApplicationSets for dynamic, multi-cluster application management.
* Implement progressive delivery with `Argo Rollouts`.
* Configure high availability and disaster recovery for `Argo CD`.
* Integrate `Argo CD` with SSO, `RBAC`, and notification systems.
* Apply `GitOps` best practices at organizational scale.

## Outline
<!-- chapter: argo-cd-architecture-deep-dive, duration: 1h -->
* `Argo CD` Architecture Deep Dive
    * Application controller internals
    * Repo server and caching
    * `Redis` and state management
    * `API` server and `gRPC`
    * Custom resource definitions
    * Reconciliation loop and sync process
<!-- chapter: applicationsets, duration: 1h -->
* ApplicationSets
    * ApplicationSet controller overview
    * List generator
    * Cluster generator
    * `Git` generator (directories and files)
    * Matrix and merge generators
    * Pull request generator
    * SCM provider generator
    * Template overrides
    * Progressive rollouts with ApplicationSets
<!-- chapter: multi-cluster-management, duration: 1h -->
* Multi-Cluster Management
    * Registering external clusters
    * Cluster credentials and secrets
    * Hub and spoke topology
    * Cluster-scoped vs namespace-scoped resources
    * Network considerations and firewalls
<!-- chapter: app-of-apps-pattern, duration: 1h -->
* App of Apps Pattern
    * Pattern overview and use cases
    * Bootstrap application structure
    * Managing application lifecycle
    * Dependency management between apps
    * Organizing repositories for App of Apps
<!-- chapter: sync-waves-and-hooks, duration: 1h -->
* Sync Waves and Hooks
    * Sync phases (pre-sync, sync, post-sync)
    * Sync wave ordering
    * Resource hooks (PreSync, Sync, PostSync, SyncFail)
    * Skip and prune policies
    * Selective sync and targeted refresh
<!-- chapter: custom-health-checks, duration: 1h -->
* Custom Health Checks
    * Built-in health assessments
    * Writing custom `Lua` health checks
    * Health check for CRDs
    * Degraded vs progressing vs healthy states
<!-- chapter: config-management-plugins, duration: 1h -->
* Config Management Plugins
    * Plugin architecture (sidecar model)
    * Writing custom CMP plugins
    * Plugin discovery and configuration
    * Use cases for custom plugins
<!-- chapter: argo-cd-with-helm-and-kustomize, duration: 1h -->
* `Argo CD` with Helm and `Kustomize`
    * Helm value files and overrides
    * Helm hooks vs `Argo CD` hooks
    * `Kustomize` overlays and patches
    * Combining Helm with `Kustomize`
    * Managing Helm chart repositories
<!-- chapter: image-updater, duration: 1h -->
* Image Updater
    * `Argo CD` Image Updater architecture
    * Update strategies (semver, latest, digest)
    * Registry configuration
    * Write-back methods (`Git`, annotation)
    * Filtering and constraining updates
<!-- chapter: notifications-engine, duration: 1h -->
* Notifications Engine
    * Notification architecture
    * Configuring triggers and templates
    * Slack, email, and webhook integrations
    * Custom notification templates
    * Subscription management
<!-- chapter: rbac-and-sso-integration, duration: 1h -->
* `RBAC` and SSO Integration
    * `Argo CD` `RBAC` policies
    * Project-level access control
    * SSO with `OIDC` and `SAML`
    * Dex configuration
    * Group-based role mapping
    * Audit logging
<!-- chapter: high-availability-setup, duration: 1h -->
* High Availability Setup
    * HA architecture overview
    * Scaling the application controller
    * Sharding strategies
    * `Redis` HA configuration
    * Resource requirements and limits
<!-- chapter: disaster-recovery, duration: 1h -->
* Disaster Recovery
    * Backup strategies
    * Exporting and importing applications
    * Recovering from cluster failures
    * `Git` as the source of truth for recovery
<!-- chapter: argo-rollouts, duration: 1h -->
* `Argo Rollouts`
    * Rollout resource overview
    * Canary deployment strategy
    * Blue-green deployment strategy
    * Analysis templates and runs
    * Integration with metric providers
    * Traffic management with `Istio` and `Nginx`
    * Rollback strategies
<!-- chapter: metrics-and-monitoring, duration: 1h -->
* Metrics and Monitoring
    * `Argo CD` `Prometheus` metrics
    * Key metrics to monitor
    * `Grafana` dashboard setup
    * Alerting on sync failures and drift
    * Performance monitoring at scale
<!-- chapter: gitops-best-practices-at-scale, duration: 1h -->
* `GitOps` Best Practices at Scale
    * Repository structure strategies (monorepo vs multi-repo)
    * Environment promotion workflows
    * Secrets management in `GitOps`
    * Drift detection and reconciliation
    * Change management and approval gates
    * Governance and compliance

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
