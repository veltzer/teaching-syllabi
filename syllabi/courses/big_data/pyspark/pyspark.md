---
tags:
  - tools:spark
  - languages:python
  - data-and-ai:big-data
level: intermediate
category: big-data
duration_hours: 24
audience:
  - audiences:developers
  - audiences:data-engineers
  - audiences:data-scientists
---
<!-- course: pyspark -->
# `PySpark`

## Description
`PySpark` is the `Python` `API` for `Apache Spark`, enabling large-scale data processing using familiar `Python` syntax. This course covers the full `PySpark` stack from RDDs and DataFrames through `Spark SQL`, streaming, and `machine learning` with `MLlib`. Students will learn to write efficient distributed data pipelines, optimize performance, and deploy `Spark` applications in production environments.

## Duration
24 hours / 3 days

## Intended Audience
* Developers building data processing pipelines with `Python`
* Data engineers designing `ETL` workflows at scale
* Data scientists who need distributed computing for large datasets

## Prerequisites
* Proficiency in `Python` programming
* Basic understanding of `SQL`
* Familiarity with data processing concepts

## Required Knowledge
* `Python` Programming (or equivalent experience)

## Objectives
* Create and configure SparkSession instances
* Process data using RDDs, DataFrames, and `Spark SQL`
* Read and write data from multiple sources
* Optimize `Spark` application performance
* Build streaming pipelines with `Spark Streaming`
* Apply basic `machine learning` with `MLlib`

## Outline
<!-- chapter: introduction-to-pyspark, duration: 2h -->
* Introduction to `PySpark`
    * `Apache Spark` architecture overview
    * SparkSession and SparkContext
    * Local vs cluster mode
    * `PySpark` shell and notebooks
    * Application structure and submission with `spark`-submit
<!-- chapter: rdds-resilient-distributed-datasets, duration: 3h -->
* RDDs (Resilient Distributed Datasets)
    * Creating RDDs
    * Transformations (map, filter, flatMap, reduceByKey, groupByKey)
    * Actions (collect, count, take, saveAsTextFile)
    * Lazy evaluation
    * Partitioning and repartitioning
    * Pair RDDs
<!-- chapter: dataframes-and-datasets, duration: 3h -->
* DataFrames and Datasets
    * Creating DataFrames
    * Schema definition and inference
    * Column operations and expressions
    * Selecting, filtering, and aggregating
    * Joins (inner, outer, cross, semi, anti)
    * Handling missing data
    * User-defined functions (UDFs)
<!-- chapter: spark-sql, duration: 2h -->
* `Spark SQL`
    * Registering temporary views
    * Writing `SQL` queries on DataFrames
    * Catalog `API`
    * Window functions (row_number, rank, lead, lag)
    * Common table expressions
<!-- chapter: data-sources, duration: 3h -->
* Data Sources
    * `CSV` and `TSV`
    * `Parquet` and ORC
    * `JSON`
    * `JDBC` and database connectivity
    * `Delta Lake` introduction
    * Schema evolution and merging
<!-- chapter: performance-tuning, duration: 4h -->
* Performance Tuning
    * Understanding the query execution plan (explain)
    * Catalyst optimizer
    * Caching and persistence levels
    * Broadcast variables
    * Accumulators
    * Partitioning strategies
    * Shuffle optimization
    * Memory management and configuration
<!-- chapter: mllib-basics, duration: 2h -->
* `MLlib` Basics
    * `ML` pipelines
    * Feature transformers
    * Classification and regression
    * Clustering
    * Model evaluation
<!-- chapter: spark-streaming, duration: 3h -->
* `Spark Streaming`
    * DStreams overview
    * Structured Streaming
    * Window operations
    * Watermarking
    * Output modes and sinks
    * Integration with `Kafka`
<!-- chapter: deployment-and-operations, duration: 2h -->
* Deployment and Operations
    * Cluster managers (Standalone, `YARN`, `Kubernetes`)
    * Application packaging
    * Logging and monitoring
    * `Spark` UI
    * Configuration best practices

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
