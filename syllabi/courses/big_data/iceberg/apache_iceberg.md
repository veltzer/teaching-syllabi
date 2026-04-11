---
tags:
  - tools:iceberg
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
<!-- course: apache_iceberg -->
# `Apache` `Iceberg`

## Description
`Apache Iceberg` is an open table format designed for huge analytic datasets. This course covers the architecture, features, and practical usage of `Iceberg`, including schema and partition evolution, time travel, snapshot management, and integration with popular query engines such as `Spark`, `Trino`, `Presto`, and `Flink`. Participants will also learn about catalog options, migration strategies, and performance optimization techniques.

## Duration
16 hours / 2 days

## Intended Audience
* Data engineers and data platform engineers
* Software developers working with data lakes
* Data scientists who need reliable large-scale data access
* Data architects evaluating open table formats
* `DevOps` engineers supporting data infrastructure

## Prerequisites
* Working knowledge of `SQL`
* Basic understanding of distributed storage and data lake concepts
* Familiarity with at least one query engine (`Spark`, `Trino`, `Presto`, or `Flink`)
* Understanding of `file` formats such as `Parquet` and ORC
* Basic command-line interface usage

## Objectives
* Understand the open table format landscape and why `Iceberg` was created
* Explain `Iceberg` architecture including metadata, manifest files, and data files
* Perform schema evolution and partition evolution without rewriting data
* Use time travel and snapshot rollback for data recovery and auditing
* Configure and manage `Iceberg` tables with `Spark`, `Trino`/`Presto`, and `Flink`
* Set up and choose between catalog implementations (`Hive`, `REST`, Nessie, `AWS Glue`)
* Apply compaction and performance optimization strategies
* Compare `Iceberg` with `Delta Lake` and `Apache Hudi`
* Plan and execute migrations from existing table formats to `Iceberg`

## Outline
<!-- chapter: open-table-format-concepts, duration: 1h -->
* Open Table Format Concepts
    * The data lakehouse paradigm
    * Problems with traditional `Hive`-style tables
    * What open table formats solve
    * Overview of `Iceberg`, `Delta Lake`, and `Hudi`
<!-- chapter: iceberg-architecture, duration: 1h -->
* `Iceberg` Architecture
    * Table specification and format versioning
    * Metadata layer: metadata files, manifest lists, and manifest files
    * Data files and `file` formats (`Parquet`, ORC, `Avro`)
    * Catalog layer and its role
    * How reads and writes interact with metadata
<!-- chapter: schema-evolution, duration: 1h -->
* Schema Evolution
    * Adding, dropping, renaming, and reordering columns
    * Type promotion rules
    * Schema evolution without rewriting data
    * Handling schema changes in downstream consumers
<!-- chapter: partitioning-in-iceberg, duration: 1h -->
* Partitioning in `Iceberg`
    * Traditional partitioning vs hidden partitioning
    * Partition transforms (identity, bucket, truncate, year, month, day, hour)
    * Partition evolution and its impact on queries
    * Writing queries without partition awareness
<!-- chapter: time-travel-and-snapshot-management, duration: 1h -->
* Time Travel and Snapshot Management
    * Snapshot isolation and consistency guarantees
    * Querying historical snapshots by timestamp and snapshot `ID`
    * Rolling back to previous table states
    * Snapshot expiration and retention policies
    * Cherry-picking and managing snapshot lineage
<!-- chapter: compaction-and-maintenance, duration: 1h -->
* Compaction and Maintenance
    * Small `file` problem and its impact on performance
    * Compaction strategies and scheduling
    * Rewriting data files and manifest files
    * Expire snapshots and remove orphan files
    * Table maintenance automation
<!-- chapter: iceberg-with-spark, duration: 2h -->
* `Iceberg` with `Spark`
    * Configuring `Spark` with `Iceberg` support
    * Creating and managing `Iceberg` tables in `Spark`
    * Reading and writing data with `Spark SQL` and DataFrame `API`
    * Merge-on-read vs copy-on-write
    * `Structured Streaming` with `Iceberg`
<!-- chapter: iceberg-with-trino-presto, duration: 1h -->
* `Iceberg` with `Trino`/`Presto`
    * Configuring `Trino` and `Presto` connectors for `Iceberg`
    * Querying `Iceberg` tables with `SQL`
    * Performance considerations and query planning
<!-- chapter: iceberg-with-flink, duration: 1h -->
* `Iceberg` with `Flink`
    * `Flink` `Iceberg` connector setup
    * Streaming writes to `Iceberg` tables
    * Batch reads and incremental reads
<!-- chapter: iceberg-catalogs, duration: 2h -->
* `Iceberg` Catalogs
    * `Hive Metastore` catalog
    * `REST` catalog specification
    * Nessie catalog for `Git`-like data versioning
    * `AWS Glue` catalog integration
    * Choosing the right catalog for your environment
<!-- chapter: comparison-with-delta-lake-and-hudi, duration: 1h -->
* Comparison with `Delta Lake` and `Hudi`
    * Feature comparison across open table formats
    * Performance characteristics and trade-offs
    * Ecosystem support and community adoption
    * Interoperability and universal format initiatives
<!-- chapter: migration-strategies, duration: 1h -->
* Migration Strategies
    * Migrating from `Hive` tables to `Iceberg`
    * In-place migration vs full rewrite approaches
    * Migrating from `Delta Lake` or `Hudi` to `Iceberg`
    * Testing and validation during migration
<!-- chapter: performance-optimization, duration: 2h -->
* Performance Optimization
    * `File` sizing and layout strategies
    * Sort order optimization
    * Predicate pushdown and column pruning
    * Caching strategies
    * Monitoring and profiling `Iceberg` table performance

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
