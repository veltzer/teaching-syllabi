---
tags:
  - concepts:big-data
  - concepts:distributed-systems
  - concepts:data-architecture
  - concepts:data-integration
  - concepts:eventual-consistency
  - concepts:scalability
level: advanced
category: data-engineering
duration_hours: 40
audience:
  - audiences:data-engineers
  - audiences:developers
  - audiences:senior-developers
  - audiences:architects
---
<!-- course: streaming_data_systems -->
# Streaming Data Systems

## Description
Modern data platforms are increasingly built around continuous streams rather than nightly batches. Streaming
systems are powerful but full of subtle traps: time semantics, late data, exactly-once delivery, stateful
processing, schema evolution and recovery from failure each have non-obvious correct answers, and getting any of
them wrong shows up as silently corrupted data months later.

This five day course is a vendor-neutral, concept-first treatment of streaming data systems. It covers the
fundamental abstractions (event time, processing time, watermarks, windowing, state), the architectures that
implement them, the trade-offs of common engines (`Flink`, `Kafka Streams`, `Spark Structured Streaming`,
`Beam`), change-data-capture, integrations with `OLAP` and lake-house systems, and the operational discipline
required to run streaming workloads in production. Participants leave able to design, build and operate
streaming pipelines and to choose the right engine for a given workload.

## Duration
40 hours / 5 days

## Intended Audience
* data engineers building or maintaining streaming pipelines
* backend developers integrating with streaming platforms
* architects designing event-driven and analytical systems
* engineers migrating workloads from batch to streaming

## Prerequisites
* `solid` programming experience in `Java`/`Scala`/`Python`
* working knowledge of at least one message broker (`Kafka`, Pulsar, `Kinesis`)
* basic familiarity with `SQL` and one analytical store
* basic distributed systems concepts (replication, partitioning, consensus)

## Objectives
* describe the streaming data model and its trade-offs vs batch
* reason about event time, processing time, watermarks and lateness
* design windowed and stateful streaming computations correctly
* choose between `Flink`, `Kafka Streams`, `Spark Structured Streaming` and `Beam` for a given workload
* implement change-data-capture pipelines from operational stores
* integrate streaming with lakehouses and `OLAP` engines
* operate streaming workloads with appropriate observability and recovery
* avoid the most common streaming pipeline failure modes

## Outline
<!-- chapter: streaming-fundamentals, duration: 2h -->
* Streaming fundamentals
    * batch vs streaming vs micro-batch
    * unbounded data and event time
    * the dataflow model and Tyler Akidau's papers
    * latency, throughput and correctness as competing goals
    * common streaming use cases
<!-- chapter: time-semantics-and-watermarks, duration: 4h -->
* Time semantics and watermarks
    * event time vs processing time vs ingestion time
    * the watermark contract
    * out-of-order events and late data
    * allowed lateness and side outputs
    * watermark generation strategies
    * the cost of getting watermarks wrong
    * debugging watermark issues in production
<!-- chapter: windowing, duration: 3h -->
* Windowing
    * tumbling, sliding, session and global `windows`
    * custom and dynamic `windows`
    * triggers and accumulation modes
    * window merging and session `windows` in detail
    * results before, at and after the watermark
    * windowing pitfalls
<!-- chapter: stateful-stream-processing, duration: 4h -->
* Stateful stream processing
    * keyed vs operator state
    * value, list, map, reducing state
    * state backends: memory, `RocksDB`
    * checkpointing and consistent snapshots
    * savepoints and version migration
    * scaling state with rescaling
    * state size, `TTL` and cleanup
<!-- chapter: delivery-guarantees-and-exactly-once, duration: 3h -->
* Delivery guarantees and exactly-once
    * at-most-once, at-least-once, effectively-exactly-once
    * idempotent producers and consumers
    * two-phase commit sinks
    * transactional `Kafka`
    * replay and reprocessing semantics
    * the limits of "exactly-once"
<!-- chapter: kafka-as-the-substrate, duration: 3h -->
* `Kafka` as the substrate
    * topics, partitions, offsets and retention
    * consumer groups and rebalancing
    * the role of `Kafka` in streaming architectures
    * `Kafka Connect` for ingest and egress
    * `Schema Registry` and schema evolution
    * compaction and changelog topics
    * `Kafka` alternatives: Pulsar, `Kinesis`, `Redpanda`
<!-- chapter: apache-flink-deep-dive, duration: 4h -->
* `Apache Flink` deep dive
    * the `Flink` execution model
    * `DataStream` and Table/`SQL` APIs
    * checkpointing internals
    * exactly-once with `Flink` and `Kafka`
    * `CEP` and pattern detection
    * `Flink SQL` for streaming analytics
    * deployment options: standalone, `Kubernetes`, `Yarn`
<!-- chapter: kafka-streams-and-ksqldb, duration: 2h -->
* `Kafka Streams` and `ksqlDB`
    * the `Kafka Streams` library model
    * `KStream`, KTable, `GlobalKTable`
    * stateful operations and changelog topics
    * deployment as regular `JVM` apps
    * `ksqlDB` for `SQL`-driven streaming
    * comparing with `Flink`
<!-- chapter: spark-structured-streaming, duration: 2h -->
* `Spark Structured Streaming`
    * the micro-batch and continuous execution models
    * watermarking and stateful operations in `Spark`
    * integration with `Delta Lake` and Iceberg
    * `Spark` vs `Flink` for streaming workloads
    * operational considerations
<!-- chapter: apache-beam-and-portability, duration: 1h -->
* `Apache Beam` and portability
    * the `Beam` model
    * runners: `Dataflow`, `Flink`, `Spark`
    * the case for and against the portability layer
<!-- chapter: change-data-capture, duration: 3h -->
* Change-data-capture
    * `CDC` patterns: log-based, query-based, trigger-based
    * `Debezium` and the `Kafka Connect` connectors
    * `MySQL` binlog, `PostgreSQL` logical decoding, `MongoDB` change streams
    * schema changes and `DDL` propagation
    * outbox pattern as `CDC` from the application side
    * `CDC` to lakehouse, search, cache
<!-- chapter: streaming-and-the-lakehouse, duration: 2h -->
* Streaming and the lakehouse
    * stream-to-lake patterns
    * `Apache Iceberg`, `Delta Lake`, `Apache Hudi` for streaming writes
    * compaction, retention and partition evolution
    * `lambda` vs kappa architectures
    * unified batch and streaming processing
<!-- chapter: streaming-olap-and-real-time-analytics, duration: 2h -->
* Streaming `OLAP` and real-time analytics
    * Druid, `Pinot`, `ClickHouse`, Materialize, `RisingWave`
    * trade-offs of pre-aggregation vs raw events
    * incremental view maintenance
    * choosing a real-time analytical store
<!-- chapter: observability-for-streaming, duration: 2h -->
* Observability for streaming
    * lag and end-to-end latency metrics
    * watermark progress monitoring
    * state size and checkpoint duration
    * back-pressure detection
    * structured logging through a streaming job
    * tracing across stream boundaries
<!-- chapter: failure-recovery-and-replay, duration: 2h -->
* Failure recovery and replay
    * recovery from checkpoint
    * replay strategies and side effects
    * dealing with poison messages and dead-letter topics
    * versioning and rolling upgrades
    * runbook patterns for streaming incidents
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * end-to-end design walkthrough on a sample real-time pipeline
    * comparing engines for the workshop's workload
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
