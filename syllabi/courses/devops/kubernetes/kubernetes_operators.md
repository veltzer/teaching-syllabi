---
tags:
  - tools:kubernetes
  - concepts:architecture
  - practices:devops
level: advanced
category: devops
duration_hours: 24
audience:
  - audiences:developers
  - audiences:devops
---
<!-- course: kubernetes_operators -->
# `Kubernetes` Operators

## Description
This course provides an in-depth exploration of the `Kubernetes` Operator pattern, teaching
participants how to extend `Kubernetes` by building custom controllers and operators. The course
covers the full lifecycle of operator development, from understanding the `Kubernetes` `API` and
custom resources to building, testing, and deploying production-grade operators using tools
such as `Operator SDK` and kubebuilder. Participants will learn how to implement reconciliation
loops, handle finalizers, set up webhooks, and manage operator deployment using the
`Operator Lifecycle Manager`.

## Duration
24 hours / 3 days

## Intended Audience
* developers who want to extend `Kubernetes` with custom controllers and operators.
* `devops` engineers responsible for managing complex applications on `Kubernetes`.
* platform engineers building internal developer platforms on `Kubernetes`.

## Prerequisites
* `solid` understanding of `Kubernetes` concepts (pods, deployments, services, namespaces).
* experience with Go programming language is recommended.
* familiarity with `kubectl` and `Kubernetes` manifests.

## Objectives
* understand the Operator pattern and when to apply it.
* gain practical knowledge of extending the `Kubernetes` `API` with custom resources.
* build operators using `Operator SDK` and kubebuilder.
* implement robust reconciliation loops, finalizers, and webhooks.
* test and deploy operators in production environments.

## Outline
<!-- chapter: operator-pattern-concepts, duration: 2h -->
* Operator pattern concepts
    * what is an operator
    * why extend `Kubernetes`
    * operator maturity model
    * real-world operator examples
<!-- chapter: kubernetes-api-and-custom-resources, duration: 2h -->
* `Kubernetes` `API` and custom resources
    * `API` server internals
    * `API` groups, versions, and resources
    * custom resource definitions (`CRDs`)
    * structural schemas and validation
    * status subresource
<!-- chapter: controller-pattern, duration: 2h -->
* Controller pattern
    * controller architecture
    * reconciliation loop
    * level-triggered vs edge-triggered
    * idempotency and convergence
    * error handling and requeueing
<!-- chapter: operator-sdk-and-kubebuilder, duration: 2h -->
* `Operator SDK` and kubebuilder
    * scaffolding a new operator project
    * building operators with Go
    * building operators with `Ansible`
    * building operators with Helm
    * project layout and code generation
<!-- chapter: client-go-internals, duration: 2h -->
* client-`go` internals
    * informers and shared informer factory
    * work queues and rate limiting
    * listers and indexers
    * dynamic client
<!-- chapter: owner-references-and-finalizers, duration: 2h -->
* Owner references and finalizers
    * garbage collection in `Kubernetes`
    * owner references and cascading deletes
    * implementing finalizers
    * cleanup logic and external resources
<!-- chapter: webhooks, duration: 2h -->
* Webhooks
    * validating admission webhooks
    * mutating admission webhooks
    * conversion webhooks
    * webhook certificate management
<!-- chapter: rbac-for-operators, duration: 2h -->
* `RBAC` for operators
    * service accounts and roles
    * cluster roles vs namespace-scoped roles
    * least privilege principle
    * `RBAC` markers in kubebuilder
<!-- chapter: testing-operators, duration: 2h -->
* Testing operators
    * unit testing controller logic
    * integration testing with envtest
    * end-to-end testing strategies
    * mocking external dependencies
<!-- chapter: operator-lifecycle-manager-olm, duration: 3h -->
* `Operator Lifecycle Manager` (OLM)
    * OLM architecture
    * creating operator bundles
    * catalog sources and subscriptions
    * upgrade strategies and channels
    * operator dependency management
<!-- chapter: operator-best-practices-and-production-deployment, duration: 3h -->
* Operator best practices and production deployment
    * high availability and leader election
    * metrics and monitoring
    * logging best practices
    * resource limits and requests
    * versioning and upgrade strategies
    * multi-tenant considerations

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
