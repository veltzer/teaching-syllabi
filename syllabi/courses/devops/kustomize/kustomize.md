---
tags:
  - tools:kustomize
  - infrastructure:kubernetes
  - practices:devops
  - practices:gitops
level: intermediate
category: devops
duration_hours: 8
audience:
  - audiences:devops
  - audiences:developers
---
<!-- course: kustomize -->
# `Kustomize`

## Description
`Kustomize` is a `Kubernetes`-native configuration management tool that allows teams to
customize application manifests without templates or forking, using a purely declarative,
patch-based approach. This one-day course teaches participants how to structure `Kustomize`
bases and overlays to manage environment-specific configuration (development, staging,
production) from a single source of truth. Participants will learn how to apply strategic
merge patches and `JSON6902` patches, generate `ConfigMaps` and `Secrets` from files and
literals, and compose Helm charts with `Kustomize` post-rendering. The course ends with
practical patterns for integrating `Kustomize` into `CI/CD` pipelines and `GitOps` workflows.

## Duration
8 hours / 1 day

## Intended Audience
* `DevOps` engineers and platform engineers managing `Kubernetes` application manifests.
* Developers responsible for configuring and deploying their own services to `Kubernetes`.
* Teams adopting `GitOps` tooling such as `Flux` or `ArgoCD`.

## Prerequisites
* Working knowledge of `Kubernetes` resources: Deployment, Service, ConfigMap, `Secret`.
* Comfortable writing and editing `YAML` files.
* Basic familiarity with `Git` and pull-request workflows.
* `kubectl` installed and configured against a `Kubernetes` cluster.

## Objectives
* Understand the `Kustomize` philosophy and how it differs from Helm templating.
* Build reusable base configurations and environment-specific overlays.
* Apply strategic merge patches and `JSON6902` patches to customize resources.
* Generate `ConfigMaps` and `Secrets` dynamically with built-in generators.
* Combine Helm chart rendering with `Kustomize` post-render hooks.
* Integrate `Kustomize` into automated deployment pipelines and `GitOps` tools.

## Outline
<!-- chapter: introduction-to-kustomize, duration: 1h -->
* Introduction to `Kustomize`
    * Why configuration management matters for `Kubernetes`
    * `Kustomize` vs. Helm: templating vs. patching philosophies
    * `kustomize` `CLI` and `kubectl` built-in integration
    * The `kustomization.yaml` file: structure and required fields

<!-- chapter: kustomize-structure-and-bases, duration: 2h -->
* `Kustomize` Structure and Bases
    * Designing a base directory with shared `Kubernetes` manifests
    * Referencing remote bases from `Git` URLs
    * Common field transformers: `namePrefix`, nameSuffix, namespace, `labels`
    * Image transformers for managing container image tags across environments

<!-- chapter: patches-and-overlays, duration: 2h -->
* Patches and Overlays
    * Strategic merge patches for modifying existing resource fields
    * `JSON6902` patches for precise add, replace, and remove operations
    * Overlay directory layout for dev, staging, and production
    * Composing multiple patches and understanding merge order

<!-- chapter: configmapgenerator-and-secretgenerator, duration: 1h -->
* `ConfigMapGenerator` and `SecretGenerator`
    * Generating `ConfigMaps` from files, literals, and environment files
    * Generating `Secrets` and understanding hash suffixes for rollout triggers
    * Controlling `generatorOptions`: disabling hash suffix, adding labels
    * Managing sensitive values without committing them to `Git`

<!-- chapter: helm-charts-with-kustomize, duration: 1h -->
* Helm Charts with `Kustomize`
    * `helmCharts` field: rendering Helm charts as `Kustomize` bases
    * Post-render patching of Helm-generated manifests
    * Inflating charts locally vs. using remote chart repositories
    * Tradeoffs of combining Helm and `Kustomize`

<!-- chapter: kustomize-in-ci-cd-pipelines, duration: 1h -->
* `Kustomize` in `CI/CD` Pipelines
    * Building and validating manifests with `kustomize build`
    * Diffing rendered output with `kubectl diff`
    * Integrating `Kustomize` into `GitHub Actions`, `GitLab CI`, and `Tekton`
    * `Kustomize` as a `Flux` and `ArgoCD` rendering engine

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
