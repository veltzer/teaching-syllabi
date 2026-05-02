---
tags:
  - practices:devops
  - practices:ci-cd
  - tools:argo-cd
  - practices:gitops
  - infrastructure:kubernetes
  - infrastructure:cloud
level: intermediate
category: devops
duration_hours: 16
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: argocd_and_gitops -->
# `ArgoCD` & `GitOps`

## Description
This course introduces the `GitOps` methodology and its practical implementation using `ArgoCD`
as a declarative `continuous delivery` tool for `Kubernetes`. Participants will learn how to manage
application deployments through `Git` repositories as the single source of truth, configure
`ArgoCD` application sets and sync policies, handle multi-cluster deployments, and implement
progressive delivery strategies.

This course assumes participants have working knowledge of `Kubernetes` and `Git`. It focuses on
the operational and architectural aspects of `GitOps` rather than basic `Kubernetes` concepts.

## Duration
16 hours / 1 day

## Intended Audience
* `DevOps` engineers adopting `GitOps` practices for `Kubernetes` deployments.
* platform engineers building `continuous delivery` platforms.
* developers who deploy applications to `Kubernetes` and want to understand `GitOps` workflows.
* SREs looking to improve deployment reliability and auditability.

## Prerequisites
* Working knowledge of `Kubernetes` (deployments, services, namespaces, `kubectl`).
* `Solid` understanding of `Git` workflows (branching, pull requests).
* Familiarity with `YAML` and `Kubernetes` manifests.
* Basic understanding of Helm or `Kustomize` is helpful.

## Required Knowledge
* Introduction to `Kubernetes` (or equivalent experience)
* Helm (or equivalent experience)

## Objectives
* understand the core concepts and principles of `GitOps`
* gain practical knowledge of `ArgoCD` installation, configuration, and operations
* gain practical knowledge of application sets, sync policies, and multi-cluster management
* gain practical knowledge of progressive delivery patterns with `GitOps`

## Outline
<!-- chapter: introduction-to-gitops, duration: 1h -->
* Introduction to `GitOps`
    * What is `GitOps` and its core principles
    * Push-based vs pull-based deployment models
    * `Git` as the single source of truth
    * Benefits of declarative infrastructure
    * Comparing `GitOps` tools (`ArgoCD`, `Flux`, `Jenkins X`)
<!-- chapter: argocd-architecture-and-installation, duration: 1h -->
* `ArgoCD` Architecture and Installation
    * `ArgoCD` components and architecture
    * Installation methods (Helm, manifests, operator)
    * `ArgoCD` `CLI` and web UI
    * Authentication and authorization
    * `RBAC` configuration
<!-- chapter: applications-in-argocd, duration: 3h -->
* Applications in `ArgoCD`
    * Defining applications
    * Source repositories and target clusters
    * Manifest generation tools
        * Plain `YAML` manifests
        * Helm charts
        * `Kustomize` overlays
        * Jsonnet
    * Application health and status
    * Application metadata and labels
<!-- chapter: sync-policies-and-strategies, duration: 2h -->
* Sync Policies and Strategies
    * Manual vs automated sync
    * Self-healing and auto-prune
    * Sync `windows` and scheduling
    * Sync phases and hooks (pre-sync, sync, post-sync)
    * Retry policies
    * Selective sync and resource tracking
<!-- chapter: application-sets, duration: 3h -->
* Application Sets
    * What are application sets and why use them
    * Generators
        * List generator
        * Cluster generator
        * `Git` directory and file generators
        * Matrix and merge generators
    * Templates and overrides
    * Progressive rollouts with application sets
<!-- chapter: multi-cluster-management, duration: 1h -->
* Multi-Cluster Management
    * Registering and managing clusters
    * Cluster credentials and authentication
    * Deploying across multiple clusters
    * Cluster-specific configurations
    * Hub and spoke patterns
<!-- chapter: repository-and-secret-management, duration: 1h -->
* Repository and Secret Management
    * Repository credentials and access
    * Private repository configuration
    * Secret management with `ArgoCD`
    * Integration with external secret managers (Vault, `Sealed Secrets`, `External Secrets Operator`)
<!-- chapter: progressive-delivery, duration: 2h -->
* Progressive Delivery
    * Introduction to progressive delivery concepts
    * `Argo Rollouts` overview
    * Canary deployments with `ArgoCD`
    * Blue/green deployments
    * Analysis and metrics-driven promotion
    * Rollback strategies
<!-- chapter: gitops-workflows-and-best-practices, duration: 2h -->
* `GitOps` Workflows and Best Practices
    * Repository structure patterns (app-of-apps, monorepo, polyrepo)
    * Environment promotion strategies
    * Drift detection and reconciliation
    * Disaster recovery and backup
    * Audit trails and compliance
    * Notification and alerting integration

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
