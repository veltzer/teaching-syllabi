---
tags:
  - tools:terraform
  - infrastructure:infrastructure-as-code
  - infrastructure:cloud
  - practices:devops
level: beginner
category: devops
duration_hours_short: 8
duration_hours_long: 24
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
  - audiences:managers
duration_hours: 24
---
<!-- course: terraform_introduction -->
# `Terraform` Introduction

## Description
`Terraform` is one of the leading tools in `DevOps` automation and infrastructure
as code approaches with an advantage of being able to work with multiple cloud
providers. This course teaches all the relevant information that one needs to
get started using `Terraform` and compares `Terraform` to other solution tackling the
same problems.

## Duration
* Short: 8 hours / 1 day
* Long: 24 hours / 3 days

## Intended Audience
* Aspiring `DevOps` who would like to study `Terraform` as their first `DevOps` tool.
* `Devops` who want to start using `Terraform`
* `Devops` who have been using `Terraform` but have not had any formal education on
how to use it correctly.
* Developers who wish to do their own `DevOps` work using `Terraform`.
* Any other interested party such as team leaders, managers etc.

## Prerequisites
* No special experience is required.
* Experience with any type of cloud is beneficial but not required.
* Tech affinity is required.

## Objectives
* Participants will be able to understand what the main problem that `Terraform` solves is,
and how it compares with competing or other tools in the `DevOps` space.
* Participants will be able to use `Terraform` to build simple architectures.
* Participants will learn how to use `Terraform` correctly and avoid it's pitfalls.

## Exercises
The course includes exercises on `AWS` for every chapter. [long]
The exercises could be modified to work on other cloud providers (`GCP`, `Azure`)
but this will `require` some work.

## Outline
<!-- chapter: introduction-to-terraform, duration: 3h -->
* Introduction to `Terraform`
    * Overview of `Terraform` architecture
    * Obtaining and installing `Terraform`
    * `Terraform` `CLI`
    * Infrastructure life cycle
<!-- chapter: language-components, duration: 3h -->
* Language Components
    * Resources
    * `Terraform` Providers: `AWS`, Microsoft `Azure`, `Google Cloud`, On-premise
    * Modules
    * Data providers
    * Patterns for structuring projects
<!-- chapter: infrastructure-as-code, duration: 4h -->
* Infrastructure as Code
    * Abstracting services and resources
    * Planning your architecture
    * Creating Configuration Files
    * Setting up a simple two-tier `AWS` architecture
    * Using `Packer` to pre-configure `Amazon Machine Images` (`AMIs`)
    * Using `Consul` for Service Discovery
    * Terminating infrastructure with Destroy
<!-- chapter: state-management, duration: 3h -->
* State Management
    * Mapping real world resources to configurations
    * Recording metadata
    * Creating infrastructure plans
    * Inspecting and modifying state
<!-- chapter: environment-variables, duration: 1h -->
* Environment Variables
    * Dealing with Parameters
    * Key variables (TF_LOG, TF_VAR_name, ...)
<!-- chapter: managing-resources, duration: 2h -->
* Managing Resources
    * Implicit and Explicit Dependencies
    * Non-dependent Resources
    * Iterating on Resources
<!-- chapter: terraform-git-ops, duration: 2h -->
* `Terraform` & `Git` Ops
    * `Git` as the source of truth
    * Using `Terraform` to describe deployment
    * Deploying environments with CI pipelines
<!-- chapter: terraform-test-automation, duration: 1h -->
* `Terraform` Test Automation
    * Terratest
    * Unit Testing `Terraform` Modules
<!-- chapter: terraform-security, duration: 3h -->
* `Terraform` Security
    * Securing your `Terraform` Pipeline
    * System Accounts & Permissions
    * `Terraform` back end configuration
    * Handling Environments separately
<!-- chapter: maintenance-and-troubleshooting, duration: 2h -->
* Maintenance and Troubleshooting
    * Checking `OCI` service status
    * Verbose Logging
    * Error messages

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
