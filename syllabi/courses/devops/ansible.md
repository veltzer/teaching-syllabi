---
tags:
  - practices:devops
  - tools:ansible
  - infrastructure:configuration-management
  - infrastructure:cloud
  - practices:automation
level: intermediate
category: devops
duration_hours: 16
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: ansible -->
# `Ansible`

## Description
This course provides a thorough introduction to `Ansible` as a configuration management and
automation tool. Participants will learn how to write playbooks, organize code with roles, manage
inventory, use modules effectively, and understand the principle of idempotency. The course also
covers `Ansible Galaxy` for sharing and reusing roles, AWX/Tower for enterprise workflow
management, and testing `Ansible` code with Molecule.

This course is practical and assumes participants have basic `Linux` system administration skills.
It focuses on real-world automation scenarios rather than abstract concepts.

## Duration
16 hours / 2 days

## Intended Audience
* `DevOps` engineers looking to automate configuration management and provisioning.
* system administrators who want to manage infrastructure at scale.
* developers who want to automate deployment and environment setup.
* platform engineers building automation frameworks for their organizations.

## Prerequisites
* Basic `Linux` system administration skills (`file` system, services, packages).
* Familiarity with the command line and `SSH`.
* Basic understanding of `YAML` syntax.
* Experience with version control (`Git`).

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* understand the core concepts and principles of `Ansible` automation
* gain practical knowledge of playbooks, roles, and inventory management
* gain practical knowledge of `Ansible Galaxy`, AWX/Tower, and Molecule
* gain practical knowledge of idempotent automation patterns

## Outline
<!-- chapter: introduction-to-ansible, duration: 1h -->
* Introduction to `Ansible`
    * What is `Ansible` and why agentless matters
    * `Ansible` architecture and components
    * Comparing `Ansible` with other configuration management tools (`Puppet`, `Chef`, `SaltStack`)
    * Installing and configuring `Ansible`
    * `Ansible` control node and managed nodes
<!-- chapter: inventory-management, duration: 2h -->
* Inventory Management
    * Static inventory files
    * Inventory groups and group hierarchies
    * Host and group variables
    * Dynamic inventory
        * Cloud provider inventory plugins (`AWS`, `Azure`, `GCP`)
        * Custom inventory scripts
    * Inventory patterns and host selection
<!-- chapter: ad-hoc-commands, duration: 1h -->
* Ad-Hoc Commands
    * Running ad-hoc commands with `ansible`
    * Common ad-hoc use cases
    * Parallelism and forks
    * Privilege escalation with become
<!-- chapter: playbooks, duration: 2h -->
* Playbooks
    * Playbook structure and `YAML` syntax
    * Plays, tasks, and handlers
    * Task naming and documentation
    * Variables and facts
        * Variable precedence and scoping
        * Registered variables
        * `Ansible` facts and setup module
        * Custom facts
    * Conditionals with `when`
    * Loops and iteration
    * Tags for selective execution
    * Error handling (ignore_errors, block/rescue/always)
<!-- chapter: modules, duration: 2h -->
* Modules
    * Understanding `Ansible` modules
    * Core modules
        * Package management (`apt`, `yum`, `pip`)
        * `File` management (copy, template, `file`, lineinfile)
        * Service management (service, `systemd`)
        * User and group management
        * Command execution (command, shell, raw, script)
    * Cloud modules
    * Network modules
    * Writing custom modules
<!-- chapter: templates-and-jinja2, duration: 1h -->
* Templates and Jinja2
    * Jinja2 template syntax
    * Variables and filters in templates
    * Conditional logic in templates
    * Loops in templates
    * Template `file` management and best practices
<!-- chapter: idempotency, duration: 1h -->
* Idempotency
    * What idempotency means in practice
    * Designing idempotent tasks
    * Common idempotency pitfalls
    * Using changed_when and failed_when
    * `Check` mode and diff mode
<!-- chapter: roles, duration: 1h -->
* Roles
    * Role directory structure
    * Creating and using roles
    * Role dependencies
    * Role defaults and variables
    * Role distribution and reuse
    * Organizing projects with roles
<!-- chapter: ansible-galaxy, duration: 1h -->
* `Ansible Galaxy`
    * Browsing and installing roles from Galaxy
    * Collections vs roles
    * Installing and managing collections
    * Creating and publishing to Galaxy
    * Requirements files for dependency management
<!-- chapter: awx-ansible-tower, duration: 1h -->
* AWX / `Ansible Tower`
    * AWX and Tower overview and architecture
    * Installation and setup
    * Projects, inventories, and credentials
    * Job templates and workflows
    * Role-based access control
    * Scheduling and notifications
    * `API` access and integration
<!-- chapter: ansible-vault, duration: 1h -->
* `Ansible Vault`
    * Encrypting sensitive data
    * `Vault` passwords and password files
    * Encrypting files vs encrypting variables
    * `Vault` integration in playbooks and `CI/CD`
<!-- chapter: testing-with-molecule, duration: 1h -->
* Testing with Molecule
    * What is Molecule and why test `Ansible` code
    * Molecule scenarios and drivers
    * Testing with `Docker` containers
    * Writing verifier tests
    * Integrating Molecule into `CI/CD` pipelines
    * Linting with `ansible`-lint and yamllint
<!-- chapter: best-practices-and-patterns, duration: 1h -->
* Best Practices and Patterns
    * Directory layout and project organization
    * Naming conventions
    * Variable management strategies
    * Performance tuning (pipelining, `SSH` multiplexing, mitogen)
    * Security considerations
    * Scaling `Ansible` for large environments

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
