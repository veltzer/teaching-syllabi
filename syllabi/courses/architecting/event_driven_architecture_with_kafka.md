---
tags:
  - tools:kafka
  - concepts:architecture
  - concepts:distributed-systems
  - concepts:microservices
level: advanced
category: architecture
duration_hours: 16
audience:
  - audiences:architects
  - audiences:developers
  - audiences:devops
---
<!-- course: event_driven_architecture_with_kafka -->
# `Event-Driven Architecture` with `Kafka`

## Description
This course provides an in-depth exploration of `event-driven architecture` using `Apache Kafka` as the
central event backbone. Participants will learn how to design and implement systems based on event
sourcing and `CQRS` patterns, handle schema evolution, achieve exactly-once semantics, and apply
advanced patterns such as the `saga` pattern and the outbox pattern. The course also covers operational
concerns including dead letter topics and monitoring strategies for production `Kafka` deployments.

## Duration
16 hours / 2 days

## Intended Audience
* software architects designing event-driven systems
* senior developers building `microservices` with `Kafka`
* `DevOps` engineers responsible for `Kafka` infrastructure

## Prerequisites
* `solid` understanding of distributed systems concepts
* experience with `microservices` architecture
* familiarity with message queues and publish/subscribe patterns

## Objectives
* understand the principles and trade-offs of `event-driven architecture`
* design systems using `event sourcing` and `CQRS` patterns
* configure and operate `Kafka` as an event backbone
* implement exactly-once semantics and transactional messaging
* apply the `saga` pattern and outbox pattern for distributed transactions
* set up monitoring and handle failure scenarios with dead letter topics

## Outline
<!-- chapter: introduction-to-event-driven-architecture, duration: 1h -->
* introduction to `event-driven architecture`
    * event-driven vs request-driven architectures
    * benefits and trade-offs of event-driven design
    * event notifications vs event-carried state transfer
<!-- chapter: event-sourcing, duration: 2h -->
* `event sourcing`
    * principles of `event sourcing`
    * event store design
    * rebuilding state from events
    * snapshots and compaction
    * handling schema evolution in event stores
<!-- chapter: cqrs-command-query-responsibility-segregation, duration: 1h -->
* `CQRS` (Command Query Responsibility Segregation)
    * separating read and write models
    * eventual consistency considerations
    * projections and materialized views
    * combining `CQRS` with `event sourcing`
<!-- chapter: kafka-as-an-event-backbone, duration: 2h -->
* `Kafka` as an event backbone
    * `Kafka` architecture overview
    * topics, partitions, and consumer groups
    * producers and consumers configuration
    * `Kafka Streams` and ksqlDB
    * `Kafka Connect` for data integration
<!-- chapter: schema-registry, duration: 1h -->
* schema registry
    * the role of schema registry in event-driven systems
    * `Avro`, Protobuf, and `JSON Schema` support
    * schema evolution and compatibility modes
    * forward, backward, and full compatibility
<!-- chapter: exactly-once-semantics, duration: 1h -->
* exactly-once semantics
    * at-least-once vs at-most-once vs exactly-once
    * idempotent producers
    * transactional messaging in `Kafka`
    * end-to-end exactly-once with `Kafka Streams`
<!-- chapter: saga-pattern, duration: 2h -->
* `saga` pattern
    * choreography-based sagas
    * orchestration-based sagas
    * compensating transactions
    * `saga` execution coordinators
    * error handling and rollback strategies
<!-- chapter: outbox-pattern, duration: 2h -->
* outbox pattern
    * the dual-write problem
    * transactional outbox design
    * change data capture with Debezium
    * polling-based vs log-based outbox implementations
<!-- chapter: dead-letter-topics, duration: 2h -->
* dead letter topics
    * handling poison pills and malformed messages
    * dead letter topic configuration
    * retry strategies and backoff policies
    * alerting on dead letter topic activity
<!-- chapter: monitoring-and-operations, duration: 2h -->
* monitoring and operations
    * `Kafka` cluster monitoring with `JMX` and `Prometheus`
    * consumer lag monitoring
    * throughput and latency metrics
    * capacity planning and scaling strategies
    * operational best practices for production deployments

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
