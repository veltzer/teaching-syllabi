---
tags:
  - data-and-ai:data-engineering
  - tools:dbt
  - languages:sql
  - concepts:data-transformation
  - concepts:analytics-engineering
level: intermediate
category: data-engineering
duration_hours: 16
audience:
  - audiences:developers
  - audiences:data-engineers
  - audiences:data-analysts
---
<!-- course: dbt -->
# `dbt` (Data Build Tool)

## Description
`dbt` (Data Build Tool) is an open-source transformation framework that enables data teams to transform data in their warehouses using `SQL` and software engineering best practices. This course covers the full `dbt` workflow, including models, transformations, testing, documentation, sources, snapshots, macros, and packages. Participants will learn how to build modular, testable, and well-documented data transformation pipelines using `dbt Core` and `dbt Cloud`.

## Duration
16 hours / 1 day

## Intended Audience
* Data engineers building transformation layers in data warehouses
* Analytics engineers developing data models for business intelligence
* Data analysts seeking to adopt software engineering practices for `SQL`
* `SQL` developers transitioning to modern analytics workflows
* Data platform engineers integrating `dbt` into existing pipelines

## Prerequisites
* Intermediate proficiency in `SQL` (joins, aggregations, window functions, CTEs)
* Basic understanding of data warehousing concepts
* Familiarity with `Git` version control
* Access to a cloud data warehouse (Snowflake, `BigQuery`, `Redshift`, or `Databricks`)
* Basic command-line interface knowledge
* Understanding of `ETL`/`ELT` concepts

## Objectives
* Understand the `dbt` ecosystem and its role in the modern data stack
* Build and organize `dbt` models using best practices
* Implement data transformations with `SQL` and Jinja templating
* Write and run data tests for quality assurance
* Generate and maintain data documentation automatically
* Use sources and snapshots to manage data lineage and history
* Create reusable macros and leverage community packages
* Deploy `dbt` projects in production environments

## Outline
<!-- chapter: introduction-to-dbt-and-the-modern-data-stack, duration: 2h -->
* Introduction to `dbt` and the Modern Data Stack
    * The evolution of data transformation: `ETL` to `ELT`
    * What is `dbt` and where it fits in the data stack
    * `dbt Core` vs `dbt Cloud`
    * `dbt` project structure and key files
    * Setting up a `dbt` project and connecting to a data warehouse
    * The `dbt` workflow: develop, test, document, deploy
    * profiles.yml and connection configuration
<!-- chapter: models-and-materializations, duration: 2h -->
* Models and Materializations
    * What are `dbt` models
    * Writing your first model in `SQL`
    * Materialization types: view, table, incremental, ephemeral
    * Choosing the right materialization strategy
    * Model configurations and overrides
    * `ref()` function and model dependencies
    * Model naming conventions and project organization
    * Staging, intermediate, and mart layers
    * Building a DAG of models
<!-- chapter: jinja-and-advanced-transformations, duration: 2h -->
* Jinja and Advanced Transformations
    * Introduction to Jinja templating in `dbt`
    * Variables, control structures, and loops
    * Using `{{ config() }}` blocks
    * Environment variables and project variables
    * Conditional logic in models
    * Working with `dbt` context variables
    * Generating dynamic `SQL` with Jinja
<!-- chapter: testing-and-data-quality, duration: 2h -->
* Testing and Data Quality
    * Why testing matters in data pipelines
    * Schema tests: unique, not_null, accepted_values, relationships
    * Custom data tests with `SQL` queries
    * Configuring test severity levels
    * Testing strategies for different model layers
    * `dbt test` command and test selection
    * Integration with data quality frameworks
<!-- chapter: documentation-and-data-lineage, duration: 1h -->
* Documentation and Data Lineage
    * Auto-generated documentation from schema files
    * Writing model and column descriptions in `YAML`
    * `dbt docs generate` and `dbt docs serve`
    * The `dbt` documentation site and DAG visualization
    * Data lineage tracking and impact analysis
    * Documentation best practices for large projects
<!-- chapter: sources-and-seeds, duration: 2h -->
* Sources and Seeds
    * Defining sources in `YAML` configuration
    * Source freshness checks and alerts
    * Using `{{ source() }}` in models
    * Loading static data with seeds
    * `When` to use seeds vs other data loading methods
    * Source versioning and multi-database sources
<!-- chapter: snapshots-and-slowly-changing-dimensions, duration: 1h -->
* Snapshots and Slowly Changing Dimensions
    * What are snapshots in `dbt`
    * Snapshot strategies: timestamp and check
    * Configuring snapshot targets and invalidation
    * Implementing Slowly Changing Dimensions (SCD Type 2)
    * Snapshot best practices and limitations
<!-- chapter: macros-packages-and-reusability, duration: 2h -->
* Macros, Packages, and Reusability
    * What are macros and when to use them
    * Writing custom macros
    * Macro arguments and default values
    * `dbt` packages and the `dbt` hub
    * Installing and using community packages (dbt_utils, dbt_expectations)
    * Creating reusable code patterns
    * Overriding default `dbt` behavior with macros
<!-- chapter: deployment-and-production-workflows, duration: 2h -->
* Deployment and Production Workflows
    * `dbt` commands: run, test, build, compile, debug
    * Slim CI with state comparison and deferred runs
    * `dbt Cloud` jobs and scheduling
    * Integrating `dbt` with orchestration tools (`Airflow`, `Dagster`)
    * Environment management (development, staging, production)
    * Version control and `Git` workflows for `dbt` projects

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
