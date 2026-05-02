---
tags:
  - concepts:etl
  - concepts:data-architecture
  - concepts:data-integration
  - concepts:data-transformation
  - concepts:big-data
  - concepts:workflow-orchestration
level: intermediate
category: data-engineering
duration_hours: 40
audience:
  - audiences:data-engineers
  - audiences:analytics-engineers
  - audiences:developers
  - audiences:architects
---
<!-- course: etl_vs_elt_and_modern_data_pipelines -->
# `ETL` vs `ELT` and Modern Data Pipelines

## Description
The data engineering landscape has fundamentally inverted. The classic `ETL` (extract, transform, load) workflow,
designed when storage was expensive and compute was cheap on-prem, has been largely replaced by `ELT` (extract,
load, transform) on top of warehouses and lakehouses where the economics are reversed. Most teams' pipelines
are now a mix of both, often without anyone having made an explicit choice between them.

This five day course covers the modern data-pipeline landscape end to end. It covers the architectural choice
between `ETL` and `ELT`, the orchestration patterns and tools (`Airflow`, `Dagster`, `Prefect`, Temporal),
the integration with `dbt` and the analytics-engineering workflow, idempotent and reprocessable pipelines,
backfill strategy, lineage and observability, the relationship to streaming and `CDC`, and the operational
practices that `make` pipelines maintainable. Examples are drawn from Snowflake, `BigQuery`, `Databricks`,
`Redshift` and lakehouse engines. Participants leave able to design new data pipelines correctly and to fix
the ones they inherited.

## Duration
40 hours / 5 days

## Intended Audience
* data engineers building or maintaining production pipelines
* analytics engineers using `dbt` and modern warehouses
* developers integrating with data platforms
* architects designing data platforms
* engineers migrating from `ETL` tools to `ELT` workflows

## Prerequisites
* working knowledge of `SQL` and at least one analytical store
* basic familiarity with at least one orchestrator (`Airflow`, `Dagster`, `Prefect`)
* exposure to `dbt` is helpful but not required
* some experience operating data pipelines in production

## Objectives
* compare `ETL` and `ELT` and pick the right architecture for a workload
* design pipelines that are idempotent and reprocessable
* operate the major orchestrators with appropriate patterns
* integrate `dbt` into a pipeline correctly
* implement backfill, replay and recovery
* observe and govern data pipelines at scale
* avoid the most common pipeline failure modes

## Outline
<!-- chapter: the-etl-elt-shift, duration: 2h -->
* The `ETL`-`ELT` shift
    * the original `ETL` rationale
    * what changed: cheap warehouse compute, separation of storage and compute
    * the `ELT` rationale and its constraints
    * `EtLT` and the realistic middle ground
    * what `ETL` is still good for
    * how to read a pipeline as `ETL`, `ELT` or `EtLT`
<!-- chapter: extract-and-ingestion, duration: 3h -->
* Extract and ingestion
    * full extract vs incremental extract
    * `CDC`-based ingestion: Debezium, `Fivetran`, `Airbyte`, `Stitch`
    * `API`-based ingestion patterns
    * file-based ingestion and the staging area
    * the connectors-vs-build dilemma
    * cross-reference to the Streaming Data Systems course
<!-- chapter: load-patterns-into-the-warehouse, duration: 3h -->
* Load patterns into the warehouse
    * append-only loads
    * `MERGE` (`upsert`) patterns
    * type-2 historical loads
    * partition-overwrite loads
    * the staging-table-then-swap pattern
    * idempotent loads and re-runnable jobs
<!-- chapter: transformation-with-dbt, duration: 3h -->
* Transformation with `dbt`
    * the `dbt` model as the unit of transformation
    * sources, refs, exposures
    * incremental models and snapshots
    * `dbt` tests and `dbt` docs
    * `dbt-utils`, `dbt-expectations`, `dbt-project-evaluator`
    * `dbt Cloud` vs `dbt Core` vs custom orchestration
    * the analytics-engineering workflow end to end
<!-- chapter: orchestration-fundamentals, duration: 3h -->
* Orchestration fundamentals
    * the orchestrator's job
    * `DAG` modeling: tasks, dependencies, sensors
    * scheduling: cron, sensors, event-driven
    * retries, timeouts, alerting
    * dynamic vs static `DAGs`
    * the right level of granularity for a task
<!-- chapter: airflow-deep-dive, duration: 3h -->
* `Airflow` deep dive
    * the `Airflow` architecture
    * operators, sensors, hooks, providers
    * the `XCom` data flow and its limits
    * `TaskFlow API` and modern idioms
    * `Airflow` deployment options: managed, Helm, custom
    * `Airflow` for `ELT` and `dbt` orchestration
    * `Airflow` anti-patterns
<!-- chapter: dagster-and-the-asset-model, duration: 3h -->
* `Dagster` and the asset model
    * software-defined assets
    * the asset graph as the dependency graph
    * partitioning, backfills, sensors in `Dagster`
    * `Dagster` `IO` managers
    * `dbt` integration in `Dagster`
    * comparing `Dagster` to `Airflow`
<!-- chapter: prefect-and-temporal, duration: 2h -->
* `Prefect` and Temporal
    * `Prefect`'s flow-and-task model
    * `Prefect` deployments and work pools
    * Temporal workflows and activities
    * the case for Temporal in data pipelines
    * comparing the four orchestrators on real workloads
<!-- chapter: idempotent-and-reprocessable-pipelines, duration: 3h -->
* Idempotent and reprocessable pipelines
    * idempotency at the task level
    * idempotency at the pipeline level
    * partitioned outputs as a foundation
    * deterministic transformations
    * cross-reference to the Idempotency course
    * detecting non-idempotent jobs in production
<!-- chapter: backfill-and-replay, duration: 3h -->
* Backfill and replay
    * the backfill problem
    * partition-based backfill
    * the cost of a year-long backfill
    * parallel vs sequential backfill
    * backfilling without contaminating production
    * the `Dagster` backfill model
<!-- chapter: data-lineage-and-observability, duration: 3h -->
* Data lineage and observability
    * column-level lineage
    * `OpenLineage` and `Marquez`
    * `dbt`'s lineage and its limits
    * orchestrator-level observability
    * cross-reference to the Data Quality and Validation course
    * incident triage with lineage
<!-- chapter: cost-and-performance-of-pipelines, duration: 2h -->
* Cost and performance of pipelines
    * warehouse cost as a primary lever
    * partitioning and clustering for cost
    * incremental processing as a cost strategy
    * detecting expensive queries early
    * cross-reference to the Cloud Cost Optimization course
<!-- chapter: streaming-and-batch-side-by-side, duration: 2h -->
* Streaming and batch side by side
    * the `lambda` vs kappa debate revisited
    * Iceberg, `Delta Lake`, `Hudi` for unified storage
    * micro-batch as a middle ground
    * choosing between batch, streaming and micro-batch
    * cross-reference to the Streaming Data Systems course
<!-- chapter: data-pipeline-testing, duration: 3h -->
* Data pipeline testing
    * unit-testable transformations
    * fixture-based pipeline tests
    * end-to-end tests against ephemeral environments
    * data-quality tests at the boundary
    * cross-reference to the Data Quality and Validation course
    * the `dbt`-test discipline
<!-- chapter: pipeline-anti-patterns-and-case-studies, duration: 1h -->
* Pipeline anti-patterns and case studies
    * the all-knowing `DAG`
    * the silent partial-failure pipeline
    * the cron-job graveyard
    * the pipeline that nobody owns
    * a real production migration from `ETL` to `ELT`
    * the analytics team that took ownership of pipelines
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * design walkthrough of a sample pipeline
    * group review of an `Airflow`/`Dagster` `DAG`
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
