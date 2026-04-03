---
tags:
  - tools:mongodb
  - databases:nosql
  - data-and-ai:databases
  - concepts:data-modeling
level: advanced
category: database
duration_hours: 16
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: advanced_mongodb -->
# Advanced `MongoDB`

## Description
This advanced course is designed for developers and database professionals who already have working knowledge of `MongoDB` and need to master its most powerful features. Participants will dive deep into the aggregation framework, sharding for horizontal scalability, change streams for real-time data processing, and `MongoDB Atlas` cloud platform capabilities. The course also covers multi-document transactions, advanced schema `design patterns`, sophisticated indexing strategies, and production monitoring techniques.

## Duration
16 hours / 2 days

## Intended Audience
* Experienced `MongoDB` developers seeking advanced skills
* Database engineers optimizing `MongoDB` deployments
* Backend developers building scalable distributed applications
* Software architects designing data-intensive systems

## Prerequisites
* Working experience with `MongoDB` `CRUD` operations
* Familiarity with `MongoDB` document model and basic queries
* Understanding of indexing fundamentals
* Experience with `JSON`/BSON data formats
* Basic knowledge of distributed systems concepts

## Objectives
* Build complex data transformations using the aggregation framework
* Design and manage sharded clusters for horizontal scaling
* Implement real-time data processing with change streams
* Leverage `MongoDB Atlas` features for cloud deployments
* Implement multi-document transactions for data consistency
* Apply advanced schema `design patterns` for optimal performance
* Create and manage sophisticated indexing strategies
* Monitor and troubleshoot `MongoDB` deployments in production

## Outline
<!-- chapter: advanced-aggregation-pipelines, duration: 2h -->
* Advanced Aggregation Pipelines
    * Pipeline architecture and optimization
    * $match, $group, $project, and $sort deep dive
    * $lookup for cross-collection joins
    * $unwind and `array` processing
    * $facet for multi-faceted aggregations
    * $graphLookup for recursive queries
    * $merge and $out for materialized views
    * Window functions and $setWindowFields
    * Expression operators and custom expressions
    * Pipeline performance optimization

<!-- chapter: sharding, duration: 2h -->
* Sharding
    * Sharding architecture and components
    * Shard key selection strategies
    * Hashed vs ranged sharding
    * Chunks, balancing, and migrations
    * Zone sharding for data locality
    * Adding and removing shards
    * Sharded cluster operations
    * Query routing and mongos
    * Sharding anti-patterns
    * Monitoring sharded clusters

<!-- chapter: change-streams, duration: 2h -->
* Change Streams
    * Change stream architecture
    * Opening and configuring change streams
    * Change event types and structure
    * Resume tokens and fault tolerance
    * Pre-image and post-image support
    * Filtering change events with pipelines
    * Database and cluster-level change streams
    * Event-driven application patterns
    * Integration with message queues
    * Scaling change stream consumers

<!-- chapter: mongodb-atlas, duration: 2h -->
* `MongoDB Atlas`
    * Atlas architecture and tiers
    * Cluster deployment and configuration
    * Atlas Search with `Lucene`
    * Atlas Data Federation
    * Atlas Triggers and Functions
    * Atlas Charts for visualization
    * Atlas `CLI` and `API` automation
    * Performance Advisor and recommendations
    * Atlas security features
    * Cost optimization strategies

<!-- chapter: multi-document-transactions, duration: 2h -->
* Multi-Document Transactions
    * Transaction architecture in `MongoDB`
    * Transaction `API` and syntax
    * Read and write concerns in transactions
    * Causal consistency sessions
    * Transaction lifecycle and timeouts
    * Retry logic and error handling
    * Transactions across sharded clusters
    * Performance implications
    * `When` to use (and avoid) transactions

<!-- chapter: schema-design-patterns, duration: 2h -->
* Schema `Design Patterns`
    * Attribute pattern
    * Bucket pattern for time series
    * Computed pattern for derived data
    * Document versioning pattern
    * Extended reference pattern
    * Outlier pattern for anomalous data
    * Polymorphic pattern
    * Subset pattern for working sets
    * Tree and graph patterns
    * Anti-patterns and common mistakes

<!-- chapter: advanced-indexing-strategies, duration: 2h -->
* Advanced Indexing Strategies
    * Compound index optimization
    * Multikey index behavior and limitations
    * Wildcard indexes for dynamic schemas
    * Text indexes and search scoring
    * Geospatial indexes: 2d and 2dsphere
    * Partial and sparse indexes
    * `TTL` indexes for data lifecycle
    * Hidden indexes for testing
    * Index intersection analysis
    * Using `explain()` for index tuning

<!-- chapter: monitoring-and-operations, duration: 2h -->
* Monitoring and Operations
    * `MongoDB` monitoring tools overview
    * mongostat and mongotop usage
    * Server status and diagnostic commands
    * Profiler configuration and analysis
    * Log analysis techniques
    * Performance metrics and alerts
    * `Ops Manager` and `Cloud Manager`
    * Capacity planning
    * Backup and restore strategies
    * Operational best practices

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
