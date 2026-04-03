---
tags:
  - tools:flink
  - data-and-ai:big-data
  - data-and-ai:streaming
level: intermediate
category: big-data
duration_hours: 32
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: apache_flink -->
# `Apache Flink`

## Description
`Apache Flink` is a distributed stream processing framework designed for stateful computations
over bounded and unbounded data streams. `Flink` provides exactly-once state consistency,
event-time processing, and high throughput with low latency, making it a leading choice for
real-time data processing at scale.

Throughout this course, students will gain deep expertise in stream processing with `Flink`.
Starting with fundamental concepts and architecture, the course progresses through the
`DataStream API`, windowing, state management, fault tolerance, connectors, and production
deployment strategies.

## Duration
32 hours / 4 days

## Intended Audience
* Developers and data scientists who want to build real-time stream processing applications using `Apache Flink`

## Prerequisites
* Previous programming experience with `Java` or `Scala`
* Basic understanding of distributed systems concepts
* Familiarity with messaging systems such as `Apache Kafka`

## Required Knowledge
* Introduction to `Apache Kafka` (or equivalent experience)

## Objectives
* Understand stream processing concepts and the `Apache Flink` architecture
* Build stream processing applications using the `DataStream API`
* Implement event-time processing with watermarks and `windows`
* Manage application state with keyed and operator state
* Configure fault tolerance using checkpoints and savepoints
* Connect `Flink` to external systems using built-in connectors
* Write analytical queries using the Table `API` and `Flink SQL`
* Deploy, monitor, and tune `Flink` applications in production

## Outline
<!-- chapter: introduction-to-stream-processing, duration: 2h -->
* Introduction to Stream Processing
    * Batch vs stream processing
    * Bounded and unbounded data streams
    * Stream processing use cases
    * Overview of `Apache Flink`
    * Comparison with `Spark Streaming`
<!-- chapter: flink-architecture, duration: 2h -->
* `Flink` Architecture
    * JobManager and TaskManager
    * Task slots and parallelism
    * Execution graphs
    * Checkpointing mechanism
    * High availability configuration
<!-- chapter: datastream-api-fundamentals, duration: 2h -->
* `DataStream API` Fundamentals
    * Setting up a `Flink` project
    * Data sources and sinks
    * Basic transformations (map, flatMap, filter)
    * KeyBy and partitioning
    * Rich functions and accumulators
<!-- chapter: event-time-and-watermarks, duration: 2h -->
* Event Time and Watermarks
    * Processing time vs event time vs ingestion time
    * Watermark generation strategies
    * Handling late data
    * Allowed lateness
    * Side outputs for late elements
<!-- chapter: windows, duration: 3h -->
* `Windows`
    * Tumbling `windows`
    * Sliding `windows`
    * Session `windows`
    * Global `windows`
    * Window functions (reduce, aggregate, process)
    * Window triggers and evictors
<!-- chapter: state-management, duration: 2h -->
* State Management
    * Keyed state (ValueState, ListState, MapState, ReducingState, AggregatingState)
    * Operator state (ListState, BroadcastState)
    * State backends (HashMapStateBackend, EmbeddedRocksDBStateBackend)
    * State `TTL` and cleanup
    * Queryable state
<!-- chapter: fault-tolerance, duration: 2h -->
* Fault Tolerance
    * Checkpoints and checkpoint configuration
    * Exactly-once vs at-least-once semantics
    * Savepoints and application versioning
    * Recovering from failures
    * End-to-end exactly-once guarantees
<!-- chapter: connectors, duration: 3h -->
* Connectors
    * `Apache Kafka` connector
    * `JDBC` connector
    * Filesystem connector
    * `Elasticsearch` connector
    * Custom source and sink functions
<!-- chapter: table-api-and-flink-sql, duration: 3h -->
* Table `API` and `Flink SQL`
    * Table environments
    * Creating tables from streams
    * `SQL` queries on streaming data
    * Dynamic tables and continuous queries
    * Joins in streaming `SQL`
    * Catalog management
<!-- chapter: complex-event-processing-cep, duration: 2h -->
* Complex Event Processing (CEP)
    * Pattern detection in event streams
    * Defining patterns with the CEP library
    * Pattern matching and selection
    * Use cases for CEP
<!-- chapter: advanced-topics, duration: 3h -->
* Advanced Topics
    * Side outputs
    * `Async` `I/O` for external data access
    * Broadcast state pattern
    * Connected streams
    * Process functions and timers
<!-- chapter: deployment, duration: 3h -->
* Deployment
    * Standalone cluster deployment
    * Deploying on `YARN`
    * Deploying on `Kubernetes`
    * Application mode vs session mode
    * Configuration and resource management
<!-- chapter: monitoring-and-performance-tuning, duration: 3h -->
* Monitoring and Performance Tuning
    * `Flink` web UI and metrics
    * Integrating with `Prometheus` and `Grafana`
    * Backpressure detection and resolution
    * Memory tuning
    * Network buffer configuration
    * Parallelism and resource optimization

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
