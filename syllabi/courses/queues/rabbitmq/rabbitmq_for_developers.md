---
tags:
  - tools:rabbitmq
  - data-and-ai:message-queues
  - concepts:distributed-systems
level: intermediate
category: message-queue
duration_hours: 16
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: rabbitmq_for_developers -->
# `RabbitMQ` for Developers

## Description
This course provides a comprehensive introduction to `RabbitMQ` for software developers. It covers the `AMQP` protocol, core messaging concepts such as exchanges, queues, and bindings, as well as advanced routing patterns, pub/sub, RPC, dead letter queues, message persistence, and client libraries. Students will learn to design and implement reliable messaging solutions and test their messaging infrastructure.

## Duration
16 hours / 2 days

## Intended Audience
* Software developers building distributed applications
* Backend engineers integrating messaging into their systems
* Architects designing event-driven and microservice architectures

## Prerequisites
* `Solid` programming experience in at least one language (`Python`, `Java`, `JavaScript`, or similar).
* Basic understanding of networking and client-server communication.
* Familiarity with distributed systems concepts is helpful but not required.

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)

## Objectives
* Understand the `AMQP` protocol and `RabbitMQ` architecture.
* Configure and work with exchanges, queues, and bindings.
* Implement common messaging patterns including pub/sub and RPC.
* Design routing strategies using direct, topic, fanout, and headers exchanges.
* Handle message persistence, acknowledgments, and delivery guarantees.
* Use dead letter queues for error handling and retry logic.
* Integrate `RabbitMQ` into applications using client libraries.
* Test and debug messaging workflows.

## Outline
<!-- chapter: introduction-to-rabbitmq-and-amqp, duration: 2h -->
* Introduction to `RabbitMQ` and `AMQP`:
    * Message broker concepts and use cases.
    * The `AMQP` protocol overview.
    * `RabbitMQ` architecture and components.
    * Installation and management console.
<!-- chapter: exchanges-queues-and-bindings, duration: 2h -->
* Exchanges, Queues, and Bindings:
    * Queue declaration and properties.
    * Exchange types: direct, fanout, topic, and headers.
    * Binding keys and routing keys.
    * Default and custom exchange configuration.
<!-- chapter: routing-patterns, duration: 2h -->
* Routing Patterns:
    * Direct routing for point-to-point messaging.
    * Topic-based routing with wildcards.
    * Fanout for broadcast messaging.
    * Headers exchange for attribute-based routing.
<!-- chapter: publish-subscribe, duration: 1h -->
* Publish/Subscribe:
    * Pub/sub pattern with fanout exchanges.
    * Filtering messages with topic exchanges.
    * Consumer groups and competing consumers.
<!-- chapter: rpc-with-rabbitmq, duration: 1h -->
* RPC with `RabbitMQ`:
    * Request-reply pattern.
    * Correlation `IDs` and reply queues.
    * Timeout handling and error propagation.
<!-- chapter: dead-letter-queues-and-error-handling, duration: 2h -->
* Dead Letter Queues and Error Handling:
    * Dead letter exchanges and queues.
    * Message rejection and nacking.
    * Retry strategies and delayed requeuing.
    * Poison message handling.
<!-- chapter: message-persistence-and-reliability, duration: 2h -->
* Message Persistence and Reliability:
    * Durable queues and persistent messages.
    * Publisher confirms and consumer acknowledgments.
    * Transactions vs. publisher confirms.
    * High availability queues and mirroring.
<!-- chapter: client-libraries-and-integration, duration: 2h -->
* Client Libraries and Integration:
    * Working with `RabbitMQ` client libraries.
    * Connection and channel management.
    * Serialization and message formats.
    * Integration with web frameworks and `microservices`.
<!-- chapter: testing-messaging-workflows, duration: 2h -->
* Testing Messaging Workflows:
    * Unit testing message producers and consumers.
    * Integration testing with `RabbitMQ`.
    * Monitoring and debugging with the management plugin.
    * Performance and load testing.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
