---
tags:
  - tools:databricks
  - data-and-ai:big-data
  - languages:python
  - languages:sql
level: intermediate
category: big-data
duration_hours: 24
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: databricks -->
# `Databricks`

## Description
This course provides a comprehensive introduction to the `Databricks` Lakehouse Platform, covering
workspace management, compute configuration, `Delta Lake`, `Spark` integration, `SQL` analytics, and
data governance with `Unity Catalog`. Participants will learn to build production-grade data pipelines
using the medallion architecture, leverage `MLflow` for `machine learning` workflows, and manage
streaming ingestion with `Auto Loader`. The course also addresses collaboration, security, and cost
management best practices on the `Databricks` platform.

## Duration
24 hours / 3 days

## Intended Audience
* software developers working with data platforms
* data scientists building analytical and `ML` workflows

## Prerequisites
* Basic proficiency in `Python` programming
* Familiarity with `SQL` queries
* Understanding of data engineering concepts (tables, schemas, `ETL`)
* Basic knowledge of `Apache Spark` concepts

## Required Knowledge
* `Python` Programming (or equivalent experience)

## Objectives
* **Navigate and configure the `Databricks` workspace** including notebooks, repos, clusters, and compute resources
* **Build and manage `Delta Lake` tables** with ACID transactions, time travel, and schema evolution
* **Develop data pipelines using the medallion architecture** (bronze, silver, gold) with `Spark` and `SQL`
* **Implement data governance** using `Unity Catalog` for access control, lineage, and compliance
* **Integrate `machine learning` workflows** using `MLflow` for experiment tracking and model management
* **Design production jobs and streaming pipelines** using `Databricks` workflows and `Auto Loader`

## Outline
<!-- chapter: databricks-platform-overview, duration: 3h -->
* `Databricks` Platform Overview
    * What is `Databricks`
        * Lakehouse architecture
        * `Databricks` vs traditional data platforms
        * Key platform components
    * Workspace and notebooks
        * Workspace organization
        * Notebook creation and management
        * Multi-language support (`Python`, `SQL`, `Scala`, `R`)
        * Notebook versioning and collaboration
        * `Databricks` Repos and `Git` integration
    * Clusters and compute
        * Cluster types (all-purpose, job, `SQL` warehouse)
        * Cluster configuration and auto-scaling
        * `Databricks Runtime` versions
        * Spot instances and cost optimization
        * Cluster policies
<!-- chapter: delta-lake, duration: 3h -->
* `Delta Lake`
    * `Delta Lake` fundamentals
        * ACID transactions on data lakes
        * Delta table format and transaction log
        * Schema enforcement
    * Time travel
        * Querying historical versions
        * Restoring previous versions
        * Retention policies
    * Schema evolution
        * Adding and modifying columns
        * Merge schema options
        * Schema evolution best practices
    * `Delta Lake` operations
        * MERGE (upserts)
        * DELETE and UPDATE
        * Optimize and Z-ordering
        * Vacuum and maintenance
<!-- chapter: spark-on-databricks, duration: 2h -->
* `Spark` on `Databricks`
    * DataFrame operations
        * Reading and writing data
        * Transformations and actions
        * Joins and aggregations
        * User-defined functions
    * Performance optimization
        * Adaptive query execution
        * Caching strategies
        * Broadcast joins
        * Partitioning strategies
    * Structured streaming
        * Streaming concepts on `Databricks`
        * Stream processing with `Delta Lake`
        * Watermarking and late data handling
<!-- chapter: sql-analytics, duration: 2h -->
* `SQL` Analytics
    * `Databricks SQL`
        * `SQL` warehouses
        * Query editor and history
        * `SQL` dashboards and visualizations
    * Working with Delta tables via `SQL`
        * DDL and DML operations
        * Views and materialized views
        * Query optimization
    * Connecting BI tools
        * `JDBC`/ODBC connectivity
        * Partner integrations
<!-- chapter: unity-catalog, duration: 2h -->
* `Unity Catalog`
    * Data governance fundamentals
        * Three-level namespace (catalog, schema, table)
        * Metastore configuration
        * Data discovery and search
    * Access control
        * Grants and privileges
        * Row-level and column-level security
        * Dynamic views for data masking
    * Data lineage
        * Automatic lineage tracking
        * Column-level lineage
        * Lineage visualization
    * Data sharing
        * `Delta Sharing` protocol
        * Sharing across organizations
        * Open sharing and managed sharing
<!-- chapter: mlflow-integration, duration: 2h -->
* `MLflow` Integration
    * Experiment tracking
        * Logging parameters, metrics, and artifacts
        * Experiment comparison and visualization
        * Autologging support
    * Model registry
        * Model versioning and staging
        * Model deployment from registry
        * Approval workflows
    * `MLflow` on `Databricks`
        * Managed `MLflow` features
        * Integration with notebooks
        * Serving models from `Databricks`
<!-- chapter: jobs-and-workflows, duration: 2h -->
* Jobs and Workflows
    * Job creation and scheduling
        * Task orchestration
        * Job clusters
        * Scheduling and triggers
        * Parameterized jobs
    * Workflow patterns
        * Multi-task workflows
        * Task dependencies and branching
        * Error handling and retries
        * Notifications and alerts
    * `Auto Loader` for streaming ingestion
        * `File` notification and directory listing modes
        * Schema inference and evolution
        * Supported `file` formats
        * Incremental ingestion patterns
<!-- chapter: medallion-architecture, duration: 2h -->
* Medallion Architecture
    * Bronze layer
        * Raw data ingestion
        * Data landing patterns
        * Metadata enrichment
    * Silver layer
        * Data cleaning and validation
        * Deduplication and enrichment
        * Conforming data types
    * Gold layer
        * Business-level aggregations
        * Feature tables
        * Serving layer design
    * Architecture best practices
        * Layer boundaries and contracts
        * Data quality at each layer
        * Performance considerations
<!-- chapter: collaboration-features, duration: 2h -->
* Collaboration Features
    * Notebook collaboration
        * Real-time co-editing
        * Comments and reviews
        * Notebook workflows
    * `Databricks` Repos
        * `Git` integration workflows
        * Branching and pull requests
        * `CI/CD` integration
    * Sharing and permissions
        * Workspace-level permissions
        * Object-level access control
        * Dashboard sharing
<!-- chapter: security-and-access-control, duration: 2h -->
* Security and Access Control
    * Authentication and identity
        * Identity providers and SSO
        * Service principals
        * Personal access tokens
    * Network security
        * `VPC`/`VNet` peering
        * `Private link`
        * `IP` access lists
    * Data security
        * Encryption at `rest` and in transit
        * Secrets management
        * Audit logging
<!-- chapter: cost-management, duration: 2h -->
* Cost Management
    * Understanding `Databricks` pricing
        * DBU consumption model
        * Compute vs storage costs
        * Pricing tiers
    * Cost optimization strategies
        * Cluster right-sizing
        * Auto-termination policies
        * Spot instance usage
        * `SQL` warehouse sizing
    * Monitoring and budgeting
        * Usage dashboards
        * Cost attribution
        * Budget alerts

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
