---
tags:
  - languages:java
  - practices:build-systems
  - practices:ci-cd
level: intermediate
category: language
duration_hours: 16
audience:
  - audiences:developers
---
<!-- course: java_maven -->
# `Java` `Maven`

## Description
This course provides a thorough exploration of `Apache Maven` as the standard build and project management tool for `Java` applications. Starting from `POM` structure and lifecycle fundamentals, the course progresses through dependency management, plugin development, multi-module projects, and CI integration. Students will gain the skills to manage complex `Java` builds with confidence and set up professional release workflows.

## Duration
16 hours / 1 day

## Intended Audience
* `Java` developers who want to master `Maven` for project builds and dependency management
* `DevOps` engineers responsible for `Java` build pipelines
* Team leads standardizing build processes across `Java` projects

## Prerequisites
* Working knowledge of `Java` programming
* Basic familiarity with the command line
* Understanding of software project structure and compilation concepts

## Objectives
* Understand the `Maven` `POM` structure and project object model
* Master `Maven` lifecycle phases and how they orchestrate builds
* Manage dependencies effectively using repositories, scopes, and BOMs
* Configure and use `Maven` plugins for custom build tasks
* Set up multi-module projects with proper inheritance and aggregation
* Integrate `Maven` builds into `CI/CD` pipelines

## Outline
<!-- chapter: introduction-to-maven, duration: 1h -->
* Introduction to `Maven`
    * What is `Maven` and why use it
    * Convention over configuration philosophy
    * Installing and configuring `Maven`
    * The `Maven` wrapper
<!-- chapter: pom-structure, duration: 1h -->
* `POM` Structure
    * Project coordinates: groupId, artifactId, version
    * `POM` inheritance and the super `POM`
    * Effective `POM`
    * Properties and variable substitution
    * `POM` packaging types
<!-- chapter: lifecycle-and-phases, duration: 1h -->
* Lifecycle and Phases
    * The default lifecycle
    * The `clean` lifecycle
    * The site lifecycle
    * Phase bindings and goals
    * Executing specific phases and goals
<!-- chapter: dependency-management, duration: 2h -->
* Dependency Management
    * Declaring dependencies
    * Dependency scopes: compile, provided, runtime, test, system
    * Transitive dependencies and dependency resolution
    * Dependency exclusions
    * Bill of Materials (BOM) imports
    * Dependency convergence and version conflicts
    * The dependencyManagement section
<!-- chapter: repositories, duration: 1h -->
* Repositories
    * Local repository structure
    * Central repository and remote repositories
    * Repository mirrors and settings.`xml`
    * Deploying artifacts to remote repositories
    * Repository managers: `Nexus` and Artifactory
<!-- chapter: plugins, duration: 2h -->
* Plugins
    * Plugin architecture and configuration
    * Commonly used plugins: compiler, surefire, jar, war
    * The `Maven` shade plugin and fat JARs
    * Code quality plugins: Checkstyle, SpotBugs, PMD
    * Custom plugin configuration and execution bindings
<!-- chapter: profiles, duration: 1h -->
* Profiles
    * Defining and activating profiles
    * Environment-specific profiles
    * Profile activation triggers
    * Using profiles for build customization
<!-- chapter: multi-module-projects, duration: 2h -->
* Multi-Module Projects
    * Aggregation vs inheritance
    * Parent `POM` design
    * Module dependency ordering and the reactor
    * Building specific modules
    * Sharing configuration across modules
<!-- chapter: release-plugin-and-versioning, duration: 2h -->
* Release Plugin and Versioning
    * SNAPSHOT vs release versions
    * The `Maven` release plugin workflow
    * Preparing and performing releases
    * Version management strategies
    * The versions plugin
<!-- chapter: site-generation, duration: 1h -->
* Site Generation
    * Generating project documentation
    * Configuring reports: Javadoc, test results, code coverage
    * Customizing the site descriptor
    * Publishing project sites
<!-- chapter: ci-integration, duration: 2h -->
* CI Integration
    * `Maven` in `Jenkins` pipelines
    * `Maven` in `GitHub Actions` and `GitLab CI`
    * Caching strategies for faster builds
    * Parallel builds and build optimization
    * Reproducible builds

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
