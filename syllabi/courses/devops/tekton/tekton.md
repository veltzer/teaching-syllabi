---
tags:
  - tools:tekton
  - infrastructure:ci-cd
  - infrastructure:kubernetes
  - practices:devops
level: intermediate
category: devops
duration_hours: 16
audience:
  - audiences:devops
  - audiences:developers
---
<!-- course: tekton -->
# `Tekton`

## Description
`Tekton` is a cloud-native, `Kubernetes`-native framework for building `CI/CD` systems,
providing first-class `Kubernetes` custom resources for defining and running pipelines
entirely within the cluster. This course introduces participants to the complete `Tekton`
ecosystem, from authoring reusable `Tasks` and composing them into `Pipelines`, through
triggering those pipelines in response to `Git` and webhook events with `Tekton Triggers`.
Participants will learn how to share artifacts between steps using workspaces, reuse
community-verified automation from `Tekton Hub`, and secure their pipelines with `RBAC` and
`Tekton Chains` for end-to-end software supply chain security. The course concludes with a
comparison of `Tekton` against `Jenkins` and `GitHub Actions` to help teams choose the
right tool for their context.

## Duration
16 hours / 2 days

## Intended Audience
* `DevOps` engineers building or migrating `CI/CD` pipelines to `Kubernetes`.
* Platform engineers creating self-service pipeline infrastructure for development teams.
* Developers who want to understand how cloud-native pipelines are structured and executed.

## Prerequisites
* Working knowledge of `Kubernetes` (pods, deployments, `RBAC`, persistent volumes).
* Familiarity with `YAML` and `Kubernetes` manifest authoring.
* Basic understanding of `CI/CD` concepts (build, test, push, deploy).
* `kubectl` installed and configured against a `Kubernetes` cluster.

## Objectives
* Understand the `Tekton` resource model and how it maps `CI/CD` concepts to `Kubernetes`.
* Write reusable `Tasks` and compose them into multi-stage `Pipelines`.
* Share data between steps and tasks using workspaces and persistent volume claims.
* Automate pipeline execution in response to external events with `Tekton Triggers`.
* Discover and integrate community tasks from `Tekton Hub`.
* Secure pipelines with `RBAC` and software supply chain attestations via `Tekton Chains`.

## Outline
<!-- chapter: introduction-to-cloud-native-ci-cd, duration: 1h -->
* Introduction to Cloud-Native `CI/CD`
    * Evolution from traditional `CI/CD` servers to cloud-native approaches
    * Why `Kubernetes`-native pipelines: scalability, isolation, and declarative configuration
    * Overview of the `Tekton` project, governance, and `CNCF` status
    * Key concepts: immutable infrastructure, ephemeral build environments

<!-- chapter: tekton-architecture, duration: 2h -->
* `Tekton` Architecture
    * Core custom resources: `Task`, `TaskRun`, `Pipeline`, `PipelineRun`
    * `Tekton Triggers`: `EventListener`, `TriggerBinding`, `TriggerTemplate`
    * `Tekton Chains` for supply chain security
    * `Tekton` Dashboard for visualizing pipeline runs
    * Controller architecture and how `Tekton` manages pod lifecycle

<!-- chapter: tasks-and-steps, duration: 2h -->
* Tasks and Steps
    * Anatomy of a `Task`: steps, params, results, and sidecars
    * Writing steps with arbitrary container images
    * Passing parameters and consuming `Task` results
    * `StepAction` resources for reusable step definitions
    * Debugging failing `TaskRuns` with `kubectl` logs and events

<!-- chapter: pipelines-and-pipelineruns, duration: 2h -->
* Pipelines and `PipelineRuns`
    * Composing `Tasks` into a `Pipeline` with sequential and parallel execution
    * Passing results between `Tasks` in a `Pipeline`
    * when expressions for conditional task execution
    * `finally` tasks for cleanup and notification regardless of outcome
    * `PipelineRun` timeouts, retries, and cancellation

<!-- chapter: workspaces-and-resources, duration: 2h -->
* Workspaces and Resources
    * Workspace types: `PersistentVolumeClaim`, `emptyDir`, `Secret`, `ConfigMap`
    * Declaring and binding workspaces in `Tasks` and `Pipelines`
    * Sharing source code and build artifacts across tasks
    * Volume claim templates for per-`PipelineRun` storage provisioning

<!-- chapter: triggers-and-eventlisteners, duration: 2h -->
* Triggers and `EventListeners`
    * `EventListener` deployment and service exposure
    * `TriggerBinding` extracting fields from webhook payloads
    * `TriggerTemplate` creating `PipelineRuns` from trigger data
    * Interceptors: `CEL`, `GitHub`, `GitLab`, and custom webhook validation
    * Securing `EventListeners` with secret-based payload verification

<!-- chapter: tekton-catalog-and-hub, duration: 2h -->
* `Tekton` Catalog and Hub
    * Browsing and installing tasks from `Tekton Hub`
    * Commonly used tasks: `git-clone`, `buildah`, `kaniko`, `helm-upgrade-from-repo`
    * Versioning catalog tasks with bundle references
    * Contributing tasks back to the community catalog

<!-- chapter: security-in-tekton, duration: 1h -->
* Security in `Tekton`
    * `RBAC` for `TaskRuns` and `PipelineRuns`: service accounts and roles
    * Running steps as non-root with security contexts
    * Managing `Docker` registry credentials as `Kubernetes` secrets
    * Network policies for `Tekton` workloads

<!-- chapter: tekton-chains-for-supply-chain-security, duration: 1h -->
* `Tekton Chains` for Supply Chain Security
    * Software supply chain threats and the `SLSA` framework
    * How `Tekton Chains` captures and signs provenance attestations
    * Configuring signers: `x509`, `KMS`, and `Sigstore` / `cosign`
    * Verifying attestations and integrating with policy engines

<!-- chapter: comparing-tekton-with-jenkins-and-github-actions, duration: 1h -->
* Comparing `Tekton` with `Jenkins` and `GitHub Actions`
    * Architectural differences: controller-based vs. agent-based vs. hosted runners
    * Developer experience: `YAML` verbosity, reusability, and discoverability
    * Ecosystem maturity: plugins, community tasks, and integrations
    * Decision framework: when to choose `Tekton`, `Jenkins`, or `GitHub Actions`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
