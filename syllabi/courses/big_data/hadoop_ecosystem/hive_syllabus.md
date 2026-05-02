---
tags:
  - tools:hive
  - tools:hadoop
  - data-and-ai:big-data
  - languages:sql
  - data-and-ai:etl
level: intermediate
category: big-data
duration_hours: 24
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: hive_syllabus -->
# Hive

## Description
This course provides a comprehensive introduction to `Apache Hive` and its role within the `Hadoop` ecosystem. Participants will learn how to use HiveQL for querying and managing large datasets stored in `HDFS`, as well as how to optimize query performance. The course also covers related tools such as Pig and `ETL` workflows for bringing data into `Hadoop`.

## Duration
24 hours / 3 days

## Intended Audience
Developers and data scientists who need to query and analyze large-scale data using `SQL`-like interfaces on top of `Hadoop`.

## Prerequisites
* Basic knowledge of `SQL` and relational database concepts.
* Familiarity with the `Hadoop` ecosystem is an advantage but not required.

## Objectives
* Understand the `Hadoop` ecosystem and the role of Hive within it
* Write HiveQL queries to analyze large datasets stored in `HDFS`
* Manage Hive databases, tables, views, and data formats
* Perform text processing and use regular expressions within Hive
* Optimize Hive query performance using partitioning, bucketing, and indexing

## Outline
<!-- chapter: introduction-to-hadoop, duration: 3h -->
* Introduction to `Hadoop`
    * Why `Hadoop`?
    * `Hadoop` overview
    * `HDFS`
    * Map/Reduce
    * Hands on: launching `Hadoop` and a map reduce job on it.
<!-- chapter: etl-basics, duration: 1h -->
* `ETL` basics
    * Bringing in data to `Hadoop`.
    * Organizing your data.
<!-- chapter: pig-introduction, duration: 3h -->
* Pig introduction:
    * What is Pig?
    * Features
    * Use cases
    * Interacting with Pig.
    * Demo by the instructor of Pig processing.
<!-- chapter: hive-introduction, duration: 4h -->
* Hive introduction
    * What is Hive?
    * Hive schema and data storage
    * Hive vs RDBMS
    * `When` to use Hive?
    * Interacting with Hive.
    * Hands on: launching Hive with pre-given schema and issuing queries
<!-- chapter: hive-as-relational-data, duration: 3h -->
* Hive as relational data
    * databases, tables
    * HiveQL
    * Data types
    * performing joins
    * built in functions
<!-- chapter: hive-data-management, duration: 4h -->
* Hive data management
    * Hive Data Formats
    * Creating databases with Hive managed tables
    * Loading data
    * Changing the schema
    * Views
    * Storing results
<!-- chapter: hive-and-text, duration: 3h -->
* Hive and text:
    * Overview of text processing
    * String functions
    * Regular expressions
    * Sentiments and N-Grams
<!-- chapter: hive-optimization, duration: 3h -->
* Hive optimization:
    * Query performance
    * Job execution plans
    * Partitioning
    * Bucketing
    * Indexing

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
