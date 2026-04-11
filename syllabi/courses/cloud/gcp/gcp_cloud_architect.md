---
tags:
  - infrastructure:cloud
  - infrastructure:gcp
  - security:iam
  - security:encryption
  - concepts:scalability
  - concepts:architecture
  - concepts:microservices
  - concepts:distributed-systems
  - infrastructure:containers
  - infrastructure:kubernetes
level: advanced
category: cloud
duration_hours: 40
audience:
  - audiences:architects
  - audiences:devops
  - audiences:team-leads
---
<!-- course: gcp_cloud_architect -->
# `Google Cloud Platform` - Cloud Architect

## Description
This advanced course teaches participants how to design, plan, and manage solutions on
`Google Cloud Platform`. It covers enterprise-grade architecture patterns including high
availability, disaster recovery, security, and compliance. Participants will learn to
evaluate trade-offs between cost, performance, and reliability, and apply the `GCP`
Well-Architected Framework to real-world scenarios. The course is aligned with the
Professional Cloud Architect certification path.

## Duration
40 hours / 5 days

## Intended Audience
* Cloud architects designing systems on `GCP`
* Senior engineers responsible for infrastructure decisions
* Technical leads evaluating cloud migration strategies
* Solutions architects who need to design enterprise-grade cloud solutions

## Prerequisites
* Working experience with `GCP` core services or equivalent cloud platform
* Understanding of networking, storage, and compute fundamentals
* Experience with distributed systems and multi-tier architectures
* Familiarity with `IAM`, security, and compliance concepts

## Objectives
* Design cloud solutions using the `GCP` Well-Architected Framework
* Plan and execute cloud migrations
* Architect highly available, scalable, and secure systems
* Design data processing, storage, and analytics solutions
* Implement governance, compliance, and cost management strategies

## Outline
<!-- chapter: solution-design-and-planning, duration: 3h -->
* Solution Design and Planning
    * Business requirements analysis: use cases, `KPI`s, and `ROI`
    * Technical requirements: availability, scalability, latency, and compliance
    * `GCP` Well-Architected Framework
    * Cost optimization strategies: CapEx vs OpEx
    * `Gemini` Cloud Assist for architecture guidance
<!-- chapter: compute-architecture, duration: 4h -->
* Compute Architecture
    * `Compute Engine`: machine types, Spot VMs, sole-tenant nodes
    * `GKE`: Autopilot, Standard, and multi-cluster architectures
    * `Cloud Run` and serverless patterns
    * `Cloud Run` functions for event-driven compute
    * `VMware` Engine for hybrid workloads
    * Choosing the right compute service
<!-- chapter: network-design, duration: 5h -->
* Network Design
    * `VPC` design: shared `VPC` and multi-project networking
    * Hybrid networking: Cloud `VPN`, `Cloud Interconnect`, and Partner Interconnect
    * `Private Service Connect` and `VPC` Service Controls
    * Global and regional load balancing
    * Cloud `CDN` and media `CDN`
    * `Cloud Armor` for `DDoS` protection and `WAF`
    * Network security: `Firewall` policies, hierarchical rules
    * `DNS` architecture with Cloud `DNS`
<!-- chapter: storage-and-database-design, duration: 5h -->
* Storage and Database Design
    * Storage selection by access pattern, volume, and performance
    * `Cloud Storage` for object storage and data lakes
    * Block and `file` storage: Persistent Disk, Filestore, NetApp Volumes
    * Cloud `SQL`, `AlloyDB`, and `Cloud Spanner` for relational workloads
    * `Firestore` and Bigtable for `NoSQL` workloads
    * `BigQuery` for analytics and data warehousing
    * Data lifecycle management and retention policies
<!-- chapter: data-processing-and-analytics, duration: 4h -->
* Data Processing and Analytics
    * Dataflow for stream and batch processing
    * Dataproc for `Hadoop` and `Spark` workloads
    * Pub/Sub for messaging and event streaming
    * `BigQuery` for analytics: partitioning, clustering, and materialized views
    * Looker and Looker Studio for visualization
    * Data governance with Dataplex
<!-- chapter: ai-and-machine-learning, duration: 3h -->
* `AI` and `Machine Learning`
    * Vertex `AI` for model training and serving
    * Pre-built `AI` `API`s: Vision, Language, Translation, Speech
    * `BigQuery` `ML` for in-database `machine learning`
    * `Gemini` models and `AI` agents
    * `AI` Hypercomputer for large-scale training
<!-- chapter: security-and-compliance, duration: 5h -->
* Security and Compliance
    * `IAM` design: resource hierarchy and policy inheritance
    * Data security: Cloud `KMS`, encryption, and key management
    * `VPC` Service Controls and context-aware access
    * `Security Command Center`
    * `Identity-Aware Proxy`
    * `Binary Authorization` for container supply chain
    * Compliance frameworks: `SOC` 2, `GDPR`, `HIPAA`
    * Data residency and sovereignty
<!-- chapter: migration-planning, duration: 4h -->
* Migration Planning
    * Migration methodologies: lift-and-shift, re-platform, re-architect
    * Migration Center for assessment and planning
    * Database Migration Service
    * Transfer Service for large-scale data migration
    * Network and licensing considerations
    * Testing and validation strategies
<!-- chapter: high-availability-and-disaster-recovery, duration: 3h -->
* High Availability and Disaster Recovery
    * Multi-zonal and multi-regional architectures
    * `RPO` and `RTO` planning
    * Backup and recovery strategies for compute, storage, and databases
    * Chaos engineering and failure testing
    * Global load balancing for failover
<!-- chapter: operations-and-cost-management, duration: 4h -->
* Operations and Cost Management
    * `Cloud Monitoring` and `Cloud Logging` at scale
    * Service catalog and deployment automation
    * FinOps: committed-use and sustained-use discounts
    * Active Assist recommendations
    * Resource labeling and cost allocation

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
