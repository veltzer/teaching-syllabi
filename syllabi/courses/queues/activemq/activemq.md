---
tags:
  - tools:activemq
  - messaging:jms
  - messaging:enterprise
  - concepts:message-broker
level: intermediate
category: message-queue
duration_hours: 24
audience:
  - audiences:developers
  - audiences:java-developers
  - audiences:architects
---
<!-- course: activemq -->
# `ActiveMQ`

## Description
`Apache ActiveMQ` is one of the most widely deployed open-source message brokers, implementing the ```Java``
Message Service` (``JMS``) specification and supporting a broad range of messaging protocols including ``AMQP``,
`STOMP`, `MQTT`, and `OpenWire`. This course provides a thorough grounding in enterprise messaging patterns,
the `JMS` `API`, and `ActiveMQ`'s persistence, clustering, and high-availability capabilities. Participants will
also explore `ActiveMQ Artemis`, the next-generation broker that underpins `Red Hat AMQ` and the future of the
`ActiveMQ` project, and will leave with practical skills for migrating and interoperating between broker
generations and competing products.

## Duration
24 hours / 3 days

## Intended Audience
* `Java` developers integrating enterprise messaging into their applications using `JMS`.
* Architects designing reliable, decoupled enterprise integration solutions.
* `DevOps` and middleware engineers operating and tuning `ActiveMQ` in production environments.
* Teams evaluating `ActiveMQ Artemis` for new deployments or migration from classic `ActiveMQ`.

## Prerequisites
* `Solid` `Java` programming experience.
* Basic understanding of enterprise application architecture and integration patterns.
* Familiarity with the command line and `XML` configuration files.

## Objectives
* Understand the fundamental concepts and benefits of enterprise messaging.
* Describe the `ActiveMQ` broker architecture and its core components.
* Install, configure, and manage an `ActiveMQ` broker.
* Use the `JMS` `API` to send and receive messages from `Java` applications.
* Implement point-to-point queue and publish-subscribe topic messaging.
* Configure message persistence with `KahaDB` and `JDBC`.
* Apply transaction and acknowledgment strategies for reliable delivery.
* Secure a broker with authentication, authorisation, and transport encryption.
* Set up `ActiveMQ` clusters and network of brokers for high availability.
* Monitor broker health using the Web Console and `JMX`.
* Explain the `ActiveMQ Artemis` architecture and its advantages.
* Plan and execute migrations and interoperability between broker implementations.

## Outline
<!-- chapter: introduction-to-enterprise-messaging, duration: 2h -->
* Introduction to Enterprise Messaging:
    * Why enterprise messaging? Decoupling, resilience, and scalability.
    * Messaging patterns: point-to-point, publish-subscribe, request-reply.
    * The `JMS` specification and its role in the `Java` ecosystem.
    * Overview of messaging protocols: `AMQP`, `STOMP`, `MQTT`, `OpenWire`.
    * `ActiveMQ` in the enterprise integration landscape.
<!-- chapter: activemq-architecture, duration: 2h -->
* `ActiveMQ` Architecture:
    * Broker components: connector, transport, message store.
    * The `ActiveMQ` broker configuration file (`activemq.xml`).
    * Destinations: queues and topics.
    * Virtual destinations and composite destinations.
    * Message lifecycle and the broker's role.
<!-- chapter: installation-and-configuration, duration: 2h -->
* Installation and Configuration:
    * Installing `ActiveMQ` on `Linux` and `Windows`.
    * Directory layout and key configuration files.
    * Starting, stopping, and checking broker status.
    * The `ActiveMQ` Web Console overview.
    * Configuring transports and ports.
<!-- chapter: jms-api-fundamentals, duration: 2h -->
* `JMS` `API` Fundamentals:
    * `ConnectionFactory`, `Connection`, `Session`, and `Destination`.
    * `MessageProducer` and `MessageConsumer` creation.
    * Message types: `TextMessage`, `BytesMessage`, `MapMessage`, `ObjectMessage`.
    * Message headers, properties, and selectors.
    * Synchronous and asynchronous (`MessageListener`) consumption.
    * JNDI lookup and dependency injection with Spring.
<!-- chapter: queue-and-topic-messaging, duration: 2h -->
* Queue and Topic Messaging:
    * Point-to-point queuing and competing consumers.
    * Publish-subscribe with durable and non-durable subscriptions.
    * Message selectors for content-based routing.
    * Wildcards in topic names.
    * Temporary queues and topics for request-reply.
<!-- chapter: message-persistence-and-storage, duration: 2h -->
* Message Persistence and Storage:
    * Persistent vs. non-persistent message delivery.
    * `KahaDB` storage: configuration and tuning.
    * `JDBC` persistence for relational database backends.
    * Journal-based persistence and performance considerations.
    * Dead letter queues and undeliverable message handling.
<!-- chapter: transactions-and-acknowledgements, duration: 2h -->
* Transactions and Acknowledgements:
    * `JMS` acknowledgment modes: AUTO, CLIENT, DUPS_OK.
    * Local `JMS` transactions and session-level rollback.
    * `XA` transactions for distributed transaction support.
    * Exactly-once delivery strategies and idempotent consumers.
    * Poison message handling and redelivery policies.
<!-- chapter: security-and-authentication, duration: 2h -->
* Security and Authentication:
    * Simple authentication plugin: users and groups.
    * `JAAS`-based authentication for enterprise environments.
    * Authorisation: destination-level `ACLs`.
    * Enabling `SSL`/`TLS` for transport encryption.
    * Certificate-based client authentication.
<!-- chapter: clustering-and-high-availability, duration: 2h -->
* Clustering and High Availability:
    * Network of brokers: store-and-forward topology.
    * Master-slave failover pairs with shared storage.
    * `Replicated LevelDB` store for clustered persistence.
    * Load balancing consumers across a network.
    * Designing for zero message loss and fast failover.
<!-- chapter: monitoring-and-management, duration: 2h -->
* Monitoring and Management:
    * `JMX` and the `ActiveMQ` management `API`.
    * Monitoring with `Hawtio` and the Web Console.
    * Key metrics: queue depth, consumer count, enqueue/dequeue rates.
    * Alerting with `Prometheus` and `Grafana`.
    * Advisory messages for broker events.
<!-- chapter: activemq-artemis, duration: 2h -->
* `ActiveMQ Artemis` (Next Generation):
    * Artemis architecture: non-blocking `I/O`, journal-based persistence.
    * Differences from classic `ActiveMQ`.
    * Address model: addresses, queues, and routing types.
    * Supported protocols: `AMQP`, `CORE`, `STOMP`, `MQTT`, `OpenWire`.
    * Clustering and high availability in `Artemis`.
<!-- chapter: migration-and-interoperability, duration: 2h -->
* Migration and Interoperability:
    * Classic `ActiveMQ` to `Artemis` migration path.
    * Interoperating with `RabbitMQ` and `Apache Kafka`.
    * Protocol bridges and transformations.
    * Phased migration strategies for production systems.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
