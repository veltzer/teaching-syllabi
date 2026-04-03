---
tags:
  - tools:loki
  - practices:observability
  - practices:log-management
  - tools:grafana
  - tools:prometheus
level: intermediate
category: observability
duration_hours: 16
audience:
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: loki -->
# `Grafana Loki`: Log Aggregation System

## Description
This course covers `Grafana Loki`, a horizontally scalable, highly available log aggregation system inspired by `Prometheus`. Participants will learn the Loki architecture, LogQL query language, label design best practices, log collection, storage configuration, alerting, and integration with `Grafana`. The course emphasizes practical skills for deploying and operating Loki in production environments.

## Duration
16 hours / 1 day

## Intended Audience
* `DevOps` engineers building centralized logging infrastructure
* System administrators managing log collection and analysis
* Platform engineers evaluating lightweight alternatives to `Elasticsearch` for logs

## Prerequisites
* Basic understanding of logging concepts and log formats.
* Familiarity with `Linux` command line.
* Experience with `Grafana` is helpful.
* Basic knowledge of `Prometheus` concepts (labels, selectors) is beneficial.

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)
* `Prometheus` and `Grafana` (or equivalent experience)
* `Grafana` Basics (or equivalent experience)

## Objectives
* Understand the Loki architecture and its components.
* Write LogQL queries for log filtering, parsing, and metric extraction.
* Design effective label strategies for log streams.
* Set up log collection with Promtail and `Grafana Agent`.
* Configure storage backends and retention policies.
* Create alerts based on log data using Loki ruler.
* Integrate Loki with `Grafana` for log exploration and correlation.

## Outline
<!-- chapter: introduction-to-loki, duration: 1h -->
* Introduction to Loki:
    * What is Loki and its design philosophy
    * Loki vs `Elasticsearch` for log management
    * Index-free approach and label-based design
    * Use cases and deployment scenarios
<!-- chapter: loki-architecture, duration: 2h -->
* Loki Architecture:
    * Ingester component
    * Querier component
    * Compactor component
    * Index gateway
    * Read and write paths
    * Ring-based distribution
<!-- chapter: deployment-modes, duration: 1h -->
* Deployment Modes:
    * Monolithic mode
    * Simple scalable mode
    * `Microservices` mode
    * Choosing the right deployment mode
<!-- chapter: logql-query-language, duration: 1h -->
* LogQL Query Language:
    * Stream selectors
    * Filter expressions (line filter, label filter)
    * Parser expressions (`json`, logfmt, regexp, pattern)
    * Line format expressions
    * Label format expressions
<!-- chapter: logql-metric-queries, duration: 1h -->
* LogQL Metric Queries:
    * Log range aggregations (rate, count_over_time, bytes_over_time)
    * Unwrapped range aggregations
    * Aggregation operators (sum, avg, min, max, topk)
    * Built-in functions
<!-- chapter: label-design-best-practices, duration: 1h -->
* Label Design Best Practices:
    * Choosing labels wisely
    * Cardinality considerations
    * Static vs dynamic labels
    * Common labeling patterns
<!-- chapter: log-collection, duration: 2h -->
* Log Collection:
    * Promtail configuration and pipeline stages
    * `Grafana Agent` for log collection
    * `Fluent Bit` and `Fluentd` output plugins
    * `Docker` and `Kubernetes` log collection
    * Relabeling and processing pipelines
<!-- chapter: storage-backends, duration: 2h -->
* Storage Backends:
    * Filesystem storage
    * `S3`-compatible object storage
    * `GCS` storage
    * Storage schema and index configuration
    * Chunk encoding and compression
<!-- chapter: retention-policies, duration: 1h -->
* Retention Policies:
    * Global retention configuration
    * Per-tenant retention
    * Compactor-based retention
    * Storage cleanup and management
<!-- chapter: alerting-with-loki-ruler, duration: 1h -->
* Alerting with Loki Ruler:
    * Configuring the ruler component
    * Writing alerting rules with LogQL
    * Recording rules
    * Integration with Alertmanager
<!-- chapter: grafana-integration, duration: 1h -->
* `Grafana` Integration:
    * Configuring Loki as a data source in `Grafana`
    * Log exploration with the Explore view
    * Correlating logs with metrics and traces
    * Building log dashboards
<!-- chapter: multi-tenancy, duration: 1h -->
* Multi-Tenancy:
    * Tenant configuration
    * Per-tenant limits and overrides
    * Authentication and authorization
<!-- chapter: performance-tuning, duration: 1h -->
* Performance Tuning:
    * Query performance optimization
    * Ingestion rate limits
    * Caching strategies
    * Resource sizing and capacity planning

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
