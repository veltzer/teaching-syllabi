---
tags:
  - concepts:feature-store
  - concepts:machine-learning
  - concepts:best-practices
  - concepts:operations
level: advanced
category: data-engineering
duration_hours: 24
audience:
  - audiences:data-engineers
  - audiences:ml-engineers
  - audiences:devops
  - audiences:senior-developers
---
<!-- course: feature_store_engineering -->
# Feature Store Engineering

## Description
A feature store is the system that produces, materializes, serves, and governs the features that machine
learning models consume. It is the boundary between a data engineering pipeline and an `ML` model. The
catalog has `MLOps` and `Feature Engineering` courses but neither covers the engineering of the feature
store itself: the dual-write between offline and online stores, the point-in-time-correctness problem,
the freshness vs cost trade-off, the registry, the lineage, and the operational realities of serving
features at low latency under load.

This three day course covers the feature store as its own system. It covers the architecture (offline
store, online store, registry, transformation pipeline), the canonical implementations (`Feast`,
`Tecton`, `Hopsworks`, `Vertex AI` Feature Store, `SageMaker` Feature Store, `Databricks` Feature
Store), the point-in-time correctness problem, the training-serving skew problem, the data freshness
question, the on-demand-feature pattern, the embedding-feature pattern, the governance story, and the
team-ownership question. Participants leave able to choose between buy and build, design the offline
and online sides correctly, and operate a feature store at production scale.

## Duration
24 hours / 3 days

## Intended Audience
* data engineers introducing a feature store into an organization
* `ML` engineers tired of the training-serving skew bug
* platform engineers building `ML` paved roads
* senior developers asked to "just take the model to production"

## Prerequisites
* working knowledge of `SQL` and at least one data warehouse
* exposure to a basic `ML` workflow
* familiarity with the `MLOps` course is helpful but not required

## Objectives
* explain why a feature store is necessary
* design the offline and online sides without dual-writes
* solve the point-in-time correctness problem
* prevent training-serving skew
* operate a feature store at low latency under load
* govern features as first-class artifacts
* choose between `Feast`, `Tecton`, and a managed offering

## Outline
<!-- chapter: what-a-feature-store-actually-is, duration: 2h -->
* What a feature store actually is
    * the boundary between data engineering and `ML`
    * offline store, online store, registry, transformations
    * what it is not: a data warehouse, a vector database
    * cross-reference to the `MLOps` course
    * the use cases that justify one and the ones that do not
<!-- chapter: the-training-serving-skew-problem, duration: 2h -->
* The training-serving skew problem
    * the canonical bug: feature value at training time differs at serving time
    * the root causes: separate code paths, time-travel bugs, schema drift
    * the cost of skew
    * the feature store as the prevention mechanism
<!-- chapter: point-in-time-correctness, duration: 3h -->
* Point-in-time correctness
    * the leaky-feature problem
    * the as-of join
    * the feature timestamp and the event timestamp
    * the "we trained on data from the future" failure
    * worked example: a point-in-time correct training dataset
<!-- chapter: offline-store-design, duration: 2h -->
* Offline store design
    * the warehouse as the offline store
    * `Snowflake`, `BigQuery`, `Redshift`, `Databricks`, `Iceberg`
    * the data model: feature view, entity, timestamp
    * partitioning for the as-of join
    * cross-reference to the Data Lakehouse course
<!-- chapter: online-store-design, duration: 2h -->
* Online store design
    * the read-latency requirement
    * `Redis`, `DynamoDB`, `Cassandra`, `ScyllaDB` as backends
    * key design and the entity model
    * the freshness vs cost trade-off
    * the "online store does not match offline store" failure
<!-- chapter: feature-pipelines, duration: 2h -->
* Feature pipelines
    * batch features, streaming features, on-demand features
    * the transformation as code
    * the dual-pipeline anti-pattern
    * the single-pipeline argument
    * cross-reference to the Streaming Data Systems course
<!-- chapter: feast-deep-dive, duration: 2h -->
* `Feast` deep dive
    * the `Feast` architecture
    * `feature_store.yaml` and the registry
    * `materialize` and `materialize-incremental`
    * the offline store and the online store providers
    * the gotchas at production scale
<!-- chapter: tecton-and-managed-offerings, duration: 2h -->
* `Tecton` and managed offerings
    * `Tecton`'s pipeline model
    * `Hopsworks` and the on-prem case
    * `Vertex AI` Feature Store, `SageMaker` Feature Store
    * `Databricks` Feature Store
    * the buy-vs-build decision
<!-- chapter: embedding-features, duration: 2h -->
* Embedding features
    * embeddings as features
    * the embedding store and the vector store
    * cross-reference to the Vector Databases Engineering course
    * the dimension-and-version problem
    * embeddings and point-in-time correctness
<!-- chapter: governance-and-the-registry, duration: 2h -->
* Governance and the registry
    * the feature registry as the catalog
    * lineage, ownership, descriptions
    * deprecation and the consumer
    * cross-reference to the Data Governance course
    * the "two teams built the same feature differently" failure
<!-- chapter: serving-at-scale, duration: 2h -->
* Serving at scale
    * the read-path latency budget
    * caching strategies
    * batching and the multi-key get
    * the "feature fetch is the bottleneck" failure
    * cost of the online store at scale
<!-- chapter: operating-a-feature-store, duration: 1h -->
* Operating a feature store
    * monitoring freshness
    * monitoring skew
    * monitoring drift
    * the on-call story
    * the migration story `when` you replace the feature store

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
