---
tags:
  - concepts:architecture
  - concepts:scalability
  - security:security
  - networking:networking
  - data-and-ai:databases
level: advanced
category: architecture
duration_hours: 40
audience:
  - audiences:architects
  - audiences:developers
---
<!-- course: large_scale_architecting -->
# Large Scale Architecture

## Description
Large scale architectures is the study of the tools and methodologies that are commonly used to solve large scale problems in large scale computer systems. These problems include: data sharing between parts of an organization, durability of data, security at large scale, data bases at large scale, computer networks at large scale, and more.

## Duration
40 hours / 5 days

## Intended Audience
Architects and senior developers responsible for designing and maintaining large scale systems.

## Prerequisites
* Several years of software development experience
* Basic understanding of distributed systems, networking, and databases

## Objectives
* Understand the pillars of well-architected systems including security, reliability, and performance
* Evaluate architectural trade-offs in large scale environments
* Apply best practices for operational excellence and cost optimization
* Design systems that meet sustainability and scalability requirements

## Exercises
* This is a theoretical course, it does not include exercises.

## Outline
<!-- chapter: pillars-of-well-architected-systems, duration: 3h -->
* pillars of well-architected systems
    * operational excellence
    * security
    * reliability
    * performance efficiency
    * cost optimization
    * sustainability
    * applying the pillars as a design lens
<!-- chapter: scalability-fundamentals, duration: 3h -->
* scalability fundamentals
    * what scalability means and what it does not
    * vertical scaling vs horizontal scaling
    * stateless vs stateful services
    * shared-nothing architectures
    * scalability bottlenecks and how to identify them
    * Amdahl's law and its practical implications
    * Little's law and system throughput
<!-- chapter: distributed-systems-theory-for-architects, duration: 3h -->
* distributed systems theory for architects
    * the fallacies of distributed computing
    * CAP theorem and real-world trade-offs
    * PACELC theorem
    * consistency models: strong, eventual, causal
    * the two generals problem and its relevance
    * failure modes in distributed systems
    * Byzantine faults and `when` they matter
<!-- chapter: high-availability-and-fault-tolerance, duration: 3h -->
* high availability and fault tolerance
    * SLA, SLO, and SLI definitions and targets
    * redundancy strategies (active-active, active-passive)
    * failure domains and blast `radius` control
    * graceful degradation and partial availability
    * bulkhead and circuit breaker patterns
    * chaos engineering principles
    * designing for the five nines
<!-- chapter: data-architecture-at-scale, duration: 4h -->
* data architecture at scale
    * relational databases under load: read replicas and sharding
    * `NoSQL` families: document, key-value, column-family, graph
    * choosing between `SQL` and `NoSQL`
    * database partitioning strategies
    * consistent hashing for data distribution
    * multi-region data replication
    * hot spots, skew, and rebalancing
    * polyglot persistence patterns
<!-- chapter: caching-at-scale, duration: 2h -->
* caching at scale
    * cache topologies: local, distributed, hierarchical
    * cache-aside, read-through, write-through, write-behind
    * cache invalidation strategies
    * thundering herd and cache stampede mitigation
    * CDN caching and edge computing
    * cost and consistency trade-offs in caching
<!-- chapter: messaging-and-event-streaming, duration: 3h -->
* messaging and event streaming
    * message queues vs event streams vs pub/sub
    * at-least-once, at-most-once, and exactly-once delivery
    * ordering guarantees and partitioned logs
    * back-pressure and consumer lag management
    * `Kafka` architecture for large-scale event streaming
    * event-driven architectures and choreography
    * `saga` pattern for distributed transactions
<!-- chapter: service-decomposition-and-boundaries, duration: 3h -->
* service decomposition and boundaries
    * `domain-driven design` at scale
    * bounded contexts and context mapping
    * defining service contracts and interfaces
    * `API` versioning and backward compatibility
    * service mesh for inter-service communication
    * sidecar proxy and service discovery patterns
    * coupling metrics and cohesion analysis
<!-- chapter: networking-at-scale, duration: 2h -->
* networking at scale
    * load balancing: layer 4 vs layer 7
    * global server load balancing and GeoDNS
    * anycast routing
    * software-defined networking fundamentals
    * network latency and bandwidth optimization
    * `TCP` tuning for high-throughput systems
    * network security zones and micro-segmentation
<!-- chapter: security-at-scale, duration: 3h -->
* security at scale
    * zero-trust architecture principles
    * identity and access management at scale (`IAM`)
    * secrets management: vaults, rotation, least privilege
    * encryption in transit and at `rest`
    * `DDoS` mitigation strategies
    * supply chain security
    * threat modeling for large systems
    * compliance at scale: `GDPR`, SOC2, `PCI`-DSS considerations
<!-- chapter: observability-and-operational-excellence, duration: 3h -->
* observability and operational excellence
    * the three pillars: metrics, logs, and traces
    * distributed tracing and correlation `IDs`
    * structured logging at scale
    * alerting strategies and on-call culture
    * SLO-based alerting and error budgets
    * capacity planning and demand forecasting
    * runbooks and operational playbooks
    * post-incident reviews and blameless culture
<!-- chapter: cost-optimization-at-scale, duration: 2h -->
* cost optimization at scale
    * understanding cost drivers in large systems
    * right-sizing compute and storage
    * spot and preemptible instance strategies
    * data transfer costs and egress optimization
    * cost attribution and chargeback models
    * efficiency metrics: cost per request, cost per transaction
    * FinOps culture and practices
<!-- chapter: multi-region-and-global-architectures, duration: 3h -->
* multi-region and global architectures
    * region and availability zone design
    * active-active vs active-passive multi-region
    * data sovereignty and residency requirements
    * global traffic management
    * cross-region replication lag and conflict resolution
    * disaster recovery strategies: RTO and RPO
    * geo-distributed databases
<!-- chapter: platform-and-infrastructure-as-product, duration: 3h -->
* platform and infrastructure as product
    * internal developer platforms
    * golden paths and paved roads
    * self-service infrastructure provisioning
    * infrastructure as code at scale
    * configuration management for large fleets
    * immutable infrastructure patterns
    * progressive delivery: canary releases, feature flags

## References
* [The 6 Pillars of the `AWS` Well-Architected Framework](`https`://`aws`.amazon.com/blogs/apn/the-6-pillars-of-the-`aws`-well-architected-framework)

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
