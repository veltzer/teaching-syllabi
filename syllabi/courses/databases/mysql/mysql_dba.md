---
tags:
  - tools:mysql
  - databases:sql
  - practices:sysadmin
level: intermediate
category: database
duration_hours: 24
audience:
  - audiences:dbas
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: mysql_dba -->
# `MySQL` DBA

## Description
This course provides comprehensive training for database administrators responsible for managing `MySQL` environments in production. Participants will learn how to install, configure, secure, back up, monitor, and troubleshoot `MySQL` servers. The course covers essential DBA tasks from initial deployment through ongoing maintenance, performance tuning, and disaster recovery planning.

The course emphasizes real-world administration scenarios, including backup strategies using multiple tools, performance diagnostics via `Performance Schema` and slow query analysis, and security hardening best practices.

## Duration
24 hours / 3 days

## Intended Audience
* Database administrators managing `MySQL` instances
* System administrators responsible for database infrastructure
* `DevOps` engineers maintaining `MySQL` in production
* Infrastructure engineers supporting database platforms

## Prerequisites
* Basic `SQL` knowledge (SELECT, INSERT, UPDATE, DELETE)
* Familiarity with `Linux` command line
* Basic understanding of relational database concepts
* Experience with server administration

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Install and upgrade `MySQL` server across environments
* Manage users, roles, and privilege hierarchies
* Implement robust backup and recovery strategies
* Monitor server health and diagnose performance issues
* Configure binary logging and replication foundations
* Harden `MySQL` security posture
* Automate routine DBA tasks

## Outline
<!-- chapter: installation-and-upgrades, duration: 2h -->
* Installation and Upgrades
    * Installation methods and options
    * Initial configuration and data directory setup
    * Version upgrade strategies
    * In-place vs logical upgrades
    * Post-upgrade validation
    * Multi-instance deployments

<!-- chapter: user-management-and-privileges, duration: 3h -->
* User Management and Privileges
    * User account creation and management
    * Authentication plugins
    * Privilege system architecture
    * Global, database, and table-level privileges
    * Role-based access control
    * Revoking and auditing privileges
    * Password policies

<!-- chapter: backup-strategies, duration: 3h -->
* Backup Strategies
    * Backup planning and policies
    * Logical backups with mysqldump
    * Parallel backups with mysqlpump
    * Physical backups with `Percona XtraBackup`
    * Incremental and differential backups
    * Backup verification and testing
    * Backup automation and scheduling

<!-- chapter: point-in-time-recovery, duration: 2h -->
* Point-in-Time Recovery
    * Binary log overview
    * Point-in-time recovery workflow
    * Applying binary logs to a restored backup
    * Recovery testing procedures
    * Disaster recovery planning
    * Documenting recovery runbooks

<!-- chapter: monitoring-and-diagnostics, duration: 2h -->
* Monitoring and Diagnostics
    * `Performance Schema` overview and configuration
    * Key `Performance Schema` tables and consumers
    * sys schema views and functions
    * Monitoring connections and threads
    * Identifying resource bottlenecks
    * Third-party monitoring tools overview

<!-- chapter: slow-query-log-and-query-analysis, duration: 2h -->
* Slow Query Log and Query Analysis
    * Enabling and configuring the slow query log
    * Analyzing slow queries with mysqldumpslow
    * Query profiling techniques
    * EXPLAIN plan interpretation
    * Index recommendations
    * Query optimization strategies

<!-- chapter: server-variables-and-configuration, duration: 3h -->
* Server Variables and Configuration
    * Key server variables for performance
    * InnoDB buffer pool tuning
    * Connection and thread configuration
    * Memory allocation settings
    * Temporary table and sort buffer sizing
    * Configuration file best practices
    * Dynamic vs `static-variables`

<!-- chapter: binary-logging-and-replication-foundations, duration: 2h -->
* Binary Logging and Replication Foundations
    * Binary log formats (statement, row, mixed)
    * Binary log management and purging
    * GTID concepts
    * Replication topology overview
    * Replication monitoring
    * Common replication issues

<!-- chapter: security-hardening, duration: 3h -->
* Security Hardening
    * Secure installation procedures
    * Network security and `SSL`/`TLS` configuration
    * Audit logging
    * Data-at-`rest` encryption
    * Secure backup handling
    * Compliance considerations
    * Security assessment checklist

<!-- chapter: automation-and-operational-best-practices, duration: 2h -->
* Automation and Operational Best Practices
    * Scripting routine DBA tasks
    * Scheduled maintenance procedures
    * Capacity planning
    * Change management for database changes
    * Documentation standards
    * On-call and incident response

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
