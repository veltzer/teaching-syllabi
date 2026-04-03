---
tags:
  - languages:scala
  - tools:spark
  - data-and-ai:big-data
level: intermediate
category: language
duration_hours: 16
audience:
  - audiences:data-engineers
  - audiences:developers
---
<!-- course: scala_for_data_engineering -->
# `Scala` for Data Engineering

## Description
This course teaches `Scala` from a data engineering perspective, focusing on the functional programming features and patterns most relevant to building data pipelines and processing large-scale datasets. Participants will learn functional `Scala`, advanced collections, pattern matching, implicits, and how to integrate with `Apache Spark` for distributed data processing. The course bridges the gap between `Scala` language proficiency and practical data engineering skills. The course includes hands on exercises.

## Duration
16 hours / 2 days

## Intended Audience
* Data engineers who need to work with `Scala`-based data processing frameworks.
* Developers building data pipelines with `Apache Spark`.
* Software engineers transitioning into data engineering roles using the `Scala` ecosystem.

## Prerequisites
* Programming experience in `Scala`, `Java`, or another object-oriented language.
* Basic understanding of data processing concepts.
* Familiarity with `SQL` and relational databases.

## Objectives
* Write functional `Scala` code using immutable data structures and higher-order functions
* Use advanced `Scala` collections for data transformation
* Apply pattern matching and implicits in practical scenarios
* Build data pipelines with `Apache Spark` using the `Scala` `API`
* Test `Scala` data applications effectively

## Outline
<!-- chapter: functional-scala-foundations, duration: 2h -->
* Functional `Scala` Foundations
    * Immutability and pure functions
    * Higher-order functions and closures
    * Function composition and currying
    * Option, Either, and Try for error handling
    * For-comprehensions
    * Tail recursion and @tailrec
<!-- chapter: scala-collections-in-depth, duration: 2h -->
* `Scala` Collections in Depth
    * Immutable vs mutable collections
    * `Seq`, Set, and Map hierarchies
    * Transformations: map, flatMap, filter, fold, reduce
    * Grouping, partitioning, and aggregation
    * Parallel collections
    * Performance characteristics of different collection types
    * Views and lazy evaluation
<!-- chapter: pattern-matching, duration: 2h -->
* Pattern Matching
    * Match expressions and case classes
    * Extractors and unapply
    * Sealed traits and exhaustive matching
    * Pattern matching with collections
    * Custom extractors for data parsing
    * Guards and nested patterns
<!-- chapter: implicits-and-type-classes, duration: 2h -->
* Implicits and Type Classes
    * Implicit parameters and conversions
    * Type classes and ad-hoc polymorphism
    * Context bounds and implicit evidence
    * Given instances and using clauses (`Scala 3`)
    * Extension methods
    * Designing type class hierarchies for data types
<!-- chapter: apache-spark-integration, duration: 3h -->
* `Apache Spark` Integration
    * `Spark` architecture and the `Scala` `API`
    * SparkSession and configuration
    * RDDs: creation, transformations, and actions
    * DataFrames and the Dataset `API`
    * `Spark SQL` and query execution
    * Reading and writing data formats (`Parquet`, `JSON`, `CSV`, `Avro`)
    * UDFs and custom transformations
<!-- chapter: building-data-pipelines, duration: 3h -->
* Building Data Pipelines
    * `ETL` pipeline `design patterns`
    * Data validation and quality checks
    * Handling schema evolution
    * Partitioning and bucketing strategies
    * Broadcast variables and accumulators
    * Joins and shuffle optimization
    * Streaming with `Structured Streaming`
<!-- chapter: testing-scala-data-applications, duration: 2h -->
* Testing `Scala` Data Applications
    * Unit testing with ScalaTest and specs2
    * Testing `Spark` applications locally
    * Property-based testing with ScalaCheck
    * Test fixtures and shared SparkSession
    * Integration testing data pipelines
    * Data quality assertions

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
