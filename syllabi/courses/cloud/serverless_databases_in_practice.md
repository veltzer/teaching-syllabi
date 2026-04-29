---
tags:
  - concepts:databases
  - concepts:serverless
  - concepts:cloud-economics
  - concepts:scalability
  - concepts:best-practices
level: intermediate
category: cloud
duration_hours: 16
audience:
  - audiences:senior-developers
  - audiences:data-engineers
  - audiences:devops
  - audiences:architects
---
<!-- course: serverless_databases_in_practice -->
# Serverless Databases in Practice

## Description
Serverless databases — `Aurora Serverless v2`, `DynamoDB`, `Neon`, `PlanetScale`, ```Cloud SQL`` with
serverless`, `Upstash `Redis``, ``Cloudflare` D1`, `Turso` — promise no-capacity-planning, pay-per-use,
scale-to-zero relational and key-value storage. The catalog has individual database courses
(`Postgres`, `MySQL`, `DynamoDB`) and a general `Serverless in Practice` course, but does not address
the specific engineering question: `when` does a serverless database `make` sense, and what changes `when`
you adopt one? The cost model, the cold-start behavior, the connection-management approach, and the
operational story all differ from a provisioned database, and several common application patterns
break against a serverless backend.

This two day course covers serverless databases as a focused engineering topic. It covers the
canonical offerings (the relational ones, the key-value ones, the new edge-database tier), the cost
shapes (request-priced, capacity-unit-priced, scaled-up-and-down-priced), the cold-start question,
the connection-management story (which is the headline gotcha for relational serverless), the
write-vs-read scaling, the multi-region story, the `IO`-cost subtlety, the patterns that work well
(spiky traffic, low-baseline workloads) and the patterns that do not (steady high-throughput, very
low-latency tail), and the migration story `when` the workload outgrows serverless. Examples cover
several real cost scenarios. Participants leave able to `make` the serverless-database decision
deliberately.

## Duration
16 hours / 2 days

## Intended Audience
* senior developers picking a database for a new service
* data engineers operating a small-to-medium data store
* `DevOps` evaluating the operational reduction
* architects designing for spiky workloads

## Prerequisites
* working experience with at least one relational or key-value database
* exposure to the Serverless in Practice course
* familiarity with at least one cloud provider
* basic understanding of database connection management

## Objectives
* explain what makes a database serverless
* compute the cost of a workload on at least three serverless options
* recognize the workloads where serverless is the right choice
* operate a serverless database in production
* solve the connection-management problem
* migrate to or from serverless deliberately
* avoid the patterns that `make` serverless expensive

## Outline
<!-- chapter: what-makes-a-database-serverless, duration: 1h -->
* What makes a database serverless
    * scale-to-zero or near-zero
    * pay-per-use pricing
    * no capacity provisioning
    * the operational reduction
    * cross-reference to the Serverless in Practice course
<!-- chapter: the-relational-serverless-tier, duration: 2h -->
* The relational serverless tier
    * `Aurora Serverless v2`
    * `Neon`
    * `PlanetScale` (`MySQL`)
    * `Cloud SQL` with auto-scaling
    * `Supabase`
    * the differences in the model
<!-- chapter: dynamodb-as-the-canonical-key-value-serverless, duration: 2h -->
* `DynamoDB` as the canonical key-value serverless
    * on-demand capacity
    * the per-request pricing
    * the read-and-write capacity units
    * cross-reference to the `DynamoDB` course
    * the "we hit a hot partition" reality
<!-- chapter: edge-databases, duration: 1h -->
* Edge databases
    * `Cloudflare D1` (`SQLite`)
    * `Turso` (`libSQL`)
    * `Upstash Redis`
    * the read-near-the-user proposition
    * the write-amplification reality
<!-- chapter: cost-shape-of-serverless-relational, duration: 2h -->
* Cost shape of serverless relational
    * the `ACU` (`Aurora Capacity Unit`) model
    * the per-`GB`-month storage
    * the `IO` cost in `Aurora`
    * `Neon`'s compute-and-storage split
    * the "the bill spiked because of `IO`" surprise
<!-- chapter: cost-shape-of-dynamodb, duration: 2h -->
* Cost shape of `DynamoDB`
    * on-demand vs provisioned
    * the global secondary index cost
    * the streams cost
    * the "we hit the per-second limit" failure
    * the cost crossover where provisioned wins
<!-- chapter: connection-management, duration: 2h -->
* Connection management
    * the relational connection problem revisited
    * `RDS Proxy` and `Aurora Serverless`
    * `Neon`'s `pgbouncer` integration
    * `PlanetScale`'s connection model
    * cross-reference to the Connection Pooling and Database Proxies course
    * the "we connected `Lambda` directly and melted it" failure
<!-- chapter: cold-start-and-warm-up, duration: 1h -->
* Cold start and warm-up
    * the `Aurora Serverless v2` warm-up
    * the `Neon` resume behavior
    * the first-request latency
    * the warm-keepalive strategy
    * the "scale-to-zero looked free until our latency was 2 seconds" reality
<!-- chapter: workloads-that-fit, duration: 1h -->
* Workloads that fit
    * spiky and bursty
    * low-baseline-with-occasional-peaks
    * dev/test environments
    * per-tenant databases at low scale
    * the "perfect serverless workload" profile
<!-- chapter: workloads-that-do-not-fit, duration: 1h -->
* Workloads that do not fit
    * steady high-throughput
    * sub-10ms tail latency requirement
    * very large datasets
    * complex analytical queries
    * the "we paid 5x what provisioned would have cost" reality
<!-- chapter: multi-region-serverless, duration: 1h -->
* Multi-region serverless
    * `DynamoDB Global Tables`
    * `Aurora Global Database`
    * `Neon` and `Turso` regional model
    * cross-reference to the Multi-Region Architecture course
    * the cost shape across regions

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
