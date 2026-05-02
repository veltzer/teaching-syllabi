---
tags:
  - tools:gradle
  - practices:build-systems
  - languages:java
level: advanced
category: build-system
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
---
<!-- course: advanced_gradle -->
# Advanced `Gradle`

## Description
This advanced course dives deep into `Gradle`'s most powerful features for building, managing, and optimizing large-scale `Java` and `Kotlin` projects. Participants will learn to write custom plugins, leverage local and remote build caches, master variant-aware dependency management, and apply performance optimization techniques to significantly reduce build times. The course also covers the `Gradle` `Kotlin` DSL, composite builds, and artifact publishing.

## Duration
16 hours / 2 days

## Intended Audience
* Developers working on large `Java` or `Kotlin` projects who need to optimize their build processes.
* `DevOps` engineers responsible for maintaining and improving `CI/CD` build infrastructure.

## Prerequisites
* `Solid` understanding of software build concepts.
* Experience with `Java` or `Kotlin` development.

## Required Knowledge
* `Gradle`

## Objectives
* Develop custom `Gradle` plugins to encapsulate build logic.
* Configure and optimize local and remote build caches for faster builds.
* Master advanced dependency management including variant-aware resolution.
* Structure multi-project builds using convention plugins and composite builds.
* Analyze and improve build performance using build scans.
* Publish artifacts to local and remote repositories.

## Outline
<!-- chapter: custom-plugins, duration: 2h -->
* Custom Plugins
    * Plugin development fundamentals
    * Script plugins vs binary plugins
    * Plugin extension objects
    * Testing `Gradle` plugins
    * Publishing plugins to the `Gradle` Plugin Portal
    * Plugin best practices
<!-- chapter: build-cache, duration: 2h -->
* Build Cache
    * How the build cache works
    * Local build cache configuration
    * Remote build cache setup
    * Cache key computation and task output caching
    * Cacheable tasks and custom task types
    * Cache debugging and troubleshooting
<!-- chapter: dependency-management-deep-dive, duration: 2h -->
* Dependency Management Deep Dive
    * Dependency configurations and scopes
    * Dependency constraints and platforms (BOM)
    * Rich version declarations
    * Dependency locking
    * Handling dependency conflicts and resolution strategies
    * Component metadata rules
<!-- chapter: variant-aware-dependency-management, duration: 1h -->
* Variant-Aware Dependency Management
    * Understanding variants and attributes
    * Custom attributes and variants
    * Feature variants
    * Targeting specific platforms and configurations
<!-- chapter: convention-plugins, duration: 1h -->
* Convention Plugins
    * Sharing build logic across projects
    * Creating convention plugins in buildSrc
    * Convention plugins in included builds
    * Composing convention plugins
    * Standardizing project configurations
<!-- chapter: composite-builds, duration: 1h -->
* Composite Builds
    * What are composite builds?
    * Including builds with includeBuild
    * Dependency substitution
    * Developing libraries and applications together
    * Composite builds vs multi-project builds
<!-- chapter: gradle-kotlin-dsl, duration: 1h -->
* `Gradle` `Kotlin` DSL
    * Migrating from Groovy DSL to `Kotlin` DSL
    * Type-safe accessors
    * IDE support and code completion
    * Common patterns and idioms
<!-- chapter: build-scans, duration: 2h -->
* Build Scans
    * Enabling and publishing build scans
    * Analyzing build performance
    * Dependency insights
    * Identifying bottlenecks
    * Comparing builds
<!-- chapter: performance-optimization, duration: 2h -->
* Performance Optimization
    * Parallel execution
    * Configuration cache
    * Incremental builds and up-to-date checks
    * Daemon tuning
    * Profiling builds
    * Avoiding common performance pitfalls
<!-- chapter: artifact-publishing, duration: 2h -->
* Artifact Publishing
    * `Maven` Publish plugin
    * Publishing to `Maven` repositories
    * Publishing to Artifactory and `Nexus`
    * Signing artifacts
    * Publishing multi-variant libraries

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
