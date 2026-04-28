---
tags:
  - concepts:serverless
  - concepts:cloud-economics
  - concepts:scalability
  - concepts:observability
  - concepts:async-programming
  - concepts:operations
level: intermediate
category: cloud
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:devops
  - audiences:sres
  - audiences:architects
---
<!-- course: serverless_in_practice -->
# Serverless In Practice

## Description
Serverless platforms `make` it easy to ship a working endpoint and hard to ship a production system. The first
deployment takes minutes; the operational reality of cold starts, concurrency limits, packaging, eventing
`glue`, observability gaps, error handling and cost surprises shows up after a feature ships and the bill
arrives. This five day course covers serverless as an operational and engineering discipline, complementing
the architecture-level course already in the catalog.

The course is multi-cloud (`AWS Lambda`, `Google Cloud Run` and `Cloud Functions`, `Azure Functions`, `Cloudflare Workers`) but `AWS Lambda` is used as the primary worked example because it has the deepest production
ecosystem. The course covers the runtime model, cold-start engineering, packaging and deployment, eventing
and `step functions`, the database and stateful-service interaction patterns, observability and tracing,
local development, security boundaries, cost engineering, and the realistic limits of serverless. Participants
leave able to ship serverless systems that are fast, observable, debuggable and not surprisingly expensive.

## Duration
40 hours / 5 days

## Intended Audience
* developers shipping serverless functions or running them in production
* `DevOps` engineers operating serverless infrastructure at scale
* architects deciding `when` serverless is the right tool
* engineers diagnosing latency, cost or reliability issues with serverless workloads

## Prerequisites
* working knowledge of at least one cloud provider
* experience writing code in at least one language with serverless support (`Python`, `Node.js`, `Go`, `Java`, `.NET`)
* basic familiarity with `HTTP`, `IaC` and `CI`/`CD`

## Objectives
* describe the serverless execution model and its consequences
* engineer cold-start performance to acceptable levels
* package and deploy serverless functions repeatedly
* build event-driven systems on serverless primitives
* operate serverless functions with appropriate observability
* manage cost and concurrency at scale
* identify `when` serverless is the wrong choice

## Outline
<!-- chapter: the-serverless-model, duration: 2h -->
* The serverless model
    * the execution model: invoke, run, freeze, recycle
    * the operator boundary: what the platform owns vs what you own
    * `FaaS` vs containers-as-functions vs serverless containers
    * the spectrum: `Lambda`, `Cloud Run`, `App Runner`, `Container Apps`, `Workers`
    * what serverless actually pays for
<!-- chapter: cold-starts-and-warm-paths, duration: 4h -->
* Cold starts and warm paths
    * what triggers a cold start
    * factors: language runtime, package size, dependency tree, network init
    * the bimodal latency distribution
    * provisioned concurrency and minimum instances
    * `SnapStart` and `Firecracker`-level mitigations
    * `init` code optimization
    * connection reuse across invocations
    * benchmarking cold starts honestly
<!-- chapter: packaging-and-deployment, duration: 3h -->
* Packaging and deployment
    * `Zip` packaging vs container-image deployment
    * `Lambda` layers and shared dependencies
    * dependency size and the cold-start tax
    * monorepo deployment and per-function isolation
    * `IaC`: `SAM`, `Serverless Framework`, `CDK`, `Terraform`, `Pulumi`
    * `CI`/`CD` for serverless
    * canary and rolling deploys
<!-- chapter: api-and-http-frontends, duration: 3h -->
* `API` and `HTTP` frontends
    * `API Gateway`, `ALB`, `Cloud Run` direct, `Functions` direct
    * `HTTP` `API` vs `REST` `API` `Lambda` integration
    * payload shaping and `VTL` mappings
    * authorizers and `JWT` verification
    * `WebSocket` and streaming on serverless
    * comparing `API Gateway`, `Cloud Endpoints`, `Azure API Management`
<!-- chapter: event-sources-and-eventing, duration: 4h -->
* Event sources and eventing
    * the dozens of event sources for `Lambda`
    * queue-driven serverless: `SQS`, `Pub/Sub`, `Storage Queues`
    * event-bus-driven serverless: `EventBridge`, `Eventarc`, `Event Grid`
    * stream-driven serverless: `Kinesis`, `DynamoDB Streams`, `Kafka`
    * scheduled functions: cron and the timezone trap
    * event-driven choreography vs orchestration
<!-- chapter: workflow-and-step-functions, duration: 3h -->
* Workflow and `step functions`
    * `AWS Step Functions`: standard vs express
    * `GCP Workflows`, `Azure Logic Apps`, `Durable Functions`
    * choreography vs orchestration revisited
    * idempotency in workflows
    * error handling, retries, compensations
    * cross-reference to the Idempotency course
<!-- chapter: state-and-data-from-serverless, duration: 3h -->
* State and data from serverless
    * the connection-pool problem in serverless
    * `RDS Proxy`, `Cloud SQL Auth Proxy`, `Hyperdrive`
    * `DynamoDB`, `Firestore`, `Cosmos DB` from functions
    * caching: `ElastiCache`, `Memorystore`, edge caches
    * `S3`/`GCS`/`Blob Storage` direct integrations
    * the limits of stateful workflows on serverless
<!-- chapter: observability-for-serverless, duration: 3h -->
* Observability for serverless
    * structured logging without losing requests
    * `CloudWatch Logs`, `Cloud Logging`, `Application Insights`
    * metrics: invocations, duration, errors, throttles, concurrency
    * distributed tracing across function boundaries
    * `X-Ray`, `Cloud Trace`, `OpenTelemetry`
    * the cost of detailed observability
    * the gaps that serverless observability still has
<!-- chapter: error-handling-and-retries, duration: 2h -->
* Error handling and retries
    * synchronous vs asynchronous invocation
    * dead-letter queues
    * destinations on success and failure
    * retry behavior per event source
    * idempotency requirements
    * the "function as a unit of retry" mental model
<!-- chapter: concurrency-and-throttling, duration: 2h -->
* Concurrency and throttling
    * unreserved, reserved, provisioned concurrency
    * account and regional concurrency limits
    * throttle vs error vs queue
    * back-pressure with `SQS` between producer and function
    * the herd problem: scaling from 0 to 10000
    * managing concurrency for downstream protection
<!-- chapter: local-development-and-testing, duration: 2h -->
* Local development and testing
    * `SAM CLI`, `Serverless Framework offline`, `LocalStack`
    * unit testing handlers
    * integration testing with deployed dev stages
    * `Functions Framework` for local invocation
    * the parity gap between local and cloud
<!-- chapter: security-for-serverless, duration: 3h -->
* Security for serverless
    * function execution role and least privilege
    * secrets management: `Secrets Manager`, `Parameter Store`, `Vault`
    * `VPC` access vs public access
    * `IAM` boundaries and tag-based policies
    * dependency vulnerabilities in serverless packages
    * protection against malicious uploads and event injection
    * cross-reference to the Secrets Management course
<!-- chapter: cost-engineering, duration: 3h -->
* Cost engineering
    * the per-invocation cost model
    * memory size and `CPU` allocation
    * the `1M`-invocations-`per`-month rule of thumb
    * provisioned concurrency cost decisions
    * `API Gateway` and other `glue` costs
    * cost dashboards per function
    * cross-reference to the Cloud Cost Optimization course
<!-- chapter: when-serverless-is-the-wrong-choice, duration: 2h -->
* `When` serverless is the wrong choice
    * sustained high-traffic workloads
    * latency-sensitive workloads
    * long-running workloads
    * stateful workloads with large in-memory state
    * workloads with strict regulatory or hardware requirements
    * the "we will refactor `when` scale arrives" trap
<!-- chapter: case-studies-and-wrap-up, duration: 1h -->
* Case studies and wrap up
    * the function that grew into a `monolith`
    * the bill spike from a runaway recursion
    * the cold-start incident in production
    * a successful serverless rewrite
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
