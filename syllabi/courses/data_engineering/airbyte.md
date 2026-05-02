---
tags:
  - data-and-ai:data-engineering
  - tools:airbyte
  - practices:elt
  - practices:data-pipeline
  - concepts:data-integration
level: intermediate
category: data-engineering
duration_hours: 16
audience:
  - audiences:data-engineers
  - audiences:analytics-engineers
---
<!-- course: airbyte -->
# `Airbyte`

## Description
`Airbyte` is an open-source data integration platform that enables engineers to move data from hundreds of sources into warehouses, lakes, and other destinations using a modern `ELT` approach. This course covers the full `Airbyte` workflow, from understanding its architecture and deploying it locally or in the cloud to configuring sources, destinations, and sync modes for reliable data movement. Participants will learn to extend `Airbyte` by building custom connectors using the `Connector Development Kit (CDK)`, normalise ingested data, and orchestrate `Airbyte` syncs alongside `dbt` transformations and `Apache Airflow` DAGs. The course also covers monitoring, alerting, and operational best practices for running `Airbyte` in production.

## Duration
16 hours / 2 days

## Intended Audience
* Data engineers building and maintaining data ingestion pipelines
* Analytics engineers managing data warehouse ingestion and transformation workflows
* Platform engineers deploying and operating `Airbyte` in production
* Data architects designing modern `ELT` data stacks
* Engineers migrating from traditional `ETL` tools to modern open-source alternatives

## Prerequisites
* Familiarity with `ELT`/`ETL` concepts and data pipeline fundamentals
* Basic knowledge of `SQL` and relational data modelling
* Experience with `Python` programming for custom connector development
* Basic understanding of `Docker` and containerisation
* Familiarity with cloud data warehouses such as Snowflake, `BigQuery`, or `Redshift`

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `Docker` Fundamentals (or equivalent experience)

## Objectives
* Understand the `ELT` paradigm and how `Airbyte` fits into the modern data stack
* Describe `Airbyte` architecture and its core components
* Deploy `Airbyte` locally and in cloud environments
* Configure sources and destinations from the `Airbyte` connector catalogue
* Select and configure appropriate sync modes for different data change patterns
* Build custom `Airbyte` connectors using the `Connector Development Kit (CDK)`
* Apply and configure `Airbyte`'s data normalisation to produce typed destination tables
* Orchestrate `Airbyte` syncs with `Apache Airflow` and coordinate with `dbt` transformations
* Monitor sync health, diagnose failures, and configure alerting

## Outline
<!-- chapter: introduction-to-elt-and-airbyte, duration: 2h -->
* Introduction to `ELT` and `Airbyte`
    * `ETL` vs `ELT`: paradigm shift and modern data stack implications
    * What is `Airbyte` and how it compares to `Fivetran`, Stitch, and `Meltano`
    * Core `Airbyte` concepts: sources, destinations, connections, and catalogs
    * The `Airbyte` open-source ecosystem and cloud offering
    * Overview of the `Airbyte` connector catalogue: hundreds of pre-built connectors
    * `Airbyte`'s role in the modern data stack alongside `dbt`, `Airflow`, and data warehouses
    * `When` `Airbyte` is the right choice and when to consider alternatives
<!-- chapter: airbyte-architecture, duration: 1h -->
* `Airbyte` Architecture
    * Core components: web app, server, scheduler, worker, and database
    * The connector abstraction: source connectors and destination connectors
    * How `Airbyte` orchestrates sync jobs using Temporal
    * Configuration and state storage in `PostgreSQL`
    * The `Airbyte Protocol`: the contract between `Airbyte` and connectors
    * Messages in the `Airbyte Protocol`: RECORD, STATE, CATALOG, LOG, `TRACE`
    * Data flow: from source extraction to destination loading
<!-- chapter: setting-up-airbyte, duration: 1h -->
* Setting Up `Airbyte`
    * Deploying `Airbyte` locally with `Docker Compose`
    * Deploying `Airbyte` on `Kubernetes` with Helm
    * `Airbyte Cloud`: managed deployment option and differences from self-hosted
    * Navigating the `Airbyte` web UI
    * Configuring `Airbyte` settings: workspace, logging, and notifications
    * Authentication and `RBAC` in `Airbyte`
<!-- chapter: sources-and-destinations-catalog, duration: 2h -->
* Sources and Destinations Catalog
    * Browsing and selecting sources from the connector catalogue
    * Configuring common sources: `PostgreSQL`, `MySQL`, `Salesforce`, Stripe, `GitHub`
    * Configuring common destinations: Snowflake, `BigQuery`, `Redshift`, `S3`, `Databricks`
    * Setting up schema and table selection per connection
    * Understanding the stream catalog and field-level selection
    * Connector versioning and upgrading connectors
    * Connector reliability tiers: generally available, beta, and community
<!-- chapter: connection-configuration-and-sync-modes, duration: 2h -->
* Connection Configuration and Sync Modes
    * What is a connection and how it links a source to a destination
    * Full refresh sync: overwrite vs append
    * Incremental sync: append and deduped+history modes
    * Cursor fields and primary keys for incremental replication
    * Sync scheduling: manual, cron, and `API`-triggered
    * Configuring replication frequency and performance options
    * Namespace configuration and table prefixes in the destination
    * Handling schema changes: propagation settings and breaking changes
<!-- chapter: custom-connectors-with-the-cdk, duration: 3h -->
* Custom Connectors with the `CDK`
    * Why custom connectors are needed and when to build vs extend
    * Overview of the `Python CDK` for building `Airbyte` source connectors
    * Anatomy of a connector: `config.json`, `catalog.json`, and the `Python` entry point
    * Implementing a `Source` class with check, discover, and `read` methods
    * Low-code `CDK`: declarative `YAML`-based connector configuration
    * Handling authentication: `OAuth`, `API keys`, `Basic Auth`
    * Implementing incremental sync with state management
    * Packaging and publishing connectors to the `Airbyte` connector registry
    * Testing connectors with the `Airbyte` standard test suite
<!-- chapter: data-normalization, duration: 2h -->
* Data Normalization
    * What is `Airbyte`'s basic normalisation feature
    * Raw tables vs normalised tables in the destination
    * How `Airbyte` uses `dbt` under the hood for normalisation
    * Type casting, deduplication, and SCD (slowly changing dimension) handling
    * Customising normalisation with custom `dbt` transformations
    * Limitations of basic normalisation and when to use custom `dbt` models
    * Incremental normalisation and performance considerations
    * Transitioning from basic normalisation to fully custom `dbt` pipelines
<!-- chapter: orchestration-with-airflow-and-dbt, duration: 2h -->
* Orchestration with `Airflow` and `dbt`
    * Why orchestration is needed beyond `Airbyte`'s built-in scheduler
    * Triggering `Airbyte` syncs from `Apache Airflow` using the `AirbyteTriggerSyncOperator`
    * Waiting for sync completion with `AirbyteJobSensor`
    * Building end-to-end `ELT` DAGs: `Airbyte` sync → `dbt` transformation
    * Using the `Airbyte` `API` for programmatic connection management
    * `dbt` and `Airbyte` source definitions for automatic model generation
    * Managing `Airbyte` connections as code with `Terraform`
    * Best practices for coordinating ingestion and transformation pipelines
<!-- chapter: monitoring-and-alerting, duration: 1h -->
* Monitoring and Alerting
    * Monitoring sync status and run history in the `Airbyte` UI
    * Understanding sync logs and diagnosing common connector failures
    * `Airbyte` metrics and health endpoints
    * Integrating `Airbyte` alerts with Slack, email, and `PagerDuty`
    * Using the `Airbyte` `API` to query connection and job status programmatically
    * Data freshness monitoring with external tools
    * Common failure patterns and troubleshooting strategies
    * SLAs for data ingestion and operational best practices

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
