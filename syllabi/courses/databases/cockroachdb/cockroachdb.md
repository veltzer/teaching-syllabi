---
tags:
  - databases:cockroachdb
  - databases:distributed-sql
  - databases:relational
  - databases:cloud-native
level: intermediate
category: database
duration_hours: 24
audience:
  - audiences:developers
  - audiences:architects
  - audiences:dbas
---
<!-- course: cockroachdb -->
# `CockroachDB`

## Description
`CockroachDB` is a cloud-native distributed `SQL` database engineered for horizontal scalability, strong consistency, and automatic resilience to node and datacenter failures. Drawing its name from the cockroach's legendary survivability, it provides full `PostgreSQL`-compatible `SQL` while transparently distributing data across nodes and regions. This course equips developers, architects, and DBAs with the knowledge to deploy, operate, and build applications on `CockroachDB`. Participants will explore its unique architecture, understand how distributed transactions achieve serializable isolation, and learn best practices for schema design, multi-region topologies, and operational management.

## Duration
24 hours / 3 days

## Intended Audience
* Application developers building globally distributed or highly available systems
* Database architects evaluating distributed `SQL` for `microservices` and cloud-native platforms
* Database administrators managing or migrating to `CockroachDB`
* Engineers who need `PostgreSQL` compatibility with horizontal scaling
* Site reliability engineers responsible for database resilience and operations

## Prerequisites
* Working knowledge of `SQL` and relational database concepts
* Familiarity with distributed systems concepts is helpful
* Basic `Linux` command-line skills
* Experience with `PostgreSQL` or another relational database is advantageous

## Objectives
* Understand `CockroachDB`'s distributed `SQL` architecture and consensus protocol
* Deploy single-node and multi-node `CockroachDB` clusters locally and in the cloud
* Use `CockroachDB`'s `SQL` dialect including `PostgreSQL`-compatible extensions
* Design schemas that distribute data efficiently across nodes
* Work with `CockroachDB` transactions and understand its isolation guarantees
* Build effective indexing strategies including partial and expression indexes
* Configure multi-region deployments with survival goals and table locality
* Use changefeeds for CDC (Change Data Capture) integration
* Tune and monitor cluster performance using the DB Console and metrics
* Plan and execute cluster operations including upgrades and scaling

## Exercises
Hands-on labs using local `CockroachDB` clusters provisioned with `Docker Compose` or the `cockroach` binary. Students will create a multi-node cluster, model schemas for distributed access patterns, execute transactions and observe isolation behaviors, configure geo-partitioned and regional-by-row tables, set up changefeeds to `Kafka`, analyze query plans, and use the DB Console for performance investigation. Scenarios cover multi-tenant `SaaS`, e-commerce, and globally distributed application patterns.

## Outline
<!-- chapter: introduction-to-distributed-sql, duration: 2h -->
* Introduction to Distributed `SQL`
    * The CAP and PACELC theorems in practice
    * NewSQL and distributed `SQL` compared to `NoSQL`
    * Horizontal scaling vs vertical scaling for OLTP
    * Strong consistency vs eventual consistency trade-offs
    * How `CockroachDB` achieves global ACID transactions
    * Comparison with Spanner, `YugabyteDB`, and `TiDB`

<!-- chapter: cockroachdb-architecture, duration: 2h -->
* `CockroachDB` Architecture
    * Layered architecture: `SQL`, transactions, distribution, replication, storage
    * Ranges: the fundamental unit of data distribution
    * Raft consensus protocol for range replication
    * Leaseholder model and read/write paths
    * MVCC (Multi-Version Concurrency Control)
    * The Pebble storage engine
    * Gateway nodes, KV layer, and `DistSQL`

<!-- chapter: installation-and-cluster-setup, duration: 1h -->
* Installation and Cluster Setup
    * Installing `CockroachDB` binary and `Docker` image
    * Starting a single-node cluster for development
    * Bootstrapping a secure multi-node cluster
    * Joining nodes and cluster initialization
    * The DB Console overview and cluster topology view
    * `CockroachDB` Cloud (Serverless and Dedicated) overview

<!-- chapter: sql-compatibility-and-extensions, duration: 3h -->
* `SQL` Compatibility and Extensions
    * `PostgreSQL` wire protocol compatibility
    * Supported and unsupported `PostgreSQL` features
    * `CockroachDB`-specific `SQL` extensions
    * Serial types and unique `IDs`: UUID, sequences, and `gen_random_uuid()`
    * Arrays, JSONB, and spatial types
    * `CockroachDB` `SQL` shell (`cockroach sql`) usage
    * Connecting with `psql`, `pgAdmin`, and Hibernate

<!-- chapter: data-types-and-schemas, duration: 2h -->
* Data Types and Schemas
    * Choosing primary keys for distributed performance: UUIDs vs sequential `IDs`
    * The hotspot problem with sequential primary keys
    * Schema design for even data distribution
    * Column families for reducing read amplification
    * Computed columns and virtual computed columns
    * Schema changes and online DDL in `CockroachDB`
    * `cockroach` schema change best practices

<!-- chapter: transactions-and-isolation, duration: 3h -->
* Transactions and Isolation
    * `CockroachDB`'s serializable isolation level
    * Transaction retries and client-side retry loops
    * Optimistic vs pessimistic locking in `CockroachDB`
    * Savepoints for nested transaction simulation
    * Transaction contention and the contention metrics
    * Follower reads and AS OF SYSTEM TIME
    * Read committed isolation (when to use it)
    * Debugging transaction conflicts with the DB Console

<!-- chapter: indexing-strategies, duration: 2h -->
* Indexing Strategies
    * Primary index and secondary indexes in distributed context
    * Index back-fills and online index creation
    * Partial indexes for filtered workloads
    * Expression indexes
    * Covering indexes and index-only scans
    * Inverted indexes for JSONB and arrays
    * Multi-column index column ordering
    * Analyzing query plans with EXPLAIN and `EXPLAIN ANALYZE`

<!-- chapter: multi-region-deployment, duration: 3h -->
* Multi-Region Deployment
    * Multi-region architecture concepts in `CockroachDB`
    * Regions and survival goals: zone vs region survival
    * Table locality modes: REGIONAL BY TABLE, REGIONAL BY ROW, GLOBAL
    * Non-voting replicas for fast reads
    * Super regions for data domiciling and compliance
    * Geo-partitioned replicas with partition zone configs
    * Latency tradeoffs for multi-region writes
    * Testing multi-region behavior in a local demo cluster

<!-- chapter: changefeeds-and-cdc, duration: 2h -->
* Changefeeds and CDC
    * What are changefeeds and Change Data Capture use cases
    * Core changefeeds for simple streaming
    * Enterprise changefeeds with `Kafka` and `cloud storage` sinks
    * Changefeed message formats: `JSON` and `Avro`
    * Filtering and transformation options
    * At-least-once delivery and idempotency handling
    * Monitoring changefeed performance and lag

<!-- chapter: performance-tuning, duration: 2h -->
* Performance Tuning
    * Identifying slow queries with the Statement Activity page
    * Index recommendations from the DB Console
    * Query plan diagrams and distribution details
    * Controlling query plans with hints
    * Connection pooling with `PgBouncer` and `pgx`
    * Bulk operations: IMPORT, EXPORT, and `COPY`
    * Resource governors and admission control

<!-- chapter: operations-and-monitoring, duration: 2h -->
* Operations and Monitoring
    * Rolling upgrades and version compatibility
    * Adding and decommissioning nodes safely
    * `Prometheus` metrics and `Grafana` dashboards
    * Key metrics: QPS, latency, range count, under-replicated ranges
    * Backup and restore with `BACKUP` and `RESTORE`
    * Point-in-time recovery
    * Cluster log collection and debug `zip`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
