---
tags:
  - databases:scylladb
  - databases:cassandra
  - databases:nosql
  - databases:wide-column
  - tools:scylladb
level: intermediate
category: database
duration_hours: 24
audience:
  - audiences:developers
  - audiences:architects
  - audiences:dbas
---
<!-- course: scylladb -->
# `ScyllaDB`

## Description
`ScyllaDB` is a high-performance, `Apache Cassandra`-compatible wide-column `NoSQL` database rebuilt in `C++` around a shard-per-core architecture that dramatically reduces latency and increases throughput compared to `Cassandra`. Designed to handle millions of operations per second on commodity hardware, `ScyllaDB` is used by organizations that `require` ultra-low latency at massive scale. This course covers `ScyllaDB`'s architecture, data modeling philosophy, CQL usage, operational management, and performance tuning. Participants will also learn about `ScyllaDB`'s unique capabilities including the Alternator `DynamoDB`-compatible `API`, materialized views, and advanced compaction strategies.

## Duration
24 hours / 3 days

## Intended Audience
* Backend developers building high-throughput, low-latency data services
* Database architects designing large-scale distributed storage solutions
* DBAs managing `ScyllaDB` or `Apache Cassandra` clusters
* Engineers planning migrations from `Cassandra` to `ScyllaDB`
* Platform engineers evaluating `NoSQL` databases for real-time workloads

## Prerequisites
* `Solid` understanding of distributed systems concepts
* Working knowledge of at least one programming language (`Java`, `Python`, or `Go`)
* Familiarity with relational database concepts and `SQL`
* Basic `Linux` system administration skills
* Prior experience with `Cassandra` or another `NoSQL` database is beneficial

## Objectives
* Understand `ScyllaDB`'s shard-per-core architecture and how it differs from `Cassandra`
* Model data effectively for `ScyllaDB`'s distributed, partitioned storage
* Write efficient CQL queries and use `ScyllaDB` drivers correctly
* Choose and configure appropriate compaction strategies for different workloads
* Configure replication, consistency levels, and understand their trade-offs
* Use secondary indexes and materialized views appropriately
* Tune `ScyllaDB` performance at hardware, OS, and database configuration levels
* Monitor cluster health and diagnose operational issues
* Plan and execute migrations from `Apache Cassandra` to `ScyllaDB`
* Use the Alternator `API` for `DynamoDB`-compatible workloads

## Exercises
Hands-on labs using a multi-node `ScyllaDB` cluster provisioned with `Docker Compose`. Students will design and implement data models for real-world use cases, execute CQL from the `cqlsh` shell and `Python` driver, configure compaction strategies and observe their effects, set consistency levels and observe trade-offs, create materialized views, use `scyllatop` and `nodetool` for monitoring, run benchmarks with `cassandra-stress`, and practice a rolling migration from `Cassandra`. Scenarios include user activity feeds, IoT telemetry, and leaderboard systems.

## Outline
<!-- chapter: introduction-to-scylladb, duration: 2h -->
* Introduction to `ScyllaDB`
    * The scalability and latency challenges `ScyllaDB` addresses
    * `ScyllaDB` vs `Apache Cassandra`: architectural differences and compatibility
    * `ScyllaDB` vs `DynamoDB` and other wide-column stores
    * `ScyllaDB` Open Source, Enterprise, and Cloud editions
    * Key use cases: real-time analytics, IoT, ad tech, and gaming leaderboards
    * `ScyllaDB` ecosystem: drivers, tools, and integrations

<!-- chapter: architecture-and-shard-per-core, duration: 2h -->
* Architecture and the Shard-per-Core Model
    * Seastar framework and asynchronous, non-blocking `I/O`
    * Shard-per-core: how each `CPU` core owns its data shards
    * Elimination of thread contention and lock overhead
    * Ring architecture and consistent hashing (token ring)
    * Virtual nodes (vnodes) in `ScyllaDB`
    * Gossip protocol and failure detection
    * Read and write paths through the cluster
    * Memtables, SSTables, and the commit log

<!-- chapter: data-modeling-for-scylladb, duration: 3h -->
* Data Modeling for `ScyllaDB`
    * Query-first data modeling approach
    * Partition keys, clustering keys, and their role
    * Wide rows and time-series data patterns
    * Denormalization and data duplication strategies
    * One-to-many and many-to-many modeling patterns
    * Avoiding hotspot partitions
    * Anti-patterns: large partitions, excessive tombstones
    * Data modeling tools and validation techniques

<!-- chapter: cql-and-driver-usage, duration: 3h -->
* CQL and Driver Usage
    * CQL syntax: keyspace and table creation
    * INSERT, SELECT, UPDATE, DELETE with partition and clustering key constraints
    * CQL collections: sets, lists, and maps
    * User-defined types (UDTs) and frozen types
    * Lightweight transactions with IF conditions
    * BATCH operations: logged and unlogged
    * `ScyllaDB` `Python` driver: session management and prepared statements
    * Asynchronous query execution and paging
    * Token-aware and latency-aware load balancing policies

<!-- chapter: compaction-strategies, duration: 2h -->
* Compaction Strategies
    * Why compaction is necessary: SSTables and read amplification
    * SizeTieredCompactionStrategy (STCS): for write-heavy workloads
    * LeveledCompactionStrategy (LCS): for read-heavy workloads
    * TimeWindowCompactionStrategy (TWCS): for time-series data
    * IncrementalCompactionStrategy (ICS): `ScyllaDB`-specific improvement
    * Choosing the right strategy for your access patterns
    * Compaction throughput and `I/O` throttling

<!-- chapter: consistency-levels-and-replication, duration: 2h -->
* Consistency Levels and Replication
    * Replication factor and `NetworkTopologyStrategy`
    * Consistency levels: ANY, ONE, QUORUM, LOCAL_QUORUM, EACH_QUORUM, ALL
    * Read vs write consistency trade-offs
    * Tunable consistency and availability during failures
    * Hinted handoff and repair
    * `nodetool repair` and incremental repair in `ScyllaDB`
    * Multi-datacenter replication patterns

<!-- chapter: secondary-indexes-and-materialized-views, duration: 2h -->
* Secondary Indexes and Materialized Views
    * Local secondary indexes and their scoped behavior in `ScyllaDB`
    * Global secondary indexes
    * Limitations of secondary indexes in distributed systems
    * Materialized views: definition and automatic maintenance
    * Trade-offs of materialized views: write amplification
    * `ScyllaDB` filtering: `ALLOW FILTERING` and `when` it is safe
    * Choosing between index, view, and denormalization

<!-- chapter: performance-tuning, duration: 3h -->
* Performance Tuning
    * Hardware selection: `CPU`, NVMe SSDs, and network
    * OS tuning: `ScyllaDB` setup scripts and kernel parameters
    * `JVM`-free operation and reduced GC pauses
    * `ScyllaDB` configuration: `scylla.yaml` key parameters
    * Monitoring with `Prometheus` and `Grafana ScyllaDB` dashboards
    * Using `scyllatop` and `nodetool tpstats` for real-time diagnostics
    * Benchmarking with `cassandra-stress`
    * Identifying and resolving hot partitions
    * Read vs write path tuning

<!-- chapter: operations-and-monitoring, duration: 2h -->
* Operations and Monitoring
    * `ScyllaDB` cluster topology management with `nodetool`
    * Adding and removing nodes with `bootstrap` and decommission
    * Rolling upgrades between `ScyllaDB` versions
    * Backup and restore with `scylla-manager`
    * `ScyllaDB` Manager for automated scheduling
    * Key operational metrics and alerting thresholds
    * Diagnosing performance issues with tracing

<!-- chapter: migration-from-cassandra, duration: 2h -->
* Migration from `Cassandra`
    * Compatibility between `ScyllaDB` and `Apache Cassandra`
    * Live migration using the `ScyllaDB` Migrator
    * Offline migration via SSTable export and import
    * Driver compatibility: using existing `Cassandra` client code
    * Schema and configuration differences to review before migration
    * Testing and validation strategies
    * Rollback planning

<!-- chapter: alternator-dynamodb-compatible-api, duration: 1h -->
* Alternator: `DynamoDB`-Compatible `API`
    * What is Alternator and its use cases
    * Enabling and configuring the Alternator endpoint
    * Using `DynamoDB` SDKs with `ScyllaDB` Alternator
    * Data model mapping between `DynamoDB` and CQL
    * Limitations and behavioral differences
    * Migration from `DynamoDB` to `ScyllaDB`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
