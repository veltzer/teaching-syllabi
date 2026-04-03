---
tags:
  - tools:mongodb
  - data-and-ai:nosql
  - audiences:administration
  - practices:performance
level: intermediate
category: database
duration_hours: 40
audience:
  - audiences:dbas
  - audiences:sysadmins
  - audiences:architects
  - audiences:devops
---
<!-- course: mongodb_dba -->
# `MongoDB` DBA

## Description
`MongoDB` is a leading `NoSQL` document database that provides high performance, high availability, and automatic scaling for modern applications. As organizations increasingly adopt `MongoDB` for their critical applications, the need for skilled database administrators who can effectively manage, optimize, and secure `MongoDB` deployments has become essential.

This course provides comprehensive training for database administrators who need to deploy, maintain, monitor, and optimize `MongoDB` databases in production environments. Participants will gain hands-on experience with installation, configuration, backup strategies, performance tuning, security implementation, and troubleshooting of `MongoDB` clusters.

The course focuses on `MongoDB` version 7 and covers both on-premise and cloud deployment scenarios.

## Duration
40 hours / 5 days

## Intended Audience
* Database administrators transitioning from relational databases to `NoSQL`
* System administrators responsible for `MongoDB` deployments
* `DevOps` engineers who need to manage `MongoDB` in production
* IT professionals responsible for database infrastructure
* Technical architects designing `MongoDB`-based solutions

## Prerequisites
* Basic understanding of database concepts and administration
* Familiarity with `Linux` command line and basic system administration
* Understanding of `JSON` data format
* Experience with any database management system is beneficial

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Install and configure `MongoDB` in various deployment scenarios
* Design and implement effective backup and recovery strategies
* Monitor and optimize `MongoDB` performance
* Implement comprehensive security measures
* Manage replica sets and sharded clusters
* Troubleshoot common `MongoDB` issues
* Plan and execute `MongoDB` upgrades
* Implement disaster recovery procedures

## Exercises
Hands-on exercises performed on `Linux` virtual machines with `MongoDB` Community or Enterprise Edition. Students will work with replica sets, sharded clusters, and various administrative tools including `MongoDB Compass`, mongosh, and monitoring solutions. Real-world scenarios include setting up production-grade clusters, performing backups and restores, implementing security, and troubleshooting performance issues.

## Outline
<!-- chapter: introduction-to-mongodb-architecture, duration: 2h -->
* Introduction to `MongoDB` Architecture
    * Document model and BSON
    * `MongoDB` components and processes
    * Storage engines (WiredTiger)
    * Memory management
    * Journaling and durability
    * `MongoDB` editions and licensing
<!-- chapter: installation-and-configuration, duration: 2h -->
* Installation and Configuration
    * System requirements and capacity planning
    * Installation methods
    * Configuration `file` structure
    * Essential configuration parameters
    * Directory structure and `file` permissions
    * Starting and stopping `MongoDB`
    * Upgrading `MongoDB`
<!-- chapter: mongodb-shell-and-tools, duration: 2h -->
* `MongoDB` Shell and Tools
    * Using mongosh
    * Administrative commands
    * `MongoDB` Database Tools
    * `MongoDB Compass`
    * `MongoDB` command line tools
    * Scripting administrative tasks
<!-- chapter: data-management, duration: 2h -->
* Data Management
    * Database and collection management
    * Document validation
    * Indexes and index strategies
    * `TTL` indexes
    * Capped collections
    * Views and materialized views
    * Data import and export
<!-- chapter: replica-sets, duration: 3h -->
* Replica Sets
    * Replica set architecture
    * Setting up replica sets
    * Election and failover
    * Read preference and write concern
    * Replica set maintenance
    * Adding and removing members
    * Priority and hidden members
    * Arbiter nodes
<!-- chapter: sharding, duration: 3h -->
* Sharding
    * Sharding concepts and architecture
    * Shard keys and strategies
    * Setting up sharded clusters
    * Config servers
    * mongos routers
    * Chunk management
    * Balancer configuration
    * Adding and removing shards
<!-- chapter: backup-and-recovery, duration: 3h -->
* Backup and Recovery
    * Backup strategies
    * mongodump and mongorestore
    * `File` system snapshots
    * Point-in-time recovery
    * Backing up sharded clusters
    * Backup verification
    * Cloud backup solutions
    * Disaster recovery planning
<!-- chapter: security, duration: 3h -->
* Security
    * Authentication mechanisms
    * Role-based access control
    * Creating users and roles
    * `TLS`/`SSL` configuration
    * Encryption at `rest`
    * Auditing
    * Network security
    * Security best practices
<!-- chapter: monitoring-and-performance-tuning, duration: 3h -->
* Monitoring and Performance Tuning
    * Monitoring tools and metrics
    * Database profiler
    * `explain()` plans
    * Query optimization
    * Index optimization
    * Connection pooling
    * Working set sizing
    * Performance best practices
<!-- chapter: operations-and-maintenance, duration: 2h -->
* Operations and Maintenance
    * Log `file` management
    * Compact and repair operations
    * Statistics and diagnostics
    * Health checks
    * Automation with `MongoDB` Ops Manager
    * Cloud Manager
    * Rolling maintenance
<!-- chapter: high-availability-and-disaster-recovery, duration: 2h -->
* High Availability and Disaster Recovery
    * Designing for high availability
    * Multi-datacenter deployments
    * Failover procedures
    * Recovery procedures
    * Testing disaster recovery
    * RTO and RPO considerations
<!-- chapter: troubleshooting, duration: 3h -->
* Troubleshooting
    * Common issues and solutions
    * Analyzing log files
    * Performance bottlenecks
    * Replication issues
    * Sharding problems
    * Connection issues
    * Data corruption
    * Emergency procedures
<!-- chapter: mongodb-atlas-administration, duration: 2h -->
* `MongoDB` Atlas Administration
    * Atlas architecture
    * Cluster deployment
    * Monitoring in Atlas
    * Backup in Atlas
    * Security features
    * Performance advisor
    * Atlas `CLI` and `API`
<!-- chapter: migration-strategies, duration: 2h -->
* Migration Strategies
    * Migration planning
    * Data migration tools
    * Migration from RDBMS
    * Zero-downtime migrations
    * Data validation
    * Rollback procedures
<!-- chapter: advanced-topics, duration: 6h -->
* Advanced Topics
    * Change streams
    * Transactions
    * Schema `design patterns`
    * Time series collections
    * GridFS
    * Full-text search
    * Aggregation pipeline administration

## Installations
Each student should have:

* A `Linux` virtual machine (`Ubuntu` 24.04 LTS recommended) or access to cloud instances
* Minimum 8 GB `RAM` per machine (16 GB recommended for running multiple `MongoDB` instances)
* At least 50 GB of free disk space for data files and exercises
* Free, unrestricted internet access for downloading `MongoDB` packages and documentation
* Administrative (`sudo`) privileges on the machine
* `MongoDB` Community Edition will be installed during the course (no pre-installation required)
* Optional: `MongoDB Compass` for graphical administration
* Text editor of choice (`vim`, `nano`, or `VSCode`)
* Students planning to work with `MongoDB` Atlas should have access to create a free Atlas account
* For `Windows` users: WSL2 with `Ubuntu` is acceptable, or native `Windows` `MongoDB` installation
* For `MacOS` users: Native `MongoDB` installation is fully supported

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
