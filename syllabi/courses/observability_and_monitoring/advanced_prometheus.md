---
tags:
  - tools:prometheus
  - practices:monitoring
  - practices:observability
level: advanced
category: observability
duration_hours: 16
audience:
  - audiences:devops
  - audiences:sres
  - audiences:developers
---
<!-- course: advanced_prometheus -->
# Advanced `Prometheus`

## Description
This advanced course takes participants beyond the basics of `Prometheus` into production-grade monitoring and observability. The course covers `PromQL` in depth, recording and alerting rules with `Alertmanager`, federation, remote storage backends such as Thanos, Cortex, and Mimir, service discovery, relabeling, and high availability configurations. Participants will gain the skills needed to operate `Prometheus` at scale with confidence.

## Duration
16 hours / 2 days

## Intended Audience
* `DevOps` engineers and SREs operating `Prometheus` in production environments.
* Developers who need to write advanced queries and build alerting pipelines.

## Prerequisites
* `Solid` understanding of monitoring and observability concepts.
* Experience operating distributed systems.

## Required Knowledge
* `Prometheus` and `Grafana`

## Objectives
* Write complex `PromQL` queries for advanced analysis and troubleshooting.
* Design and implement recording rules for performance optimization.
* Configure `Alertmanager` with routing, grouping, and notification pipelines.
* Set up `Prometheus` federation for multi-cluster monitoring.
* Integrate remote write/read for long-term storage solutions.
* Implement high availability and capacity planning for `Prometheus` deployments.

## Outline
<!-- chapter: promql-deep-dive, duration: 2h -->
* `PromQL` Deep Dive
    * Data types and selectors
    * Range vectors and instant vectors
    * Aggregation operators
    * Binary operators and vector matching
    * Subqueries
    * Common query patterns and anti-patterns
    * Query performance optimization
<!-- chapter: recording-rules, duration: 1h -->
* Recording Rules
    * Why recording rules matter
    * Writing effective recording rules
    * Naming conventions
    * Rule group evaluation
    * Using recording rules for dashboards
<!-- chapter: alerting-rules-and-alertmanager, duration: 2h -->
* Alerting Rules and `Alertmanager`
    * Alerting rule syntax and evaluation
    * Alert states and lifecycle
    * `Alertmanager` architecture
    * Routing tree configuration
    * Grouping, inhibition, and silencing
    * Notification receivers (email, Slack, `PagerDuty`, webhooks)
    * `Alertmanager` high availability
    * Alert template customization
<!-- chapter: federation, duration: 1h -->
* Federation
    * Hierarchical federation
    * Cross-service federation
    * Federation use cases and patterns
    * Scaling with federation
    * Limitations and trade-offs
<!-- chapter: remote-write-and-read, duration: 1h -->
* Remote Write and Read
    * Remote write protocol
    * Remote read protocol
    * Configuring remote endpoints
    * Write-ahead log and reliability
    * Performance tuning for remote write
<!-- chapter: long-term-storage, duration: 2h -->
* Long-Term Storage
    * Thanos architecture and components
    * Cortex architecture and multi-tenancy
    * Mimir as a scalable metrics backend
    * Comparing long-term storage solutions
    * Object storage integration
    * Data retention and compaction
<!-- chapter: service-discovery, duration: 1h -->
* Service Discovery
    * Static vs dynamic service discovery
    * Supported service discovery mechanisms
    * `Kubernetes` service discovery
    * Consul, `DNS`, and file-based discovery
    * Custom service discovery with `HTTP` SD
<!-- chapter: relabeling, duration: 1h -->
* Relabeling
    * Relabeling concepts and stages
    * relabel_configs vs metric_relabel_configs
    * Common relabeling patterns
    * Dropping and keeping targets and metrics
    * Label manipulation for multi-tenant environments
<!-- chapter: exemplars, duration: 1h -->
* Exemplars
    * What are exemplars?
    * Instrumenting code with exemplars
    * Querying exemplars in `PromQL`
    * Exemplar integration with `Grafana` and tracing backends
<!-- chapter: high-availability, duration: 2h -->
* High Availability
    * `Prometheus` HA pair configurations
    * Deduplication strategies
    * `Alertmanager` clustering
    * Cross-region monitoring
    * Failover and recovery procedures
<!-- chapter: capacity-planning, duration: 2h -->
* Capacity Planning
    * Understanding `Prometheus` resource consumption
    * Estimating storage requirements
    * Cardinality management
    * Scaling strategies (vertical vs horizontal)
    * Performance benchmarking and tuning

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
