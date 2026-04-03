---
tags:
  - data-and-ai:data-engineering
  - tools:trino
  - databases:distributed-sql
  - practices:data-engineering
  - databases:query-engine
level: intermediate
category: data-engineering
duration_hours: 24
audience:
  - audiences:data-engineers
  - audiences:data-scientists
  - audiences:analysts
---
<!-- course: trino -->
# `Trino`

## Description
`Trino` (formerly `PrestoSQL`) is a high-performance distributed `SQL` query engine designed to run interactive and batch analytical queries against data wherever it lives — data lakes, warehouses, relational databases, and `NoSQL` stores — without moving the data. This course covers `Trino` from first principles, progressing through cluster setup, connector configuration, `SQL` capabilities, and advanced query optimisation techniques. Participants will learn how to federate queries across multiple heterogeneous data sources, apply fine-grained security and access control, and operate `Trino` clusters in production with observability and tuning. The course concludes with a practical comparison of `Trino` versus `Spark SQL` and a discussion of `Trino`'s role in the modern data stack.

## Duration
24 hours / 3 days

## Intended Audience
* Data engineers designing and maintaining data lake query infrastructure
* Data scientists and analysts querying large-scale datasets interactively
* Platform engineers deploying and operating `Trino` clusters
* Architects evaluating distributed `SQL` engines for analytical workloads
* Engineers migrating from `Hive`, `Presto`, or `Spark SQL` to `Trino`

## Prerequisites
* Strong proficiency in `SQL`: joins, aggregations, window functions, and CTEs
* Familiarity with `Linux` command-line tools and `bash`
* Basic understanding of distributed systems and big data concepts
* Experience with cloud object storage (`S3`, `GCS`, `ADLS`)
* Basic knowledge of `Docker` and container management

## Required Knowledge
* `SQL` Intermediate (or equivalent experience)
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Understand `Trino`'s architecture and how it executes distributed queries
* Install and configure a `Trino` cluster with coordinators and workers
* Configure and use connectors for `Hive`, `Iceberg`, `Delta Lake`, `JDBC`, and more
* Write advanced `Trino SQL` using built-in functions, `lambda` expressions, and window functions
* Analyse and optimise query plans for improved performance
* Implement security with authentication, authorisation, and column-level masking
* Execute cross-source federated queries joining data from disparate systems
* Monitor and operate `Trino` clusters with metrics, logging, and diagnostics
* Compare `Trino` and `Spark SQL` to select the appropriate engine for given workloads

## Outline
<!-- chapter: introduction-to-trino, duration: 2h -->
* Introduction to `Trino`
    * What is `Trino` and the problem it solves
    * History: `Facebook Presto`, `PrestoSQL`, and the `Trino` rename
    * Key characteristics: ANSI `SQL`, federated queries, pluggable connectors
    * `Trino` vs `Hive`, `Impala`, `Spark SQL`, and `BigQuery`
    * Typical use cases: interactive analytics, data lake queries, data federation
    * `Trino` in the modern data stack
    * Overview of the `Trino` community and ecosystem
<!-- chapter: trino-architecture, duration: 2h -->
* `Trino` Architecture
    * Coordinator and worker node roles
    * Query lifecycle: submission, planning, scheduling, and execution
    * The `Trino` query planner and cost-based optimiser
    * Stage, task, and split concepts
    * Memory management: query memory limits, memory pools, and spilling
    * Exchange operator and data shuffling between workers
    * Connector `SPI`: how `Trino` abstracts data sources
    * Fault tolerance execution mode and retry semantics
<!-- chapter: installation-and-cluster-setup, duration: 2h -->
* Installation and Cluster Setup
    * System requirements and `Java` prerequisites
    * Installing `Trino` on bare metal and `Docker`
    * Deploying `Trino` on `Kubernetes` with the `Trino Helm` chart
    * Coordinator and worker configuration files
    * Configuring memory, parallelism, and scheduling policies
    * `JVM` tuning for `Trino` workloads
    * `Trino CLI` and `JDBC` driver setup
    * Health checks and readiness probes for production deployments
<!-- chapter: connectors-hive-iceberg-delta-lake-jdbc, duration: 3h -->
* Connectors: `Hive`, `Iceberg`, `Delta Lake`, `JDBC`
    * `Hive` connector: configuring the `Hive Metastore`, reading `ORC` and `Parquet`
    * `Iceberg` connector: table formats, schema evolution, and time travel
    * `Delta Lake` connector: reading `Delta` tables from `S3` and `ADLS`
    * `JDBC` connectors: `PostgreSQL`, `MySQL`, `SQL Server` — configuration and limitations
    * `Kafka` connector for querying streaming data
    * `MongoDB` and `Elasticsearch` connectors for `NoSQL` federation
    * Object storage configuration: `S3`, `GCS`, `ADLS` credentials and endpoints
    * Connector performance tuning: predicate pushdown, projection pushdown
<!-- chapter: trino-sql-and-functions, duration: 3h -->
* `Trino SQL` and Functions
    * ANSI `SQL` compliance and `Trino` extensions
    * Data types: primitive, complex (`ARRAY`, `MAP`, `ROW`), and `JSON`
    * String, date/time, and mathematical functions
    * `Array` and map functions: `transform`, `filter`, `reduce`, `map_filter`
    * `Lambda` expressions and higher-order functions
    * Window functions: `ROW_NUMBER`, `RANK`, `LAG`, `LEAD`, `NTILE`
    * Approximate aggregations: `approx_distinct`, `approx_percentile`
    * `UNNEST` for flattening arrays and maps
    * Regular expression functions and `LIKE` patterns
    * `EXPLAIN` and `EXPLAIN ANALYZE` for understanding query plans
<!-- chapter: query-performance-and-optimization, duration: 3h -->
* Query Performance and Optimisation
    * Reading and interpreting `Trino` query plans
    * Cost-based optimiser: statistics collection and table statistics
    * Partition pruning and predicate pushdown
    * Join strategies: broadcast join, partitioned join, dynamic filtering
    * Optimising `file` formats: `Parquet` vs `ORC`, column statistics, and row groups
    * `Iceberg` table optimisation: compaction, sorting, and Z-ordering
    * Query resource groups and workload management
    * Identifying and resolving slow queries with the `Trino UI`
    * Memory spilling configuration for large aggregations
<!-- chapter: security-and-access-control, duration: 2h -->
* Security and Access Control
    * Authentication options: `Kerberos`, `LDAP`, `JWT`, `OAuth2`, certificates
    * Internal cluster communication security with `TLS`
    * Authorisation with `file`-based rules and `Apache Ranger`
    * Column-level security: column masking and row filtering
    * System access control and connector-level permissions
    * User impersonation and service account patterns
    * Audit logging for compliance and security monitoring
    * Secrets management for connector credentials
<!-- chapter: federation-joining-data-across-sources, duration: 2h -->
* Federation: Joining Data Across Sources
    * What is query federation and why it is powerful
    * Cross-connector `JOIN` queries: `Hive` + `PostgreSQL` + `Kafka`
    * Federated query planning and optimisation challenges
    * Push-down capabilities and their impact on federated query performance
    * Data virtualisation patterns with `Trino`
    * Practical examples: enriching data lake records with relational dimension tables
    * Limitations of federation: latency, data volume, and connector capabilities
    * Materialising frequently federated queries for performance
<!-- chapter: operations-and-monitoring, duration: 2h -->
* Operations and Monitoring
    * `Trino Web UI`: query details, stages, tasks, and resource usage
    * `JMX` metrics and the `Trino` metrics endpoint
    * Integrating with `Prometheus` and `Grafana` for cluster dashboards
    * Logging configuration and log aggregation
    * Graceful worker shutdown and rolling upgrades
    * Query history and `Trino` event listeners for audit trails
    * Capacity planning: worker sizing and concurrency limits
    * Troubleshooting common failure modes: OOM, spill, and stalled queries
<!-- chapter: trino-vs-spark-sql-comparison, duration: 2h -->
* `Trino` vs `Spark SQL` Comparison
    * Fundamental architectural differences: MPP engine vs distributed processing framework
    * Query latency and interactive query performance
    * Batch processing and `ETL` suitability
    * Connector ecosystems and data source coverage
    * Resource management and multi-tenancy
    * Operational complexity and cluster management
    * Community, commercial support, and long-term trajectory
    * Decision framework: `when` to use `Trino`, `when` to use `Spark SQL`
<!-- chapter: trino-in-the-modern-data-stack, duration: 1h -->
* `Trino` in the Modern Data Stack
    * `Trino` as the query layer in a data lakehouse
    * Integration with `Apache Iceberg` for open table format analytics
    * Connecting `Trino` to `dbt` for transformation workflows
    * `Trino` with `Apache Superset`, `Metabase`, and `Tableau` for BI
    * Managed `Trino` offerings: `Starburst`, `AWS Athena`, `Lyft Presto`
    * Migration paths from legacy `Hive` workloads to `Trino`
    * Future directions: `Trino` native execution engine and `Velox` integration

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
