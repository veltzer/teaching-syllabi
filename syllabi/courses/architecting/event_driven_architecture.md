---
tags:
  - concepts:architecture
  - concepts:distributed-systems
  - concepts:microservices
level: intermediate
category: architecture
duration_hours: 24
audience:
  - audiences:developers
  - audiences:architects
  - audiences:devops
---
<!-- course: event_driven_architecture -->
# `Event-Driven Architecture`

## Description
This course provides a comprehensive guide to designing, building, and operating event-driven systems. Participants will learn the fundamental concepts behind `event-driven architecture`, explore various messaging patterns and broker technologies, and understand how to apply patterns such as `event sourcing`, `CQRS`, and sagas in production systems. The course addresses practical concerns including schema evolution, idempotency, delivery guarantees, testing, monitoring, and common anti-patterns to avoid.

## Duration
24 hours / 3 days

## Intended Audience
* Software developers building distributed and `microservices`-based systems
* Software architects designing scalable and decoupled systems
* Technical leads evaluating messaging and event-driven strategies
* Backend engineers working with message brokers and streaming platforms
* `DevOps` engineers supporting event-driven infrastructure

## Prerequisites
* `Solid` understanding of software development fundamentals
* Familiarity with `REST APIs` and web service architecture
* Basic knowledge of distributed systems concepts
* Experience with at least one programming language (e.g., `Java`, `Python`, `C#`, Go)
* Basic understanding of databases and data persistence

## Required Knowledge
* `Python` Programming (or equivalent experience)

## Objectives
* Understand the principles and trade-offs of `event-driven architecture`
* Distinguish between events, commands, and queries and apply each appropriately
* Select and configure message brokers such as `Kafka`, `RabbitMQ`, `AWS SNS/SQS`, and `Azure Service Bus`
* Implement `event sourcing` and `CQRS` patterns
* Design reliable event-driven systems with idempotency and delivery guarantees
* Manage event schema evolution without breaking consumers
* Apply `saga` and choreography patterns for distributed workflows
* Monitor, observe, and troubleshoot event-driven systems in production

## Outline
<!-- chapter: event-driven-architecture-fundamentals, duration: 3h -->
* `Event-Driven Architecture` Fundamentals
    * What is `event-driven architecture` and why it matters
    * Events vs commands vs queries: definitions and responsibilities
    * Event types: domain events, integration events, and notifications
    * Event-driven vs request-driven architectures: trade-offs
    * Coupling and cohesion in event-driven systems
    * Producers, consumers, and event channels
    * Publish-subscribe and point-to-point messaging models
    * `Event-driven architecture` in the broader system landscape
<!-- chapter: message-brokers-and-streaming-platforms, duration: 3h -->
* Message Brokers and Streaming Platforms
    * Message broker fundamentals: topics, queues, partitions, and consumer groups
    * `Apache Kafka`: architecture, partitioning, replication, and consumer groups
    * `RabbitMQ`: exchanges, queues, bindings, and routing strategies
    * `AWS SNS/SQS`: fan-out, filtering, and integration patterns
    * `Azure Service Bus`: topics, subscriptions, and message sessions
    * Broker selection criteria: throughput, ordering, durability, and ecosystem
    * Configuring dead letter queues for failed message handling
    * Message serialization formats: `JSON`, `Avro`, `Protobuf`
<!-- chapter: event-sourcing-and-cqrs, duration: 3h -->
* `Event Sourcing` and `CQRS`
    * `Event sourcing`: storing state as a sequence of immutable events
    * Event store design: append-only logs and stream management
    * Rebuilding state from event history
    * Snapshots and performance optimization
    * Command Query Responsibility Segregation (`CQRS`): separating reads and writes
    * Building projections and read models from event streams
    * Eventual consistency: implications and user experience strategies
    * `When` `event sourcing` and `CQRS` are appropriate and when they are not
<!-- chapter: reliability-and-delivery-guarantees, duration: 3h -->
* Reliability and Delivery Guarantees
    * At-most-once, at-least-once, and exactly-once delivery semantics
    * Achieving idempotency in event consumers
    * Deduplication strategies and idempotency keys
    * Transactional outbox pattern for reliable event publishing
    * Ordering guarantees and partition-based ordering
    * Handling poison messages and retry policies
    * Circuit breakers and backpressure in event processing
    * Ensuring data consistency across services
<!-- chapter: saga-and-choreography-patterns, duration: 4h -->
* Saga and Choreography Patterns
    * Distributed transactions and the two-phase commit problem
    * Saga pattern: orchestration approach with a central coordinator
    * Choreography pattern: decentralized coordination through events
    * Designing compensating transactions for failure recovery
    * Long-running processes and timeout management
    * Combining orchestration and choreography
    * Error handling and partial failure scenarios
    * Tracking `saga` state and progress
<!-- chapter: event-schema-evolution-and-governance, duration: 4h -->
* Event Schema Evolution and Governance
    * The importance of event schema management
    * Schema evolution strategies: backward, forward, and full compatibility
    * Schema registry: `Confluent Schema Registry`, `AWS Glue Schema Registry`
    * Versioning events: embedding version in schema vs topic-based versioning
    * Handling breaking changes gracefully
    * Event catalogs and documentation
    * Event ownership and governance policies
    * Contracts between producers and consumers
<!-- chapter: event-driven-microservices-in-practice, duration: 4h -->
* Event-Driven `Microservices` in Practice
    * Decomposing monoliths into event-driven `microservices`
    * Service boundaries and event ownership
    * Testing event-driven systems: unit, integration, and contract testing
    * Consumer-driven contract testing for events
    * Monitoring and observability: distributed tracing, metrics, and logging
    * Correlation `IDs` and event traceability
    * Common anti-patterns: event soup, distributed `monolith`, and `temporal` coupling
    * Performance considerations: throughput, latency, and scaling strategies

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
