---
tags:
  - languages:java
  - tools:spring
  - tools:spring-data
  - concepts:databases
  - concepts:persistence
level: intermediate
category: language
duration_hours: 8
audience:
  - audiences:developers
---
<!-- course: spring_data -->
# `Spring Data`

## Description
This course provides a focused exploration of `Spring Data JPA` for building data access layers in `Java` applications. Covering repository abstractions, query derivation methods, specifications for dynamic queries, projections, auditing, pagination, and working with multiple data sources, the course equips developers with the skills to implement efficient and maintainable data persistence with `Spring Boot`.

## Duration
8 hours / 1 day

## Intended Audience
* `Java` developers building data-driven backend applications
* `Spring Boot` developers who need to implement efficient data access layers
* Software engineers working with relational databases in the `Spring` ecosystem
* Backend developers looking to move beyond basic `JDBC` and manual `SQL`
* Developers maintaining applications with complex query and data requirements

## Prerequisites
* Intermediate proficiency in `Java` programming (classes, interfaces, generics, annotations)
* Working knowledge of `Spring Boot` and dependency injection
* `Solid` understanding of relational databases and `SQL`
* Basic familiarity with `JPA` and `ORM` concepts
* Experience with build tools (`Maven` or `Gradle`)
* Experience with an IDE such as `IntelliJ IDEA` or `Eclipse`

## Objectives
* Understand the `Spring Data` repository abstraction and its layered architecture
* Create and customize `JPA` repositories with derived query methods
* Build dynamic queries using Specification and `Criteria API`
* Apply projections to optimize data retrieval and reduce overhead
* Implement entity auditing with creation and modification tracking
* Configure pagination and sorting for large result sets
* Set up and manage multiple data sources in a single application

## Outline
<!-- chapter: introduction-to-spring-data-jpa, duration: 1h -->
* Introduction to `Spring Data JPA`
    * Overview of the `Spring Data` project and module ecosystem
    * `JPA` and `Hibernate` foundations in `Spring Boot`
    * Entity mapping: annotations, relationships, and inheritance strategies
    * Auto-configuration and data source setup
    * Schema generation and initialization strategies
    * `Spring Data JPA` vs. plain `JPA` and `Hibernate`
<!-- chapter: repository-interfaces-and-query-methods, duration: 2h -->
* Repository Interfaces and Query Methods
    * CrudRepository, JpaRepository, and PagingAndSortingRepository
    * Derived query methods from method names
    * Query keywords: findBy, countBy, deleteBy, existsBy
    * Property expressions and nested property traversal
    * Limiting and sorting query results
    * Optional `return-types` and null handling
    * Custom repository implementations
    * @Query annotation with JPQL and native `SQL`
    * Named queries and query lookup strategies
    * Modifying queries with @Modifying
<!-- chapter: specifications-and-dynamic-queries, duration: 1h -->
* Specifications and Dynamic Queries
    * Introduction to the Specification interface
    * Building reusable Specification predicates
    * Combining specifications with and, or, and not
    * `Criteria API` fundamentals for complex queries
    * Querydsl integration as an alternative
    * Type-safe dynamic filtering patterns
<!-- chapter: projections, duration: 1h -->
* Projections
    * Interface-based closed projections
    * Interface-based open projections with @Value
    * Class-based (DTO) projections
    * Dynamic projections with generic repository methods
    * Nested projections for related entities
    * Projections with native queries
    * Performance implications of projection strategies
<!-- chapter: auditing, duration: 1h -->
* Auditing
    * Enabling `JPA` auditing with @EnableJpaAuditing
    * @CreatedDate, @LastModifiedDate, @CreatedBy, and @LastModifiedBy annotations
    * Implementing the AuditorAware interface
    * Auditing with `Spring Security` integration
    * Auditable base entity patterns
    * Entity lifecycle callbacks and event listeners
    * Envers for historical data auditing
<!-- chapter: pagination-and-sorting, duration: 1h -->
* Pagination and Sorting
    * Pageable and Sort parameters in repository methods
    * Page, Slice, and List `return-types`
    * Custom page size and default sorting configuration
    * Pagination in `REST APIs` with `Spring Data Web` support
    * PageableHandlerMethodArgumentResolver configuration
    * Keyset pagination for large datasets
    * Performance considerations with pagination
<!-- chapter: multiple-data-sources, duration: 1h -->
* Multiple Data Sources
    * Configuring multiple DataSource beans
    * Separate EntityManagerFactory instances per data source
    * Organizing entities and repositories by package
    * Transaction management across data sources
    * @Primary and @Qualifier annotations for disambiguation
    * JTA and distributed transactions
    * Read-write splitting patterns
    * Testing with multiple data sources

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
