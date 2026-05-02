---
tags:
  - concepts:architecture
  - data-and-ai:data-engineering
  - concepts:distributed-systems
level: advanced
category: architecture
duration_hours: 16
audience:
  - audiences:architects
  - audiences:data-engineers
  - audiences:team-leads
  - audiences:managers
---
<!-- course: data_mesh -->
# Data Mesh

## Description
This course provides a comprehensive exploration of the data mesh paradigm, a decentralized approach to data architecture and organizational design. Participants will learn the four core principles of data mesh: domain-oriented data ownership, data as a product, self-serve data platform, and federated computational governance. The course covers practical aspects of designing data products, establishing data contracts, ensuring data quality, driving organizational change, and building platform engineering capabilities for data. Comparisons with traditional data lake and data warehouse approaches provide context for adoption decisions.

## Duration
16 hours / 2 days

## Intended Audience
* Software and data architects evaluating decentralized data architectures
* Data engineers building and operating data platforms
* Technical leads overseeing data strategy and data team structures
* Engineering managers responsible for data-related organizational decisions

## Prerequisites
* Experience with data architecture and data infrastructure
* Understanding of distributed systems concepts
* Familiarity with data warehousing and data lake concepts

## Objectives
* Articulate the four core principles of data mesh and their rationale
* Design domain-oriented data ownership structures aligned with business domains
* Define and build data products with clear interfaces and quality guarantees
* Architect a self-serve data platform that enables domain teams to own their data
* Establish federated computational governance policies and standards
* Create data contracts that formalize agreements between data producers and consumers
* Compare data mesh with data lake and data warehouse architectures
* Plan and execute organizational change for data mesh adoption

## Outline
<!-- chapter: introduction-to-data-mesh, duration: 1h -->
* Introduction to Data Mesh
    * The challenges of centralized data architectures
    * Monolithic data platforms and their limitations
    * The origins and motivation of the data mesh paradigm
    * Overview of the four core principles
    * `When` data mesh is appropriate and when it is not
<!-- chapter: domain-oriented-data-ownership, duration: 1h -->
* Domain-Oriented Data Ownership
    * Decomposing data along business domain boundaries
    * Identifying domain data owners and their responsibilities
    * Aligning data ownership with `domain-driven design` concepts
    * Cross-domain data dependencies and relationships
    * Avoiding data silos while enabling domain autonomy
    * Team topologies for domain data ownership
<!-- chapter: data-as-a-product, duration: 2h -->
* Data as a Product
    * Defining a data product and its characteristics
    * Data product thinking: usability, reliability, and discoverability
    * Data product interfaces: APIs, events, and datasets
    * Data product lifecycle management
    * Versioning data products
    * Documentation and discoverability standards
    * Measuring data product success and adoption
<!-- chapter: self-serve-data-platform, duration: 2h -->
* Self-Serve Data Platform
    * The role of the platform in enabling domain teams
    * Platform capabilities: storage, compute, ingestion, and delivery
    * Infrastructure as code for data products
    * Developer experience and self-service tooling
    * Data product templates and golden paths
    * Monitoring, observability, and alerting for data products
    * Platform team structure and responsibilities
<!-- chapter: federated-computational-governance, duration: 2h -->
* Federated Computational Governance
    * The need for governance in decentralized architectures
    * Federated governance model: global policies with local autonomy
    * Computational governance: encoding policies as code
    * Interoperability standards and cross-domain compatibility
    * Security and access control policies
    * Compliance and regulatory considerations
    * Governance automation and enforcement mechanisms
<!-- chapter: data-contracts, duration: 2h -->
* Data Contracts
    * What are data contracts and why they matter
    * Defining schema contracts between producers and consumers
    * Semantic contracts and business meaning
    * Service-level agreements for data quality and freshness
    * Contract testing and validation
    * Breaking changes and contract evolution
    * Tooling for data contract management
<!-- chapter: data-quality, duration: 1h -->
* Data Quality
    * Data quality dimensions: accuracy, completeness, timeliness, and consistency
    * Data quality ownership in a decentralized model
    * Quality checks and validation at the source
    * Data quality monitoring and alerting
    * Data lineage and impact analysis
    * Handling data quality incidents and remediation
<!-- chapter: comparison-with-data-lake-and-data-warehouse, duration: 1h -->
* Comparison with Data Lake and Data Warehouse
    * Traditional data warehouse architecture and trade-offs
    * Data lake architecture and challenges
    * Data lakehouse as a hybrid approach
    * How data mesh differs from and complements these architectures
    * Migration paths from centralized to decentralized data architectures
    * Hybrid approaches and coexistence strategies
<!-- chapter: organizational-change-for-data-mesh, duration: 2h -->
* Organizational Change for Data Mesh
    * Assessing organizational readiness for data mesh
    * Cultural shifts: from centralized data teams to embedded data ownership
    * Change management strategies and stakeholder alignment
    * Incremental adoption and pilot programs
    * Measuring progress and demonstrating value
    * Common pitfalls and lessons learned from data mesh implementations
<!-- chapter: implementation-strategies, duration: 2h -->
* Implementation Strategies
    * Starting with a data mesh pilot: selecting initial domains
    * Building the minimum viable data platform
    * Iterating on governance policies based on real-world experience
    * Scaling data mesh across the organization
    * Technology choices and vendor landscape
    * Maturity model for data mesh adoption

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
