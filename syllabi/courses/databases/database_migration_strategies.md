---
tags:
  - concepts:databases
  - practices:devops
  - practices:ci-cd
level: intermediate
category: database
duration_hours: 16
audience:
  - audiences:developers
  - audiences:dbas
  - audiences:devops
---
<!-- course: database_migration_strategies -->
# Database Migration Strategies

## Description
This course covers modern strategies and tools for managing database schema changes in production environments. Participants will learn how to perform zero-downtime migrations, implement schema versioning with tools like Flyway and Liquibase, apply the expand-contract pattern for backward-compatible changes, and integrate database migrations into `CI/CD` pipelines. The course also addresses data migration techniques, blue-green database deployments, rollback strategies, and testing practices for migrations.

## Duration
16 hours / 1 day

## Intended Audience
* Backend developers responsible for database schema changes
* `DevOps` engineers integrating database changes into deployment pipelines
* Database administrators managing schema evolution in production
* Team leads overseeing release processes involving database changes

## Prerequisites
* Experience with software development and deployment workflows
* Understanding of relational database concepts and schema design

## Required Knowledge
* `SQL` (or equivalent relational database experience)

## Objectives
* Plan and execute zero-downtime database migrations
* Implement schema versioning using Flyway and Liquibase
* Apply the expand-contract pattern for backward-compatible schema changes
* Design and execute safe data migrations
* Set up blue-green database deployment strategies
* Develop reliable rollback strategies for failed migrations
* Integrate database migrations into `CI/CD` pipelines

## Outline
<!-- chapter: fundamentals-of-database-migrations, duration: 1h -->
* Fundamentals of Database Migrations
    * Why database migrations are challenging
    * Schema evolution vs data migration
    * Migration as code: version-controlled schema changes
    * Idempotent and repeatable migrations
    * Migration naming conventions and ordering
<!-- chapter: zero-downtime-migrations, duration: 2h -->
* Zero-Downtime Migrations
    * The problem with downtime during schema changes
    * Online schema change techniques
    * Non-blocking `ALTER TABLE` operations
    * Strategies for adding and removing columns safely
    * Managing constraint changes without locking
    * Table rebuild strategies for large tables
<!-- chapter: schema-versioning-with-flyway, duration: 1h -->
* Schema Versioning with Flyway
    * Flyway architecture and concepts
    * Versioned migrations, undo migrations, and repeatable migrations
    * Flyway configuration and environments
    * Baseline and repair operations
    * Flyway callbacks and placeholders
<!-- chapter: schema-versioning-with-liquibase, duration: 2h -->
* Schema Versioning with Liquibase
    * Liquibase changelogs and changesets
    * Supported formats: `XML`, `YAML`, `JSON`, and `SQL`
    * Contexts and labels for environment-specific changes
    * Liquibase diff and snapshot capabilities
    * Generating changelogs from existing databases
<!-- chapter: the-expand-contract-pattern, duration: 2h -->
* The Expand-Contract Pattern
    * Principles of backward-compatible schema changes
    * The expand phase: adding new structures alongside old
    * The migration phase: moving data and updating application code
    * The contract phase: removing deprecated structures
    * Coordinating schema changes with application deployments
    * Multi-version application compatibility
<!-- chapter: data-migrations, duration: 2h -->
* Data Migrations
    * Strategies for migrating large volumes of data
    * Batched data migrations to minimize lock contention
    * Backfilling new columns with default values
    * Data transformation during migration
    * Validating data integrity after migration
<!-- chapter: blue-green-database-deployments, duration: 2h -->
* Blue-Green Database Deployments
    * Blue-green deployment concepts applied to databases
    * Database synchronization between blue and green environments
    * Cutover strategies and traffic switching
    * Handling schema divergence during deployment
    * Challenges and limitations of blue-green database deployments
<!-- chapter: rollback-strategies, duration: 2h -->
* Rollback Strategies
    * Designing migrations with rollback in mind
    * Forward-only vs reversible migrations
    * Compensating migrations for irreversible changes
    * Point-in-time recovery as a rollback mechanism
    * Testing rollback procedures
<!-- chapter: migration-testing-and-ci-cd-integration, duration: 2h -->
* Migration Testing and `CI/CD` Integration
    * Testing migrations against production-like data
    * Migration dry runs and validation
    * Integrating migrations into `CI/CD` pipelines
    * Automated migration testing in staging environments
    * Monitoring migration execution in production
    * Migration governance and approval workflows

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
