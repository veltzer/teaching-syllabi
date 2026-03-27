---
tags:
  - tools:redis
  - data-and-ai:nosql
  - data-and-ai:caching
  - concepts:data-structures
level: intermediate
category: database
duration_days: 3
audience:
  - audiences:developers
---
# `Redis`: In-Memory Data Structure Store

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

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
* Introduction to `Redis`:
    * Overview of `NoSQL` and `Redis`.
    * Installation and basic commands.
    * `Redis` data types introduction.
* `Redis` Data Structures:
    * Strings:
        * String operations: `SET`, `GET`, `APPEND`, etc.
    * Lists:
        * List operations: `LPUSH`, `RPUSH`, `LPOP`, `RPOP`, etc.
    * Sets:
        * Set operations: `SADD`, `SREM`, `SINTER`, `SUNION`, etc.
    * Sorted Sets:
        * Sorted set operations: `ZADD`, `ZRANGE`, `ZRANK`, etc.
    * Hashes:
        * Hash operations: `HSET`, `HGET`, `HGETALL`, etc.
    * Use cases for each data structure.
* Caching with `Redis`:
    * Caching strategies.
    * Implementing caching in applications.
    * Time-to-live (TTL) and eviction policies.
* Pub/Sub Messaging:
    * Publish/subscribe model.
    * Implementing pub/sub with `Redis`.
    * Use cases for pub/sub.
* `Redis` Transactions and Scripting:
    * Transactions: `MULTI`, `EXEC`, `DISCARD`, `WATCH`.
    * Lua scripting in `Redis`.
    * Atomic operations.
* `Redis` Persistence:
    * `RDB` and `AOF` persistence.
    * Configuration and tuning.
    * Data recovery.
* `Redis` Configuration and Management:
    * Configuration parameters.
    * Monitoring and logging.
    * Security considerations.
* `Redis` Cluster:
    * `Redis` Cluster architecture.
    * Sharding and replication.
    * Cluster management.
* Integrating `Redis` with Applications:
    * `Redis` clients (`Python`, `JavaScript`, etc.).
    * Connecting `Redis` to web applications.

## Textbooks and Resources
* `Redis` Documentation: [https://`Redis`.io/docs/](https://`Redis`.io/docs/)
* "`Redis` in Action" by Josiah Carlson (Optional)
* Various online tutorials and articles.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
