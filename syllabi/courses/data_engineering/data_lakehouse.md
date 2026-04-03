---
tags:
  - data-and-ai:data-engineering
  - tools:delta-lake
  - tools:iceberg
  - concepts:data-lakehouse
  - concepts:data-architecture
  - concepts:big-data
level: intermediate
category: data-engineering
duration_hours: 16
audience:
  - audiences:developers
  - audiences:data-engineers
  - audiences:architects
---
<!-- course: data_lakehouse -->
# Data Lakehouse

## Description
The data lakehouse architecture combines the flexibility and cost-efficiency of data lakes with the reliability and performance of data warehouses. This course covers the key technologies and concepts behind the lakehouse paradigm, including `Delta Lake`, `Apache Iceberg`, open table formats, time travel, schema evolution, ACID transactions, and query optimization. Participants will learn how to design, implement, and optimize lakehouse architectures for modern analytical and `machine learning` workloads.

## Duration
16 hours / 2 days

## Intended Audience
* Data engineers designing and building modern data platforms
* Data architects evaluating lakehouse strategies
* Platform engineers managing large-scale data infrastructure
* Analytics engineers working with `Spark`-based data pipelines
* Software engineers transitioning to data-intensive applications

## Prerequisites
* Understanding of data warehousing and data lake concepts
* Familiarity with `SQL` and distributed query engines
* Basic knowledge of `Apache Spark` and `PySpark`
* Understanding of `file` formats (`Parquet`, ORC, `Avro`)
* Familiarity with `cloud storage` (`S3`, `GCS`, `ADLS`)
* Basic understanding of distributed systems concepts

## Objectives
* Understand the lakehouse architecture and its advantages over traditional approaches
* Compare and evaluate open table formats (`Delta Lake`, `Apache Iceberg`, `Apache Hudi`)
* Implement ACID transactions on data lake storage
* Use time travel and versioning for data auditing and rollback
* Design schemas with evolution support for changing business requirements
* Optimize query performance using partitioning, compaction, and data skipping
* Build production-ready lakehouse pipelines with best practices

## Outline
<!-- chapter: introduction-to-the-data-lakehouse-architecture, duration: 1h -->
* Introduction to the Data Lakehouse Architecture
    * Evolution of data architectures: data warehouse, data lake, lakehouse
    * Limitations of traditional data lakes and data warehouses
    * The lakehouse paradigm: combining the best of both worlds
    * Key properties: ACID transactions, schema enforcement, BI support
    * Open table formats and the open data ecosystem
    * Lakehouse reference architecture and components
    * Comparison of lakehouse platforms and engines
<!-- chapter: open-table-formats-overview, duration: 1h -->
* Open Table Formats Overview
    * What are open table formats and why they matter
    * `Delta Lake`, `Apache Iceberg`, and `Apache Hudi` comparison
    * Metadata layers and transaction logs
    * `File` organization and manifest structures
    * Community adoption and ecosystem support
    * Interoperability and format conversion
    * Choosing the right table format for your use case
<!-- chapter: delta-lake, duration: 2h -->
* `Delta Lake`
    * `Delta Lake` architecture and design principles
    * The transaction log (_delta_log)
    * Creating and managing Delta tables
    * ACID transactions and concurrency control
    * Schema enforcement and schema evolution
    * Time travel with versioning
    * MERGE, UPDATE, and DELETE operations
    * `Change Data Feed` for downstream consumers
    * `Delta Lake` on `Spark`, `Flink`, and standalone readers
    * `Delta Sharing` for secure data sharing
<!-- chapter: apache-iceberg, duration: 2h -->
* `Apache Iceberg`
    * `Iceberg` architecture and table specification
    * Metadata tree: snapshots, manifests, and manifest lists
    * Creating and managing `Iceberg` tables
    * ACID transactions and snapshot isolation
    * Schema evolution: adding, dropping, renaming, and reordering columns
    * Partition evolution without rewriting data
    * Time travel and snapshot management
    * Hidden partitioning and partition transforms
    * `Iceberg` with `Spark`, `Trino`, `Flink`, and other engines
    * Catalog integration (`Hive Metastore`, `AWS Glue`, Nessie)
<!-- chapter: acid-transactions-on-data-lakes, duration: 2h -->
* ACID Transactions on Data Lakes
    * Why ACID matters for data lakes
    * Optimistic concurrency control
    * Conflict resolution strategies
    * Write-ahead logs and commit protocols
    * Serializable and snapshot isolation levels
    * Handling concurrent readers and writers
    * Transaction guarantees across different engines
<!-- chapter: time-travel-and-data-versioning, duration: 2h -->
* Time Travel and Data Versioning
    * Understanding data versioning in lakehouse formats
    * Querying historical snapshots by version and timestamp
    * Use cases: auditing, debugging, regulatory compliance
    * Rolling back to previous versions
    * Retention policies and snapshot expiration
    * Storage cost implications of versioning
    * Implementing data lineage with versioning
<!-- chapter: schema-evolution-and-data-management, duration: 2h -->
* Schema Evolution and Data Management
    * Schema-on-read vs schema-on-write
    * Adding, removing, and modifying columns
    * Type promotion and widening rules
    * Partition evolution strategies
    * Handling backward and forward compatibility
    * Data migration patterns for schema changes
    * Metadata management and governance
<!-- chapter: query-optimization-and-performance-tuning, duration: 2h -->
* Query Optimization and Performance Tuning
    * Data layout optimization: Z-ordering, clustering, sorting
    * `File` compaction and small `file` problem
    * Data skipping with column statistics
    * Partition pruning strategies
    * Predicate pushdown and filter optimization
    * Caching strategies for frequently accessed data
    * Optimizing read and write performance
    * Benchmarking and performance monitoring
<!-- chapter: production-patterns-and-best-practices, duration: 2h -->
* Production Patterns and Best Practices
    * Medallion architecture: bronze, silver, gold layers
    * Streaming and batch ingestion patterns
    * CDC (Change Data Capture) integration
    * Data quality enforcement and validation
    * Lakehouse governance and access control
    * Cost management and storage optimization
    * Monitoring and observability for lakehouse workloads
    * Migration strategies from existing data platforms

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
