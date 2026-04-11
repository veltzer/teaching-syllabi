---
tags:
  - concepts:serverless
  - concepts:architecture
  - concepts:distributed-systems
  - infrastructure:cloud
level: intermediate
category: architecture
duration_hours: 16
audience:
  - audiences:architects
  - audiences:developers
  - audiences:devops
---
<!-- course: serverless_architecture -->
# Serverless Architecture

## Description
This course covers the principles and patterns of serverless architecture in a cloud-agnostic manner. Students will learn how to design, build, and operate event-driven applications using Functions as a Service (FaaS) and Backend as a Service (BaaS) offerings. The course addresses real-world challenges such as cold starts, state management, testing strategies, and cost optimization, and compares serverless platforms across major cloud providers.

## Duration
16 hours / 2 days

## Intended Audience
* Software architects evaluating serverless for new or existing projects.
* Developers building event-driven and cloud-native applications.
* `DevOps` engineers managing serverless deployments and operations.

## Prerequisites
* Experience with at least one cloud platform (`AWS`, `Azure`, or `GCP`).
* Familiarity with distributed systems concepts.
* Programming experience in a modern language such as `Python`, `JavaScript`, or `Go`.

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)
* Introduction to `Azure` (or equivalent experience)
* `GCP` Fundamentals (or equivalent experience)

## Objectives
* Understand the serverless execution model and its trade-offs.
* Design event-driven architectures using serverless components.
* Apply patterns for state management in stateless environments.
* Implement effective testing strategies for serverless applications.
* Optimize serverless deployments for cost and performance.
* Compare serverless offerings across major cloud vendors.

## Outline
<!-- chapter: introduction-to-serverless, duration: 1h -->
* Introduction to Serverless
    * What serverless means and what it does not
    * Evolution from monoliths to `microservices` to serverless
    * FaaS vs BaaS vs containers
    * The serverless execution model
    * `When` serverless is and is not a good fit
<!-- chapter: serverless-design-patterns, duration: 2h -->
* Serverless `Design Patterns`
    * `Event-driven architecture` fundamentals
    * Fan-out and fan-in patterns
    * Choreography vs orchestration
    * `API` composition pattern
    * `Saga` pattern for distributed transactions
    * `CQRS` and `event sourcing` in serverless
<!-- chapter: cold-starts-and-performance, duration: 1h -->
* Cold Starts and Performance
    * Understanding cold start causes and impact
    * Language runtime considerations
    * Provisioned concurrency and warm-up strategies
    * Memory and timeout tuning
    * Connection pooling and reuse
<!-- chapter: state-management, duration: 2h -->
* State Management
    * Stateless function design
    * External state stores and databases
    * Caching strategies
    * Workflow orchestration with `step functions`
    * Durable execution patterns
    * Handling idempotency and retries
<!-- chapter: event-sources-and-integration, duration: 2h -->
* Event Sources and Integration
    * `HTTP` and `API` gateways
    * Message queues and streaming
    * Storage and database triggers
    * Scheduled and cron-based invocations
    * Event filtering and routing
    * Dead letter queues and error handling
<!-- chapter: testing-serverless-applications, duration: 2h -->
* Testing Serverless Applications
    * Unit testing functions in isolation
    * Integration testing with emulators
    * End-to-end testing strategies
    * Local development and debugging
    * Contract testing between services
    * Observability, tracing, and logging
<!-- chapter: cost-optimization, duration: 2h -->
* Cost Optimization
    * Serverless pricing models
    * Identifying and eliminating waste
    * Right-sizing memory and duration
    * Comparing cost at different scales
    * Reserved capacity and committed use
    * Monitoring and alerting on cost
<!-- chapter: vendor-comparison, duration: 2h -->
* Vendor Comparison
    * `AWS Lambda` and ecosystem
    * `Azure Functions` and ecosystem
    * `Google Cloud Functions` and `Cloud Run`
    * Open-source alternatives (`Knative`, OpenFaaS)
    * Portability considerations and abstraction layers
    * Multi-cloud serverless strategies
<!-- chapter: security-and-operational-concerns, duration: 2h -->
* Security and Operational Concerns
    * Least privilege for function roles
    * Secret management
    * Network isolation and `VPC` integration
    * Deployment strategies (canary, blue-green)
    * Infrastructure as Code for serverless
    * Versioning and alias management

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
