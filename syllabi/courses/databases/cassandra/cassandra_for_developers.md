---
tags:
  - tools:cassandra
  - data-and-ai:big-data
level: intermediate
category: database
duration_hours: 24
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: cassandra_for_developers -->
# `Apache Cassandra` for Developers

## Description
`Apache Cassandra` is a highly scalable, distributed `NoSQL` database designed to handle large volumes of data across many commodity servers with no single point of failure. This course equips developers and data scientists with the knowledge and skills to design, build, and optimize applications powered by `Cassandra`. Participants will learn `Cassandra`'s unique architecture, data modeling techniques, and application integration patterns.

The course emphasizes practical data modeling strategies that align with `Cassandra`'s distributed nature, helping participants avoid common pitfalls and build applications that scale effectively.

## Duration
24 hours / 3 days

## Intended Audience
* Application developers building distributed, data-intensive systems
* Data scientists working with large-scale datasets
* Backend engineers designing for high availability and scalability
* Software engineers evaluating `NoSQL` databases for their projects
* Developers migrating from relational databases to `Cassandra`

## Prerequisites
* Proficiency in at least one programming language (`Java`, `Python`, or `JavaScript` preferred)
* Basic understanding of database concepts
* Familiarity with distributed systems concepts is helpful but not required
* Basic command line skills

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)

## Objectives
* Understand `Cassandra`'s distributed architecture and how it achieves high availability
* Design effective data models using partition keys, clustering columns, and denormalization
* Write efficient queries using CQL
* Implement application-level patterns for consistency and performance
* Work with advanced features including collections, UDTs, and lightweight transactions
* Monitor and troubleshoot `Cassandra` clusters
* Integrate `Cassandra` with application code using modern drivers

## Exercises
Hands-on exercises using a multi-node `Cassandra` cluster. Students will design data models for real-world use cases, write CQL queries, build application integrations using `Cassandra` drivers, configure consistency levels, analyze performance with tracing, and use nodetool for cluster inspection. Scenarios cover time-series data, user activity tracking, and product catalog use cases.

## Outline
<!-- chapter: distributed-database-concepts, duration: 1h -->
* Distributed Database Concepts
    * CAP theorem and trade-offs
    * Eventual consistency vs strong consistency
    * Horizontal scaling and data distribution
    * Comparison with relational databases
    * `When` to choose `Cassandra`

<!-- chapter: cassandra-architecture, duration: 2h -->
* `Cassandra` Architecture
    * Ring architecture and consistent hashing
    * Virtual nodes (vnodes)
    * Gossip protocol and failure detection
    * Partitioners and data distribution
    * Snitch configuration
    * Read and write paths
    * Commit log, memtables, and SSTables
    * Compaction strategies

<!-- chapter: cql-fundamentals, duration: 2h -->
* CQL Fundamentals
    * cqlsh and CQL basics
    * Keyspace creation and configuration
    * Table creation and schema definition
    * INSERT, SELECT, UPDATE, DELETE
    * Data types in CQL
    * BATCH statements
    * `ALLOW FILTERING` and its implications

<!-- chapter: data-modeling, duration: 2h -->
* Data Modeling
    * Query-driven data modeling approach
    * Partition keys and data distribution
    * Clustering columns and sort order
    * Compound primary keys
    * Denormalization strategies
    * One-to-many and many-to-many patterns
    * Time-series data modeling
    * Data modeling best practices and anti-patterns

<!-- chapter: collections-and-user-defined-types, duration: 2h -->
* Collections and User-Defined Types
    * Sets, lists, and maps
    * Frozen vs non-frozen collections
    * User-defined types (UDTs)
    * Tuples
    * `When` to use collections vs separate tables
    * Limitations and performance considerations

<!-- chapter: secondary-indexes-and-materialized-views, duration: 2h -->
* Secondary Indexes and Materialized Views
    * Secondary indexes and their limitations
    * SASI indexes
    * Storage-attached indexing
    * Materialized views
    * Materialized view limitations and trade-offs
    * Choosing the right indexing strategy

<!-- chapter: lightweight-transactions, duration: 1h -->
* Lightweight Transactions
    * `IF NOT EXISTS` and IF conditions
    * Compare-and-set semantics
    * Paxos protocol in `Cassandra`
    * Performance implications
    * Use cases and alternatives

<!-- chapter: batch-operations-and-atomicity, duration: 1h -->
* Batch Operations and Atomicity
    * Logged and unlogged batches
    * Counter batches
    * Batch performance implications
    * `When` to use and avoid batches
    * Application-level batching patterns

<!-- chapter: time-to-live-and-data-expiration, duration: 1h -->
* Time-to-Live and Data Expiration
    * `TTL` on columns and rows
    * Default `TTL` on tables
    * `TTL` use cases
    * Interaction with updates

<!-- chapter: tombstones-and-compaction, duration: 2h -->
* Tombstones and Compaction
    * How deletes work in `Cassandra`
    * Tombstone types and lifecycle
    * gc_grace_seconds configuration
    * Compaction strategies: SizeTiered, Leveled, TimeWindow
    * Choosing and tuning compaction
    * Tombstone-related performance issues

<!-- chapter: drivers-and-application-integration, duration: 2h -->
* Drivers and Application Integration
    * DataStax drivers overview
    * Connection and session management
    * Prepared statements
    * Asynchronous query execution
    * Retry policies and speculative execution
    * Load balancing policies
    * Object mapping frameworks
    * Error handling patterns

<!-- chapter: consistency-levels, duration: 2h -->
* Consistency Levels
    * Read and write consistency levels
    * ONE, QUORUM, LOCAL_QUORUM, ALL
    * Consistency level trade-offs
    * Achieving strong consistency
    * Consistency and availability during failures

<!-- chapter: multi-datacenter-replication, duration: 2h -->
* Multi-Datacenter Replication
    * NetworkTopologyStrategy
    * Datacenter-aware consistency levels
    * Cross-datacenter replication mechanics
    * Use cases for multi-datacenter deployment
    * Latency considerations

<!-- chapter: performance-tuning-and-monitoring, duration: 2h -->
* Performance Tuning and Monitoring
    * Query tracing
    * nodetool commands for diagnostics
    * Key performance metrics
    * `JMX` monitoring
    * Identifying and resolving hotspots
    * Read and write optimization techniques
    * Hardware and configuration considerations

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
