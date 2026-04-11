---
tags:
  - tools:prometheus
  - practices:observability
  - practices:monitoring
level: intermediate
category: observability
duration_hours: 16
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: prometheus_deep_dive -->
# `Prometheus` Deep Dive

## Description
This course provides a comprehensive deep dive into `Prometheus`, the leading open-source monitoring and alerting toolkit. Participants will master PromQL, learn to instrument applications, configure service discovery, set up alerting with `Alertmanager`, and explore long-term storage solutions. The course prepares teams to build robust, scalable monitoring infrastructure with `Prometheus`.

## Duration
16 hours / 2 days

## Intended Audience
* Developers who need to instrument and monitor their applications
* `DevOps` engineers building monitoring infrastructure
* System administrators responsible for alerting and incident response

## Prerequisites
* Basic understanding of monitoring concepts (metrics, alerting).
* Familiarity with `Linux` command line.
* Basic knowledge of `HTTP` and networking.
* Experience with containerized environments is helpful.

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Understand the `Prometheus` architecture and pull-based model.
* Write advanced PromQL queries for analysis and alerting.
* Instrument applications using `Prometheus` client libraries.
* Configure service discovery for dynamic environments.
* Set up `Alertmanager` with routing, grouping, and silencing.
* Implement long-term storage with Thanos or Cortex.
* Operate `Prometheus` in `Kubernetes` environments.

## Outline
<!-- chapter: prometheus-architecture, duration: 1h -->
* `Prometheus` Architecture:
    * Pull-based monitoring model
    * Time-series database (TSDB) internals
    * Data model (metrics, labels, samples)
    * Scrape configuration and targets
    * Storage engine and retention
<!-- chapter: promql-fundamentals, duration: 1h -->
* PromQL Fundamentals:
    * Instant vectors and range vectors
    * Selectors and matchers
    * Arithmetic and comparison operators
    * Aggregation operators (sum, avg, min, max, count, topk)
    * Functions (rate, irate, increase, histogram_quantile, predict_linear)
<!-- chapter: advanced-promql, duration: 1h -->
* Advanced PromQL:
    * Subqueries
    * Recording rules for performance
    * Label manipulation functions
    * Common query patterns and anti-patterns
    * Dashboard-oriented queries
<!-- chapter: metric-types, duration: 1h -->
* Metric Types:
    * Counters and their usage patterns
    * Gauges for point-in-time values
    * Histograms for distribution measurement
    * Summaries vs histograms
    * Choosing the right metric type
<!-- chapter: instrumentation, duration: 2h -->
* Instrumentation:
    * `Go` client library
    * `Python` client library
    * `Java`/`JVM` client library
    * Naming conventions and best practices
    * Custom collectors and exporters
<!-- chapter: service-discovery, duration: 2h -->
* Service Discovery:
    * Static target configuration
    * `Kubernetes` service discovery
    * `DNS`-based service discovery
    * `File`-based service discovery
    * `Consul` service discovery
    * Relabeling for target manipulation
<!-- chapter: alerting-with-alertmanager, duration: 2h -->
* Alerting with `Alertmanager`:
    * Alerting rules in `Prometheus`
    * `Alertmanager` architecture
    * Routing tree configuration
    * Grouping and deduplication
    * Inhibition rules
    * Silencing alerts
    * Notification integrations (email, `Slack`, `PagerDuty`, webhooks)
<!-- chapter: relabeling, duration: 1h -->
* Relabeling:
    * relabel_configs for target relabeling
    * metric_relabel_configs for metric manipulation
    * Dropping metrics and labels
    * Common relabeling patterns
<!-- chapter: federation, duration: 1h -->
* Federation:
    * Hierarchical federation
    * Cross-service federation
    * Use cases and limitations
<!-- chapter: remote-write-and-remote-read, duration: 1h -->
* Remote Write and Remote Read:
    * Remote storage integrations
    * Remote write protocol
    * Remote read for querying external storage
<!-- chapter: long-term-storage, duration: 1h -->
* Long-Term Storage:
    * Thanos architecture and components
    * Cortex for horizontally scalable `Prometheus`
    * Choosing between Thanos and Cortex
    * Object storage backends
<!-- chapter: prometheus-on-kubernetes, duration: 1h -->
* `Prometheus` on `Kubernetes`:
    * `Prometheus` Operator
    * ServiceMonitor and PodMonitor resources
    * kube-`prometheus`-stack
    * Monitoring `Kubernetes` components
<!-- chapter: performance-tuning, duration: 1h -->
* Performance Tuning:
    * Cardinality management
    * Scrape interval optimization
    * Storage sizing and retention
    * Resource allocation and limits

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
