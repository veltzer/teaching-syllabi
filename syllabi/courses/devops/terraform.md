---
tags:
  - practices:devops
  - tools:terraform
  - infrastructure:infrastructure-as-code
  - infrastructure:cloud
  - tools:terragrunt
level: intermediate
category: devops
duration_hours: 24
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: terraform -->
<!-- Track gap: `Packer` integration for machine image building -->
# `Terraform` / Infrastructure as Code

## Description
This course provides a comprehensive introduction to `Terraform` and the Infrastructure as Code
(IaC) paradigm. Participants will learn how to define, provision, and manage cloud infrastructure
using `Terraform`'s declarative configuration language (HCL). The course covers providers,
resources, state management, modules, workspaces, and backends, as well as advanced tooling
such as Terragrunt for managing complex multi-environment deployments.

This course is practical and cloud-agnostic in its approach, though examples will primarily use
`AWS` and `Azure` providers. Participants should have basic familiarity with cloud services before
attending.

## Duration
24 hours / 3 days

## Intended Audience
* `DevOps` engineers looking to adopt or deepen their knowledge of Infrastructure as Code.
* cloud engineers responsible for provisioning and managing infrastructure.
* developers who want to understand and contribute to infrastructure definitions.
* platform engineers building reusable infrastructure modules for their organizations.

## Prerequisites
* Basic understanding of `cloud computing` concepts (`AWS`, `Azure`, or `GCP`).
* Familiarity with the command line and terminal usage.
* Basic understanding of networking concepts (VPCs, subnets, `DNS`).
* Experience with version control (`Git`).

## Required Knowledge
* Introduction to `Azure` (or equivalent experience)
* `GCP` Fundamentals (or equivalent experience)

## Objectives
* understand the core concepts and principles of Infrastructure as Code with `Terraform`
* gain practical knowledge of providers, resources, and HCL syntax
* gain practical knowledge of state management, modules, and workspaces
* gain practical knowledge of Terragrunt and advanced deployment patterns

## Outline
<!-- chapter: introduction-to-infrastructure-as-code, duration: 1h -->
* Introduction to Infrastructure as Code
    * What is Infrastructure as Code and why it matters
    * Declarative vs imperative approaches
    * Comparing IaC tools (`Terraform`, `Pulumi`, `CloudFormation`, Bicep)
    * Immutable vs mutable infrastructure
    * `Terraform` architecture and how it works
<!-- chapter: getting-started-with-terraform, duration: 1h -->
* Getting Started with `Terraform`
    * Installing and configuring `Terraform`
    * HCL syntax fundamentals
    * The `Terraform` workflow (init, plan, apply, destroy)
    * `Terraform` `CLI` commands and options
    * Configuration `file` structure and organization
<!-- chapter: providers, duration: 2h -->
* Providers
    * What are providers and how they work
    * Provider configuration and authentication
    * Provider versioning and constraints
    * Multi-provider configurations
    * Community and third-party providers
    * Provider aliases for multi-region deployments
<!-- chapter: resources-and-data-sources, duration: 2h -->
* Resources and Data Sources
    * Resource blocks and lifecycle
    * Resource dependencies (implicit and explicit)
    * Data sources for reading existing infrastructure
    * Resource meta-arguments (count, for_each, depends_on, lifecycle)
    * Provisioners and `when` to use them
    * Import of existing resources
<!-- chapter: variables-and-outputs, duration: 2h -->
* Variables and Outputs
    * Input variables and type constraints
    * Variable definitions and precedence
    * Local values and expressions
    * Output values and cross-module references
    * Sensitive values handling
    * Variable validation rules
<!-- chapter: expressions-and-functions, duration: 2h -->
* Expressions and Functions
    * `Terraform` expression syntax
    * String interpolation and templates
    * Conditional expressions
    * for expressions and collection transformations
    * Built-in functions (string, numeric, collection, filesystem)
    * Dynamic blocks
<!-- chapter: state-management, duration: 2h -->
* State Management
    * Understanding `Terraform` state
    * Local vs remote state
    * State `file` structure and contents
    * State locking and concurrency
    * State manipulation commands (`state mv`, `state rm`, taint, untaint)
    * Handling state drift
    * Sensitive data in state files
<!-- chapter: backends, duration: 2h -->
* Backends
    * Backend types and configuration
    * `S3` backend with `DynamoDB` locking
    * `Azure` Storage backend
    * `GCS` backend
    * `Terraform` Cloud as a backend
    * Backend migration
<!-- chapter: modules, duration: 2h -->
* Modules
    * Module concepts and benefits
    * Writing reusable modules
    * Module inputs, outputs, and composition
    * Module sources (local, registry, `Git`, `S3`)
    * `Terraform` Registry and public modules
    * Module versioning and best practices
    * Nested modules and module `design patterns`
<!-- chapter: workspaces, duration: 1h -->
* Workspaces
    * Workspace concepts and use cases
    * Creating and switching workspaces
    * Workspace-based environment separation
    * Limitations and alternatives to workspaces
<!-- chapter: terragrunt, duration: 2h -->
* Terragrunt
    * What is Terragrunt and `when` to use it
    * DRY configuration with Terragrunt
    * Managing multiple environments
    * Dependency management between modules
    * Before and after hooks
    * Remote state configuration with Terragrunt
<!-- chapter: testing-and-validation, duration: 1h -->
* Testing and Validation
    * `terraform validate` and `terraform fmt`
    * tflint and static analysis
    * `terraform plan` as a testing mechanism
    * Policy as code with Sentinel and `OPA`
    * Integration testing strategies
<!-- chapter: ci-cd-for-terraform, duration: 2h -->
* `CI/CD` for `Terraform`
    * Automating `Terraform` in pipelines
    * Plan and apply workflows
    * Pull request automation and plan previews
    * Managing secrets in `CI/CD` for `Terraform`
    * Drift detection in automated workflows
<!-- chapter: best-practices-and-patterns, duration: 2h -->
* Best Practices and Patterns
    * Repository and directory structure
    * Naming conventions
    * Tagging strategies
    * Handling breaking changes
    * Security considerations and least privilege
    * Cost management and resource lifecycle

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
