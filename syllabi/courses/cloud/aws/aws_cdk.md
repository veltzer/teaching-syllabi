---
tags:
  - infrastructure:aws
  - infrastructure:cloud
  - infrastructure:infrastructure-as-code
level: intermediate
category: cloud
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
  - audiences:architects
---
<!-- course: aws_cdk -->
# `AWS` CDK

## Description
This course provides an in-depth look at the `AWS` Cloud Development Kit (CDK), a modern infrastructure-as-code framework that allows you to define cloud infrastructure using familiar programming languages such as `TypeScript` and `Python`. Participants will learn how to model, provision, and manage `AWS` resources using CDK constructs, stacks, and pipelines, and will understand how CDK compares to other IaC tools like `CloudFormation` and `Terraform`.

## Duration
16 hours / 2 days

## Intended Audience
* Developers who want to define and manage `AWS` infrastructure using code.
* `DevOps` engineers looking to adopt a programmatic approach to infrastructure provisioning.
* Architects evaluating infrastructure-as-code solutions for their organizations.

## Prerequisites
* Familiarity with software development concepts and practices.
* Basic understanding of `cloud computing` principles.

## Required Knowledge
* Introduction to `AWS`
* `TypeScript` Programming or `Python` Programming

## Objectives
* Understand the `AWS` CDK architecture and how it synthesizes `CloudFormation` templates.
* Define cloud infrastructure using CDK constructs at various abstraction levels.
* Organize infrastructure into stacks and manage multiple environments.
* Build deployment pipelines using CDK Pipelines.
* Write tests for CDK applications.
* Apply best practices for maintainable and scalable CDK projects.

## Outline
<!-- chapter: introduction-to-aws-cdk, duration: 2h -->
* Introduction to `AWS` CDK
    * What is infrastructure as code?
    * CDK overview and architecture
    * CDK vs `CloudFormation` vs `Terraform`
    * Setting up a CDK project
    * The CDK `CLI`
<!-- chapter: cdk-constructs, duration: 2h -->
* CDK Constructs
    * L1 constructs (CFN resources)
    * L2 constructs (intent-based `API`)
    * L3 constructs (patterns)
    * Writing custom constructs
    * Construct composition and reuse
<!-- chapter: stacks-and-environments, duration: 2h -->
* Stacks and Environments
    * Defining stacks
    * Stack dependencies and cross-stack references
    * Environment-aware stacks
    * Managing multiple environments (dev, staging, production)
    * Stack synthesis and deployment
<!-- chapter: core-aws-services-with-cdk, duration: 2h -->
* Core `AWS` Services with CDK
    * `Lambda` functions
    * `API Gateway`
    * `DynamoDB` tables
    * `S3` buckets
    * `IAM` roles and policies
    * `VPC` and networking
<!-- chapter: aspects-and-escape-hatches, duration: 2h -->
* Aspects and Escape Hatches
    * Using aspects for cross-cutting concerns
    * Compliance and tagging with aspects
    * Escape hatches for unsupported features
    * Overriding synthesized `CloudFormation`
<!-- chapter: cdk-pipelines, duration: 2h -->
* CDK Pipelines
    * Continuous deployment with CDK Pipelines
    * Defining pipeline stages
    * Adding validation steps
    * Self-mutating pipelines
    * Multi-account deployments
<!-- chapter: testing-cdk-applications, duration: 2h -->
* Testing CDK Applications
    * Unit testing with assertions
    * Snapshot testing
    * Fine-grained assertion testing
    * Integration testing strategies
<!-- chapter: best-practices, duration: 2h -->
* Best Practices
    * Project structure and organization
    * Construct library development
    * Managing configuration and secrets
    * Versioning and dependency management
    * Security best practices
    * Performance considerations

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
