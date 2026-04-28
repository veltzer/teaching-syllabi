---
tags:
  - concepts:distributed-systems
  - concepts:eventual-consistency
  - concepts:acid
  - concepts:microservices
  - concepts:architecture
  - concepts:design-patterns
  - concepts:best-practices
level: advanced
category: architecture
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:architects
---
<!-- course: idempotency_and_distributed_consistency -->
# Idempotency and Distributed Consistency

## Description
The single most underrated topic in distributed systems is idempotency. Most production bugs in distributed systems
trace back to it: duplicate payments, double-booked seats, replayed webhooks, drifted counters, lost messages
that turn out not to be lost. The fix is rarely difficult once you know the pattern, and almost always painful
if you discover it after the system has already shipped.

This five day course is dedicated entirely to idempotency, exactly-once semantics and the related distributed
consistency patterns. It covers the theory (what idempotency really means in a distributed setting, why
"exactly-once" is a marketing term, the relationship to consensus and to transactions), the patterns that `make`
distributed operations safe to retry (idempotency keys, deduplication, transactional outbox, sagas, deterministic
replay), and the operational practices that keep these systems healthy in production. Examples are drawn from
payments, e-commerce, messaging and streaming systems. Participants leave able to design distributed APIs and
workflows that survive every retry `storm`, network partition and replay scenario their users can throw at them.

## Duration
40 hours / 5 days

## Intended Audience
* senior developers building distributed APIs and workflows
* architects designing systems with strong correctness requirements
* engineers working on payments, billing, ordering or messaging systems
* engineers who have ever debugged a duplicate-charge or duplicate-message incident

## Prerequisites
* `solid` backend development experience
* working knowledge of `HTTP`, at least one database and at least one message broker
* basic familiarity with distributed systems concepts (replication, partitioning, consensus)
* experience operating production systems is helpful

## Objectives
* define idempotency precisely in a distributed setting
* design APIs whose retry semantics are safe by construction
* implement and operate idempotency-key systems at scale
* apply transactional outbox, inbox and `saga` patterns correctly
* reason about exactly-once delivery and its real-world limits
* design deterministic replay and recovery flows
* avoid the most common distributed correctness pitfalls

## Outline
<!-- chapter: why-idempotency-is-the-most-underrated-topic, duration: 2h -->
* Why idempotency is the most underrated topic
    * the universal retry problem
    * payments, messages and writes that must not duplicate
    * the cost of getting this wrong, with public examples
    * idempotency vs commutativity vs determinism
    * what "at-least-once" really means in production
<!-- chapter: defining-idempotency-precisely, duration: 3h -->
* Defining idempotency precisely
    * mathematical idempotency vs operational idempotency
    * idempotency at the function vs the operation vs the workflow level
    * `HTTP` semantics: which methods are idempotent and which are not
    * idempotency in the presence of side effects
    * "weak" idempotency and its uses
    * the difference between idempotent and safe
<!-- chapter: at-least-once-everywhere, duration: 2h -->
* At-least-once everywhere
    * why distributed systems retry
    * timeouts, partial failure and the unknown outcome
    * client retries vs server retries vs broker retries
    * retry storms and back-off strategies
    * "exactly-once" as a marketing term
    * effectively-exactly-once: what it actually means
<!-- chapter: idempotency-keys-the-pattern, duration: 4h -->
* Idempotency keys: the pattern
    * the client-supplied key model
    * key scope: per-customer, per-merchant, global
    * the request-fingerprint approach
    * storage and lookup of keys
    * `TTL` and key retention
    * concurrent retries with the same key
    * `Stripe`-style idempotency `API` design
<!-- chapter: deduplication-and-replay-windows, duration: 3h -->
* Deduplication and replay `windows`
    * server-side deduplication tables
    * bloom filters and probabilistic dedup
    * window-based dedup in streaming
    * `Kafka` exactly-once and producer idempotence
    * dedup and partition assignment
    * recovering from dedup-table corruption
<!-- chapter: transactions-and-their-limits, duration: 2h -->
* Transactions and their limits
    * `ACID` revisited
    * the `XA` two-phase commit and why it lost
    * single-database transactions as the easy case
    * what transactions cannot give you across services
    * isolation levels and idempotency interactions
<!-- chapter: the-transactional-outbox-pattern, duration: 3h -->
* The transactional outbox pattern
    * the "publish after commit" problem
    * the outbox table design
    * relay process and `CDC`-driven publishers
    * outbox at scale: partitioning, retention, cleanup
    * outbox and ordering guarantees
    * common outbox bugs
<!-- chapter: the-inbox-pattern-and-consumer-side-dedup, duration: 2h -->
* The inbox pattern and consumer-side dedup
    * inbox table design
    * processing-with-dedup transaction
    * combining inbox with exactly-once consumers
    * inbox table growth and cleanup
    * inbox vs database-internal idempotency
<!-- chapter: sagas-and-long-running-workflows, duration: 4h -->
* Sagas and long-running workflows
    * the `saga pattern` and compensation
    * orchestration vs choreography for sagas
    * idempotency requirements for `saga` steps
    * retries and partial completion
    * `saga` state stores
    * `Temporal`, `Cadence`, `Camunda`, custom orchestrators
    * the cost of compensation logic
<!-- chapter: deterministic-replay, duration: 3h -->
* Deterministic replay
    * `event sourcing` and replay
    * deterministic vs nondeterministic event handlers
    * external side effects during replay
    * versioning event handlers and replay
    * using replay for backfill and migration
    * deterministic replay in `Temporal` workflows
<!-- chapter: idempotent-api-design, duration: 3h -->
* Idempotent `API` design
    * choosing `PUT` vs `POST` vs `POST` with idempotency key
    * naming and modeling resources idempotently
    * idempotency in batch endpoints
    * `webhooks` that retry forever
    * `webhook` consumer requirements
    * documenting idempotency for `API` clients
<!-- chapter: distributed-counters-and-aggregates, duration: 2h -->
* Distributed counters and aggregates
    * naive counters drift under retries
    * idempotent increment patterns
    * `CRDT`s for distributed counting and sets
    * idempotency in stream aggregations
    * reconciling drift after the fact
<!-- chapter: time-clocks-and-ordering, duration: 2h -->
* Time, clocks and ordering
    * physical clocks vs logical clocks
    * Lamport and vector clocks
    * `HLC` (`hybrid logical clock`)
    * monotonic time inside a service
    * the relationship between ordering and idempotency
    * ordering across partitions and shards
<!-- chapter: testing-and-verifying-idempotency, duration: 2h -->
* Testing and verifying idempotency
    * unit tests for idempotent operations
    * fault-injection: duplicate requests, reordered requests
    * property-based testing of distributed APIs
    * `Jepsen`-style external verification
    * production verification: shadow comparisons, audits
<!-- chapter: incident-response-for-correctness-bugs, duration: 2h -->
* Incident response for correctness bugs
    * detecting silent duplication
    * reconciliation jobs and the audit ledger
    * recovering from a non-idempotent rollout
    * customer-facing communication on duplication incidents
    * post-incident hardening
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * end-to-end design walkthrough on a sample payments flow
    * group review of an idempotent `API` design
    * recommended reading and further study

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
