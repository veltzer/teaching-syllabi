---
tags:
  - concepts:databases
  - concepts:scalability
  - concepts:distributed-systems
  - concepts:best-practices
level: advanced
category: database
duration_hours: 24
audience:
  - audiences:dbas
  - audiences:senior-developers
  - audiences:architects
  - audiences:data-engineers
---
<!-- course: sharding_strategies -->
# Sharding Strategies

## Description
At some scale every database has to be sharded. The catalog covers `Database Design`, `Database
Internals`, `Database Migration Strategies`, `Query Optimization and Indexing`, and several
distributed-database courses (`CockroachDB`, `Cassandra`, `ScyllaDB`, `DynamoDB`). It does not have a
focused course on the engineering decision of how to shard a database that is currently single-node.
That decision — what to shard on, how to route queries, how to rebalance, how to migrate — has more
operational consequence than almost any other decision a system makes.

This three day course covers sharding as its own engineering discipline. It covers when to shard (and
when to absolutely not), the choice of shard key, the routing layer, hash sharding vs range sharding
vs directory sharding, the cross-shard query problem, the rebalancing problem, the resharding problem
(adding or removing shards), the failover within a shard, the relationship to read replicas, the
operational tooling, and the patterns that `make` sharding succeed or fail. Examples include `Vitess` for
`MySQL`, Citus for Postgres, `MongoDB`'s sharding, Discord's migration to scylla, `Figma`'s
horizontal `Postgres` sharding, and Pinterest's `MySQL` sharding history. Participants leave able to
`make` the sharding decision deliberately and avoid the migrations that have killed organizations.

## Duration
24 hours / 3 days

## Intended Audience
* `DBAs` and senior developers facing a single-node ceiling
* architects designing a system from scratch that will need sharding
* data engineers operating large transactional databases
* engineers who have inherited a sharded system

## Prerequisites
* `solid` relational database knowledge
* exposure to the Database Internals course
* familiarity with at least one of `Postgres`, `MySQL`, `MongoDB`
* basic distributed systems background

## Objectives
* decide whether sharding is justified
* pick a shard key correctly
* design the routing layer
* operate cross-shard queries with eyes open
* execute a resharding migration
* recognize the patterns that doom sharding projects
* compare horizontal sharding to alternatives

## Outline
<!-- chapter: when-to-shard-and-when-not-to, duration: 2h -->
* `When` to shard and when not to
    * the "we are at the single-node ceiling" sign
    * the alternatives: read replicas, vertical scaling, archiving
    * the "we sharded too early" failure
    * the "we sharded too late" failure
    * the staged path to a sharded system
<!-- chapter: choosing-a-shard-key, duration: 3h -->
* Choosing a shard key
    * the cardinality requirement
    * the access-pattern requirement
    * the no-cross-shard-join goal
    * the customer-`id`, user-id, tenant-`id` pattern
    * the "we picked the wrong key and resharded twice" disaster
    * worked example: e-commerce, social, `SaaS`
<!-- chapter: hash-vs-range-vs-directory, duration: 2h -->
* Hash vs range vs directory
    * hash sharding: even distribution
    * range sharding: ordered queries
    * directory sharding: explicit map
    * consistent hashing
    * the trade-offs of each
<!-- chapter: the-routing-layer, duration: 2h -->
* The routing layer
    * library-level routing
    * proxy-level routing
    * `Vitess` `vtgate`
    * the "we hard-coded the routing in `200` places" failure
    * routing as a single point of failure
<!-- chapter: cross-shard-queries, duration: 2h -->
* Cross-shard queries
    * the scatter-gather pattern
    * the cost of scatter-gather
    * the application-side join
    * the analytics warehouse outside the shards
    * the "every query became a scatter-gather" failure
<!-- chapter: cross-shard-transactions, duration: 2h -->
* Cross-shard transactions
    * the no-distributed-transactions rule
    * the `saga` as the alternative
    * cross-reference to the `Saga Pattern` course
    * the two-phase-commit option and its costs
    * worked example
<!-- chapter: rebalancing, duration: 2h -->
* Rebalancing
    * the hot shard problem
    * the rebalancing primitive
    * the impact on writes
    * the impact on the routing layer
    * the "rebalancing took six weeks and we were unavailable" failure
<!-- chapter: resharding, duration: 3h -->
* Resharding
    * the add-shards operation
    * the change-shard-key operation (almost always a rewrite)
    * the data-movement strategy
    * the dual-write phase
    * the cutover
    * cross-reference to the Database Migration Strategies course
<!-- chapter: per-shard-failover-and-replication, duration: 2h -->
* Per-shard failover and replication
    * each shard has its own primary and replicas
    * per-shard high availability
    * the "we had high availability per shard, but not across" subtlety
    * the cross-region question for sharded systems
    * cross-reference to the Multi-Region Architecture course
<!-- chapter: vitess-deep-dive, duration: 1h -->
* `Vitess` deep dive
    * `Vitess` architecture
    * `vtgate`, vttablet, `vtctld`
    * `MySQL`-compatible sharding
    * `YouTube`'s history with `Vitess`
    * when `Vitess` is the right answer
<!-- chapter: citus-deep-dive, duration: 1h -->
* `Citus` deep dive
    * `Citus` architecture
    * `Postgres`-compatible sharding
    * coordinator and worker model
    * the `Microsoft Azure` adoption
    * when `Citus` is the right answer
<!-- chapter: case-studies, duration: 2h -->
* Case studies
    * `Pinterest`'s `MySQL` sharding history
    * `Figma`'s horizontal `Postgres` sharding
    * `Discord`'s migration to `Cassandra`/`ScyllaDB`
    * `Notion`'s `Postgres` sharding
    * what each got right and what they got wrong

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
