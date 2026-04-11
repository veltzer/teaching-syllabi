---
tags:
  - languages:java
  - concepts:persistence
  - concepts:databases
  - concepts:oop
level: intermediate
category: language
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: java_hibernate -->
# `Java` `Hibernate`/`JPA`

## Description
This course provides comprehensive coverage of `Java` persistence using `Hibernate` and
the `JPA` specification. Participants will learn entity mapping, relationship modeling,
querying strategies, caching, and performance optimization techniques. The course also
covers integration with `Spring Data JPA` and database migration strategies.

## Duration
24 hours / 3 days

## Intended Audience
* `Java` developers who need to work with relational databases.
* Backend developers building data-driven applications with `Java`.

## Prerequisites
* `Solid` experience in `Java` programming.
* Basic understanding of relational databases and `SQL`.

## Objectives
* Participants will gain a thorough understanding of
    * The `JPA` specification and its relationship to `Hibernate`.
    * Entity mapping and relationship modeling.
    * Querying with JPQL and the Criteria `API`.
    * Caching strategies and performance optimization.
    * Common pitfalls such as the N+1 problem.
    * Integration with `Spring Data JPA`.

## Outline
<!-- chapter: jpa-specification, duration: 2h -->
* `JPA` Specification
    * `JPA` architecture and providers
    * Persistence units and configuration
    * Entity manager and persistence context
    * Entity lifecycle and states
<!-- chapter: entity-mapping, duration: 2h -->
* Entity Mapping
    * Basic annotations and column mapping
    * Primary key generation strategies
    * Embedded types and composites
    * Inheritance mapping strategies
    * Table and column naming conventions
<!-- chapter: relationships, duration: 3h -->
* Relationships
    * One-to-one mapping
    * One-to-many and many-to-one mapping
    * Many-to-many mapping
    * Bidirectional vs unidirectional relationships
    * Cascade types and orphan removal
    * Join tables and join columns
<!-- chapter: lazy-vs-eager-loading, duration: 2h -->
* Lazy vs Eager Loading
    * Fetch types and their implications
    * Lazy initialization exceptions
    * Entity graphs
    * Fetch joins
    * Open Session in View pattern
<!-- chapter: querying, duration: 3h -->
* Querying
    * JPQL syntax and capabilities
    * Criteria `API`
    * Native `SQL` queries
    * Named queries
    * Projections and DTOs
    * Pagination and sorting
<!-- chapter: the-n-1-problem, duration: 2h -->
* The N+1 Problem
    * Understanding the N+1 query issue
    * Detection strategies
    * Solutions with fetch joins
    * Batch fetching
    * Subselect fetching
<!-- chapter: caching, duration: 2h -->
* Caching
    * First-level cache (persistence context)
    * Second-level cache configuration
    * Cache providers (Ehcache, Infinispan)
    * Query cache
    * Cache eviction strategies
<!-- chapter: transactions, duration: 2h -->
* Transactions
    * Transaction management in `JPA`
    * Optimistic vs pessimistic locking
    * Isolation levels
    * Transaction propagation
    * Handling concurrent access
<!-- chapter: query-optimization, duration: 2h -->
* Query Optimization
    * Query plan analysis
    * Index considerations
    * Bulk operations
    * Stateless sessions
    * Read-only queries
<!-- chapter: database-migrations, duration: 2h -->
* Database Migrations
    * Schema generation strategies
    * `Flyway` integration
    * `Liquibase` integration
    * Migration best practices
<!-- chapter: spring-data-jpa-integration, duration: 2h -->
* `Spring Data JPA` Integration
    * Repository abstraction
    * Derived query methods
    * Custom repository implementations
    * Specifications and querydsl
    * Auditing support

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
