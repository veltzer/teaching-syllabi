---
tags:
  - tools:cassandra
  - databases:nosql
  - data-and-ai:databases
  - concepts:data-modeling
level: intermediate
category: database
duration_hours: 16
audience:
  - audiences:devops
  - audiences:dbas
---
<!-- course: cassandra_administration -->
# `Cassandra` Administration

## Description
This course provides comprehensive training on administering `Apache Cassandra` clusters in production environments. Participants will learn how to manage day-to-day cluster operations, perform repairs, configure compaction strategies, and monitor cluster health. The course also covers backup and restore procedures, security hardening, multi-datacenter deployments, and performance tuning techniques essential for maintaining reliable and high-performing `Cassandra` infrastructure.

## Duration
16 hours / 2 days

## Intended Audience
* Database administrators managing `Cassandra` clusters
* `DevOps` engineers responsible for `Cassandra` infrastructure
* Site reliability engineers supporting `Cassandra` deployments
* System administrators expanding into `NoSQL` database management

## Prerequisites
* Basic understanding of `Cassandra` architecture and data model
* Familiarity with `Linux` system administration
* Command-line proficiency
* Basic networking concepts
* Understanding of distributed systems fundamentals

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Perform routine cluster operations including scaling and topology changes
* Execute and manage repair processes for data consistency
* Select and configure compaction strategies for different workloads
* Set up comprehensive monitoring and alerting for `Cassandra` clusters
* Implement backup and restore procedures for disaster recovery
* Harden `Cassandra` security with authentication, authorization, and encryption
* Design and manage multi-datacenter deployments
* Diagnose and resolve performance bottlenecks

## Outline
<!-- chapter: cluster-operations, duration: 2h -->
* Cluster Operations
    * `Cassandra` architecture review
    * nodetool command reference
    * Adding and decommissioning nodes
    * Bootstrapping new nodes
    * Token management and virtual nodes
    * Rolling restarts and upgrades
    * Seed node configuration
    * Topology changes and snitch configuration
    * `cassandra`.`yaml` key parameters
    * Operational runbooks

<!-- chapter: repair, duration: 2h -->
* Repair
    * Why repair is necessary
    * Full repair vs incremental repair
    * Subrange repairs
    * `nodetool repair` options and flags
    * Repair scheduling strategies
    * Reaper for automated repairs
    * Repair impact on cluster performance
    * Troubleshooting failed repairs
    * Anti-entropy repair internals

<!-- chapter: compaction, duration: 2h -->
* Compaction
    * Compaction overview and purpose
    * Size-tiered compaction strategy (STCS)
    * Leveled compaction strategy (LCS)
    * Time-window compaction strategy (TWCS)
    * Unified compaction strategy
    * Choosing the right strategy per table
    * Compaction throughput tuning
    * Monitoring compaction progress
    * Tombstone management and gc_grace_seconds

<!-- chapter: monitoring, duration: 2h -->
* Monitoring
    * Key `Cassandra` metrics to track
    * `JMX` metrics and MBeans
    * `Prometheus` and `Grafana` integration
    * nodetool monitoring commands
    * System table queries for diagnostics
    * Log analysis and log levels
    * Alerting strategies and thresholds
    * OpsCenter overview
    * Custom monitoring dashboards
    * Capacity planning metrics

<!-- chapter: backup-and-restore, duration: 2h -->
* Backup and Restore
    * Snapshot-based backups with `nodetool snapshot`
    * Incremental backups
    * Backup storage and retention strategies
    * Restoring from snapshots
    * Point-in-time recovery with commit logs
    * Medusa for backup automation
    * Cross-datacenter backup strategies
    * Backup validation and testing
    * Disaster recovery planning

<!-- chapter: security, duration: 2h -->
* Security
    * Authentication configuration
    * Role-based authorization
    * CQL permissions management
    * `TLS`/`SSL` for client-to-node encryption
    * `TLS`/`SSL` for node-to-node encryption
    * `JMX` security hardening
    * Audit logging
    * Network security and `firewall` rules
    * Security best practices checklist

<!-- chapter: multi-datacenter-deployments, duration: 2h -->
* Multi-Datacenter Deployments
    * Multi-datacenter architecture
    * NetworkTopologyStrategy configuration
    * Replication factor planning
    * Consistency levels across datacenters
    * DC-aware load balancing
    * Cross-datacenter latency considerations
    * Datacenter failover procedures
    * Adding a new datacenter
    * Geo-distribution patterns

<!-- chapter: performance-tuning, duration: 2h -->
* Performance Tuning
    * `JVM` and garbage collection tuning
    * Heap and off-heap memory configuration
    * Read and write path optimization
    * Disk `I/O` optimization
    * commitlog and memtable tuning
    * Bloom filter and key cache configuration
    * Thread pool tuning
    * Query tracing and slow query analysis
    * Hardware sizing recommendations
    * Benchmarking with `cassandra`-stress

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
