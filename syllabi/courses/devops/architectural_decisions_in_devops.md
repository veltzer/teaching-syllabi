---
tags:
  - practices:devops
  - concepts:architecture
  - practices:ci-cd
  - infrastructure:infrastructure-as-code
level: advanced
category: devops
duration_hours: 24
audience:
  - audiences:architects
  - audiences:devops
  - audiences:managers
---
<!-- course: architectural_decisions_in_devops -->
# Architectural Decisions in `DevOps`

## Description
This course explores the key architectural decisions that `DevOps` teams face when designing and
evolving their software delivery pipelines, infrastructure, and operational practices. Rather than
prescribing a single "right" approach, this course examines the tradeoffs, constraints, and
organizational implications of each decision. Participants will learn to evaluate options such as
monorepo vs polyrepo, declarative vs imperative infrastructure, push vs pull deployment models,
and many more, using real-world case studies and structured decision frameworks.

This course is not a hands-on tool tutorial. It focuses on the architectural thinking behind
tool and process choices so that teams can `make` informed decisions that align with their
organizational context, scale, and maturity.

## Duration
24 hours / 3 days

## Intended Audience
* `DevOps` engineers and platform engineers making infrastructure and pipeline decisions.
* Software architects who need to understand the operational implications of their designs.
* Engineering managers and tech leads responsible for tooling and process choices.
* Site reliability engineers evaluating operational tradeoffs.
* Anyone involved in designing or evolving a software delivery organization.

## Prerequisites
* Basic familiarity with software development workflows (version control, `CI/CD` concepts).
* General understanding of `cloud computing` and containerization concepts.
* Experience working in a team that delivers software to production.

## Objectives
* understand the core concepts and principles of Architectural Decisions in ```DevOps``
* gain practical knowledge of Decision Frameworks for ```DevOps``
* gain practical knowledge of Source Code Management Strategy
* gain practical knowledge of `CI/CD`` Pipeline Architecture

## Outline
<!-- chapter: decision-frameworks-for-devops, duration: 1h -->
* Decision Frameworks for `DevOps`
    * What makes a decision "architectural" in `DevOps`
    * Reversibility and cost of change
    * Organizational context and Conway's Law
    * Evaluating tradeoffs systematically
    * Documenting decisions with Architecture Decision Records (ADRs)
<!-- chapter: source-code-management-strategy, duration: 2h -->
* Source Code Management Strategy
    * Monorepo vs polyrepo
        * Scaling considerations
        * Tooling requirements for monorepos
        * Dependency management across repositories
        * Impact on team autonomy and coupling
    * Branching strategies
        * Trunk-based development vs feature branching
        * `Git` Flow and its variations
        * Release branching vs release from trunk
        * Branch protection and merge policies
    * Code ownership models
        * Strong ownership vs collective ownership
        * CODEOWNERS and review policies
<!-- chapter: ci-cd-pipeline-architecture, duration: 3h -->
* `CI/CD` Pipeline Architecture
    * Centralized vs decentralized pipeline management
        * Shared pipeline libraries and templates
        * Platform teams vs embedded `DevOps`
        * Balancing standardization with team autonomy
    * Build vs buy for `CI/CD` tooling
        * Self-hosted vs `SaaS` `CI/CD` systems
        * Vendor lock-in considerations
        * Migration cost and portability
    * Pipeline `design patterns`
        * Fan-out and fan-in
        * Pipeline as code vs UI-configured pipelines
        * Triggered vs scheduled vs event-driven pipelines
    * Build caching and dependency management
        * Remote build caches
        * Dependency vendoring vs dynamic resolution
        * Reproducible builds
    * `GitOps` vs traditional push-based `CI/CD`
        * Pull-based reconciliation model
        * Drift detection and self-healing
        * When `GitOps` is appropriate and when it is not
<!-- chapter: artifact-management-and-promotion, duration: 1h -->
* Artifact Management and Promotion
    * Artifact repository strategies
        * Single vs multiple artifact repositories
        * Promotion between stages (dev, staging, production)
    * Versioning strategies
        * Semantic versioning vs commit-based versioning
        * Immutable artifacts and traceability
    * Container image management
        * Base image strategies and supply chain security
        * Image scanning and policy enforcement
        * Slim images vs full images
<!-- chapter: infrastructure-as-code-decisions, duration: 2h -->
* Infrastructure as Code Decisions
    * Declarative vs imperative approaches
        * `Terraform` and its state model
        * `Pulumi` and general-purpose languages
        * `CloudFormation` and cloud-native IaC
    * State management tradeoffs
        * Remote state backends
        * State locking and collaboration
        * State file per environment vs shared state
    * Module and abstraction strategies
        * Reusable modules vs inline configuration
        * Abstraction layers and platform engineering
    * Drift detection and reconciliation
        * Continuous vs on-demand drift detection
        * Auto-remediation risks and benefits
<!-- chapter: containerization-decisions, duration: 1h -->
* Containerization Decisions
    * When to containerize and when not to
        * Suitability for different workload types
        * Overhead and complexity costs
    * Container runtime choices
        * `Docker` vs `containerd` vs other runtimes
        * Rootless containers and security implications
    * Base image strategies
        * Distroless vs `alpine` vs full OS images
        * Custom base images and organizational standards
        * Multi-stage builds and build optimization
<!-- chapter: orchestration-and-compute-choices, duration: 2h -->
* Orchestration and Compute Choices
    * `Kubernetes` vs managed container services vs serverless
        * Operational complexity and team capability
        * Cost models and scaling characteristics
        * Portability vs managed convenience
    * `Kubernetes` architecture decisions
        * Cluster per team vs shared clusters
        * Namespace strategies and multi-tenancy
        * Managed `Kubernetes` vs self-managed
    * Serverless architecture tradeoffs
        * Cold start implications
        * Vendor lock-in depth
        * Event-driven vs request-driven models
<!-- chapter: environment-strategy, duration: 2h -->
* Environment Strategy
    * How many environments and why
        * Production-like vs lightweight environments
        * Cost implications of environment proliferation
    * Ephemeral vs persistent environments
        * Preview environments for pull requests
        * On-demand staging environments
        * Cleanup and lifecycle management
    * Environment parity and configuration drift
        * Ensuring consistency across environments
        * Data management in non-production environments
<!-- chapter: deployment-strategies, duration: 2h -->
* Deployment Strategies
    * Blue/green deployments
        * Infrastructure cost implications
        * Database compatibility requirements
    * Canary deployments
        * Traffic splitting mechanisms
        * Metrics and rollback criteria
    * Rolling deployments
        * Update ordering and health checks
        * Backward compatibility requirements
    * Feature flags as a deployment strategy
        * Flag lifecycle management
        * Testing complexity with flag combinations
        * Technical debt from long-lived flags
    * Progressive delivery and experimentation
<!-- chapter: configuration-and-secrets-management, duration: 1h -->
* Configuration and Secrets Management
    * Baked-in vs runtime configuration
        * Immutable deployments with baked config
        * Dynamic configuration and feature toggles
        * Restart vs hot-reload tradeoffs
    * Secrets management approaches
        * Vault and secrets managers vs encrypted config
        * Secret rotation strategies
        * Secrets in `CI/CD` pipelines
    * Configuration as code vs configuration services
<!-- chapter: observability-architecture, duration: 2h -->
* Observability Architecture
    * Metrics vs logs vs traces
        * When to use each signal type
        * Cost and storage implications
        * Correlation across signal types
    * Push vs pull collection models
        * `Prometheus` pull model vs agent-based push
        * Scalability considerations
    * Centralized vs distributed observability
        * Single pane of glass vs team-owned dashboards
        * Observability platform build vs buy
    * Alerting strategy
        * Alert fatigue and noise reduction
        * SLO-based alerting vs threshold-based alerting
        * On-call and escalation architecture
<!-- chapter: service-mesh-decisions, duration: 1h -->
* Service Mesh Decisions
    * When a service mesh is warranted
        * Complexity vs benefit analysis
        * Alternative approaches to service-to-service communication
    * Sidecar proxy vs proxyless mesh
        * Resource overhead considerations
        * Performance implications
    * mTLS, traffic management, and observability through mesh
<!-- chapter: multi-cloud-and-cloud-strategy, duration: 1h -->
* Multi-Cloud and Cloud Strategy
    * Single cloud vs multi-cloud vs hybrid
        * Cost of abstraction layers
        * Avoiding vendor lock-in vs embracing cloud-native services
        * Regulatory and data sovereignty requirements
    * Cloud-agnostic tooling tradeoffs
        * Lowest common denominator problem
        * Abstraction layers and their maintenance cost
    * Disaster recovery and high availability across regions
<!-- chapter: database-migration-strategies-in-ci-cd, duration: 1h -->
* Database Migration Strategies in `CI/CD`
    * Schema migration approaches
        * Versioned migrations vs state-based migrations
        * Forward-only vs reversible migrations
    * Zero-downtime migration patterns
        * Expand and contract pattern
        * Dual-write strategies
    * Data migration and seeding in pipelines
<!-- chapter: testing-strategy-tradeoffs, duration: 2h -->
* Testing Strategy Tradeoffs
    * The test pyramid in `CI/CD` pipelines
        * Unit vs integration vs end-to-end balance
        * Cost of test maintenance at each level
    * Shift-left testing
        * Static analysis and linting in pipelines
        * Security scanning integration points
        * Contract testing vs integration testing
    * Test environment management
        * Test data strategies
        * Service virtualization and mocking
        * Parallel test execution and pipeline speed
    * Testing in production
        * Synthetic monitoring
        * Chaos engineering as a testing practice
        * Observability-driven testing

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
