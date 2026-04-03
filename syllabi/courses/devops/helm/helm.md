---
tags:
  - tools:helm
  - tools:kubernetes
  - practices:devops
level: intermediate
category: devops
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
---
<!-- course: helm -->
# `Helm`

## Description
This course provides a thorough introduction to `Helm`, the package manager for `Kubernetes`.
Students will learn how to create, manage, and deploy `Helm` charts, use template functions
and pipelines, manage chart dependencies, and work with chart repositories. The course also
covers release management, hooks, chart testing, Helmfile for managing multiple releases,
`OCI` registry support, and security best practices including chart signing and provenance
verification.

## Duration
16 hours / 1 day

## Intended Audience
* Software developers and `DevOps` engineers who work with `Kubernetes` and want to manage application deployments using `Helm`.
* Teams looking to standardize their `Kubernetes` deployment workflows.

## Prerequisites
* Working knowledge of `Kubernetes` concepts (pods, deployments, services, namespaces).
* Familiarity with `YAML` syntax.
* Basic command-line experience.

## Required Knowledge
* Introduction to `Kubernetes` (or equivalent experience)

## Objectives
* Understand `Helm` architecture and how it interacts with `Kubernetes`.
* Create, customize, and package `Helm` charts.
* Use template functions, pipelines, named templates, and partials effectively.
* Manage releases with install, upgrade, and rollback operations.
* Use Helmfile to manage multiple `Helm` releases declaratively.
* Apply security best practices including chart signing and provenance verification.

## Outline
<!-- chapter: helm-overview-and-architecture, duration: 1h -->
* `Helm` Overview and Architecture
    * What is `Helm`?
    * `Helm` 3 architecture (no Tiller)
    * How `Helm` interacts with the `Kubernetes` `API`
    * `Helm` `CLI` basics
    * Release concept and revision history
<!-- chapter: charts, duration: 1h -->
* Charts
    * Chart directory structure
    * Chart.`yaml` metadata
    * values.`yaml` and value overriding
    * Templates and rendered manifests
    * Chart packaging and versioning
<!-- chapter: creating-charts, duration: 1h -->
* Creating Charts
    * Scaffolding a new chart with `helm create`
    * Writing `Kubernetes` manifests as templates
    * Default values and schema validation
    * Chart linting with `helm lint`
<!-- chapter: template-functions-and-pipelines, duration: 1h -->
* Template Functions and Pipelines
    * Built-in template functions
    * Sprig library functions
    * Pipelines and chaining functions
    * Flow control (if, else, with, range)
    * Variables and scope
<!-- chapter: named-templates-and-partials, duration: 1h -->
* Named Templates and Partials
    * Defining named templates with define
    * Using include and template
    * The _helpers.tpl `file`
    * Template composition patterns
<!-- chapter: chart-dependencies, duration: 1h -->
* Chart Dependencies
    * Declaring dependencies in Chart.`yaml`
    * `helm dependency update` and `helm dependency build`
    * Condition and tags for optional dependencies
    * Overriding sub-chart values
    * Aliasing dependencies
<!-- chapter: chart-repositories, duration: 1h -->
* Chart Repositories
    * Repository structure and index files
    * Adding and managing repositories
    * Hosting a chart repository
    * ChartMuseum and alternatives
    * Searching for charts
<!-- chapter: helm-install-upgrade-and-rollback, duration: 1h -->
* `Helm` Install, Upgrade, and Rollback
    * `helm install` options and flags
    * `helm upgrade` and the --set / -f flags
    * `helm rollback` and revision selection
    * Atomic installs and upgrades
    * Wait and timeout configuration
<!-- chapter: release-management, duration: 1h -->
* Release Management
    * Listing and inspecting releases
    * Release history and diffs
    * Uninstalling releases
    * Keeping release history after uninstall
    * Namespace management
<!-- chapter: hooks, duration: 1h -->
* Hooks
    * What are `Helm` hooks?
    * Hook types: pre-install, post-install, pre-upgrade, post-upgrade, pre-delete, post-delete, pre-rollback, post-rollback
    * Hook weights and ordering
    * Hook deletion policies
    * Common hook use cases (database migrations, cache warming)
<!-- chapter: chart-testing, duration: 1h -->
* Chart Testing
    * Writing test pods
    * `helm test` command
    * Test hooks and annotations
    * Integration testing strategies
<!-- chapter: helmfile-for-managing-multiple-releases, duration: 1h -->
* Helmfile for Managing Multiple Releases
    * What is Helmfile?
    * helmfile.`yaml` structure
    * Defining multiple releases
    * Environment-specific values
    * `helmfile sync`, `helmfile diff`, and `helmfile apply`
<!-- chapter: oci-registry-support, duration: 1h -->
* `OCI` Registry Support
    * `OCI` artifacts and `Helm` charts
    * Pushing charts to `OCI` registries
    * Pulling and installing from `OCI` registries
    * Using `Docker Hub`, `ECR`, ACR, and GCR as chart registries
<!-- chapter: security, duration: 1h -->
* Security
    * Chart signing with GPG keys
    * Provenance files and verification
    * `helm verify` and `helm install --verify`
    * Best practices for secure chart distribution
    * Scanning charts for misconfigurations
<!-- chapter: best-practices, duration: 2h -->
* Best Practices
    * Chart naming and versioning conventions
    * Label and annotation standards
    * Resource requests and limits in templates
    * Reusable and composable chart design
    * Documentation and NOTES.txt

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
