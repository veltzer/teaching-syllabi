---
tags:
  - tools:beam
  - data-and-ai:big-data
  - data-and-ai:streaming
level: intermediate
category: big-data
duration_hours: 24
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: apache_beam -->
# `Apache Beam`

## Description
This course provides a thorough introduction to `Apache Beam`, the unified programming model for
both batch and streaming data processing. Participants will learn to build portable data pipelines
using PCollections, PTransforms, windowing, and triggers, and deploy them on multiple runners
including DirectRunner, `Google Cloud Dataflow`, `Apache Flink`, and `Apache Spark`. The course
covers advanced topics such as state and timers, side inputs, cross-language transforms, `Beam SQL`,
and pipeline testing and monitoring.

## Duration
24 hours / 3 days

## Intended Audience
* software developers building data processing pipelines
* data scientists working with batch and streaming data

## Prerequisites
* Proficiency in `Python` or `Java` programming
* Basic understanding of distributed systems concepts
* Familiarity with data processing patterns (batch, streaming)
* Experience with command-line tools

## Required Knowledge
* `Python` Programming (or equivalent experience)

## Objectives
* **Understand the Beam programming model** including PCollections, PTransforms, and pipeline construction
* **Implement windowing and triggering strategies** for streaming data using fixed, sliding, and session `windows`
* **Write custom DoFn transforms** with state and timers for complex stateful processing
* **Deploy pipelines on multiple runners** including DirectRunner, Dataflow, `Flink`, and `Spark`
* **Test and validate pipelines** using Beam's testing utilities and assertion transforms
* **Apply advanced features** including side inputs, schema-aware transforms, and `Beam SQL`

## Outline
<!-- chapter: unified-batch-and-streaming-model, duration: 2h -->
* Unified Batch and Streaming Model
    * Why `Apache Beam`
        * The need for unified processing
        * Portability across runners
        * Beam vs native `Spark`/`Flink` APIs
    * Beam architecture overview
        * `SDK` layer
        * Runner layer
        * Execution engines
    * Key concepts
        * Bounded vs unbounded data
        * Event time vs processing time
        * Watermarks
<!-- chapter: beam-programming-model, duration: 2h -->
* Beam Programming Model
    * Pipelines
        * Pipeline construction
        * Pipeline options
        * Pipeline execution
    * PCollections
        * Creating PCollections
        * PCollection properties (immutability, element types)
        * Bounded and unbounded PCollections
    * PTransforms
        * Core transforms (Map, FlatMap, Filter, GroupByKey)
        * Combining elements (CombineGlobally, CombinePerKey)
        * Flatten and partition
        * Composite transforms
<!-- chapter: pardo-and-dofn, duration: 2h -->
* ParDo and DoFn
    * ParDo fundamentals
        * Writing a DoFn
        * ProcessElement method
        * Output tags and multiple outputs
    * Lifecycle methods
        * Setup and Teardown
        * StartBundle and FinishBundle
        * Bundle processing semantics
    * Advanced DoFn features
        * Accessing timestamp and window
        * Restriction tracking (splittable DoFn)
        * Error handling patterns
<!-- chapter: windowing, duration: 2h -->
* Windowing
    * Fixed `windows`
        * Window size configuration
        * Aligned and unaligned `windows`
    * Sliding `windows`
        * Window size and period
        * Overlapping elements
    * Session `windows`
        * Gap duration
        * Merging behavior
    * Global `windows`
        * Default windowing
        * Use cases
    * Window assignment and merging
        * Custom window functions
        * Window coders
<!-- chapter: triggers-and-accumulation, duration: 2h -->
* Triggers and Accumulation
    * Trigger types
        * Event time triggers
        * Processing time triggers
        * Data-driven triggers
        * Composite triggers
    * Accumulation modes
        * Accumulating
        * Discarding
        * Accumulating and retracting
    * Allowed lateness
        * Late data handling
        * Garbage collection
    * Trigger `design patterns`
        * Early and late firings
        * Speculative results
<!-- chapter: side-inputs, duration: 2h -->
* Side Inputs
    * Side input patterns
        * View as singleton
        * View as list
        * View as map
        * View as multimap
    * Side input use cases
        * Enrichment joins
        * Dynamic configuration
        * Lookup tables
    * Side input performance
        * Caching behavior
        * Size considerations
        * Freshness in streaming
<!-- chapter: state-and-timers, duration: 2h -->
* State and Timers
    * State types
        * Value state
        * Bag state
        * Combining state
        * Map state
        * Set state
    * Timer types
        * Event time timers
        * Processing time timers
    * Stateful processing patterns
        * Sessionization
        * Deduplication
        * Batching elements
        * Custom windowing logic
<!-- chapter: i-o-connectors, duration: 2h -->
* `I/O` Connectors
    * Built-in connectors
        * `File` `I/O` (TextIO, AvroIO, ParquetIO)
        * Database `I/O` (JdbcIO, BigQueryIO)
        * Messaging `I/O` (KafkaIO, PubSubIO)
    * Connector configuration
        * Read and write options
        * Schema mapping
        * Error handling
    * Custom `I/O` development
        * Source and sink `API`
        * Bounded and unbounded sources
        * Dynamic work rebalancing
<!-- chapter: runners, duration: 2h -->
* Runners
    * DirectRunner
        * Local development and testing
        * Debugging pipelines
    * `Google Cloud Dataflow`
        * Dataflow service configuration
        * Autoscaling
        * Streaming engine
        * Flex templates
    * `Apache Flink` runner
        * `Flink` cluster deployment
        * Checkpointing and savepoints
        * Configuration options
    * `Apache Spark` runner
        * `Spark` cluster deployment
        * Batch and streaming modes
        * Configuration options
<!-- chapter: testing-pipelines, duration: 1h -->
* Testing Pipelines
    * Unit testing transforms
        * TestPipeline
        * PAssert assertions
        * Testing DoFn logic
    * Integration testing
        * Test `I/O` connectors
        * End-to-end pipeline tests
    * Testing windowed and triggered pipelines
        * TestStream
        * Advancing watermarks
        * Verifying output timing
<!-- chapter: schema-aware-transforms, duration: 2h -->
* Schema-Aware Transforms
    * Beam schemas
        * Schema definition
        * Schema inference
        * Row types
    * Schema transforms
        * Field selection
        * Field renaming
        * Type conversion
    * `Beam SQL`
        * `SQL` transform
        * `SQL` dialect support
        * Joins and aggregations in `SQL`
        * Mixing `SQL` and programmatic transforms
<!-- chapter: cross-language-transforms, duration: 1h -->
* Cross-Language Transforms
    * Multi-language pipelines
        * Expansion service
        * `Python` transforms in `Java` pipelines
        * `Java` transforms in `Python` pipelines
    * Cross-language `I/O`
        * Using `Java` connectors from `Python`
        * Configuration and serialization
<!-- chapter: deployment-and-monitoring, duration: 2h -->
* Deployment and Monitoring
    * Pipeline deployment strategies
        * Template-based deployment
        * Containerized deployment
        * `CI/CD` for pipelines
    * Monitoring and observability
        * Pipeline metrics
        * Custom counters and distributions
        * Logging best practices
    * Performance tuning
        * Fusion optimization
        * Parallelism configuration
        * Memory management
        * Shuffle optimization

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
