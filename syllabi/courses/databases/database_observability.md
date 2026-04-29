---
tags:
  - concepts:databases
  - concepts:observability
  - concepts:performance
  - concepts:operations
  - concepts:best-practices
level: advanced
category: database
duration_hours: 16
audience:
  - audiences:dbas
  - audiences:senior-developers
  - audiences:devops
  - audiences:sres
---
<!-- course: database_observability -->
# Database Observability

## Description
Most production databases are observed with three numbers: `CPU`, memory, and connection count. That is
not enough. The hard incidents are queries that worked yesterday and are slow today, replication that
is silently lagging, locks held longer than the application thinks, plans that flipped from index to
sequential scan, and connection pools that are exhausted upstream. The catalog covers per-database
administration (`Postgres`, `MySQL`, `MongoDB`, etc.) and the general observability stack (`Prometheus`,
`Grafana`, `OpenTelemetry`). It does not cover the specific discipline of making a database observable.

This two day course covers database observability as its own engineering practice. It covers the
canonical signals (queries, plans, locks, replication, IO, cache, connections, transactions, vacuum/GC),
the instrumentation approach (`auto_explain`, `pg_stat_statements`, `Performance Schema`,
`MySQL Performance Insights`, `MongoDB Profiler`, `RDS Performance Insights`), the dashboard that
matters, the alerts that page (and the ones that should not), the workflow of the on-call `DBA` or
on-call developer, the relationship to `APM`, the cost of observability itself, and the patterns that
`make` observability survive a database upgrade. Examples cover `Postgres`, `MySQL`, and `MongoDB`.
Participants leave able to `make` their database observable enough to debug a real incident.

## Duration
16 hours / 2 days

## Intended Audience
* `DBAs` upgrading their observability stack
* senior developers operating a database
* `DevOps` and `SREs` responsible for database health
* developers who are on-call for the database tier

## Prerequisites
* working experience with at least one relational database
* exposure to the `Prometheus` and `Grafana` course
* familiarity with the Query Optimization and Indexing course is helpful

## Objectives
* identify the canonical observability signals for a database
* instrument a database for production observability
* design dashboards that surface real problems
* set alerts that page on real failures
* connect database observability to application observability
* operate the observability itself
* compare observability across `Postgres`, `MySQL`, `MongoDB`

## Outline
<!-- chapter: why-cpu-and-memory-are-not-enough, duration: 1h -->
* Why `CPU` and memory are not enough
    * the queries-changed-without-warning problem
    * the silent-replication-lag problem
    * the lock-held-longer-than-expected problem
    * cross-reference to the Database Internals course
    * the canonical incident: "everything looks fine and queries are slow"
<!-- chapter: the-canonical-signals, duration: 2h -->
* The canonical signals
    * queries: counts, latencies, plans
    * locks: blockers, waiters, durations
    * replication: lag, throughput, conflicts
    * IO: reads, writes, cache hits
    * connections: pool, waits, idles
    * transactions: open, long, blocked
    * vacuum/GC: pending, throughput, age
<!-- chapter: postgres-observability, duration: 3h -->
* `Postgres` observability
    * `pg_stat_statements` as the foundation
    * `pg_stat_activity` for live state
    * `auto_explain` for slow plans
    * `pg_stat_replication` for replicas
    * `pgwatch2`, `pgexporter`, `Datadog` integration
    * the "we forgot to enable `pg_stat_statements`" reality
<!-- chapter: mysql-observability, duration: 2h -->
* `MySQL` observability
    * `Performance Schema` overview
    * `sys` schema for human-readable views
    * `Performance Insights` (`AWS RDS`)
    * `mysqld-exporter` for `Prometheus`
    * the "`Performance Schema` overhead" question
<!-- chapter: mongodb-observability, duration: 2h -->
* `MongoDB` observability
    * `MongoDB Profiler`
    * `currentOp` for live state
    * `Atlas` performance advisor
    * `mongodb-exporter` for `Prometheus`
    * the slow-query log
<!-- chapter: query-level-observability, duration: 1h -->
* Query-level observability
    * the per-query latency histogram
    * the plan-changed alert
    * the worst-query dashboard
    * cross-reference to the Query Optimization and Indexing course
    * the "we have no per-query data" reality
<!-- chapter: connecting-to-application-observability, duration: 1h -->
* Connecting to application observability
    * the application trace context that survives into the database
    * `OpenTelemetry` semantic conventions for `db.*`
    * cross-reference to the `OpenTelemetry` Deep Dive course
    * the "we cannot tie the slow query to the slow request" failure
    * end-to-end traces
<!-- chapter: alerting-on-databases, duration: 2h -->
* Alerting on databases
    * the alerts that should page
    * the alerts that should ticket
    * the cardinality of database alerts
    * the "we paged on `CPU` and missed the real issue" failure
    * `SLO`-driven database alerts
<!-- chapter: observability-during-incidents, duration: 1h -->
* Observability during incidents
    * the runbook query for "what is happening right now"
    * the kill-the-bad-query dance
    * the slow-replica failover signal
    * cross-reference to the Incident Response and Postmortems course
    * the post-incident query-timeline reconstruction
<!-- chapter: cost-of-observability-itself, duration: 1h -->
* Cost of observability itself
    * the overhead of `pg_stat_statements`
    * the overhead of `Performance Schema`
    * the cost of profiling
    * the cardinality cost in `Prometheus`
    * cross-reference to the Cardinality Engineering course

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
