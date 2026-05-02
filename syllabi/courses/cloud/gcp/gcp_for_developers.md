---
tags:
  - infrastructure:gcp
  - infrastructure:cloud
  - concepts:serverless
  - practices:devops
level: intermediate
category: cloud
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
---
<!-- course: gcp_for_developers -->
# `GCP` for Developers

## Description
This course teaches developers how to build, deploy, and manage applications on the `Google Cloud Platform`. It covers key developer-facing services including `Cloud Run`, `Cloud Functions`, `Firestore`, Pub/Sub, `Cloud Build`, and `BigQuery`. Participants will gain practical experience with serverless computing, `NoSQL` data storage, event-driven messaging, `CI/CD` pipelines, and data analytics on `GCP`.

## Duration
16 hours / 2 days

## Intended Audience
* Software developers building or migrating applications to `GCP`.
* Backend engineers looking to adopt serverless and cloud-native patterns on `Google Cloud`.
* `DevOps` engineers who want to understand `GCP` developer services and `CI/CD` tooling.

## Prerequisites
* Experience in at least one programming language (`Python`, Go, or `Node.js` recommended).
* Basic understanding of cloud concepts and containerization.
* Familiarity with command-line tools.

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `Node.js` Backend Development (or equivalent experience)

## Objectives
* Deploy containerized applications with `Cloud Run` and event-driven functions with `Cloud Functions`.
* Model and query data using `Firestore`.
* Implement asynchronous messaging patterns with Pub/Sub.
* Build `CI/CD` pipelines using `Cloud Build`.
* Run analytical queries on large datasets with `BigQuery`.

## Outline
<!-- chapter: introduction-to-gcp-for-developers, duration: 2h -->
* Introduction to `GCP` for Developers
    * `GCP` developer ecosystem overview
    * gcloud `CLI` and Cloud Shell
    * `IAM` roles and service accounts
    * Project organization and resource hierarchy
<!-- chapter: cloud-run, duration: 2h -->
* `Cloud Run`
    * Container-based serverless computing
    * Deploying containerized applications
    * Autoscaling and concurrency settings
    * Custom domains and traffic management
    * Connecting to other `GCP` services
    * `Cloud Run` Jobs
<!-- chapter: cloud-functions, duration: 2h -->
* `Cloud Functions`
    * Event-driven and `HTTP`-triggered functions
    * Supported runtimes and function frameworks
    * Environment variables and secrets
    * `Cloud Functions` (2nd gen) and `Cloud Run` integration
    * Error handling and retries
    * Local development and testing
<!-- chapter: firestore, duration: 2h -->
* `Firestore`
    * Document-oriented data model
    * Collections, documents, and subcollections
    * Queries and indexing
    * Real-time listeners
    * Security rules
    * Native mode vs. Datastore mode
<!-- chapter: pub-sub, duration: 2h -->
* Pub/Sub
    * Topics and subscriptions
    * Push and pull delivery
    * Message ordering and exactly-once delivery
    * Dead-letter topics
    * Integration with `Cloud Functions` and `Cloud Run`
    * Schema management
<!-- chapter: cloud-build, duration: 2h -->
* `Cloud Build`
    * Build configuration and build steps
    * Triggers and source repositories
    * Building and pushing container images
    * Integrating with `Cloud Run` and `GKE`
    * Artifact Registry
    * Automated testing in build pipelines
<!-- chapter: bigquery-basics, duration: 2h -->
* `BigQuery` Basics
    * `BigQuery` architecture overview
    * Datasets, tables, and schemas
    * Running `SQL` queries in `BigQuery`
    * Loading and exporting data
    * Querying external data sources
    * Cost management and query optimization
<!-- chapter: putting-it-all-together, duration: 2h -->
* Putting It All Together
    * Designing event-driven architectures on `GCP`
    * End-to-end application patterns
    * Security best practices
    * Monitoring and logging with Cloud Operations

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
