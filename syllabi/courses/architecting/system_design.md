---
tags:
  - concepts:architecture
  - concepts:scalability
  - concepts:distributed-systems
  - concepts:design-patterns
level: intermediate
category: architecture
duration_hours: 24
audience:
  - audiences:developers
  - audiences:architects
  - audiences:team-leads
---
<!-- course: system_design -->
# System Design

## Description
This course teaches the principles and practices of designing large-scale, distributed systems. Participants will learn how to analyze requirements, perform back-of-envelope estimations, and `make` informed architectural decisions. The course covers fundamental building blocks such as load balancers, caching strategies, database sharding, message queues, and consistent hashing. Real-world case studies including a URL shortener, chat system, news feed, and search engine provide practical design experience.

## Duration
24 hours / 3 days

## Intended Audience
* Software developers preparing for system design discussions and interviews
* Software architects designing scalable distributed systems
* Technical leads making architectural decisions for growing applications
* Engineers transitioning from single-server to distributed architectures

## Prerequisites
* Several years of software development experience
* Familiarity with web application architecture and `HTTP`
* Basic understanding of databases and `SQL`
* Experience with at least one backend programming language

## Objectives
* Analyze functional and non-functional requirements for system design
* Perform back-of-envelope estimations for capacity, storage, and bandwidth
* Design systems that scale horizontally to handle millions of users
* Select and configure appropriate load balancing strategies
* Design caching strategies using `Redis` and CDN solutions
* Apply database sharding and partitioning techniques
* Design `API` interfaces and apply rate limiting
* Use consistent hashing for distributed data placement
* Design complete systems through real-world case studies

## Outline
<!-- chapter: requirements-analysis-and-estimation, duration: 2h -->
* Requirements Analysis and Estimation
    * Gathering functional and non-functional requirements
    * Defining system constraints and assumptions
    * Back-of-envelope estimation techniques
    * Estimating queries per second, storage, and bandwidth
    * Defining service-level objectives and service-level agreements
    * Identifying bottlenecks early in the design process
<!-- chapter: api-design, duration: 2h -->
* `API` Design
    * RESTful `API` design principles
    * `API` versioning strategies
    * Pagination, filtering, and sorting
    * Idempotency and retry safety
    * `API` rate limiting: token bucket and sliding window algorithms
    * `API gateway` patterns and responsibilities
<!-- chapter: load-balancing, duration: 2h -->
* Load Balancing
    * Load balancing algorithms: round-robin, least connections, weighted, and `IP` hash
    * Layer 4 vs layer 7 load balancing
    * Health checks and failover
    * Global server load balancing and geographic routing
    * Load balancer high availability
    * Service discovery and dynamic backend registration
<!-- chapter: caching-strategies, duration: 2h -->
* Caching Strategies
    * Cache-aside, read-through, write-through, and write-behind patterns
    * `Redis` as a distributed cache: data structures, persistence, and clustering
    * CDN caching for static and dynamic content
    * Cache invalidation strategies and consistency
    * Cache stampede prevention and thundering herd mitigation
    * Multi-tier caching architectures
    * Cache sizing and eviction policies
<!-- chapter: database-design-and-scaling, duration: 3h -->
* Database Design and Scaling
    * Choosing between `SQL` and `NoSQL` databases
    * Database replication: primary-replica and multi-primary
    * Vertical and horizontal partitioning (sharding)
    * Sharding strategies: range-based, hash-based, and directory-based
    * Handling cross-shard queries and distributed transactions
    * Database connection pooling and query optimization
    * Read replicas and eventual consistency
<!-- chapter: message-queues, duration: 3h -->
* Message Queues
    * Synchronous vs asynchronous communication
    * Message queue architectures and use cases
    * Point-to-point vs publish-subscribe patterns
    * Message ordering, deduplication, and delivery guarantees
    * Dead letter queues and retry strategies
    * `Event-driven architecture` with message queues
    * Backpressure and flow control
<!-- chapter: consistent-hashing, duration: 2h -->
* Consistent Hashing
    * The problem of data distribution in distributed systems
    * Consistent hashing algorithm and virtual nodes
    * Handling node addition and removal
    * Data replication with consistent hashing
    * Applications: distributed caches, databases, and load balancers
<!-- chapter: case-study-url-shortener, duration: 2h -->
* Case Study: URL Shortener
    * Requirements and constraints
    * URL encoding and key generation strategies
    * Database schema and storage considerations
    * Read-heavy optimization and caching
    * Analytics and click tracking
    * Handling high traffic and scaling
<!-- chapter: case-study-chat-system, duration: 2h -->
* Case Study: Chat System
    * Real-time messaging requirements
    * `WebSocket` connections and connection management
    * Message storage and retrieval
    * Group chat and presence service design
    * Push notifications and offline message delivery
    * Message ordering and delivery guarantees
<!-- chapter: case-study-news-feed, duration: 2h -->
* Case Study: News Feed
    * Feed generation: fan-out on write vs fan-out on read
    * Feed ranking and personalization
    * Media storage and serving
    * Handling celebrity users and hot partitions
    * Feed caching and pagination
    * Real-time feed updates
<!-- chapter: case-study-search-engine, duration: 2h -->
* Case Study: Search Engine
    * Web crawling architecture and politeness
    * Indexing: inverted index construction and storage
    * Query processing and ranking algorithms
    * Autocomplete and typeahead suggestions
    * Search result caching
    * Scaling search across multiple data centers

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
