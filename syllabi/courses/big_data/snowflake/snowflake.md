---
tags:
  - tools:snowflake
  - data-and-ai:big-data
  - data-and-ai:data-analysis
  - languages:sql
level: intermediate
category: big-data
duration_hours: 24
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: snowflake -->
# Snowflake

## Description
Snowflake is a cloud-native data platform that provides a fully managed data warehouse,
data lake, and data sharing solution. With its unique multi-cluster shared data architecture,
Snowflake separates compute from storage, enabling near-unlimited scalability and concurrency
without the complexity of traditional data warehouses.

Throughout this course, students will learn how to effectively use Snowflake for data
warehousing and analytics. Starting with architecture and core concepts, the course covers
data loading, querying, advanced features like time travel and data sharing, and production
optimization strategies.

## Duration
24 hours / 3 days

## Intended Audience
* Developers and data scientists who want to build and manage data solutions on the Snowflake cloud data platform

## Prerequisites
* `Solid` understanding of `SQL`
* Basic knowledge of data warehousing concepts
* Familiarity with `cloud computing` fundamentals

## Objectives
* Understand Snowflake's unique architecture and how it differs from traditional data warehouses
* Create and manage databases, schemas, and tables effectively
* Load data into Snowflake using various methods including `COPY INTO` and Snowpipe
* Query structured and semi-structured data using Snowflake `SQL` extensions
* Use time travel, cloning, and data sharing features
* Implement stored procedures, UDFs, tasks, and streams
* Configure access control and security
* Optimize performance and manage costs

## Outline
<!-- chapter: introduction-to-cloud-data-warehousing, duration: 1h -->
* Introduction to Cloud Data Warehousing
    * Traditional vs cloud data warehouses
    * The modern data stack
    * Overview of Snowflake
    * Snowflake editions and cloud providers
<!-- chapter: snowflake-architecture, duration: 1h -->
* Snowflake Architecture
    * Virtual warehouses (compute layer)
    * Storage layer
    * Cloud services layer
    * Multi-cluster architecture
    * How compute and storage are separated
<!-- chapter: databases-schemas-and-tables, duration: 1h -->
* Databases, Schemas, and Tables
    * Creating and managing databases
    * Schema organization
    * Table types (permanent, transient, temporary, external)
    * Data types and constraints
    * Sequences and auto-increment
<!-- chapter: loading-data, duration: 2h -->
* Loading Data
    * Stages (internal and external)
    * `COPY INTO` command
    * `File` formats (`CSV`, `JSON`, `Parquet`, `Avro`, ORC)
    * Snowpipe for continuous loading
    * External stages (`S3`, `Azure Blob`, `GCS`)
    * Bulk loading best practices
<!-- chapter: querying-data, duration: 2h -->
* Querying Data
    * Snowflake `SQL` extensions
    * Working with semi-structured data (`JSON`, `XML`, `Avro`)
    * FLATTEN function for nested data
    * LATERAL joins
    * PIVOT and UNPIVOT
    * Recursive CTEs
<!-- chapter: time-travel-and-fail-safe, duration: 1h -->
* Time Travel and Fail-Safe
    * Time travel concepts and configuration
    * Querying historical data
    * Restoring dropped objects
    * Fail-safe period
    * Retention periods and storage impact
<!-- chapter: cloning, duration: 1h -->
* Cloning
    * Zero-copy cloning
    * Cloning databases, schemas, and tables
    * Use cases (development, testing, backups)
<!-- chapter: data-sharing-and-marketplace, duration: 1h -->
* Data Sharing and Marketplace
    * Secure data sharing
    * Creating and managing shares
    * Reader accounts
    * Snowflake Marketplace
    * Data exchange
<!-- chapter: views-and-materialized-views, duration: 1h -->
* Views and Materialized Views
    * Standard views
    * Secure views
    * Materialized views
    * `When` to use each type
<!-- chapter: stored-procedures-and-udfs, duration: 2h -->
* Stored Procedures and UDFs
    * `JavaScript` UDFs
    * `SQL` UDFs
    * `Python` UDFs
    * Stored procedures in `JavaScript` and `Snowflake Scripting`
    * External functions
<!-- chapter: tasks-and-streams, duration: 1h -->
* Tasks and Streams
    * Change data capture with streams
    * Creating and scheduling tasks
    * Task trees and dependencies
    * Monitoring task execution
<!-- chapter: access-control, duration: 2h -->
* Access Control
    * Role-based access control (`RBAC`)
    * System-defined roles
    * Custom roles and role hierarchies
    * Privileges on objects
    * Row-level and column-level security
<!-- chapter: performance-optimization, duration: 2h -->
* Performance Optimization
    * Clustering keys
    * Query result caching
    * Warehouse caching
    * Warehouse sizing and auto-scaling
    * Query profiling and optimization
    * Search optimization service
<!-- chapter: cost-management, duration: 2h -->
* Cost Management
    * Understanding Snowflake credits
    * Warehouse auto-suspend and auto-resume
    * Resource monitors
    * Cost attribution and tracking
    * Storage cost optimization
<!-- chapter: snowpark, duration: 2h -->
* Snowpark
    * Introduction to Snowpark
    * Snowpark for `Python`
    * DataFrame `API`
    * User-defined functions in Snowpark
    * `Machine learning` with Snowpark
<!-- chapter: integration-with-bi-tools, duration: 2h -->
* Integration with BI Tools
    * Connecting to Tableau
    * Connecting to `Power BI`
    * Connecting to Looker
    * ODBC and `JDBC` drivers
    * Partner Connect

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
