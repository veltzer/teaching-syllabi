---
tags:
  - tools:clickhouse
  - data-and-ai:big-data
  - data-and-ai:data-analysis
level: intermediate
category: database
duration_hours: 24
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: clickhouse_for_developers -->
# `ClickHouse` for Developers

## Description
This course provides comprehensive training in `ClickHouse`, a high-performance column-oriented database for online analytical processing (OLAP). Participants will learn how to design schemas, write efficient queries, optimize performance, and integrate `ClickHouse` into their data pipelines and analytics workflows.

The course emphasizes practical experience with real-world analytical scenarios, preparing developers and data scientists to leverage `ClickHouse` for large-scale data analysis and reporting.

## Duration
24 hours / 3 days

## Intended Audience
* Developers building analytics and reporting applications
* Data scientists working with large-scale analytical data
* Data engineers designing data pipelines
* Backend developers integrating OLAP capabilities
* Analytics engineers transitioning to `ClickHouse`

## Prerequisites
* `Solid` understanding of `SQL` fundamentals
* Basic understanding of database concepts
* Familiarity with `Linux` command line
* Experience with at least one programming language

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Understand column-oriented database concepts and `ClickHouse` architecture
* Design efficient table schemas using appropriate engines
* Write optimized `SQL` queries for analytical workloads
* Implement materialized views and dictionaries
* Configure partitioning, sharding, and replication
* Monitor and optimize `ClickHouse` performance
* Integrate `ClickHouse` with external tools and data sources

## Exercises
Hands-on lab exercises covering schema design, data ingestion, query writing, materialized views, dictionaries, and performance optimization. Students will create tables with various `MergeTree` engine variants, load and transform large datasets, write complex analytical queries, build materialized views for real-time aggregation, configure dictionaries for data enrichment, and analyze query performance. Exercises use realistic analytical datasets and workloads.

## Outline
<!-- chapter: column-oriented-database-concepts, duration: 1h -->
* Column-Oriented Database Concepts
    * Row-oriented vs column-oriented storage
    * Advantages for analytical workloads
    * Compression benefits of columnar storage
    * `When` to use `ClickHouse` vs row-oriented databases
    * Comparison with other OLAP systems: `Apache Druid`, `Apache Pinot`, Vertica

<!-- chapter: clickhouse-architecture, duration: 2h -->
* `ClickHouse` Architecture
    * Server architecture overview
    * `MergeTree` engine family fundamentals
    * Data storage and merge process
    * Parts, partitions, and granules
    * Primary index and sparse indexing
    * Query processing pipeline
    * Distributed query execution

<!-- chapter: sql-dialect-and-data-types, duration: 2h -->
* `SQL` Dialect and Data Types
    * `ClickHouse` `SQL` syntax and extensions
    * Numeric types: UInt8 through UInt256, Float32, `Float64`, Decimal
    * String types: String, FixedString, LowCardinality
    * Date and time types: Date, DateTime, DateTime64
    * Complex types: `Array`, Tuple, Map, Nested
    * Nullable types and their performance implications
    * Type conversion functions

<!-- chapter: table-engines, duration: 2h -->
* Table Engines
    * `MergeTree` engine and its variants
    * ReplacingMergeTree for deduplication
    * SummingMergeTree for pre-aggregation
    * AggregatingMergeTree for incremental aggregation
    * CollapsingMergeTree and VersionedCollapsingMergeTree
    * Log family engines
    * Integration engines: `Kafka`, `MySQL`, `PostgreSQL`, `S3`
    * Distributed engine for cluster queries

<!-- chapter: creating-and-managing-tables, duration: 1h -->
* Creating and Managing Tables
    * Table creation with `CREATE TABLE`
    * Choosing primary keys and ordering keys
    * `TTL` expressions for data lifecycle management
    * `ALTER TABLE` operations
    * Schema migrations and data transformations
    * Temporary tables and table functions

<!-- chapter: inserting-data, duration: 1h -->
* Inserting Data
    * Batch inserts and best practices
    * Insert formats: `CSV`, `JSON`, `Parquet`, Native
    * Streaming data with `Kafka` engine
    * Buffer engine for high-frequency inserts
    * Deduplication and idempotent inserts
    * Insert performance optimization

<!-- chapter: queries-and-aggregations, duration: 2h -->
* Queries and Aggregations
    * SELECT queries and filtering
    * Aggregate functions: standard and specialized
    * -If, -`Array`, and -State combinators
    * `GROUP BY` with `WITH ROLLUP`, `WITH CUBE`, `WITH TOTALS`
    * Window functions
    * Approximate aggregation functions: uniqHLL12, quantileTDigest
    * `Array` and string functions
    * Date and time functions

<!-- chapter: materialized-views, duration: 2h -->
* Materialized Views
    * Materialized view concepts in `ClickHouse`
    * Creating materialized views
    * Source and target table relationships
    * Aggregating materialized views
    * Chaining materialized views
    * Backfilling historical data
    * Use cases and `design patterns`

<!-- chapter: dictionaries, duration: 2h -->
* Dictionaries
    * External dictionary concepts
    * Dictionary sources: files, databases, `HTTP`
    * Dictionary layouts: flat, hashed, range_hashed, cache
    * Creating and managing dictionaries
    * Using dictionaries in queries
    * Dictionary refresh and updates
    * Performance considerations

<!-- chapter: joins-and-subqueries, duration: 1h -->
* Joins and Subqueries
    * Join types in `ClickHouse`: JOIN, `GLOBAL JOIN`
    * Join algorithms: hash, partial_merge, direct
    * Join performance considerations
    * Subqueries and IN operators
    * `WITH-clauses` (common table expressions)
    * Best practices for join optimization

<!-- chapter: partitioning-and-sharding, duration: 1h -->
* Partitioning and Sharding
    * Partition key design and selection
    * Partition operations: detach, attach, drop
    * Sharding concepts and strategies
    * Distributed table and shard routing
    * Cluster configuration
    * Data distribution and rebalancing

<!-- chapter: replication, duration: 1h -->
* Replication
    * ReplicatedMergeTree engine family
    * `ZooKeeper` / `ClickHouse Keeper` for coordination
    * Replication setup and configuration
    * Monitoring replication status
    * Handling replication lag and failures
    * Multi-datacenter replication

<!-- chapter: performance-optimization, duration: 2h -->
* Performance Optimization
    * Query profiling with EXPLAIN and system.query_log
    * Index types: primary, skipping (minmax, set, bloom_filter)
    * Projection tables for query acceleration
    * Memory usage optimization
    * Compression codecs and their impact
    * Settings for query performance tuning
    * Benchmarking with `clickhouse`-benchmark

<!-- chapter: monitoring, duration: 2h -->
* Monitoring
    * System tables for monitoring
    * system.query_log and system.processes
    * system.metrics, system.events, system.asynchronous_metrics
    * Integration with `Prometheus` and `Grafana`
    * Monitoring disk usage and merge activity
    * Alert configuration

<!-- chapter: integration-with-visualization-tools, duration: 2h -->
* Integration with Visualization Tools
    * Connecting `Grafana` to `ClickHouse`
    * Superset integration
    * Metabase integration
    * `JDBC` and ODBC drivers
    * Client libraries for popular programming languages
    * `REST` `API` and `HTTP` interface

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
