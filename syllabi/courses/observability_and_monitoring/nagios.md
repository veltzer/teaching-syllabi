---
tags:
  - practices:monitoring
  - practices:observability
  - practices:sre
level: intermediate
category: observability
duration_hours: 8
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
  - audiences:sres
---
<!-- course: nagios -->
# `Nagios` Monitoring

## Description
`Nagios` is one of the most widely adopted open source monitoring systems,
providing comprehensive infrastructure monitoring through host and service checks,
alerting, and performance data collection. This course covers the core concepts
of `Nagios` monitoring, from basic installation and configuration through advanced
topics such as distributed monitoring and event handlers. Participants will learn
how to build a robust monitoring solution using `Nagios` that provides full
visibility into their infrastructure.

## Duration
8 hours / 1 day

## Intended Audience
* Developers who need to integrate monitoring into their applications and infrastructure.
* System administrators responsible for maintaining and monitoring servers and services.
* `DevOps` engineers who need to implement monitoring as part of their `CI/CD` and infrastructure pipelines.
* Site reliability engineers building observability into production systems.

## Prerequisites
* Basic `Linux` system administration skills.
* Familiarity with networking concepts such as `TCP`/`IP`, `DNS`, and `HTTP`.
* Experience with command-line tools and shell scripting.

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Understand the `Nagios` architecture and core monitoring concepts.
* Configure host and service checks for infrastructure monitoring.
* Write and deploy custom `Nagios` plugins.
* Set up notifications, escalations, and event handlers.
* Implement distributed monitoring for large-scale environments.
* Collect and visualize performance data using `Nagios` dashboards.

## Outline
<!-- chapter: introduction-to-nagios, duration: 1h -->
* Introduction to `Nagios`
    * Overview of monitoring and observability
    * `Nagios` architecture and components
    * Installation and initial configuration
    * Web interface overview
<!-- chapter: host-and-service-checks, duration: 1h -->
* Host and Service Checks
    * Defining hosts and host groups
    * Configuring service checks
    * `Check` intervals, retry logic, and scheduling
    * Synthetic monitoring with active checks
    * Passive checks and external commands
<!-- chapter: nagios-plugins, duration: 1h -->
* `Nagios` Plugins
    * Standard plugin library
    * Writing custom plugins
    * Plugin return codes and output format
    * Threshold configuration and best practices
<!-- chapter: nrpe-nagios-remote-plugin-executor, duration: 1h -->
* NRPE (`Nagios` Remote Plugin Executor)
    * NRPE architecture and communication
    * Installing and configuring NRPE on remote hosts
    * Securing NRPE connections
    * Running remote checks through NRPE
<!-- chapter: notifications-and-escalations, duration: 1h -->
* Notifications and Escalations
    * Contact and contact group configuration
    * Notification commands and methods (email, SMS, webhooks)
    * Notification periods and filtering
    * Escalation policies and chains
    * Alert fatigue management
<!-- chapter: dashboards-and-performance-data, duration: 1h -->
* Dashboards and Performance Data
    * `Nagios` web interface customization
    * Performance data collection and processing
    * Integrating with graphing tools (PNP4Nagios, `Grafana`)
    * Status maps and tactical overviews
<!-- chapter: event-handlers, duration: 1h -->
* Event Handlers
    * Event handler concepts and use cases
    * Writing event handler scripts
    * Auto-remediation patterns
    * State types and handler triggers
<!-- chapter: distributed-monitoring, duration: 1h -->
* Distributed Monitoring
    * Distributed monitoring architecture
    * Parent-child host relationships
    * NSCA and passive check forwarding
    * Scaling `Nagios` for large environments
    * High availability considerations

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
