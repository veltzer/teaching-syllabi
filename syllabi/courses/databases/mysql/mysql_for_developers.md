---
tags:
  - tools:mysql
  - databases:sql
  - data-and-ai:databases
  - concepts:data-modeling
level: intermediate
category: database
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: mysql_for_developers -->
# `MySQL` for Developers

## Description
This course provides developers with comprehensive training on `MySQL`, one of the world's most popular relational database management systems. Participants will learn how to write efficient queries, design performant schemas, and leverage advanced `MySQL` features such as `JSON` support, stored procedures, triggers, and views. The course also covers indexing strategies, transactions, replication basics, and performance tuning techniques essential for building production-grade applications.

## Duration
24 hours / 3 days

## Intended Audience
* Application developers working with `MySQL` databases
* Backend developers building data-driven applications
* Full-stack developers needing relational database skills
* Software engineers optimizing database performance

## Prerequisites
* Basic understanding of relational database concepts
* Familiarity with `SQL` syntax (SELECT, INSERT, UPDATE, DELETE)
* Experience with at least one programming language
* Basic command-line skills

## Objectives
* Write complex queries using joins, subqueries, and common table expressions
* Design and implement effective indexing strategies
* Leverage `MySQL` `JSON` support for semi-structured data
* Create and manage stored procedures, triggers, and views
* Implement transactions with proper isolation levels
* Understand `MySQL` replication architecture and basics
* Diagnose and resolve common performance bottlenecks
* Apply best practices for schema design and query optimization

## Outline
<!-- chapter: introduction-to-mysql-architecture, duration: 2h -->
* Introduction to `MySQL` Architecture
    * `MySQL` server architecture overview
    * Storage engines: InnoDB vs MyISAM
    * InnoDB internals and buffer pool
    * Connection handling and thread model
    * `MySQL` configuration basics
    * Development environment setup

<!-- chapter: advanced-sql-queries, duration: 2h -->
* Advanced `SQL` Queries
    * Complex SELECT statements
    * Filtering and sorting techniques
    * Aggregate functions and grouping
    * `CASE-expressions` and conditional logic
    * UNION and set operations
    * Common table expressions (CTEs)
    * Recursive queries
    * Window functions

<!-- chapter: joins-and-subqueries, duration: 2h -->
* Joins and Subqueries
    * Inner and outer joins
    * Self joins and cross joins
    * Correlated and non-correlated subqueries
    * Subqueries in SELECT, FROM, and WHERE clauses
    * EXISTS and IN operators
    * Derived tables
    * Join optimization techniques

<!-- chapter: indexing-strategies, duration: 3h -->
* Indexing Strategies
    * How B-tree indexes work in InnoDB
    * Primary keys and clustered indexes
    * Secondary indexes and covering indexes
    * Composite indexes and column order
    * Full-text indexes
    * Spatial indexes
    * Index maintenance and monitoring
    * Using EXPLAIN to analyze query plans

<!-- chapter: json-support-in-mysql, duration: 2h -->
* `JSON` Support in `MySQL`
    * `JSON` data type and storage
    * `JSON` functions: JSON_EXTRACT, JSON_SET, JSON_REPLACE
    * `JSON` path expressions
    * Indexing `JSON` columns with generated columns
    * `JSON` aggregation functions
    * `When` to use `JSON` vs normalized columns
    * Querying nested `JSON` structures

<!-- chapter: stored-procedures-and-functions, duration: 2h -->
* Stored Procedures and Functions
    * Creating and managing stored procedures
    * Input, output, and inout parameters
    * Control flow: IF, CASE, LOOP, WHILE
    * Cursors and handlers
    * User-defined functions
    * Error handling and diagnostics
    * Security and permissions for routines

<!-- chapter: triggers, duration: 2h -->
* Triggers
    * BEFORE and AFTER triggers
    * INSERT, UPDATE, and DELETE triggers
    * Accessing OLD and NEW row values
    * Trigger use cases and patterns
    * Trigger limitations and pitfalls
    * Auditing and data validation with triggers

<!-- chapter: views, duration: 2h -->
* Views
    * Creating and managing views
    * Updatable views
    * View performance considerations
    * Materialized view patterns in `MySQL`
    * Using views for security and abstraction
    * Common view `design patterns`

<!-- chapter: transactions-and-concurrency, duration: 2h -->
* Transactions and Concurrency
    * ACID properties in `MySQL`
    * Transaction syntax and lifecycle
    * Isolation levels: `READ UNCOMMITTED`, `READ COMMITTED`, `REPEATABLE READ`, SERIALIZABLE
    * Locking mechanisms: row locks, table locks, gap locks
    * Deadlock detection and prevention
    * Optimistic vs pessimistic locking patterns
    * Transaction best practices

<!-- chapter: replication-basics, duration: 2h -->
* Replication Basics
    * `MySQL` replication architecture
    * Binary log formats: statement, row, mixed
    * Source-replica setup
    * GTID-based replication
    * Replication lag monitoring
    * Read/write splitting patterns
    * `Group replication` overview

<!-- chapter: performance-tuning, duration: 3h -->
* Performance Tuning
    * Query profiling with EXPLAIN and `EXPLAIN ANALYZE`
    * Slow query log analysis
    * `MySQL` `Performance Schema`
    * Buffer pool tuning
    * Query cache considerations
    * Optimizing joins and subqueries
    * Batch operations and bulk loading
    * Connection pooling strategies
    * Monitoring tools and metrics

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
