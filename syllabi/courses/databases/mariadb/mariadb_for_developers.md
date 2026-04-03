---
tags:
  - databases:mariadb
  - databases:mysql
  - databases:relational
  - databases:sql
  - tools:mariadb
level: intermediate
category: database
duration_hours: 24
audience:
  - audiences:developers
  - audiences:dbas
---
<!-- course: mariadb_for_developers -->
# `MariaDB` for Developers

## Description
`MariaDB` is a community-developed, fully open-source relational database management system that originated as a drop-in replacement for `MySQL` and has since evolved with unique features and performance improvements. This course provides developers and database administrators with a comprehensive understanding of `MariaDB` from basic `SQL` through advanced features such as stored procedures, triggers, and full-text search. Participants will explore `MariaDB`-specific enhancements including columnar storage with `ColumnStore`, `temporal` tables, and enhanced replication capabilities. The course combines theoretical foundations with practical exercises on real-world schema design, query optimization, and production operations.

## Duration
24 hours / 3 days

## Intended Audience
* Application developers building on relational databases
* Database administrators managing `MariaDB` or `MySQL` instances
* Engineers migrating from `MySQL` to `MariaDB`
* Backend developers who need to write and optimize complex `SQL`
* Architects designing data storage layers for web and enterprise applications

## Prerequisites
* Basic programming experience in any language
* Familiarity with fundamental database concepts (tables, rows, columns)
* Some prior exposure to `SQL` is helpful but not required
* Basic `Linux` command-line skills

## Objectives
* Install, configure, and connect to `MariaDB` server instances
* Write correct and efficient `SQL` for data retrieval and manipulation
* Design normalized schemas and choose appropriate data types
* Create stored procedures, functions, triggers, and events
* Build and use indexes to optimize query performance
* Manage transactions and understand concurrency control with InnoDB
* Utilize `MariaDB`-specific features including `temporal` tables and dynamic columns
* Set up basic replication and understand high-availability options
* Implement security best practices and manage user privileges
* Perform backup and recovery using `mysqldump` and `mariabackup`

## Exercises
Hands-on labs using a local `MariaDB` server. Students will design and implement a multi-table relational schema, write queries ranging from basic SELECTs to complex multi-table joins and aggregations, create stored procedures and triggers, analyze and optimize slow queries using EXPLAIN, configure replication between two server instances, and practice backup and point-in-time recovery. Scenarios include e-commerce, content management, and reporting use cases.

## Outline
<!-- chapter: introduction-to-mariadb, duration: 1h -->
* Introduction to `MariaDB`
    * History of `MariaDB` and its relationship with `MySQL`
    * `MariaDB` vs `MySQL`: key differences and compatibility
    * `MariaDB` editions: Community, Enterprise, and SkySQL
    * The `MariaDB` ecosystem: tools and connectors
    * `When` to choose `MariaDB`

<!-- chapter: installation-and-configuration, duration: 1h -->
* Installation and Configuration
    * Installing `MariaDB` on `Linux`, `macOS`, and with `Docker`
    * The `mysql_secure_installation` script
    * Key configuration parameters in `my.cnf`
    * Connecting with the `mariadb` `CLI` client
    * GUI tools: `DBeaver`, `HeidiSQL`, and `MySQL Workbench`
    * Understanding the data directory structure

<!-- chapter: sql-fundamentals, duration: 2h -->
* `SQL` Fundamentals
    * Creating and managing databases and tables
    * INSERT, SELECT, UPDATE, DELETE operations
    * Filtering with WHERE and operators
    * Sorting with `ORDER BY` and limiting with LIMIT
    * Aliases and basic string functions
    * NULL handling and IS NULL / IS NOT NULL
    * Basic aggregate functions: COUNT, SUM, AVG, MIN, MAX

<!-- chapter: advanced-sql-queries, duration: 3h -->
* Advanced `SQL` Queries
    * INNER, LEFT, RIGHT, and FULL OUTER JOINs
    * Self joins and cross joins
    * Subqueries and correlated subqueries
    * Common Table Expressions (CTEs) with WITH
    * Window functions: ROW_NUMBER, RANK, LEAD, LAG
    * `GROUP BY` with ROLLUP and CUBE
    * UNION, INTERSECT, and EXCEPT
    * Full-text search with MATCH AGAINST

<!-- chapter: mariadb-data-types-and-functions, duration: 2h -->
* `MariaDB` Data Types and Functions
    * Numeric types: `INT`, BIGINT, DECIMAL, FLOAT
    * String types: VARCHAR, TEXT, CHAR, ENUM
    * Date and time types: DATE, DATETIME, TIMESTAMP, TIME
    * The `JSON` data type and `JSON` functions
    * Dynamic columns with BLOB-based storage
    * `Temporal` tables for historical data tracking
    * Spatial data types and functions

<!-- chapter: stored-procedures-and-triggers, duration: 3h -->
* Stored Procedures and Triggers
    * Creating and calling stored procedures
    * Parameters: IN, OUT, and INOUT
    * Control flow: IF, CASE, LOOP, WHILE, REPEAT
    * Error handling with DECLARE HANDLER
    * User-defined functions (UDFs)
    * Creating and managing triggers
    * BEFORE and AFTER triggers for INSERT, UPDATE, DELETE
    * Scheduled events with the Event Scheduler

<!-- chapter: indexing-and-performance, duration: 3h -->
* Indexing and Performance
    * How indexes work: B-tree and hash indexes
    * Primary keys and unique indexes
    * Composite indexes and column order
    * Full-text indexes
    * Reading and interpreting EXPLAIN output
    * The slow query log and `performance schema`
    * Query optimizer hints
    * Index maintenance: fragmentation and ANALYZE TABLE
    * Avoiding common performance anti-patterns

<!-- chapter: transactions-and-concurrency, duration: 2h -->
* Transactions and Concurrency
    * ACID properties in `MariaDB` InnoDB
    * START TRANSACTION, COMMIT, and ROLLBACK
    * Savepoints
    * InnoDB isolation levels: READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE
    * Row-level locking and lock contention
    * Deadlocks: detection, debugging, and prevention
    * Optimistic vs pessimistic locking patterns

<!-- chapter: mariadb-specific-features, duration: 2h -->
* `MariaDB`-Specific Features
    * Sequence objects for auto-generated values
    * Invisible columns
    * System-versioned `temporal` tables
    * `ColumnStore` storage engine for analytical queries
    * `Spider` storage engine for table sharding
    * `MyRocks` storage engine overview
    * `CONNECT` engine for external data sources

<!-- chapter: replication-overview, duration: 2h -->
* Replication Overview
    * Binary log and replication formats: row, statement, mixed
    * Setting up primary/replica replication
    * GTID-based replication in `MariaDB`
    * Semisynchronous replication
    * Multi-source replication use cases
    * Parallel replication for performance
    * Monitoring replication lag

<!-- chapter: security-and-user-management, duration: 2h -->
* Security and User Management
    * Authentication plugins: `mysql_native_password`, `ed25519`, `PAM`
    * Creating users and managing passwords
    * GRANT and REVOKE privilege system
    * Role-based access control
    * `SSL/TLS` encryption for connections
    * Auditing with the Audit Plugin
    * Hardening a `MariaDB` installation

<!-- chapter: backup-and-recovery, duration: 1h -->
* Backup and Recovery
    * Logical backups with `mysqldump` and `mydumper`
    * Physical backups with `mariabackup`
    * Incremental and partial backups
    * Point-in-time recovery using the binary log
    * Backup verification and restore testing
    * Backup scheduling and retention policies

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
