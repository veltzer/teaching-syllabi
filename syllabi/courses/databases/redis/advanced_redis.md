---
tags:
  - tools:redis
  - databases:nosql
  - data-and-ai:databases
  - data-and-ai:caching
level: advanced
category: database
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
  - audiences:architects
---
<!-- course: advanced_redis -->
# Advanced `Redis`

## Description
This advanced course dives deep into `Redis` features and operational patterns for engineers who already have foundational `Redis` knowledge. Participants will master `Redis` clustering, `Redis Streams` for event-driven architectures, `Lua` scripting for atomic operations, and advanced pub/sub patterns. The course also covers persistence strategies, `Redis Sentinel` for high availability, custom modules, memory optimization techniques, and security hardening for production deployments.

## Duration
16 hours / 2 days

## Intended Audience
* Experienced developers working with `Redis` in production
* Backend engineers building high-performance distributed systems
* `DevOps` engineers managing `Redis` infrastructure
* Software architects designing caching and messaging systems

## Prerequisites
* Working experience with `Redis` data structures and basic commands
* Understanding of distributed systems concepts
* Familiarity with `Linux` system administration
* Experience with at least one programming language (`Python`, `Java`, or `Node.js`)

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `Linux` Fundamentals (or equivalent experience)
* `Node.js` Backend Development (or equivalent experience)

## Objectives
* Design and manage `Redis` clusters for horizontal scalability
* Implement event-driven architectures using `Redis Streams`
* Write `Lua` scripts for complex atomic operations
* Build robust pub/sub messaging patterns
* Select and configure appropriate persistence strategies
* Deploy `Redis Sentinel` for high availability
* Extend `Redis` functionality with modules
* Optimize memory usage and apply security best practices

## Outline
<!-- chapter: redis-clustering, duration: 2h -->
* `Redis` Clustering
    * Cluster architecture and hash slots
    * Cluster setup and configuration
    * Data sharding and distribution
    * Adding and removing nodes
    * Cluster resharding
    * Handling failover scenarios
    * Client-side cluster support
    * Cross-slot operations and limitations
    * Cluster monitoring and diagnostics

<!-- chapter: redis-streams, duration: 2h -->
* `Redis Streams`
    * Stream data structure internals
    * Producing messages with XADD
    * Consuming messages with XREAD
    * Consumer groups and acknowledgments
    * XREADGROUP and XACK patterns
    * Stream trimming and retention
    * Pending entries list management
    * Claiming and recovering messages
    * `Event sourcing` patterns with Streams

<!-- chapter: lua-scripting, duration: 2h -->
* `Lua` Scripting
    * `Lua` language basics for `Redis`
    * EVAL and EVALSHA commands
    * Accessing keys and arguments
    * Atomic operations with scripts
    * Script caching and management
    * Debugging `Lua` scripts
    * Common scripting patterns
    * Performance considerations
    * `Redis` Functions (v7+)

<!-- chapter: pub-sub-patterns, duration: 1h -->
* Pub/Sub Patterns
    * Pub/sub architecture in `Redis`
    * Channel-based pub/sub
    * Pattern-based subscriptions
    * Pub/sub vs Streams comparison
    * Reliable messaging patterns
    * Fan-out and fan-in architectures
    * Scaling pub/sub across clusters
    * Sharded pub/sub in `Redis` 7

<!-- chapter: persistence-strategies, duration: 1h -->
* Persistence Strategies
    * RDB snapshots: configuration and trade-offs
    * AOF append-only file: modes and rewriting
    * Hybrid persistence (RDB + AOF)
    * Persistence performance impact
    * Backup and restore procedures
    * Disaster recovery planning
    * Choosing the right persistence strategy

<!-- chapter: redis-sentinel, duration: 2h -->
* `Redis Sentinel`
    * Sentinel architecture and quorum
    * Configuring Sentinel nodes
    * Automatic failover mechanism
    * Sentinel monitoring capabilities
    * Client integration with Sentinel
    * Sentinel vs Cluster comparison
    * Operational best practices
    * Troubleshooting Sentinel issues

<!-- chapter: redis-modules, duration: 2h -->
* `Redis` Modules
    * Module architecture and `API`
    * RedisJSON for document storage
    * RediSearch for full-text search
    * RedisTimeSeries for time series data
    * RedisBloom for probabilistic data structures
    * RedisGraph overview
    * Loading and managing modules
    * Module selection guidelines

<!-- chapter: memory-optimization, duration: 2h -->
* Memory Optimization
    * `Redis` memory model and overhead
    * Memory-efficient data structures
    * Object encoding and optimization
    * Key expiration strategies
    * Eviction policies and configuration
    * Memory fragmentation analysis
    * MEMORY command usage
    * Large key detection and remediation
    * Compression techniques

<!-- chapter: security, duration: 2h -->
* Security
    * Authentication with `ACLs`
    * User and permission management
    * `TLS`/`SSL` encryption
    * Network security and binding
    * Command renaming and disabling
    * Protected mode configuration
    * Security auditing
    * Securing `Redis` in production environments

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
