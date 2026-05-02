---
tags:
  - tools:jaeger
  - observability:distributed-tracing
  - observability:monitoring
  - concepts:opentelemetry
level: intermediate
category: observability
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
  - audiences:sres
---
<!-- course: jaeger -->
# `Jaeger` Distributed Tracing

## Description
As microservice architectures grow in complexity, understanding the flow of a single request across dozens of services becomes a critical operational challenge. `Jaeger` is a battle-tested, open-source end-to-end distributed tracing system originally built by Uber and now hosted by the Cloud Native Computing Foundation. This course teaches participants how to deploy and operate `Jaeger`, instrument their applications using `OpenTelemetry`, and use the `Jaeger` UI to diagnose latency issues and understand service dependencies. Students will also learn advanced topics including sampling configuration, storage backend selection, and integration with `Prometheus` and `Grafana` to build a comprehensive observability stack.

## Duration
16 hours / 2 days

## Intended Audience
* Developers building and operating microservice-based applications who need to diagnose latency and correctness issues across service boundaries.
* `DevOps` engineers and SREs responsible for deploying and maintaining observability infrastructure in cloud-native environments.
* Platform engineers evaluating or adopting distributed tracing as part of an observability strategy.

## Prerequisites
* Familiarity with `microservices` and container-based deployments (`Docker`, `Kubernetes`).
* Basic experience with at least one programming language (Go, `Python`, `Java`, or `JavaScript`).
* Understanding of `HTTP` and basic networking concepts.
* Some exposure to observability concepts (metrics, logs) is helpful but not required.

## Required Knowledge
* `Docker` and `Kubernetes` fundamentals (or equivalent experience)
* `Linux` command-line proficiency

## Objectives
* Understand the principles and motivations behind distributed tracing
* Explain `Jaeger`'s architecture and how its components interact
* Instrument applications using the `OpenTelemetry` `SDK` to emit traces to `Jaeger`
* Deploy `Jaeger` in all-in-one, production, and `Kubernetes`-native configurations
* Navigate the `Jaeger` UI to search, visualize, and compare traces
* Configure head-based and tail-based sampling strategies to control trace volume
* Select and configure appropriate storage backends for different scale requirements
* Integrate `Jaeger` with `Prometheus` and `Grafana` for unified observability dashboards

## Outline
<!-- chapter: introduction-to-distributed-tracing, duration: 2h -->
* Introduction to Distributed Tracing
    * Observability in microservice architectures
    * The three pillars: metrics, logs, and traces
    * What distributed tracing solves: latency, errors, and dependencies
    * Traces, spans, and trace context explained
    * History: Dapper, `Zipkin`, OpenTracing, and the rise of `OpenTelemetry`
    * Overview of `Jaeger` and its place in the `CNCF` landscape
<!-- chapter: jaeger-architecture, duration: 2h -->
* `Jaeger` Architecture and Components
    * `Jaeger` agent and collector roles
    * Query service and `Jaeger` UI
    * Ingester and `Kafka`-based pipeline
    * All-in-one deployment for development
    * Production deployment topology
    * Data flow from instrumented application to storage
    * Configuration overview and environment variables
<!-- chapter: instrumentation-with-opentelemetry, duration: 3h -->
* Instrumentation with `OpenTelemetry`
    * `OpenTelemetry` `SDK` overview for trace instrumentation
    * Configuring the OTLP exporter to send spans to `Jaeger`
    * Creating spans manually: start, end, attributes, and events
    * Auto-instrumentation for `HTTP`, `gRPC`, and database clients
    * Context propagation with W3C Trace Context headers
    * Baggage propagation across service boundaries
    * Correlating traces with logs using trace and span `IDs`
    * Language-specific examples: Go, `Python`, `Java`
<!-- chapter: deploying-jaeger, duration: 2h -->
* Deploying `Jaeger`
    * Running `Jaeger` all-in-one with `Docker`
    * Deploying `Jaeger` on `Kubernetes` with the `Jaeger` Operator
    * Configuring the collector for high availability
    * Securing `Jaeger` with `TLS` and authentication
    * Helm chart deployment and configuration options
    * Resource sizing and capacity planning
<!-- chapter: analyzing-traces-in-jaeger-ui, duration: 2h -->
* Analyzing Traces in the `Jaeger` UI
    * Searching traces by service, operation, tags, and duration
    * Trace timeline view and span details
    * Identifying critical path and bottlenecks
    * Comparing traces side by side
    * Service dependency graph and call graphs
    * Deep linking and sharing traces
    * Trace statistics and error analysis
<!-- chapter: sampling-strategies, duration: 2h -->
* Sampling Strategies
    * Why sampling is necessary at scale
    * Head-based sampling: constant, probabilistic, rate-limiting
    * Tail-based sampling: sampling after the fact
    * Remote sampling configuration via `Jaeger` backend
    * Adaptive sampling and its trade-offs
    * Per-service and per-operation sampling rules
    * Impact of sampling on observability coverage
<!-- chapter: storage-backends, duration: 2h -->
* Storage Backends
    * In-memory storage for development and testing
    * `Elasticsearch` and `OpenSearch` as production backends
    * `Cassandra` for large-scale deployments
    * `Badger` embedded storage for single-node deployments
    * Configuring retention policies and index management
    * Performance characteristics and capacity planning per backend
    * Migrating between storage backends
<!-- chapter: integration-with-prometheus-and-grafana, duration: 1h -->
* Integration with `Prometheus` and `Grafana`
    * Exposing `Jaeger` internal metrics to `Prometheus`
    * Creating `Grafana` dashboards for `Jaeger` operational metrics
    * Linking traces in `Grafana` Tempo or `Jaeger` via exemplars
    * Correlating `Prometheus` alerts with `Jaeger` traces for root cause analysis
    * Building a unified observability workflow

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
