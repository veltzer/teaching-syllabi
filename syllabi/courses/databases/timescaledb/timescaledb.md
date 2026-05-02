---
tags:
  - tools:timescaledb
  - tools:postgresql
  - data-and-ai:data-analysis
level: intermediate
category: database
duration_hours: 16
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: timescaledb -->
# TimescaleDB: Time-Series Database on `PostgreSQL`

## Description
This course covers TimescaleDB, a time-series database built as an extension on top of `PostgreSQL`. Participants will learn how to model, store, and query time-series data efficiently using hypertables, continuous aggregates, compression, and specialized time functions. The course also covers integration with visualization tools, performance tuning, and comparison with other time-series solutions.

## Duration
16 hours / 2 days

## Intended Audience
* Software developers working with time-series data
* Data scientists and data engineers building analytics pipelines
* Backend engineers designing monitoring and IoT systems

## Prerequisites
* `Solid` understanding of `SQL` and relational databases.
* Familiarity with `PostgreSQL` basics.
* Basic understanding of time-series data concepts.

## Required Knowledge
* `PostgreSQL` for Developers (or equivalent experience)

## Objectives
* Understand the TimescaleDB architecture including hypertables and chunks.
* Install and configure TimescaleDB on `PostgreSQL`.
* Design schemas and create hypertables for time-series workloads.
* Use continuous aggregates and compression for efficient storage and querying.
* Write advanced time-series queries using hyperfunctions and time_bucket.
* Integrate TimescaleDB with `Grafana` for visualization.
* Tune TimescaleDB for production performance.

## Outline
<!-- chapter: introduction-to-time-series-data, duration: 1h -->
* Introduction to Time-Series Data:
    * What is time-series data
    * Common use cases (IoT, monitoring, financial data, logs)
    * Challenges of time-series at scale
    * Comparison with `InfluxDB` and `Prometheus`
<!-- chapter: timescaledb-architecture, duration: 1h -->
* TimescaleDB Architecture:
    * TimescaleDB as a `PostgreSQL` extension
    * Hypertables and chunks
    * How TimescaleDB partitions data automatically
    * Advantages of building on `PostgreSQL`
<!-- chapter: installation-and-setup, duration: 1h -->
* Installation and Setup:
    * Installing TimescaleDB on `PostgreSQL`
    * Configuration parameters (timescaledb.max_background_workers, memory settings)
    * Verifying the installation
<!-- chapter: creating-and-managing-hypertables, duration: 1h -->
* Creating and Managing Hypertables:
    * Converting regular tables to hypertables
    * Choosing partition columns and chunk intervals
    * Schema design for time-series data
    * Multi-dimensional partitioning
<!-- chapter: querying-time-series-data, duration: 1h -->
* Querying Time-Series Data:
    * time_bucket function for time-based aggregation
    * Hyperfunctions (approximate count distinct, percentile, time-weighted averages)
    * Gap filling and interpolation
    * Last observation carried forward
<!-- chapter: continuous-aggregates, duration: 2h -->
* Continuous Aggregates:
    * Creating continuous aggregates
    * Refresh policies
    * Real-time aggregation
    * Cascading continuous aggregates
<!-- chapter: data-retention-and-compression, duration: 2h -->
* Data Retention and Compression:
    * Data retention policies
    * Automated data dropping
    * Native compression
    * Compression policies and scheduling
    * Querying compressed data
<!-- chapter: real-time-aggregation, duration: 1h -->
* Real-Time Aggregation:
    * Combining real-time and materialized data
    * Streaming aggregation patterns
    * Handling late-arriving data
<!-- chapter: grafana-integration, duration: 2h -->
* `Grafana` Integration:
    * Connecting `Grafana` to TimescaleDB
    * Building time-series dashboards
    * Using TimescaleDB-specific query patterns in `Grafana`
    * Alerting on time-series data
<!-- chapter: multi-node-setup, duration: 2h -->
* Multi-Node Setup:
    * Distributed hypertables
    * Access nodes and data nodes
    * Data distribution strategies
    * Limitations and considerations
<!-- chapter: performance-tuning, duration: 2h -->
* Performance Tuning:
    * Index strategies for time-series queries
    * Chunk sizing optimization
    * Memory and disk configuration
    * Query optimization techniques
    * Monitoring TimescaleDB performance

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
