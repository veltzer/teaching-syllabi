---
tags:
  - tools:pulumi
  - practices:devops
  - practices:automation
level: intermediate
category: devops
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
---
<!-- course: pulumi -->
# `Pulumi`

## Description
This course covers `Pulumi`, a modern infrastructure as code platform that allows
engineers to define and manage cloud infrastructure using general-purpose programming
languages such as `TypeScript`, `Python`, and Go. The course begins with foundational
IaC concepts and a comparison with `Terraform`, then progresses through `Pulumi`
architecture, writing infrastructure code, managing state and secrets, testing, and
policy enforcement with CrossGuard. Students will gain hands-on experience provisioning
resources across major cloud providers and `Kubernetes`, and learn how to integrate
`Pulumi` into `CI/CD` workflows.

## Duration
16 hours / 2 days

## Intended Audience
* Software developers and `DevOps` engineers looking to manage infrastructure using familiar programming languages.
* Teams evaluating or migrating to `Pulumi` from `Terraform` or other IaC tools.

## Prerequisites
* Experience with at least one programming language (`TypeScript`, `Python`, or Go).
* Basic understanding of `cloud computing` concepts (`AWS`, `Azure`, or `GCP`).
* Familiarity with command-line tools.

## Required Knowledge
* `Python` Programming (or equivalent experience)
* Introduction to `Azure` (or equivalent experience)
* `GCP` Fundamentals (or equivalent experience)
* `TypeScript` Programming (or equivalent experience)

## Objectives
* Understand infrastructure as code principles and how `Pulumi` implements them.
* Write infrastructure definitions using `TypeScript`, `Python`, or Go.
* Manage `Pulumi` stacks, state, and secrets effectively.
* Create reusable component resources and share them across stacks.
* Test infrastructure code using unit and integration testing frameworks.
* Enforce policies with CrossGuard and integrate `Pulumi` into `CI/CD` pipelines.

## Outline
<!-- chapter: infrastructure-as-code-concepts, duration: 1h -->
* Infrastructure as Code Concepts
    * What is infrastructure as code?
    * Benefits of IaC over manual provisioning
    * Declarative vs imperative approaches
    * State management fundamentals
<!-- chapter: pulumi-vs-terraform-comparison, duration: 1h -->
* `Pulumi` vs `Terraform` Comparison
    * Architecture differences
    * Language support and flexibility
    * State management approaches
    * Ecosystem and community
    * `When` to choose `Pulumi` over `Terraform`
<!-- chapter: pulumi-architecture, duration: 1h -->
* `Pulumi` Architecture
    * Projects and project structure
    * Stacks and stack configuration
    * The `Pulumi` engine and resource providers
    * State backends (local, `Pulumi` Cloud, `S3`, `Azure Blob`, `GCS`)
    * The `Pulumi` `CLI`
<!-- chapter: writing-infrastructure-in-typescript, duration: 1h -->
* Writing Infrastructure in `TypeScript`
    * Setting up a `TypeScript` project
    * Defining resources
    * Inputs, outputs, and interpolation
    * `Async` operations and promises
    * Stack outputs and exports
<!-- chapter: writing-infrastructure-in-python, duration: 1h -->
* Writing Infrastructure in `Python`
    * Setting up a `Python` project
    * Resource definitions and configuration
    * Working with outputs and apply
    * Virtual environments and dependency management
<!-- chapter: writing-infrastructure-in-go, duration: 1h -->
* Writing Infrastructure in Go
    * Setting up a Go project
    * Resource definitions in Go
    * Error handling patterns
    * Module organization
<!-- chapter: resource-providers, duration: 2h -->
* Resource Providers
    * `AWS` provider and common resources
    * `Azure` provider and common resources
    * `GCP` provider and common resources
    * `Kubernetes` provider
    * Community and third-party providers
    * Provider configuration and versioning
<!-- chapter: component-resources, duration: 1h -->
* Component Resources
    * What are component resources?
    * Creating custom components
    * Encapsulating infrastructure patterns
    * Sharing components across projects
    * Publishing component packages
<!-- chapter: stack-references, duration: 1h -->
* Stack References
    * Cross-stack dependencies
    * Reading outputs from other stacks
    * Organizing multi-stack architectures
    * Stack reference patterns and best practices
<!-- chapter: secrets-management, duration: 1h -->
* Secrets Management
    * Built-in secrets encryption
    * Secrets providers (`Pulumi` Cloud, `AWS KMS`, `Azure Key Vault`, `GCP KMS`)
    * Handling sensitive configuration values
    * Secret outputs and their propagation
<!-- chapter: testing-infrastructure-code, duration: 1h -->
* Testing Infrastructure Code
    * Unit testing with mocks
    * Property testing
    * Integration testing
    * Testing patterns and strategies
    * Testing frameworks for each language
<!-- chapter: policy-as-code-with-crossguard, duration: 1h -->
* Policy as Code with CrossGuard
    * What is CrossGuard?
    * Writing policy packs
    * Advisory vs mandatory policies
    * Validating resource properties
    * Deploying and enforcing policies
<!-- chapter: ci-cd-integration, duration: 1h -->
* `CI/CD` Integration
    * `Pulumi` in `GitHub Actions`
    * `Pulumi` in `GitLab` CI
    * `Pulumi` in `Jenkins`
    * Automating previews on pull requests
    * Automated deployments and stack updates
<!-- chapter: migration-from-terraform, duration: 2h -->
* Migration from `Terraform`
    * Importing existing resources
    * Converting `Terraform` HCL to `Pulumi`
    * Using tf2pulumi
    * Coexistence strategies
    * Migration planning and execution

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
