---
tags:
  - concepts:databases
  - concepts:database-design
  - concepts:data-modeling
  - concepts:data-architecture
  - concepts:normalization
  - concepts:domain-driven-design
level: intermediate
category: database
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:dbas
  - audiences:data-engineers
  - audiences:data-architects
  - audiences:architects
---
<!-- course: data_modeling_in_depth -->
# Data Modeling in Depth

## Description
Data modeling is one of the few engineering skills whose mistakes follow you for years. The schema you ship in
year one shapes the queries, joins, indexes, migrations and integrations you will be paying for in year five.
Most developers learn modeling by osmosis from a single language and a single relational database, then apply
those reflexes badly to document stores, time-series databases, graphs and warehouses where the rules are
different.

This five day course is a paradigm-spanning treatment of data modeling. It covers the conceptual/logical/physical
distinction, normalization and the cases where you should and should not denormalize, dimensional modeling for
analytics, modeling for `OLTP` vs `OLAP` vs document vs key-value vs graph vs time-series stores, the relationship
between domain models and database models, and the operational realities of evolving a schema in production.
Participants leave able to model new domains correctly across paradigms and to read existing schemas critically.

## Duration
40 hours / 5 days

## Intended Audience
* developers designing or refactoring database schemas
* `DBAs` and data engineers responsible for schema quality
* architects whose system design begins with the data model
* engineers transitioning between relational, document, graph and analytical paradigms

## Prerequisites
* working knowledge of `SQL` and at least one relational database
* exposure to at least one non-relational database
* basic familiarity with at least one programming language and `ORM`

## Objectives
* model a domain at the conceptual, logical and physical levels
* apply normalization correctly and recognize `when` to denormalize
* design dimensional models for analytical workloads
* choose between relational, document, key-value, graph and time-series modeling
* evolve a schema in production without breakage
* read an existing schema and identify its strengths and weaknesses
* avoid the modeling mistakes that cause years of pain

## Outline
<!-- chapter: why-modeling-matters, duration: 2h -->
* Why modeling matters
    * the long shadow of the first schema
    * modeling as design, not data entry
    * the relationship between domain modeling and data modeling
    * conceptual, logical and physical levels
    * the difference between modeling and `ORM` configuration
<!-- chapter: conceptual-modeling, duration: 3h -->
* Conceptual modeling
    * entities, relationships, attributes
    * `ER` diagrams and the Chen vs `IDEF1X` notations
    * `UML` class diagrams as data models
    * cardinality and participation
    * weak entities and identifying relationships
    * recognizing `when` a thing is an attribute vs an entity
<!-- chapter: logical-modeling-and-normalization, duration: 4h -->
* Logical modeling and normalization
    * functional dependencies
    * `1NF`, `2NF`, `3NF`, `BCNF`
    * `4NF` and multivalued dependencies
    * `5NF` and join dependencies
    * `6NF` for `temporal` and time-series modeling
    * normalization for correctness, denormalization for performance
    * the "normalize, then measure" rule
<!-- chapter: physical-modeling-for-relational-databases, duration: 3h -->
* Physical modeling for relational databases
    * choosing primary keys: natural, surrogate, composite
    * `UUID` vs auto-increment vs `ULID`/`KSUID`
    * indexing strategy from queries, not from columns
    * partitioning at the table level
    * materialized views and indexed views
    * physical layout choices in `PostgreSQL` and `MySQL`
<!-- chapter: when-and-how-to-denormalize, duration: 2h -->
* `When` and how to denormalize
    * the cost of joins at scale
    * read-vs-write ratio as a denormalization driver
    * controlled redundancy and update anomalies
    * computed columns and triggers
    * materialized views as managed denormalization
    * denormalize last, not first
<!-- chapter: domain-driven-design-and-data-modeling, duration: 3h -->
* `Domain-driven design` and data modeling
    * aggregates as data-modeling boundaries
    * value objects and their persistence
    * entity identity vs row identity
    * the relationship between bounded contexts and schemas
    * mapping rich domain models to database schemas
    * the "anemic schema" anti-pattern
<!-- chapter: modeling-for-document-stores, duration: 3h -->
* Modeling for document stores
    * embedded vs referenced documents
    * the right size for a document
    * read-pattern-driven design
    * arrays and the cost of unbounded growth
    * indexing inside documents
    * `MongoDB`, `DocumentDB`, `Cosmos DB` modeling idioms
    * common document-store modeling mistakes
<!-- chapter: modeling-for-key-value-and-wide-column, duration: 3h -->
* Modeling for key-value and wide-column
    * single-table design in `DynamoDB`
    * partition key and sort key
    * access pattern catalog as the design driver
    * `GSI`s and overloaded indexes
    * `Cassandra` and `ScyllaDB` partition modeling
    * the "model for queries first" rule
    * common single-table-design pitfalls
<!-- chapter: modeling-for-graph-databases, duration: 2h -->
* Modeling for graph databases
    * nodes and relationships as first-class
    * direction, type, properties on edges
    * `Neo4j` and `Cypher` modeling
    * `GraphRAG` and graph-as-knowledge-base
    * `when` a graph database is right and `when` it is overkill
<!-- chapter: modeling-for-time-series-and-events, duration: 2h -->
* Modeling for time-series and events
    * the wide-narrow decision
    * tags, fields and time keys in `InfluxDB`/`TimescaleDB`
    * downsampling and retention modeling
    * append-only modeling for events
    * cardinality control
<!-- chapter: dimensional-modeling-for-analytics, duration: 3h -->
* Dimensional modeling for analytics
    * facts, dimensions, grain
    * star schema vs `snowflake` schema
    * slowly changing dimensions: types 0 to 7
    * conformed dimensions
    * `Kimball` vs `Inmon` vs `Data Vault`
    * dimensional modeling for `BigQuery`/`Snowflake`/`Redshift`
<!-- chapter: data-vault-and-anchor-modeling, duration: 2h -->
* Data `Vault` and Anchor Modeling
    * hubs, links, satellites
    * Data `Vault` 2.0
    * anchor modeling and `6NF`
    * `when` these approaches are worth the complexity
    * combining with dimensional models for the consumer layer
<!-- chapter: schema-evolution-and-migrations, duration: 3h -->
* Schema evolution and migrations
    * additive evolution as the default
    * expand-and-contract for schema changes
    * online migrations on large tables
    * dual-write `windows`
    * data migrations vs schema migrations
    * tools: `Flyway`, `Liquibase`, `Alembic`, `gh-ost`, `pt-online-schema-change`
<!-- chapter: modeling-anti-patterns, duration: 2h -->
* Modeling anti-patterns
    * the entity-attribute-value anti-pattern
    * the god table
    * polymorphic associations
    * boolean explosion
    * `JSON` columns as a substitute for modeling
    * deletion flags vs proper history tables
    * recognizing each in the wild
<!-- chapter: case-studies, duration: 2h -->
* Case studies
    * modeling a multi-tenant `B2B` `SaaS`
    * modeling a billing system
    * modeling an event log alongside a relational core
    * modeling a search-heavy product catalog
    * modeling user history with privacy in mind
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * group review of a real schema, with critique
    * design walkthrough of a sample domain across paradigms
    * recommended reading: `Kleppmann`, `Kimball`, `Linstedt`, `Codd`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
