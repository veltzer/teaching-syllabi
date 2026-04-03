---
tags:
  - databases:postgresql
  - databases:sql
  - databases:relational
  - concepts:data-modeling
  - tools:postgresql
level: intermediate
category: database
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: postgresql_for_developers -->
# `PostgreSQL` for Developers

## Description
This course provides developers with a deep understanding of `PostgreSQL`, one of the most powerful and feature-rich open-source relational databases. Participants will `go` beyond basic `SQL` to master advanced querying techniques, indexing strategies, JSONB document storage, stored procedures with PL/pgSQL, table partitioning, and performance optimization. The course emphasizes practical, real-world patterns that developers encounter `when` building production applications backed by `PostgreSQL`.

## Duration
24 hours / 3 days

## Intended Audience
* Application developers building `PostgreSQL`-backed systems
* Backend engineers working with relational databases
* Software engineers looking to deepen their `SQL` and database skills
* Developers migrating from other relational databases to `PostgreSQL`

## Prerequisites
* Working knowledge of basic `SQL` (SELECT, INSERT, UPDATE, DELETE, JOIN)
* Familiarity with relational database concepts (tables, keys, normalization)
* Proficiency in at least one programming language
* Basic command-line skills

## Objectives
* Write advanced `SQL` queries using CTEs, window functions, and subqueries
* Design and implement effective indexing strategies for query performance
* Leverage JSONB for flexible document storage within a relational model
* Write stored procedures and functions using PL/pgSQL
* Implement table partitioning for large datasets
* Use `PostgreSQL` extensions to extend database capabilities
* Analyze and optimize query execution plans
* Apply best practices for schema design and performance tuning

## Outline
<!-- chapter: postgresql-architecture-and-internals, duration: 2h -->
* `PostgreSQL` Architecture and Internals
    * `PostgreSQL` process model and memory architecture
    * MVCC and transaction isolation levels
    * Write-ahead logging (WAL)
    * VACUUM and autovacuum
    * Configuration tuning for developers
    * Catalog tables and system views

<!-- chapter: advanced-sql-techniques, duration: 2h -->
* Advanced `SQL` Techniques
    * Subqueries and correlated subqueries
    * Common Table Expressions (CTEs)
    * Recursive CTEs for hierarchical data
    * LATERAL joins
    * UNION, INTERSECT, and EXCEPT
    * UPSERT with `ON CONFLICT`
    * RETURNING clause
    * Advanced JOIN patterns

<!-- chapter: window-functions, duration: 2h -->
* Window Functions
    * Window function syntax and concepts
    * ROW_NUMBER, RANK, DENSE_RANK
    * LAG, LEAD, FIRST_VALUE, LAST_VALUE
    * SUM, AVG, COUNT as window aggregates
    * Frame specifications (ROWS, RANGE, GROUPS)
    * `PARTITION BY` and `ORDER BY` in `windows`
    * Practical use cases: running totals, moving averages, `top`-N queries

<!-- chapter: indexing-strategies, duration: 3h -->
* Indexing Strategies
    * B-tree indexes and their behavior
    * GIN indexes for full-text search and JSONB
    * GiST indexes for geometric and range types
    * BRIN indexes for large sequential datasets
    * Hash indexes
    * Partial indexes
    * Expression indexes
    * Covering indexes (INCLUDE)
    * Multi-column index design
    * Index-only scans
    * Monitoring index usage and bloat

<!-- chapter: jsonb-and-semi-structured-data, duration: 3h -->
* JSONB and Semi-Structured Data
    * `JSON` vs JSONB in `PostgreSQL`
    * JSONB operators and functions
    * Querying nested JSONB documents
    * JSONB path expressions
    * Indexing JSONB columns with GIN
    * JSONB aggregation functions
    * Combining relational and document models
    * `When` to use JSONB vs normalized tables

<!-- chapter: pl-pgsql-programming, duration: 3h -->
* PL/pgSQL Programming
    * Function and procedure syntax
    * Variables, control structures, and loops
    * Error handling and exceptions
    * Returning sets and tables
    * Triggers and trigger functions
    * Dynamic `SQL` with EXECUTE
    * Composite types and record variables
    * Debugging and testing PL/pgSQL code

<!-- chapter: table-partitioning, duration: 3h -->
* Table Partitioning
    * Declarative partitioning in modern `PostgreSQL`
    * Range partitioning
    * List partitioning
    * Hash partitioning
    * Partition pruning and query optimization
    * Managing partitions (adding, detaching, dropping)
    * Indexing partitioned tables
    * Migrating existing tables to partitioned tables

<!-- chapter: postgresql-extensions, duration: 3h -->
* `PostgreSQL` Extensions
    * Extension architecture and management
    * pg_stat_statements for query analysis
    * pg_trgm for similarity search
    * PostGIS overview for geospatial data
    * uuid-ossp and pgcrypto
    * hstore for key-value storage
    * tablefunc for cross-tabulation
    * Creating custom extensions

<!-- chapter: query-optimization-and-performance, duration: 3h -->
* Query Optimization and Performance
    * Reading and interpreting EXPLAIN / `EXPLAIN ANALYZE`
    * Understanding query planner decisions
    * Statistics and ANALYZE
    * Common performance anti-patterns
    * Connection pooling with PgBouncer
    * Batch processing techniques
    * Materialized views
    * Performance monitoring tools

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
