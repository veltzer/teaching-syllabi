---
tags:
  - data-and-ai:data-engineering
  - tools:apache-hudi
  - practices:data-lake
  - databases:lakehouse
  - practices:data-engineering
  - concepts:acid
level: intermediate
category: data-engineering
duration_hours: 24
audience:
  - audiences:data-engineers
  - audiences:data-architects
---
<!-- course: apache_hudi -->
# `Apache Hudi`

## Description
`Apache Hudi` (`Hadoop` Upserts Deletes and Incrementals) is an open-source transactional data lake platform that brings database-like capabilities — upserts, deletes, ACID transactions, and incremental processing — to cloud object storage and `HDFS`. This course provides a thorough grounding in `Hudi`'s architecture, table types, and write/read APIs, enabling participants to build reliable, scalable lakehouse solutions on top of `Amazon S3`, `ADLS`, or `HDFS`. Participants will learn to integrate `Hudi` with `Apache Spark` and `Apache Flink`, perform schema evolution, configure compaction and clustering for performance, and run incremental pipelines that efficiently process only changed data. The course concludes with a comparative analysis of `Apache Hudi`, `Delta Lake`, and `Apache Iceberg` to help participants choose the right open table format for their use case.

## Duration
24 hours / 3 days

## Intended Audience
* Data engineers building lakehouse architectures on cloud object storage
* Data architects designing scalable and transactional data lake platforms
* Engineers migrating from Hive-based data warehouses to open table formats
* Platform engineers deploying and operating `Hudi`-based data infrastructure
* Data engineers working with `Apache Spark` and `Apache Flink` for large-scale `ETL`

## Prerequisites
* Proficiency in `Apache Spark` for data processing (`PySpark` or `Scala`)
* Strong understanding of `SQL` and data modelling concepts
* Familiarity with cloud object storage (`S3`, `ADLS`, or `GCS`)
* Basic understanding of `Hive Metastore` or `AWS Glue` catalog
* Experience with `Linux` command-line tools and `Docker`

## Required Knowledge
* `Apache Spark` Fundamentals (or equivalent experience)
* `SQL` Intermediate (or equivalent experience)

## Objectives
* Understand the challenges of managing mutable data in data lakes and how `Hudi` addresses them
* Describe `Hudi`'s architecture, storage model, and timeline
* Choose between Copy-on-Write and Merge-on-Read table types based on workload requirements
* Write data to `Hudi` tables using `Spark` datasource and `DeltaStreamer`
* Query `Hudi` tables using snapshot, incremental, and read-optimised query types
* Build incremental data pipelines using `Hudi`'s changelog and incremental query APIs
* Manage schema evolution safely across `Hudi` table versions
* Integrate `Hudi` with `Apache Flink` for streaming write workloads
* Configure and tune compaction and clustering for optimal read performance
* Compare `Apache Hudi`, `Delta Lake`, and `Apache Iceberg` for lakehouse architecture decisions

## Outline
<!-- chapter: introduction-to-data-lake-challenges, duration: 2h -->
* Introduction to Data Lake Challenges
    * The data lake promise: cheap, scalable storage for raw data
    * Traditional data lake limitations: no ACID transactions, no upserts, no deletes
    * The problem of late-arriving data and mutable records
    * `GDPR` and compliance requirements: the right to erasure in data lakes
    * CDC (change data capture) and the need to reflect source system changes
    * What is a lakehouse: combining data lake storage with data warehouse capabilities
    * Overview of open table formats: `Apache Hudi`, `Delta Lake`, `Apache Iceberg`
    * Why organisations choose `Apache Hudi`
<!-- chapter: apache-hudi-architecture, duration: 2h -->
* `Apache Hudi` Architecture
    * `Hudi` storage model: base files, log files, and file groups
    * The `Hudi` timeline: a consistent ordered log of all table actions
    * Timeline actions: `COMMIT`, DELTA_COMMIT, COMPACTION, CLEAN, `CLUSTERING`
    * `Hudi` metadata table: fast file listing and column statistics
    * Index types: Bloom filter, `HBase`, bucket, record-level indexes
    * `Hudi` table services: compaction, cleaning, clustering, and archiving
    * Integration with `Hive Metastore`, `AWS Glue`, and `Apache Atlas`
    * `Hudi` versioning and the record key / partition path model
<!-- chapter: table-types-cow-vs-mor, duration: 2h -->
* Table Types: Copy-on-Write vs Merge-on-Read
    * Copy-on-Write (`CoW`): how writes rewrite base `Parquet` files
    * `CoW` trade-offs: write amplification vs fast reads
    * Merge-on-Read (`MoR`): writes go to `delta` log files, merged at read time
    * `MoR` trade-offs: low write latency vs merge overhead at read time
    * Read query types on `MoR` tables: snapshot, read-optimised, and incremental
    * Choosing between `CoW` and `MoR` based on write and read SLAs
    * Hybrid workloads: mixing `CoW` and `MoR` tables in a single pipeline
    * Converting between `CoW` and `MoR` table types
<!-- chapter: writing-data-with-hudi, duration: 3h -->
* Writing Data with `Hudi`
    * `Hudi` `Spark` datasource: reading and writing with the `hudi` format
    * Write operations: `INSERT`, UPSERT, BULK_INSERT, DELETE, `INSERT_OVERWRITE`
    * Record key and partition path configuration
    * Configuring the `Hudi` index for upsert matching
    * `DeltaStreamer`: a built-in tool for continuous and incremental ingestion
    * `DeltaStreamer` sources: `Kafka`, `S3`, DFS, `JDBC`
    * Schema provider configuration with `DeltaStreamer`
    * Writing to `Hudi` with `Apache Flink`
    * Tuning write performance: parallelism, file sizing, and compaction triggers
<!-- chapter: querying-hudi-tables, duration: 2h -->
* Querying `Hudi` Tables
    * Snapshot queries: reading the latest committed snapshot
    * Read-optimised queries: querying only compacted base files for faster reads
    * Incremental queries: reading only records changed since a given commit
    * Querying `Hudi` tables with `Spark SQL`
    * Querying `Hudi` tables with Hive via `HoodieParquetInputFormat`
    * Querying `Hudi` tables with `Trino` and Presto
    * Querying `Hudi` tables with `AWS Athena`
    * Time travel: querying `Hudi` tables at a specific point in time
<!-- chapter: incremental-processing, duration: 2h -->
* Incremental Processing
    * What is incremental processing and why it is more efficient than full scans
    * Using `Hudi` incremental queries to get changed records since a checkpoint
    * Building incremental `ETL` pipelines with `Spark` and `Hudi`
    * Incremental ingestion from `Kafka` using `DeltaStreamer`
    * Chaining incremental pipelines: propagating changes across multiple `Hudi` tables
    * Incremental processing with `Hudi` and `Apache Flink` for low-latency updates
    * Handling late-arriving data in incremental pipelines
    * Checkpointing and fault tolerance in incremental `Hudi` jobs
<!-- chapter: schema-evolution, duration: 2h -->
* Schema Evolution
    * The importance of schema evolution in long-lived data lake tables
    * `Hudi` schema evolution support: adding, renaming, and dropping columns
    * Schema compatibility modes: backward, forward, and full compatibility
    * Schema registry integration: `Confluent Schema Registry`, `AWS Glue Schema Registry`
    * Evolving schemas with `DeltaStreamer` and `SchemaProvider`
    * Managing schema migrations in production without downtime
    * `Parquet` schema evolution and its interaction with `Hudi` base files
    * Common schema evolution pitfalls and how to avoid them
<!-- chapter: hudi-with-spark-and-flink, duration: 3h -->
* `Hudi` with `Spark` and `Flink`
    * Setting up `Hudi` with `PySpark` and `Scala Spark`
    * `Hudi` `Spark` bundle configuration and dependency management
    * `Spark` `SQL` DDL for creating and altering `Hudi` tables
    * Writing streaming data to `Hudi` with `Spark Structured Streaming`
    * `Hudi Flink` integration: writing `Hudi` tables from `Flink` jobs
    * `Flink` checkpoint integration for exactly-once `Hudi` writes
    * Comparing `Spark` and `Flink` write paths for `Hudi`
    * Best practices for managing `Hudi` table services in `Spark` and `Flink` pipelines
    * Performance benchmarking and tuning tips for large-scale `Hudi` workloads
<!-- chapter: compaction-and-clustering, duration: 2h -->
* Compaction and Clustering
    * Why compaction is necessary for `MoR` tables
    * Inline compaction vs asynchronous compaction strategies
    * Configuring compaction scheduling: commit count and time-based triggers
    * Running compaction as a separate `Spark` job for isolation
    * What is clustering and how it improves query performance
    * Clustering strategies: linear, z-order, and space-filling curves
    * Configuring clustering: sort columns, file size targets, and scheduling
    * Balancing write throughput and read performance through table service tuning
<!-- chapter: hudi-vs-delta-lake-vs-iceberg, duration: 2h -->
* `Hudi` vs `Delta Lake` vs Iceberg
    * Overview of the open table format landscape
    * `Apache Hudi`: strengths in upsert-heavy and CDC-driven workloads
    * `Delta Lake`: strengths in `Spark`-native ecosystems and `Databricks` integration
    * `Apache Iceberg`: strengths in multi-engine support, hidden partitioning, and metadata
    * Comparison matrix: ACID support, schema evolution, time travel, engine compatibility
    * Performance benchmarks and real-world workload considerations
    * Migration paths: moving between table formats
    * Choosing the right table format for your organisation's requirements
<!-- chapter: operations-and-monitoring, duration: 2h -->
* Operations and Monitoring
    * `Hudi CLI`: inspecting table metadata, timeline, and file system view
    * Monitoring `Hudi` table health: file counts, commit age, and compaction lag
    * Cleaning policies: keeping N commits, time-based retention, and incremental queries
    * Archiving the `Hudi` timeline for long-running tables
    * Repairing corrupted `Hudi` tables and rolling back failed commits
    * `Hudi` metrics: `JMX`, `Prometheus`, and `Datadog` reporter integration
    * Operational runbooks: handling compaction failures and stuck jobs
    * `Hudi` upgrade and migration procedures between major versions

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
