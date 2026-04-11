---
tags:
  - tools:prometheus
  - tools:grafana
  - practices:monitoring
  - practices:observability
  - tools:kubernetes
level: intermediate
category: observability
duration_hours: 16
audience:
  - audiences:sysadmins
  - audiences:devops
  - audiences:managers
---
<!-- course: prometheus_and_grafana -->
# `Prometheus` and `Grafana`

## Description
As current deployed applications and systems are becoming more complex with tools like `Kubernetes` and large cloud deployments, the need to understand how a system is performing and understand the source of problems as they appear becomes more important. In order to achieve all this new solutions are appearing, both for collecting distributed data about system status and for visualizing it for system engineers to digest.

`Prometheus` is a widely used time series database for storing online performance data of running systems and allow to create alerts in cases of issues. `Prometheus` is used in conjunction with other visualization solution in order to visualize on line and historic data to system engineers.

`Grafana` is a widely used visualization solution used to create dashboards and panels that `let` engineers penetrate the complexity of today's deployments. It is fairly easy to use and flexible and allow end user, even those without programming experience, to modify panels and dashboards and get at the information that they need.

## Duration
16 hours / 2 days

## Intended Audience
* Systems Administrators, IT Managers, SREs and `DevOps` / Operations engineers who want to collect and visualize data about their deployed systems using `Prometheus`.
* Any users of `Grafana` dashboards who want to understand how to modify their dashboards and panels in order to better monitor and understand what their systems are doing.

## Prerequisites
* Tech affinity.
* Some command line usage of `Linux` is recommended.

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Why Monitoring & Metrics are important
* `Prometheus` Architecture
* Obtaining & Configuring `Prometheus`
* Data collection methods
* Service Discovery
* Monitoring with `Prometheus`
* Setting up alerts
* Visualization with `Grafana`

## Outline
<!-- chapter: introduction, duration: 2h -->
* Introduction
    * Why is Monitoring important?
    * What should I be monitoring?
    * Which tools will suit my needs best?
    * `Prometheus` overview
    * `Grafana` overview
<!-- chapter: getting-started-with-prometheus, duration: 1h -->
* Getting started with `Prometheus`
    * Pre-requisites
    * Installing & configuring `Prometheus`
<!-- chapter: monitoring-fundamentals, duration: 3h -->
* Monitoring Fundamentals
    * What to monitor?
        * Node Exporter
        * `StatsD` Exporter
        * Graphite Exporter
        * Other popular community exporters
    * Push and Pull data collection
    * Service Level Objectives (SLOs)
    * Service Level Indicators (SLIs)
<!-- chapter: setting-up-your-metrics, duration: 6h -->
* Setting up your Metrics
    * Instrumenting an application
    * Endpoints
    * Label Naming
    * Working with Time Series data
    * Querying with PromQL
    * Metric types:
    * Counters
    * Gauges
    * Histograms
    * Functions and Operators
        * Aggregation
        * Binary Operators
        * Functions
    * Monitoring Apps
    * Collectors
    * Self-destructing apps
    * Platform as a Service (PAAS)
    * Jobs and Instances
    * Service Discovery
<!-- chapter: alerts, duration: 2h -->
* Alerts
    * Defining Alerting rules
    * Templating
    * Alert notifications
    * Setting up and configuring `Alertmanager` with `Prometheus`
    * Grouping
    * Inhibition
    * Silences
    * Behavior
<!-- chapter: visualization-with-grafana, duration: 2h -->
* Visualization with `Grafana`
    * Installing and configuring `Grafana` to work with `Prometheus`
    * Create a Dashboard
    * Adding a metrics endpoint as a data source
    * Securing user permissions and authentication
    * Publishing dashboards / snapshots

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
