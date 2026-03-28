---
tags:
  - tools:buck2
  - practices:build-systems
  - practices:monorepo
level: intermediate
category: build-system
duration_hours: 16
audience:
  - audiences:developers
---
# `Buck2`

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
`Buck2` is a high-performance, large-scale build system developed by Meta. It is a ground-up rewrite of the original Buck, written in `Rust`, and designed for speed, correctness, and scalability. This course covers `Buck2`'s architecture, its `Starlark`-based rule system, and how to use it effectively for multi-language monorepo development.

## Duration
16 hours / 2 days

## Intended Audience
* Software developers working with large or multi-language codebases
* `DevOps` engineers managing build infrastructure
* Teams considering a migration to `Buck2` or monorepo workflows

## Prerequisites
* Software development experience in at least one compiled language
* Basic familiarity with build systems concepts

## Objectives
* Understand `Buck2`'s architecture and how it differs from other build systems
* Write BUCK files and configure `Buck2` projects
* Create and use custom rules with `Starlark`
* Configure remote execution
* Integrate `Buck2` into CI/CD pipelines

## Outline
* Introduction to `Buck2`
    * History and motivation (from Buck to `Buck2`)
    * Comparison with other build systems (`Make`, `CMake`, `Bazel`, `Gradle`)
    * Core concepts: targets, cells, packages, configurations
    * The `Buck2` daemon and incremental computation engine
    * Installing and configuring `Buck2`
* BUCK Files and Project Structure
    * Project layout and cell configuration
    * Writing BUCK files
    * Built-in rules for `C`/`C++`, `Java`, `Python`, `Rust`, `Go`
    * Target visibility and access control
    * Managing third-party dependencies
* The `Starlark` Rule System
    * `Starlark` syntax and semantics
    * Writing custom rules
    * Providers and artifacts
    * Actions and command execution
    * Transitions and platform configuration
    * Testing custom rules
* Building Multi-Language Projects
    * Cross-language dependencies
    * Protocol Buffers and gRPC with `Buck2`
    * Building containers
    * Platform-specific builds and select()
* Testing with `Buck2`
    * Test rules and test runners
    * Test parallelism
    * Local and remote test execution
    * Code coverage
* Performance and Scalability
    * Incremental builds and the DICE computation framework
    * Remote execution
    * Build profiling and critical path analysis
    * Virtual filesystems and lazy materialization
    * Dealing with large monorepos
* Integration and Migration
    * Integrating `Buck2` into CI/CD pipelines
    * Migrating from Buck v1, `Bazel`, or other build systems
    * IDE integration
    * Build observability and logging

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
