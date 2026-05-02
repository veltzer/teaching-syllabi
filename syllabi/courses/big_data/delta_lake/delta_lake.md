---
tags:
  - tools:delta-lake
  - data-and-ai:big-data
  - languages:sql
level: intermediate
category: big-data
duration_hours: 16
audience:
  - audiences:developers
  - audiences:data-scientists
  - audiences:architects
  - audiences:devops
---
<!-- course: delta_lake -->
# `Delta Lake`

## Description
`Delta Lake` is an open-source storage layer that brings ACID transactions, scalable metadata handling, and data versioning to data lakes. This course covers the architecture and features of `Delta Lake`, including time travel, schema enforcement and evolution, DML operations, performance optimization with Z-ordering and liquid clustering, and integration with `Spark`, `Databricks`, and standalone engines via `delta`-rs.

## Duration
16 hours / 2 days

## Intended Audience
* Data engineers building and maintaining data pipelines
* Software developers working with data lake architectures
* Data scientists who need reliable and versioned data access
* Data architects evaluating lakehouse storage layers
* `DevOps` engineers supporting data platforms

## Prerequisites
* Working knowledge of `SQL`
* Basic understanding of `Apache Spark` and distributed computing concepts
* Familiarity with data lake storage (`S3`, `ADLS`, `GCS`)
* Understanding of file formats such as `Parquet`
* Basic command-line interface usage

## Objectives
* Understand the `Delta Lake` architecture and transaction log
* Leverage ACID transactions for reliable data lake operations
* Use time travel for data auditing, recovery, and reproducibility
* Apply schema enforcement and schema evolution to manage data changes
* Perform MERGE, UPDATE, and DELETE operations on data lake tables
* Optimize table performance with VACUUM, OPTIMIZE, Z-ordering, and liquid clustering
* Configure and use `Delta Sharing` for secure data sharing
* Integrate `Delta Lake` with `Spark`, `Databricks`, and `delta`-rs
* Compare `Delta Lake` with Iceberg and `Hudi`

## Outline
<!-- chapter: delta-lake-overview-and-architecture, duration: 2h -->
* `Delta Lake` Overview and Architecture
    * The data lakehouse paradigm and `Delta Lake` role
    * Transaction log (_delta_log) internals
    * Optimistic concurrency control
    * `Delta Lake` protocol and reader/writer compatibility
    * `Delta Lake` open-source vs `Databricks` managed offering
<!-- chapter: acid-transactions-on-data-lakes, duration: 1h -->
* ACID Transactions on Data Lakes
    * Atomicity and consistency guarantees
    * Concurrent read and write handling
    * Conflict resolution and retry mechanisms
    * Write-ahead log and checkpoint files
<!-- chapter: time-travel, duration: 1h -->
* Time Travel
    * Querying data by version number and timestamp
    * Restoring tables to previous versions
    * Auditing data changes over time
    * Retention policies and time travel limitations
<!-- chapter: schema-enforcement-and-evolution, duration: 1h -->
* Schema Enforcement and Evolution
    * Schema validation on write
    * Adding and merging new columns
    * Column mapping and renaming
    * Handling schema mismatches in pipelines
<!-- chapter: dml-operations, duration: 2h -->
* DML Operations
    * `MERGE INTO` for upserts and slowly changing dimensions
    * UPDATE and DELETE operations
    * Conditional operations and predicate handling
    * Change Data Feed for capturing row-level changes
    * Streaming reads from change data feed
<!-- chapter: table-maintenance-and-optimization, duration: 2h -->
* Table Maintenance and Optimization
    * VACUUM command and file cleanup
    * OPTIMIZE command for file compaction
    * Z-ordering for data skipping and query acceleration
    * Liquid clustering as next-generation data layout
    * Auto-optimization settings and best practices
<!-- chapter: uniform-universal-format, duration: 1h -->
* UniForm (Universal Format)
    * Cross-format compatibility with Iceberg and `Hudi`
    * Enabling UniForm on Delta tables
    * Reading Delta tables from Iceberg-compatible engines
    * Use cases and limitations
<!-- chapter: delta-sharing, duration: 1h -->
* `Delta Sharing`
    * Open protocol for secure data sharing
    * Sharing data across organizations and platforms
    * Setting up `Delta Sharing` server and recipients
    * Consuming shared data from various clients
<!-- chapter: delta-lake-with-spark, duration: 1h -->
* `Delta Lake` with `Spark`
    * Configuring `Spark` with `Delta Lake` support
    * Creating and managing Delta tables
    * Batch and streaming operations
    * Performance tuning for `Spark` workloads
<!-- chapter: delta-lake-standalone-delta-rs, duration: 1h -->
* `Delta Lake` Standalone (`delta`-rs)
    * `delta`-rs Rust-based engine overview
    * `Python` bindings (deltalake package)
    * Reading and writing Delta tables without `Spark`
    * Integration with Pandas, `Polars`, and `DuckDB`
<!-- chapter: integration-with-databricks-and-other-engines, duration: 1h -->
* Integration with `Databricks` and Other Engines
    * `Databricks` runtime and Delta optimizations
    * `Unity` Catalog and governance features
    * Integration with `Trino`, Presto, and Athena
    * Integration with `Flink` and other streaming engines
<!-- chapter: comparison-with-iceberg-and-hudi, duration: 1h -->
* Comparison with Iceberg and `Hudi`
    * Feature comparison across open table formats
    * Performance characteristics and trade-offs
    * Community adoption and ecosystem support
    * Choosing the right format for your use case
<!-- chapter: best-practices, duration: 1h -->
* Best Practices
    * Table design and partitioning strategies
    * Pipeline architecture patterns
    * Monitoring and alerting on Delta tables
    * Cost management and storage optimization

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
