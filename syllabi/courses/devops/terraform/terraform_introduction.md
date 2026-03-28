---
tags:
  - tools:terraform
  - infrastructure:infrastructure-as-code
  - infrastructure:cloud
  - practices:devops
level: beginner
category: devops
duration_hours: 24
audience:
  - practices:devops
---
# `Terraform` Introduction

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
`Terraform` is one of the leading tools in `DevOps` automation and infrastructure
as code approaches with an advantage of being able to work with multiple cloud
providers. This course teaches all the relevant information that one needs to
get started using `Terraform` and compares `Terraform` to other solution tackling the
same problems.

## Duration
24 hours / 3 days

## Intended Audience
* Aspiring `DevOps` who would like to study `Terraform` as their first `DevOps` tool.
* Devops who want to start using `Terraform`
* Devops who have been using `Terraform` but have not had any formal education on
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
The course includes exercises on `AWS` for every chapter.
The exercises could be modified to work on other cloud providers (`GCP`, `Azure`)
but this will require some work.

## Outline
* Introduction to `Terraform`
    * Overview of `Terraform` architecture
    * Obtaining and installing `Terraform`
    * `Terraform` CLI
    * Infrastructure life cycle
* Language Components
    * Resources
    * `Terraform` Providers: `AWS`, Microsoft `Azure`, `Google Cloud`, On-premise
    * Modules
    * Data providers
    * Patterns for structuring projects
* Infrastructure as Code
    * Abstracting services and resources
    * Planning your architecture
    * Creating Configuration Files
    * Setting up a simple two-tier `AWS` architecture
    * Using Packer to pre-configure Amazon Machine Images (AMIs)
    * Using Consul for Service Discovery
    * Terminating infrastructure with Destroy
* State Management
    * Mapping real world resources to configurations
    * Recording metadata
    * Creating infrastructure plans
    * Inspecting and modifying state
* Environment Variables
    * Dealing with Parameters
    * Key variables (`TF_LOG`, `TF_VAR_name`, ...)
* Managing Resources
    * Implicit and Explicit Dependencies
    * Non-dependent Resources
    * Iterating on Resources
* `Terraform` & `Git` Ops
    * `Git` as the source of truth
    * Using `Terraform` to describe deployment
    * Deploying environments with CI pipelines
* `Terraform` Test Automation
    * Terratest
    * Unit Testing `Terraform` Modules
* `Terraform` Security
    * Securing your `Terraform` Pipeline
    * System Accounts & Permissions
    * `Terraform` back end configuration
    * Handling Environments separately
* Maintenance and Troubleshooting
    * Checking OCI service status
    * Verbose Logging
    * Error messages

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
