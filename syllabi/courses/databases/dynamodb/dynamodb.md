---
tags:
  - databases:dynamodb
  - databases:nosql
  - infrastructure:aws
  - concepts:data-modeling
level: intermediate
category: database
duration_hours: 16
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: dynamodb -->
# `DynamoDB`

## Description
This course provides a deep dive into `Amazon DynamoDB`, a fully managed `NoSQL` key-value and document database service on `AWS`. Participants will learn how to design efficient data models using single-table `design patterns`, configure partition keys and sort keys, leverage Global Secondary Indexes (GSIs) and Local Secondary Indexes (LSIs), and utilize advanced features such as `DynamoDB Streams`, DAX caching, and capacity management. The course emphasizes best practices for building scalable, cost-effective, and performant applications with `DynamoDB`.

## Duration
16 hours / 2 days

## Intended Audience
* Backend developers building applications on `AWS`
* Software engineers working with `NoSQL` databases
* Cloud architects designing serverless or `microservices` architectures
* Developers migrating from relational databases to `DynamoDB`

## Prerequisites
* Basic understanding of `NoSQL` database concepts
* Familiarity with `AWS` services and the `AWS Management Console`
* Proficiency in at least one programming language (`Python`, `JavaScript`, `Java`, or `Go` preferred)
* Basic understanding of `JSON` data format

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)
* Introduction to `AWS` (or equivalent experience)

## Objectives
* Understand `DynamoDB` architecture, partitioning, and data distribution
* Design effective single-table data models for complex access patterns
* Choose and configure partition keys, sort keys, GSIs, and LSIs
* Implement `DynamoDB Streams` for event-driven architectures
* Optimize read performance using DAX caching
* Select and manage appropriate capacity modes for cost and performance
* Apply best practices for query optimization, data modeling, and cost management
* Integrate `DynamoDB` with `AWS Lambda`, `API Gateway`, and other `AWS` services

## Outline
<!-- chapter: introduction-to-dynamodb, duration: 1h -->
* Introduction to `DynamoDB`
    * `DynamoDB` overview and core concepts
    * Managed `NoSQL` vs self-hosted databases
    * `DynamoDB` architecture and partitioning
    * Consistency models: eventual vs strong consistency
    * Tables, items, and attributes
    * `AWS SDK` setup and `CLI` basics
    * `DynamoDB` local for development

<!-- chapter: keys-and-data-modeling-fundamentals, duration: 1h -->
* Keys and Data Modeling Fundamentals
    * Partition keys and sort keys
    * Primary key design strategies
    * Item collections
    * Data types and nested attributes
    * Item size limits and considerations
    * Sparse indexes
    * Time-to-live (`TTL`) for data expiration

<!-- chapter: single-table-design, duration: 2h -->
* Single-Table Design
    * Why single-table design in `DynamoDB`
    * Access pattern analysis
    * Entity mapping to a single table
    * Overloading partition keys and sort keys
    * Composite sort keys for hierarchical data
    * Adjacency list pattern
    * Modeling one-to-many and many-to-many relationships
    * Migrating from relational models to single-table design
    * Common single-table design pitfalls

<!-- chapter: global-secondary-indexes-gsis-and-local-secondary-indexes-lsis, duration: 2h -->
* Global Secondary Indexes (GSIs) and Local Secondary Indexes (LSIs)
    * GSI concepts and use cases
    * LSI concepts and constraints
    * Choosing between GSIs and LSIs
    * Index projections (keys only, include, all)
    * Index overloading patterns
    * Sparse GSI patterns
    * Cost implications of indexes
    * Managing and monitoring indexes

<!-- chapter: reading-and-writing-data, duration: 2h -->
* Reading and Writing Data
    * GetItem, PutItem, UpdateItem, DeleteItem
    * Query vs Scan operations
    * Filter expressions
    * Projection expressions
    * Condition expressions for optimistic locking
    * BatchGetItem and BatchWriteItem
    * TransactGetItems and TransactWriteItems
    * Pagination and result handling
    * Error handling and retries

<!-- chapter: dynamodb-streams, duration: 2h -->
* `DynamoDB Streams`
    * Stream concepts and architecture
    * Stream record types (keys only, new image, old image, both)
    * Processing streams with `AWS Lambda`
    * Change data capture patterns
    * Cross-region replication with global tables
    * Event-driven architectures with `DynamoDB Streams`
    * Stream processing best practices
    * Handling failures and dead-letter queues

<!-- chapter: dax-dynamodb-accelerator, duration: 2h -->
* DAX (`DynamoDB` Accelerator)
    * DAX architecture and caching model
    * Item cache vs query cache
    * DAX cluster setup and configuration
    * Integrating DAX with applications
    * Cache invalidation behavior
    * `When` to use DAX vs ElastiCache
    * Cost and performance trade-offs
    * Monitoring DAX clusters

<!-- chapter: capacity-modes-and-cost-optimization, duration: 2h -->
* Capacity Modes and Cost Optimization
    * On-demand capacity mode
    * Provisioned capacity mode
    * `Auto scaling` configuration
    * Reserved capacity
    * Capacity planning and estimation
    * Read/write capacity unit calculations
    * Burst capacity and throttling
    * Cost optimization strategies
    * Monitoring with `CloudWatch` metrics

<!-- chapter: best-practices-and-integration-patterns, duration: 2h -->
* Best Practices and Integration Patterns
    * Hot partition detection and mitigation
    * Write sharding techniques
    * Large item handling strategies
    * Backup and restore options
    * Point-in-time recovery
    * Integration with `AWS Lambda`
    * Integration with `API Gateway`
    * Integration with `Step Functions`
    * `DynamoDB` in serverless architectures

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
