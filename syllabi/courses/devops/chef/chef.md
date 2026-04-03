---
tags:
  - tools:chef
  - infrastructure:infrastructure-as-code
  - infrastructure:configuration-management
  - practices:devops
level: intermediate
category: devops
duration_hours: 24
audience:
  - audiences:devops
  - audiences:sysadmins
---
<!-- course: chef -->
# `Chef`

## Description
`Chef` is a powerful infrastructure automation platform that enables teams to define
infrastructure as code using a `Ruby`-based domain-specific language. This course covers
the complete `Chef` ecosystem, from workstation setup and cookbook authoring to `Chef` Server
administration and compliance automation with `Chef InSpec`. Participants will learn how to
model complex infrastructure configurations using resources, recipes, roles, and environments,
and will gain hands-on experience with modern testing workflows using `ChefSpec` and
`Test Kitchen`. By the end of the course, participants will be able to manage infrastructure
at scale, enforce compliance policies, and integrate `Chef` into a `DevOps` pipeline.

## Duration
24 hours / 3 days

## Intended Audience
* `DevOps` engineers responsible for automating server provisioning and configuration management.
* System administrators who want to bring infrastructure under programmatic control.
* Platform engineers building reusable configuration management frameworks.

## Prerequisites
* `Solid` `Linux` system administration skills (packages, services, networking).
* Familiarity with the command line and `SSH`.
* Basic knowledge of `Ruby` syntax is beneficial but not required.
* Experience with version control (`Git`).

## Objectives
* Understand the `Chef` architecture and how its components interact.
* Write resources, recipes, and cookbooks that configure infrastructure idempotently.
* Use roles, environments, and data bags to manage complex multi-node setups.
* Test cookbook code with `ChefSpec` (unit) and `Test Kitchen` (integration).
* Administer a `Chef` Server and manage node lifecycles with `knife`.
* Enforce compliance and security baselines using `Chef InSpec`.

## Outline
<!-- chapter: introduction-to-chef, duration: 2h -->
* Introduction to `Chef`
    * What is infrastructure as code and why it matters
    * Overview of the `Chef` ecosystem (`Chef Infra`, `Chef InSpec`, `Chef Habitat`)
    * Comparing `Chef` with `Ansible`, `Puppet`, and `SaltStack`
    * Core concepts: resources, recipes, cookbooks, nodes, and run lists

<!-- chapter: chef-architecture, duration: 2h -->
* `Chef` Architecture
    * `Chef` Server, workstation, and node relationships
    * The `Chef` client run lifecycle
    * Ohai and automatic attribute collection
    * `Chef` Solo vs. `Chef` Client/Server mode

<!-- chapter: workstation-setup-and-knife, duration: 2h -->
* Workstation Setup and `knife`
    * Installing the `Chef` Workstation
    * Configuring credentials and `knife.rb`
    * Core `knife` commands: `bootstrap`, node, role, environment, cookbook
    * Managing nodes and searching the `Chef` Server index

<!-- chapter: resources-and-recipes, duration: 3h -->
* Resources and Recipes
    * Built-in resources: `package`, `service`, `file`, `directory`, `execute`, `user`
    * Writing idempotent recipes
    * Resource guards (`only_if`, `not_if`) and notifications
    * Creating custom resources with the `resource` DSL

<!-- chapter: cookbooks-and-roles, duration: 3h -->
* Cookbooks and Roles
    * Cookbook structure and metadata
    * Versioning and dependency management with `Berkshelf`
    * Defining roles and applying run lists
    * `Chef` Supermarket: finding and using community cookbooks

<!-- chapter: attributes-and-data-bags, duration: 2h -->
* Attributes and Data Bags
    * Attribute precedence and merging rules
    * Defining default, override, and automatic attributes
    * Data bags: creating, encrypting, and querying structured data
    * Using data bags to manage users, credentials, and application config

<!-- chapter: templates-and-files, duration: 2h -->
* Templates and Files
    * Managing files with the `cookbook_file` resource
    * `ERB` templates and the `template` resource
    * Rendering dynamic configuration files
    * Partial templates and shared template helpers

<!-- chapter: chef-environments, duration: 2h -->
* `Chef` Environments
    * Defining environments and cookbook version constraints
    * Promoting cookbooks through dev, staging, and production
    * Environment-specific attribute overrides
    * Workflow patterns for multi-environment management

<!-- chapter: testing-with-chefspec-and-test-kitchen, duration: 3h -->
* Testing with `ChefSpec` and `Test Kitchen`
    * Unit testing recipes with `ChefSpec` and `RSpec` matchers
    * `Test Kitchen` architecture: drivers, provisioners, and verifiers
    * Writing `InSpec` integration tests in `Test Kitchen`
    * Running the full `TDD` cycle: write, converge, verify

<!-- chapter: chef-server-administration, duration: 2h -->
* `Chef` Server Administration
    * Installing and configuring `Chef` Server
    * Managing organizations, users, and permissions
    * Bootstrapping nodes and managing the node object lifecycle
    * Backup, restore, and upgrade strategies

<!-- chapter: compliance-with-chef-inspec, duration: 1h -->
* Compliance with `Chef InSpec`
    * `InSpec` architecture and resource model
    * Writing profiles and controls for compliance automation
    * Running compliance scans locally and via `Chef` Server
    * Integrating compliance reporting into the `DevOps` pipeline

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
