---
tags:
  - concepts:opentelemetry
  - concepts:observability
  - concepts:distributed-systems
  - concepts:performance
  - concepts:microservices
  - concepts:operations
level: advanced
category: observability
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:sres
  - audiences:devops
  - audiences:performance-engineers
---
<!-- course: opentelemetry_deep_dive -->
# `OpenTelemetry` Deep Dive

## Description
`OpenTelemetry` has become the de facto standard for instrumenting distributed systems, and at first glance it looks
like a thin `SDK` you drop in and configure. In practice, running `OpenTelemetry` well at scale is a substantial
engineering effort: deciding what to instrument and what to ignore, choosing sampling strategies that preserve
diagnostic value without breaking budgets, designing the `Collector` topology, defining and enforcing semantic
conventions across teams, integrating with multiple vendor backends, and supporting non-standard workloads such as
`AI` pipelines and event-driven systems.

This five day course assumes participants have already used `OpenTelemetry` in a small-to-medium system and want to
operate it at organization scale. It covers the data model in depth, the `SDK` internals, the `Collector` as a
production system, sampling strategies, semantic conventions and `instrumentation` standards, integration patterns
across language ecosystems, and the migration story from legacy observability stacks.

## Duration
40 hours / 5 days

## Intended Audience
* `SRE`s and platform engineers running `OpenTelemetry` infrastructure
* senior developers leading `instrumentation` standards across multiple teams
* observability platform team members
* architects choosing between observability vendors and building portable strategies

## Prerequisites
* practical experience with `OpenTelemetry` `SDK` in at least one language
* working knowledge of `Kubernetes` and containerized deployments
* familiarity with at least one observability backend (`Prometheus`, `Jaeger`, Tempo, `Datadog`, etc.)
* basic understanding of distributed systems and `microservices`

## Objectives
* explain the `OpenTelemetry` data model for traces, metrics and logs in depth
* design `instrumentation` strategies across an organization
* operate the `Collector` as a production system with `HA` and capacity planning
* choose and tune sampling strategies for cost and diagnostic value
* enforce semantic conventions consistently across teams and languages
* extend `OpenTelemetry` with custom processors, exporters and instrumentations
* integrate `OpenTelemetry` with multiple backends and migrate between them
* govern an `OpenTelemetry` rollout with policies, ownership and lifecycle

## Outline
<!-- chapter: opentelemetry-architecture-revisited, duration: 2h -->
* `OpenTelemetry` architecture revisited
    * `API`, `SDK`, `Collector`, exporters, backends
    * the signals: traces, metrics, logs, profiles
    * the boundary between `OpenTelemetry` and the vendor
    * what `OpenTelemetry` is not: not a backend, not a `UI`
    * the project's governance and stability promises
<!-- chapter: the-data-model-in-depth, duration: 3h -->
* The data model in depth
    * resources, scopes and signals
    * trace context: `traceparent`, tracestate, `baggage`
    * span kinds, status, attributes and events
    * metric instruments: counter, up-down counter, histogram, gauge, observable variants
    * exemplars
    * `OTLP` and how it serializes everything
<!-- chapter: instrumentation-strategy, duration: 3h -->
* `Instrumentation` strategy
    * automatic vs manual `instrumentation`
    * what to instrument and what to ignore
    * the cost-of-instrumentation budget
    * coverage targets and how to measure them
    * `instrumentation` ownership and review
    * onboarding new services to your standard
<!-- chapter: sdk-internals, duration: 3h -->
* `SDK` internals
    * the provider, processor and exporter chain
    * batch vs simple span processors
    * buffering, back-pressure and dropped data
    * resource detection and attribute enrichment
    * context propagation across threads, async tasks and processes
    * shutdown semantics and the lost-spans problem
<!-- chapter: the-collector-as-a-production-system, duration: 4h -->
* The `Collector` as a production system
    * the `Collector` pipeline: receivers, processors, exporters, connectors
    * agent vs gateway deployment models
    * `HA`, scaling, capacity planning
    * resource limits and `OOM` avoidance
    * memory limiter, batch and queued retry processors
    * observability for the `Collector` itself
    * upgrade strategy
<!-- chapter: sampling-strategies, duration: 3h -->
* Sampling strategies
    * head sampling vs tail sampling
    * probabilistic, parent-based, rate-limiting samplers
    * tail sampling in the `Collector`
    * latency, error and rare-trace based sampling
    * sampling and statistical correctness in metrics
    * negotiating sampling budgets with cost
<!-- chapter: semantic-conventions, duration: 3h -->
* Semantic conventions
    * why semantic conventions matter at scale
    * the official semantic conventions (`HTTP`, `RPC`, database, messaging)
    * stability levels and managing breaking conventions
    * extending conventions for your organization
    * enforcement: linters, schema, code review
    * migrating from older convention versions
<!-- chapter: traces-deep-dive, duration: 2h -->
* Traces deep dive
    * span linking and span events vs separate spans
    * cross-process and cross-thread propagation
    * async and `concurrency` patterns
    * tracing message brokers and event-driven flows
    * `RPC`, database and queue semantic conventions
    * common tracing pitfalls
<!-- chapter: metrics-deep-dive, duration: 2h -->
* Metrics deep dive
    * choosing the right instrument
    * histogram bucket design and exponential histograms
    * cardinality control and attribute hygiene
    * `delta` vs cumulative temporality
    * metric views and customization
    * exemplars linking metrics to traces
<!-- chapter: logs-and-the-log-correlation-story, duration: 2h -->
* Logs and the log correlation story
    * logs as a first-class signal in `OpenTelemetry`
    * log appenders for popular logging libraries
    * trace-log correlation
    * structured logging conventions
    * migration from existing log pipelines
<!-- chapter: profiling-as-a-fourth-signal, duration: 1h -->
* Profiling as a fourth signal
    * the `OpenTelemetry` profiling effort
    * `pprof` integration
    * continuous profiling and `Pyroscope`/`Parca`
    * correlating profiles with traces
    * current state and stability
<!-- chapter: language-ecosystem-tour, duration: 3h -->
* Language ecosystem tour
    * `Java`, `Python`, Go, `Node.js`, `.NET`, Ruby, `PHP`
    * differences in maturity and idioms
    * automatic `instrumentation` across languages
    * common cross-language pitfalls
    * what to expect from third-party `instrumentation` libraries
<!-- chapter: extending-opentelemetry, duration: 3h -->
* Extending `OpenTelemetry`
    * custom processors and exporters
    * custom samplers
    * custom `instrumentation` libraries
    * the contrib repositories
    * publishing internal `instrumentation` packages
    * keeping custom code maintainable across `SDK` upgrades
<!-- chapter: vendor-integration-and-portability, duration: 2h -->
* Vendor integration and portability
    * exporting to `Datadog`, New Relic, Honeycomb, `Dynatrace`
    * exporting to open-source backends: `Tempo`, Mimir, Loki, `Jaeger`
    * dual-export and migration patterns
    * vendor lock-in and how to avoid it
    * cost considerations of `OTLP` ingest pricing
<!-- chapter: instrumentation-of-non-standard-workloads, duration: 2h -->
* `Instrumentation` of non-standard workloads
    * batch jobs and cron tasks
    * data pipelines and stream processors
    * `LLM` and `AI` pipelines
    * mobile and front-end `instrumentation`
    * serverless functions
<!-- chapter: governance-rollout-and-migration, duration: 1h -->
* Governance, rollout and migration
    * organizational rollout strategy
    * migration from `Zipkin`, `Jaeger client`, OpenCensus, `OpenTracing`
    * convention enforcement at scale
    * `instrumentation` ownership across teams
    * deprecating legacy observability stacks
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * end-to-end design walkthrough on a sample organization
    * common rollout pitfalls and how to avoid them
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
