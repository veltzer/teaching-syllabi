---
tags:
  - tools:saltstack
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
<!-- course: saltstack -->
# `SaltStack`

## Description
`SaltStack` (now `Salt Project`) is a high-speed, scalable infrastructure automation and
configuration management platform built around a remote execution engine. This course covers
the full breadth of the `Salt` ecosystem, from the master-minion architecture and state
management through advanced topics such as orchestration, event-driven automation, and
agentless execution with `Salt SSH`. Participants will learn how to express infrastructure
intent with `SLS` state files, separate data from logic using grains and pillars, and build
reactive infrastructure with the events and reactors system. The course concludes with
practical coverage of `Salt Cloud` for provisioning virtual machines across cloud providers.

## Duration
24 hours / 3 days

## Intended Audience
* `DevOps` engineers who need to automate configuration management across large fleets.
* System administrators looking to replace manual operations with repeatable automation.
* Platform engineers evaluating configuration management tools for their organization.

## Prerequisites
* `Solid` `Linux` system administration skills (packages, services, networking).
* Familiarity with the command line and `SSH`.
* Basic understanding of `YAML` and `Jinja2` templating.
* Experience with version control (`Git`).

## Objectives
* Understand the `Salt` master-minion architecture and communication model.
* Write `SLS` state files that configure systems idempotently.
* Use grains and pillars to separate node data from configuration logic.
* Build orchestrated workflows using `Salt Orchestrate`.
* Implement event-driven automation with the reactor system.
* Manage agentless targets with `Salt SSH` and provision cloud resources with `Salt Cloud`.

## Outline
<!-- chapter: introduction-to-saltstack, duration: 2h -->
* Introduction to `SaltStack`
    * What is `SaltStack` and where it fits in the `DevOps` landscape
    * Comparing `Salt` with `Ansible`, `Chef`, and `Puppet`
    * Core concepts: masters, minions, execution modules, states, pillars
    * The `Salt` communication model: `ZeroMQ` and `RAET` transports

<!-- chapter: architecture-master-and-minions, duration: 2h -->
* Architecture — Master and Minions
    * `Salt` master configuration and tuning
    * Minion authentication and key management
    * The targeting system: glob, grain, compound, and nodegroup targets
    * Masterless `Salt` (`salt`-call) for local execution

<!-- chapter: installation-and-bootstrap, duration: 2h -->
* Installation and `Bootstrap`
    * Installing the `Salt` master and minion packages
    * Using the `bootstrap` script for rapid deployment
    * Configuring `firewall` rules and accepted minion keys
    * Verifying connectivity with `test.ping`

<!-- chapter: states-and-sls-files, duration: 2h -->
* States and `SLS` Files
    * State `file` syntax and `YAML`/`Jinja2` rendering
    * Core state modules: `pkg`, `service`, `file`, `user`, `cmd`
    * State ordering with `require`, `watch`, and `onchanges`
    * The `top.sls` `file` and environment targeting
    * Highstate execution and idempotent convergence

<!-- chapter: grains-and-pillars, duration: 2h -->
* Grains and Pillars
    * Built-in grains and custom grain definitions
    * Using grains for dynamic targeting and templating
    * Pillar data: structure, `top` `file`, and environment separation
    * Encrypting sensitive pillar data with `GPG`

<!-- chapter: execution-modules-and-functions, duration: 2h -->
* Execution Modules and Functions
    * Running remote commands with `salt '*' module.function`
    * Commonly used modules: `cmd`, `network`, `disk`, `process`, `git`
    * Returning data with returners (`MySQL`, `Redis`, `Elasticsearch`)
    * Writing custom execution modules in `Python`

<!-- chapter: targeting-and-matching, duration: 2h -->
* Targeting and Matching
    * Glob and PCRE targeting
    * Grain-based and pillar-based targeting
    * Compound matching syntax
    * Nodegroups and batch execution for rolling updates

<!-- chapter: orchestration-with-salt-orchestrate, duration: 2h -->
* Orchestration with `Salt Orchestrate`
    * Differences between highstate and orchestrate
    * Writing orchestrate `SLS` files
    * Chaining states across multiple minions
    * Handling failures and conditional execution in orchestrate

<!-- chapter: events-and-reactors, duration: 2h -->
* Events and Reactors
    * The `Salt` event bus and event tags
    * Listening to events with `salt-run state.event`
    * Writing reactor `SLS` files to respond to events
    * Beacons: monitoring system state and firing events

<!-- chapter: salt-ssh-and-agentless-mode, duration: 2h -->
* `Salt SSH` and Agentless Mode
    * `When` to use `Salt SSH` vs. the minion-based approach
    * Configuring the roster `file`
    * Running states and execution modules over `SSH`
    * Limitations and performance considerations

<!-- chapter: testing-and-troubleshooting, duration: 2h -->
* Testing and Troubleshooting
    * `salt-call` for local state testing and debugging
    * Verbose and debug logging modes
    * Using `test=True` for dry-run state execution
    * Common errors: key mismatches, pillar rendering failures, targeting issues

<!-- chapter: salt-cloud, duration: 2h -->
* `Salt Cloud`
    * `Salt Cloud` architecture and provider drivers
    * Configuring cloud providers: `AWS`, `GCP`, `Azure`
    * Defining cloud profiles and maps
    * Bootstrapping and managing cloud instances end-to-end

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
