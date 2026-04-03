---
tags:
  - tools:opentelemetry
  - practices:observability
  - practices:distributed-tracing
  - practices:monitoring
  - practices:instrumentation
level: intermediate
category: observability
duration_hours: 16
audience:
  - audiences:developers
  - audiences:sres
  - audiences:devops
---
<!-- course: opentelemetry -->
# `OpenTelemetry`

## Description
Modern distributed systems are composed of many services communicating over the network, making it increasingly difficult to understand system behavior, diagnose issues, and ensure reliability. `OpenTelemetry` is the industry-standard, vendor-neutral framework for collecting telemetry data including traces, metrics, and logs from distributed applications. It provides a unified set of APIs, SDKs, and tools for instrumenting, generating, collecting, and exporting observability data.

This course provides a comprehensive understanding of `OpenTelemetry` and its three pillars of observability. Participants will learn how to instrument applications, configure collectors and exporters, propagate context across service boundaries, and leverage auto-instrumentation to gain deep visibility into their systems with minimal code changes.

## Duration
16 hours / 2 days

## Intended Audience
* Developers, SREs, and `DevOps` engineers who want to implement observability in distributed systems using `OpenTelemetry`.
* Platform engineers responsible for building and maintaining observability infrastructure.

## Prerequisites
* Experience with at least one programming language (e.g., `Python`, `Java`, `Go`, `JavaScript`).
* Familiarity with distributed systems and `microservices` architecture.
* Basic understanding of `HTTP` and networking concepts.

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)

## Objectives
* Understand the three pillars of observability: traces, metrics, and logs
* Instrument applications using the `OpenTelemetry` `SDK`
* Configure and deploy `OpenTelemetry` Collectors
* Set up exporters to send data to various backends
* Implement context propagation across service boundaries
* Leverage auto-instrumentation for rapid integration

## Outline
<!-- chapter: introduction-to-observability, duration: 2h -->
* Introduction to Observability
    * Why observability matters in distributed systems
    * The three pillars: traces, metrics, and logs
    * Overview of the `OpenTelemetry` project
    * `OpenTelemetry` components and architecture
    * Relationship to OpenTracing and OpenCensus
<!-- chapter: distributed-tracing, duration: 2h -->
* Distributed Tracing
    * Spans, traces, and trace context
    * Creating and managing spans
    * Span attributes, events, and status
    * Span links and relationships
    * Sampling strategies
        * Head-based sampling
        * Tail-based sampling
<!-- chapter: metrics, duration: 3h -->
* Metrics
    * Metric data model
    * Instrument types
        * Counters
        * Gauges
        * Histograms
        * UpDownCounters
    * Metric views and aggregations
    * Metric exemplars
<!-- chapter: logs, duration: 1h -->
* Logs
    * Log data model
    * Log record attributes
    * Correlating logs with traces
    * Log bridges and appenders
<!-- chapter: instrumentation, duration: 1h -->
* Instrumentation
    * Manual instrumentation with the `OpenTelemetry` `SDK`
    * Creating custom spans and metrics
    * Adding attributes and events
    * Best practices for instrumentation
<!-- chapter: auto-instrumentation, duration: 1h -->
* Auto-Instrumentation
    * How auto-instrumentation works
    * Language-specific auto-instrumentation agents
    * Configuring auto-instrumentation
    * Combining auto and manual instrumentation
<!-- chapter: context-propagation, duration: 1h -->
* Context Propagation
    * The W3C Trace Context standard
    * Baggage propagation
    * Cross-service context propagation
    * Propagators and injection/extraction
<!-- chapter: opentelemetry-collector, duration: 2h -->
* `OpenTelemetry` Collector
    * Collector architecture
    * Receivers, processors, and exporters
    * Deploying the Collector as an agent and gateway
    * Collector configuration
    * Building custom Collector pipelines
    * Health monitoring and troubleshooting
<!-- chapter: exporters-and-backends, duration: 1h -->
* Exporters and Backends
    * OTLP (`OpenTelemetry` Protocol)
    * Exporting to `Jaeger`, `Zipkin`, and `Prometheus`
    * Exporting to commercial backends
    * Configuring multiple exporters
<!-- chapter: production-considerations, duration: 2h -->
* Production Considerations
    * Performance and overhead
    * Scaling the Collector
    * Security and data privacy
    * Resource detection and semantic conventions
    * Migrating existing instrumentation to `OpenTelemetry`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
