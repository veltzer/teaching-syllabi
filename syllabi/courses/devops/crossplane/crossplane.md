---
tags:
  - tools:crossplane
  - tools:kubernetes
  - practices:devops
  - practices:automation
  - infrastructure:aws
  - infrastructure:azure
  - infrastructure:gcp
level: advanced
category: devops
duration_hours: 16
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: crossplane -->
# `Crossplane`

## Description
This course provides a comprehensive introduction to `Crossplane`, a `Kubernetes`-native
infrastructure as code framework. Participants will learn how to use `Crossplane` to provision
and manage cloud infrastructure across `AWS`, `Azure`, and `GCP` using `Kubernetes` APIs. The
course covers providers, managed resources, compositions, composite resource definitions,
and production deployment patterns, along with a comparison to traditional tools like `Terraform`.

## Duration
16 hours / 2 days

## Intended Audience
* `devops` engineers managing cloud infrastructure with `Kubernetes`.
* platform engineers building self-service infrastructure platforms.
* infrastructure teams evaluating `Kubernetes`-native IaC approaches.

## Prerequisites
* `solid` understanding of `Kubernetes` concepts (custom resources, controllers, `RBAC`).
* experience with at least one cloud provider (`AWS`, `Azure`, or `GCP`).
* familiarity with infrastructure as code concepts.

## Required Knowledge
* Introduction to `Kubernetes` (or equivalent experience)
* Introduction to `Azure` (or equivalent experience)
* `GCP` Fundamentals (or equivalent experience)

## Objectives
* understand `Crossplane` architecture and its role in `Kubernetes`-native infrastructure management.
* provision and manage cloud resources using `Crossplane` providers.
* build reusable infrastructure abstractions with compositions and XRDs.
* deploy and operate `Crossplane` in production environments.

## Outline
<!-- chapter: crossplane-overview, duration: 1h -->
* `Crossplane` overview
    * what is `Crossplane`
    * `Kubernetes`-native infrastructure as code
    * control plane of control planes
    * `Crossplane` vs traditional IaC tools
<!-- chapter: architecture, duration: 1h -->
* Architecture
    * providers and provider configurations
    * managed resources
    * composite resources
    * claims
    * control plane architecture
<!-- chapter: installing-crossplane, duration: 1h -->
* Installing `Crossplane`
    * installation with Helm
    * `Crossplane` `CLI`
    * verifying the installation
    * upgrading `Crossplane`
<!-- chapter: provider-configuration, duration: 1h -->
* Provider configuration
    * `AWS` provider setup
    * `Azure` provider setup
    * `GCP` provider setup
    * credential management
    * provider versioning
<!-- chapter: defining-managed-resources, duration: 1h -->
* Defining managed resources
    * creating cloud resources as `Kubernetes` objects
    * resource configuration and parameters
    * observing resource status
    * importing existing resources
    * deletion policies
<!-- chapter: compositions-and-xrds, duration: 2h -->
* Compositions and XRDs
    * composite resource definitions (XRDs)
    * building compositions
    * resource templates
    * patching and transforms
    * composition functions
<!-- chapter: claims, duration: 1h -->
* Claims
    * namespace-scoped resource requests
    * claim vs composite resource
    * self-service infrastructure patterns
    * claim lifecycle
<!-- chapter: environment-configs-and-usage-policies, duration: 1h -->
* Environment configs and usage policies
    * environment configurations
    * usage policies for resource protection
    * policy enforcement
<!-- chapter: crossplane-vs-terraform, duration: 2h -->
* `Crossplane` vs `Terraform`
    * architectural differences
    * reconciliation vs plan-apply
    * state management comparison
    * team workflow differences
    * migration considerations
<!-- chapter: rbac-and-multi-tenancy, duration: 1h -->
* `RBAC` and multi-tenancy
    * `RBAC` for `Crossplane` resources
    * namespace isolation
    * multi-tenant patterns
    * claim-based access control
<!-- chapter: testing-compositions, duration: 1h -->
* Testing compositions
    * unit testing with `crossplane`-`cli`
    * rendering and validating compositions
    * integration testing strategies
    * test automation
<!-- chapter: ci-cd-integration, duration: 1h -->
* `CI/CD` integration
    * `GitOps` workflows with `Crossplane`
    * integration with `ArgoCD` and `Flux`
    * pipeline `design patterns`
    * promotion across environments
<!-- chapter: production-best-practices, duration: 2h -->
* Production best practices
    * high availability setup
    * monitoring and observability
    * backup and disaster recovery
    * performance tuning
    * troubleshooting common issues

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
