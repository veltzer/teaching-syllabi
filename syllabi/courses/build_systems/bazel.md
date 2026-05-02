---
tags:
  - tools:bazel
  - practices:build-systems
  - practices:monorepo
level: intermediate
category: build-system
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
---
<!-- course: bazel -->
# `Bazel`

## Description
`Bazel` is a fast, scalable, multi-language build system originally developed by Google. It is designed for large codebases and monorepos, providing hermetic builds, remote caching, and remote execution. This course covers `Bazel` from the ground up, including its build model, rule system, and integration into real-world development workflows.

## Duration
16 hours / 2 days

## Intended Audience
* Software developers working with large or multi-language codebases
* `DevOps` engineers managing build infrastructure
* Teams considering a migration to `Bazel` or monorepo workflows

## Prerequisites
* Software development experience in at least one compiled language
* Basic familiarity with build systems concepts

## Objectives
* Understand `Bazel`'s build model and how it differs from traditional build systems
* Write BUILD files and configure `Bazel` workspaces
* Create and use custom rules with Starlark
* Configure remote caching and remote execution
* Integrate `Bazel` into `CI/CD` pipelines

## Outline
<!-- chapter: introduction-to-bazel, duration: 2h -->
* Introduction to `Bazel`
    * History and motivation (from Google's Blaze to open-source `Bazel`)
    * Comparison with other build systems (Make, `CMake`, `Gradle`, Buck2)
    * Core concepts: targets, labels, packages, workspaces
    * The hermetic build model
    * Installing and configuring `Bazel`
<!-- chapter: build-files-and-workspaces, duration: 3h -->
* BUILD Files and Workspaces
    * WORKSPACE and MODULE.`bazel` files
    * Writing BUILD files
    * Built-in rules for C/`C++`, `Java`, `Python`, Go
    * Filegroups and genrules
    * Visibility and access control
    * Managing third-party dependencies with Bzlmod
<!-- chapter: the-starlark-language, duration: 2h -->
* The Starlark Language
    * Starlark syntax and semantics
    * Writing custom rules
    * Providers and aspects
    * Macros vs rules
    * Testing custom rules
<!-- chapter: building-multi-language-projects, duration: 2h -->
* Building Multi-Language Projects
    * Cross-language dependencies
    * `Protocol Buffers` and `gRPC` with `Bazel`
    * Building containers with rules_oci
    * `Java`, `C++`, `Python`, and Go interoperability
<!-- chapter: testing-with-bazel, duration: 2h -->
* Testing with `Bazel`
    * Test rules and test suites
    * Test sharding and parallelism
    * Flaky test handling
    * Code coverage
<!-- chapter: performance-and-scalability, duration: 3h -->
* Performance and Scalability
    * Incremental and cached builds
    * Remote caching (`HTTP`, `gRPC`)
    * Remote execution with `Bazel` Remote Execution `API`
    * Build profiling and optimization
    * Dealing with large monorepos
<!-- chapter: integration-and-migration, duration: 2h -->
* Integration and Migration
    * Integrating `Bazel` into `CI/CD` pipelines
    * Migrating from Make, `CMake`, or `Gradle`
    * IDE integration (IntelliJ, `VS Code`)
    * Build event protocol and build observability

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
