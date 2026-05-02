---
tags:
  - tools:prefect
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
<!-- course: prefect -->
# `Prefect`

## Description
`Prefect` is a modern workflow orchestration framework that makes it easy to build, schedule, and monitor data pipelines. This course covers `Prefect` architecture, flows and tasks, deployments, work pools, blocks, and integration with cloud services and databases. Participants will learn to build resilient data pipelines with retries, caching, and observability, and deploy them using `Docker` and `Kubernetes`.

## Duration
16 hours / 2 days

## Intended Audience
* Data engineers building data pipelines and workflows
* Software developers automating data processes
* Data scientists operationalizing models and analyses
* Platform engineers supporting orchestration infrastructure
* `MLOps` engineers managing `ML` pipelines

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
* Understand `Prefect` architecture and core concepts
* Build flows and tasks with parameters, retries, and caching
* Configure deployments with schedules and triggers
* Set up work pools and workers for distributed execution
* Use blocks for storage, notifications, and integrations
* Monitor and observe flow runs through the `Prefect` UI
* Integrate `Prefect` with `cloud storage` and databases
* Deploy `Prefect` with `Docker` and `Kubernetes`
* Compare `Prefect` with `Airflow` and `Dagster`

## Outline
<!-- chapter: prefect-overview-and-architecture, duration: 1h -->
* `Prefect` Overview and Architecture
    * The evolution of workflow orchestration
    * `Prefect` philosophy: workflows as code
    * Architecture: `Prefect` server, `API`, UI, agents, and workers
    * `Prefect` 2.x design principles
    * Setting up a `Prefect` development environment
<!-- chapter: flows-and-tasks, duration: 2h -->
* Flows and Tasks
    * Defining flows with the @flow decorator
    * Defining tasks with the @task decorator
    * Task dependencies and execution order
    * Flow and task parameters
    * `Return-values` and result handling
    * Subflows and flow composition
    * `Async` flows and tasks
<!-- chapter: retries-and-caching, duration: 1h -->
* Retries and Caching
    * Configuring retry policies on tasks and flows
    * Exponential backoff and jitter
    * Task caching strategies and cache keys
    * Cache expiration policies
    * Handling transient failures gracefully
<!-- chapter: scheduling, duration: 1h -->
* Scheduling
    * Cron schedules and interval schedules
    * RRule schedules for complex patterns
    * Schedule configuration on deployments
    * Pausing and resuming schedules
<!-- chapter: deployments, duration: 1h -->
* Deployments
    * Deployment concepts and lifecycle
    * Creating deployments with `prefect deploy`
    * `prefect`.`yaml` configuration
    * Parameterized deployments
    * Triggering deployments via `API` and UI
    * Deployment versioning and updates
<!-- chapter: work-pools-and-workers, duration: 1h -->
* Work Pools and Workers
    * Work pool types (process, `Docker`, `Kubernetes`, cloud-managed)
    * Worker setup and configuration
    * Infrastructure configuration per work pool
    * Scaling workers for parallel execution
    * Work queue priorities and concurrency limits
<!-- chapter: blocks, duration: 1h -->
* Blocks
    * Block concept and registry
    * Storage blocks (`S3`, `GCS`, `Azure Blob`, `GitHub`)
    * Notification blocks (Slack, email, `PagerDuty`)
    * Database blocks and connection management
    * Secret blocks for credential management
    * Creating custom blocks
<!-- chapter: artifacts, duration: 1h -->
* Artifacts
    * Creating artifacts from flow and task runs
    * `Markdown`, table, and link artifacts
    * Using artifacts for data lineage and documentation
    * Viewing artifacts in the `Prefect` UI
<!-- chapter: prefect-cloud-vs-self-hosted, duration: 1h -->
* `Prefect` Cloud vs Self-Hosted
    * `Prefect` Cloud features and managed infrastructure
    * Workspaces and `RBAC`
    * Automations and event-driven triggers
    * Self-hosted `Prefect` server setup
    * `When` to choose Cloud vs self-hosted
<!-- chapter: prefect-ui, duration: 1h -->
* `Prefect` UI
    * Navigating flow runs and task runs
    * Monitoring deployment status
    * Viewing logs and artifacts
    * Filtering and searching runs
    * Dashboard overview and notifications
<!-- chapter: integration-with-cloud-storage-and-databases, duration: 1h -->
* Integration with `Cloud Storage` and Databases
    * Reading and writing to `S3`, `GCS`, and `Azure Blob`
    * Database operations with `SQLAlchemy` and connection blocks
    * Integration with Snowflake, `BigQuery`, and `Databricks`
    * Working with Pandas and Dask DataFrames
<!-- chapter: comparison-with-airflow-and-dagster, duration: 1h -->
* Comparison with `Airflow` and `Dagster`
    * Architectural differences and trade-offs
    * DAG-based vs dynamic workflow execution
    * Feature comparison and ecosystem maturity
    * Migration considerations from `Airflow`
<!-- chapter: testing-flows, duration: 1h -->
* Testing Flows
    * Unit testing flows and tasks
    * Mocking external dependencies
    * Testing with `Prefect` test utilities
    * Integration testing strategies
<!-- chapter: docker-and-kubernetes-deployment, duration: 1h -->
* `Docker` and `Kubernetes` Deployment
    * `Docker` image builds for `Prefect` flows
    * `Docker` work pool configuration
    * `Kubernetes` deployment with Helm
    * `Kubernetes` work pool and job templates
    * Production deployment patterns
<!-- chapter: monitoring-and-observability, duration: 1h -->
* Monitoring and Observability
    * Flow run notifications and alerts
    * Automations for failure handling
    * Integrating with external monitoring tools
    * Performance metrics and optimization
    * Logging best practices

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
