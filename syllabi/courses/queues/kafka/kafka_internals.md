---
tags:
  - tools:kafka
  - data-and-ai:message-queues
  - data-and-ai:streaming
  - concepts:distributed-systems
level: advanced
category: message-queue
duration_hours: 16
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: kafka_internals -->
# `Kafka` Internals

## Description
The `Kafka` Internals training course is designed to teach students about the publish/subscribe messaging system with many advanced configurations. `Apache Kafka` is an open-source stream processing platform used to provide a unified, high-throughput, low-latency system for handling real-time data feeds from a wide range of source systems.

The course begins with covering configurations, allowing students to discover brokers, consumers, producers, and topics. Next, students will build their own `Kafka` clusters. The course will conclude by looking at applying their knowledge from the course to real-world scenarios like processing real-time stock price updates from an `API` and consolidating that into a data lake.

## Duration
16 hours / 2 days

## Intended Audience
* Developers and developer teams looking to leverage `Kafka` architecture that know `Java` and basic `Linux` commands.

## Prerequisites
* `Java` programming

## Objectives
* Understand the `Kafka` architecture and describe the roles and responsibilities of various Daemons
* Use producers, consumers, and brokers within `Kafka`
* Construct a streaming `ETL` pipeline using `Kafka` Connect
* Explain how and `when` to use `Kafka` developer APIs
* Perform real-time analytics using KSQL

## Outline
<!-- chapter: kafka-fundamentals-internals, duration: 5h -->
* `Kafka` Fundamentals & Internals
    * Logical Architecture of `Kafka`
    * Physical Architecture of `Kafka`
        * Partitions
        * Topics
        * Replicas
        * Producers & Consumers
        * Brokers
    * Roles and Responsibilities of various components
    * Replication mechanism
    * Message Delivery Semantic
    * Key Terminologies
    * Key configuration settings of Brokers, Producers, Consumers, etc.
    * Schema Evolution Concepts
    * Hands-on Exercise(s)
<!-- chapter: zookeeper, duration: 1h -->
* `Zookeeper`
    * Role of `Zookeeper`
    * `Zookeeper` Basic Operations
    * `Apache Kafka` - `Zookeeper` Role
    * Exploring `Zookeeper`
<!-- chapter: kafka-administration, duration: 1h -->
* `Kafka` Administration
    * Things to consider in Administration
    * Monitoring `Kafka`
    * `Kafka` Security
    * Performance Tuning `Kafka` Cluster
<!-- chapter: kafka-integration, duration: 2h -->
* `Kafka` Integration
    * End to End Data Pipeline using `Kafka`
    * Why `Kafka` Connect?
    * Architecture
    * Tuning
    * Build End to End Streaming `ETL` Pipeline
    * Hands-on Exercise(s)
<!-- chapter: kafka-core-apis, duration: 5h -->
* `Kafka` Core APIs
    * Overview
    * Producer `API`
        * Sync Producers
        * `Async` Producers
        * Message Acknowledgment
        * Batching Messages
        * Keyed and Non-Keyed Messages
        * Compression
        * Batching
    * Consumer `API`
    * Hands-on Exercise(s)
<!-- chapter: ksql-db, duration: 2h -->
* KSQL DB
    * Overview
    * What is KSQLDB
    * Why KSQLDB
    * Hands-on Exercise(s)

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
