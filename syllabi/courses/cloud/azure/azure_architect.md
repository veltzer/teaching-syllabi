---
tags:
  - infrastructure:azure
  - infrastructure:cloud
  - concepts:architecture
  - concepts:scalability
level: advanced
category: cloud
duration_hours: 40
audience:
  - audiences:architects
  - audiences:developers
  - audiences:devops
---
<!-- course: azure_architect -->
# `Azure` Solutions Architect

## Description
This advanced course prepares participants to design comprehensive solutions on `Microsoft Azure` following the `Azure Well-Architected Framework`. Participants will learn to `make` informed architectural decisions across compute, data, networking, identity, and security domains. The course covers real-world `design patterns`, migration strategies, governance at scale, and cost optimization, equipping architects with the knowledge to build reliable, secure, and performant cloud solutions.

## Duration
40 hours / 5 days

## Intended Audience
* Architects designing enterprise-scale `Azure` solutions
* Senior developers making architectural decisions on `Azure`
* `DevOps` engineers involved in infrastructure design and automation

## Prerequisites
* Hands-on experience with `Azure` services (compute, storage, networking)
* Understanding of identity and security concepts in `Azure`
* Familiarity with infrastructure as code (`ARM` templates, `Bicep`, or `Terraform`)
* Experience with application development patterns (`microservices`, APIs)

## Objectives
* Apply the `Azure Well-Architected Framework` pillars to solution design
* Design identity architectures using `Microsoft Entra ID`
* Select appropriate compute, data, and networking services for given requirements
* Architect highly available and disaster-resilient solutions
* Plan migration and modernization strategies for existing workloads
* Implement governance and cost management at enterprise scale

## Outline
<!-- chapter: azure-well-architected-framework, duration: 4h -->
* `Azure Well-Architected Framework`
    * Reliability pillar (fault tolerance, recovery, testing)
    * Security pillar (defense in depth, zero trust)
    * Cost optimization pillar (right-sizing, reserved instances, budgets)
    * Operational excellence pillar (automation, monitoring, `DevOps`)
    * Performance efficiency pillar (scaling, caching, partitioning)
    * Well-Architected Review process
    * Trade-offs between pillars
<!-- chapter: identity-architecture, duration: 4h -->
* Identity Architecture
    * `Microsoft Entra ID` tenant design
    * `Azure AD B2C` for customer-facing applications
    * Federation with external identity providers
    * Hybrid identity (password hash sync, pass-through authentication, `AD FS`)
    * Privileged Identity Management
    * Conditional Access architecture
    * Workload identities and `Managed Identities`
<!-- chapter: compute-architecture, duration: 4h -->
* Compute Architecture
    * Virtual machines (sizing, availability, placement groups)
    * `Azure App Service` (plans, scaling, networking integration)
    * `Azure Functions` (hosting plans, `durable functions`, triggers)
    * `Azure Container Apps` (`microservices`, Dapr, scaling rules)
    * `Azure Kubernetes Service` (cluster design, networking, storage)
    * Compute decision framework (`when` to use what)
    * Hybrid compute with `Azure Arc`
<!-- chapter: data-architecture, duration: 4h -->
* Data Architecture
    * `Azure SQL Database` (DTU vs. vCore, elastic pools, Hyperscale)
    * `Azure Cosmos DB` (`API` selection, partitioning, consistency levels)
    * Storage accounts (blob, `file`, table, queue, Data Lake)
    * Caching strategies with `Azure Cache for Redis`
    * Data residency and sovereignty requirements
    * Polyglot persistence patterns
    * Database migration strategies
<!-- chapter: networking-design, duration: 4h -->
* Networking Design
    * Hub-spoke topology design
    * `Azure Virtual WAN` architecture
    * `ExpressRoute` design and redundancy
    * Network segmentation and micro-segmentation
    * `DNS` architecture (public, private, hybrid)
    * Load balancing decision tree
    * Network security architecture (`Firewall`, NSGs, `WAF`)
    * Private connectivity to PaaS services
<!-- chapter: application-architecture-patterns, duration: 4h -->
* Application Architecture Patterns
    * `Microservices` architecture on `Azure`
    * `Event-driven architecture` (`Event Grid`, `Event Hubs`, `Service Bus`)
    * `CQRS` and `event sourcing` patterns
    * `API` management and gateway patterns
    * Asynchronous messaging and queue-based load leveling
    * `Saga` pattern for distributed transactions
    * Sidecar and ambassador patterns
<!-- chapter: high-availability-and-disaster-recovery, duration: 4h -->
* High Availability and Disaster Recovery
    * Availability zones and region pairs
    * Multi-region deployment patterns (active-active, active-passive)
    * `Azure Site Recovery` and replication strategies
    * Backup strategies and retention policies
    * RPO and RTO planning
    * Chaos engineering and failure injection
    * Health modeling and self-healing architectures
<!-- chapter: migration-and-modernization, duration: 4h -->
* Migration and Modernization
    * Assessment and discovery tools
    * Migration strategies (rehost, refactor, rearchitect, rebuild)
    * `Azure Migrate` for server and database migration
    * Application modernization paths
    * Strangler fig pattern for incremental migration
    * Data migration approaches and tools
<!-- chapter: governance-at-scale, duration: 4h -->
* Governance at Scale
    * Management Group hierarchy design
    * `Azure Policy` for enterprise compliance
    * `Azure Blueprints` for environment standardization
    * Landing zone architecture
    * Subscription design and resource organization
    * Tagging strategy and naming conventions
    * Regulatory compliance frameworks
<!-- chapter: cost-management-and-optimization, duration: 4h -->
* Cost Management and Optimization
    * `Azure Cost Management` and budgets
    * Reserved instances and savings plans
    * Spot VMs for fault-tolerant workloads
    * Right-sizing recommendations
    * Storage cost optimization (tiering, lifecycle policies)
    * FinOps practices and culture
    * Cost allocation and chargeback models

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
