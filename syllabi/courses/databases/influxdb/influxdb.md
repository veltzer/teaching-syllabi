---
tags:
  - databases:influxdb
  - databases:time-series
  - databases:nosql
  - tools:influxdb
level: intermediate
category: database
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
  - audiences:sysadmins
---
<!-- course: influxdb -->
# `InfluxDB`

## Description
`InfluxDB` is a purpose-built time-series database optimized for high-write-throughput ingestion of metrics, events, and IoT sensor data. This course covers `InfluxDB` from its core architecture and data model through to production deployment, monitoring, and integration with visualization tools like `Grafana`. Participants will learn both the classic `InfluxDB` 1.x concepts and the modern `InfluxDB` 2.x and 3.x platform, including the `Flux` scripting language for powerful data transformations. By the end of the course, attendees will be equipped to design time-series solutions, write efficient queries, implement downsampling strategies, and set up alerting pipelines.

## Duration
16 hours / 2 days

## Intended Audience
* Developers building applications that produce or consume time-series data
* `DevOps` and platform engineers collecting infrastructure and application metrics
* System administrators managing monitoring stacks
* IoT engineers ingesting sensor and telemetry data
* Engineers evaluating time-series databases for observability platforms

## Prerequisites
* Basic knowledge of databases and `SQL` concepts
* Familiarity with command-line tools
* Experience with at least one scripting language (`Python`, `Bash`, or similar)
* Basic understanding of monitoring and metrics concepts is helpful

## Objectives
* Understand the architecture and design goals of `InfluxDB`
* Model time-series data using measurements, tags, and fields effectively
* Write data using the line protocol, client libraries, and `Telegraf`
* Query and transform data using the `Flux` language
* Implement downsampling and retention policies to manage data lifecycle
* Create tasks and alerting rules using the `InfluxDB` UI and `API`
* Visualize time-series data using `Grafana` with `InfluxDB` as a data source
* Understand clustering, high availability, and capacity planning for `InfluxDB`

## Exercises
Hands-on labs using a local `InfluxDB` 2.x instance. Students will set up `Telegraf` to collect system metrics, write data using the line protocol and `Python` client library, query and transform time-series data with `Flux`, create downsampling tasks with continuous queries, configure alert checks and notification endpoints, and build dashboards in `Grafana`. Scenarios include infrastructure monitoring, application performance tracking, and IoT sensor data pipelines.

## Outline
<!-- chapter: introduction-to-time-series-databases, duration: 1h -->
* Introduction to Time-Series Databases
    * What is time-series data and its characteristics
    * Challenges with storing time-series in relational databases
    * Overview of the time-series database landscape
    * `InfluxDB` history and versions: 1.x, 2.x, and 3.x
    * Key use cases: metrics, IoT, observability, and finance

<!-- chapter: influxdb-architecture, duration: 2h -->
* `InfluxDB` Architecture
    * Storage engine: TSM (Time-Structured Merge Tree)
    * WAL (Write-Ahead Log) and cache
    * Shards, shard groups, and retention policies in 1.x
    * Buckets and organizations in 2.x
    * Write and query paths
    * The `InfluxDB` IOx columnar storage engine (v3)
    * Cardinality and its impact on performance

<!-- chapter: data-model-measurements-tags-fields, duration: 2h -->
* Data Model: Measurements, Tags, and Fields
    * Line protocol syntax and structure
    * Measurements as metric namespaces
    * Tags as indexed metadata dimensions
    * Fields as unindexed value columns
    * Timestamps and time precision
    * Tag cardinality best practices
    * Schema `design patterns` for metrics and events

<!-- chapter: writing-data, duration: 2h -->
* Writing Data
    * Writing via the line protocol over `HTTP`
    * Using the `InfluxDB` `CLI` (`influx` command)
    * `Telegraf` agent: architecture and configuration
    * Core `Telegraf` input and output plugins
    * `Python`, `Go`, and `JavaScript` client libraries
    * Batch writes and write optimizations
    * Handling write errors and retries

<!-- chapter: querying-with-flux, duration: 3h -->
* Querying with `Flux`
    * Introduction to the `Flux` functional data language
    * `from()`, `range()`, `filter()`, `yield()` pipeline basics
    * Aggregations: `mean()`, `sum()`, `count()`, `last()`
    * `aggregateWindow()` for time-bucketed aggregations
    * Joins: `join()` and `union()` across measurements
    * Transformations: `map()`, `pivot()`, `drop()`, `keep()`
    * `Flux` variables, functions, and control flow
    * InfluxQL for 1.x compatibility

<!-- chapter: downsampling-and-retention-policies, duration: 2h -->
* Downsampling and Retention Policies
    * Why downsampling is essential for long-term storage
    * Retention policies in `InfluxDB` 1.x
    * Bucket retention in `InfluxDB` 2.x
    * Creating continuous queries for automatic downsampling
    * `Flux` tasks for scheduled downsampling
    * Data lifecycle management patterns
    * Storage cost optimization strategies

<!-- chapter: tasks-and-alerts, duration: 2h -->
* Tasks and Alerts
    * `InfluxDB` tasks: scheduling `Flux` scripts
    * Creating, managing, and debugging tasks
    * Checks: threshold, deadman, and custom checks
    * Notification rules and notification endpoints
    * Integrating with `PagerDuty`, `Slack`, and email
    * Alert lifecycle and state management

<!-- chapter: visualization-with-grafana, duration: 1h -->
* Visualization with `Grafana`
    * Connecting `Grafana` to `InfluxDB` as a data source
    * Writing `Flux` queries in `Grafana` panels
    * Building time-series dashboards
    * Variables and templating in `Grafana`
    * Alerting in `Grafana` vs `InfluxDB` native alerts

<!-- chapter: influxdb-clustering-and-high-availability, duration: 1h -->
* `InfluxDB` Clustering and High Availability
    * `InfluxDB` OSS vs `InfluxDB` Enterprise vs `InfluxDB` Cloud
    * High availability with `InfluxDB` Enterprise clustering
    * Replication factor and anti-entropy
    * `InfluxDB` Cloud multi-region architecture
    * Backup and restore strategies
    * Capacity planning and scaling considerations

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
