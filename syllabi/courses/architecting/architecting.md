---
tags:
  - concepts:architecture
  - concepts:microservices
  - infrastructure:cloud
  - practices:ci-cd
  - concepts:design-patterns
level: intermediate
category: architecture
duration_hours: 40
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: architecting -->
# Architecting

## Description
This course about architecting in a modern computing environment, either on a cloud or on premise.
It presents all the major topics that a modern systems architect needs to know such as micro-service architecture,
queues, `CI/CD`, data lakes, various data store types and much more.
The course teaches which tradeoffs exist between various requirements and how to apply common sense and
pick the right tradeoff for your case.

## Duration
40 hours / 5 days

## Intended Audience
* Seasoned developers who would like to progress to the role of architect.

## Prerequisites
* Experience in the tech sector as developers or team leaders.

## Objectives
* Foster a deep understanding of architectural principles and patterns
* Develop the ability to analyze and evaluate trade-offs
* Stay abreast of emerging technologies and trends
* Promote a holistic approach to system design

## Outline
<!-- chapter: introduction-to-modern-software-architecture, duration: 1h -->
* Introduction to Modern Software Architecture
    * Evolution of software architecture
    * `Cloud computing` fundamentals
    * Architectural patterns and styles
<!-- chapter: basic-concepts, duration: 1h -->
* Basic concepts
    * Durability
    * Availability
    * Throughput
    * Scalability
    * Everything fails principle
    * Some concepts are at odds with each other
    * How to achieve them?
<!-- chapter: other-concepts, duration: 1h -->
* Other concepts
    * Reliability, Performance, Latency
    * Maintainability, Security, Interoperability
    * Usability, Portability, Extensibility
    * Modularity, Testability, Observability, Elasticity
<!-- chapter: containers, duration: 1h -->
* Containers
    * Why do we need containers?
    * Evolution of containerization
        * `Docker`
        * `docker`-compose
        * swarm
        * `Kubernetes`
        * service mesh
    * How much to put into a container?
<!-- chapter: microservices-architecture, duration: 1h -->
* `Microservices` Architecture
    * Monolithic vs. `Microservices` architecture
    * Designing and implementing `Microservices`
    * Service discovery and `API` gateways
<!-- chapter: micro-service-design-patterns, duration: 2h -->
* Micro-Service `Design patterns`
    * Why `design patterns`?
    * Common patterns:
        * Circuit Breaker
        * `API` Gateway
        * Service Discovery
        * Load Balancer
        * `Saga`
        * `Event Sourcing`
        * Command Query Responsibility Segregation
        * Bulkhead
        * Sidecar
        * Strangler Fig
        * Backend for Frontend
<!-- chapter: devops-and-ci-cd, duration: 1h -->
* `DevOps` and `CI/CD`
    * `DevOps` principles and practices
    * Continuous Integration and Continuous Deployment
    * Infrastructure as Code (IaC)
<!-- chapter: caching-strategies-and-content-delivery-networks-cdns, duration: 2h -->
* Caching strategies and Content Delivery Networks (CDNs)
    * Fundamentals of Caching and CDNs
        * Types of caches and their roles
        * CDN architecture and components
    * Caching Strategies in Modern Applications
        * Client-side, server-side, and distributed caching
        * Cache coherence and invalidation techniques
    * Leveraging CDNs for Performance and Scalability
        * Content replication and distribution
        * Static vs. dynamic content caching
    * Optimizing Caching and CDN Usage
        * Performance metrics and monitoring
        * Security considerations and best practices
    * Future Trends in Caching and Content Delivery
        * Edge computing and serverless CDNs
        * `AI`-driven caching predictions
<!-- chapter: data-lakes, duration: 3h -->
* Data Lakes
    * Introduction to Data Lakes
        * Definition and core concepts
        * Comparison with traditional data warehouses
    * Architectural Components of Data Lakes
        * Storage layers and data formats
        * Processing engines and analytics tools
    * Introduction to Data Lakehouse
        * Evolution of a data Lakehouse
        * Key Features and Capabilities
        * Examples (`Apache Iceberg`, `Delta Lake`, `Apache Hudi`, ...)
    * Data Ingestion and Management
        * Batch and real-time data ingestion
        * Data governance and metadata management
    * Data Lake Implementation Strategies
        * Cloud-based vs on-premises data lakes
        * Hybrid and multi-cloud approaches
    * Analytics and `Machine Learning` on Data Lakes
        * Big data processing frameworks
        * `AI`/`ML` model training and deployment
<!-- chapter: queues, duration: 3h -->
* Queues
    * Understanding Queues in Distributed Systems
        * Definition and core concepts
        * Types of queues and their use cases
    * Queue-Based Architectural Patterns
        * Publish-Subscribe model
        * Work Queue / Task Queue pattern
        `Event-Driven Architecture` with queues
    * Implementing Queues in Cloud Environments
        * Message brokers and queue services (e.g., `RabbitMQ`, `Apache Kafka`, `Amazon SQS`)
        * Scaling and performance considerations
    * Designing for Reliability and Fault Tolerance
        * Message persistence and durability
        * Dead letter queues and error handling
    * Advanced Queue Concepts and Optimizations
        * Priority queues and message ordering
        * Batching and message compression
    * Examples: `RabbitMQ`, `Apache Kafka`, `Amazon SQS`
<!-- chapter: databases, duration: 5h -->
* Databases
    * Introduction to Databases
        * Core concepts of database management systems (DBMS)
        * Data modeling and schema design
        * ACID properties and transaction management
        * Database security and access control
    * `SQL` Databases
        * Relational model and normalization
        * `SQL` query language and data manipulation
        * Database indexing and optimization
        * Transaction isolation levels and concurrency control
        * Common `SQL` database systems (e.g., `MySQL`, `PostgreSQL`, `Oracle`)
    * `NoSQL` Databases
        * Key-value stores
        * Document databases
        * Column-family stores
        * Graph databases
        * CAP theorem and distributed systems
        * Common `NoSQL` database systems (e.g., `MongoDB`, `Cassandra`, `Redis`, `Neo4j`, `DynamoDB`)
        * Comparison of common `NoSQL` database systems (scalability, row length, number of indexes, compaction, ...)
    * Choosing the Right Database
        * Data access patterns and application requirements
        * Performance, scalability, and consistency considerations
        * Data modeling and schema design for `SQL` vs `NoSQL`
        * Hybrid database architectures
    * Database Architecture and Design
        * Data partitioning and sharding
        * Replication and high availability
        * Database clustering and load balancing
        * Data warehousing and analytics
        * Cloud-based database solutions
<!-- chapter: workflow-orchestration-and-data-pipelines, duration: 4h -->
* Workflow Orchestration and Data Pipelines
    * Introduction to Workflow Orchestration
        * Concepts of workflow orchestration, data pipelines, and their benefits
        * Common use cases and challenges
        * Overview of popular workflow orchestration tools
    * `Apache Airflow`
        * `Airflow` architecture and components (DAGs, operators, executors)
        * Building and scheduling workflows in `Airflow`
        * Best practices for `Airflow` development
        * `Airflow` integration with data sources and tools
    * Other Workflow Orchestration Tools
        * Overview of `Prefect`, `Dagster`, and other relevant tools
        * Comparative analysis of different tools and their strengths
        * Choosing the right tool for specific use cases
    * Data Pipelines
        * Key components and `design patterns` for data pipelines
        * Data extraction, transformation, and loading (`ETL`)
        * Data validation and quality assurance
        * Handling data pipeline failures and retries
    * Advanced Topics
        * Scaling and optimizing workflows and pipelines
        * Monitoring and observability for workflows
        * Security and access control in workflow systems
        * Integrating `machine learning` models into pipelines
<!-- chapter: architecting-systems-for-big-data, duration: 5h -->
* Architecting Systems for Big Data
    * Introduction to Big Data
        * The 3 Vs (Volume, Velocity, Variety) and beyond
        * Challenges and opportunities of big data
        * Use cases and applications of big data across industries
    * Big Data Ecosystem
        * Overview of key components and technologies
        * Data storage (`HDFS`, object storage, `NoSQL` databases)
        * Data processing (`MapReduce`, `Spark`, `Flink`)
        * Data ingestion and streaming (`Kafka`, `Flume`)
        * Data visualization and analytics tools
    * Big Data Architecture Patterns
        * `Lambda` architecture
        * Kappa architecture
        * Data lake vs. data warehouse
        * Real-time vs. batch processing
        * `Microservices` and big data
    * Data Ingestion and Storage
        * Data collection and integration from various sources
        * Data cleaning and preprocessing
        * Choosing the right storage technology for different data types
        * Data partitioning and indexing for efficient access
    * Data Processing and Analysis
        * Distributed computing paradigms (`MapReduce`, `Spark`)
        * Stream processing and real-time analytics
        * `Machine learning` and `AI` on big data
        * Data visualization and exploration techniques
    * Big Data Security and Governance
        * Data privacy and compliance
        * Access control and authentication
        * Data encryption and anonymization
        * Data lineage and auditing
<!-- chapter: monitoring-and-observability, duration: 6h -->
* Monitoring and Observability
    * Introduction to Monitoring and Observability
        * Key concepts: monitoring, observability, metrics, logs, traces
        * The three pillars of observability
        * Benefits of effective monitoring and observability
        * Common challenges in monitoring complex systems
    * Metrics
        * Types of metrics (counters, gauges, histograms, summaries)
        * Metric collection and aggregation
        * Choosing the right metrics for different systems and use cases
        * Introduction to `Prometheus` and other metric collection tools
    * Logs
        * Log aggregation and analysis
        * Structured logging and log formats
        * Log-based alerting and anomaly detection
        * Tools for log management (`ELK stack`, `Splunk`, etc.)
    * Traces
        * Distributed tracing and its importance
        * Tracing instrumentation and propagation
        * Trace visualization and analysis
        * `OpenTelemetry` and other tracing tools
    * Alerting and Anomaly Detection
        * Setting up effective alerting systems
        * Defining alert thresholds and rules
        * Anomaly detection techniques
        * Reducing alert fatigue and noise
    * Dashboards and Visualization
        * Creating informative and actionable dashboards
        * `Grafana` and other visualization tools
        * Best practices for dashboard design
    * Building Observable Systems
        * Designing for observability from the start
        * Instrumenting code for metrics, logs, and traces
        * Observability in `Microservices` and cloud-native architectures
<!-- chapter: the-evolution-of-disaster-recovery, duration: 1h -->
* The Evolution of Disaster recovery
    * Backup and Restore
    * Pilot Light
    * Warm Standby
    * Hot Site/Multi Site
    * Cloud Based DR
    * Data Replication
<!-- chapter: serverless-computing, duration: 1h -->
* Serverless Computing
    * Function as a Service (FaaS)
    * `Event-driven architecture`
<!-- chapter: security-and-compliance-in-the-cloud, duration: 1h -->
* Security and Compliance in the Cloud
    * Identity and Access Management (`IAM`)
    * Encryption and key management
    * Compliance frameworks and best practices
<!-- chapter: emerging-trends-and-technologies, duration: 1h -->
* Emerging Trends and Technologies
    * Edge computing
    * `AI` and `machine learning` in cloud architecture
    * Blockchain and distributed systems

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
