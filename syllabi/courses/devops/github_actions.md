---
tags:
  - practices:devops
  - practices:ci-cd
  - tools:github-actions
  - tools:gitlab
  - practices:automation
level: intermediate
category: devops
duration_hours: 16
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: github_actions -->
# `GitHub Actions` & `GitLab CI`

## Description
This course covers modern `CI/CD` pipeline design and implementation using `GitHub Actions` and
`GitLab CI`. Participants will learn how to author workflows, configure runners, manage artifacts
and environments, and leverage advanced features such as matrix builds and reusable workflows.
The course compares both platforms side by side, enabling participants to apply `CI/CD` best
practices regardless of which platform their organization uses.

This course is hands-on and assumes participants are already comfortable with `Git` and basic
software development workflows. It focuses on practical pipeline construction rather than
abstract `CI/CD` theory.

## Duration
16 hours / 2 days

## Intended Audience
* developers who want to automate their build, test, and deployment processes.
* `DevOps` engineers looking to adopt or migrate to `GitHub Actions` or `GitLab CI`.
* team leads responsible for establishing `CI/CD` standards and practices.
* anyone involved in software delivery who wants to understand modern pipeline tooling.

## Prerequisites
* `Solid` working knowledge of `Git` (branching, merging, pull requests).
* Basic understanding of `CI/CD` concepts (builds, tests, deployments).
* Familiarity with `YAML` syntax.
* Experience with at least one programming language.

## Objectives
* understand the core concepts and principles of modern `CI/CD` pipelines
* gain practical knowledge of `GitHub Actions` workflows and `GitLab CI` pipelines
* gain practical knowledge of runners, artifacts, and environments
* gain practical knowledge of matrix builds and reusable workflows

## Outline
<!-- chapter: introduction-to-modern-ci-cd, duration: 1h -->
* Introduction to Modern `CI/CD`
    * Evolution of `CI/CD` tooling
    * Pipeline as code philosophy
    * Comparing `GitHub Actions` and `GitLab CI` architectures
    * Event-driven vs schedule-driven pipelines
<!-- chapter: github-actions-fundamentals, duration: 2h -->
* `GitHub Actions` Fundamentals
    * Workflow files and `YAML` structure
    * Triggers and events
        * Push, pull request, and manual triggers
        * Webhook and repository dispatch events
        * Scheduled workflows with cron expressions
    * Jobs and steps
        * Job dependencies and ordering
        * Conditional execution with `if-expressions`
        * Timeout and concurrency settings
    * Actions marketplace
        * Using community actions
        * Versioning and pinning actions
<!-- chapter: gitlab-ci-fundamentals, duration: 2h -->
* `GitLab CI` Fundamentals
    * .`gitlab`-ci.yml structure
    * Stages and jobs
    * Pipeline types
        * Branch pipelines
        * Merge request pipelines
        * Multi-project pipelines
    * Rules and workflow keywords
    * include and extends for configuration reuse
<!-- chapter: runners-and-execution-environments, duration: 2h -->
* Runners and Execution Environments
    * `GitHub Actions` runners
        * `GitHub`-hosted vs self-hosted runners
        * Runner groups and labels
        * Runner images and pre-installed software
    * `GitLab CI` runners
        * Shared, group, and project runners
        * Runner executors (shell, `Docker`, `Kubernetes`)
        * Runner registration and configuration
    * Language setup actions
        * `setup-python`, `setup-node`, `setup-ruby` and similar
        * Built-in dependency caching via setup actions
        * How setup actions configure `PATH` and tool directories
        * Replacing manual `GITHUB_PATH` manipulation with setup actions
    * Container-based execution
        * Using `Docker` containers in jobs
        * Service containers and sidecars
<!-- chapter: artifacts-and-caching, duration: 2h -->
* Artifacts and Caching
    * Build artifacts
        * Uploading and downloading artifacts
        * Artifact retention policies
        * Passing data between jobs
    * Dependency caching
        * Built-in caching via setup actions (`setup-python`, `setup-node`)
        * `actions/cache` for tool-specific caches
        * Cache key strategies
            * Per-commit keys (`github.sha`) vs per-config keys (`hashFiles`) vs fixed keys
            * Tradeoffs between cache granularity and cache proliferation
            * Letting the tool manage its own staleness with a fixed cache key
        * Cache scopes and fallback behavior
        * `restore-keys` for partial cache matching and when it adds unnecessary complexity
    * Installing binaries from `GitHub` releases
        * Using `gh release download` with `GITHUB_TOKEN`
        * Why authentication is needed even for public repos (rate limiting)
        * Alternatives: `cargo-binstall`, `cargo install`, dedicated marketplace actions
        * Tradeoffs between pre-built binaries and compiling from source
    * Job outputs and environment files
<!-- chapter: environments-and-deployments, duration: 1h -->
* Environments and Deployments
    * Environment definitions and protection rules
    * Required environment declarations
        * Why `deploy-pages` requires the `github-pages` environment
        * Environment as a permissions and authorization mechanism
    * Deployment approvals and gates
    * Environment-specific variables and secrets
    * Deployment status tracking and rollback
    * Environment URL metadata
        * `When` environment URLs add value vs unnecessary noise
        * Keeping workflow files minimal and maintainable
    * `Jekyll` processing and `.nojekyll`
        * `When` `.nojekyll` is needed vs when `deploy-pages` bypasses `Jekyll` entirely
        * Avoiding unnecessary workarounds in modern deployment workflows
    * Review environments and dynamic environments
<!-- chapter: secrets-and-variables-management, duration: 1h -->
* Secrets and Variables Management
    * Repository, organization, and environment secrets
    * Variable scoping and precedence
    * Masking and protecting sensitive values
    * Integration with external secret stores
<!-- chapter: matrix-builds, duration: 1h -->
* Matrix Builds
    * Matrix strategy configuration
    * Combining multiple dimensions
    * Including and excluding specific combinations
    * Fail-fast and max-parallel settings
    * Dynamic matrices
<!-- chapter: reusable-workflows-and-templates, duration: 2h -->
* Reusable Workflows and Templates
    * `GitHub Actions` reusable workflows
        * Workflow call trigger
        * Inputs and secrets passing
        * Output propagation
    * `GitLab CI` templates and includes
        * Local, remote, and template includes
        * Extending and overriding jobs
    * Organizational workflow standardization
    * Versioning shared workflow libraries
<!-- chapter: advanced-pipeline-patterns, duration: 1h -->
* Advanced Pipeline Patterns
    * Monorepo path filtering
    * Conditional job execution and skip logic
    * Multi-stage deployment pipelines
    * Pipeline composition and chaining
    * Status checks and branch protection integration
    * Job consolidation
        * Runner spin-up overhead and artifact transfer costs
        * `When` to merge jobs vs when to keep them separate
        * Eliminating unnecessary job dependencies
<!-- chapter: security-and-compliance-in-pipelines, duration: 1h -->
* Security and Compliance in Pipelines
    * Supply chain security for actions and images
    * `OIDC` and keyless authentication
    * Code scanning and dependency review integration
    * Audit logging and compliance controls
    * Least privilege for workflow permissions

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
