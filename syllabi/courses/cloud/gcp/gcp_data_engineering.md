---
tags:
  - infrastructure:cloud
  - infrastructure:gcp
  - concepts:big-data
  - data-and-ai:data-engineering
  - data-and-ai:big-data
  - data-and-ai:streaming
  - data-and-ai:data-analytics
  - security:iam
level: intermediate
category: big-data
duration_hours: 32
audience:
  - audiences:data-engineers
  - audiences:developers
  - audiences:architects
---
<!-- course: gcp_data_engineering -->
# `Google Cloud Platform` - Data Engineering

## Description
This course covers data engineering on `Google Cloud Platform`. Participants will learn to design
and build data processing systems, implement data pipelines for batch and streaming workloads,
and manage storage and analytics solutions at scale. The course covers `BigQuery`, Dataflow,
Dataproc, Pub/Sub, and the full `GCP` data stack. It is aligned with the Professional Data
Engineer certification path.

## Duration
32 hours / 4 days

## Intended Audience
* Data engineers building data pipelines on `GCP`
* Software engineers transitioning to data engineering roles
* Architects designing data platforms and analytics solutions
* Data analysts who need to build production-grade data workflows

## Prerequisites
* Proficiency in `SQL` and at least one programming language (`Python` or `Java`)
* Basic understanding of distributed systems and data processing
* Familiarity with `GCP` core services or equivalent cloud platform
* Understanding of batch and stream processing concepts

## Objectives
* Design and implement data processing pipelines using Dataflow and Dataproc
* Build and optimize analytics solutions with `BigQuery`
* Implement real-time streaming architectures with Pub/Sub
* Apply data governance, security, and compliance controls
* Manage and automate data workloads with Cloud `Composer`

## Outline
<!-- chapter: data-engineering-on-google-cloud, duration: 3h -->
* Data Engineering on `Google Cloud`
    * `GCP` data services overview
    * Data lifecycle: ingestion, processing, storage, and analysis
    * Security and compliance: `IAM`, encryption, and data governance
    * Data residency and regulatory compliance
    * Multi-environment architectures (dev, staging, production)
<!-- chapter: data-ingestion, duration: 3h -->
* Data Ingestion
    * Batch ingestion: Storage Transfer Service, Transfer Appliance
    * Streaming ingestion with Pub/Sub
    * Managed `Kafka` on `GCP`
    * Change data capture with Datastream
    * Database Migration Service
    * Data integration with Cloud Data Fusion
<!-- chapter: batch-processing, duration: 3h -->
* Batch Processing
    * Dataflow for batch pipelines (`Apache` Beam)
    * Dataproc for `Hadoop` and `Spark` workloads
    * Dataproc Serverless
    * `BigQuery` for `SQL`-based batch processing
    * Transformation patterns and data cleaning
    * Dataform for `SQL`-based data transformation
<!-- chapter: stream-processing, duration: 3h -->
* Stream Processing
    * Pub/Sub architecture and delivery guarantees
    * Dataflow for streaming pipelines
    * Windowing, watermarks, and late-arriving data
    * Exactly-once processing semantics
    * Streaming into `BigQuery` and `Cloud Storage`
    * Real-time dashboards and alerting
<!-- chapter: bigquery, duration: 5h -->
* `BigQuery`
    * Architecture: storage, compute, and columnar format
    * Table design: partitioning, clustering, and nested fields
    * Query optimization and slot management
    * `BigQuery` Editions and reservations
    * Materialized views and BI Engine
    * `BigQuery` `ML` for in-database `machine learning`
    * `BigQuery` Data Transfer Service
    * Cost management and query optimization
<!-- chapter: data-storage, duration: 4h -->
* Data Storage
    * `Cloud Storage`: classes, lifecycle rules, and organization
    * Cloud `SQL` and `AlloyDB` for relational workloads
    * `Cloud Spanner` for globally distributed data
    * `Firestore` and Bigtable for `NoSQL` workloads
    * Memorystore for caching
    * Choosing the right storage service
<!-- chapter: data-lakes-and-governance, duration: 4h -->
* Data Lakes and Governance
    * BigLake for unified data lake and warehouse
    * Dataplex for data governance and discovery
    * Dataplex Catalog for metadata management
    * Data quality rules and profiling
    * Analytics Hub for data sharing
    * Column-level security and data masking
<!-- chapter: workflow-orchestration, duration: 3h -->
* Workflow Orchestration
    * Cloud `Composer` (`Apache Airflow`) for DAG-based orchestration
    * Workflows for `API`-based orchestration
    * `CI/CD` for data pipelines
    * Job scheduling and dependency management
    * Error handling and retry strategies
<!-- chapter: monitoring-and-optimization, duration: 4h -->
* Monitoring and Optimization
    * `Cloud Monitoring` for pipeline health
    * `BigQuery` admin panel and query diagnostics
    * Resource optimization: autoscaling and right-sizing
    * Cost management: persistent vs job-based clusters
    * Troubleshooting data pipeline failures
    * Backup, recovery, and disaster mitigation

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
