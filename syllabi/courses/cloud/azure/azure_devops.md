---
tags:
  - infrastructure:azure
  - infrastructure:cloud
  - practices:devops
  - practices:ci-cd
level: intermediate
category: cloud
duration_hours: 16
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
  - audiences:managers
---
<!-- course: azure_devops -->
# `Azure DevOps`

## Description
This course provides a comprehensive overview of the `Azure DevOps` platform and its core services. Participants will learn how to plan work with boards, manage source code with repos, build `CI/CD` pipelines, manage packages with artifacts, create test plans, and implement release management strategies. The course is designed for teams looking to adopt `Azure DevOps` as their end-to-end software delivery platform.

## Duration
16 hours / 2 days

## Intended Audience
* Developers and `DevOps` engineers adopting `Azure DevOps` for their software delivery workflow.
* Team leads and project managers who want to manage work items and track progress with `Azure Boards`.
* QA engineers responsible for testing strategy and test plan management.

## Prerequisites
* Basic understanding of software development lifecycle concepts.
* Familiarity with version control (e.g., `Git`).
* Experience with `CI/CD` concepts is helpful but not required.

## Objectives
* Navigate and configure `Azure DevOps` projects and organizations.
* Manage work items, sprints, and backlogs using `Azure Boards`.
* Use `Azure Repos` for source control with `Git`.
* Build and maintain `CI/CD` pipelines using `Azure Pipelines`.
* Manage package feeds with `Azure Artifacts`.
* Create and execute test plans with `Azure Test Plans`.
* Implement release management and deployment strategies.

## Outline
<!-- chapter: introduction-to-azure-devops, duration: 2h -->
* Introduction to `Azure DevOps`
    * `Azure DevOps` services overview
    * Organizations, projects, and teams
    * Navigation and project settings
    * Extensions and marketplace
    * Security and permissions model
<!-- chapter: azure-boards, duration: 2h -->
* `Azure Boards`
    * Work item types and customization
    * Backlogs and sprint planning
    * `Kanban` boards and task boards
    * Queries and dashboards
    * Epics, features, and user stories
    * Integration with `Azure Repos` and `Azure Pipelines`
<!-- chapter: azure-repos, duration: 2h -->
* `Azure Repos`
    * `Git` repositories in `Azure DevOps`
    * Branching strategies and branch policies
    * Pull requests and code reviews
    * Branch protection and merge policies
    * Repository management and permissions
    * Integration with `IDEs` and editors
<!-- chapter: azure-pipelines, duration: 3h -->
* `Azure Pipelines`
    * `YAML` pipelines and classic pipelines
    * Build pipeline fundamentals
    * Triggers and pipeline variables
    * Stages, jobs, and steps
    * Pipeline templates and reuse
    * Agent pools and self-hosted agents
    * Multi-stage pipelines
    * Service connections and secure files
    * Pipeline caching and optimization
<!-- chapter: azure-artifacts, duration: 2h -->
* `Azure Artifacts`
    * Package feeds and upstream sources
    * `NuGet`, `npm`, `Maven`, `Python`, and universal packages
    * Versioning strategies
    * Publishing and consuming packages
    * Feed permissions and scoping
    * Integration with `Azure Pipelines`
<!-- chapter: azure-test-plans, duration: 2h -->
* `Azure Test Plans`
    * Manual testing and test case management
    * Test suites and test configurations
    * Exploratory testing
    * Test execution and tracking
    * Integration with `Azure Boards` and `Azure Pipelines`
    * Automated test integration
<!-- chapter: release-management, duration: 3h -->
* Release Management
    * Deployment strategies (blue-green, canary, rolling)
    * Environments and approvals
    * Gates and deployment gates
    * Release pipelines vs. multi-stage `YAML` pipelines
    * Deployment to `Azure` services
    * Rollback strategies
    * Monitoring deployments

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
