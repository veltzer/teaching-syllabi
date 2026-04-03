---
tags:
  - data-and-ai:data-engineering
  - tools:apache-nifi
  - practices:data-pipeline
  - practices:data-flow
  - concepts:etl
level: intermediate
category: data-engineering
duration_hours: 24
audience:
  - audiences:data-engineers
  - audiences:devops
---
<!-- course: apache_nifi -->
# `Apache NiFi`

## Description
`Apache NiFi` is a powerful, open-source data integration and flow management platform that enables the automation of data movement between disparate systems with a visual, drag-and-drop interface. This course covers the full breadth of `NiFi`, from understanding its core architecture and components to designing complex data flows, configuring processors, managing back-pressure, and securing multi-tenant deployments. Participants will learn how to build reliable, scalable, and observable data pipelines that handle a wide variety of data formats and protocols, including `HTTP`, `Kafka`, `HDFS`, `S3`, databases, and more. The course also covers `NiFi Registry` for version-controlled flow management, `MiNiFi` for edge data collection, and high-availability clustering. By the end of the course, participants will be able to design and operate production-grade `NiFi` data flows.

## Duration
24 hours / 3 days

## Intended Audience
* Data engineers building and maintaining data ingestion and integration pipelines
* `DevOps` engineers managing `NiFi` infrastructure and deployments
* Platform engineers designing data movement architectures
* `ETL` developers migrating from traditional tools to `NiFi`
* Systems integrators connecting heterogeneous data sources and destinations

## Prerequisites
* Familiarity with `ETL`/`ELT` concepts and data pipeline design
* Basic understanding of networking and common data protocols (`HTTP`, `FTP`, `Kafka`)
* Experience with `Linux` command-line tools
* Basic knowledge of `JSON`, `XML`, and `CSV` data formats
* Familiarity with `Docker` for running local `NiFi` instances

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)
* `Docker` Fundamentals (or equivalent experience)

## Objectives
* Understand `NiFi` architecture, core components, and the `FlowFile` model
* Design and implement end-to-end data flows using the `NiFi` canvas
* Configure and tune processors, connections, and back-pressure settings
* Use controller services for shared resources such as database connection pools and `SSL` contexts
* Track data lineage and provenance for compliance and debugging
* Manage flow versioning and promotion across environments using `NiFi Registry`
* Secure `NiFi` with `TLS`, authentication, and multi-tenant authorisation
* Deploy and manage `NiFi` clusters for high availability and horizontal scalability
* Deploy `MiNiFi` agents for lightweight edge data collection
* Build real-world pipelines integrating databases, `Kafka`, `S3`, and `REST APIs`

## Outline
<!-- chapter: introduction-to-apache-nifi, duration: 2h -->
* Introduction to `Apache NiFi`
    * What is `Apache NiFi` and its use cases
    * History and the origins of `NiFi` at the NSA (Niagarafiles)
    * Core concepts: `FlowFiles`, processors, connections, and process groups
    * The `NiFi` canvas: navigating the web UI
    * `NiFi` vs traditional `ETL` tools and messaging systems
    * Installation and first steps with `Docker`
    * Overview of the `NiFi` ecosystem: `NiFi Registry`, `MiNiFi`, `NiFi Stateless`
<!-- chapter: nifi-architecture-and-components, duration: 2h -->
* `NiFi` Architecture and Components
    * `NiFi` `JVM` architecture: `FlowController`, `ProcessScheduler`, `ContentRepository`
    * Repository types: `FlowFile` repository, content repository, provenance repository
    * The `FlowFile`: attributes, content, and lineage
    * Processors: lifecycle (`RUNNING`, `STOPPED`, `INVALID`), scheduling strategies
    * Connections: queues, prioritisation, and back-pressure thresholds
    * Process groups and remote process groups for flow organisation
    * Controller services and reporting tasks
    * `NiFi` `threading` model and concurrent task configuration
<!-- chapter: nifi-flow-design, duration: 3h -->
* `NiFi` Flow Design
    * Design principles for maintainable and reusable flows
    * Input/output ports and process group composition
    * Routing `FlowFiles` with `RouteOnAttribute` and `RouteOnContent`
    * Handling `FlowFile` failures and the failure relationship
    * Using funnels, labels, and comments for readable flows
    * Template-based flow reuse (legacy) vs `NiFi Registry`-based reuse
    * Managing flow complexity with nested process groups
    * Designing for idempotency and exactly-once semantics
<!-- chapter: processors-and-connections, duration: 3h -->
* Processors and Connections
    * Ingestion processors: `GetFile`, `GetHTTP`, `ConsumeKafka`, `ListS3`, `QueryDatabaseTable`
    * Transformation processors: `UpdateAttribute`, `ReplaceText`, `JoltTransformJSON`, `ExecuteScript`
    * Routing and control flow: `RouteOnAttribute`, `RouteOnContent`, `ControlRate`
    * Output processors: `PutFile`, `PutKafka`, `PutS3Object`, `PutDatabaseRecord`
    * Expression Language for dynamic attribute evaluation
    * Record-based processors: `QueryRecord`, `ConvertRecord`, `LookupRecord`
    * Connection prioritisation and `FlowFile` expiration policies
    * Monitoring processor performance metrics
<!-- chapter: controller-services, duration: 2h -->
* Controller Services
    * What are controller services and why they exist
    * `DBCPConnectionPool` for database connectivity
    * `StandardSSLContextService` for `TLS` configuration
    * Record reader and writer services: `JSON`, `CSV`, `Avro`, `Parquet`
    * `HadoopConfiguration` and cloud provider credential services
    * Scoping controller services: process group vs root-level
    * Enabling, disabling, and modifying controller services in a live flow
    * Sharing controller services across multiple processors
<!-- chapter: data-provenance-and-lineage, duration: 2h -->
* Data Provenance and Lineage
    * What is data provenance and why it matters for compliance and debugging
    * The `NiFi` provenance repository: storage and retention configuration
    * Querying provenance events: filtering by `FlowFile`, processor, and time range
    * Replaying `FlowFiles` from provenance for debugging and reprocessing
    * Lineage graph: visualising the complete journey of a `FlowFile`
    * Provenance storage trade-offs: performance vs retention
    * Sending provenance events to external systems for audit
    * Integrating provenance data with data catalogues and governance platforms
<!-- chapter: nifi-registry-and-version-control, duration: 2h -->
* `NiFi Registry` and Version Control
    * What is `NiFi Registry` and its role in flow lifecycle management
    * Installing and configuring `NiFi Registry`
    * Connecting `NiFi` to a `NiFi Registry` instance
    * Committing flows to `NiFi Registry` and managing versions
    * Comparing flow versions and reverting changes
    * Promoting flows across environments: development, staging, production
    * Using `Git`-backed flow storage in `NiFi Registry`
    * Team collaboration workflows with `NiFi Registry`
<!-- chapter: security-and-multi-tenancy, duration: 2h -->
* Security and Multi-Tenancy
    * Securing `NiFi` with two-way `TLS` for node-to-node communication
    * Authentication options: certificates, `LDAP`, `Kerberos`, `OIDC`
    * Authorisation: policy-based access control for components and data
    * Multi-tenancy with restricted process groups and isolated users
    * Configuring `NiFi` with a secure keystore and truststore
    * Sensitive property encryption with `NiFi` master key
    * Auditing user actions and access through `NiFi` audit logs
    * Best practices for secrets management: `HashiCorp Vault` integration
<!-- chapter: clustering-and-high-availability, duration: 2h -->
* Clustering and High Availability
    * `NiFi` cluster architecture: primary node, coordinator node, and cluster members
    * `ZooKeeper` for cluster coordination and state management
    * Flow replication: ensuring all nodes run the same flow
    * Load distribution and `FlowFile` affinity in a cluster
    * Failover behaviour and node reconnection
    * Scaling out: adding and removing cluster nodes
    * Site-to-Site protocol for secure inter-cluster data transfer
    * Monitoring cluster health with `NiFi` system diagnostics and `Prometheus`
<!-- chapter: nifi-minifi-for-edge, duration: 2h -->
* `NiFi MiNiFi` for Edge Data Collection
    * What is `MiNiFi` and its role in edge computing architectures
    * `MiNiFi Java` vs `MiNiFi C++`: capabilities and use cases
    * Designing `MiNiFi` flows in `NiFi` and exporting them as `MiNiFi` templates
    * Deploying `MiNiFi` agents on edge devices and `IoT` gateways
    * `MiNiFi` Command and Control (`C2`) for remote agent management
    * Forwarding data from `MiNiFi` agents to `NiFi` using Site-to-Site
    * Resource constraints and optimising `MiNiFi` for low-power devices
    * Edge-to-cloud pipeline patterns with `MiNiFi` and `NiFi`
<!-- chapter: real-world-pipelines, duration: 2h -->
* Real-World Pipelines
    * Ingesting data from relational databases with CDC and `QueryDatabaseTable`
    * Building `Kafka`-to-data-lake pipelines with schema registry integration
    * `REST` `API` polling and enrichment pipelines
    * `S3` event-driven ingestion with `ListS3` and `FetchS3Object`
    * Data quality validation and routing pipelines
    * Error handling patterns: retry queues, dead letter flows, and alerting
    * Performance tuning: back-pressure, concurrent tasks, and repository sizing
    * Operational best practices: monitoring, alerting, and capacity planning

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
