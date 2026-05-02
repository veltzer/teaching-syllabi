---
tags:
  - concepts:data-lakehouse
  - concepts:databases
  - concepts:best-practices
  - concepts:data-architecture
level: advanced
category: data-engineering
duration_hours: 24
audience:
  - audiences:data-engineers
  - audiences:data-architects
  - audiences:senior-developers
  - audiences:architects
---
<!-- course: lakehouse_table_formats_compared -->
# Lakehouse Table Formats Compared: Iceberg, `Delta Lake`, `Hudi`

## Description
The catalog has `Apache Iceberg`, `Delta Lake`, and `Apache Hudi` as separate courses, plus `Data
Lakehouse` for the broader concept. None of those is the focused architecture decision: which table
format should a team pick for a new lakehouse, and on what basis. The decision matters: each format has
different strengths in writes vs reads, schema evolution, time travel, streaming ingestion, deletion
performance, catalog ecosystem, and vendor support. A wrong choice locks an organization into a multi-year
migration when the data volume grows.

This three day course is the comparative engineering course that helps the architecture decision. It
covers the lakehouse model and what an open table format provides, then covers Iceberg, `Delta Lake`,
and `Hudi` side by side: file layout, metadata structure, write path, read path, transaction model,
schema-evolution capabilities, time travel, copy-on-write vs merge-on-read, deletion vectors and the
`GDPR` RIGHT_TO_BE_FORGOTTEN story, the catalog story (`AWS Glue`, `Hive Metastore`, `Unity Catalog`,
`Polaris`, Nessie), the engine compatibility (`Spark`, `Trino`, `Flink`, Snowflake, `BigQuery`,
`DuckDB`), the streaming-ingestion story, and the migration story between formats. Examples and labs use
the open-source distributions of each. Participants leave able to `make` the format decision deliberately.

## Duration
24 hours / 3 days

## Intended Audience
* data engineers picking a table format for a new lakehouse
* data architects evaluating a migration between formats
* senior developers operating a lakehouse
* architects designing a multi-engine analytics stack

## Prerequisites
* working experience with at least one of Iceberg, `Delta Lake`, `Hudi`
* familiarity with the Data Lakehouse course
* exposure to `Spark` or `Trino`
* basic understanding of `Parquet`

## Objectives
* explain what an open table format provides
* compare Iceberg, `Delta Lake`, and `Hudi` on the dimensions that matter
* pick a format for a given workload
* design the catalog layer
* operate the chosen format in production
* migrate from one format to another
* recognize the patterns that doom a lakehouse

## Outline
<!-- chapter: what-an-open-table-format-actually-is, duration: 2h -->
* What an open table format actually is
    * the limits of `Parquet`-on-`S3`
    * `ACID` over object storage
    * schema evolution as a first-class operation
    * time travel
    * cross-reference to the Data Lakehouse course
<!-- chapter: file-layout-and-metadata, duration: 2h -->
* `File` layout and metadata
    * Iceberg's manifest hierarchy
    * `Delta Lake`'s `_delta_log`
    * `Hudi`'s timeline and indexing
    * how writes and reads use the metadata
    * the metadata-explosion failure mode
<!-- chapter: transaction-models, duration: 2h -->
* Transaction models
    * snapshot isolation in Iceberg
    * optimistic concurrency in Delta
    * `Hudi`'s timeline
    * the cross-engine concurrent-write problem
    * the "two writers raced and one lost" failure
<!-- chapter: copy-on-write-vs-merge-on-read, duration: 2h -->
* Copy-on-write vs merge-on-read
    * the trade-off
    * which workload is each best for
    * `Hudi`'s explicit choice
    * Iceberg's position-deletes and equality-deletes
    * Delta's deletion vectors
<!-- chapter: schema-evolution, duration: 2h -->
* Schema evolution
    * column add, drop, rename, reorder, type-change
    * Iceberg's field-`id` approach
    * Delta's schema-on-read
    * `Hudi`'s schema reconciliation
    * the "we renamed a column and broke every reader" failure
<!-- chapter: time-travel, duration: 1h -->
* Time travel
    * snapshot-based reads
    * the as-of-timestamp query
    * the version-`id` query
    * use cases: debugging, reproducibility, `GDPR`
    * the storage cost of time travel
<!-- chapter: deletion-and-gdpr, duration: 2h -->
* Deletion and `GDPR`
    * the "right to be forgotten" requirement
    * deletion vectors in Delta
    * row-level deletes in Iceberg
    * `Hudi`'s deletion options
    * cross-reference to the `GDPR` and Compliance course
    * the "we cannot prove the row is gone" reality
<!-- chapter: catalog-layer, duration: 2h -->
* Catalog layer
    * `AWS Glue` `Catalog`
    * `Hive Metastore`
    * `Unity Catalog`
    * `Polaris` (Iceberg `REST` catalog)
    * `Nessie` (`git`-like)
    * picking the catalog
<!-- chapter: engine-compatibility, duration: 2h -->
* Engine compatibility
    * `Spark` support across formats
    * `Trino` support across formats
    * `Flink` for streaming ingestion
    * Snowflake, `BigQuery`, Athena external tables
    * `DuckDB` and the analyst use case
    * the "the engine could not read our format" reality
<!-- chapter: streaming-ingestion, duration: 2h -->
* Streaming ingestion
    * `Flink`-to-Iceberg
    * `Spark Structured Streaming`-to-Delta
    * `Hudi`'s `DeltaStreamer`
    * the small-files problem
    * the compaction strategy
<!-- chapter: operational-realities, duration: 2h -->
* Operational realities
    * the small-files problem
    * the compaction job
    * the snapshot-cleanup job
    * the metadata-rewrite job
    * the "we ran out of file handles" failure
<!-- chapter: making-the-decision, duration: 2h -->
* Making the decision
    * the decision matrix
    * the workload-driven choice
    * the ecosystem-driven choice
    * the vendor-lock-in question
    * worked example: pick a format for three different workloads
<!-- chapter: migration-between-formats, duration: 1h -->
* Migration between formats
    * the dual-write strategy
    * the in-place upgrade (Iceberg `Migrate`, Delta `convert`)
    * the rewrite-everything approach
    * the "we wanted to migrate and could not afford it" reality

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
