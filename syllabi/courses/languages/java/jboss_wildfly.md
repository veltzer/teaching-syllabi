---
tags:
  - languages:java
  - practices:sysadmin
  - networking:web
level: intermediate
category: language
duration_hours: 16
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: jboss_wildfly -->
# JBoss/WildFly Administration

## Description
This course covers the administration and management of JBoss/WildFly application servers. Students will learn the architecture of WildFly, how to install and configure it in standalone and domain modes, deploy applications, configure datasources and `JMS`, set up clustering and session replication, manage security, and tune performance. The course prepares administrators and developers to run production-grade `Java EE` environments.

## Duration
16 hours / 2 days

## Intended Audience
* `Java` developers deploying applications to WildFly or `JBoss EAP`
* System administrators managing `Java` application server infrastructure
* `DevOps` engineers responsible for `Java EE` application environments

## Prerequisites
* Basic `Java` and `Java EE` concepts
* Familiarity with `Linux` or `Windows` server administration
* Understanding of networking fundamentals (`TCP`/`IP`, `HTTP`)
* Basic command-line proficiency

## Required Knowledge
* `Java` Programming (or equivalent experience)
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Understand the WildFly architecture and subsystem model
* Install and configure WildFly in standalone and domain modes
* Deploy and manage `Java EE` applications
* Configure datasources, `JMS`, and other subsystems
* Set up clustering and high availability with session replication
* Secure the application server and deployed applications
* Monitor and tune WildFly for production performance

## Outline
<!-- chapter: introduction-to-jboss-wildfly, duration: 1h -->
* Introduction to JBoss/WildFly
    * History: from JBoss to WildFly
    * WildFly vs `JBoss EAP`
    * `Java EE` and `Jakarta EE` standards support
    * Architecture overview and subsystem model
<!-- chapter: installation-and-configuration, duration: 1h -->
* Installation and Configuration
    * Downloading and installing WildFly
    * Directory structure and key files
    * Configuration files: standalone.`xml` and domain.`xml`
    * Management interfaces: `CLI`, web console, and `REST API`
    * Environment variables and system properties
<!-- chapter: domain-vs-standalone-mode, duration: 1h -->
* Domain vs Standalone Mode
    * Standalone mode: `when` and how to use
    * Domain mode architecture
    * Domain controller and host controllers
    * Server groups and server instances
    * Managing multiple servers from a single point
    * Choosing between modes
<!-- chapter: deployment, duration: 1h -->
* Deployment
    * Deployment methods: `CLI`, web console, filesystem scanner
    * Deploying WAR, EAR, and JAR archives
    * Deployment overlays
    * Managed and unmanaged deployments
    * Rolling deployments in domain mode
    * Exploded deployments
<!-- chapter: datasource-configuration, duration: 1h -->
* Datasource Configuration
    * `JDBC` driver installation as modules
    * Configuring datasources
    * Connection pool settings
    * XA datasources
    * Datasource testing and validation
    * Connection pool monitoring
<!-- chapter: jms-configuration, duration: 1h -->
* `JMS` Configuration
    * `ActiveMQ Artemis` embedded messaging
    * Configuring queues and topics
    * Connection factories
    * Message persistence and journaling
    * Dead letter and expiry queues
    * Remote `JMS` clients
<!-- chapter: clustering, duration: 1h -->
* Clustering
    * Clustering architecture in WildFly
    * JGroups and cluster communication
    * Cluster discovery mechanisms
    * Infinispan cache configuration
    * Load balancing with mod_cluster
    * Failover and high availability
<!-- chapter: session-replication, duration: 1h -->
* Session Replication
    * `HTTP` session replication setup
    * Distributable web applications
    * Session affinity and sticky sessions
    * Fine-grained replication strategies
    * Session passivation and persistence
<!-- chapter: security-subsystem, duration: 2h -->
* Security Subsystem
    * Elytron security framework
    * Security domains and realms
    * Authentication mechanisms
    * Role-based access control (`RBAC`) for management
    * `SSL/TLS` configuration
    * Securing the management interfaces
    * Application security with Elytron
<!-- chapter: logging, duration: 2h -->
* Logging
    * Logging subsystem architecture
    * Log categories and handlers
    * `File`, console, and periodic rotating handlers
    * Per-deployment logging configuration
    * Log formatters and filters
    * Integrating with external logging frameworks
<!-- chapter: monitoring, duration: 2h -->
* Monitoring
    * Management `CLI` for runtime metrics
    * Web console dashboards
    * `JMX` and MBean access
    * Health and readiness checks
    * Integration with `Prometheus` and `Grafana`
    * Alerting strategies
<!-- chapter: performance-tuning, duration: 2h -->
* Performance Tuning
    * `JVM` settings and garbage collector tuning
    * Thread pool configuration
    * Connection pool optimization
    * Undertow web server tuning
    * Buffer sizes and IO worker threads
    * Profiling and identifying bottlenecks
    * Capacity planning considerations

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
