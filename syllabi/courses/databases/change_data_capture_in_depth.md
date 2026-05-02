---
tags:
  - concepts:databases
  - concepts:data-integration
  - concepts:best-practices
  - concepts:operations
level: advanced
category: database
duration_hours: 24
audience:
  - audiences:data-engineers
  - audiences:senior-developers
  - audiences:architects
  - audiences:devops
---
<!-- course: change_data_capture_in_depth -->
# Change Data Capture in Depth

## Description
Change Data Capture (`CDC`) is the discipline of turning a database's change history into a stream that
other systems can consume. It is what powers most modern data integration: data lakes hydrated from
operational databases, search indexes that stay in sync, caches that invalidate themselves, microservice
events that are derived from the source-of-truth, and the `outbox` pattern. The catalog has touches on
streaming systems and on `Kafka`, but `CDC` as its own engineering discipline is large enough to deserve
its own course.

This three day course covers `CDC` from the database's transaction log to the consumer. It covers
log-based vs query-based vs trigger-based `CDC`, the Debezium architecture, the `Maxwell` and
`AWS DMS` architectures, schema evolution under `CDC`, the exactly-once question, the snapshot-and-stream
problem, the `outbox` pattern, the relationship of CDC to `event sourcing`, the operational realities of
running `CDC` against a busy `OLTP` database, the failure modes (replication slot bloat, snapshot drift,
schema-skew), and the data-governance story. Participants leave able to choose a `CDC` approach, design
the consumer side correctly, and operate a `CDC` pipeline that does not break the source database.

## Duration
24 hours / 3 days

## Intended Audience
* data engineers building integration pipelines from operational databases
* senior developers introducing `CDC` into a production system
* architects designing event-driven systems on top of relational data
* platform engineers running `CDC` as a paved-road service

## Prerequisites
* working knowledge of at least one relational database
* familiarity with `Kafka` or a comparable message system
* exposure to the Streaming Data Systems course is helpful

## Objectives
* choose between log-based, query-based, and trigger-based `CDC`
* operate `Debezium` against a production database safely
* handle schema evolution end-to-end
* solve the snapshot-and-stream problem
* implement the `outbox` pattern correctly
* reason about delivery semantics
* recognize and prevent the operational failures
* compare `CDC` to `event sourcing`

## Outline
<!-- chapter: what-cdc-is-and-what-it-is-not, duration: 1h -->
* What `CDC` is and what it is not
    * the change log as a primary source
    * `CDC` vs replication vs `ETL`
    * `CDC` vs `event sourcing`
    * cross-reference to the `Event Sourcing` in Practice course
    * the use cases that need `CDC` and the ones that do not
<!-- chapter: log-based-vs-query-based-vs-trigger-based, duration: 2h -->
* Log-based vs query-based vs trigger-based
    * the transaction log as the truth
    * the polling approach and its costs
    * the trigger approach and its costs
    * why log-based dominates in production
    * vendor support across `Postgres`, `MySQL`, Oracle, `SQL Server`
<!-- chapter: postgres-logical-replication-and-wal, duration: 2h -->
* `Postgres` logical replication and `WAL`
    * the write-ahead log as the source
    * replication slots
    * publication and subscription
    * `wal2json` and `pgoutput`
    * the replication-slot-bloat failure
    * cross-reference to the `Postgres` course
<!-- chapter: mysql-binlog-cdc, duration: 2h -->
* `MySQL` binlog `CDC`
    * the `binlog` format options
    * row-based vs statement-based
    * `GTID` and the resumable position
    * the `binlog` retention question
    * cross-reference to the `MySQL` course
<!-- chapter: debezium-architecture, duration: 3h -->
* `Debezium` architecture
    * `Debezium` connectors and `Kafka Connect`
    * the source-connector lifecycle
    * the offset store and the schema history
    * `Debezium` topology against a production database
    * the "we ran `Debezium` once and it crashed our primary" failure
<!-- chapter: snapshot-and-stream, duration: 2h -->
* Snapshot and stream
    * the initial snapshot problem
    * snapshot consistency
    * the locking vs non-locking trade-off
    * incremental snapshots
    * the "the snapshot took two days and the `binlog` rolled" failure
<!-- chapter: schema-evolution-under-cdc, duration: 2h -->
* Schema evolution under `CDC`
    * the schema registry
    * column adds, column drops, column renames
    * type changes
    * the consumer-vs-producer schema drift
    * cross-reference to the `API` Evolution and Versioning course
<!-- chapter: delivery-semantics, duration: 2h -->
* Delivery semantics
    * at-least-once is the default
    * the deduplication strategy
    * the idempotent-consumer pattern
    * cross-reference to the Idempotency course
    * the exactly-once myth
<!-- chapter: the-outbox-pattern, duration: 2h -->
* The `outbox` pattern
    * the dual-write problem
    * the outbox table as transactional event source
    * `Debezium`'s outbox event router
    * the cleanup strategy
    * the "we used a queue alongside the database and lost events" failure
<!-- chapter: alternatives-to-debezium, duration: 1h -->
* Alternatives to `Debezium`
    * `Maxwell`, Canal, `AWS DMS`, `Striim`
    * `Postgres`-native: pg_recvlogical, `wal2json`
    * managed `CDC`: `Fivetran`, `Airbyte`
    * cross-reference to the `Airbyte` course
    * picking among them
<!-- chapter: cdc-consumers-and-sinks, duration: 2h -->
* `CDC` consumers and sinks
    * search index sink
    * data warehouse sink
    * cache invalidation sink
    * service-event sink
    * the consumer that cannot keep up
<!-- chapter: operating-cdc-in-production, duration: 2h -->
* Operating `CDC` in production
    * monitoring lag
    * monitoring slot bloat
    * the failover question
    * `DBA` coordination
    * the "we forgot the slot existed and the disk filled" incident
<!-- chapter: governance-and-pii, duration: 1h -->
* Governance and `PII`
    * the change stream contains everything, including secrets
    * masking at the source
    * masking at the sink
    * cross-reference to the `GDPR` and Compliance course
    * audit and lineage

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
