---
tags:
  - databases:arangodb
  - databases:multi-model
  - databases:graph
  - databases:document
  - databases:nosql
level: intermediate
category: database
duration_hours: 24
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: arangodb -->
# `ArangoDB`

## Description
`ArangoDB` is a native multi-model database that supports document, key-value, and graph data models within a single engine, allowing teams to avoid the operational complexity of maintaining separate stores for different data access patterns. Using the expressive `AQL` (`ArangoDB` Query Language), developers can query and join across all three models in a single query. This course provides a deep and practical guide to `ArangoDB` — from its architecture and document store operations through advanced graph modeling, traversals, and shortest-path algorithms. Participants will also learn about indexing, multi-document transactions, cluster deployment, and performance monitoring, leaving them ready to design and operate `ArangoDB`-backed applications in production.

## Duration
24 hours / 3 days

## Intended Audience
* Developers building applications that combine document, graph, and key-value access patterns
* Architects evaluating multi-model databases to simplify their data platform
* Engineers working on knowledge graphs, fraud detection, or social network features
* Teams considering migration from `MongoDB`, `Neo4j`, or similar single-model databases
* Backend engineers who want a single flexible database without sacrificing query power

## Prerequisites
* Programming experience in `JavaScript`, `Python`, or another language
* Familiarity with `NoSQL` database concepts (documents, collections)
* Basic understanding of graph theory (nodes, edges, paths) is helpful
* Prior experience with any document or graph database is beneficial but not required

## Objectives
* Understand `ArangoDB`'s multi-model architecture and when to use it
* Perform `CRUD` operations on document collections via the `ArangoDB` web UI and `API`
* Write complex queries using `AQL` across documents, edges, and graphs
* Design effective graph data models for relationship-heavy workloads
* Execute graph traversals, shortest-path searches, and pattern matching
* Create and use indexes to optimize query performance
* Manage multi-document and multi-collection ACID transactions
* Deploy `ArangoDB` in single-server and cluster modes
* Monitor cluster health and tune performance

## Exercises
Hands-on labs using a local `ArangoDB` instance and the `arangosh` shell. Students will create databases and collections, import and query document datasets, build a social graph with vertex and edge collections, execute traversal queries to find relationships, implement shortest-path and k-nearest-neighbors queries, create persistent and `TTL` indexes, run multi-collection transactions, use `Foxx` `microservices` for server-side logic, and deploy a two-shard cluster with `Docker Compose`. Scenarios include social network analysis, product recommendation graphs, and supply chain tracking.

## Outline
<!-- chapter: introduction-to-multi-model-databases, duration: 2h -->
* Introduction to Multi-Model Databases
    * The proliferation of specialized databases and its costs
    * Multi-model vs polyglot persistence: trade-offs
    * `ArangoDB` data models: document, key-value, and graph
    * `ArangoDB` editions: Community, Enterprise, and `ArangoGraph` Cloud
    * Key use cases: knowledge graphs, fraud detection, and content management
    * Comparison with `MongoDB`, `Neo4j`, `Couchbase`, and `DynamoDB`

<!-- chapter: arangodb-architecture, duration: 2h -->
* `ArangoDB` Architecture
    * Storage engine: `RocksDB` for persistence
    * Collections: document and edge collections
    * Databases and namespaces
    * The `ArangoDB` server: arangod, coordinator, and DB-Server roles
    * Cluster architecture: coordinators, DB-Servers, and Agency
    * Replication: leader-follower and Active Failover
    * The `arangosh` shell and web console overview

<!-- chapter: document-store-operations, duration: 3h -->
* Document Store Operations
    * Creating databases and collections
    * Document structure: `_id`, `_key`, and `_rev` system attributes
    * Inserting, reading, updating, and replacing documents
    * Bulk imports with `arangoimport`
    * Collection properties and schema validation
    * Using the `ArangoDB` `HTTP` `REST API`
    * Drivers: `arangojs`, `arangopy`, and `Java` driver
    * Error handling and conflict management

<!-- chapter: aql-arangodb-query-language, duration: 3h -->
* AQL: `ArangoDB` Query Language
    * AQL syntax overview: FOR, RETURN, FILTER, SORT, LIMIT
    * Document attribute access and `array` operations
    * String, numeric, and date functions
    * Aggregation with COLLECT and AGGREGATE
    * Subqueries and nested `FOR-loops`
    * `LET` for variable binding and query readability
    * UPSERT and INSERT operations in AQL
    * `Bind` parameters for safe, reusable queries
    * Explaining and profiling AQL queries

<!-- chapter: graph-data-modeling, duration: 3h -->
* Graph Data Modeling
    * Named graphs: vertex and edge collections
    * Directed and undirected edges
    * Edge attributes for relationship metadata
    * Modeling one-to-many and many-to-many relationships
    * Hyperedges and hypergraph patterns
    * Property graph model and its advantages
    * Anti-patterns: deeply nested documents vs edges
    * Real-world graph schemas: social network, dependency graph, and org hierarchy

<!-- chapter: graph-traversals-and-shortest-paths, duration: 3h -->
* Graph Traversals and Shortest Paths
    * FOR v, e, p IN traversal syntax
    * Depth-limited and depth-exact traversals
    * Traversal direction: OUTBOUND, INBOUND, ANY
    * Filtering vertices and edges during traversal
    * Shortest path with SHORTEST_PATH
    * k-Shortest paths with K_SHORTEST_PATHS
    * k-Nearest-Neighbors with K_PATHS
    * Pattern matching with graph traversals
    * Performance considerations for large graph traversals

<!-- chapter: indexes-in-arangodb, duration: 2h -->
* Indexes in `ArangoDB`
    * Primary index on `_key`
    * Persistent indexes: single-field and composite
    * `TTL` indexes for automatic document expiry
    * Full-text indexes for text search
    * Geo-spatial indexes for location-based queries
    * Edge indexes for efficient graph traversal
    * `ArangoSearch` views for full-text and ranked search
    * Index usage analysis with EXPLAIN

<!-- chapter: transactions, duration: 2h -->
* Transactions
    * ACID transactions in `ArangoDB`
    * Stream transactions: locking and execution model
    * `JavaScript` transactions with `arangosh`
    * Multi-document and multi-collection transactions
    * Transaction isolation and conflict handling
    * Retry logic for transaction conflicts
    * Distributed transactions in cluster mode
    * Limitations and best practices

<!-- chapter: deployment-and-cluster-setup, duration: 2h -->
* Deployment and Cluster Setup
    * Single-server deployment for development
    * Active Failover setup for high availability
    * Cluster mode: coordinator and DB-Server topology
    * Deployment with `Docker` and `Docker Compose`
    * `ArangoDB` `Kubernetes` Operator
    * Sharding: number of shards and replication factor
    * `ArangoGraph` Cloud: managed service overview
    * Backup and restore with `arangodump` and `arangorestore`

<!-- chapter: performance-and-monitoring, duration: 2h -->
* Performance and Monitoring
    * The `ArangoDB` web console: statistics, query editor, and graph explorer
    * Slow query log and query statistics
    * `ArangoDB` metrics endpoint and `Prometheus` integration
    * `Grafana` dashboards for `ArangoDB`
    * Memory and cache tuning parameters
    * Replication lag monitoring
    * Common performance anti-patterns and how to fix them
    * Capacity planning and hardware recommendations

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
