---
tags:
  - tools:maven
  - build:java
  - build:jvm
  - practices:build-automation
  - languages:java
level: intermediate
category: build-system
duration_hours: 24
audience:
  - audiences:developers
  - audiences:java-developers
---
<!-- course: maven -->
# `Maven`

## Description
`Apache Maven` is the de-facto standard build and project management tool for `Java` and `JVM`-based projects.
This course provides a thorough understanding of `Maven`'s build lifecycle, dependency resolution, and plugin
ecosystem, enabling developers to manage complex multi-module projects with confidence. Participants will learn
to work with `Maven` repositories, configure environment-specific profiles, and integrate `Maven` into modern
`CI/CD` pipelines. The course closes with a practical comparison against `Gradle` to help teams `make` informed
tooling decisions.

## Duration
24 hours / 3 days

## Intended Audience
* `Java` and `JVM` developers who want to master their primary build toolchain.
* Backend engineers responsible for maintaining and improving build pipelines.
* `DevOps` engineers integrating `Maven`-based projects into automated delivery pipelines.
* Tech leads evaluating build tooling strategies for their teams.

## Prerequisites
* `Solid` working knowledge of `Java` programming.
* Basic familiarity with the command line and `file` system navigation.
* Some prior exposure to compiling and running `Java` applications is assumed.

## Objectives
* Understand the `Maven` build lifecycle and its phases.
* Create and maintain well-structured `POM` files.
* Manage project dependencies and transitive dependency resolution.
* Work with local, central, and private `Maven` repositories.
* Configure and use `Maven` plugins effectively.
* Build multi-module `Maven` projects.
* Use profiles to manage environment-specific configuration.
* Manage release versions and automate the release process.
* Write custom `Maven` plugins for specialized build requirements.
* Integrate `Maven` builds with `CI/CD` systems.
* Evaluate trade-offs between `Maven` and `Gradle`.

## Outline
<!-- chapter: introduction-to-maven, duration: 2h -->
* Introduction to `Maven`:
    * History and motivation behind `Maven`.
    * `Maven` philosophy: convention over configuration.
    * Installation and verifying the environment.
    * The `Maven` command-line interface.
<!-- chapter: project-structure-and-pom, duration: 2h -->
* Project Structure and `POM`:
    * Standard directory layout.
    * Anatomy of the `pom.xml` `file`.
    * Coordinates: `groupId`, `artifactId`, `version`.
    * Parent `POM` and inheritance.
<!-- chapter: build-lifecycle-and-phases, duration: 2h -->
* Build Lifecycle and Phases:
    * The three built-in lifecycles: default, `clean`, site.
    * Lifecycle phases and their ordering.
    * Binding plugins to phases.
    * Running partial builds and skipping phases.
<!-- chapter: dependencies-and-repositories, duration: 3h -->
* Dependencies and Repositories:
    * Declaring dependencies and dependency scopes.
    * Transitive dependencies and dependency mediation.
    * Excluding and overriding transitive dependencies.
    * `Maven` Central, remote repositories, and mirrors.
    * Setting up a private repository with `Nexus` or `Artifactory`.
    * `Bill of Materials` (`BOM`) for version alignment.
<!-- chapter: plugins-and-goals, duration: 2h -->
* Plugins and Goals:
    * Plugin lifecycle and goal binding.
    * Commonly used core plugins: compiler, surefire, jar, shade.
    * Configuring plugin executions.
    * Plugin management in parent `POM`.
<!-- chapter: multi-module-projects, duration: 3h -->
* Multi-Module Projects:
    * Structuring a multi-module `Maven` reactor.
    * Aggregator and parent `POM` patterns.
    * Inter-module dependencies.
    * Reactor build order and selective builds.
    * Sharing configuration across modules.
<!-- chapter: profiles-and-environment-configuration, duration: 2h -->
* Profiles and Environment Configuration:
    * Declaring and activating profiles.
    * Environment-specific properties and resources.
    * Profile activation by OS, JDK, or property.
    * Best practices for portable builds.
<!-- chapter: release-and-version-management, duration: 2h -->
* Release and Version Management:
    * SNAPSHOT vs. release versioning.
    * The `maven-release-plugin` workflow.
    * Semantic versioning practices.
    * Automating changelog and tagging.
<!-- chapter: custom-plugins, duration: 2h -->
* Custom Plugins:
    * Plugin development lifecycle.
    * Writing a `Mojo` in `Java`.
    * Accessing project metadata from a plugin.
    * Testing and distributing custom plugins.
<!-- chapter: integration-with-ci-cd, duration: 2h -->
* Integration with `CI/CD`:
    * Running `Maven` in `Jenkins`, `GitHub Actions`, and `GitLab CI`.
    * Caching the local repository for faster builds.
    * Deploying artifacts to remote repositories from pipelines.
    * Build reproducibility and deterministic builds.
<!-- chapter: maven-vs-gradle-comparison, duration: 2h -->
* `Maven` vs `Gradle` Comparison:
    * Build model and configuration style differences.
    * Performance: incremental builds and build caching.
    * Ecosystem and plugin availability.
    * Choosing the right tool for your project.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
