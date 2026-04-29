---
tags:
  - concepts:observability
  - concepts:distributed-systems
  - concepts:performance
  - concepts:best-practices
level: advanced
category: observability
duration_hours: 24
audience:
  - audiences:senior-developers
  - audiences:devops
  - audiences:sres
  - audiences:performance-engineers
---
<!-- course: distributed_tracing_in_practice -->
# Distributed Tracing in Practice

## Description
The catalog has `OpenTelemetry`, `OpenTelemetry Deep Dive`, `Jaeger`, and `Datadog`. Each touches
distributed tracing. None is the focused course on the engineering practice of operating distributed
tracing in a real production system: how to instrument across the stack, how to propagate context
through every boundary (`HTTP`, `gRPC`, message queue, database, batch job, frontend), how to sample
without losing the rare failure, how to exploit traces in incidents and in steady state, and how to
keep the tracing bill from exceeding the infrastructure bill.

This three day course covers distributed tracing as a focused practice. It covers the canonical span
model, the propagation standards (`W3C Trace Context`, `B3`), the per-language `SDKs` (auto and
manual instrumentation in `Python`, `Java`, `Go`, `Node.js`, `.NET`), the cross-boundary cases (the
`async` message-queue trace, the cron-job trace, the frontend `RUM` trace, the worker-pool trace), the
sampling decisions (head, tail, probabilistic, parent-based, dynamic), the backend choices (`Jaeger`,
`Tempo`, `Honeycomb`, `Datadog APM`, `New Relic`, `AWS X-Ray`, `Google Cloud Trace`), the
trace-as-a-debugging-tool workflow (the slow-trace investigation, the error-attribution), the
trace-as-a-design-tool insight (the service-dependency map, the request flow), the cost discipline
(cross-reference to cardinality), the cardinality-of-attributes problem, the propagation through
proxies and load balancers, and the patterns that `make` tracing actually used. Examples include real
production debugging walkthroughs. Participants leave able to deploy and exploit distributed tracing.

## Duration
24 hours / 3 days

## Intended Audience
* senior developers instrumenting services
* `DevOps` and `SREs` operating the tracing stack
* performance engineers using traces for analysis
* developers debugging tail-latency incidents

## Prerequisites
* working experience with at least one distributed system
* exposure to the `OpenTelemetry` Deep Dive course
* familiarity with at least one observability stack
* basic understanding of `HTTP` and `gRPC`

## Objectives
* explain the span model and the trace structure
* propagate context across all boundaries
* instrument with `OpenTelemetry` in at least one language
* pick a sampling strategy
* deploy and operate a tracing backend
* debug a real incident with traces
* recognize the patterns that `make` tracing useless

## Outline
<!-- chapter: the-span-model, duration: 1h -->
* The span model
    * `trace_id`, `span_id`, parent
    * span attributes
    * span events
    * the canonical example
    * cross-reference to the `OpenTelemetry` Deep Dive course
<!-- chapter: w3c-trace-context-and-b3, duration: 2h -->
* `W3C Trace Context` and `B3`
    * the `traceparent` and `tracestate` headers
    * the `B3` legacy
    * propagator interoperability
    * the "the trace stopped at the gateway" failure
    * the multi-vendor case
<!-- chapter: instrumentation-auto-and-manual, duration: 3h -->
* Instrumentation: auto and manual
    * auto-instrumentation in `Python`, `Java`, `Node.js`, `.NET`
    * the manual span for the business operation
    * the right attributes per span
    * the no-too-many-spans rule
    * the "auto-instrumentation produced 1000 spans per request" failure
<!-- chapter: cross-language-and-cross-runtime, duration: 2h -->
* Cross-language and cross-runtime
    * the `Python`-to-`Go` `gRPC` call
    * the `Java`-to-`Node.js` `HTTP` call
    * the consistent semantic conventions
    * the `OpenTelemetry` `Collector` as the bridge
    * the "the trace was broken across services" reality
<!-- chapter: async-and-message-queue-tracing, duration: 2h -->
* `Async` and message-queue tracing
    * `Kafka` and trace context in headers
    * `RabbitMQ` and trace context
    * the worker-pool case
    * the "the trace ended at the producer" failure
    * the link span vs the parent span
<!-- chapter: frontend-tracing-and-rum, duration: 2h -->
* Frontend tracing and `RUM`
    * the browser `OpenTelemetry SDK`
    * the `traceparent` from the page to the backend
    * the `Web Vitals` integration
    * the "we cannot see the user-side latency" reality
    * cross-reference to the Network Observability Engineering course
<!-- chapter: sampling-strategies, duration: 3h -->
* Sampling strategies
    * head sampling at fixed rate
    * parent-based sampling
    * tail sampling on the `Collector`
    * dynamic sampling (rate-by-priority)
    * the "we sampled out every error" anti-pattern
    * picking
<!-- chapter: the-tracing-backend, duration: 2h -->
* The tracing backend
    * `Jaeger`
    * `Grafana Tempo`
    * `Honeycomb`
    * `Datadog APM`, `New Relic`, `AWS X-Ray`, `Google Cloud Trace`
    * the cost shape of each
    * picking
<!-- chapter: opentelemetry-collector-pipelines, duration: 2h -->
* `OpenTelemetry Collector` pipelines
    * receiver, processor, exporter
    * the per-tenant routing
    * tail-sampling on the collector
    * the "we deployed without a collector and shipped from each pod" failure
    * the deployment topology
<!-- chapter: tracing-during-an-incident, duration: 2h -->
* Tracing during an incident
    * the slow-trace investigation
    * the per-step latency breakdown
    * the error-attribution walkthrough
    * the "the trace told us the answer in 30 seconds" experience
    * the runbook
<!-- chapter: tracing-as-a-design-tool, duration: 1h -->
* Tracing as a design tool
    * the service-dependency map
    * the discovery of unexpected calls
    * the "we did not know we depended on that" finding
    * the architecture-review with traces
    * the per-team trace dashboard
<!-- chapter: cost-and-cardinality, duration: 1h -->
* Cost and cardinality
    * the per-trace cost
    * the per-attribute cardinality
    * cross-reference to the Cardinality Engineering course
    * the "we shipped traces and the bill exploded" reality
    * the budget per service
<!-- chapter: troubleshooting-tracing-itself, duration: 1h -->
* Troubleshooting tracing itself
    * the broken propagation
    * the missing service
    * the wrong-clock skew
    * the "we cannot tell if the trace is wrong or the system is" debugging
    * the validation tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
