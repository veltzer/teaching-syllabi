---
tags:
  - tools:apache-pulsar
  - messaging:pub-sub
  - messaging:streaming
  - concepts:distributed-systems
level: intermediate
category: message-queue
duration_hours: 24
audience:
  - audiences:developers
  - audiences:architects
  - audiences:data-engineers
---
<!-- course: apache_pulsar -->
# `Apache Pulsar`

## Description
`Apache Pulsar` is a cloud-native, distributed messaging and streaming platform that combines the durability
and replayability of a log-based system with the flexibility of a traditional message broker. This course
covers `Pulsar`'s unique multi-layer architecture separating compute from storage, its rich subscription model,
and the `Pulsar Functions` serverless compute framework. Participants will learn to design tenancy and namespace
hierarchies, build event-driven applications, connect external systems via `Pulsar IO`, and operate `Pulsar` in
production with geo-replication and tiered storage. The course concludes with a practical guide for teams
migrating from `Apache Kafka`.

## Duration
24 hours / 3 days

## Intended Audience
* Backend developers building high-throughput event-driven and streaming applications.
* Data engineers integrating `Pulsar` into real-time data pipelines.
* Architects designing multi-tenant, globally distributed messaging platforms.
* Engineers evaluating `Pulsar` as a replacement for or complement to `Apache Kafka`.

## Prerequisites
* `Solid` programming experience in `Java`, `Python`, or `Go`.
* Familiarity with distributed systems concepts such as replication, partitioning, and fault tolerance.
* Basic understanding of messaging patterns (pub/sub, queuing) is assumed.

## Objectives
* Explain `Pulsar`'s architecture and how it differs from `Kafka` and traditional brokers.
* Design topic hierarchies using tenants, namespaces, and topics.
* Produce and consume messages using the `Pulsar` client `API`.
* Choose and configure the appropriate subscription type for each use case.
* Write lightweight stream-processing logic with `Pulsar Functions`.
* Connect external systems using `Pulsar IO` source and sink connectors.
* Configure tiered storage to offload cold data to object stores.
* Set up geo-replication for disaster recovery and global distribution.
* Secure a `Pulsar` cluster with authentication and authorisation.
* Plan and execute a migration from `Apache Kafka` to `Apache Pulsar`.

## Outline
<!-- chapter: introduction-to-apache-pulsar, duration: 2h -->
* Introduction to `Apache Pulsar`:
    * Messaging and streaming use cases.
    * `Pulsar` history and the Yahoo! origins.
    * Key differentiators: multi-tenancy, geo-replication, unified queuing and streaming.
    * Installing `Pulsar` locally and with `Docker`.
    * First producer and consumer walkthrough.
<!-- chapter: pulsar-architecture, duration: 2h -->
* `Pulsar` Architecture:
    * Brokers, `BookKeeper` ledgers, and `ZooKeeper` coordination.
    * Separation of compute and storage layers.
    * Bookie quorums and write/read quorum semantics.
    * Topic ownership and bundle assignment.
    * Persistent vs. non-persistent topics.
<!-- chapter: topics-namespaces-and-tenants, duration: 2h -->
* Topics, Namespaces, and Tenants:
    * Multi-tenancy model and isolation boundaries.
    * Creating and managing tenants and namespaces.
    * Partitioned topics and partition routing.
    * Topic compaction and retention policies.
    * Namespace-level policies: `TTL`, backlog quotas, deduplication.
<!-- chapter: producers-and-consumers, duration: 3h -->
* Producers and Consumers:
    * `Pulsar` client `API` overview.
    * Producer configuration: routing modes, compression, batching.
    * Consumer configuration: receive modes and push vs. pull.
    * Message acknowledgment: individual and cumulative.
    * Schema registry and schema enforcement.
    * Readers and the seek `API` for log replay.
<!-- chapter: subscriptions-and-message-ordering, duration: 2h -->
* Subscriptions and Message Ordering:
    * Subscription types: exclusive, shared, failover, key-shared.
    * Ordering guarantees per subscription type.
    * Dead-letter topics and retry topics.
    * Negative acknowledgment and redelivery policies.
<!-- chapter: pulsar-functions, duration: 3h -->
* `Pulsar` Functions:
    * Serverless stream processing in `Pulsar`.
    * Writing functions in `Java`, `Python`, and `Go`.
    * Function deployment: local runner, cluster mode.
    * State storage and counters in functions.
    * Function metrics and monitoring.
    * `Pulsar` `SQL` and `Flink` integration overview.
<!-- chapter: pulsar-io-connectors, duration: 2h -->
* `Pulsar IO` Connectors:
    * Source and sink connector architecture.
    * Built-in connectors: `Kafka`, `Cassandra`, `Elasticsearch`, `JDBC`.
    * Deploying and managing connectors.
    * Writing a custom connector.
<!-- chapter: tiered-storage, duration: 2h -->
* Tiered Storage:
    * Hot vs. cold data and storage cost optimisation.
    * Offloading ledger segments to `S3`, `GCS`, or `Azure Blob`.
    * Configuring offload policies per namespace.
    * Reading offloaded data transparently.
<!-- chapter: geo-replication, duration: 2h -->
* Geo-Replication:
    * Active-active and active-passive replication topologies.
    * Configuring replication clusters.
    * Per-message replication and deduplication.
    * Failover and replication lag monitoring.
<!-- chapter: authentication-and-authorisation, duration: 2h -->
* Authentication and Authorisation:
    * Authentication mechanisms: `JWT`, `TLS`, `OAuth2`, `Kerberos`.
    * Role-based access control (`RBAC`) for topics and namespaces.
    * Encryption at `rest` and in transit.
    * Audit logging best practices.
<!-- chapter: kafka-migration-to-pulsar, duration: 2h -->
* `Kafka` Migration to `Pulsar`:
    * `Pulsar`'s `Kafka` compatibility protocol (`KoP`).
    * Topic and consumer group mapping.
    * Incremental migration strategies.
    * Comparing operational characteristics and trade-offs.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
