---
tags:
  - tools:mysql
  - databases:sql
  - practices:performance
  - practices:tuning
level: advanced
category: database
duration_hours: 16
audience:
  - audiences:dbas
  - audiences:developers
  - audiences:performance-engineers
---
<!-- course: mysql_performance_tuning -->
# `MySQL` Performance Tuning

## Description
This advanced course provides comprehensive training in `MySQL` performance optimization, covering query tuning, indexing strategies, and server configuration. Participants will learn to diagnose and resolve performance bottlenecks using EXPLAIN plan analysis, `Performance Schema`, and the sys schema. The course addresses both query-level and system-level optimization techniques for InnoDB-based deployments.

The course emphasizes practical, data-driven approaches to performance tuning, enabling participants to systematically identify and resolve the most impactful performance issues in production `MySQL` environments.

## Duration
16 hours / 2 days

## Intended Audience
* Database administrators responsible for `MySQL` performance
* Backend developers writing and optimizing `SQL` queries
* Performance engineers conducting database assessments
* `DevOps` engineers managing `MySQL` infrastructure

## Prerequisites
* Working knowledge of `SQL` and relational database concepts
* Experience administering or developing against `MySQL`
* Basic understanding of `Linux` operating system
* Familiarity with InnoDB storage engine

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Analyze and optimize `SQL` queries using EXPLAIN plans
* Design effective indexing strategies for various workloads
* Understand InnoDB internals and tune the buffer pool
* Use `Performance Schema` and sys schema for diagnostics
* Identify and resolve slow queries through log analysis
* Apply schema optimization techniques for performance
* Implement partitioning strategies for large datasets
* Configure connection pooling for high-concurrency environments

## Outline
<!-- chapter: query-optimization, duration: 1h -->
* Query Optimization
    * Query execution lifecycle in `MySQL`
    * Optimizer behavior and cost-based decisions
    * Query rewriting techniques
    * Subquery optimization
    * Join optimization strategies
    * Prepared statements and performance
<!-- chapter: explain-plan-analysis, duration: 1h -->
* EXPLAIN Plan Analysis
    * Reading EXPLAIN output
    * `EXPLAIN ANALYZE` for execution profiling
    * Understanding access types and their performance implications
    * Identifying full table scans and inefficient joins
    * Using `EXPLAIN FORMAT=JSON` and `FORMAT=TREE`
    * Visual explain tools
<!-- chapter: indexing-strategies, duration: 2h -->
* Indexing Strategies
    * B-tree index internals and usage patterns
    * Composite index design and column ordering
    * Covering indexes
    * Full-text indexes
    * Spatial indexes
    * Index condition pushdown
    * Invisible indexes for safe testing
    * Index maintenance and overhead considerations
<!-- chapter: innodb-internals, duration: 2h -->
* InnoDB Internals
    * InnoDB architecture overview
    * Clustered index and secondary indexes
    * Row format and page structure
    * MVCC and transaction isolation
    * Undo logs and redo logs
    * Adaptive hash index
    * Change buffering
<!-- chapter: buffer-pool-tuning, duration: 1h -->
* Buffer Pool Tuning
    * Buffer pool sizing and configuration
    * Multiple buffer pool instances
    * Buffer pool dump and reload
    * Monitoring buffer pool hit ratio
    * Page flushing and dirty page management
    * LRU algorithm and midpoint insertion
<!-- chapter: query-cache, duration: 1h -->
* Query Cache
    * Query cache behavior and limitations
    * `When` to enable and disable query cache
    * Alternatives to query cache in `MySQL` 8.0
    * Application-level caching strategies
    * Using ProxySQL for query caching
<!-- chapter: slow-query-log-analysis, duration: 1h -->
* Slow Query Log Analysis
    * Configuring the slow query log
    * Setting appropriate thresholds
    * Using mysqldumpslow for log analysis
    * pt-query-digest for advanced analysis
    * Identifying `top` offending queries
    * Long-running query management
<!-- chapter: performance-schema, duration: 1h -->
* `Performance Schema`
    * `Performance Schema` architecture
    * Instruments, consumers, and events
    * Statement and stage analysis
    * Wait event analysis
    * Memory instrumentation
    * Configuring for minimal overhead
<!-- chapter: sys-schema, duration: 1h -->
* sys Schema
    * Overview of sys schema views
    * Finding unused indexes
    * Identifying redundant indexes
    * Host and user activity summaries
    * Statement analysis views
    * `I/O` analysis views
<!-- chapter: schema-optimization, duration: 2h -->
* Schema Optimization
    * Data type selection for performance
    * Normalization vs denormalization trade-offs
    * Column and row size optimization
    * Table compression
    * Generated columns for optimization
    * Temporary table optimization
<!-- chapter: partitioning-for-performance, duration: 1h -->
* Partitioning for Performance
    * Partition types (RANGE, LIST, HASH, KEY)
    * Partition pruning and its impact on queries
    * Partitioning large tables
    * Partition maintenance operations
    * `When` partitioning helps and `when` it does not
<!-- chapter: connection-pooling, duration: 2h -->
* Connection Pooling
    * Connection overhead in `MySQL`
    * `MySQL` thread pool plugin
    * Application-side connection pooling
    * ProxySQL for connection management
    * Monitoring connection usage
    * Tuning max_connections and related variables

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
