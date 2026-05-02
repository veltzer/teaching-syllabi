---
tags:
  - concepts:databases
  - concepts:database-design
  - concepts:persistence
  - concepts:distributed-systems
  - concepts:acid
  - concepts:eventual-consistency
  - concepts:performance
level: advanced
category: database
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:dbas
  - audiences:architects
---
<!-- course: database_internals -->
# Database Internals

## Description
Databases are the most heavily engineered piece of software most developers will ever depend on, and they are also
the most opaque. This five day course opens the box. It is not a course about how to use any specific database; it is
a course about what every relational and `NoSQL` system is doing under the hood and why.

The course follows the lifecycle of a query, from the moment it arrives over the wire until results land back at the
client. Along the way it covers storage layout (B-trees vs `LSM`-trees), buffer management, write-ahead logging,
transaction isolation and `MVCC`, query planning and join algorithms, replication topologies, consensus, and the
trade-offs that `make` a database fast, durable, consistent or available. Participants leave able to read database
documentation critically, debug production performance issues from first principles, and `make` informed choices between
`PostgreSQL`, `MySQL`, `Cassandra`, `RocksDB`, `CockroachDB` and similar systems.

## Duration
40 hours / 5 days

## Intended Audience
* senior developers who depend on databases and want to understand them
* `DBAs` who want a deeper theoretical foundation under their day-to-day operational work
* architects choosing between database technologies for new systems
* engineers who are debugging production database performance issues

## Prerequisites
* `solid` `SQL` and at least basic exposure to one relational and one `NoSQL` database
* basic operating systems literacy (files, page cache, memory hierarchy)
* basic understanding of data structures (`B-tree`, hash table, tree)

## Objectives
* explain the path of a query through a database from socket to result
* compare storage engine families and their performance trade-offs
* reason about transaction isolation, anomalies and `MVCC`
* understand write-ahead logging, recovery and durability
* analyze query plans and the cost models behind them
* compare replication and consensus mechanisms
* read source code and documentation of real database systems
* `make` informed architectural decisions between database options

## Outline
<!-- chapter: anatomy-of-a-database, duration: 2h -->
* Anatomy of a database
    * the layered architecture of a typical database
    * client protocol, parser, planner, executor, storage
    * the path of a `SELECT` and the path of an `INSERT`
    * what is shared between relational and `NoSQL` engines
    * what differs between them
<!-- chapter: storage-fundamentals, duration: 3h -->
* Storage fundamentals
    * pages, blocks and the unit of `IO`
    * heap files and slotted pages
    * row stores vs column stores
    * `TOAST`, large objects and out-of-line storage
    * data file layout in `PostgreSQL` and `MySQL`/`InnoDB`
    * the page cache and the database buffer pool
<!-- chapter: b-trees-in-depth, duration: 3h -->
* `B-trees` in depth
    * `B-tree` and `B+tree` structure
    * splits, merges and rebalancing
    * `latch` coupling and concurrent traversal
    * fill factor and page splits in practice
    * index-organized tables vs heap with secondary indexes
    * covering and partial indexes
<!-- chapter: lsm-trees-and-write-optimized-storage, duration: 3h -->
* `LSM`-trees and write-optimized storage
    * write amplification, read amplification, space amplification
    * `MemTable`, `SSTable`, levels and tiers
    * compaction strategies: leveled, size-tiered, universal
    * bloom filters and read path optimization
    * `RocksDB`, `Cassandra` and `ScyllaDB` storage engines
    * when `LSM` beats `B-tree` and when it loses
<!-- chapter: buffer-management-and-page-cache, duration: 2h -->
* Buffer management and page cache
    * the buffer pool's role
    * replacement policies: `LRU`, 2Q, clockpro, `ARC`
    * dirty pages, checkpoints and background writers
    * direct `IO` vs the operating system page cache
    * memory pressure and eviction storms
<!-- chapter: write-ahead-logging-and-recovery, duration: 3h -->
* Write-ahead logging and recovery
    * the durability problem
    * `WAL` design and `fsync` discipline
    * `ARIES` recovery protocol
    * checkpointing strategies
    * group commit and pipelined `WAL` writes
    * `WAL` in `PostgreSQL`, `MySQL` and `RocksDB`
<!-- chapter: transactions-and-isolation-levels, duration: 3h -->
* Transactions and isolation levels
    * `ACID` revisited
    * the `SQL` standard isolation levels and their anomalies
    * dirty read, non-repeatable read, phantom read, write skew
    * read-committed, repeatable-read, serializable
    * snapshot isolation and its anomalies
    * serializable snapshot isolation
<!-- chapter: mvcc-and-concurrency-control, duration: 3h -->
* `MVCC` and concurrency control
    * pessimistic vs optimistic concurrency control
    * two-phase locking and deadlock detection
    * `MVCC` row versioning
    * `MVCC` implementation in `PostgreSQL` (xmin/xmax, `vacuum`)
    * `MVCC` implementation in `MySQL`/`InnoDB` (undo logs)
    * long-running transactions and bloat
<!-- chapter: query-parsing-and-planning, duration: 3h -->
* Query parsing and planning
    * lexer, parser, semantic analyzer
    * relational algebra and logical plans
    * physical plans and access paths
    * cost-based optimization
    * statistics, histograms and selectivity estimation
    * plan caching and prepared statements
<!-- chapter: join-and-aggregation-algorithms, duration: 3h -->
* Join and aggregation algorithms
    * nested loop join with and without index
    * hash join, build and probe phases
    * sort-merge join
    * join order and the optimizer's search problem
    * grouping with hash aggregate vs sort aggregate
    * window function execution
<!-- chapter: indexes-beyond-b-trees, duration: 2h -->
* Indexes beyond `B-trees`
    * hash indexes
    * `GiST`, `GIN` and inverted indexes
    * `BRIN` and block-range indexes
    * spatial indexes (`R-tree`)
    * vector indexes (`HNSW`, `IVF`)
    * partial, expression and functional indexes
<!-- chapter: replication-and-high-availability, duration: 3h -->
* Replication and high availability
    * physical vs logical replication
    * synchronous, asynchronous and quorum replication
    * single-leader, multi-leader and leaderless models
    * failover, fencing and split brain
    * replication lag and read-your-writes consistency
<!-- chapter: distributed-consensus-and-distributed-databases, duration: 3h -->
* Distributed consensus and distributed databases
    * the `CAP` and `PACELC` theorems
    * `Paxos`, Raft and `ZAB`
    * consensus in `etcd`, `CockroachDB`, `TiDB`, Spanner
    * sharding strategies: range, hash, directory
    * distributed transactions and two-phase commit
    * deterministic databases and `Calvin`
<!-- chapter: column-stores-and-analytical-engines, duration: 2h -->
* Column stores and analytical engines
    * vectorized execution
    * compression schemes for columnar data
    * `Parquet` and `ORC` file formats
    * `ClickHouse` and `DuckDB` engine internals
    * the `OLTP`/OLAP divide and `HTAP` systems
<!-- chapter: case-studies-and-reading-source-code, duration: 2h -->
* Case studies and reading source code
    * tour of `PostgreSQL` source layout
    * tour of `RocksDB` source layout
    * tour of `SQLite` source layout
    * recommended papers and books for further study
    * end-to-end walkthrough of a single query through a real engine

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
