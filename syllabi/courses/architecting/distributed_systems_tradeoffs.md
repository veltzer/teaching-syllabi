---
tags:
  - concepts:distributed-systems
  - concepts:architecture
  - concepts:eventual-consistency
  - concepts:acid
  - concepts:scalability
  - concepts:databases
level: advanced
category: architecture
duration_hours: 40
audience:
  - audiences:architects
  - audiences:senior-developers
  - audiences:developers
  - audiences:dbas
---
<!-- course: distributed_systems_tradeoffs -->
# Distributed Systems Tradeoffs

## Description
Most courses on distributed systems either teach algorithms (Paxos, Raft, gossip) or teach a specific stack
(`Kafka`, `Cassandra`, Spanner). This course is different. It is built around the tradeoffs that every distributed
system has to `make` and that every engineer who works on one needs to understand: consistency vs availability,
latency vs durability, throughput vs ordering, simplicity vs flexibility.

The course covers the `CAP` and `PACELC` theorems precisely, the spectrum of consistency models from linearizable
to eventually consistent, replication and partitioning trade-offs, the realities of clocks and ordering, the
practical impact of failure modes, and how these choices play out in real database and messaging systems
(`PostgreSQL`, `Cassandra`, `DynamoDB`, `CockroachDB`, Spanner, `Kafka`, `S3`, `etcd`). Participants leave able
to read a system's documentation and rapidly understand its tradeoff profile, and to design new systems with
the tradeoffs surfaced rather than buried.

## Duration
40 hours / 5 days

## Intended Audience
* architects designing distributed systems with non-trivial correctness requirements
* senior developers building on top of distributed databases and messaging systems
* `DBAs` choosing or operating distributed data stores
* engineers preparing for systems-design interviews

## Prerequisites
* `solid` backend development experience
* basic distributed systems concepts (replication, partitioning, consensus at a high level)
* working knowledge of at least one database and one message broker
* basic familiarity with `HTTP` and networking

## Objectives
* state the `CAP` and `PACELC` theorems precisely and apply them
* compare consistency models and choose the weakest sufficient one
* reason about replication strategies and their failure modes
* understand partitioning and rebalancing tradeoffs
* read a real system's docs and identify its tradeoff profile
* design systems with explicit, surfaced tradeoff decisions

## Outline
<!-- chapter: why-tradeoffs-not-algorithms, duration: 2h -->
* Why tradeoffs, not algorithms
    * what makes distributed systems hard
    * why "best practices" are usually contradictory
    * the architect's job: choosing tradeoffs
    * tradeoff vocabulary used throughout the course
    * the cost of pretending tradeoffs don't exist
<!-- chapter: cap-and-pacelc-precisely, duration: 3h -->
* `CAP` and `PACELC` precisely
    * what `CAP` actually says and what it does not
    * the misuse of `CAP` in marketing
    * `PACELC`: the latency-vs-consistency dimension
    * proof sketch and intuition
    * mapping real systems onto the `CAP`/`PACELC` axes
    * why "`CP`" and "`AP`" are oversimplifications
<!-- chapter: consistency-models-the-spectrum, duration: 4h -->
* Consistency models: the spectrum
    * linearizability
    * sequential consistency
    * causal consistency
    * `PRAM` and read-your-writes
    * eventual consistency
    * monotonic reads and monotonic writes
    * snapshot isolation in distributed databases
    * what "strong consistency" usually means in marketing
<!-- chapter: replication-strategies, duration: 3h -->
* Replication strategies
    * single-leader replication
    * multi-leader replication and conflict resolution
    * leaderless replication and quorum reads/writes
    * synchronous, asynchronous, semi-synchronous
    * chain replication
    * the failure mode each strategy actually has
<!-- chapter: partitioning-and-rebalancing, duration: 3h -->
* Partitioning and rebalancing
    * range partitioning, hash partitioning, directory partitioning
    * consistent hashing
    * hot partitions and skew
    * resharding without downtime
    * rebalancing during failure
    * the operational cost of getting this wrong
<!-- chapter: clocks-time-and-ordering, duration: 3h -->
* Clocks, time and ordering
    * physical clocks and their drift
    * Lamport timestamps and vector clocks
    * `HLC` (`hybrid logical clock`)
    * Spanner's `TrueTime` model
    * causal ordering vs total ordering
    * the role of clocks in consensus
<!-- chapter: consensus-paxos-raft-and-zab, duration: 3h -->
* Consensus: `Paxos`, Raft and `ZAB`
    * the consensus problem precisely stated
    * `Paxos` at a high level
    * `Raft` and the focus on understandability
    * `ZAB` and `ZooKeeper`
    * leader election and log replication
    * what consensus does and does not give you
<!-- chapter: failure-models-and-detection, duration: 2h -->
* Failure models and detection
    * crash, omission, byzantine
    * the impossibility of perfect failure detection
    * timeouts and accusation
    * fencing tokens and avoiding split brain
    * partial failure: the real enemy
<!-- chapter: distributed-transactions, duration: 3h -->
* Distributed transactions
    * what makes a transaction "distributed"
    * two-phase commit and its failure modes
    * three-phase commit and why it is rarely used
    * `Percolator` and Spanner transactions
    * `Calvin` and deterministic transactions
    * the realistic alternative: idempotency and sagas
<!-- chapter: cap-in-real-databases, duration: 3h -->
* `CAP` in real databases
    * `PostgreSQL` replication: what it really gives you
    * `Cassandra` and tunable consistency
    * `DynamoDB` and the consistency modes
    * `CockroachDB` and `TiDB` claims
    * Spanner and `TrueTime`'s tradeoff
    * `MongoDB`'s evolution of consistency guarantees
    * the "global, strongly-consistent" claim and what it costs
<!-- chapter: messaging-and-streaming-tradeoffs, duration: 3h -->
* Messaging and streaming tradeoffs
    * at-most-once, at-least-once, effectively-exactly-once
    * ordering guarantees per partition vs across partitions
    * `Kafka`, Pulsar, `Kinesis` consistency profiles
    * the "stream as a database" tradeoff
    * end-to-end latency vs durability vs ordering
<!-- chapter: storage-systems-tradeoffs, duration: 2h -->
* Storage systems tradeoffs
    * `S3`-style object stores: strong read-after-write but no transactions
    * distributed file systems: `HDFS`, Ceph, `GlusterFS`
    * the durability-vs-cost frontier
    * eventual consistency in metadata services
    * the limits of "11 nines"
<!-- chapter: making-tradeoffs-visible-in-architecture, duration: 2h -->
* Making tradeoffs visible in architecture
    * the explicit tradeoff section in design docs
    * tradeoff matrices for stakeholder review
    * non-functional requirements as tradeoff statements
    * how to argue with "we want both" demands
    * recording rejected alternatives
<!-- chapter: case-studies, duration: 3h -->
* Case studies
    * `Amazon` `S3` and `Dynamo` papers re-examined
    * `Google` Spanner paper re-examined
    * `Cassandra` and `DynamoDB` head-to-head
    * a real production failure traced to a misunderstood tradeoff
    * design walkthrough on a sample distributed counter
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * tradeoff analysis exercise on a sample system design
    * recommended reading: `Kleppmann`, Brewer, Abadi, `Bailis`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
