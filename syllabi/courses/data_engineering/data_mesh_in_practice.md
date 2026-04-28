---
tags:
  - concepts:data-architecture
  - concepts:data-integration
  - concepts:domain-driven-design
  - concepts:architecture
  - concepts:operations
  - concepts:best-practices
level: advanced
category: data-engineering
duration_hours: 40
audience:
  - audiences:data-engineers
  - audiences:analytics-engineers
  - audiences:data-architects
  - audiences:architects
  - audiences:team-leads
---
<!-- course: data_mesh_in_practice -->
# Data Mesh In Practice

## Description
The architecting course on data mesh in the catalog covers the philosophical model: domain ownership, data
as a product, self-serve platform, federated computational governance. This course is the implementation
companion. It is for engineers who have to ship the mesh, not just argue for it.

This five day course covers data mesh as an engineering program. It covers what a data product actually is
in code, the platform that makes data products viable for non-platform teams, contracts and federated
governance, the realistic migration story from a centralized data team to a mesh, the operational
discipline (`SLOs` for data, lineage, discovery, deprecation), the org and team-topology implications, and
the failure modes. The course is grounded in the original `Zhamak Dehghani` writing and the public
case studies from `Zalando`, `Netflix`, `Intuit`, `JPMorgan` and similar organizations.

## Duration
40 hours / 5 days

## Intended Audience
* data engineers and analytics engineers in mesh-bound organizations
* architects driving a data mesh program
* tech leads owning a domain's data products
* engineers responsible for the data platform that backs the mesh
* leaders evaluating whether to adopt mesh

## Prerequisites
* `solid` data-engineering experience
* exposure to at least one warehouse or lakehouse
* working knowledge of at least one orchestrator
* exposure to the architectural-level data-mesh material is helpful

## Objectives
* define a data product precisely and ship one
* design contracts at domain boundaries
* operate federated computational governance without ceremony
* build the self-serve platform that mesh requires
* migrate from centralized to mesh in a way that survives the transition
* recognize the cases where mesh is wrong for the organization
* avoid the most common mesh program failure modes

## Outline
<!-- chapter: what-data-mesh-actually-is, duration: 2h -->
* What data mesh actually is
    * the four principles revisited
    * what mesh is not (just decentralization, just `dbt` per team)
    * the relationship to `domain-driven design`
    * the `Zhamak Dehghani` framing
    * the cases where mesh is the right answer
    * the cases where it is not
<!-- chapter: domain-ownership-in-the-data-context, duration: 3h -->
* Domain ownership in the data context
    * mapping operational domains to data domains
    * the bounded-context-as-data-domain
    * shared-kernel data and the cross-domain product
    * cross-reference to the Event Storming course
    * the "who owns this dashboard" question
<!-- chapter: data-as-a-product, duration: 4h -->
* Data as a product
    * what a data product actually contains
    * the data product specification
    * input ports, output ports, control plane
    * the `DATSIS` characteristics: discoverable, addressable, trustworthy, self-describing, interoperable, secure
    * versioning a data product
    * publishing and deprecating
    * the data product as a `dbt` project, plus the metadata layer
<!-- chapter: data-product-contracts, duration: 3h -->
* Data product contracts
    * schema, semantics, freshness, ownership
    * cross-reference to the Data Quality and Validation course
    * `Avro`, `Protobuf`, `JSON Schema` as contracts for data
    * versioning and breaking-change discipline
    * the "consumer-driven data contract" pattern
    * automated contract enforcement in `CI`
<!-- chapter: the-self-serve-data-platform, duration: 4h -->
* The self-serve data platform
    * what the platform must provide for mesh to work
    * ingest, storage, transformation, observability, discovery, governance
    * the platform team vs the domain team
    * cross-reference to the Platform Engineering course
    * golden paths for data products
    * the data product scaffolding template
    * the cost of every domain rebuilding the same thing
<!-- chapter: the-data-product-developer-experience, duration: 2h -->
* The data product developer experience
    * the new-data-product flow
    * the time-to-first-value metric
    * the "five-minute new product" goal
    * documentation and discovery `UX`
    * data product `IDP` (`Backstage`, custom)
<!-- chapter: federated-computational-governance, duration: 3h -->
* Federated computational governance
    * the governance forum
    * what gets decided centrally vs federated
    * standards encoded as code, not as documents
    * automated policy: `OPA`, `Great Expectations`, `dbt-project-evaluator`
    * `PII` and access control across domains
    * cross-reference to the Secrets Management course's audit chapter
<!-- chapter: discovery-and-the-data-catalog, duration: 3h -->
* Discovery and the data catalog
    * the catalog as the front door
    * `DataHub`, `OpenMetadata`, `Atlan`, `Collibra`, `Amundsen`
    * the catalog and the platform `IDP`
    * search, lineage, ownership in the catalog
    * the catalog that is and is not maintained
    * cross-reference to the Internal Documentation and DevEx course
<!-- chapter: lineage-and-observability-for-mesh, duration: 3h -->
* Lineage and observability for mesh
    * column-level lineage across domains
    * `OpenLineage` for cross-team lineage
    * incident triage with multi-domain lineage
    * cross-reference to the Data Quality and Validation course
    * `SLOs` for data products
<!-- chapter: data-mesh-on-modern-warehouses-and-lakehouses, duration: 3h -->
* Data mesh on modern warehouses and lakehouses
    * `Snowflake`, `BigQuery`, `Databricks` for mesh
    * `Apache Iceberg` and `Delta Lake` as mesh substrates
    * cross-account / cross-project access patterns
    * data sharing primitives
    * the cost-control story across teams
<!-- chapter: streaming-and-the-event-driven-mesh, duration: 2h -->
* Streaming and the event-driven mesh
    * cross-reference to the Streaming Data Systems course
    * domain events as data product inputs
    * `Kafka` topic ownership in mesh
    * the relationship between operational events and data products
<!-- chapter: organizational-shape, duration: 3h -->
* Organizational shape
    * domain teams, platform team, governance forum
    * the central data team's role after mesh
    * the embedded data engineer pattern
    * `Team Topologies` for data mesh
    * the analytics-engineer role in mesh
    * staffing and seniority needed for mesh to work
<!-- chapter: migrating-from-centralized-to-mesh, duration: 3h -->
* Migrating from centralized to mesh
    * the central-data-team starting point
    * extracting one domain at a time
    * the strangler pattern for data products
    * the platform-first migration variant
    * preserving stakeholder reporting during migration
    * common reasons mesh migrations fail
<!-- chapter: anti-patterns-failure-modes-and-wrap-up, duration: 2h -->
* Anti-patterns, failure modes and wrap up
    * the mesh that is just rebranded silos
    * the platform that nobody uses
    * the governance forum that became a bottleneck
    * the "every domain reinvented the dashboard" pattern
    * the data product that nobody owns
    * the unfunded mandate
    * walkthrough of a public mesh case study
    * recommended reading: `Dehghani`, `Zalando` and `Netflix` blog posts

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
