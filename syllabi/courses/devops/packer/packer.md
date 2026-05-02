---
tags:
  - tools:packer
  - practices:devops
  - practices:automation
level: intermediate
category: devops
duration_hours: 16
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: packer -->
# `Packer`

## Description
This course covers HashiCorp `Packer`, a tool for building automated machine images across
multiple platforms from a single source configuration. Students will learn how to create
reproducible, version-controlled images for cloud and on-premises environments.

The course progresses from image building fundamentals through `Packer` architecture,
HCL2 template syntax, builders, provisioners, and post-processors. Students will gain
practical experience building images for multiple platforms, integrating `Packer` into
`CI/CD` pipelines, and establishing golden image pipelines.

## Duration
16 hours / 1 day

## Intended Audience
* `DevOps` engineers responsible for building and maintaining machine images for cloud and on-premises infrastructure.

## Prerequisites
* Familiarity with command-line tools and scripting.
* Basic understanding of virtualization and `cloud computing` concepts.
* Experience with at least one cloud provider (`AWS`, `Azure`, or `GCP`) is helpful.

## Required Knowledge
* Introduction to `Azure` (or equivalent experience)
* `GCP` Fundamentals (or equivalent experience)

## Objectives
* Understand the benefits of automated image building.
* Write `Packer` templates using HCL2 syntax.
* Build images for multiple platforms using different builders.
* Configure provisioners to install software and harden images.
* Integrate `Packer` into `CI/CD` pipelines.
* Establish golden image pipelines for production environments.

## Outline
<!-- chapter: image-building-concepts, duration: 1h -->
* Image Building Concepts
    * Why automate image building?
    * Immutable infrastructure principles
    * Golden images and base image strategy
    * Comparison with `Dockerfile` approach
<!-- chapter: packer-architecture, duration: 1h -->
* `Packer` Architecture
    * Templates and their structure
    * Builders, provisioners, and post-processors
    * Build lifecycle and execution order
    * `Packer` plugins ecosystem
<!-- chapter: hcl2-template-syntax, duration: 2h -->
* HCL2 Template Syntax
    * source blocks
    * build blocks
    * Variables and locals
    * Variable files and environment variables
    * Functions and expressions
    * Data sources
    * Dynamic blocks
<!-- chapter: builders, duration: 2h -->
* Builders
    * Amazon AMI builder (amazon-`ebs`, amazon-instance)
    * `Docker` builder
    * `VMware` builder
    * `VirtualBox` builder
    * `Azure` builder
    * `GCP` builder
    * Builder configuration and communicators
<!-- chapter: provisioners, duration: 2h -->
* Provisioners
    * Shell provisioner
    * `File` provisioner
    * `Ansible` provisioner
    * Chef provisioner
    * Puppet provisioner
    * Provisioner ordering and error handling
    * Inline vs script-based provisioning
<!-- chapter: post-processors, duration: 2h -->
* Post-Processors
    * `Docker` push post-processor
    * Vagrant post-processor
    * Manifest post-processor
    * Checksum post-processor
    * Chaining post-processors
<!-- chapter: packer-build-workflow, duration: 2h -->
* `Packer` Build Workflow
    * Validating templates
    * Running builds
    * Debugging builds
    * Parallel builds across platforms
    * Build-time variables and overrides
<!-- chapter: testing-images, duration: 1h -->
* Testing Images
    * Image validation strategies
    * Using InSpec and Serverspec
    * Automated compliance checking
    * Smoke testing built images
<!-- chapter: ci-cd-integration, duration: 1h -->
* `CI/CD` Integration
    * `Packer` in `Jenkins` pipelines
    * `Packer` in `GitHub Actions`
    * Triggering builds on source changes
    * Artifact management and versioning
<!-- chapter: golden-image-pipelines, duration: 2h -->
* Golden Image Pipelines
    * Base image layering strategy
    * Security patching workflows
    * Image promotion across environments
    * Image lifecycle and deprecation

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
