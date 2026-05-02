---
tags:
  - concepts:data-architecture
  - concepts:best-practices
  - concepts:operations
  - concepts:data-modeling
level: intermediate
category: data-engineering
duration_hours: 16
audience:
  - audiences:data-engineers
  - audiences:senior-developers
  - audiences:architects
  - audiences:data-architects
---
<!-- course: data_contracts -->
# Data Contracts

## Description
A `data contract` is the agreement between the producer of data and the consumer of data: schema, semantics,
quality guarantees, ownership, and the way changes happen. The catalog has `Data Mesh`, `Data Mesh in
Practice`, `Data Quality and Validation`, `Data Modeling in Depth`, and `Data Governance and Quality`.
None of those covers the focused engineering of a data contract — the `API`-style interface that makes
data products predictable. Without contracts, an upstream column rename silently breaks five
downstream dashboards and three `ML` features at three in the morning.

This two day course covers data contracts as a working engineering practice. It covers the contract as
an artefact (schema, semantics, freshness, quality, owner, breaking-change policy), the contract
languages (`Protobuf`, `Avro`, `JSON Schema`, `dbt` contracts, `Open Data Contract Standard`), the
producer-side enforcement (the `CI` check, the schema registry), the consumer-side enforcement (the
contract test, the alert), the relationship to data mesh and data products, the change-management
story, the breaking-change procedure, the observability story, and the patterns that `make` contracts
succeed. Examples are drawn from the public engineering writing of `GoCardless`, Convoy, `Shopify`,
`Glovo`, and the open-source `Data Contract CLI` ecosystem. Participants leave able to introduce data
contracts into an organization and operate them without slowing the team down.

## Duration
16 hours / 2 days

## Intended Audience
* data engineers introducing contracts to their pipelines
* senior developers producing data that another team consumes
* architects designing data interfaces
* data architects rolling out data mesh

## Prerequisites
* working data-engineering experience
* exposure to the Data Mesh in Practice course
* familiarity with at least one schema-evolution system
* basic understanding of `CI/CD`

## Objectives
* explain what belongs in a data contract
* express a contract in a chosen language
* enforce contracts on the producer side
* enforce contracts on the consumer side
* manage contract change without breaking downstreams
* recognize when contracts are over-engineered
* connect contracts to data mesh and data products

## Outline
<!-- chapter: what-a-data-contract-is, duration: 1h -->
* What a data contract is
    * the analogy to an `API` contract
    * what belongs in it
    * what does not belong in it
    * cross-reference to the Data Mesh in Practice course
    * the canonical incident that contracts prevent
<!-- chapter: the-anatomy-of-a-contract, duration: 2h -->
* The anatomy of a contract
    * schema: shape and types
    * semantics: what each field means
    * quality: validity, completeness, accuracy
    * freshness: when it lands and when it is current
    * owner: a real human
    * breaking-change policy
<!-- chapter: contract-languages, duration: 2h -->
* Contract languages
    * `Protobuf` and `Avro` for streaming
    * `JSON Schema` for documents
    * `dbt` model contracts for warehouse
    * `Open Data Contract Standard` (`ODCS`)
    * `Datacontract CLI`
    * picking the language
<!-- chapter: producer-side-enforcement, duration: 2h -->
* Producer-side enforcement
    * the `CI` check on schema change
    * the schema registry as the gatekeeper
    * the breaking-change rejection
    * the producer's `unit` test against the contract
    * the "we shipped a breaking change because the gate was off" failure
<!-- chapter: consumer-side-enforcement, duration: 2h -->
* Consumer-side enforcement
    * the contract test in the consumer pipeline
    * the alert when expected fields are missing
    * `Great Expectations` and `Soda` for downstream checks
    * cross-reference to the Data Quality and Validation course
    * the "the consumer silently used `null` for a missing field" failure
<!-- chapter: changes-and-versioning, duration: 2h -->
* Changes and versioning
    * additive vs breaking
    * the `v1`/`v2` parallel-publish strategy
    * the deprecation timeline
    * the consumer-migration tracking
    * cross-reference to the `API` Evolution and Versioning course
<!-- chapter: contracts-and-data-mesh, duration: 1h -->
* Contracts and data mesh
    * the data product as a contracted thing
    * the federated computational governance
    * cross-reference to the Data Mesh course
    * the "we have a mesh and no contracts" failure
    * the "we have contracts and no mesh" failure
<!-- chapter: observability-of-contracts, duration: 1h -->
* Observability of contracts
    * the contract-violation metric
    * the contract-coverage metric
    * the breaking-change attempt rate
    * the per-product health dashboard
    * the "we cannot tell if our contracts work" reality
<!-- chapter: organizational-patterns, duration: 1h -->
* Organizational patterns
    * the contract owner
    * the contract review
    * the cross-team contract negotiation
    * the "the platform team writes everyone's contracts" failure
    * the federated approach
<!-- chapter: rollout-strategy, duration: 1h -->
* Rollout strategy
    * starting with one critical pipeline
    * the priority-based rollout
    * the "boil-the-ocean" anti-pattern
    * the contract registry as the source of truth
    * iterating
<!-- chapter: case-studies, duration: 1h -->
* Case studies
    * `GoCardless` and `Glovo` writeups
    * `Convoy`'s data contract program
    * `Shopify`'s contract approach
    * the failed program and what went wrong
    * recommended reading: `Data Contracts` ecosystem

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
