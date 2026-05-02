---
tags:
  - tools:mysql
  - practices:performance
level: intermediate
category: database
duration_hours: 32
audience:
  - audiences:dbas
  - audiences:sysadmins
  - audiences:architects
  - audiences:devops
---
<!-- course: mysql_administration -->
# `MySQL` Administration

## Description
This course provides comprehensive training in `MySQL` database administration, covering architecture, installation, configuration, backup and recovery, replication, performance tuning, security, and high availability. Participants will gain the practical skills needed to deploy, manage, and optimize `MySQL` in production environments.

The course emphasizes hands-on experience with real-world administrative scenarios, preparing database administrators and system administrators to maintain reliable, secure, and performant `MySQL` deployments.

## Duration
32 hours / 4 days

## Intended Audience
* Database administrators managing `MySQL` instances
* System administrators responsible for database infrastructure
* `DevOps` engineers deploying and maintaining `MySQL`
* IT professionals transitioning to `MySQL` administration
* Infrastructure engineers designing database architectures

## Prerequisites
* Basic understanding of relational database concepts
* Familiarity with `SQL` fundamentals
* `Linux` command line proficiency
* Basic networking knowledge (`TCP`/`IP`, ports, firewalls)

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Understand `MySQL` architecture and storage engines
* Install, configure, and manage `MySQL` instances
* Implement robust backup and recovery strategies
* Configure and manage various replication topologies
* Monitor and troubleshoot performance issues
* Tune `MySQL` for optimal performance
* Implement security best practices including `SSL`/`TLS` and encryption at `rest`
* Set up high availability solutions with `MySQL InnoDB Cluster`

## Exercises
Hands-on lab exercises covering installation, configuration, user management, backup and recovery, replication setup, monitoring, and performance tuning. Students will configure my.cnf, perform backups with mysqldump and xtrabackup, set up asynchronous and semi-synchronous replication, analyze slow queries with EXPLAIN, configure `Performance Schema` monitoring, and deploy `MySQL InnoDB Cluster`. Exercises simulate realistic production scenarios and failure conditions.

## Outline
<!-- chapter: mysql-architecture, duration: 2h -->
* `MySQL` Architecture
    * `MySQL` server architecture overview
    * Client-server communication protocol
    * `Threading` model and connection handling
    * Query execution pipeline
    * Storage engine architecture
    * InnoDB as the default storage engine
    * Other storage engines: MyISAM, Memory, Archive
    * The data dictionary

<!-- chapter: installation-and-configuration, duration: 2h -->
* Installation and Configuration
    * Installing `MySQL` on `Linux` and other platforms
    * Package managers vs binary distributions
    * mysqld initialization and data directory setup
    * Directory structure and file layout
    * my.cnf configuration file structure
    * Key server parameters and system variables
    * `systemd` integration and service management
    * Startup and shutdown procedures

<!-- chapter: user-management-and-privileges, duration: 2h -->
* User Management and Privileges
    * The `MySQL` privilege system
    * Creating and managing user accounts
    * Authentication plugins: caching_sha2_password, mysql_native_password
    * GRANT and REVOKE operations
    * Role-based access control
    * Account resource limits
    * Password policies and expiration
    * Best practices for privilege design

<!-- chapter: backup-and-recovery, duration: 3h -->
* Backup and Recovery
    * Backup strategies overview: logical vs physical
    * Logical backups with mysqldump
    * Parallel backups with mysqlpump
    * Physical backups with `Percona XtraBackup`
    * Binary log overview and configuration
    * Point-in-time recovery using binary logs
    * Backup verification and testing
    * Backup scheduling and automation
    * Restoring from backups

<!-- chapter: replication, duration: 3h -->
* Replication
    * Replication concepts and architecture
    * Asynchronous replication setup
    * Semi-synchronous replication
    * GTID-based replication
    * Binary log formats: ROW, STATEMENT, MIXED
    * Multi-source replication
    * Replication filters
    * `Group Replication` concepts and setup
    * Monitoring and troubleshooting replication

<!-- chapter: innodb-internals, duration: 3h -->
* InnoDB Internals
    * InnoDB buffer pool architecture
    * Buffer pool sizing and configuration
    * Redo log and write-ahead logging
    * Undo logs and MVCC
    * InnoDB tablespace management
    * `File`-per-table vs shared tablespace
    * Data page structure
    * Adaptive hash index
    * Change buffer

<!-- chapter: performance-tuning, duration: 3h -->
* Performance Tuning
    * Query optimization fundamentals
    * Using EXPLAIN and `EXPLAIN ANALYZE`
    * Slow query log configuration and analysis
    * Index strategies and optimization
    * Memory parameters: innodb_buffer_pool_size, sort_buffer_size, join_buffer_size
    * `I/O` tuning: innodb_io_capacity, innodb_flush_method
    * Thread and connection tuning
    * Query cache considerations
    * Benchmarking with sysbench

<!-- chapter: monitoring, duration: 2h -->
* Monitoring
    * `Performance Schema` architecture and configuration
    * Key `Performance Schema` tables and consumers
    * sys schema views and utilities
    * `SHOW STATUS` and `SHOW VARIABLES`
    * INFORMATION_SCHEMA tables
    * Monitoring replication health
    * Integration with `Prometheus` and `Grafana`
    * Alert configuration and thresholds

<!-- chapter: security, duration: 2h -->
* Security
    * `SSL`/`TLS` configuration for encrypted connections
    * Certificate management and rotation
    * `MySQL Enterprise Audit` log
    * InnoDB tablespace encryption (encryption at `rest`)
    * Binary log encryption
    * Network security and `firewall` rules
    * Secure deployment best practices
    * Compliance considerations

<!-- chapter: high-availability, duration: 3h -->
* High Availability
    * High availability concepts and architectures
    * `MySQL InnoDB Cluster` architecture
    * Setting up `MySQL InnoDB Cluster`
    * `MySQL Router` for connection routing
    * `MySQL Shell` for cluster management
    * Automatic failover and recovery
    * Split-brain prevention
    * Testing failover scenarios

<!-- chapter: partitioning, duration: 2h -->
* Partitioning
    * Partitioning concepts and use cases
    * RANGE, LIST, HASH, and KEY partitioning
    * Subpartitioning
    * Partition pruning and query optimization
    * Partition management operations
    * Limitations and best practices

<!-- chapter: upgrade-strategies, duration: 2h -->
* Upgrade Strategies
    * Minor version upgrades
    * Major version upgrades: in-place vs logical
    * mysql_upgrade and upgrade checks
    * Testing upgrades in staging environments
    * Rollback planning
    * Replication-based upgrade strategies
    * Compatibility considerations

<!-- chapter: troubleshooting, duration: 3h -->
* Troubleshooting
    * Error log analysis
    * Diagnosing connection issues
    * Lock contention and deadlock analysis
    * Disk space and storage issues
    * Crash recovery procedures
    * Memory usage troubleshooting
    * Common performance bottlenecks
    * Diagnostic tools and utilities

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
