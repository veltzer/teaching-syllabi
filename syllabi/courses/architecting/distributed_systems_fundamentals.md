---
tags:
  - concepts:distributed-systems
  - concepts:architecture
  - concepts:scalability
  - concepts:algorithms
level: advanced
category: architecture
duration_hours: 24
audience:
  - audiences:architects
  - audiences:developers
---
<!-- course: distributed_systems_fundamentals -->
# Distributed Systems Fundamentals

## Description
This course provides a comprehensive foundation in the theory and practice of distributed systems.
Participants will study the fundamental theorems, consistency models, and consensus algorithms that
underpin modern distributed architectures. The course covers distributed clocks, conflict-free
replicated data types, leader election, partitioning strategies, replication techniques, and the
various failure modes that distributed systems must handle. This knowledge is essential for
architects and developers building reliable, scalable distributed applications.

## Duration
24 hours / 3 days

## Intended Audience
* software architects designing distributed systems
* senior developers building scalable applications
* engineers working on infrastructure and platform services

## Prerequisites
* strong programming background in at least one language
* familiarity with networking fundamentals
* basic understanding of databases and data structures

## Objectives
* understand the CAP theorem and its implications for system design
* compare and apply different consistency models
* explain and reason about consensus algorithms such as Raft and Paxos
* work with distributed clocks and ordering of events
* apply CRDTs for conflict-free data replication
* design systems with appropriate partitioning and replication strategies
* identify and mitigate common failure modes in distributed systems

## Outline
<!-- chapter: introduction-to-distributed-systems, duration: 2h -->
* introduction to distributed systems
    * what makes a system distributed
    * motivations for distribution (scalability, availability, fault tolerance)
    * challenges and fallacies of distributed computing
    * the eight fallacies of distributed computing
<!-- chapter: cap-theorem, duration: 2h -->
* CAP theorem
    * consistency, availability, and partition tolerance
    * CAP theorem proof and implications
    * PACELC theorem as an extension of CAP
    * making trade-offs in real-world systems
<!-- chapter: consistency-models, duration: 2h -->
* consistency models
    * strong consistency
    * eventual consistency
    * causal consistency
    * linearizability and sequential consistency
    * read-your-writes and session guarantees
    * tunable consistency in distributed databases
<!-- chapter: consensus-algorithms, duration: 5h -->
* consensus algorithms
    * the consensus problem
    * Paxos algorithm
        * basic Paxos
        * multi-Paxos
        * limitations and practical considerations
    * Raft algorithm
        * leader election in Raft
        * log replication
        * safety guarantees
        * membership changes
    * Byzantine fault tolerance
    * practical applications of consensus (etcd, `ZooKeeper`)
<!-- chapter: distributed-clocks, duration: 2h -->
* distributed clocks
    * the problem of time in distributed systems
    * physical clocks and clock synchronization (NTP)
    * Lamport logical clocks
    * vector clocks
    * hybrid logical clocks
    * ordering of events and causality
<!-- chapter: crdts-conflict-free-replicated-data-types, duration: 2h -->
* CRDTs (Conflict-free Replicated Data Types)
    * state-based CRDTs (CvRDTs)
    * operation-based CRDTs (CmRDTs)
    * common CRDT types (counters, sets, registers, sequences)
    * applications of CRDTs in real-world systems
    * trade-offs and limitations of CRDTs
<!-- chapter: leader-election, duration: 2h -->
* leader election
    * the need for leader election
    * bully algorithm
    * ring-based election
    * leader election with `ZooKeeper` and etcd
    * lease-based leadership
    * split-brain scenarios and fencing
<!-- chapter: partitioning, duration: 2h -->
* partitioning
    * horizontal vs vertical partitioning
    * hash-based partitioning
    * range-based partitioning
    * consistent hashing
    * partition rebalancing strategies
    * cross-partition queries and scatter-gather
<!-- chapter: replication, duration: 2h -->
* replication
    * single-leader replication
    * multi-leader replication
    * leaderless replication
    * synchronous vs asynchronous replication
    * quorum reads and writes
    * replication lag and its consequences
<!-- chapter: failure-modes, duration: 3h -->
* failure modes
    * crash failures vs Byzantine failures
    * network partitions
    * partial failures and gray failures
    * cascading failures
    * failure detection (heartbeats, phi accrual detector)
    * circuit breaker pattern
    * bulkhead pattern
    * designing for failure (chaos engineering principles)

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
