---
tags:
  - tools:redis
  - data-and-ai:nosql
  - data-and-ai:caching
  - concepts:data-structures
level: intermediate
category: database
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: redis_for_developers -->
# `Redis`: In-Memory Data Structure Store

## Description
This course provides an introduction to `Redis`, an open-source, in-memory data structure store, used as a database, cache, and message broker. We cover fundamental concepts, data structures, advanced features, and practical applications of `Redis`. Students gain experience through labs and projects, enabling them to utilize `Redis` in various real-world scenarios.

## Duration
24 hours / 3 days

## Intended Audience
* software developers working with databases
* backend engineers and data engineers

## Prerequisites
* Basic understanding of data structures and algorithms.
* Familiarity with command-line interfaces.
* Basic programming knowledge (`Python`, `JavaScript`, or any other scripting language).

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)

## Objectives
* Understand the core concepts of `Redis` and its architecture.
* Work with various `Redis` data structures (strings, lists, sets, sorted sets, hashes).
* Implement caching strategies using `Redis`.
* Utilize `Redis` for pub/sub messaging.
* Configure and manage `Redis` instances.
* Apply advanced `Redis` features such as transactions, scripting, and persistence.
* Integrate `Redis` with applications using different programming languages.
* Understand `Redis` cluster and scalability.

## Outline
<!-- chapter: introduction-to-redis, duration: 2h -->
* Introduction to `Redis`:
    * Overview of `NoSQL` and `Redis`.
    * Installation and basic commands.
    * `Redis` data types introduction.
<!-- chapter: redis-data-structures, duration: 7h -->
* `Redis` Data Structures:
    * Strings:
        * String operations: SET, GET, APPEND, etc.
    * Lists:
        * List operations: LPUSH, RPUSH, LPOP, RPOP, etc.
    * Sets:
        * Set operations: SADD, SREM, SINTER, SUNION, etc.
    * Sorted Sets:
        * Sorted set operations: ZADD, ZRANGE, ZRANK, etc.
    * Hashes:
        * Hash operations: HSET, HGET, HGETALL, etc.
    * Use cases for each data structure.
<!-- chapter: caching-with-redis, duration: 2h -->
* Caching with `Redis`:
    * Caching strategies.
    * Implementing caching in applications.
    * Time-to-live (`TTL`) and eviction policies.
<!-- chapter: pub-sub-messaging, duration: 2h -->
* Pub/Sub Messaging:
    * Publish/subscribe model.
    * Implementing pub/sub with `Redis`.
    * Use cases for pub/sub.
<!-- chapter: redis-transactions-and-scripting, duration: 2h -->
* `Redis` Transactions and Scripting:
    * Transactions: MULTI, EXEC, DISCARD, WATCH.
    * Lua scripting in `Redis`.
    * Atomic operations.
<!-- chapter: redis-persistence, duration: 2h -->
* `Redis` Persistence:
    * RDB and AOF persistence.
    * Configuration and tuning.
    * Data recovery.
<!-- chapter: redis-configuration-and-management, duration: 2h -->
* `Redis` Configuration and Management:
    * Configuration parameters.
    * Monitoring and logging.
    * Security considerations.
<!-- chapter: redis-cluster, duration: 2h -->
* `Redis` Cluster:
    * `Redis` Cluster architecture.
    * Sharding and replication.
    * Cluster management.
<!-- chapter: integrating-redis-with-applications, duration: 3h -->
* Integrating `Redis` with Applications:
    * `Redis` clients (`Python`, `JavaScript`, etc.).
    * Connecting `Redis` to web applications.

## Textbooks and Resources
* `Redis` Documentation: [`https`://`Redis`.io/docs/](`https`://`Redis`.io/docs/)
* "`Redis` in Action" by Josiah Carlson (Optional)
* Various online tutorials and articles.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
