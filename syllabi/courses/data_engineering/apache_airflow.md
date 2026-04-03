---
tags:
  - data-and-ai:data-engineering
  - tools:airflow
  - languages:python
  - concepts:workflow-orchestration
  - concepts:scheduling
level: intermediate
category: data-engineering
duration_hours: 16
audience:
  - audiences:developers
  - audiences:data-engineers
  - audiences:devops
---
<!-- course: apache_airflow -->
# `Apache Airflow`

## Description
`Apache Airflow` is an open-source platform for programmatically authoring, scheduling, and monitoring workflows. This course covers the core concepts of `Airflow`, including DAGs, operators, sensors, scheduling, XComs, connections, and monitoring. Participants will learn how to design and implement robust data pipelines, manage dependencies between tasks, and apply best practices for building production-grade workflow orchestration systems.

## Duration
16 hours / 2 days

## Intended Audience
* Data engineers building and maintaining data pipelines
* `Python` developers working with workflow orchestration
* `DevOps` engineers managing `Airflow` deployments
* Data analysts automating data processing workflows
* Software engineers integrating `Airflow` into data platforms

## Prerequisites
* Intermediate proficiency in `Python` programming
* Basic understanding of `SQL` and relational databases
* Familiarity with command-line tools and terminal usage
* Understanding of `ETL`/`ELT` concepts and data pipeline fundamentals
* Basic knowledge of `Docker` and containerization

## Required Knowledge
* `Docker` Fundamentals (or equivalent experience)
* `Python` Programming (or equivalent experience)

## Objectives
* Understand `Airflow` architecture and its core components
* Design and implement DAGs for complex data workflows
* Use built-in and custom operators and sensors effectively
* Configure scheduling, retries, and task dependencies
* Exchange data between tasks using XComs
* Manage connections, variables, and secrets securely
* Monitor and troubleshoot DAG runs and task failures
* Apply best practices for production-grade `Airflow` deployments

## Outline
<!-- chapter: introduction-to-apache-airflow, duration: 1h -->
* Introduction to `Apache Airflow`
    * What is workflow orchestration
    * `Airflow` architecture overview
    * Core components: web server, scheduler, executor, metadata database
    * Executor types: SequentialExecutor, LocalExecutor, CeleryExecutor, KubernetesExecutor
    * Installing and configuring `Airflow`
    * Navigating the `Airflow` web UI
<!-- chapter: dags-and-task-dependencies, duration: 2h -->
* DAGs and Task Dependencies
    * What is a DAG (Directed Acyclic Graph)
    * DAG definition and configuration
    * Default arguments and DAG-level settings
    * Defining task dependencies with bitshift operators and set_upstream/set_downstream
    * Branching and conditional logic with BranchPythonOperator
    * Trigger rules and task lifecycle
    * DAG serialization and DAG bags
    * Dynamic DAG generation
<!-- chapter: operators, duration: 2h -->
* Operators
    * Overview of operator types
    * BashOperator and PythonOperator
    * Database operators: PostgresOperator, MySqlOperator
    * Cloud operators: `S3`, `GCS`, `BigQuery`
    * DockerOperator and KubernetesPodOperator
    * Transfer operators for moving data between systems
    * Creating custom operators
    * `TaskFlow API` and the @task decorator
<!-- chapter: sensors, duration: 2h -->
* Sensors
    * What are sensors and how they work
    * FileSensor, S3KeySensor, HttpSensor
    * ExternalTaskSensor for cross-DAG dependencies
    * Sensor modes: poke vs reschedule
    * Sensor timeouts and configuration
    * Deferrable operators and `async` sensors
    * Smart sensors and resource optimization
<!-- chapter: scheduling-and-execution, duration: 2h -->
* Scheduling and Execution
    * Cron expressions and timetables
    * Data intervals and logical dates
    * Backfilling and catchup behavior
    * Manual triggers and DAG run parameters
    * Pools and concurrency management
    * Priority weights and task queues
    * SLAs and alerting
<!-- chapter: xcoms-and-data-passing, duration: 1h -->
* XComs and Data Passing
    * What are XComs (cross-communications)
    * Pushing and pulling XComs
    * XCom backends for large data
    * Limitations of XComs and `when` to use external storage
    * `TaskFlow API` for implicit XCom passing
    * Custom XCom backends
<!-- chapter: connections-variables-and-security, duration: 2h -->
* Connections, Variables, and Security
    * Managing connections in the UI and via `CLI`
    * Connection types and hooks
    * Variables and configuration management
    * Secrets backends (`HashiCorp Vault`, `AWS Secrets Manager`)
    * Role-based access control (`RBAC`)
    * DAG-level permissions and access policies
<!-- chapter: monitoring-logging-and-troubleshooting, duration: 2h -->
* Monitoring, Logging, and Troubleshooting
    * Task logs and log management
    * `Airflow` metrics and health checks
    * Integration with `Prometheus` and `Grafana`
    * Email and `Slack` alerting on task failures
    * Debugging failed tasks and common issues
    * Performance tuning and scaling strategies
<!-- chapter: best-practices-and-production-patterns, duration: 2h -->
* Best Practices and Production Patterns
    * DAG `design patterns` and anti-patterns
    * Idempotency and atomicity in tasks
    * Testing DAGs and operators
    * `CI/CD` for `Airflow` deployments
    * Managing DAG versioning and migrations
    * Organizing DAGs in large projects
    * Resource management and cost optimization

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
