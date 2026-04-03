---
tags:
  - concepts:architecture
  - concepts:best-practices
  - practices:devops
  - infrastructure:containers
level: intermediate
category: architecture
duration_hours: 16
audience:
  - audiences:developers
  - audiences:architects
  - audiences:devops
---
<!-- course: twelve_factor_app -->
# The Twelve-Factor App

## Description
This course explores the twelve-factor methodology for building modern, cloud-native applications. Participants will learn each of the twelve factors in depth, understand the reasoning behind them, and see how they apply to real-world development using containers and `Kubernetes`. The course also covers extensions beyond the original twelve factors, including `API`-first design, telemetry, and security considerations.

## Duration
16 hours / 1 day

## Intended Audience
* Software developers building cloud-native applications
* Software architects designing deployment-ready systems
* `DevOps` engineers seeking to align development practices with operational needs
* Technical leads guiding teams toward modern application design

## Prerequisites
* Experience developing web applications or backend services
* Basic familiarity with `Docker` and containerization concepts
* Understanding of environment variables and configuration management
* General awareness of cloud deployment models

## Required Knowledge
* `Docker` Fundamentals (or equivalent experience)

## Objectives
* Understand the motivation and principles behind the twelve-factor methodology
* Apply each of the twelve factors to application design and development
* Identify violations of twelve-factor principles in existing applications
* Map twelve-factor practices to container and `Kubernetes` deployment patterns
* Extend the methodology with modern practices such as `API`-first design, telemetry, and security

## Outline
<!-- chapter: introduction-to-the-twelve-factor-methodology, duration: 1h -->
* Introduction to the Twelve-Factor Methodology
    * Origins and motivation
    * The problem of environment-dependent applications
    * Overview of the twelve factors
    * Relationship to cloud-native and `microservices` architectures
<!-- chapter: codebase, duration: 1h -->
* Codebase
    * One codebase tracked in version control, many deploys
    * Relationship between codebases, apps, and deploys
    * Monorepo vs multi-repo considerations
<!-- chapter: dependencies, duration: 1h -->
* Dependencies
    * Explicitly declare and isolate dependencies
    * Dependency manifests and lock files
    * Avoiding reliance on system-wide packages
    * Vendoring vs package managers
<!-- chapter: config, duration: 1h -->
* Config
    * Strict separation of config from code
    * Storing config in environment variables
    * Config management in containerized environments
    * Secrets management
<!-- chapter: backing-services, duration: 1h -->
* Backing Services
    * Treating backing services as attached resources
    * Loose coupling to databases, caches, and message queues
    * Swapping backing services without code changes
    * Service discovery patterns
<!-- chapter: build-release-run, duration: 1h -->
* Build, Release, Run
    * Strictly separating build, release, and run stages
    * Immutable release artifacts
    * Release versioning and rollback
    * `CI/CD` pipeline alignment
<!-- chapter: processes, duration: 1h -->
* Processes
    * Executing the app as one or more stateless processes
    * Share-nothing architecture
    * Sticky sessions and their drawbacks
    * Storing state in backing services
<!-- chapter: port-binding, duration: 1h -->
* Port Binding
    * Exporting services via port binding
    * Self-contained applications
    * Embedded servers vs external application servers
<!-- chapter: concurrency, duration: 1h -->
* Concurrency
    * Scaling out via the process model
    * Process types and workload diversity
    * Horizontal scaling patterns
    * Container orchestration and scaling
<!-- chapter: disposability, duration: 1h -->
* Disposability
    * Maximizing robustness with fast startup and graceful shutdown
    * Signal handling and shutdown hooks
    * Crash-only design
    * Robustness against sudden termination
<!-- chapter: dev-prod-parity, duration: 1h -->
* Dev/Prod Parity
    * Keeping development, staging, and production as similar as possible
    * Time gap, personnel gap, and tools gap
    * Using containers to reduce environment drift
    * Local development with production-like services
<!-- chapter: logs, duration: 1h -->
* Logs
    * Treating logs as event streams
    * Writing to stdout/stderr
    * Log aggregation and centralized logging
    * Structured logging practices
<!-- chapter: admin-processes, duration: 1h -->
* Admin Processes
    * Running admin and management tasks as one-off processes
    * Database migrations as admin processes
    * REPL and diagnostic tools
    * Automation of administrative tasks
<!-- chapter: beyond-twelve-factor, duration: 1h -->
* Beyond Twelve-Factor
    * `API`-first design
    * Telemetry and observability
    * Security as a first-class concern
    * Authentication and authorization patterns
<!-- chapter: practical-application-with-containers-and-kubernetes, duration: 2h -->
* Practical Application with Containers and `Kubernetes`
    * Mapping twelve-factor principles to `Docker` best practices
    * `Kubernetes` primitives aligned with twelve-factor patterns
    * `ConfigMaps`, Secrets, and environment configuration
    * Health checks, readiness probes, and disposability
    * Deploying a twelve-factor application end to end

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
