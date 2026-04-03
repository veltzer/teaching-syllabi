---
tags:
  - infrastructure:kubernetes
  - infrastructure:containers
  - practices:devops
  - languages:go
  - concepts:programming
level: advanced
category: containers
duration_hours: 16
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: kubernetes_for_developers -->
# `Kubernetes` for Developers

## Description
This advanced course is designed for developers who want to build `Kubernetes`-native
applications. Students will learn how to extend `Kubernetes` by writing custom operators,
Custom Resource Definitions (CRDs), and admission webhooks. The course covers the
client-`go` library, the controller-runtime framework, and the patterns and best
practices for building production-grade `Kubernetes` extensions. By the end of the course,
students will be able to design, implement, and deploy their own `Kubernetes` operators
and controllers.

## Duration
16 hours / 2 days

## Intended Audience
* Developers who want to build applications that integrate deeply with `Kubernetes`.
* Platform engineers building internal developer platforms on `Kubernetes`.
* Backend developers who need to write `Kubernetes` operators and controllers.
* Software architects designing `Kubernetes`-native systems.

## Prerequisites
* `Solid` understanding of `Kubernetes` concepts (pods, services, deployments, namespaces).
* Experience with the `Go` programming language.
* Familiarity with the `Kubernetes` `API` and `kubectl`.
* Understanding of `REST` APIs and `YAML`/`JSON` formats.

## Objectives
* Understand the `Kubernetes` `API` machinery and extension points
* Design and implement Custom Resource Definitions (CRDs)
* Build `Kubernetes` operators using client-`go` and controller-runtime
* Implement admission webhooks for validation and mutation
* Apply best practices for testing and deploying `Kubernetes`-native applications

## Outline
<!-- chapter: the-kubernetes-api-and-extension-model, duration: 2h -->
* The `Kubernetes` `API` and Extension Model
    * Review of `Kubernetes` architecture from a developer perspective
    * The `Kubernetes` `API` server and `API` groups
    * Resources, sub-resources, and `API` versioning
    * Understanding the `Kubernetes` object model
    * `API` discovery and `OpenAPI` schemas
    * Extension points in `Kubernetes`
<!-- chapter: custom-resource-definitions-crds, duration: 2h -->
* Custom Resource Definitions (CRDs)
    * What are CRDs and why do we need them?
    * Defining a CRD with `YAML`
    * Schema validation with `OpenAPI` v3
    * Versioning CRDs and conversion webhooks
    * Status subresource and printer columns
    * CRD categories and short names
    * Working with custom resources using `kubectl`
<!-- chapter: the-client-go-library, duration: 3h -->
* The client-`go` Library
    * Overview of client-`go` and its components
    * Connecting to the `Kubernetes` `API` server
    * Typed clients vs dynamic clients
    * Informers and the shared informer factory
    * Work queues and rate limiting
    * Listers and caching
    * Error handling and retry patterns
<!-- chapter: building-operators-with-controller-runtime, duration: 3h -->
* Building Operators with controller-runtime
    * What is an operator and the operator pattern?
    * Introduction to controller-runtime and Kubebuilder
    * Scaffolding a new operator project
    * The reconciliation loop
    * Watching resources and setting up event handlers
    * Owner references and garbage collection
    * Finalizers for cleanup logic
    * Status management and condition reporting
    * Leader election for high availability
<!-- chapter: admission-webhooks, duration: 3h -->
* Admission Webhooks
    * What are admission webhooks?
    * Validating admission webhooks
    * Mutating admission webhooks
    * Webhook configuration and certificate management
    * Implementing webhooks with controller-runtime
    * Testing webhooks locally
    * Failure policies and performance considerations
<!-- chapter: testing-and-deployment-best-practices, duration: 3h -->
* Testing and Deployment Best Practices
    * Unit testing controllers and reconcilers
    * Integration testing with envtest
    * End-to-end testing strategies
    * Building and packaging operator images
    * Deploying operators with `Helm` or OLM
    * Operator lifecycle management
    * Logging, metrics, and observability for operators
    * Versioning and upgrade strategies

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
