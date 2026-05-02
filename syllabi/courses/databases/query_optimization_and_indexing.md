---
tags:
  - concepts:databases
  - concepts:database-design
  - concepts:performance
  - concepts:optimization
  - concepts:persistence
level: intermediate
category: database
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:dbas
  - audiences:data-engineers
---
<!-- course: query_optimization_and_indexing -->
# Query Optimization and Indexing

## Description
Most production database performance problems are bad queries against bad indexes. The fix is rarely a hardware
upgrade or a database change; it is the engineer learning to read execution plans, understand the optimizer's
cost model, and choose the right index for the workload. The skills are learnable in a structured way and
transfer between database engines.

This five day course is a hands-on, engineer-facing treatment of query optimization across the major relational
engines. It covers reading and reasoning about execution plans, the optimizer's cost model and statistics,
indexing strategy from access patterns, query rewriting, partitioning, parameter sniffing and plan stability,
and the operational discipline of finding and fixing slow queries in production. The course uses `PostgreSQL`,
`MySQL` and `SQL Server` as worked examples and notes where Oracle, `MariaDB` and `CockroachDB` differ.
Participants leave able to diagnose and fix slow queries, design indexes that earn their cost, and build the
discipline that keeps query performance predictable.

## Duration
40 hours / 5 days

## Intended Audience
* developers writing production `SQL` against any major engine
* `DBAs` and senior engineers tuning production queries
* data engineers writing pipeline `SQL` against analytical stores
* engineers responding to "the database is slow" incidents

## Prerequisites
* `solid` `SQL` and at least basic exposure to one relational database
* basic understanding of indexes, transactions and joins
* working knowledge of at least one programming language

## Objectives
* read and interpret execution plans across major engines
* design indexes from real access patterns
* rewrite queries for performance without changing their results
* reason about the optimizer's cost model and statistics
* operate large databases with predictable query performance
* diagnose and fix slow-query incidents under time pressure
* build a query-performance discipline on a team

## Outline
<!-- chapter: the-mental-model-of-a-query, duration: 2h -->
* The mental model of a query
    * how a query becomes an execution plan
    * parser, planner, executor revisited
    * cost-based optimization in one paragraph
    * the difference between logical and physical plans
    * cross-reference to the Database Internals course
    * what the optimizer can and cannot fix
<!-- chapter: reading-execution-plans, duration: 4h -->
* Reading execution plans
    * `EXPLAIN` and `EXPLAIN ANALYZE` in `PostgreSQL`
    * `EXPLAIN` and `EXPLAIN FORMAT=JSON` in `MySQL`
    * `SET STATISTICS` and the actual plan in `SQL Server`
    * plan visualizers: `explain.dalibo`, pev, `Plan Explorer`
    * estimated vs actual rows and the divergence problem
    * common plan shapes: nested loop, hash join, sort merge
    * reading the plan top-down and bottom-up
<!-- chapter: indexes-the-foundation, duration: 4h -->
* Indexes: the foundation
    * `B-tree` indexes in depth
    * single-column vs multi-column indexes
    * leftmost-prefix rule and column order
    * covering indexes and the included-columns trick
    * partial and filtered indexes
    * expression and functional indexes
    * unique indexes and constraint enforcement
    * the cost of an index on writes
<!-- chapter: index-types-beyond-b-tree, duration: 3h -->
* Index types beyond `B-tree`
    * hash indexes
    * `GIN` and GiST in `PostgreSQL`
    * `BRIN` for time-series and append-only tables
    * full-text indexes
    * spatial indexes (`R-tree`, `R*`-tree)
    * `JSON`-path indexes
    * vector indexes (`HNSW`, `IVF`)
    * choosing an index type from access patterns
<!-- chapter: statistics-and-the-optimizer, duration: 3h -->
* Statistics and the optimizer
    * what statistics the optimizer actually uses
    * histograms, `MCV`, distinct counts
    * stale statistics as a slow-query cause
    * extended and multi-column statistics
    * `auto-analyze` and its limits
    * forcing statistics refresh during incidents
    * cross-engine differences in statistics handling
<!-- chapter: join-strategies-and-tuning, duration: 3h -->
* Join strategies and tuning
    * nested loop join with and without index
    * hash join: build and probe phases
    * sort-merge join
    * the optimizer's join order search
    * join order hints and the cases where they help
    * `LATERAL` and correlated subqueries
    * recognizing the wrong join strategy from a plan
<!-- chapter: query-rewriting-techniques, duration: 3h -->
* Query rewriting techniques
    * pushing predicates closer to scans
    * eliminating subqueries and `IN` lists
    * `EXISTS` vs IN vs `JOIN`
    * `UNION` vs `UNION ALL`
    * window functions vs self-joins
    * `CTE` materialization differences across engines
    * the "rewrite, do not hint" rule
<!-- chapter: pagination-and-cursor-patterns, duration: 2h -->
* Pagination and `cursor` patterns
    * `OFFSET`/`LIMIT` and its cliff
    * keyset pagination
    * deep pagination patterns
    * `cursor`-based pagination for `APIs`
    * combining pagination with sort stability
<!-- chapter: aggregation-and-grouping, duration: 2h -->
* Aggregation and grouping
    * hash aggregate vs sort aggregate
    * `GROUP BY` with rollups, cubes, grouping sets
    * pre-aggregation and materialized views
    * approximate aggregates: `HyperLogLog`, t-digest
    * window functions for grouping-without-grouping
<!-- chapter: partitioning-for-performance, duration: 3h -->
* Partitioning for performance
    * range, list, hash partitioning
    * partition pruning in plans
    * partition-wise joins
    * the cost of too many partitions
    * partition-aware indexing
    * `pg_partman`, `pt-partition`, `SQL Server` partition functions
<!-- chapter: parameter-sniffing-and-plan-stability, duration: 2h -->
* Parameter sniffing and plan stability
    * the parameter-sniffing problem in `SQL Server` and others
    * plan caching strategies across engines
    * `OPTIMIZE FOR` hints
    * forced plans and plan baselines
    * plan-management tools: `Query Store`, pg_stat_statements, `MySQL` `Performance Schema`
<!-- chapter: indexing-strategy-from-workloads, duration: 3h -->
* Indexing strategy from workloads
    * starting from access patterns, not columns
    * `pg_stat_statements` and the slow-query log
    * unused-index detection
    * duplicate and redundant index detection
    * the index-tuning advisor and its blind spots
    * the cost of one more index revisited
<!-- chapter: locking-blocking-and-mvcc-effects-on-queries, duration: 2h -->
* Locking, blocking and `MVCC` effects on queries
    * row-level vs page-level vs table-level locks
    * `MVCC` bloat and VACUUM in `PostgreSQL`
    * undo log growth in `MySQL`
    * blocking and chain-of-blocking queries
    * lock-wait timeouts and isolation-level surprises
<!-- chapter: olap-vs-oltp-tuning, duration: 2h -->
* `OLAP` vs `OLTP` tuning
    * the very different optimizer goals
    * column stores: `ClickHouse`, `DuckDB`, `BigQuery`, Snowflake
    * partition pruning and clustering
    * vectorized execution
    * cross-reference to the Database Internals course
<!-- chapter: production-incident-tuning-and-wrap-up, duration: 2h -->
* Production incident tuning and wrap up
    * the slow-query incident playbook
    * `pg_stat_activity` and the equivalents
    * killing the right query
    * temporary index creation under load
    * post-incident permanent fixes
    * cross-reference to the Incident Response courses
    * group review of an `EXPLAIN ANALYZE` plan from a real query
    * recommended reading: `Greene`, Winand, `PostgreSQL` and `MySQL` docs

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
