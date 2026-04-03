---
tags:
  - infrastructure:gcp
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
<!-- course: gcp_migration -->
# Migrating to `GCP`

## Description
This course provides a comprehensive guide to planning and executing migrations to the `Google Cloud Platform`. Participants will learn migration strategies and methodologies, use `Google Cloud` migration tools for virtual machines, containers, databases, and storage, and apply best practices for application modernization. The course covers the full migration lifecycle from assessment and planning through execution and optimization, including hybrid and multi-cloud scenarios with `Anthos`.

## Duration
24 hours / 3 days

## Intended Audience
* Developers involved in migrating applications to `GCP`
* System administrators managing infrastructure migration projects
* Cloud architects designing migration strategies and landing zones
* `DevOps` engineers automating migration workflows

## Prerequisites
* Basic understanding of `GCP` core services
* Familiarity with on-premises infrastructure concepts
* Experience with virtual machines and containerization
* Understanding of database and storage fundamentals

## Objectives
* Develop a migration plan using the `Google Cloud Adoption Framework`
* Assess workloads and select appropriate migration strategies
* Migrate virtual machines using `Migrate to Virtual Machines`
* Containerize and migrate applications using `Migrate to Containers`
* Perform database migrations with `Database Migration Service` and `Datastream`
* Transfer data at scale using `Storage Transfer Service` and `Transfer Appliance`
* Design landing zones with proper resource hierarchy and governance
* Implement hybrid and multi-cloud architectures with `Anthos`
* Estimate costs and perform `TCO` analysis for migration projects

## Outline
<!-- chapter: migration-planning-and-strategies, duration: 2h -->
* Migration Planning and Strategies
    * Migration types: lift-and-shift, move-and-improve, rip-and-replace
    * Assessment and discovery of existing workloads
    * Dependency mapping and application profiling
    * Migration wave planning and prioritization
    * Risk assessment and mitigation strategies
<!-- chapter: google-cloud-adoption-framework, duration: 2h -->
* `Google Cloud Adoption Framework`
    * Framework pillars: learn, lead, scale, secure
    * Maturity phases and readiness assessment
    * Building a cloud center of excellence
    * Organizational change management
    * Governance and compliance considerations
<!-- chapter: migrate-to-virtual-machines-m2vm, duration: 2h -->
* `Migrate to Virtual Machines` (`M2VM`)
    * Architecture and components
    * Source environment preparation
    * Configuring and running migration waves
    * Testing and validation of migrated VMs
    * Cutover planning and execution
<!-- chapter: migrate-to-containers, duration: 2h -->
* `Migrate to Containers`
    * Assessing applications for containerization
    * Automated container generation
    * Migration to `GKE` and `Cloud Run`
    * Fit assessment and modernization recommendations
    * Post-migration optimization
<!-- chapter: database-migration, duration: 2h -->
* Database Migration
    * `Database Migration Service` for `MySQL`, `PostgreSQL`, and `SQL Server`
    * Continuous replication and minimal-downtime migration
    * `Datastream` for change data capture
    * Schema and data validation
    * Migration to `Cloud SQL`, `AlloyDB`, and `Cloud Spanner`
<!-- chapter: storage-transfer, duration: 2h -->
* Storage Transfer
    * `Transfer Appliance` for large-scale offline transfers
    * `Storage Transfer Service` for online transfers
    * `gsutil` for command-line data transfer
    * Transfer scheduling and bandwidth management
    * Data integrity verification
<!-- chapter: bigquery-data-transfer-service, duration: 2h -->
* `BigQuery Data Transfer Service`
    * Transferring data from `SaaS` applications
    * Cross-cloud data transfers
    * Scheduled and recurring transfers
    * Data transformation during transfer
    * Monitoring transfer runs
<!-- chapter: application-modernization, duration: 2h -->
* Application Modernization
    * Modernization patterns and decision framework
    * Refactoring monoliths to `microservices`
    * Adopting managed services and serverless
    * `API` management with `Apigee`
    * `Event-driven architecture` patterns
<!-- chapter: hybrid-and-multi-cloud-with-anthos, duration: 2h -->
* Hybrid and Multi-Cloud with `Anthos`
    * `Anthos` architecture and components
    * `Anthos` on-premises and multi-cloud deployment
    * `Anthos Config Management` for policy enforcement
    * `Anthos Service Mesh` for service networking
    * Workload migration between environments
<!-- chapter: landing-zones-and-resource-hierarchy, duration: 2h -->
* Landing Zones and Resource Hierarchy
    * Designing the resource hierarchy (organizations, folders, projects)
    * `IAM` policies and organizational constraints
    * Networking foundation and connectivity
    * Logging, monitoring, and security baselines
    * Automating landing zone deployment with `Terraform`
<!-- chapter: cost-estimation-and-tco-analysis, duration: 2h -->
* Cost Estimation and `TCO` Analysis
    * `Google Cloud Pricing Calculator`
    * Total cost of ownership methodology
    * Comparing on-premises vs. cloud costs
    * Committed use discounts and sustained use discounts
    * Cost optimization recommendations
<!-- chapter: migration-at-scale-best-practices, duration: 2h -->
* Migration at Scale Best Practices
    * Automating migration workflows
    * Parallel migration execution
    * Rollback strategies and disaster recovery
    * Performance benchmarking and validation
    * Post-migration optimization and right-sizing

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
