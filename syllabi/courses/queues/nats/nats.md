---
tags:
  - tools:nats
  - messaging:pub-sub
  - messaging:cloud-native
  - concepts:distributed-systems
level: intermediate
category: message-queue
duration_hours: 16
audience:
  - audiences:developers
  - audiences:architects
  - audiences:devops
---
<!-- course: nats -->
# `NATS`

## Description
`NATS` is an ultra-lightweight, cloud-native messaging system designed for simplicity, performance, and
resilience in `microservices` and distributed systems. This course covers the full `NATS` stack from the
foundational core publish-subscribe model through the persistence and exactly-once semantics of `JetStream`,
and the built-in key-value and object stores that turn `NATS` into a complete distributed data layer. Participants
will also learn how to secure clusters with `TLS` and `NKey` authentication and how to scale horizontally with
clustering and leaf node topologies.

## Duration
16 hours / 2 days

## Intended Audience
* Developers building `microservices`, edge computing, or IoT applications.
* Platform and `DevOps` engineers evaluating lightweight messaging infrastructure.
* Architects designing cloud-native systems that require low-latency communication.

## Prerequisites
* `Solid` programming experience in at least one language (Go, `Python`, `JavaScript`, or similar).
* Basic understanding of networking and client-server communication.
* Familiarity with publish-subscribe patterns is helpful but not required.

## Objectives
* Understand the `NATS` subject hierarchy and core messaging model.
* Implement publish-subscribe and fan-out messaging patterns.
* Build synchronous request-reply workflows over `NATS`.
* Persist and replay messages using `NATS JetStream` streams.
* Configure consumers for push- and pull-based message delivery.
* Use the `NATS` key-value store for distributed state management.
* Store and retrieve binary data with the `NATS` object store.
* Secure a `NATS` deployment with `TLS`, `NKeys`, and `Accounts`.
* Deploy and operate a `NATS` cluster with leaf node extensions.

## Outline
<!-- chapter: introduction-to-nats, duration: 1h -->
* Introduction to `NATS`:
    * The `NATS` philosophy: simplicity, speed, and resiliency.
    * Core `NATS` vs `JetStream`: when to use each.
    * Installing the `NATS` server and `nats` `CLI`.
    * Subject naming conventions and wildcards (`*` and `>`).
<!-- chapter: core-nats-publish-subscribe, duration: 2h -->
* Core `NATS` — Publish Subscribe:
    * Subjects, publishers, and subscribers.
    * Fan-out and broadcast messaging.
    * Queue groups for load-balanced consumers.
    * At-most-once delivery semantics.
    * Subject hierarchies and namespacing strategies.
<!-- chapter: request-reply-pattern, duration: 1h -->
* Request Reply Pattern:
    * Synchronous request-reply over `NATS`.
    * Inbox subjects and automatic reply routing.
    * Scatter-gather patterns for parallel responses.
    * Timeout handling and service discovery.
<!-- chapter: nats-jetstream, duration: 2h -->
* `NATS JetStream`:
    * Motivation: persistence, replay, and exactly-once delivery.
    * Enabling and configuring `JetStream`.
    * Publish with acknowledgment and idempotent publishing.
    * At-least-once and exactly-once delivery guarantees.
    * `JetStream` `API` overview.
<!-- chapter: streams-and-consumers, duration: 2h -->
* Streams and Consumers:
    * Stream configuration: subjects, limits, retention, and storage.
    * Consumer types: push and pull.
    * Durable vs. ephemeral consumers.
    * Ack policies: explicit, none, and all.
    * Consumer filtering and subject transforms.
    * Replay policies and start positions.
<!-- chapter: key-value-store, duration: 2h -->
* Key-Value Store:
    * `JetStream`-backed key-value store overview.
    * Get, put, delete, and purge operations.
    * Watching keys for real-time change notifications.
    * `TTL`, history, and revision tracking.
    * Use cases: feature flags, configuration, leader election.
<!-- chapter: object-store, duration: 2h -->
* Object Store:
    * Storing large binary objects in `NATS`.
    * Chunked upload and download.
    * Listing and describing stored objects.
    * Use cases: firmware distribution, artifact sharing.
<!-- chapter: nats-security, duration: 2h -->
* `NATS` Security:
    * `TLS` configuration for client and cluster connections.
    * Authentication: username/password, `NKeys`, `JWT` credentials.
    * Accounts and the decentralised security model.
    * Subject-level permissions and import/export.
<!-- chapter: nats-clustering-and-leaf-nodes, duration: 2h -->
* `NATS` Clustering and Leaf Nodes:
    * Server clustering for high availability.
    * Route and gateway connections.
    * Leaf nodes for edge and regional deployments.
    * Monitoring with the `NATS` monitoring endpoint and `nats-surveyor`.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
