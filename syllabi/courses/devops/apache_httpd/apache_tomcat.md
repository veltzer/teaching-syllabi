---
tags:
  - languages:java
  - networking:web
  - practices:sysadmin
level: intermediate
category: devops
duration_hours: 16
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: apache_tomcat -->
# `Apache Tomcat`

## Description
`Apache Tomcat` is the most widely used open-source `Java` servlet container and web server, powering countless enterprise applications. This course covers `Tomcat` architecture, configuration, deployment, security, and performance tuning. Students will learn to install and manage `Tomcat` instances, deploy web applications, configure connection pools, set up clustering, and monitor production environments.

## Duration
16 hours / 1 day

## Intended Audience
* `Java` developers deploying web applications on `Tomcat`
* System administrators managing `Tomcat` server infrastructure
* `DevOps` engineers responsible for `Tomcat` deployment and operations

## Prerequisites
* Basic `Java` and web application concepts
* Familiarity with `Linux` command line
* Understanding of `HTTP` protocol basics

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Install and configure `Apache Tomcat`
* Deploy and manage web applications
* Configure JNDI resources and `JDBC` connection pools
* Secure `Tomcat` with `SSL/TLS` and access controls
* Monitor `Tomcat` with `JMX` and logging
* Tune `Tomcat` for optimal performance

## Outline
<!-- chapter: tomcat-architecture, duration: 1h -->
* `Tomcat` Architecture
    * `Tomcat` components overview
    * Catalina (servlet container)
    * Coyote (`HTTP` connector)
    * Jasper (JSP engine)
    * Request processing pipeline
    * Class loader hierarchy
    * Directory structure
<!-- chapter: installation-and-configuration, duration: 1h -->
* Installation and Configuration
    * Installation methods
    * Environment variables (CATALINA_HOME, JAVA_HOME)
    * server.`xml` structure and elements
    * context.`xml` configuration
    * web.`xml` defaults
    * Catalina properties
    * Running as a service
<!-- chapter: connectors, duration: 1h -->
* Connectors
    * `HTTP` connector configuration
    * AJP connector and integration with `Apache HTTP Server`
    * NIO, NIO2, and APR connectors
    * Connection timeout and keep-alive settings
    * Thread pool configuration (maxThreads, minSpareThreads, acceptCount)
    * Compression settings
<!-- chapter: virtual-hosts, duration: 1h -->
* Virtual Hosts
    * Configuring virtual hosts in server.`xml`
    * Host aliases
    * Default host
    * Automatic application deployment
    * Host-specific logging
<!-- chapter: web-application-deployment, duration: 1h -->
* Web Application Deployment
    * WAR `file` structure
    * Deploying via the Manager application
    * Hot deployment and autoDeploy
    * Context configuration
    * Parallel deployment
    * Undeploy and reload
<!-- chapter: jndi-resources, duration: 1h -->
* JNDI Resources
    * JNDI overview and naming
    * Configuring resources in context.`xml` and server.`xml`
    * Resource links
    * Environment entries
    * Custom resource factories
<!-- chapter: jdbc-connection-pools, duration: 1h -->
* `JDBC` Connection Pools
    * `Tomcat` `JDBC` connection pool
    * Configuration parameters (maxActive, maxIdle, maxWait)
    * Validation queries
    * Connection leak detection
    * Abandoned connection handling
    * Pool monitoring
<!-- chapter: session-management, duration: 1h -->
* Session Management
    * Session configuration
    * Session timeout settings
    * Persistent sessions (FileStore, JDBCStore)
    * Session replication
    * Cookie configuration
    * Session serialization
<!-- chapter: clustering, duration: 1h -->
* Clustering
    * Cluster architecture
    * Multicast and static membership
    * Session replication strategies
    * DeltaManager vs BackupManager
    * Load balancing with mod_jk and mod_proxy
    * Farm deployment
<!-- chapter: ssl-tls-configuration, duration: 1h -->
* `SSL/TLS` Configuration
    * Generating keystores and certificates
    * Configuring `HTTPS` connector
    * Client certificate authentication
    * `SSL/TLS` protocol and cipher selection
    * Redirect `HTTP` to `HTTPS`
<!-- chapter: security-hardening, duration: 2h -->
* Security Hardening
    * Removing default applications
    * Security Manager
    * Realm configuration (UserDatabase, `JDBC`, `LDAP`)
    * Access restrictions by `IP`
    * `CSRF` protection
    * Security headers
    * Running as non-root user
<!-- chapter: logging, duration: 1h -->
* Logging
    * `Tomcat` logging architecture (JULI)
    * Access log valve configuration
    * Application logging
    * Log rotation
    * Integrating with Log4j2 or SLF4J
<!-- chapter: monitoring-with-jmx, duration: 1h -->
* Monitoring with `JMX`
    * Enabling `JMX` remote access
    * MBeans overview
    * Monitoring with JConsole and VisualVM
    * Key metrics to monitor
    * Health `check` endpoints
    * Integration with monitoring tools
<!-- chapter: performance-tuning, duration: 2h -->
* Performance Tuning
    * `JVM` tuning for `Tomcat` (heap size, garbage collection)
    * Connector thread pool optimization
    * Compression and caching
    * Static content serving
    * JSP compilation settings
    * Memory leak prevention
    * GC logging and analysis

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
