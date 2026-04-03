---
tags:
  - tools:dagster
  - data-and-ai:big-data
  - data-and-ai:etl
  - practices:automation
level: intermediate
category: big-data
duration_hours: 16
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: dagster -->
# `Dagster`

## Description
`Dagster` is a modern data orchestration platform built around the concept of software-defined assets. This course covers `Dagster` architecture and core abstractions including assets, ops, jobs, resources, and IO managers. Participants will learn to build, test, and deploy data pipelines with schedules, sensors, and partitions, and integrate `Dagster` with tools like `dbt`, `Spark`, and `Pandas`.

## Duration
16 hours / 2 days

## Intended Audience
* Data engineers building and maintaining data pipelines
* Software developers transitioning to data engineering
* Data scientists who need to operationalize data workflows
* Platform engineers supporting data infrastructure
* Analytics engineers working with `dbt` and orchestration tools

## Prerequisites
* Proficiency in `Python` programming
* Basic understanding of data engineering concepts (`ETL`/`ELT`)
* Familiarity with `SQL` and relational databases
* Understanding of `Docker` basics
* Experience with version control (`Git`)

## Required Knowledge
* `Docker` Fundamentals (or equivalent experience)
* `Python` Programming (or equivalent experience)

## Objectives
* Understand `Dagster` philosophy and the software-defined assets paradigm
* Build asset graphs that model data dependencies and lineage
* Create ops, jobs, and graphs for imperative pipeline definitions
* Configure resources and IO managers for flexible data access
* Set up schedules, sensors, and partitions for automated execution
* Write and run tests for `Dagster` assets and ops
* Integrate `Dagster` with `dbt`, `Spark`, and `Pandas`
* Deploy `Dagster` with `Docker` and `Kubernetes`
* Compare `Dagster` with `Airflow` and `Prefect`

## Outline
<!-- chapter: dagster-overview-and-philosophy, duration: 1h -->
* `Dagster` Overview and Philosophy
    * The evolution of data orchestration
    * Software-defined assets concept
    * `Dagster` architecture: Dagit UI, daemon, and code locations
    * Comparison with task-based orchestrators
    * Setting up a `Dagster` development environment
<!-- chapter: assets-and-asset-graphs, duration: 1h -->
* Assets and Asset Graphs
    * Defining software-defined assets
    * Asset dependencies and lineage
    * Asset materialization and observation
    * Multi-asset definitions
    * Asset groups and code locations
    * Freshness policies and auto-materialization
<!-- chapter: ops-jobs-and-graphs, duration: 1h -->
* Ops, Jobs, and Graphs
    * Defining ops with inputs and outputs
    * Building graphs from ops
    * Creating jobs from graphs and assets
    * Configuration system and config schemas
    * Dynamic outputs and mapping
<!-- chapter: resources-and-io-managers, duration: 1h -->
* Resources and IO Managers
    * Resource concept and dependency injection
    * Built-in resources and custom resource definitions
    * IO managers for reading and writing data
    * Built-in IO managers (filesystem, `S3`, `GCS`, database)
    * Custom IO managers for specific storage backends
    * Resource configuration per environment
<!-- chapter: schedules-and-sensors, duration: 2h -->
* Schedules and Sensors
    * Cron-based schedules
    * Custom schedule functions
    * Sensor definitions and evaluation
    * Asset sensors and multi-asset sensors
    * Run status sensors for monitoring
    * Combining schedules and sensors
<!-- chapter: partitions, duration: 1h -->
* Partitions
    * Time-based partitions (daily, weekly, monthly)
    * Static and dynamic partitions
    * Partitioned assets and jobs
    * Partition mapping between assets
    * Backfilling partitioned assets
<!-- chapter: dagster-types-and-metadata, duration: 1h -->
* `Dagster` Types and Metadata
    * Type system and type checking
    * Metadata annotations on assets and ops
    * Asset metadata and data quality checks
    * Logging and event handling
<!-- chapter: testing, duration: 1h -->
* Testing
    * Unit testing assets and ops
    * Testing with mock resources and IO managers
    * Integration testing with `Dagster` test utilities
    * Testing schedules and sensors
<!-- chapter: dagster-cloud-vs-oss, duration: 1h -->
* `Dagster` Cloud vs OSS
    * `Dagster` Cloud features and managed infrastructure
    * Branch deployments and `CI/CD` integration
    * Alerting and monitoring in `Dagster` Cloud
    * `When` to choose Cloud vs self-hosted
<!-- chapter: dagster-ui-dagit, duration: 1h -->
* `Dagster` UI (Dagit)
    * Navigating the asset graph
    * Monitoring runs and run history
    * Launchpad and run configuration
    * Viewing logs and metadata
    * Global asset lineage view
<!-- chapter: integrations, duration: 1h -->
* Integrations
    * `dbt` integration with `dagster`-`dbt`
    * `Spark` integration with `dagster`-`spark`
    * `Pandas` and `PySpark` DataFrame integration
    * Database integrations (`PostgreSQL`, `Snowflake`, `BigQuery`)
    * `Cloud storage` integrations (`S3`, `GCS`, `ADLS`)
<!-- chapter: comparison-with-airflow-and-prefect, duration: 1h -->
* Comparison with `Airflow` and `Prefect`
    * Architectural differences and trade-offs
    * Migration paths from `Airflow` to `Dagster`
    * Feature comparison and ecosystem maturity
    * Choosing the right orchestrator
<!-- chapter: deployment, duration: 1h -->
* Deployment
    * Local development and single-process deployment
    * `Docker` and `Docker Compose` deployment
    * `Kubernetes` deployment with `Helm` charts
    * Configuring executors (in-process, multiprocess, Celery, K8s)
<!-- chapter: monitoring-and-alerting, duration: 1h -->
* Monitoring and Alerting
    * Built-in monitoring and health checks
    * Setting up alerts (email, `Slack`, `PagerDuty`)
    * Run failure handling and retry policies
    * Performance monitoring and optimization
<!-- chapter: best-practices, duration: 1h -->
* Best Practices
    * Project structure and code organization
    * Environment management (dev, staging, production)
    * `CI/CD` pipelines for `Dagster` projects
    * Data quality and observability patterns

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
