---
tags:
  - concepts:data-architecture
  - concepts:data-modeling
  - concepts:testing
  - concepts:observability
  - concepts:best-practices
  - concepts:operations
level: intermediate
category: data-engineering
duration_hours: 40
audience:
  - audiences:data-engineers
  - audiences:analytics-engineers
  - audiences:developers
  - audiences:data-architects
  - audiences:architects
---
<!-- course: data_quality_and_validation -->
# Data Quality and Validation

## Description
Bad data ships silently. A pipeline that runs to completion every night and writes a `clean`-looking row count
into a destination table can be quietly wrong for months before anybody downstream notices. By that point the
mistakes are baked into reports, models, and customer communications, and the cost of repair dwarfs the cost
that disciplined validation would have imposed up front.

This five day course covers data quality and validation as engineering disciplines. It covers the dimensions
of data quality (accuracy, completeness, freshness, validity, uniqueness, consistency), the data-contract
pattern, schema and value-level validation, the major tools (`Great Expectations`, `Soda`, `dbt tests`,
`Monte Carlo`, `Datafold`, `Elementary`), `SLOs` for data, and the operational practices that turn data quality
from "we should do that someday" into a continuous, observable property of the data platform. Examples are
drawn from analytical, operational and `ML` data systems.

## Duration
40 hours / 5 days

## Intended Audience
* data engineers building or maintaining production pipelines
* analytics engineers responsible for trusted data models
* `ML` engineers whose models depend on input data quality
* data architects designing data platforms with quality as a property
* engineers responding to a "the data is wrong" incident

## Prerequisites
* working knowledge of `SQL` and at least one analytical store
* basic familiarity with at least one `ETL`/`ELT` tool
* exposure to a workflow orchestrator (`Airflow`, `Dagster`, `Prefect`)
* some experience operating data pipelines in production

## Objectives
* enumerate the dimensions of data quality and define each precisely
* design data contracts between producers and consumers
* implement schema-, value- and statistical-level validation
* operate data-quality tooling at scale
* set `SLOs` for data and alert against them
* respond to a data-quality incident
* embed data quality into the development workflow rather than bolt it on

## Outline
<!-- chapter: why-data-quality-fails-silently, duration: 2h -->
* Why data quality fails silently
    * the absence of failures as evidence of correctness, falsely
    * the long latency between bad data and detection
    * cost of a `BI` dashboard built on bad data
    * cost of an `ML` model built on bad data
    * organizational incentives that keep quality low
    * what good looks like
<!-- chapter: dimensions-of-data-quality, duration: 3h -->
* Dimensions of data quality
    * accuracy
    * completeness
    * freshness and timeliness
    * validity
    * uniqueness
    * consistency
    * lineage and provenance
    * conformance to business rules
    * how to measure each
<!-- chapter: data-contracts, duration: 4h -->
* Data contracts
    * the contract between producer and consumer
    * schema, semantics, freshness, ownership
    * `Avro`, `Protobuf`, `JSON Schema` for contracts
    * versioning and breaking-change discipline
    * who owns the contract: producer, consumer, or platform
    * `Confluent`/`Apache Schema Registry`, `Buf`, custom registries
    * contracts at the operational, analytical and `ML` boundaries
<!-- chapter: schema-validation, duration: 2h -->
* Schema validation
    * structural validation: shape, types, required fields
    * automatic schema inference and its dangers
    * runtime validation in pipelines
    * schema validation in messaging (`Kafka` schema registry)
    * schema validation in analytical loads
    * the cost of strict vs lax schemas
<!-- chapter: value-and-business-rule-validation, duration: 3h -->
* Value and business-rule validation
    * range checks, regex, enum membership
    * referential integrity outside the database
    * business invariants ("revenue is always non-negative")
    * cross-row and cross-table checks
    * `temporal` invariants ("created_at <= updated_at")
    * value distribution drift
<!-- chapter: statistical-and-anomaly-detection, duration: 3h -->
* Statistical and anomaly detection
    * row count anomalies
    * null-rate anomalies
    * cardinality anomalies
    * distributional drift: `KS` test, `PSI`, `Wasserstein`
    * time-series-aware checks
    * managed anomaly detection: `Monte Carlo`, `Bigeye`, `Anomalo`
<!-- chapter: great-expectations-deep-dive, duration: 3h -->
* `Great Expectations` deep dive
    * expectations as the unit of test
    * expectation suites and validation runs
    * data context, datasources, batch requests
    * data docs as a living artifact
    * `Great Expectations` `V3` `API` and the `V1` revisions
    * integration with `Airflow`, `Dagster`, `Prefect`, `dbt`
<!-- chapter: dbt-tests-and-elementary, duration: 3h -->
* `dbt` tests and `Elementary`
    * built-in `dbt` tests: not_null, unique, accepted_values, relationships
    * generic and singular tests
    * `dbt-expectations` and `dbt-utils`
    * test severity, warn vs error
    * `Elementary` for observability over `dbt` runs
    * the analytics-engineering quality stack
<!-- chapter: soda-and-other-validation-tools, duration: 2h -->
* `Soda` and other validation tools
    * `Soda` checks language
    * `SodaCL` and reusable checks
    * `Datafold` and data diff
    * `Monte Carlo` and managed observability
    * choosing between tools by team profile
<!-- chapter: data-observability, duration: 3h -->
* Data observability
    * the five pillars: freshness, volume, schema, distribution, lineage
    * lineage as a first-class artifact
    * `OpenLineage` and `Marquez`
    * column-level lineage
    * incident triage with lineage
    * the data observability `vs` data quality distinction
<!-- chapter: data-slos, duration: 3h -->
* Data `SLOs`
    * `SLI`s for data: freshness, completeness, accuracy
    * defining the user of the data
    * burn-rate alerting for data
    * error budgets for pipelines
    * communicating data `SLOs` upstream and downstream
    * the relationship to product `SLOs`
<!-- chapter: validation-in-streaming-pipelines, duration: 2h -->
* Validation in streaming pipelines
    * shift-left validation at the producer
    * dead-letter topics for invalid records
    * sampling-based validation in stream
    * windowed quality checks
    * cross-reference to the Streaming Data Systems course
<!-- chapter: validation-for-ml-pipelines, duration: 2h -->
* Validation for `ML` pipelines
    * training-serving skew detection
    * feature drift in production
    * label quality validation
    * data validation as a `feature store` responsibility
    * `TFX` data validation and `Great Expectations` for `ML`
<!-- chapter: incident-response-for-data-quality, duration: 2h -->
* Incident response for data quality
    * detection: alerts, user reports, downstream noise
    * impact estimation: which dashboards, models, decisions
    * containment: pause pipelines, freeze tables, roll back
    * eradication: fix the data, fix the producer, fix the contract
    * recovery: backfill safely
    * postmortem and the lesson loop
<!-- chapter: program-and-organization, duration: 2h -->
* Program and organization
    * the data quality officer or program owner
    * embedding quality into pipeline development
    * the producer-consumer-platform triangle
    * incentives, dashboards and review meetings
    * cultural patterns that keep quality high
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * design walkthrough of a quality program for a sample data platform
    * group review of a real pipeline's checks
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
