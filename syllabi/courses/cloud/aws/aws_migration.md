---
tags:
  - infrastructure:aws
  - infrastructure:cloud
  - concepts:migration
level: intermediate
category: cloud
duration_hours: 24
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:architects
  - audiences:devops
---
<!-- course: aws_migration -->
# Migrating to `AWS`

## Description
This course covers the strategies, tools, and best practices for migrating workloads to `AWS`. Students will learn how to plan and execute migrations of varying complexity, from simple lift-and-shift to full re-architecture. The course addresses server, database, and storage migrations using native `AWS` migration services, and covers organizational readiness including landing zone setup, cost estimation, and post-migration optimization.

## Duration
24 hours / 3 days

## Intended Audience
* Developers involved in migrating applications to `AWS`.
* System administrators planning infrastructure migrations.
* Architects designing cloud migration strategies.
* `DevOps` engineers automating migration workflows.

## Prerequisites
* Working knowledge of `AWS` core services (`EC2`, `S3`, `VPC`, `IAM`).
* Basic understanding of on-premises infrastructure (servers, databases, networking).
* Familiarity with the `AWS` Management Console and `CLI`.

## Objectives
* Evaluate and select appropriate migration strategies for different workloads.
* Use `AWS` migration tools to discover, plan, and execute migrations.
* Migrate databases using `DMS` and `SCT`.
* Transfer large-scale data using `AWS` storage migration services.
* Set up landing zones and governance for migrated workloads.
* Estimate costs and optimize workloads post-migration.

## Outline
<!-- chapter: cloud-migration-strategies, duration: 2h -->
* Cloud Migration Strategies
    * The 7 Rs of migration (rehost, replatform, repurchase, refactor, retire, retain, relocate)
    * Assessing workloads for migration readiness
    * Building a migration business case
    * Migration phases (assess, mobilize, migrate, modernize)
    * Organizational readiness and team structure
<!-- chapter: aws-migration-hub, duration: 2h -->
* `AWS Migration Hub`
    * Setting up `Migration Hub`
    * Tracking migration progress across tools
    * Application grouping and discovery
    * `Migration Hub Orchestrator`
    * Integration with partner migration tools
<!-- chapter: aws-application-discovery-service, duration: 2h -->
* `AWS Application Discovery Service`
    * Agentless discovery with the `Discovery Connector`
    * Agent-based discovery for detailed data collection
    * Dependency mapping and visualization
    * Exporting discovery data for analysis
    * Integration with `Migration Hub`
<!-- chapter: aws-application-migration-service-mgn, duration: 2h -->
* `AWS Application Migration Service` (`MGN`)
    * `MGN` architecture and replication workflow
    * Installing and configuring the replication agent
    * Launch templates and launch settings
    * Testing and cutover workflows
    * Post-launch actions and automation
    * Migrating at scale with wave planning
<!-- chapter: database-migration-with-dms-and-sct, duration: 2h -->
* Database Migration with `DMS` and `SCT`
    * `AWS Database Migration Service` architecture
    * Replication instances and endpoints
    * Homogeneous and heterogeneous migrations
    * `AWS Schema Conversion Tool` for schema transformation
    * Continuous replication and change data capture
    * Validating data migration completeness
    * Common migration scenarios (Oracle to Aurora, `SQL Server` to `PostgreSQL`)
<!-- chapter: storage-migration, duration: 2h -->
* Storage Migration
    * `AWS DataSync` for file and object transfer
    * `AWS Transfer Family` for `SFTP`, `FTPS`, and `FTP` workflows
    * `AWS Snow Family` (`Snowcone`, `Snowball`, `Snowmobile`) for large-scale transfers
    * `S3` Transfer Acceleration
    * Choosing the right storage migration method
    * Hybrid storage with `Storage Gateway`
<!-- chapter: vmware-cloud-on-aws, duration: 2h -->
* `VMware` Cloud on `AWS`
    * Architecture and use cases
    * Extending `VMware` environments to `AWS`
    * Migration using `VMware HCX`
    * Hybrid management and operations
    * Integration with native `AWS` services
<!-- chapter: re-platforming-and-re-architecting, duration: 2h -->
* Re-Platforming and Re-Architecting
    * Re-platforming strategies (containerizing, moving to managed services)
    * Re-architecting for cloud-native patterns
    * Migrating to serverless architectures
    * Breaking monoliths into `microservices`
    * Strangler fig pattern for incremental modernization
<!-- chapter: migration-at-scale, duration: 2h -->
* Migration at Scale
    * Wave planning and execution
    * Automating migration workflows
    * Parallel migration streams
    * Handling dependencies between applications
    * Communication and rollback planning
    * Migration factory approach
<!-- chapter: aws-well-architected-framework-review, duration: 2h -->
* `AWS Well-Architected Framework` Review
    * The five pillars applied to migrated workloads
    * Running a Well-Architected review
    * Identifying and prioritizing improvements
    * Common anti-patterns in migrated architectures
    * Using the `Well-Architected Tool`
<!-- chapter: landing-zones-and-aws-control-tower, duration: 2h -->
* Landing Zones and `AWS Control Tower`
    * Multi-account strategy and organizational design
    * Setting up `AWS Control Tower`
    * Account factory and account provisioning
    * Guardrails and compliance controls
    * Customizing landing zones with Account Factory for `Terraform`
    * Network architecture for landing zones
<!-- chapter: cost-estimation-and-tco-analysis, duration: 2h -->
* Cost Estimation and `TCO` Analysis
    * `AWS Pricing Calculator`
    * `TCO` comparison (on-premises vs cloud)
    * Identifying cost optimization opportunities post-migration
    * Right-sizing migrated workloads with `Compute Optimizer`
    * Reserved Instances and Savings Plans for migrated workloads
    * Tagging strategy for cost allocation

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
