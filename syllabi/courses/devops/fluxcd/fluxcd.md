---
tags:
  - tools:fluxcd
  - infrastructure:gitops
  - infrastructure:kubernetes
  - practices:devops
  - practices:continuous-delivery
level: intermediate
category: devops
duration_hours: 16
audience:
  - audiences:devops
  - audiences:developers
---
<!-- course: fluxcd -->
# `Flux CD`

## Description
`Flux CD` is a `CNCF` graduated tool that implements `GitOps` for `Kubernetes`, keeping
cluster state continuously synchronized with configuration stored in `Git` repositories.
This course provides a comprehensive introduction to `Flux v2`, covering its modular
controller-based architecture and the full set of controllers: Source, `Kustomize`, `Helm`,
and Notification. Participants will learn how to `bootstrap` `Flux` into a cluster, manage
application delivery through `Kustomizations` and `HelmReleases`, and implement secure
multi-tenant workflows. The course also covers progressive delivery strategies with
`Flagger` and positions `Flux` against `ArgoCD` to help teams `make` informed tooling decisions.

## Duration
16 hours / 2 days

## Intended Audience
* `DevOps` engineers who want to implement `GitOps` workflows on `Kubernetes`.
* Platform engineers building self-service delivery platforms for development teams.
* Developers who need to understand how their applications are continuously delivered.

## Prerequisites
* Practical experience with `Kubernetes` (deployments, services, namespaces, `RBAC`).
* Familiarity with `Helm` charts and `Kustomize` overlays.
* Comfortable working with `Git` workflows and pull requests.
* Basic understanding of `YAML` and `Kubernetes` manifests.

## Objectives
* Understand the `GitOps` principles and how `Flux` implements them on `Kubernetes`.
* `Bootstrap` and configure `Flux` in a `Kubernetes` cluster using the `flux` `CLI`.
* Manage application delivery with the `Kustomize` and `Helm` controllers.
* Implement multi-tenancy isolation and least-privilege access policies.
* Set up alerts and notifications using the Notification controller.
* Apply progressive delivery patterns with `Flagger` for safe automated rollouts.

## Outline
<!-- chapter: introduction-to-gitops, duration: 1h -->
* Introduction to `GitOps`
    * `GitOps` principles: declarative, versioned, automated, and continuously reconciled
    * Push vs. pull-based delivery models
    * Benefits of `GitOps` for security, auditability, and drift prevention
    * Overview of the `GitOps` tooling landscape

<!-- chapter: flux-architecture-and-components, duration: 2h -->
* `Flux` Architecture and Components
    * `Flux v2` design: composable controllers vs. the monolithic v1 approach
    * The source, `kustomize`, `helm`, notification, and image automation controllers
    * `Flux` custom resources: `GitRepository`, `Kustomization`, `HelmRelease`, `Alert`
    * How `Flux` reconciles desired state with cluster state

<!-- chapter: installing-and-bootstrapping-flux, duration: 2h -->
* Installing and Bootstrapping `Flux`
    * Prerequisites: `kubectl`, `flux` `CLI`, and `Git` provider access
    * Bootstrapping `Flux` with `GitHub`, `GitLab`, and `Gitea`
    * Repository structure conventions for `Flux` management
    * Verifying and troubleshooting the `bootstrap` installation

<!-- chapter: kustomization-controller, duration: 2h -->
* `Kustomization` Controller
    * The `Kustomization` custom resource and its fields
    * Health checks, timeout, and retry configuration
    * Dependency ordering between `Kustomizations`
    * Pruning and garbage collection of removed resources

<!-- chapter: helm-controller, duration: 2h -->
* `Helm` Controller
    * `HelmRepository` and `HelmChart` source resources
    * Writing `HelmRelease` manifests with value overrides
    * Upgrade strategies and rollback policies
    * Managing secrets for private `Helm` registries with `SOPS` or `Sealed Secrets`

<!-- chapter: source-controller, duration: 2h -->
* Source Controller
    * Supported source types: `GitRepository`, `OCIRepository`, `Bucket`
    * Interval-based polling and webhook-triggered reconciliation
    * Verifying `Git` commit signatures and `OCI` artifact digests
    * Artifact caching and how other controllers consume source artifacts

<!-- chapter: notification-controller, duration: 1h -->
* Notification Controller
    * `Provider` resources: `Slack`, `Microsoft Teams`, `PagerDuty`, `GitHub` commit status
    * Writing `Alert` resources to filter and route events
    * Sending notifications on reconciliation success and failure
    * Using `Receiver` resources for inbound webhook triggers

<!-- chapter: multi-tenancy-with-flux, duration: 2h -->
* Multi-Tenancy with `Flux`
    * Tenant isolation using namespaces and service accounts
    * Restricting `Kustomizations` with `serviceAccountName` impersonation
    * Repository-per-team and monorepo patterns
    * `Flux` `RBAC`: limiting controller permissions with `ClusterRoles`

<!-- chapter: flux-vs-argocd-comparison, duration: 1h -->
* `Flux` vs. `ArgoCD` Comparison
    * Architectural differences: `CLI`-first vs. UI-first
    * Feature parity: multi-tenancy, image automation, progressive delivery
    * Integration points with broader `CNCF` tooling
    * Guidance for choosing between `Flux` and `ArgoCD`

<!-- chapter: progressive-delivery-with-flagger, duration: 1h -->
* Progressive Delivery with `Flagger`
    * `Flagger` deployment strategies: canary, blue/green, A/B testing
    * Integrating `Flagger` with `Flux` `HelmReleases`
    * Configuring analysis metrics and rollback thresholds
    * Observing canary rollout progress and handling failures

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
