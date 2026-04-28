---
tags:
  - concepts:architecture
  - concepts:domain-driven-design
  - concepts:distributed-systems
  - concepts:eventual-consistency
  - concepts:design-patterns
  - concepts:persistence
level: advanced
category: architecture
duration_hours: 40
audience:
  - audiences:architects
  - audiences:senior-developers
  - audiences:developers
---
<!-- course: event_sourcing_in_practice -->
# `Event Sourcing` In Practice

## Description
`Event sourcing` is one of those architectural choices that looks simple on the whiteboard and reveals all of
its complexity in production. Storing every state change as an immutable event gives you a perfect audit log,
deterministic replay, free history, and a beautifully decoupled read side; it also gives you event versioning,
projection management, snapshotting, schema evolution and a much harder operational story than people expect.

This five day course is dedicated entirely to `event sourcing` as an engineering discipline. The existing
`CQRS` and `Event Sourcing` course bundles two big topics together; this course focuses on `ES` end to end:
aggregate design, event modeling, write-side consistency, projection design, snapshotting, event versioning
and migration, the operational story (replay, repair, recovery), and the patterns that `make` event-sourced
systems maintainable over years. Examples are drawn from `EventStoreDB`, `Kurrent`, `Axon`, `Marten` and
custom-on-`Postgres`/`Kafka` implementations.

## Duration
40 hours / 5 days

## Intended Audience
* architects designing or evaluating event-sourced systems
* senior developers building or maintaining event-sourced applications
* engineers migrating an existing system to `event sourcing`
* engineers who have shipped one event-sourced system and want to do the next one better

## Prerequisites
* `solid` backend development experience
* working knowledge of at least one database and at least one message broker
* basic familiarity with `domain-driven design`
* exposure to event-driven architectures is helpful

## Objectives
* describe `event sourcing` precisely and distinguish it from related patterns
* design aggregates, commands and events for an event-sourced domain
* implement and operate the write side with proper consistency guarantees
* design projections that keep up with the event stream
* version events and migrate event schemas over years
* operate event-sourced systems including replay, repair and recovery
* recognize `when` `event sourcing` is and is not the right choice

## Outline
<!-- chapter: what-event-sourcing-actually-is, duration: 2h -->
* What `event sourcing` actually is
    * events as the source of truth, state as derived
    * `event sourcing` vs `event-driven architecture` vs event notification
    * `event sourcing` vs change-data-capture
    * the relationship to `CQRS` and to `domain-driven design`
    * why people overuse and under-use `event sourcing`
    * what `event sourcing` is and is not good for
<!-- chapter: events-and-the-event-log, duration: 3h -->
* Events and the event log
    * the immutable append-only log
    * event identity and ordering
    * stream-per-aggregate vs stream-per-category vs single global stream
    * event metadata: causation, correlation, user, timestamp
    * the event store as a persistence boundary
    * event-store implementations: `EventStoreDB`, `Kurrent`, `Marten`, `Axon Server`, custom
<!-- chapter: aggregate-design-for-event-sourcing, duration: 4h -->
* Aggregate design for `event sourcing`
    * the aggregate as a consistency boundary
    * commands as inputs, events as outputs
    * the aggregate's job: validate and emit
    * sizing aggregates for an event-sourced system
    * referential integrity across aggregates
    * the "aggregates that touch each other" anti-pattern
    * cross-reference to the Event Storming course
<!-- chapter: command-side-consistency, duration: 3h -->
* Command-side consistency
    * loading an aggregate by replay
    * optimistic concurrency on the stream
    * conflict resolution under concurrent commands
    * idempotent command handling
    * cross-reference to the Idempotency course
    * write-throughput limits per stream
<!-- chapter: snapshots-and-replay-performance, duration: 3h -->
* Snapshots and replay performance
    * the load-time problem at high event counts
    * snapshot strategy: every N events, every M seconds, on demand
    * snapshot storage and versioning
    * snapshot invalidation `when` aggregates change shape
    * snapshot rebuild and warm-up
    * choosing not to snapshot
<!-- chapter: projections-and-the-read-side, duration: 4h -->
* Projections and the read side
    * the projection as a derived view
    * pull-based and push-based projection updates
    * single-stream projections vs multi-stream projections
    * idempotent projection updates
    * choosing the storage for a projection
    * read-your-writes and the staleness window
    * multiple projections per stream
    * the failure of "the projection is the database"
<!-- chapter: projection-management, duration: 3h -->
* Projection management
    * deploying a new projection from a populated event store
    * rebuilding a projection without taking the system down
    * versioning projections
    * the "swap projection version" pattern
    * projection lag monitoring
    * recovering from a corrupted projection
<!-- chapter: event-schema-evolution, duration: 4h -->
* Event schema evolution
    * adding fields to events
    * deprecating events and the long tail
    * upcasters: in-event, in-handler, in-pipeline
    * the "events are forever" rule
    * weak schema vs strict schema
    * migrating event types over years
    * cross-reference to the `API` Evolution course
<!-- chapter: event-versioning-strategies, duration: 2h -->
* Event versioning strategies
    * versioned event names
    * versioned schemas with one event name
    * lazy upcasting on read
    * eager upcasting via stream rewrite (rarely)
    * compatibility levels for events
    * communicating event versions across services
<!-- chapter: integration-and-cross-bounded-context-events, duration: 2h -->
* Integration and cross-bounded-context events
    * domain events vs integration events
    * the outbox pattern as the bridge
    * cross-reference to the Idempotency course's outbox chapter
    * event translation at context boundaries
    * the consumer-driven event contract
<!-- chapter: testing-event-sourced-systems, duration: 2h -->
* Testing event-sourced systems
    * given/`when`/then over events and commands
    * pure aggregate tests without `IO`
    * projection tests with controlled event streams
    * end-to-end tests against the event store
    * property-based testing of aggregates
    * snapshot/golden-master testing for projections
<!-- chapter: operational-story-replay-and-repair, duration: 3h -->
* Operational story: replay and repair
    * deterministic replay as a feature
    * replaying with side effects: how to avoid double-spending
    * fixing a bug in an aggregate retroactively
    * compensating events vs editing events (almost never)
    * cleanup events and forgetting (`GDPR`)
    * the audit story `when` you cannot edit history
<!-- chapter: gdpr-and-personal-data, duration: 2h -->
* `GDPR` and personal data
    * the immutable log vs the right to erasure
    * crypto-shredding pattern
    * tombstone events for soft erasure
    * personal-data segregation streams
    * legal review and the architecture decision
<!-- chapter: scaling-event-sourcing, duration: 2h -->
* Scaling `event sourcing`
    * partitioning by stream
    * sharding aggregates across nodes
    * event-store replication
    * geographic distribution
    * the cost of cross-stream queries on the write side
<!-- chapter: when-event-sourcing-is-wrong-and-case-studies, duration: 1h -->
* `When` `event sourcing` is wrong, and case studies
    * `CRUD` apps that pretend to need history
    * write-throughput-bound workloads
    * domains where state matters more than transitions
    * teams without the operational maturity for it
    * the "we used `CQRS` and `ES` because it was cool" anti-pattern
    * walkthrough of an event-sourced billing domain
    * lessons learned from a multi-year event-sourced system
    * recommended reading: `Vernon`, `Young`, `Fowler`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
