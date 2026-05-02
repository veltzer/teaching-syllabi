---
tags:
  - tools:postgresql
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
<!-- course: postgresql_administration -->
# `PostgreSQL` Administration

## Description
This course provides comprehensive training in `PostgreSQL` database administration, covering everything from initial installation and configuration through advanced topics like replication, high availability, and performance tuning. Participants will gain the skills needed to deploy, manage, monitor, and optimize `PostgreSQL` in production environments.

The course emphasizes practical, hands-on experience with real-world administrative scenarios, preparing DBAs and system administrators to maintain reliable, secure, and performant `PostgreSQL` deployments.

## Duration
32 hours / 4 days

## Intended Audience
* Database administrators managing `PostgreSQL` instances
* System administrators responsible for database infrastructure
* `DevOps` engineers deploying and maintaining `PostgreSQL`
* IT professionals transitioning to `PostgreSQL` administration
* Infrastructure engineers designing database architectures

## Prerequisites
* Basic understanding of relational database concepts
* Familiarity with `SQL` fundamentals
* `Linux` command line proficiency
* Basic networking knowledge (`TCP`/`IP`, ports, firewalls)

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Install, configure, and manage `PostgreSQL` instances
* Implement robust backup and recovery strategies
* Configure streaming and logical replication
* Set up high availability solutions
* Monitor and troubleshoot performance issues
* Tune `PostgreSQL` for optimal performance
* Implement security best practices including `SSL` and row-level security
* Plan and execute version upgrades

## Exercises
Hands-on lab exercises covering installation, configuration, backup and recovery, replication setup, monitoring, and performance tuning. Students will configure `postgresql`.conf and pg_hba.conf, perform point-in-time recovery, set up streaming replication, configure monitoring dashboards, analyze and resolve performance bottlenecks, and implement security hardening. Exercises simulate realistic production scenarios and failure conditions.

## Outline
<!-- chapter: installation-and-configuration, duration: 2h -->
* Installation and Configuration
    * Installing `PostgreSQL` on `Linux` and other platforms
    * Package managers vs source compilation
    * initdb and cluster initialization
    * Directory structure and file layout
    * `postgresql`.conf key parameters
    * pg_hba.conf configuration
    * pg_ctl and `systemd` integration
    * Startup and shutdown procedures

<!-- chapter: authentication-and-access-control, duration: 2h -->
* Authentication and Access Control
    * Authentication methods: trust, `md5`, scram-`sha`-256, peer, cert
    * pg_hba.conf rules and matching
    * `LDAP` and `RADIUS` integration
    * Certificate-based authentication
    * Connection limits and timeouts

<!-- chapter: user-and-role-management, duration: 2h -->
* User and Role Management
    * Roles and privileges model
    * Creating and managing users
    * Role inheritance and membership
    * GRANT and REVOKE operations
    * Default privileges
    * Schema-level permissions
    * Best practices for role design

<!-- chapter: backup-strategies, duration: 2h -->
* Backup Strategies
    * Logical backups with pg_dump and pg_dumpall
    * Physical backups with pg_basebackup
    * WAL archiving configuration
    * Point-in-time recovery (PITR)
    * Backup verification and testing
    * Backup scheduling and automation
    * Third-party backup tools: pgBackRest, Barman

<!-- chapter: replication, duration: 3h -->
* Replication
    * Streaming replication setup
    * Synchronous vs asynchronous replication
    * Replication slots
    * Logical replication concepts
    * Publication and subscription model
    * Logical decoding
    * Replication monitoring and troubleshooting
    * Failover and switchover procedures

<!-- chapter: high-availability, duration: 2h -->
* High Availability
    * High availability concepts and architectures
    * Patroni for automatic failover
    * pgpool-II for connection pooling and load balancing
    * `HAProxy` with `PostgreSQL`
    * Virtual `IP` management
    * Split-brain prevention
    * Testing failover scenarios

<!-- chapter: monitoring, duration: 3h -->
* Monitoring
    * pg_stat views overview
    * pg_stat_activity for active sessions
    * pg_stat_user_tables and pg_stat_user_indexes
    * pg_stat_statements for query analysis
    * pg_stat_replication for replication monitoring
    * Log analysis and configuration
    * Integration with `Prometheus` and `Grafana`
    * Alert configuration

<!-- chapter: vacuum-and-autovacuum, duration: 2h -->
* Vacuum and Autovacuum
    * MVCC and dead tuple management
    * Manual VACUUM and `VACUUM FULL`
    * Autovacuum configuration and tuning
    * Transaction `ID` wraparound prevention
    * Monitoring vacuum activity
    * Troubleshooting vacuum issues

<!-- chapter: performance-tuning, duration: 3h -->
* Performance Tuning
    * Memory parameters: shared_buffers, work_mem, effective_cache_size
    * WAL configuration: wal_buffers, checkpoint_completion_target
    * Planner parameters: random_page_cost, effective_io_concurrency
    * Connection tuning: max_connections, connection pooling
    * `I/O` tuning and storage considerations
    * Query performance analysis
    * Benchmarking with pgbench
    * Workload-specific tuning profiles

<!-- chapter: connection-management, duration: 2h -->
* Connection Management
    * max_connections and resource implications
    * Connection pooling with `PgBouncer`
    * pgpool-II for connection management
    * Idle session management
    * Connection timeout configuration
    * Monitoring connection usage

<!-- chapter: security, duration: 3h -->
* Security
    * `SSL`/`TLS` configuration
    * Certificate management
    * Row-level security policies
    * Column-level encryption
    * Audit logging
    * Network security and `firewall` rules
    * Security hardening checklist
    * Compliance considerations

<!-- chapter: upgrade-strategies, duration: 2h -->
* Upgrade Strategies
    * Minor version upgrades
    * Major version upgrades with pg_upgrade
    * Logical replication for zero-downtime upgrades
    * Dump and restore upgrades
    * Testing upgrades
    * Rollback planning
    * Extension compatibility

<!-- chapter: tablespaces-and-storage-management, duration: 2h -->
* Tablespaces and Storage Management
    * Tablespace creation and management
    * Moving data between tablespaces
    * Storage monitoring and capacity planning
    * Disk layout best practices
    * Managing large objects

<!-- chapter: extension-management, duration: 2h -->
* Extension Management
    * Installing and managing extensions
    * Commonly used extensions: pg_stat_statements, PostGIS, pg_trgm
    * contrib modules overview
    * Extension versioning and upgrades
    * Creating custom extensions

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
