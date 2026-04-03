---
tags:
  - data-and-ai:data-science
  - concepts:best-practices
level: intermediate
category: big-data
duration_hours: 16
audience:
  - audiences:data-scientists
  - audiences:managers
---
<!-- course: data_governance_and_quality -->
# Data Governance and Quality

## Description
This course covers the principles and practices of data governance and data quality management for
modern data-driven organizations. Participants will learn how to establish governance frameworks,
implement data quality controls, manage metadata and lineage, and ensure compliance with regulations
such as `GDPR` and `CCPA`. The course explores tools like `Great Expectations`, `dbt` tests, and
Soda, as well as organizational models including data mesh and the roles of data stewards and
data owners.

## Duration
16 hours / 2 days

## Intended Audience
* data scientists responsible for data quality in analytical workflows
* managers overseeing data strategy and compliance

## Prerequisites
* Basic understanding of data management concepts (databases, data warehouses, data lakes)
* Familiarity with `SQL`
* Awareness of organizational data workflows
* No programming experience required

## Objectives
* **Establish a data governance program** with clear roles, policies, and organizational accountability
* **Measure and improve data quality** across accuracy, completeness, consistency, and timeliness dimensions
* **Implement data cataloging and metadata management** for data discovery and lineage tracking
* **Apply data quality tools** such as `Great Expectations`, `dbt` tests, and Soda for automated validation
* **Ensure regulatory compliance** with `GDPR`, `CCPA`, and other data protection requirements
* **Design data contracts and governance models** including data mesh principles

## Outline
<!-- chapter: data-governance-fundamentals, duration: 2h -->
* Data Governance Fundamentals
    * What is data governance
        * Definition and scope
        * Business value of governance
        * Governance vs management
    * Governance frameworks
        * DAMA-DMBOK framework
        * DGI Data Governance Framework
        * Custom framework design
    * Organizational roles
        * Data steward responsibilities
        * Data owner responsibilities
        * Data custodian responsibilities
        * Data governance council
    * Building a data governance program
        * Maturity assessment
        * Roadmap development
        * Stakeholder engagement
        * Success metrics and KPIs
<!-- chapter: data-quality-dimensions, duration: 2h -->
* Data Quality Dimensions
    * Accuracy
        * Measuring accuracy
        * Source-of-truth validation
        * Correction strategies
    * Completeness
        * `Null-value` analysis
        * Required field enforcement
        * Imputation strategies
    * Consistency
        * Cross-system consistency checks
        * Referential integrity
        * Business rule validation
    * Timeliness
        * Data freshness monitoring
        * SLA definition and tracking
        * Latency measurement
    * Additional dimensions
        * Uniqueness and deduplication
        * Validity and conformance
        * Relevance and appropriateness
<!-- chapter: data-catalogs, duration: 1h -->
* Data Catalogs
    * Catalog fundamentals
        * Purpose and benefits
        * Catalog vs data dictionary
        * Searchability and discovery
    * Catalog features
        * Automated metadata harvesting
        * Business glossary
        * Tagging and classification
        * User annotations and ratings
    * Catalog tools
        * Open-source catalogs
        * Cloud-native catalogs
        * Enterprise catalog platforms
<!-- chapter: metadata-management, duration: 1h -->
* Metadata Management
    * Metadata types
        * Technical metadata
        * Business metadata
        * Operational metadata
    * Metadata collection
        * Automated extraction
        * Manual curation
        * Metadata standards
    * Data lineage
        * Column-level lineage
        * Pipeline lineage tracking
        * Impact analysis
        * Lineage visualization
<!-- chapter: master-data-management, duration: 1h -->
* Master Data Management
    * MDM concepts
        * Master data entities
        * Golden record creation
        * Match and merge strategies
    * MDM implementation styles
        * Registry style
        * Consolidation style
        * Centralized style
        * Coexistence style
    * Reference data management
        * Code tables and lookups
        * Standardization rules
        * Cross-system synchronization
<!-- chapter: data-classification-and-sensitive-data, duration: 1h -->
* Data Classification and Sensitive Data
    * Data classification schemes
        * Sensitivity levels
        * Confidentiality categories
        * Regulatory classification
    * `PII` and sensitive data handling
        * `PII` identification and discovery
        * Data masking and anonymization
        * Pseudonymization techniques
        * Tokenization
    * Data retention and disposal
        * Retention policies
        * Archival strategies
        * Secure data destruction
<!-- chapter: data-quality-tools, duration: 2h -->
* Data Quality Tools
    * `Great Expectations`
        * Expectation suites
        * Validation and checkpoints
        * Data docs generation
        * Integration with pipelines
    * `dbt` tests
        * Schema tests
        * Custom data tests
        * Test macros and packages
        * Test result reporting
    * Soda
        * Soda checks language
        * Scan definitions
        * Anomaly detection
        * Incident management
    * Tool selection criteria
        * Integration capabilities
        * Scalability and performance
        * Community and support
<!-- chapter: data-contracts, duration: 2h -->
* Data Contracts
    * Contract fundamentals
        * What is a data contract
        * Producer and consumer agreements
        * Schema specifications
    * Contract components
        * Schema definitions
        * Quality expectations
        * SLA and freshness guarantees
        * Ownership and contact information
    * Contract enforcement
        * Automated validation
        * Breaking change detection
        * Version management
<!-- chapter: data-mesh-concepts, duration: 2h -->
* Data Mesh Concepts
    * Data mesh principles
        * Domain-oriented ownership
        * Data as a product
        * Self-serve data platform
        * Federated computational governance
    * Implementing data mesh
        * Domain identification
        * Data product design
        * Platform capabilities
        * Governance in a mesh
    * Data mesh vs traditional approaches
        * Centralized vs decentralized
        * Trade-offs and considerations
        * Migration strategies
<!-- chapter: compliance, duration: 2h -->
* Compliance
    * `GDPR`
        * Key principles and rights
        * Data subject access requests
        * Data protection impact assessments
        * Cross-border data transfers
    * `CCPA`
        * Consumer rights
        * Business obligations
        * Opt-out mechanisms
    * Other regulations
        * `HIPAA` for healthcare data
        * SOX for financial data
        * Industry-specific requirements
    * Compliance implementation
        * Privacy by design
        * Consent management
        * Audit trails and documentation
        * Breach notification procedures

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
