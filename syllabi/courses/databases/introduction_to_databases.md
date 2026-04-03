---
tags:
  - concepts:databases
level: beginner
category: database
duration_hours: 24
audience:
  - audiences:developers
  - audiences:devops
---
<!-- course: introduction_to_databases -->
# Introduction to Databases

## Description
A unified introduction to both `SQL` and `NoSQL` databases with hands-on practice.
This course takes students from the fundamentals of what databases are and why we
need them, through relational database concepts and `SQL` syntax, to document databases
and `NoSQL` paradigms. Students will gain practical experience with both `MySQL` and
`MongoDB`, and learn how to choose the right database for their use case.

## Duration
24 hours / 3 days

## Intended Audience
* Developers who need to work with databases in their applications
* `DevOps` engineers who need to manage and maintain database infrastructure

## Prerequisites
* Basic programming experience in any language
* Familiarity with the command line

## Objectives
* Understand fundamental database concepts and terminology
* Write `SQL` queries to create, read, update, and delete data
* Install, configure, and perform basic administration of `MySQL`
* Install, configure, and perform `CRUD` operations with `MongoDB`
* Compare relational and document databases and understand the trade-offs
* Know `when` to choose `SQL` vs `NoSQL` for a given use case
* Understand the role of Object Relational Mappers (`ORMs`)

## Outline
<!-- chapter: what-are-databases, duration: 2h -->
* What Are Databases
    * Why we need databases
    * `File`-based storage vs database management systems
    * Types of databases overview
    * `ACID` properties
    * Database transactions
<!-- chapter: relational-database-concepts, duration: 2h -->
* Relational Database Concepts
    * Tables, rows, and columns
    * Primary keys and foreign keys
    * Relationships (one-to-one, one-to-many, many-to-many)
    * Normalization and denormalization
    * Indexes and their purpose
<!-- chapter: database-schemas-and-migrations, duration: 2h -->
* Database Schemas and Migrations
    * What is a schema
    * Creating and modifying schemas
    * Schema versioning
    * Database migrations and why they matter
    * Migration tools and workflows
<!-- chapter: sql-vs-nosql, duration: 2h -->
* `SQL` vs `NoSQL`
    * Relational vs non-relational paradigms
    * Document stores, key-value stores, graph databases, column-family stores
    * `When` to use `SQL`
    * `When` to use `NoSQL`
    * Hybrid approaches
<!-- chapter: sql-syntax, duration: 3h -->
* `SQL` Syntax
    * `SELECT` statements and filtering with `WHERE`
    * `INSERT`, `UPDATE`, and `DELETE`
    * `JOIN` types (inner, left, right, full)
    * `GROUP BY` and aggregate functions
    * `ORDER BY` and `LIMIT`
    * Subqueries and nested queries
    * Creating and altering tables
<!-- chapter: mysql, duration: 3h -->
* `MySQL`
    * Installation and setup
    * Configuration basics
    * Creating users and managing permissions
    * Importing and exporting data
    * Basic administration tasks
    * Using the `MySQL` command-line client
    * Common storage engines (`InnoDB`, `MyISAM`)
<!-- chapter: mongodb, duration: 3h -->
* `MongoDB`
    * Installation and setup
    * Configuration basics
    * Documents and collections
    * `CRUD` operations (insert, `find`, update, delete)
    * Creating users and managing access
    * Querying with filters and projections
    * Indexing in `MongoDB`
<!-- chapter: comparing-relational-and-document-databases, duration: 3h -->
* Comparing Relational and Document Databases
    * Data modeling differences
    * Schema flexibility vs schema enforcement
    * Scalability characteristics
    * Query capabilities
    * Transaction support
    * Performance considerations
<!-- chapter: object-relational-mappers, duration: 2h -->
* Object Relational Mappers (`ORMs`)
    * What is an `ORM`
    * Benefits and drawbacks of using an `ORM`
    * Popular `ORMs` by language (`SQLAlchemy`, `Hibernate`, `Sequelize`, `TypeORM`)
    * `When` to use raw `SQL` vs an `ORM`
<!-- chapter: choosing-the-right-database, duration: 2h -->
* Choosing the Right Database for Your Use Case
    * Evaluating requirements (consistency, availability, partition tolerance)
    * Read-heavy vs write-heavy workloads
    * Structured vs unstructured data
    * Scaling requirements
    * Ecosystem and community support

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
