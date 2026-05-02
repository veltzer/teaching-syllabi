---
tags:
  - concepts:observability
  - concepts:performance
  - concepts:cloud-economics
  - concepts:best-practices
level: advanced
category: observability
duration_hours: 16
audience:
  - audiences:senior-developers
  - audiences:devops
  - audiences:sres
  - audiences:performance-engineers
---
<!-- course: cardinality_engineering -->
# Cardinality Engineering

## Description
Cardinality is the silent killer of observability budgets. The catalog has `Prometheus and Grafana`,
`Advanced Prometheus`, `Prometheus Deep Dive`, `OpenTelemetry`, `OpenTelemetry Deep Dive`,
`VictoriaMetrics`, `Grafana` (basic and deep dive), Loki, Datadog, and `Dynatrace`. Each touches
the cardinality issue. None is the focused course on the engineering of cardinality: how to predict
it, how to measure it, how to reduce it without losing the signal you need, and how to design metrics
and logs to be cardinality-friendly from the start. Cardinality bills now exceed infrastructure bills
at many organizations. The team that does not engineer cardinality discovers this when the
observability vendor sends an emergency invoice or when `Prometheus` `OOMs`.

This two day course covers cardinality engineering as a focused practice. It covers what cardinality
is and where it comes from (the high-cardinality label, the user-`ID` mistake, the request-`ID`
mistake), the measurement (`prometheus_tsdb_head_series`, the `Datadog` cardinality view, the
`Grafana` cardinality explorer), the budgets per metric, the reduction techniques (label dropping,
relabeling, recording rules, exemplars-instead-of-labels, head sampling, tail sampling), the
exemplar-and-trace alternative, the per-vendor cost model (`Datadog` per-custom-metric, New Relic
per-`MELT`, Honeycomb per-event), the high-cardinality observability tools (`Honeycomb`,
`ClickHouse`-backed OTEL), the alerting story for cardinality itself, and the patterns that `make`
cardinality engineering a habit. Examples include real production cost-explosion incidents.
Participants leave able to control cardinality without losing the signal they need.

## Duration
16 hours / 2 days

## Intended Audience
* senior developers writing instrumentation
* `DevOps` engineers operating the metrics stack
* `SREs` managing observability cost
* performance engineers using metrics for analysis

## Prerequisites
* working experience with at least one metrics system
* exposure to the `Prometheus` Deep Dive course
* familiarity with the `OpenTelemetry` Deep Dive course is helpful
* basic understanding of time-series storage

## Objectives
* explain what cardinality is and where it explodes
* measure cardinality across the stack
* set per-metric and per-team cardinality budgets
* reduce cardinality without losing the signal
* compare metrics, exemplars, and structured events
* recognize and prevent the canonical cardinality disasters
* connect cardinality engineering to cost discipline

## Outline
<!-- chapter: what-cardinality-actually-is, duration: 1h -->
* What cardinality actually is
    * the unique-label-combination count
    * the time-series count
    * the per-metric vs per-target distinction
    * cross-reference to the Advanced `Prometheus` course
    * the canonical "we put `user_id` on a metric" disaster
<!-- chapter: where-cardinality-comes-from, duration: 2h -->
* Where cardinality comes from
    * the `user_id` mistake
    * the `request_id` mistake
    * the `path` with parameters
    * the dynamic environment
    * the "`Kubernetes` pod name as a label" reality
    * the multiplicative explosion across labels
<!-- chapter: measuring-cardinality, duration: 2h -->
* Measuring cardinality
    * `prometheus_tsdb_head_series` and friends
    * `topk()` and `count by (label)`
    * the `Datadog` cardinality view
    * the `Grafana` cardinality explorer
    * the per-metric trend over time
    * the alert that fires when cardinality spikes
<!-- chapter: per-metric-budgets, duration: 1h -->
* Per-metric budgets
    * the per-metric cardinality limit
    * the per-team budget
    * the deny-on-overflow vs sample-on-overflow choice
    * the "we never set a budget and ran out of memory" reality
    * the documentation pattern
<!-- chapter: reducing-cardinality, duration: 2h -->
* Reducing cardinality
    * label dropping
    * relabeling at scrape time
    * recording rules to aggregate
    * the per-bucket bucketing of high-cardinality keys
    * the "reduce-and-cache" pattern
    * the trade-off with debugging
<!-- chapter: exemplars-instead-of-labels, duration: 2h -->
* Exemplars instead of labels
    * the exemplar concept
    * `Prometheus` exemplars
    * `OpenTelemetry` exemplars
    * the trace-from-the-metric link
    * cross-reference to the Distributed Tracing in Practice course
    * when exemplars replace high-cardinality labels
<!-- chapter: high-cardinality-observability-tools, duration: 2h -->
* High-cardinality observability tools
    * `Honeycomb` and the structured-event model
    * `ClickHouse`-backed observability
    * the column-store argument
    * the "we moved off `Prometheus` for the high-cardinality use case" reality
    * picking
<!-- chapter: per-vendor-cost-models, duration: 2h -->
* Per-vendor cost models
    * `Datadog` custom metrics pricing
    * New Relic `MELT` pricing
    * `Honeycomb` event pricing
    * `Splunk` ingest pricing
    * the "we got a $200k bill from custom metrics" experience
<!-- chapter: head-and-tail-sampling, duration: 1h -->
* Head and tail sampling
    * trace head-sampling
    * trace tail-sampling
    * the per-service sampling rate
    * cross-reference to the `OpenTelemetry` Deep Dive course
    * the "we sampled out the rare failure" trap
<!-- chapter: instrumentation-discipline, duration: 1h -->
* Instrumentation discipline
    * the per-`PR` review of new metrics
    * the per-team naming convention
    * the "we cannot have any new label without approval" rigidity
    * the balance: enabling teams while preventing explosions
    * the periodic cardinality review

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
