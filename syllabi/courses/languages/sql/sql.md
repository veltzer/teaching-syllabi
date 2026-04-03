---
tags:
  - languages:sql
  - data-and-ai:databases
level: beginner
category: language
duration_hours: 32
audience:
  - audiences:developers
  - audiences:dbas
---
<!-- course: sql -->
# `SQL`

## Description
`SQL` (Structured Query Language) is the standard language for managing and manipulating relational databases. This course covers fundamental to advanced `SQL` concepts and teaches how to effectively query, update, and manage database systems across different platforms.

## Duration
32 hours / 4 days

## Intended Audience
* Database administrators and developers
* Software developers working with data-driven applications
* Data analysts and business intelligence professionals
* System administrators managing database systems
* Students and professionals seeking to enhance their database skills
* Anyone working with relational databases in their daily tasks

## Prerequisites
* Basic understanding of computer systems and `file` organization
* Familiarity with basic mathematical and logical concepts
* Understanding of data concepts (what is data, records, fields)
* Basic computer literacy and ability to use command-line interfaces
* No prior programming experience required, but helpful
* Access to a computer with database software installation capabilities

## Objectives
* Write efficient `SQL` queries to retrieve, filter, and sort data from single and multiple tables
* Design and implement database schemas with proper normalization and constraints
* Perform data manipulation operations including INSERT, UPDATE, DELETE, and MERGE
* Utilize advanced `SQL` features such as window functions, CTEs, and subqueries
* Optimize query performance through proper indexing and query design
* Implement database security measures and manage user permissions
* Create and manage database objects including views, stored procedures, and triggers
* Handle transactions and understand ACID principles
* Apply best practices for `SQL` coding, documentation, and maintenance
* Troubleshoot common `SQL` problems and performance issues

## Outline
<!-- chapter: introduction-to-sql-and-databases, duration: 3h -->
* Introduction to `SQL` and Databases
    * History and evolution of `SQL`
    * `SQL` standards (`SQL`-86, `SQL`-92, `SQL`:1999, `SQL`:2003, `SQL`:2016)
    * Database concepts and relational model
    * Database Management Systems (`MySQL`, `PostgreSQL`, `SQL Server`, `Oracle`)
    * Setting up the development environment
    * Database client tools and interfaces
    * First query: SELECT statement
<!-- chapter: basic-sql-syntax-and-data-types, duration: 2h -->
* Basic `SQL` Syntax and Data Types
    * `SQL` statement structure and syntax rules
    * Basic data types (INTEGER, VARCHAR, DATE, DECIMAL, BOOLEAN)
    * `NULL-values` and their handling
    * Comments in `SQL`
    * Case sensitivity and naming conventions
    * `SQL` keywords and reserved words
<!-- chapter: data-retrieval-select-statements, duration: 3h -->
* Data Retrieval (SELECT Statements)
    * Basic SELECT syntax
    * Filtering data with WHERE clause
    * Sorting results with `ORDER BY`
    * Limiting results (LIMIT, `TOP`, ROWNUM)
    * Column aliases and expressions
    * DISTINCT keyword for unique results
    * Pattern matching with LIKE and wildcards
<!-- chapter: working-with-multiple-tables, duration: 2h -->
* Working with Multiple Tables
    * Understanding table relationships
    * `INNER JOIN` operations
    * `OUTER JOINs` (LEFT, RIGHT, FULL)
    * `CROSS JOIN` and self-joins
    * Using table aliases
    * Subqueries in FROM clause
<!-- chapter: functions-and-expressions, duration: 2h -->
* Functions and Expressions
    * Aggregate functions (COUNT, SUM, AVG, MIN, MAX)
    * String functions (CONCAT, SUBSTRING, UPPER, LOWER, TRIM)
    * Date and time functions
    * Mathematical functions
    * Conditional expressions (CASE, COALESCE, NULLIF)
    * Type conversion functions (CAST, CONVERT)
<!-- chapter: grouping-and-summarizing-data, duration: 2h -->
* Grouping and Summarizing Data
    * `GROUP BY` clause fundamentals
    * HAVING clause for group filtering
    * Multiple column grouping
    * Grouping with aggregate functions
    * ROLLUP and CUBE operations
    * Window functions and OVER clause
<!-- chapter: advanced-querying-techniques, duration: 2h -->
* Advanced Querying Techniques
    * Subqueries (scalar, correlated, EXISTS)
    * Common Table Expressions (CTEs)
    * Recursive queries
    * Set operations (UNION, INTERSECT, EXCEPT)
    * Advanced JOIN techniques
    * Query optimization basics
<!-- chapter: data-modification, duration: 3h -->
* Data Modification
    * INSERT statements (single and multiple rows)
    * UPDATE statements with conditions
    * DELETE statements and truncation
    * MERGE/UPSERT operations
    * Working with transactions
    * COMMIT and ROLLBACK
    * Transaction isolation levels
<!-- chapter: database-schema-and-structure, duration: 3h -->
* Database Schema and Structure
    * `CREATE TABLE` statements
    * Data types and constraints
    * Primary keys and foreign keys
    * Indexes and their types
    * Views creation and management
    * Stored procedures and functions
    * Triggers and their applications
<!-- chapter: advanced-sql-features, duration: 2h -->
* Advanced `SQL` Features
    * Window functions (ROW_NUMBER, RANK, DENSE_RANK)
    * Pivot and unpivot operations
    * Regular expressions in `SQL`
    * `JSON` data handling
    * `Array` and `XML` operations
    * `Temporal` tables and versioning
<!-- chapter: performance-and-optimization, duration: 2h -->
* Performance and Optimization
    * Query execution plans
    * Index optimization strategies
    * Query performance tuning
    * Statistics and query analyzer
    * Partitioning concepts
    * Database normalization principles
<!-- chapter: security-and-administration, duration: 3h -->
* Security and Administration
    * User management and permissions
    * Database roles and privileges
    * `SQL` injection prevention
    * Data encryption basics
    * Backup and recovery concepts
    * Database maintenance tasks
<!-- chapter: best-practices-and-standards, duration: 3h -->
* Best Practices and Standards
    * `SQL` coding standards and style guides
    * Error handling techniques
    * Documentation and commenting
    * Testing `SQL` queries
    * Version control for database schemas
    * Common `SQL` antipatterns and pitfalls

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
