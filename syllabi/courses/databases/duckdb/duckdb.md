---
tags:
  - databases:duckdb
  - databases:analytical
  - databases:olap
  - databases:sql
  - tools:duckdb
level: intermediate
category: database
duration_hours: 16
audience:
  - audiences:developers
  - audiences:data-engineers
  - audiences:data-scientists
---
<!-- course: duckdb -->
# `DuckDB`

## Description
`DuckDB` is an in-process analytical database designed for high-performance OLAP workloads directly within your application process, eliminating the need for a separate database server. It delivers vectorized query execution and columnar storage, making it exceptionally fast for analytical queries over large datasets. This course provides a comprehensive introduction to `DuckDB`, covering everything from installation and basic `SQL` to advanced analytics, `file` format integration, and performance tuning. Participants will learn how to leverage `DuckDB` in data engineering pipelines, data science workflows, and application backends using `Python`, `R`, and other languages.

## Duration
16 hours / 2 days

## Intended Audience
* Data engineers building `ETL` pipelines and local analytics workflows
* Data scientists who want fast in-process `SQL` over large datasets
* Application developers looking to embed analytical query capabilities
* Analysts migrating from heavyweight OLAP systems to lightweight alternatives
* Engineers evaluating modern alternatives to `SQLite` for analytical workloads

## Prerequisites
* Working knowledge of `SQL` (SELECT, `GROUP BY`, JOINs)
* Basic experience with at least one of `Python`, `R`, or a `JVM` language
* Familiarity with tabular data concepts (rows, columns, schemas)

## Objectives
* Understand `DuckDB`'s architecture and what makes it suited for OLAP workloads
* Install and use `DuckDB` via `CLI`, `Python`, `R`, and `JDBC` interfaces
* Write advanced `SQL` queries including window functions, CTEs, and lateral joins
* Read from and write to `Parquet`, `CSV`, `JSON`, and `Arrow` formats natively
* Use `DuckDB` extensions to expand functionality
* Integrate `DuckDB` with `Python` data tools including `Pandas` and `Polars`
* Tune query performance using the optimizer, profiling, and parallelism settings
* Apply `DuckDB` to common data engineering and analytics patterns

## Exercises
Hands-on labs using `DuckDB` via both the `CLI` and `Python` `API`. Students will load and query datasets from `Parquet` and `CSV` files, write complex analytical `SQL`, build multi-step transformations using CTEs, install and use extensions such as `httpfs` and `spatial`, integrate results with `Pandas` DataFrames, and profile queries to identify bottlenecks. Real-world scenarios include log analytics, financial aggregations, and geospatial data processing.

## Outline
<!-- chapter: introduction-to-duckdb, duration: 1h -->
* Introduction to `DuckDB`
    * What is `DuckDB` and the in-process analytics paradigm
    * OLAP vs OLTP and where `DuckDB` fits
    * Columnar storage and vectorized execution overview
    * Comparison with `SQLite`, `PostgreSQL`, `Spark`, and `Snowflake`
    * `When` to use `DuckDB` and its limitations

<!-- chapter: installation-and-interfaces, duration: 1h -->
* Installation and Interfaces
    * Installing `DuckDB` `CLI`, `Python` package, and `R` package
    * The `DuckDB` `CLI`: basic navigation and commands
    * In-memory vs persistent databases
    * Connecting via `JDBC` and ODBC
    * Using the `DuckDB` web shell

<!-- chapter: sql-fundamentals-in-duckdb, duration: 2h -->
* `SQL` Fundamentals in `DuckDB`
    * Creating tables and inserting data
    * SELECT, WHERE, `GROUP BY`, HAVING, `ORDER BY`
    * Joins: inner, outer, cross, and lateral
    * Subqueries and scalar subqueries
    * Common Table Expressions (CTEs)
    * `DuckDB` `SQL` dialect extensions and conveniences

<!-- chapter: advanced-sql-and-analytics, duration: 3h -->
* Advanced `SQL` and Analytics
    * Window functions: RANK, DENSE_RANK, ROW_NUMBER, LAG, LEAD
    * OVER clauses: PARTITION BY and `ORDER BY` within `windows`
    * PIVOT and UNPIVOT operations
    * ASOF joins for time-series data alignment
    * UNNEST and list processing functions
    * String functions, date/time functions, and regex support
    * Aggregate functions and statistical aggregates

<!-- chapter: reading-and-writing-files, duration: 2h -->
* Reading and Writing Files
    * Reading `CSV` files with `read_csv_auto`
    * Reading and writing `Parquet` files
    * Reading `JSON` and `NDJSON` files
    * Querying files directly with `SELECT * FROM 'file.parquet'`
    * Reading from `S3` and `HTTP` endpoints using `httpfs`
    * Writing query results to files
    * Schema inference and override options

<!-- chapter: duckdb-extensions, duration: 2h -->
* `DuckDB` Extensions
    * Extension architecture and the extension repository
    * Installing and loading extensions
    * `httpfs`: remote `file` access
    * `spatial`: geospatial data with WKT and WKB
    * `json`: advanced `JSON` processing
    * `tpch` and `tpcds`: built-in benchmarking
    * Community extensions and building custom extensions

<!-- chapter: python-and-r-integration, duration: 2h -->
* `Python` and `R` Integration
    * The `duckdb` `Python` package `API`
    * Querying `Pandas` DataFrames and `Polars` DataFrames in-place
    * Registering `Python` objects as virtual tables
    * `Arrow` and zero-copy data exchange
    * Integration with `dbt` using `dbt-duckdb`
    * `R` integration via `duckdb` `R` package
    * Embedding `DuckDB` in application code

<!-- chapter: performance-tuning, duration: 2h -->
* Performance Tuning
    * `DuckDB` query optimizer and explain plans
    * Parallelism and thread configuration
    * Memory limits and buffer management
    * Projection and filter pushdown
    * Statistics and query profiling with `EXPLAIN ANALYZE`
    * Partitioned `Parquet` files and partition pruning
    * Indexing options: min-max indexes and ART indexes

<!-- chapter: use-cases-and-patterns, duration: 1h -->
* Use Cases and Patterns
    * `DuckDB` as a local data lakehouse query engine
    * Replacing `pandas` pipelines with `SQL`
    * Using `DuckDB` in `CI/CD` pipelines for data validation
    * Embedded analytics in applications
    * `DuckDB`-WASM for browser-based analytics
    * Operational patterns and best practices

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
