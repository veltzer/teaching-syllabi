---
tags:
  - databases:druid
  - databases:olap
  - databases:time-series
  - databases:real-time-analytics
  - tools:apache-druid
level: intermediate
category: database
duration_hours: 24
audience:
  - audiences:developers
  - audiences:data-engineers
  - audiences:architects
---
<!-- course: apache_druid -->
# `Apache Druid`

## Description
`Apache Druid` is a high-performance, real-time analytics database designed for sub-second OLAP queries on large-scale event and time-series datasets. Originally developed at MetaMarkets and open-sourced in 2012, Druid is widely used for powering interactive dashboards, user-facing analytics products, and operational monitoring systems at companies such as Netflix, Airbnb, and LinkedIn. This course provides a comprehensive understanding of Druid's unique architecture, ingestion model, data model, and query capabilities. Participants will learn how to ingest data from batch sources and streaming systems like `Kafka`, write efficient `Druid SQL` and native queries, operate and tune clusters, and integrate Druid into broader data platform architectures.

## Duration
24 hours / 3 days

## Intended Audience
* Data engineers building real-time analytics pipelines
* Backend developers powering user-facing analytics and dashboards
* Data platform architects evaluating OLAP stores for sub-second query requirements
* Engineers integrating Druid with `Kafka`, `Spark`, or data lake platforms
* DBAs and operations staff managing large-scale Druid deployments

## Prerequisites
* Familiarity with `SQL` and relational database concepts
* Basic understanding of distributed systems and big data concepts
* Experience with at least one of `Kafka`, `Spark`, or `Hadoop` is helpful
* Basic `Linux` system administration skills

## Objectives
* Understand Druid's architecture and how it delivers sub-second analytical queries
* Ingest data from batch files and streaming sources including `Kafka`
* Model data in Druid using dimensions, metrics, and timestamp columns effectively
* Write correct and efficient `Druid SQL` and native `JSON` queries
* Understand segment internals, indexing, and rollup
* Operate, scale, and maintain Druid clusters in production
* Integrate Druid with upstream systems such as `Apache Kafka` and `Apache Spark`
* Configure security, access control, and multi-tenancy
* Monitor cluster health and diagnose performance issues

## Exercises
Hands-on labs using a local Druid cluster deployed with `Docker Compose`. Students will ingest `CSV` and `Parquet` batch data, set up a `Kafka`-based streaming ingestion spec, query data with `Druid SQL` using the Druid console and `API`, configure rollup and aggregation at ingest time, inspect segment metadata, run compaction tasks, configure `TLS` and basic authentication, set up `Prometheus` metrics export, and integrate a `Spark` job to write to Druid. Scenarios cover clickstream analytics, ad impression tracking, and application performance monitoring.

## Outline
<!-- chapter: introduction-to-apache-druid, duration: 2h -->
* Introduction to `Apache Druid`
    * What is `Apache Druid` and its design goals
    * OLAP vs OLTP and where Druid fits
    * Key differentiators: sub-second queries, real-time ingestion, and rollup
    * Druid use cases: user-facing analytics, operational monitoring, and ad tech
    * Comparison with `ClickHouse`, `Pinot`, `BigQuery`, and `Elasticsearch`
    * Druid ecosystem and community

<!-- chapter: architecture-and-components, duration: 2h -->
* Architecture and Components
    * Process types: Coordinator, Overlord, Broker, Router, Historical, MiddleManager
    * Deep storage: `S3`, `HDFS`, and local file systems
    * Metadata storage: `MySQL` or `PostgreSQL` for cluster state
    * `ZooKeeper` for coordination
    * Segment lifecycle: creation, loading, and handoff
    * Query routing: Broker to Historical and MiddleManager
    * Data flows: batch ingestion, streaming ingestion, and query paths
    * High availability and fault tolerance

<!-- chapter: data-ingestion-batch-and-streaming, duration: 3h -->
* Data Ingestion: Batch and Streaming
    * Ingestion spec structure: `dataSchema`, `ioConfig`, `tuningConfig`
    * Native batch ingestion from local files, `S3`, and `HDFS`
    * `SQL`-based ingestion with `INSERT INTO`
    * `Kafka` indexing service: supervisor specs and lag monitoring
    * `Kinesis` indexing service overview
    * Tranquility server for push-based streaming (legacy)
    * Schema auto-discovery and explicit schema definition
    * Handling late-arriving data and out-of-order events

<!-- chapter: data-model-and-segments, duration: 2h -->
* Data Model and Segments
    * Druid data model: timestamp, dimensions, and metrics
    * Granularity: segment granularity and query granularity
    * Rollup: pre-aggregation at ingestion time and its benefits
    * Approximate aggregations: `HyperLogLog` and quantile sketches
    * Segment files: columnar storage format internals
    * Bitmap indexes for dimension filtering
    * Partitioning strategies: time-based and hash partitioning
    * Segment sizing and the impact on query performance

<!-- chapter: druid-sql-and-native-queries, duration: 3h -->
* `Druid SQL` and Native Queries
    * `Druid SQL` syntax and `PostgreSQL` dialect compatibility
    * Time functions: `TIME_FLOOR`, `TIME_PARSE`, and `__time`
    * Aggregation functions: `COUNT`, `SUM`, `APPROX_COUNT_DISTINCT`, `THETASKETCH`
    * `GROUPBY`, `TOPN`, and `TIMESERIES` native query types
    * Filtering: exact, range, regex, and selector filters
    * Joins in `Druid SQL`: broadcast and sort-merge
    * `EXPLAIN PLAN` for query analysis
    * Native `JSON` query `API` for advanced use cases

<!-- chapter: indexing-internals, duration: 2h -->
* Indexing Internals
    * The Peon process and task execution
    * MiddleManager and Indexer process modes
    * Compaction tasks for merging and re-indexing segments
    * Automatic compaction configuration
    * Re-indexing to change schema or rollup
    * Kill tasks for data deletion
    * Task queue management and priority

<!-- chapter: cluster-operations-and-tuning, duration: 3h -->
* Cluster Operations and Tuning
    * Sizing Historical, Broker, and MiddleManager nodes
    * Druid configuration files and common tuning parameters
    * `JVM` heap and direct memory tuning
    * Segment caching on Historical nodes
    * Query context parameters for performance control
    * Load rules for data tiering and retention
    * Auto-scaling Historical tier
    * Druid on `Kubernetes` with the `Druid Operator`

<!-- chapter: integration-with-kafka-and-spark, duration: 3h -->
* Integration with `Kafka` and `Spark`
    * Designing `Kafka` topics for optimal Druid ingestion
    * Supervisor specs: topic partitioning and offset management
    * Handling `Kafka` schema registry and `Avro`/`Protobuf` messages
    * Lag monitoring and scaling `Kafka` indexing tasks
    * Writing `Spark` jobs that output to Druid via `Kafka` or batch files
    * Using `Spark` for Druid compaction and re-ingestion
    * Druid as a sink in `Apache Flink` pipelines
    * Integration with `dbt` using the `dbt-druid` adapter

<!-- chapter: security-and-access-control, duration: 2h -->
* Security and Access Control
    * `TLS` encryption for inter-node and client communication
    * Authentication: basic auth, `Kerberos`, and `LDAP`
    * Authorization: resource-based access control (`RBAC`)
    * Datasource-level and config-level permissions
    * Audit logging
    * Multi-tenancy patterns with namespace isolation
    * Securing deep storage access with `IAM` roles

<!-- chapter: monitoring-and-troubleshooting, duration: 2h -->
* Monitoring and Troubleshooting
    * Druid emitter framework: `Prometheus` and logging emitters
    * Key metrics: query latency, ingestion lag, segment count, and `JVM` GC
    * `Grafana` dashboards for Druid
    * The Druid web console: task management, segment view, and query editor
    * Diagnosing slow queries with query metrics and broker logs
    * Common ingestion issues: parse exceptions, lag, and OOM
    * Coordinator duty logs and segment balancing issues

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
