---
tags:
  - tools:great-expectations
  - data-and-ai:data-science
  - practices:testing
level: intermediate
category: big-data
duration_hours: 16
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: great_expectations -->
# `Great Expectations`

## Description
`Great Expectations` is an open-source data quality framework that helps teams validate, document, and profile their data. This course covers the architecture and usage of `Great Expectations`, including defining expectation suites, running validations, generating data docs, and integrating with `Pandas`, `Spark`, and `SQL` backends. Participants will also learn to integrate data quality checks into `CI/CD` pipelines and compare `Great Expectations` with other data quality tools.

## Duration
16 hours / 1 day

## Intended Audience
* Data engineers responsible for pipeline reliability
* Data scientists who need to ensure data quality
* Analytics engineers building trusted data models
* Software developers working on data-intensive applications
* QA engineers extending testing to data validation

## Prerequisites
* Proficiency in `Python` programming
* Familiarity with `Pandas` DataFrames
* Basic understanding of `SQL`
* Experience with data pipelines or `ETL` processes
* Basic command-line interface usage

## Required Knowledge
* `Python` Programming (or equivalent experience)

## Objectives
* Understand data quality concepts and why they matter
* Navigate the `Great Expectations` architecture and components
* Create and manage expectation suites with built-in and custom expectations
* Run validations with checkpoints and review results
* Generate and publish data docs for documentation and collaboration
* Integrate `Great Expectations` with `Pandas`, `Spark`, and `SQL` data sources
* Set up data quality checks in `CI/CD` pipelines
* Configure stores for various backends (filesystem, `S3`, `GCS`, `Azure`)
* Compare `Great Expectations` with Soda and `dbt` tests

## Outline
<!-- chapter: data-quality-concepts, duration: 1h -->
* Data Quality Concepts
    * Why data quality matters in modern data systems
    * Common data quality dimensions (completeness, accuracy, consistency, timeliness)
    * Data contracts and data quality SLAs
    * Shift-left approach to data testing
<!-- chapter: great-expectations-architecture, duration: 2h -->
* `Great Expectations` Architecture
    * Data sources and data connectors
    * Expectations and expectation suites
    * Checkpoints and validation operators
    * Data docs and documentation generation
    * Stores and backends
    * Data context and project structure
<!-- chapter: expectation-suites, duration: 1h -->
* Expectation Suites
    * Creating expectation suites interactively and programmatically
    * Built-in expectations (column values, types, ranges, uniqueness, nullability)
    * Table-level expectations (row count, column presence)
    * Multi-column and cross-table expectations
    * Organizing and versioning expectation suites
<!-- chapter: custom-expectations, duration: 1h -->
* Custom Expectations
    * Writing custom expectation classes
    * Parameterized custom expectations
    * Rendering custom expectations in data docs
    * Packaging and sharing custom expectations
<!-- chapter: validation, duration: 2h -->
* Validation
    * Running validations against data batches
    * Validation results and result format
    * Success and failure thresholds
    * Handling validation failures in pipelines
    * Validation actions (store, notify, update)
<!-- chapter: data-docs, duration: 1h -->
* Data Docs
    * Generating data docs from validation results
    * Hosting data docs locally and on `cloud storage`
    * Customizing data docs appearance
    * Using data docs for team collaboration and auditing
<!-- chapter: profiling, duration: 1h -->
* Profiling
    * Automated data profiling to generate initial expectations
    * Using profiler results to `bootstrap` expectation suites
    * Profiling statistics and data summaries
<!-- chapter: integration-with-pandas-spark-and-sql, duration: 1h -->
* Integration with `Pandas`, `Spark`, and `SQL`
    * `Pandas` backend configuration and usage
    * `Spark` backend for large-scale data validation
    * `SQL` backend for database validation (`PostgreSQL`, `MySQL`, `BigQuery`, `Snowflake`)
    * Choosing the right backend for your data
<!-- chapter: ci-cd-integration, duration: 1h -->
* `CI/CD` Integration
    * Running `Great Expectations` in automated pipelines
    * Integrating with `GitHub Actions`, `GitLab CI`, and `Jenkins`
    * Failing builds on data quality violations
    * Generating reports as pipeline artifacts
<!-- chapter: checkpoint-configuration, duration: 1h -->
* Checkpoint Configuration
    * Defining checkpoints with `YAML` and `Python`
    * Multi-batch and multi-suite checkpoints
    * Checkpoint actions (store results, send notifications, update data docs)
    * Scheduling checkpoint runs
<!-- chapter: stores, duration: 2h -->
* Stores
    * Filesystem stores for local development
    * `S3` and `GCS` stores for cloud deployments
    * `Azure Blob` store configuration
    * Database-backed metadata stores
    * Configuring stores for different environments
<!-- chapter: comparison-with-other-data-quality-tools, duration: 1h -->
* Comparison with Other Data Quality Tools
    * Soda core and Soda cloud comparison
    * `dbt` tests and data quality approach
    * Deequ and `AWS Glue` data quality
    * Choosing the right tool for your stack
<!-- chapter: best-practices, duration: 1h -->
* Best Practices
    * Expectation suite `design patterns`
    * Managing expectations across environments
    * Alerting and notification strategies
    * Scaling data quality validation

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
