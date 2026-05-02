---
tags:
  - tools:hadoop
  - tools:hive
  - data-and-ai:big-data
level: intermediate
category: big-data
duration_hours: 16
audience:
  - audiences:data-engineers
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: hadoop_pig_and_hive -->
# `Hadoop` Pig & Hive

## Description
`Apache Pig` and `Apache Hive` are high-level abstractions over `Hadoop` `MapReduce` that simplify large-scale data processing. Pig provides a data flow scripting language (`Pig Latin`) while Hive offers a `SQL`-like interface (HiveQL) for querying data stored in `HDFS`. This course covers both tools in depth, including their optimization techniques, UDF development, and guidance on migrating workloads to `Spark`.

## Duration
16 hours / 2 days

## Intended Audience
* Data engineers building `ETL` pipelines on `Hadoop`
* Developers processing large datasets with Pig or Hive
* Data scientists querying data warehouses on `HDFS`

## Prerequisites
* Basic understanding of `Hadoop` and `HDFS`
* Familiarity with `SQL`
* Basic programming experience

## Objectives
* Write data processing scripts in `Pig Latin`
* Query and analyze data using HiveQL
* Develop user-defined functions for both Pig and Hive
* Optimize Pig and Hive jobs for performance
* Choose the appropriate tool for different data processing tasks
* Plan migration paths from Pig/Hive to `Spark`

## Outline
<!-- chapter: introduction-to-high-level-hadoop-tools, duration: 1h -->
* Introduction to High-Level `Hadoop` Tools
    * Motivation for Pig and Hive
    * Pig vs Hive vs `MapReduce`
    * Execution engines overview
    * `When` to use Pig vs Hive
<!-- chapter: apache-pig-fundamentals, duration: 1h -->
* `Apache Pig` Fundamentals
    * Pig architecture and execution modes
    * `Pig Latin` syntax
    * Data types (scalar, complex)
    * Loading and storing data (LOAD, STORE)
    * Schemas and type casting
<!-- chapter: pig-relational-operations, duration: 2h -->
* Pig Relational Operations
    * FILTER, FOREACH, GENERATE
    * GROUP and COGROUP
    * JOIN (inner, outer, replicated, skewed)
    * `ORDER BY`, LIMIT, DISTINCT
    * UNION and CROSS
    * Nested FOREACH
    * FLATTEN operator
<!-- chapter: udfs-in-pig, duration: 1h -->
* UDFs in Pig
    * Eval functions
    * Filter functions
    * Load and store functions
    * Writing UDFs in `Java`
    * Writing UDFs in `Python`
    * Registering and using UDFs
<!-- chapter: pig-optimization, duration: 1h -->
* Pig Optimization
    * Execution plan analysis (EXPLAIN, ILLUSTRATE)
    * Combiner usage
    * Multi-query execution
    * Memory management
    * Data skew handling
    * Performance best practices
<!-- chapter: apache-hive-architecture, duration: 1h -->
* `Apache Hive` Architecture
    * Hive components (Metastore, driver, compiler, executor)
    * `Hive Metastore` and schema-on-read
    * Execution engines (`MapReduce`, Tez, `Spark`)
    * HiveServer2 and Beeline
    * Hive ACID transactions
<!-- chapter: hiveql, duration: 2h -->
* HiveQL
    * Database and table management
    * Data types (primitive, complex, collection)
    * SELECT, WHERE, `GROUP BY`, HAVING, `ORDER BY`
    * Joins (inner, outer, semi, cross, map-side)
    * Subqueries and common table expressions
    * Set operations (UNION, INTERSECT)
    * Windowing and analytics functions
<!-- chapter: partitioning-and-bucketing, duration: 1h -->
* Partitioning and Bucketing
    * Static and dynamic partitioning
    * Partition pruning
    * Bucketing and sorted bucketing
    * Choosing partition columns
    * Managing partitions
<!-- chapter: serde-serializer-deserializer, duration: 1h -->
* SerDe (Serializer/Deserializer)
    * Built-in SerDes (`CSV`, `JSON`, ORC, `Parquet`, `Avro`)
    * Custom SerDe development
    * RegexSerDe for log parsing
    * `File` format comparison and selection
<!-- chapter: hive-udfs, duration: 1h -->
* Hive UDFs
    * Standard UDFs
    * User-defined aggregate functions (UDAFs)
    * User-defined table-generating functions (UDTFs)
    * GenericUDF interface
    * Deploying and registering UDFs
<!-- chapter: hive-optimization, duration: 2h -->
* Hive Optimization
    * Tez execution engine
    * Vectorized query execution
    * Cost-based optimizer (CBO)
    * ORC and `Parquet` file format tuning
    * Map-side joins and bucket map joins
    * Predicate pushdown
    * Statistics collection and usage
    * Configuration tuning
<!-- chapter: pig-vs-hive-comparison, duration: 1h -->
* Pig vs Hive Comparison
    * Language paradigm differences
    * Performance characteristics
    * Use case suitability
    * Ecosystem integration
    * Community and tooling
<!-- chapter: migration-to-spark, duration: 1h -->
* Migration to `Spark`
    * Why migrate from Pig/Hive to `Spark`
    * `Spark SQL` as a Hive replacement
    * Converting Pig scripts to `PySpark`
    * Hive on `Spark` execution engine
    * Migration strategies and planning
    * Coexistence patterns

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
