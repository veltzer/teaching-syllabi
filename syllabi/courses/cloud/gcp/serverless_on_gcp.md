---
tags:
  - infrastructure:gcp
  - infrastructure:cloud
  - concepts:architecture
level: intermediate
category: cloud
duration_hours: 24
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: serverless_on_gcp -->
# Serverless on `GCP`

## Description
This course covers the full range of serverless computing options available on `Google Cloud Platform`.
Participants will learn how to build, deploy, and manage serverless applications using `Cloud Functions`,
`Cloud Run`, and `App Engine`, along with supporting services such as Eventarc, `Cloud Tasks`, and
`Cloud Scheduler`. The course also addresses integration with data services, networking, security,
monitoring, and cost optimization strategies for serverless workloads.

## Duration
24 hours / 3 days

## Intended Audience
* developers building applications on `Google Cloud Platform`.
* developers transitioning from traditional server-based architectures to serverless.
* backend engineers looking to reduce operational overhead with managed services.

## Prerequisites
* basic understanding of `cloud computing` concepts.
* experience with at least one programming language (`Python`, `Node.js`, Go, or `Java`).
* familiarity with `GCP` console and gcloud `CLI` is helpful.

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `Node.js` Backend Development (or equivalent experience)

## Objectives
* understand serverless architecture principles on `GCP`.
* build and deploy applications using `Cloud Functions`, `Cloud Run`, and `App Engine`.
* integrate serverless workloads with event-driven services and data stores.
* implement security, monitoring, and cost optimization for serverless applications.

## Outline
<!-- chapter: serverless-concepts-on-gcp, duration: 2h -->
* Serverless concepts on `GCP`
    * what is serverless computing
    * benefits and trade-offs
    * overview of `GCP` serverless portfolio
    * choosing the right serverless option
<!-- chapter: cloud-functions, duration: 3h -->
* `Cloud Functions`
    * `HTTP`-triggered functions
    * event-driven functions
    * 2nd generation `Cloud Functions`
    * runtime environments and dependencies
    * environment variables and secrets
    * local development and testing
<!-- chapter: cloud-run, duration: 3h -->
* `Cloud Run`
    * container-based serverless
    * services and revisions
    * jobs for batch workloads
    * traffic splitting and gradual rollouts
    * concurrency and scaling settings
    * custom domains
<!-- chapter: app-engine, duration: 2h -->
* `App Engine`
    * standard environment vs flexible environment
    * application structure and configuration
    * versioning and traffic management
    * when to choose `App Engine` over `Cloud Run`
<!-- chapter: api-management, duration: 2h -->
* `API` management
    * `Cloud Endpoints`
    * `API Gateway`
    * authentication and rate limiting
    * `API` versioning strategies
<!-- chapter: event-driven-architecture, duration: 2h -->
* `Event-driven architecture`
    * Eventarc triggers and event routing
    * `Cloud Tasks` for asynchronous processing
    * `Cloud Scheduler` for cron-based workloads
    * Pub/Sub integration
    * `Cloud Storage` triggers
<!-- chapter: data-services-integration, duration: 2h -->
* Data services integration
    * `Firestore` for serverless applications
    * `Cloud SQL` with serverless compute
    * connection management and pooling
    * data modeling considerations
<!-- chapter: networking-and-security, duration: 2h -->
* Networking and security
    * serverless `VPC` access
    * `Identity-Aware Proxy`
    * service identity and `IAM`
    * securing function endpoints
<!-- chapter: monitoring-and-operations, duration: 2h -->
* Monitoring and operations
    * `Cloud Monitoring` for serverless
    * `Cloud Logging` integration
    * tracing and debugging
    * alerting and SLOs
<!-- chapter: cost-optimization, duration: 2h -->
* Cost optimization
    * pricing models for each serverless option
    * right-sizing and concurrency tuning
    * cold start mitigation
    * minimum instances vs scale-to-zero
<!-- chapter: comparison-of-gcp-serverless-options, duration: 2h -->
* Comparison of `GCP` serverless options
    * `Cloud Functions` vs `Cloud Run` vs `App Engine`
    * decision framework
    * migration paths between services

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
