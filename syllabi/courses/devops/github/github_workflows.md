---
tags:
  - tools:github
  - practices:ci-cd
  - practices:automation
  - practices:devops
level: intermediate
category: devops
duration_hours: 8
audience:
  - audiences:developers
  - practices:devops
---
# GitHub Workflows

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
`GitHub Actions` and `GitHub Workflows` provide powerful automation capabilities for continuous integration, continuous deployment, and general task automation. This course covers fundamental to advanced workflow concepts and teaches how to effectively automate software development processes using `GitHub's` native `CI/CD` platform.

## Duration
8 hours / 1 day

## Intended Audience
* Software developers and `DevOps` engineers
* Development team leads and project managers
* System administrators managing deployment processes
* Quality assurance engineers working with automated testing
* Open source contributors and maintainers
* Anyone looking to automate repetitive development tasks

## Prerequisites
* Basic understanding of `Git` version control system
* Familiarity with `GitHub` repository management
* Basic knowledge of command-line interfaces
* Understanding of software development lifecycle concepts
* Basic familiarity with `YAML` syntax (helpful but not required)
* Experience with at least one programming language
* Access to a `GitHub` account with repository creation permissions

## Objectives
* Create and configure `GitHub Actions` workflows for automated tasks
* Implement `CI/CD` pipelines for code testing, building, and deployment
* Utilize pre-built actions from the `GitHub Marketplace`
* Write custom actions using `JavaScript`, `Docker`, and composite actions
* Manage workflow triggers, events, and scheduling with `cron` expressions
* Handle secrets, environment variables, and secure deployment practices
* Debug and troubleshoot workflow failures effectively
* Optimize workflow performance and resource usage
* Implement matrix builds for multi-platform testing
* Apply best practices for workflow organization and maintainability

## Outline
* Introduction to `GitHub Actions` and Workflows
    * Overview of `CI/CD` concepts and benefits
    * `GitHub Actions` architecture and components
    * Workflows, jobs, steps, and actions relationship
    * `GitHub Actions` vs other `CI/CD` platforms
    * Setting up your first workflow
    * Understanding the `.github/workflows` directory
    * Basic `YAML` syntax for workflows
* Workflow Fundamentals
    * Workflow file structure and syntax
    * Essential workflow components (`name`, `on`, `jobs`)
    * Understanding runners (`ubuntu-latest`, `windows-latest`, `macos-latest`)
    * Job dependencies and execution order
    * Workflow status badges and monitoring
    * Basic workflow examples and templates
* Events and Triggers
    * Push and pull request triggers
    * Scheduled workflows with `cron` expressions
    * Manual workflow dispatch (`workflow_dispatch`)
    * Repository events (`issues`, `releases`, `fork`)
    * External webhooks and repository dispatch
    * Conditional execution with `if` statements
    * Path-based filtering and branch targeting
* Actions and Marketplace
    * Using pre-built actions from `GitHub Marketplace`
    * Popular actions (`actions/checkout`, `actions/setup-node`, `actions/upload-artifact`)
    * Action versioning and pinning strategies
    * Reading action documentation and parameters
    * Community actions vs official actions
    * Action security considerations
* Environment Management
    * Working with environment variables (`env`, `$GITHUB_ENV`)
    * Using `GitHub Secrets` for sensitive data
    * Repository, environment, and organization secrets
    * Context variables (`${{ github.ref }}`, `${{ runner.os }}`)
    * Artifact upload and download (`actions/upload-artifact`)
    * Cache management (`actions/cache`)
* Advanced Workflow Features
    * Matrix builds for multi-platform testing
    * Conditional jobs and steps
    * Job outputs and data passing between jobs
    * Reusable workflows and workflow templates
    * Composite actions creation
    * Service containers and databases
    * Self-hosted runners setup and management
* Custom Actions Development
    * Types of custom actions (`JavaScript`, `Docker`, `Composite`)
    * Creating `JavaScript` actions with `Node.js`
    * Building `Docker` container actions
    * Action metadata files (`action.yml`)
    * Input and output parameters
    * Publishing actions to `GitHub Marketplace`
    * Action testing and validation
* Best Practices and Optimization
    * Workflow organization and naming conventions
    * Security best practices and `GITHUB_TOKEN` permissions
    * Performance optimization and resource management
    * Debugging workflows and troubleshooting common issues
    * Monitoring workflow usage and billing
    * Documentation and team collaboration
    * Version control for workflow files

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
