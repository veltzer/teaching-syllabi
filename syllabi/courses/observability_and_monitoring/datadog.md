---
tags:
  - tools:datadog
  - practices:observability
  - practices:monitoring
level: intermediate
category: observability
duration_hours: 16
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
  - audiences:sres
---
<!-- course: datadog -->
# `Datadog`

## Description
`Datadog` is a comprehensive cloud-based monitoring and analytics platform that provides full-stack observability for modern applications and infrastructure. This course covers the complete Datadog platform, from agent installation and infrastructure monitoring through APM, log management, synthetics, and Real User Monitoring. Students will learn how to build effective dashboards, set up alerting strategies, and leverage `Datadog` to gain deep visibility into their systems.

## Duration
16 hours / 2 days

## Intended Audience
* Software developers who need to monitor and observe their applications
* `DevOps` and SRE engineers building monitoring infrastructure
* System administrators responsible for infrastructure health
* Platform engineers evaluating or adopting `Datadog`

## Prerequisites
* Basic understanding of `Linux` command line
* Familiarity with web applications and distributed systems
* Basic knowledge of monitoring concepts (metrics, logs, traces)
* Experience with `Docker` or `Kubernetes` is helpful but not required

## Required Knowledge
* `Docker` Fundamentals (or equivalent experience)
* Introduction to `Kubernetes` (or equivalent experience)
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Install and configure the `Datadog Agent` across different environments
* Monitor infrastructure health including hosts, containers, and cloud services
* Implement APM and distributed tracing for application performance visibility
* Set up log collection, parsing, and analysis pipelines
* Build meaningful dashboards and configure effective alerting strategies
* Use synthetics and RUM for end-user experience monitoring
* Manage `Datadog` costs through tagging strategies and usage optimization

## Outline
<!-- chapter: datadog-overview, duration: 1h -->
* `Datadog` Overview
    * What is `Datadog` and the observability landscape
    * `Datadog` platform architecture
    * Core products: infrastructure monitoring, APM, logs, synthetics, RUM
    * Navigating the `Datadog` web interface
    * Organizations, teams, and role-based access control
<!-- chapter: datadog-agent, duration: 1h -->
* `Datadog Agent`
    * Agent architecture and components
    * Installation on `Linux`, `Windows`, and `macOS`
    * `Docker` and `Kubernetes` deployment
    * Agent configuration and `datadog`.`yaml`
    * Agent checks and custom checks
    * Agent troubleshooting and status commands
    * Cluster Agent for `Kubernetes`
<!-- chapter: infrastructure-monitoring, duration: 1h -->
* Infrastructure Monitoring
    * Host maps and infrastructure overview
    * System metrics: `CPU`, memory, disk, network
    * Process monitoring
    * Container monitoring (`Docker`, `Kubernetes`)
    * Cloud integrations (`AWS`, `Azure`, `GCP`)
    * Network Performance Monitoring
    * Live processes and containers
<!-- chapter: metrics, duration: 1h -->
* Metrics
    * Metric types: count, rate, gauge, histogram, distribution
    * Custom metrics with DogStatsD
    * Metric submission via the `Datadog` `API`
    * Metric metadata and units
    * Metric queries and functions
    * Metric aggregation and rollups
    * Managing custom metric volumes
<!-- chapter: apm-and-distributed-tracing, duration: 2h -->
* APM and Distributed Tracing
    * APM architecture and concepts
    * Instrumenting applications (`Python`, `Java`, Go, `Node.js`, `.NET`)
    * Automatic vs manual instrumentation
    * Service maps and service catalog
    * Trace search and analytics
    * Continuous profiler
    * Error tracking
    * Connecting traces with logs and infrastructure metrics
<!-- chapter: log-management, duration: 2h -->
* Log Management
    * Log collection and agent configuration
    * Log sources: files, `Docker`, `Kubernetes`, cloud services
    * Log processing pipelines
    * Parsing rules: Grok, `JSON`, and custom parsers
    * Log indexes and retention policies
    * Log analytics and patterns
    * Log archives and rehydration
    * Connecting logs with traces
<!-- chapter: dashboards-and-widgets, duration: 1h -->
* Dashboards and Widgets
    * Dashboard types: timeboards and screenboards
    * Widget types: timeseries, top list, heatmap, distribution, query value
    * Template variables and dynamic dashboards
    * Dashboard sharing and permissions
    * Embedding dashboards
    * Out-of-the-box dashboards for integrations
<!-- chapter: alerting-and-slos, duration: 2h -->
* Alerting and SLOs
    * Monitor types: metric, log, APM, composite, anomaly, forecast
    * Monitor configuration: thresholds, notifications, recovery
    * Downtime scheduling and maintenance `windows`
    * Service Level Objectives (SLOs)
    * SLO alerts and error budgets
    * Notification channels: email, Slack, `PagerDuty`, webhooks
    * Alert fatigue reduction and best practices
<!-- chapter: synthetics, duration: 1h -->
* Synthetics
    * `API` tests: `HTTP`, `SSL`, `DNS`, `TCP`, `gRPC`
    * Multistep `API` tests
    * Browser tests: recording and playback
    * Private locations for internal service testing
    * `CI/CD` integration for synthetic tests
    * Monitoring global performance and availability
<!-- chapter: real-user-monitoring-rum, duration: 1h -->
* Real User Monitoring (RUM)
    * RUM `SDK` setup for web and mobile applications
    * Session replay
    * User actions, views, and errors tracking
    * Performance metrics: Core Web Vitals
    * RUM and session analytics
    * Connecting RUM with traces and logs
<!-- chapter: security-monitoring, duration: 1h -->
* Security Monitoring
    * Cloud Security Posture Management (CSPM)
    * Cloud Workload Security
    * Application Security Monitoring (ASM)
    * Threat detection rules
    * Security signals and investigation
<!-- chapter: integrations-and-api, duration: 1h -->
* Integrations and `API`
    * Built-in integrations overview
    * `Datadog` `REST API`
    * `Terraform` provider for `Datadog`
    * Webhooks and event-driven automation
<!-- chapter: tagging-strategy-and-cost-management, duration: 1h -->
* Tagging Strategy and Cost Management
    * Tagging best practices and conventions
    * Unified service tagging
    * Reserved tags and auto-discovered tags
    * Understanding `Datadog` pricing model
    * Estimating and controlling costs
    * Usage attribution and chargeback

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
