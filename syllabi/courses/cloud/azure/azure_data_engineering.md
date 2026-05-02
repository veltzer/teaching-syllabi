---
tags:
  - infrastructure:azure
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
<!-- course: azure_data_engineering -->
# `Azure` Data Engineering

## Description
This course covers the design and implementation of data solutions on `Microsoft Azure`. Participants will learn to build end-to-end data pipelines using `Azure Data Factory`, process large-scale data with `Azure Synapse Analytics` and `Azure Databricks`, and implement real-time streaming with `Azure Stream Analytics` and `Event Hubs`. The course also addresses data governance, `Delta Lake`, and modern data architecture patterns including data mesh on `Azure`.

## Duration
32 hours / 4 days

## Intended Audience
* Developers building data-intensive applications on `Azure`
* Data engineers designing and maintaining data pipelines
* Architects planning enterprise data platforms on `Azure`

## Prerequisites
* Basic understanding of `Azure` services and the `Azure` portal
* Familiarity with `SQL` and relational database concepts
* Basic programming experience (`Python` or `SQL`)
* Understanding of data concepts (`ETL`, data warehousing, data lakes)

## Objectives
* Design and implement data storage solutions using `Azure Data Lake Storage Gen2` and `Azure SQL Database`
* Build data pipelines with `Azure Data Factory`
* Process and analyze data with `Azure Synapse Analytics` and `Azure Databricks`
* Implement real-time data streaming with `Azure Stream Analytics` and `Event Hubs`
* Apply data governance practices using `Microsoft Purview`
* Optimize data solutions for performance and cost

## Outline
<!-- chapter: azure-data-platform-overview, duration: 2h -->
* `Azure` Data Platform Overview
    * Data services landscape on `Azure`
    * Choosing the right data store
    * Data architecture patterns (`lambda`, kappa, medallion)
    * Data roles and responsibilities
<!-- chapter: azure-data-lake-storage-gen2, duration: 3h -->
* `Azure Data Lake Storage Gen2`
    * Hierarchical namespace and filesystem semantics
    * Access control (`RBAC`, `ACLs`, shared key)
    * Data organization strategies and folder structures
    * Performance tuning and best practices
    * Integration with analytics services
<!-- chapter: azure-data-factory, duration: 4h -->
* `Azure Data Factory`
    * Pipelines, activities, and datasets
    * Linked services and integration runtimes
    * Data flows (mapping and wrangling)
    * Triggers (schedule, tumbling window, event-based)
    * Parameterization and dynamic content
    * Monitoring and troubleshooting pipelines
    * `CI/CD` for `Data Factory`
<!-- chapter: azure-synapse-analytics, duration: 4h -->
* `Azure Synapse Analytics`
    * Synapse workspace architecture
    * Dedicated `SQL` pools (formerly `SQL DW`)
    * Serverless `SQL` pools
    * `Apache Spark` pools
    * Synapse Pipelines and integration with `Data Factory`
    * `Synapse Link` for operational analytics
    * Security and access control in Synapse
<!-- chapter: azure-databricks, duration: 4h -->
* `Azure Databricks`
    * Workspace setup and cluster management
    * Notebooks and collaborative development
    * `Apache Spark` on `Databricks`
    * `Delta Lake` on `Azure`
    * Delta Live Tables
    * `Unity` Catalog for data governance
    * `MLflow` integration
<!-- chapter: real-time-data-processing, duration: 2h -->
* Real-Time Data Processing
    * `Azure Event Hubs` (partitions, consumer groups, capture)
    * `Azure Stream Analytics` (windowing, `temporal` queries)
    * Processing guarantees and late-arriving data
    * Real-time dashboards and alerting
<!-- chapter: azure-cosmos-db-for-analytics, duration: 2h -->
* `Azure Cosmos DB` for Analytics
    * Multi-model capabilities and `API` choices
    * Analytical store and `Synapse Link`
    * Partitioning strategies for analytics
    * Global distribution and consistency models
<!-- chapter: azure-sql-database, duration: 2h -->
* `Azure SQL Database`
    * Deployment options (single database, elastic pool, managed instance)
    * Performance tiers and scaling
    * Intelligent query processing
    * Data migration strategies
<!-- chapter: power-bi-integration, duration: 2h -->
* `Power BI` Integration
    * Connecting `Power BI` to `Azure` data services
    * DirectQuery vs. import mode
    * Dataflows and data refresh patterns
    * Row-level security
<!-- chapter: data-governance-with-microsoft-purview, duration: 3h -->
* Data Governance with `Microsoft Purview`
    * Data catalog and discovery
    * Data lineage tracking
    * Classification and sensitivity labels
    * Glossary management
    * Integration with `Azure` data services
<!-- chapter: modern-data-architecture-patterns, duration: 2h -->
* Modern Data Architecture Patterns
    * Data mesh principles on `Azure`
    * Domain-oriented data ownership
    * Data products and self-serve infrastructure
    * Federated governance
<!-- chapter: cost-optimization, duration: 2h -->
* Cost Optimization
    * Monitoring and analyzing data platform costs
    * Reserved capacity and spot instances
    * Storage tiering and lifecycle management
    * Compute auto-scaling strategies

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
