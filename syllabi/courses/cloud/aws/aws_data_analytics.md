---
tags:
  - infrastructure:aws
  - infrastructure:cloud
  - concepts:big-data
level: intermediate
category: cloud
duration_hours: 32
audience:
  - audiences:developers
  - audiences:data-engineers
  - audiences:architects
---
<!-- course: aws_data_analytics -->
# `AWS` Data Analytics

## Description
This course provides a comprehensive guide to building and managing data analytics solutions on `AWS`. It covers the full analytics pipeline from data ingestion and storage through processing, analysis, and visualization. Students will learn how to design scalable data lake architectures, implement real-time and batch processing pipelines, and leverage managed analytics services to derive insights from large datasets while maintaining governance and cost efficiency.

## Duration
32 hours / 4 days

## Intended Audience
* Developers building data-intensive applications on `AWS`.
* Data engineers designing and maintaining analytics pipelines.
* Architects planning enterprise data analytics strategies on `AWS`.

## Prerequisites
* Working knowledge of `AWS` core services (`EC2`, `S3`, `VPC`, `IAM`).
* Basic understanding of `SQL` and data concepts.
* Familiarity with the `AWS` Management Console and `CLI`.

## Objectives
* Design and implement a data lake architecture on `AWS` using `S3` and `Lake Formation`.
* Build real-time and batch data ingestion pipelines with `Kinesis` and `Glue`.
* Query and analyze data using `Athena` and `Redshift`.
* Create interactive dashboards and visualizations with `QuickSight`.
* Orchestrate complex data workflows with `Step Functions` and `MWAA`.
* Apply data governance, security, and cost optimization best practices.

## Outline
<!-- chapter: data-lakes-on-aws, duration: 2h -->
* Data Lakes on `AWS`
    * Data lake concepts and architecture patterns
    * `S3` as the data lake foundation
    * Data lake storage layers (raw, curated, refined)
    * Data formats and partitioning strategies (`Parquet`, ORC, `Avro`)
    * `S3` lifecycle policies for analytics workloads
<!-- chapter: aws-lake-formation, duration: 2h -->
* `AWS Lake Formation`
    * Setting up a data lake with `Lake Formation`
    * Data catalog and metadata management
    * Fine-grained access control and permissions
    * Cross-account data sharing
    * Data filters and cell-level security
<!-- chapter: real-time-data-ingestion-with-kinesis, duration: 2h -->
* Real-Time Data Ingestion with `Kinesis`
    * `Kinesis Data Streams` architecture and configuration
    * `Kinesis Data Firehose` for delivery to `S3`, `Redshift`, and `OpenSearch`
    * `Kinesis Data Analytics` for real-time `SQL` and `Apache` `Flink` applications
    * Scaling and capacity management
    * Error handling and dead-letter queues
<!-- chapter: aws-glue, duration: 3h -->
* `AWS Glue`
    * `Glue` crawlers and the data catalog
    * `ETL` jobs with `PySpark` and `Glue Studio`
    * `Glue` job bookmarks and incremental processing
    * `Glue DataBrew` for visual data preparation
    * `Glue` schema registry
    * Optimizing `Glue` job performance
<!-- chapter: querying-with-amazon-athena, duration: 2h -->
* Querying with `Amazon Athena`
    * Serverless querying over `S3` data
    * Table definitions and partitions
    * Performance tuning with partitioning and bucketing
    * `Athena` named work groups and cost controls
    * Federated queries across data sources
<!-- chapter: amazon-redshift, duration: 3h -->
* `Amazon Redshift`
    * Cluster architecture and node types
    * `Redshift Serverless`
    * Loading data into `Redshift` (COPY, `Glue`, `Firehose`)
    * Distribution styles and sort keys
    * `Redshift Spectrum` for querying `S3` data
    * Workload management and concurrency scaling
<!-- chapter: amazon-emr, duration: 3h -->
* `Amazon EMR`
    * `EMR` cluster setup and configuration
    * Running `Spark`, `Hive`, and `Presto` on `EMR`
    * `EMR` on `EKS` and `EMR Serverless`
    * Cost optimization with Spot Instances
    * Monitoring and troubleshooting `EMR` jobs
<!-- chapter: amazon-quicksight, duration: 3h -->
* `Amazon QuickSight`
    * Connecting to data sources
    * Building datasets and SPICE ingestion
    * Creating analyses and interactive dashboards
    * Embedding dashboards in applications
    * Row-level and column-level security
<!-- chapter: amazon-opensearch-service, duration: 3h -->
* `Amazon OpenSearch Service`
    * Cluster provisioning and sizing
    * Ingesting data from `Kinesis`, `Lambda`, and `S3`
    * Querying and visualizing with OpenSearch Dashboards
    * Index management and lifecycle policies
    * Security and fine-grained access control
<!-- chapter: data-pipeline-orchestration, duration: 3h -->
* Data Pipeline Orchestration
    * `AWS Step Functions` for workflow orchestration
    * `MWAA` (Managed Workflows for `Apache` `Airflow`)
    * Building end-to-end analytics pipelines
    * Error handling and retry strategies
    * Scheduling and event-driven triggers with `EventBridge`
<!-- chapter: data-governance-and-security, duration: 3h -->
* Data Governance and Security
    * Data classification and tagging
    * Encryption at `rest` and in transit for analytics services
    * `IAM` policies for analytics workloads
    * Auditing data access with `CloudTrail`
    * Compliance considerations for data analytics
<!-- chapter: cost-optimization-for-analytics, duration: 3h -->
* Cost Optimization for Analytics
    * Choosing the right service for the workload
    * `S3` storage class optimization
    * Reserved capacity and savings plans for `Redshift` and `EMR`
    * Monitoring analytics costs with `Cost Explorer`
    * Right-sizing and auto-scaling strategies

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
