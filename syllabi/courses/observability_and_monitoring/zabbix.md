---
tags:
  - tools:zabbix
  - observability:monitoring
  - observability:alerting
  - infrastructure:enterprise
level: intermediate
category: observability
duration_hours: 24
audience:
  - audiences:sysadmins
  - audiences:devops
  - audiences:network-engineers
---
<!-- course: zabbix -->
# `Zabbix` Enterprise Monitoring

## Description
`Zabbix` is a mature, open-source enterprise monitoring platform capable of monitoring the availability and performance of IT infrastructure components including servers, networks, applications, cloud resources, and services. Unlike lightweight cloud-native monitoring tools, `Zabbix` provides an all-in-one solution covering data collection, storage, visualization, alerting, and automation from a single platform with no per-host licensing costs. This course provides comprehensive training on deploying and operating `Zabbix` in enterprise environments, covering everything from basic host and item configuration to advanced topics such as `SNMP` integration, distributed monitoring with proxies, and automation through the `Zabbix` `API`. Participants will leave with the skills to design and maintain production-grade monitoring for complex heterogeneous infrastructures.

## Duration
24 hours / 3 days

## Intended Audience
* System administrators responsible for monitoring on-premise and cloud infrastructure across multiple platforms and operating systems.
* `DevOps` engineers integrating `Zabbix` into `CI/CD` pipelines and automating infrastructure monitoring.
* Network engineers who need to monitor network devices, switches, routers, and firewalls using `SNMP` and `IPMI`.

## Prerequisites
* `Solid` `Linux` system administration skills, including service management and networking commands.
* Basic understanding of networking concepts: `IP`, `SNMP`, `ICMP`, `TCP/UDP`.
* Familiarity with relational databases (`MySQL` or `PostgreSQL`) at a basic administrative level.
* Experience with `JSON` or scripting (`Bash`, `Python`) is helpful for automation topics.

## Required Knowledge
* `Linux` System Administration (or equivalent experience)
* Networking fundamentals

## Objectives
* Understand `Zabbix` architecture and deploy it in a production-ready configuration
* Configure hosts, templates, and items to collect data from diverse infrastructure components
* Build intelligent triggers and actions to detect and respond to problems automatically
* Set up flexible notification and escalation policies for alerting
* Monitor network infrastructure using `SNMP` and `IPMI`
* Deploy and manage `Zabbix` agents including active `check` configurations
* Design informative dashboards and generate scheduled reports
* Implement distributed monitoring using `Zabbix` proxies for remote locations
* Automate `Zabbix` configuration and integrate with external systems using the `API`

## Outline
<!-- chapter: introduction-to-zabbix, duration: 2h -->
* Introduction to `Zabbix`
    * Enterprise monitoring challenges and requirements
    * `Zabbix` features, capabilities, and supported platforms
    * `Zabbix` vs other monitoring solutions: `Nagios`, `Prometheus`, `Datadog`
    * Core concepts: hosts, items, triggers, actions, and media types
    * `Zabbix` licensing model and community resources
    * Overview of the `Zabbix` web interface
<!-- chapter: installation-and-architecture, duration: 2h -->
* Installation and Architecture
    * `Zabbix` server, database, frontend, and agent components
    * Installing `Zabbix` server on `RHEL`/`Debian` with `MySQL`/`PostgreSQL`
    * `Docker` and `Docker Compose` deployment
    * `Zabbix` frontend setup with `Nginx` and `Apache`
    * Initial configuration wizard and first login
    * `Zabbix` server configuration `file`: key parameters
    * Database maintenance and housekeeping settings
<!-- chapter: hosts-templates-and-items, duration: 3h -->
* Hosts, Templates and Items
    * Creating and organizing hosts and host groups
    * Host interfaces: `Zabbix` agent, `SNMP`, `IPMI`, `JMX`
    * Item types: agent, simple `check`, internal, external, calculated, dependent
    * Key syntax and item configuration parameters
    * User macros and global macros for reusable configuration
    * Templates: structure, linking, and inheritance
    * Low-level discovery rules and item prototypes
    * Managing templates with versioning and import/export
<!-- chapter: triggers-and-actions, duration: 3h -->
* Triggers and Actions
    * Trigger expression syntax and functions
    * Trigger severity levels and dependency configuration
    * Hysteresis: problem and recovery expressions
    * Event correlation to suppress noise and reduce alert storms
    * Actions: operations, recovery operations, and update operations
    * Action conditions and filters
    * Remote command execution via actions
    * Event acknowledgement and manual problem closing
<!-- chapter: notifications-and-alerting, duration: 2h -->
* Notifications and Alerting
    * Media types: email, `SMS`, `Slack`, `PagerDuty`, webhooks
    * User groups and permission-based notification routing
    * Escalation policies: time-based and severity-based escalation
    * Maintenance `windows` to suppress alerts during planned downtime
    * Custom notification message templates
    * Testing and debugging notification delivery
<!-- chapter: network-monitoring, duration: 2h -->
* Network Monitoring
    * Monitoring network availability with `ICMP` checks
    * `TCP` port checks and service availability items
    * Network discovery and auto-registration of hosts
    * Bandwidth and interface utilization monitoring
    * Monitoring `DNS`, `HTTP`, `FTP`, and other services
    * Web scenario monitoring for multi-step `HTTP` transactions
<!-- chapter: snmp-and-ipmi-integration, duration: 2h -->
* `SNMP` and `IPMI` Integration
    * `SNMP` protocol fundamentals: OIDs, MIBs, versions v1/v2c/v3
    * Configuring `SNMP` items in `Zabbix`
    * Importing and using vendor MIB files
    * `SNMP` traps: receiving and processing trap data
    * `IPMI` monitoring for physical server hardware sensors
    * Configuring `IPMI` interface and item discovery
    * Templates for common network vendors: Cisco, Juniper, HP
<!-- chapter: zabbix-agent-and-active-checks, duration: 2h -->
* `Zabbix` Agent and Active Checks
    * Passive vs active agent `check` modes
    * Installing and configuring `Zabbix` agent v2
    * Agent configuration: server, listen port, host metadata
    * Custom user parameters and external scripts
    * Active checks and the active agent proxy buffer
    * `Zabbix` agent on `Windows`: service installation and configuration
    * Monitoring `Docker` containers with the `Zabbix` agent
<!-- chapter: dashboards-and-reports, duration: 2h -->
* Dashboards and Reports
    * Building custom dashboards with widgets: graphs, maps, tables, clocks
    * Dynamic dashboards using host groups and template variables
    * Network maps and topology visualization
    * Screens (classic view) and slide shows
    * Scheduled `PDF` report generation
    * Audit log and event log review
<!-- chapter: distributed-monitoring-and-proxies, duration: 2h -->
* Distributed Monitoring and Proxies
    * `When` to use `Zabbix` proxies: remote locations, firewalls, scale
    * Active vs passive proxy modes
    * Installing and configuring a `Zabbix` proxy
    * Assigning hosts to proxies
    * Proxy performance monitoring and troubleshooting
    * High-availability `Zabbix` server configuration
<!-- chapter: api-and-automation, duration: 2h -->
* `API` and Automation
    * `Zabbix` `API` overview: `JSON-RPC` protocol
    * Authentication and session management
    * Creating and updating hosts, items, and triggers via `API`
    * Bulk import and export with `XML`/`JSON`
    * Infrastructure-as-code with `Terraform` `Zabbix` provider
    * Integration with `Ansible` for automated host registration
    * Sending custom data with `zabbix_sender`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
