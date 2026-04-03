---
tags:
  - infrastructure:gcp
  - infrastructure:cloud
level: beginner
category: cloud
duration_hours: 32
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: gcp_fundamentals -->
# `GCP` Fundamentals

## Description
This course provides a comprehensive introduction to the `Google Cloud Platform` (`GCP`). Participants will gain hands-on experience with the core services and capabilities of `GCP`, including compute, storage, networking, databases, serverless, and monitoring. The course is designed to build a `solid` foundation for working with `GCP` and prepares participants for more advanced cloud topics and certification paths.

## Duration
32 hours / 4 days

## Intended Audience
* Developers looking to build and deploy applications on `GCP`
* System administrators transitioning to cloud infrastructure
* `DevOps` engineers seeking to manage cloud-based environments

## Prerequisites
* Basic understanding of networking and operating systems
* Familiarity with command-line tools
* No prior `GCP` experience is required

## Objectives
* Understand the core concepts and architecture of the `Google Cloud Platform`
* Create and manage virtual machines using `Compute Engine`
* Configure and use `Cloud Storage` for object storage needs
* Design and implement `VPC` networking with subnets, `firewall` rules, and peering
* Apply `IAM` policies and best practices for access control
* Deploy and manage relational databases with `Cloud SQL`
* Build serverless applications using `Cloud Functions`, `App Engine`, and `Cloud Run`
* Monitor infrastructure and applications using `Cloud Monitoring` and `Cloud Logging`
* Query and analyze data with `BigQuery`
* Implement event-driven architectures using Pub/Sub
* Apply deployment best practices for production workloads on `GCP`

## Outline
<!-- chapter: introduction-to-gcp, duration: 3h -->
* Introduction to `GCP`
    * What is `Cloud Computing`?
    * Overview of the `Google Cloud Platform`
    * `GCP` Global Infrastructure (Regions, Zones)
    * Navigating the `GCP Console`
    * The gcloud `CLI`
    * Resource hierarchy: Organizations, Folders, Projects
<!-- chapter: compute-engine, duration: 3h -->
* `Compute Engine`
    * Creating and managing virtual machines
    * Machine types and custom configurations
    * Persistent disks and snapshots
    * Instance groups and autoscaling
    * Preemptible and spot VMs
    * Startup scripts and metadata
<!-- chapter: cloud-storage, duration: 3h -->
* `Cloud Storage`
    * Storage classes (Standard, Nearline, Coldline, Archive)
    * Buckets and objects
    * Access control and signed URLs
    * Lifecycle management policies
    * Versioning and retention
    * Transfer tools and strategies
<!-- chapter: vpc-networking, duration: 3h -->
* `VPC` Networking
    * `Virtual Private Cloud` concepts
    * Subnets and `IP` addressing
    * `Firewall` rules and network tags
    * Cloud `NAT` and `Cloud Router`
    * `VPC` peering and Shared `VPC`
    * Load balancing options
<!-- chapter: identity-and-access-management-iam, duration: 2h -->
* Identity and Access Management (`IAM`)
    * `IAM` roles and permissions
    * Service accounts and keys
    * Resource-level policies
    * Organization policies and constraints
    * Best practices for least privilege
<!-- chapter: cloud-sql, duration: 2h -->
* `Cloud SQL`
    * Supported database engines (`MySQL`, `PostgreSQL`, `SQL Server`)
    * Creating and configuring instances
    * High availability and failover
    * Backups and point-in-time recovery
    * Connecting from applications and `Compute Engine`
<!-- chapter: cloud-functions, duration: 2h -->
* `Cloud Functions`
    * Introduction to serverless computing
    * Writing and deploying functions
    * Event triggers (`HTTP`, Pub/Sub, `Cloud Storage`)
    * Environment variables and secrets
    * Monitoring and debugging functions
<!-- chapter: app-engine, duration: 2h -->
* `App Engine`
    * Standard vs. Flexible environments
    * Deploying applications
    * Versioning and traffic splitting
    * Scaling configurations
    * Working with app.`yaml`
<!-- chapter: cloud-run, duration: 2h -->
* `Cloud Run`
    * Container-based serverless computing
    * Building and deploying containers
    * Configuring concurrency and scaling
    * Custom domains and `HTTPS`
    * Integrating with other `GCP` services
<!-- chapter: cloud-monitoring-and-cloud-logging, duration: 3h -->
* `Cloud Monitoring` and `Cloud Logging`
    * Setting up monitoring dashboards
    * Creating alerting policies
    * Working with metrics and uptime checks
    * Log collection and log-based metrics
    * Log sinks and exports
    * Error Reporting integration
<!-- chapter: introduction-to-bigquery, duration: 2h -->
* Introduction to `BigQuery`
    * `BigQuery` architecture and concepts
    * Loading and querying data
    * `SQL` syntax in `BigQuery`
    * Partitioned and clustered tables
    * Cost management and best practices
<!-- chapter: pub-sub, duration: 2h -->
* Pub/Sub
    * Publish/subscribe messaging model
    * Topics and subscriptions
    * Push vs. pull delivery
    * Message ordering and deduplication
    * Integration with `Cloud Functions` and Dataflow
<!-- chapter: deployment-best-practices, duration: 3h -->
* Deployment Best Practices
    * Infrastructure as Code with `Deployment Manager` and `Terraform`
    * `CI/CD` pipelines with `Cloud Build`
    * Environment management (dev, staging, production)
    * Cost optimization strategies
    * Security hardening and compliance
    * The `Google Cloud` Well-Architected Framework

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
