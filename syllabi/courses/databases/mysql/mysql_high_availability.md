---
tags:
  - tools:mysql
  - databases:sql
  - practices:sre
  - concepts:scalability
level: advanced
category: database
duration_hours: 16
audience:
  - audiences:dbas
  - audiences:sysadmins
  - audiences:devops
  - audiences:architects
---
<!-- course: mysql_high_availability -->
# `MySQL` High Availability

## Description
This advanced course covers the design and implementation of highly available `MySQL` architectures. Participants will learn to configure and manage `MySQL` replication topologies, `InnoDB Cluster`, and proxy-based routing solutions. The course addresses failover strategies, monitoring, and disaster recovery planning to ensure maximum uptime for mission-critical database workloads.

The course provides hands-on experience with modern `MySQL` HA technologies including `Group Replication`, `MySQL Router`, and ProxySQL, preparing participants to build resilient database infrastructure.

## Duration
16 hours / 2 days

## Intended Audience
* Database administrators building highly available `MySQL` deployments
* System administrators managing database infrastructure
* `DevOps` engineers automating database failover and recovery
* Architects designing resilient data tier solutions

## Prerequisites
* Experience administering `MySQL` in production environments
* Understanding of InnoDB storage engine fundamentals
* Basic networking knowledge (`TCP`/`IP`, `DNS`)
* Familiarity with `Linux` system administration

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Configure and manage asynchronous, semi-synchronous, and GTID-based replication
* Deploy `MySQL Group Replication` for automatic failover
* Set up `InnoDB Cluster` with `MySQL Shell` and `MySQL Router`
* Implement proxy-based routing with ProxySQL
* Design failover and switchover strategies
* Monitor replication health and troubleshoot issues
* Plan and execute disaster recovery procedures

## Outline
<!-- chapter: replication-fundamentals, duration: 1h -->
* Replication Fundamentals
    * Binary log formats (statement, row, mixed)
    * Asynchronous replication architecture
    * Configuring source and replica servers
    * Replication filters and channels
    * Replication lag causes and mitigation
<!-- chapter: semi-synchronous-replication, duration: 1h -->
* Semi-Synchronous Replication
    * Semi-sync replication architecture
    * Configuring semi-synchronous replication
    * Loss-less semi-synchronous replication
    * Performance implications and tuning
    * Fallback behavior to asynchronous mode
<!-- chapter: gtid-based-replication, duration: 1h -->
* GTID-Based Replication
    * Global Transaction Identifiers overview
    * Configuring GTID replication
    * GTID auto-positioning
    * Migrating from `file`-position to GTID replication
    * GTID lifecycle and purging
<!-- chapter: group-replication, duration: 1h -->
* `Group Replication`
    * `Group Replication` architecture and concepts
    * Single-primary vs multi-primary mode
    * Group communication and consensus protocol
    * Configuring `Group Replication`
    * Handling network partitions
    * Flow control mechanisms
<!-- chapter: innodb-cluster, duration: 2h -->
* `InnoDB Cluster`
    * `InnoDB Cluster` architecture
    * Deploying with `MySQL Shell`
    * Cluster management operations
    * Adding and removing instances
    * Cluster recovery and rejoin
    * `InnoDB ClusterSet` for disaster recovery
<!-- chapter: mysql-router, duration: 1h -->
* `MySQL Router`
    * `MySQL Router` architecture and routing
    * Bootstrapping `MySQL Router` with `InnoDB Cluster`
    * Read-write splitting
    * Connection routing vs classic routing
    * Monitoring and troubleshooting `MySQL Router`
<!-- chapter: proxysql, duration: 2h -->
* ProxySQL
    * ProxySQL architecture and configuration
    * Query routing rules
    * Read-write splitting with ProxySQL
    * Connection multiplexing
    * Query caching and rewriting
    * Monitoring backends and health checks
<!-- chapter: failover-strategies, duration: 2h -->
* Failover Strategies
    * Planned switchover procedures
    * Automatic failover mechanisms
    * Manual failover workflows
    * Failover testing and validation
    * Application-level failover handling
    * `DNS`-based failover approaches
<!-- chapter: read-replicas, duration: 1h -->
* Read Replicas
    * Scaling reads with replicas
    * Load balancing across replicas
    * Replica consistency considerations
    * Delayed replicas for point-in-time recovery
    * Read replica promotion
<!-- chapter: multi-source-replication, duration: 1h -->
* Multi-Source Replication
    * Multi-source replication architecture
    * Configuring multiple replication channels
    * Channel management and filtering
    * Conflict resolution considerations
    * Use cases for data aggregation
<!-- chapter: monitoring-replication-health, duration: 1h -->
* Monitoring Replication Health
    * Key replication metrics to monitor
    * `Performance Schema` replication tables
    * Monitoring replication lag
    * Alerting on replication failures
    * Tools for replication monitoring (pt-heartbeat, PMM)
<!-- chapter: backup-strategies-for-ha, duration: 1h -->
* Backup Strategies for HA
    * Backup methods compatible with HA topologies
    * `MySQL Enterprise Backup` and xtrabackup
    * Backup from replicas
    * Point-in-time recovery with binary logs
    * Backup verification and testing
<!-- chapter: disaster-recovery, duration: 1h -->
* Disaster Recovery
    * RPO and RTO planning
    * Geographic replication for DR
    * `InnoDB ClusterSet` for cross-datacenter DR
    * DR testing and runbook development
    * Recovery procedures and validation

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
