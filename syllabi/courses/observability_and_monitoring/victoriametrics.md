---
tags:
  - tools:victoriametrics
  - observability:metrics
  - observability:monitoring
  - concepts:prometheus-compatible
level: intermediate
category: observability
duration_hours: 16
audience:
  - audiences:devops
  - audiences:sres
  - audiences:sysadmins
---
<!-- course: victoriametrics -->
# `VictoriaMetrics`

## Description
`VictoriaMetrics` is a high-performance, cost-efficient, and scalable time-series database that serves as a long-term storage and query engine for `Prometheus`-compatible metrics. Purpose-built for high-cardinality workloads, `VictoriaMetrics` delivers significantly better resource utilization than `Prometheus` alone, making it suitable for large-scale production environments. This course covers the full lifecycle of operating `VictoriaMetrics`, from installation and data ingestion to advanced querying with `MetricsQL`, cluster deployments, and integration with `Grafana`. Participants will gain the knowledge to migrate from `Prometheus` to `VictoriaMetrics` and to build robust, scalable metrics pipelines.

## Duration
16 hours / 2 days

## Intended Audience
* `DevOps` engineers and SREs managing large-scale monitoring infrastructure who need an efficient alternative or complement to `Prometheus`.
* System administrators responsible for metrics collection and retention across cloud, on-premise, or hybrid environments.
* Platform engineers evaluating time-series databases for high-cardinality and long-retention use cases.

## Prerequisites
* Working knowledge of `Prometheus`, including scrape configuration, PromQL queries, and alerting rules.
* Familiarity with `Docker` and basic `Linux` administration.
* Understanding of time-series data concepts and metrics collection patterns.
* Experience with `Grafana` for dashboard creation is helpful.

## Required Knowledge
* `Prometheus` fundamentals (or equivalent experience)
* `Linux` command-line proficiency

## Objectives
* Understand the `VictoriaMetrics` architecture and its advantages over `Prometheus`
* Install and configure single-node and cluster deployments of `VictoriaMetrics`
* Ingest metrics from `Prometheus`, `Telegraf`, `InfluxDB`, and other sources
* Write efficient queries using the `MetricsQL` query language
* Configure data retention policies and manage storage efficiently
* Deploy and operate `VictoriaMetrics` cluster for horizontal scalability
* Set up alerting and recording rules with `VMAlert`
* Build `Grafana` dashboards backed by `VictoriaMetrics`

## Outline
<!-- chapter: introduction-to-victoriametrics, duration: 1h -->
* Introduction to `VictoriaMetrics`
    * Limitations of `Prometheus` at scale
    * What `VictoriaMetrics` offers: performance, compression, and compatibility
    * Single-node vs cluster architecture overview
    * `VictoriaMetrics` ecosystem: `VMAgent`, `VMAlert`, `VMAuth`, `VMOperator`
    * Comparison with Thanos, Cortex, and Mimir
    * Use cases and deployment scenarios
<!-- chapter: architecture-and-storage-engine, duration: 2h -->
* Architecture and Storage Engine
    * `VictoriaMetrics` storage internals: `MergeTree` and compression
    * Data model: metrics, labels, and timestamps
    * How `VictoriaMetrics` achieves high compression ratios
    * Index structure and label cardinality management
    * Memory and disk layout
    * Single-node component overview
    * Cluster components: `vminsert`, `vmstorage`, `vmselect`
    * Data replication and consistency guarantees
<!-- chapter: installation-and-configuration, duration: 1h -->
* Installation and Configuration
    * Installing single-node `VictoriaMetrics` from binary and `Docker`
    * Key configuration flags: retention, memory limits, storage path
    * Deploying with `Docker Compose` for local environments
    * `Kubernetes` deployment with `VMOperator`
    * Security: `TLS` configuration and basic authentication
    * Monitoring `VictoriaMetrics` itself with built-in metrics
<!-- chapter: data-ingestion, duration: 2h -->
* Data Ingestion: `Prometheus` and Others
    * Configuring `Prometheus` remote write to `VictoriaMetrics`
    * Using `VMAgent` as a lightweight `Prometheus` scrape agent
    * Ingesting data via `InfluxDB` line protocol
    * `OpenTSDB` and Graphite protocol support
    * Ingesting data via the `Prometheus` exposition format
    * Backfilling historical data with `vmctl`
    * High-availability ingestion patterns
    * Deduplication and multi-replica setups
<!-- chapter: metricsql-query-language, duration: 3h -->
* `MetricsQL` Query Language
    * `MetricsQL` vs `PromQL`: similarities and extensions
    * Instant queries and range queries
    * Label filtering and matching operators
    * Aggregation functions: sum, avg, max, count, and more
    * `MetricsQL`-specific functions: `rollup`, `aggr_over_time`, `topk_last`
    * Subqueries and nested aggregations
    * Handling staleness and gaps in data
    * Query optimization tips and pitfalls
    * Using the `vmui` query interface
<!-- chapter: retention-and-storage-management, duration: 2h -->
* Retention and Storage Management
    * Configuring global and per-tenant retention periods
    * Disk space estimation and capacity planning
    * Downsampling for long-term storage efficiency
    * Using `vmctl` for data migration and backup
    * Snapshots and point-in-time recovery
    * Deleting metrics by label selectors
    * Monitoring disk usage and storage health
<!-- chapter: clustering-mode, duration: 2h -->
* Clustering Mode
    * Cluster architecture: `vminsert`, `vmstorage`, `vmselect` in depth
    * Deploying a `VictoriaMetrics` cluster on `Kubernetes`
    * Replication factor and data redundancy
    * Horizontal scaling of each cluster component independently
    * Load balancing and routing with `vmauth`
    * Multi-tenancy and tenant isolation
    * Cluster upgrade strategies with zero downtime
<!-- chapter: alerting-with-vmalert, duration: 2h -->
* Alerting with `VMAlert`
    * `VMAlert` architecture and how it differs from `Prometheus` Alertmanager
    * Defining alerting rules and recording rules
    * Routing alerts to `Alertmanager` for notification
    * `VMAlert` high-availability configuration
    * Debugging and silencing alerts
    * Migrating existing `Prometheus` alerting rules to `VMAlert`
<!-- chapter: grafana-integration, duration: 1h -->
* `Grafana` Integration
    * Configuring `VictoriaMetrics` as a `Prometheus`-compatible data source in `Grafana`
    * Importing pre-built `VictoriaMetrics` dashboards
    * Using `MetricsQL`-specific functions in `Grafana` panels
    * Alerting from `Grafana` against `VictoriaMetrics`
    * Best practices for dashboard performance with large datasets

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
