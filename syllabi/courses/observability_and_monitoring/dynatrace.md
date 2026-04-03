---
tags:
  - tools:dynatrace
  - observability:apm
  - observability:monitoring
  - observability:aiops
level: intermediate
category: observability
duration_hours: 24
audience:
  - audiences:devops
  - audiences:sres
  - audiences:developers
---
<!-- course: dynatrace -->
# `Dynatrace`

## Description
`Dynatrace` is an `AI`-powered, full-stack observability and application performance management platform that provides automatic and intelligent monitoring across cloud-native, on-premise, and hybrid environments. By deploying a single `OneAgent`, organizations gain end-to-end visibility into applications, infrastructure, user experience, and business metrics without manual instrumentation or configuration effort. This course provides comprehensive coverage of the `Dynatrace` platform, from initial deployment to advanced use cases including `AI`-assisted anomaly detection with `Davis AI`, synthetic monitoring, log analytics, and `Kubernetes` observability with `DynaKube`. Participants will develop the skills to operate `Dynatrace` as an enterprise observability platform and leverage its automation and intelligence features to reduce mean time to resolution.

## Duration
24 hours / 3 days

## Intended Audience
* `DevOps` engineers and SREs responsible for production reliability who need a comprehensive, low-friction observability solution.
* Application developers seeking deep performance insights, code-level visibility, and fast diagnosis of regressions.
* Platform and cloud infrastructure teams managing `Kubernetes`, cloud services, and hybrid deployments at scale.

## Prerequisites
* Experience with cloud-native concepts: `Kubernetes`, containers, `microservices`.
* Familiarity with application performance concepts: response time, throughput, error rates.
* Basic understanding of `HTTP`, databases, and distributed architectures.
* Exposure to `Prometheus`, `Grafana`, or similar observability tools is helpful but not required.

## Required Knowledge
* `Kubernetes` fundamentals (or equivalent experience)
* Cloud infrastructure basics

## Objectives
* Navigate the `Dynatrace` platform and understand its core observability capabilities
* Deploy `OneAgent` across hosts, containers, and `Kubernetes` clusters
* Understand `Smartscape` topology and the automatic service dependency mapping
* Monitor application services, transactions, and code-level performance
* Analyze infrastructure metrics for hosts, cloud services, and network performance
* Use `Log Management and Analytics` to search, parse, and correlate log data
* Create synthetic monitors to proactively test user journeys and `API` availability
* Leverage `Davis AI` for automatic root cause analysis and anomaly detection
* Build `Dynatrace` dashboards and SLO monitoring for business and technical metrics
* Automate `Dynatrace` configuration and integrate with external tools via `API`
* Monitor `Kubernetes` clusters with `DynaKube` and cloud-native observability

## Outline
<!-- chapter: introduction-to-dynatrace, duration: 2h -->
* Introduction to `Dynatrace`
    * The evolution from APM to full-stack observability
    * `Dynatrace` platform architecture: `OneAgent`, `ActiveGate`, and `Dynatrace` `SaaS`/Managed
    * Core pillars: infrastructure, application, user experience, and business observability
    * `Dynatrace` vs `Datadog`, `New Relic`, and open-source alternatives
    * Licensing model: DDUs and consumption-based pricing
    * Navigating the `Dynatrace` UI: menus, entities, and search
<!-- chapter: oneagent-deployment, duration: 2h -->
* `OneAgent` Deployment
    * How `OneAgent` works: code injection and auto-discovery
    * Installing `OneAgent` on `Linux` and `Windows` hosts
    * `OneAgent` deployment on `Docker` and container runtimes
    * `Kubernetes` deployment via `DynaKube` Operator
    * `ActiveGate` for data routing, `Kubernetes` `API` monitoring, and remote plugins
    * `OneAgent` update strategies: automatic, manual, and rollback
    * Troubleshooting `OneAgent` connectivity and data reporting
<!-- chapter: smartscape-and-topology, duration: 2h -->
* `Smartscape` and Topology
    * `Smartscape` real-time dependency mapping
    * Entity types: processes, services, hosts, applications, databases
    * How `Dynatrace` automatically discovers service relationships
    * Filtering and navigating `Smartscape` for large environments
    * Using topology data for impact analysis and root cause identification
    * Tags, metadata, and management zones for entity organization
    * Host groups and environment segregation
<!-- chapter: application-and-service-monitoring, duration: 3h -->
* Application and Service Monitoring
    * Service detection and naming rules
    * Distributed traces: PurePaths and code-level visibility
    * Database calls, external service calls, and messaging system monitoring
    * Transaction and service flow analysis
    * Failure detection: error rate thresholds and anomaly detection baselines
    * Request attributes and custom properties extraction
    * Calculated service metrics for custom KPIs
    * Real User Monitoring (RUM): web and mobile application instrumentation
    * Session replay and user behavior analytics
<!-- chapter: infrastructure-monitoring, duration: 2h -->
* Infrastructure Monitoring
    * Host monitoring: `CPU`, memory, disk, and network metrics
    * Process and process group monitoring
    * Cloud integrations: `AWS`, `Azure`, `GCP` service metrics
    * `VMware` and virtual infrastructure monitoring
    * Network monitoring and traffic visibility
    * Custom metrics ingestion via `StatsD`, `Prometheus`, and `API`
    * Infrastructure alerting and baseline anomaly detection
<!-- chapter: log-management-and-analytics, duration: 2h -->
* Log Management and Analytics
    * Log ingest sources: `OneAgent`, `Fluentd`, `Logstash`, and `API`
    * Log Viewer and log search syntax
    * Log processing pipelines: parsing, masking, and enrichment
    * Attribute extraction from unstructured log data
    * Correlating logs with traces and infrastructure metrics
    * Log metrics and log-based alerting
    * Log retention, archiving, and compliance considerations
<!-- chapter: synthetic-monitoring, duration: 2h -->
* Synthetic Monitoring
    * Browser monitors: scripted single-URL and multi-step monitors
    * `HTTP` monitors for `API` and backend health checks
    * Private Synthetic Locations with `ActiveGate`
    * Monitor scheduling, geographic distribution, and frequency settings
    * Availability SLOs and synthetic-based alerting
    * Performance waterfall analysis for synthetic results
    * Integrating synthetic monitors with deployment pipelines
<!-- chapter: davis-ai-and-anomaly-detection, duration: 3h -->
* `Davis AI` and Anomaly Detection
    * How `Davis AI` builds automatic baselines for every metric
    * Problem detection: anomaly scoring and causal `AI`
    * Problem cards: root cause, impact, and affected entities
    * `Davis AI` evidence chain and `AI` reasoning transparency
    * Configuring anomaly detection sensitivity and thresholds
    * Alerting profiles and notification routing for problems
    * Integrating `Davis` problem alerts with `PagerDuty`, `Jira`, and `ServiceNow`
    * Auto-remediation workflows with `Dynatrace` Workflows and webhooks
<!-- chapter: business-analytics, duration: 2h -->
* Business Analytics
    * Defining and tracking SLOs in `Dynatrace`
    * Business events and conversion funnel analysis
    * Custom dashboards for business KPIs and technical metrics
    * Reports and scheduled delivery
    * Data Explorer for ad-hoc metric queries
    * `Dynatrace Query Language` (DQL) fundamentals
    * Notebooks for collaborative analysis and incident documentation
<!-- chapter: api-and-automation, duration: 2h -->
* `API` and Automation
    * `Dynatrace` `API` v1 and v2 overview
    * Authentication: `API` tokens and `OAuth2` client credentials
    * Querying entities, metrics, events, and problems via `API`
    * Automating configuration with `Terraform` `Dynatrace` provider
    * `Dynatrace` as Code (Monaco) for `GitOps`-based configuration management
    * Integrating `Dynatrace` into `CI/CD` pipelines for quality gates
    * Webhooks and outbound event notifications
<!-- chapter: dynakube-kubernetes-monitoring, duration: 2h -->
* `DynaKube`: `Kubernetes` Monitoring
    * `DynaKube` Operator architecture and custom resources
    * Full-stack `Kubernetes` monitoring: cluster, node, pod, and container
    * Automatic workload and service discovery in `Kubernetes`
    * `Kubernetes` events, logs, and resource utilization dashboards
    * Namespace-level observability and multi-cluster management
    * `OpenTelemetry` integration with `Dynatrace` for custom telemetry
    * `Istio` and service mesh observability

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
