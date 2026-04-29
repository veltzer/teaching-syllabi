---
tags:
  - concepts:gitops
  - concepts:operations
  - concepts:best-practices
  - concepts:distributed-systems
level: advanced
category: containers
duration_hours: 32
audience:
  - audiences:devops
  - audiences:senior-developers
  - audiences:sres
  - audiences:architects
---
<!-- course: kubernetes_operator_development -->
# `Kubernetes` Operator Development

## Description
The catalog has `Kubernetes`, `Kubernetes for Developers`, `Kubernetes Troubleshooting`, and the
related `Helm`, `Kustomize`, `ArgoCD` material. None of those covers the discipline of building a
`Kubernetes` operator: a controller that extends `Kubernetes` with custom resources and automates the
operational knowledge of running a stateful workload. Operators are the way that databases, message
queues, `ML` platforms, and internal `PaaS` services get exposed to `Kubernetes` users with a
declarative `API` that respects the platform's conventions.

This four day course covers operator development end-to-end. It covers the controller pattern and the
reconciliation loop, the choice of framework (`controller-runtime`, `Kubebuilder`, `Operator SDK`,
`KUDO`, `Metacontroller`), `CRD` design (versioning, validation, defaulting, conversion webhooks),
the watch and the work queue, the level-based vs edge-based controller, finalizers and garbage
collection, leader election, the operator capability levels (the `OperatorHub` model), the testing
story (`envtest`, `kuttl`, `chainsaw`), the upgrade story for both the operator and the operand, the
release model (`Helm` chart vs `OLM` bundle), and the operational patterns for shipping an operator
that other teams will run. Examples are drawn from the `Strimzi` (`Kafka`), `Cloudnative-PG`
(`Postgres`), `Prometheus` operator, and `Crossplane` operator codebases. Participants leave able to
ship an operator that respects `Kubernetes` conventions and survives contact with users.

## Duration
32 hours / 4 days

## Intended Audience
* platform engineers building internal `Kubernetes` paved roads
* senior developers writing operators for stateful workloads
* `DevOps` engineers maintaining or extending operators
* `SRE` running operators in production

## Prerequisites
* `solid` `Kubernetes` knowledge (the `Kubernetes` and `Kubernetes for Developers` courses)
* working `Go` experience
* familiarity with the `Helm` and `Kustomize` material
* exposure to `Crossplane` or `ArgoCD` is helpful

## Objectives
* design a `CRD` that respects `Kubernetes` `API` conventions
* build a controller with the reconciliation loop done correctly
* handle finalizers, deletion, and garbage collection
* test an operator with `envtest` and end-to-end suites
* package and distribute an operator
* upgrade both the operator and the operand
* recognize the patterns that `make` operators succeed in production

## Outline
<!-- chapter: what-an-operator-actually-is, duration: 1h -->
* What an operator actually is
    * controller plus `CRD` plus operational knowledge
    * the level-based reconciliation idea
    * the "operator pattern" paper
    * cross-reference to the `Kubernetes` course
    * `when` an operator is the right answer
<!-- chapter: the-controller-pattern, duration: 2h -->
* The controller pattern
    * the reconciliation loop as the core idea
    * desired state vs observed state
    * level-based vs edge-based
    * the "we wrote it edge-based and missed events" failure
    * the watch, the cache, the work queue
<!-- chapter: choosing-a-framework, duration: 2h -->
* Choosing a framework
    * `controller-runtime` (the underlying library)
    * `Kubebuilder` (scaffolding)
    * `Operator SDK` (`Red Hat` ecosystem)
    * `KUDO` (declarative)
    * `Metacontroller` (any-language)
    * picking for the team
<!-- chapter: crd-design, duration: 3h -->
* `CRD` design
    * the `Kubernetes API` conventions
    * the `spec`/`status` split
    * `OpenAPI` schema validation
    * defaulting and pruning
    * the version-and-conversion-webhook story
    * the "we shipped a `v1alpha1` and could not migrate" trap
<!-- chapter: writing-the-reconciler, duration: 3h -->
* Writing the reconciler
    * the `Reconcile` function contract
    * idempotent reconciliation
    * the `RequeueAfter` and the back-off
    * the `Status` update story
    * the "we updated `Status` from `Spec` and looped forever" failure
<!-- chapter: finalizers-and-deletion, duration: 2h -->
* Finalizers and deletion
    * the finalizer pattern
    * the cleanup contract
    * the "we left orphaned cloud resources" failure
    * deletion ordering
    * the worked example
<!-- chapter: leader-election-and-multi-replica, duration: 1h -->
* Leader election and multi-replica
    * why operators run with leader election
    * the `lease` lock mechanism
    * the multi-replica failover story
    * the "two leaders fought" failure
<!-- chapter: managing-the-operand, duration: 3h -->
* Managing the operand
    * the operand as the actual workload
    * generation of child resources (`Deployment`, `StatefulSet`, `Service`)
    * the `OwnerReference` and the garbage collection
    * the operand-version-vs-operator-version question
    * the worked example for a stateful database
<!-- chapter: operator-capability-levels, duration: 1h -->
* Operator capability levels
    * basic install
    * seamless upgrades
    * full lifecycle
    * deep insights (metrics, alerts)
    * autopilot (autoscaling, healing, tuning)
    * the `OperatorHub` framework
<!-- chapter: testing-operators, duration: 3h -->
* Testing operators
    * `envtest` for unit-level reconciler tests
    * `kuttl` for end-to-end tests
    * `chainsaw` as a modern alternative
    * the integration test against `kind` or `k3d`
    * the "we tested only the happy path" failure
<!-- chapter: observability-of-operators, duration: 2h -->
* Observability of operators
    * the controller-runtime metrics
    * the `Reconcile` time histogram
    * the work-queue depth alert
    * structured logging of the reconcile
    * the "the operator silently stopped reconciling" failure
<!-- chapter: packaging-and-distribution, duration: 2h -->
* Packaging and distribution
    * `Helm` chart packaging
    * `OLM` bundle packaging
    * the `ClusterServiceVersion`
    * the `kustomize` distribution
    * picking the distribution
<!-- chapter: upgrading-the-operator-and-the-operand, duration: 2h -->
* Upgrading the operator and the operand
    * the operator upgrade
    * the operand-version compatibility matrix
    * the `CRD` migration during upgrade
    * the rolling-upgrade strategy for the operand
    * the "we upgraded the operator and broke every operand" disaster
<!-- chapter: anti-patterns, duration: 2h -->
* Anti-patterns
    * the operator that is just a `kubectl` script
    * the operator that does not handle drift
    * the operator that requires manual intervention
    * the operator that ignores its own `CRD` validation
    * the "operator was unowned and rotted" failure
<!-- chapter: case-studies, duration: 3h -->
* Case studies
    * `Strimzi` (`Kafka`) walkthrough
    * `Cloudnative-PG` (`Postgres`) walkthrough
    * `Prometheus Operator` walkthrough
    * `Crossplane` model
    * recommended reading: `controller-runtime` docs, `Kubernetes` `API` conventions

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
