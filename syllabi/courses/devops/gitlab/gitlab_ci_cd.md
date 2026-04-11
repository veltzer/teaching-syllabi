---
tags:
  - tools:gitlab
  - practices:ci-cd
  - practices:devops
level: intermediate
category: devops
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
---
<!-- course: gitlab_ci_cd -->
# `GitLab` `CI/CD`

## Description
This course provides a comprehensive guide to `GitLab` `CI/CD`, covering everything from
basic pipeline configuration to advanced deployment strategies. Students will learn how to
write and maintain .`gitlab`-ci.yml files, configure runners, manage artifacts and secrets,
and implement security scanning within their pipelines. The course also covers advanced
topics such as multi-project pipelines, parent-child pipelines, review apps, container
building strategies, and `Auto DevOps`. By the end of the course, participants will be able
to design and implement robust `CI/CD` pipelines using `GitLab`.

## Duration
16 hours / 2 days

## Intended Audience
* Software developers and `DevOps` engineers who want to implement and manage `CI/CD` pipelines using `GitLab`.
* Teams migrating to `GitLab` or looking to improve their existing `GitLab` `CI/CD` workflows.

## Prerequisites
* Basic familiarity with `Git` version control.
* General understanding of `CI/CD` concepts.
* Some experience with command-line tools and `YAML` syntax.

## Objectives
* Understand `GitLab` `CI/CD` architecture and how pipelines are defined and executed.
* Write and maintain .`gitlab`-ci.yml configuration files with stages, jobs, variables, and rules.
* Configure and manage `GitLab` Runners for different execution environments.
* Implement advanced pipeline patterns including multi-project and parent-child pipelines.
* Build and push container images using `Docker`-in-`Docker` and `Kaniko`.
* Integrate security scanning (`SAST`, `DAST`, dependency scanning) into pipelines.

## Outline
<!-- chapter: gitlab-overview, duration: 1h -->
* `GitLab` Overview
    * What is `GitLab`?
    * `GitLab` editions and features
    * `CI/CD` architecture in `GitLab`
    * The role of the `GitLab` Runner
<!-- chapter: gitlab-ci-yml-syntax, duration: 1h -->
* .`gitlab`-ci.yml Syntax
    * Structure of a pipeline configuration `file`
    * Defining stages
    * Job configuration and keywords
    * rules, only, except directives
    * include and extends for reusable configuration
<!-- chapter: stages-and-jobs, duration: 1h -->
* Stages and Jobs
    * Defining and ordering stages
    * Job dependencies and needs
    * Parallel jobs and matrix builds
    * Manual and delayed jobs
    * Job timeout and retry configuration
<!-- chapter: runners, duration: 1h -->
* Runners
    * Shared runners
    * Specific runners
    * Group runners
    * Runner executors (shell, `Docker`, `Kubernetes`)
    * Registering and configuring runners
    * Runner tags and job routing
<!-- chapter: variables-and-secrets, duration: 1h -->
* Variables and Secrets
    * Predefined `CI/CD` variables
    * Custom variables at project, group, and instance level
    * Protected and masked variables
    * Variable precedence and scoping
    * Using variables in scripts and configuration
<!-- chapter: artifacts-and-caching, duration: 1h -->
* Artifacts and Caching
    * Defining and collecting job artifacts
    * Artifact expiration and browsing
    * Cache configuration and scope
    * Cache keys and policies
    * Differences between artifacts and cache
<!-- chapter: pipeline-triggers, duration: 1h -->
* Pipeline Triggers
    * Trigger tokens and `API` triggers
    * Webhook-based triggers
    * Scheduled pipelines
    * Pipeline subscriptions
<!-- chapter: multi-project-pipelines, duration: 1h -->
* Multi-Project Pipelines
    * Cross-project pipeline triggering
    * Passing variables between projects
    * Downstream pipeline status tracking
<!-- chapter: parent-child-pipelines, duration: 1h -->
* Parent-Child Pipelines
    * Defining child pipelines with trigger
    * Dynamic child pipelines
    * Strategy and dependency configuration
<!-- chapter: environments-and-deployments, duration: 1h -->
* Environments and Deployments
    * Defining environments in .`gitlab`-ci.yml
    * Environment URLs and dashboards
    * Deployment tracking and history
    * Stopping environments
    * Protected environments
<!-- chapter: review-apps, duration: 1h -->
* Review Apps
    * What are review apps?
    * Configuring dynamic environments for merge requests
    * Auto-stopping review apps
<!-- chapter: container-building-strategies, duration: 1h -->
* Container Building Strategies
    * `Docker`-in-`Docker` (DinD) setup and configuration
    * `Kaniko` for building images without `Docker` daemon
    * `GitLab` Container Registry
    * Pushing and pulling images from the registry
    * Image tagging strategies
<!-- chapter: auto-devops, duration: 1h -->
* `Auto DevOps`
    * What is `Auto DevOps`?
    * Auto Build, Auto Test, Auto Deploy
    * Customizing `Auto DevOps` stages
    * `When` to use and `when` to avoid `Auto DevOps`
<!-- chapter: merge-request-pipelines, duration: 1h -->
* Merge Request Pipelines
    * Merge request pipeline vs branch pipeline
    * Merged results pipelines
    * Merge trains
    * Configuring pipelines for merge requests
<!-- chapter: security-scanning, duration: 1h -->
* Security Scanning
    * `SAST` (Static Application Security Testing)
    * `DAST` (Dynamic Application Security Testing)
    * Dependency scanning
    * Container scanning
    * Security dashboard and vulnerability management
<!-- chapter: compliance-pipelines, duration: 1h -->
* Compliance Pipelines
    * What are compliance pipelines?
    * Configuring compliance frameworks
    * Enforcing pipeline requirements across projects
    * Audit and reporting

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
