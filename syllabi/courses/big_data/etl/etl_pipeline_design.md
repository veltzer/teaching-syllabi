---
tags:
  - data-and-ai:etl
  - data-and-ai:big-data
  - concepts:architecture
level: intermediate
category: big-data
duration_hours: 16
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: etl_pipeline_design -->
# `ETL` Pipeline Design

## Description
This course covers the design and implementation of robust `ETL` and `ELT` data pipelines. Participants
will learn pipeline architecture patterns for batch, micro-batch, and streaming workloads, as well as
data extraction, transformation, and loading strategies. The course explores orchestration tools
such as `Airflow`, `Prefect`, and `Dagster`, and covers critical production concerns including error
handling, idempotency, data validation, schema evolution, monitoring, and performance optimization.

## Duration
16 hours / 2 days

## Intended Audience
* software developers building data integration pipelines
* data scientists who need to manage data preparation workflows

## Prerequisites
* Proficiency in `Python` or `SQL`
* Basic understanding of databases and data warehouses
* Familiarity with `REST` APIs and file formats (`CSV`, `JSON`, `Parquet`)
* Experience with version control (`Git`)

## Required Knowledge
* `Python` Programming (or equivalent experience)

## Objectives
* **Design pipeline architectures** for batch, micro-batch, streaming, `lambda`, and kappa patterns
* **Implement data extraction strategies** from APIs, databases, files, and change data capture sources
* **Apply transformation patterns** for cleaning, enrichment, aggregation, and normalization
* **Configure orchestration tools** including `Airflow`, `Prefect`, and `Dagster` for pipeline scheduling and management
* **Build production-grade pipelines** with error handling, idempotency, retry logic, and monitoring
* **Optimize pipeline performance** with partitioning, parallelism, and incremental processing

## Outline
<!-- chapter: etl-vs-elt-concepts, duration: 1h -->
* `ETL` vs `ELT` Concepts
    * Traditional `ETL`
        * Extract, transform, load workflow
        * `When` to use `ETL`
        * `ETL` tool landscape
    * Modern `ELT`
        * Extract, load, transform workflow
        * Leveraging warehouse compute
        * `ELT` advantages and trade-offs
    * Hybrid approaches
        * Combining `ETL` and `ELT`
        * Choosing the right approach
        * Cost and complexity considerations
<!-- chapter: pipeline-architecture-patterns, duration: 2h -->
* Pipeline Architecture Patterns
    * Batch processing
        * Scheduled batch jobs
        * Full refresh vs incremental
        * Batch sizing strategies
    * Micro-batch processing
        * Near real-time patterns
        * Small batch intervals
        * Trade-offs with true streaming
    * Streaming processing
        * Event-driven architectures
        * Stream processing frameworks
        * Exactly-once semantics
    * `Lambda` architecture
        * Batch and speed layers
        * Serving layer
        * Pros and cons
    * Kappa architecture
        * Stream-only processing
        * Reprocessing from log
        * Simplification benefits
<!-- chapter: data-extraction, duration: 2h -->
* Data Extraction
    * `API` extraction
        * `REST` `API` pagination
        * Rate limiting and throttling
        * Authentication handling
        * Incremental `API` extraction
    * Database extraction
        * Full table extraction
        * Query-based extraction
        * Parallel extraction
        * Connection management
    * `File` extraction
        * `File` format handling (`CSV`, `JSON`, `Parquet`, `Avro`)
        * `File` system scanning
        * Compressed file handling
        * Large file processing
    * Change data capture
        * Log-based CDC
        * Trigger-based CDC
        * Timestamp-based CDC
        * CDC tools (`Debezium`, `Fivetran`)
<!-- chapter: transformation-patterns, duration: 2h -->
* Transformation Patterns
    * Data cleaning
        * Null handling
        * Deduplication
        * Data type casting
        * String normalization
    * Data enrichment
        * Lookup joins
        * Geocoding and reverse lookups
        * External data integration
        * Derived columns
    * Aggregation
        * Grouping and summarization
        * Rolling aggregations
        * Window functions
        * Approximate aggregations
    * Normalization and denormalization
        * Schema normalization patterns
        * Star and `snowflake` schemas
        * Flattening nested structures
        * Pivoting and unpivoting
<!-- chapter: data-loading-strategies, duration: 1h -->
* Data Loading Strategies
    * Full load
        * Truncate and reload
        * Swap table patterns
        * Use cases and limitations
    * Incremental load
        * Timestamp-based incremental
        * Watermark tracking
        * High watermark patterns
        * Gap detection
    * Upsert (merge)
        * Merge patterns
        * Slowly changing dimensions
        * SCD Type 1 and Type 2
        * Conflict resolution
    * Partitioned loading
        * Partition-level replacement
        * Dynamic partitioning
        * Partition pruning
<!-- chapter: orchestration-tools, duration: 1h -->
* Orchestration Tools
    * `Apache Airflow`
        * DAG definition and structure
        * Operators and sensors
        * Scheduling and dependencies
        * XComs and task communication
    * `Prefect`
        * Flow and task design
        * Dynamic workflows
        * `Prefect` Cloud and Server
        * Deployment and scheduling
    * `Dagster`
        * Software-defined assets
        * Op and job abstractions
        * IO managers
        * Observability features
    * Tool comparison
        * Feature comparison
        * Community and ecosystem
        * Operational considerations
<!-- chapter: error-handling-and-retry, duration: 1h -->
* Error Handling and Retry
    * Error handling strategies
        * Dead letter queues
        * Error logging and classification
        * Partial failure handling
        * Circuit breaker pattern
    * Retry mechanisms
        * Retry policies (fixed, exponential backoff)
        * Retry limits and escalation
        * Idempotent retries
    * Failure recovery
        * Checkpoint and restart
        * Pipeline rollback
        * Manual intervention procedures
<!-- chapter: idempotency, duration: 1h -->
* Idempotency
    * Idempotency principles
        * What makes a pipeline idempotent
        * Deterministic processing
        * Rerunnable pipelines
    * Implementation patterns
        * Partition-based idempotency
        * Upsert-based idempotency
        * Staging table patterns
        * Transaction-based approaches
<!-- chapter: data-validation, duration: 1h -->
* Data Validation
    * Input validation
        * Schema validation
        * Data type checks
        * Range and constraint checks
        * Referential integrity checks
    * Output validation
        * Row count reconciliation
        * Aggregate checks
        * Quality score thresholds
        * Anomaly detection
    * Validation frameworks
        * Integrating `Great Expectations`
        * Custom validation functions
        * Alert and notification on failure
<!-- chapter: monitoring-and-alerting, duration: 1h -->
* Monitoring and Alerting
    * Pipeline monitoring
        * Execution status tracking
        * Duration and SLA monitoring
        * Resource utilization
        * Data freshness tracking
    * Alerting strategies
        * Alert channels and escalation
        * Alert fatigue prevention
        * Severity levels
        * On-call procedures
    * Observability
        * Logging best practices
        * Metrics collection
        * Distributed tracing
        * Dashboard design
<!-- chapter: testing-pipelines, duration: 1h -->
* Testing Pipelines
    * Unit testing
        * Testing transformation logic
        * Mocking data sources
        * Assertion patterns
    * Integration testing
        * End-to-end pipeline tests
        * Test environments and fixtures
        * Data subset testing
    * Regression testing
        * Output comparison
        * Schema change detection
        * Performance regression
<!-- chapter: schema-evolution, duration: 1h -->
* Schema Evolution
    * Schema change types
        * Additive changes
        * Destructive changes
        * Type changes
    * Handling schema evolution
        * Schema-on-read vs schema-on-write
        * Forward and backward compatibility
        * Schema registry integration
    * Migration strategies
        * Automated schema migration
        * Dual-write patterns
        * Backfill procedures
<!-- chapter: performance-optimization, duration: 1h -->
* Performance Optimization
    * Extraction optimization
        * Parallel extraction
        * Pushdown predicates
        * Incremental extraction
    * Transformation optimization
        * Pushdown optimization
        * Partition-aware processing
        * Memory management
        * Caching intermediate results
    * Loading optimization
        * Bulk loading techniques
        * Parallel loading
        * Index management during loads
        * Compression strategies

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
