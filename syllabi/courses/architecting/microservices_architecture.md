---
tags:
  - concepts:microservices
  - concepts:architecture
  - concepts:distributed-systems
  - concepts:api
  - concepts:design-patterns
level: intermediate
category: architecture
duration_hours: 16
audience:
  - audiences:developers
  - audiences:architects
  - audiences:devops
  - audiences:team-leads
---
<!-- course: microservices_architecture -->
# `Microservices` Architecture

## Description
This course covers the principles, patterns, and practices of `microservices` architecture. Starting from the challenges of monolithic applications, the course guides participants through the process of decomposing systems into well-defined microservices, designing effective inter-service communication, managing distributed data, and building resilient systems. Participants will learn how to apply industry-proven patterns for service discovery, fault tolerance, deployment, testing, and observability in `microservices`-based systems.

## Duration
16 hours / 2 days

## Intended Audience
* developers building or migrating to `microservices`-based systems
* software architects designing distributed service architectures
* `DevOps` engineers supporting `microservices` infrastructure
* team leads overseeing `microservices` development teams

## Prerequisites
* several years of software development experience
* basic understanding of distributed systems concepts
* familiarity with `REST` APIs and `web services`

## Objectives
* understand the limitations of monolithic architectures and the drivers for `microservices`
* apply decomposition strategies to break down systems into `microservices`
* define service boundaries using bounded contexts
* design effective inter-service communication patterns
* implement data management strategies for distributed services
* apply resilience patterns to build fault-tolerant systems
* plan deployment, testing, and observability strategies for `microservices`

## Outline
<!-- chapter: from-monolith-to-microservices, duration: 1h -->
* from `monolith` to `microservices`
    * `monolith` architecture and its problems
    * scaling challenges of monoliths
    * organizational and deployment bottlenecks
    * when `microservices` are (and are not) the right choice
<!-- chapter: microservices-principles, duration: 1h -->
* `microservices` principles
    * single responsibility and autonomy
    * decentralized governance
    * independent deployability
    * design for failure
    * evolutionary design
<!-- chapter: decomposition-strategies, duration: 1h -->
* decomposition strategies
    * decomposition by business capability
    * decomposition by subdomain
    * strangler fig pattern
    * incremental migration approaches
<!-- chapter: service-boundaries-and-bounded-contexts, duration: 1h -->
* service boundaries and bounded contexts
    * `domain-driven design` fundamentals
    * identifying bounded contexts
    * context mapping
    * defining service contracts
    * avoiding distributed monoliths
<!-- chapter: inter-service-communication, duration: 1h -->
* inter-service communication
    * synchronous communication with `REST` and `gRPC`
    * asynchronous communication with message brokers
    * event-driven communication
    * choreography vs orchestration
    * `API` versioning and backward compatibility
<!-- chapter: api-design-for-microservices, duration: 1h -->
* `API` design for `microservices`
    * RESTful `API` best practices
    * `API` gateway pattern
    * backend for frontend pattern
    * `GraphQL` for `microservices`
    * contract-first design
<!-- chapter: data-management-patterns, duration: 1h -->
* data management patterns
    * database per service pattern
    * shared database anti-pattern
    * `saga` pattern for distributed transactions
    * `CQRS` (Command Query Responsibility Segregation)
    * `event sourcing`
    * data consistency strategies
<!-- chapter: service-discovery, duration: 1h -->
* service discovery
    * client-side vs server-side discovery
    * service registry patterns
    * `DNS`-based discovery
    * service mesh and sidecar proxy
<!-- chapter: resilience-patterns, duration: 1h -->
* resilience patterns
    * circuit breaker pattern
    * bulkhead pattern
    * retry patterns and exponential backoff
    * timeout strategies
    * fallback patterns
    * rate limiting
<!-- chapter: deployment-strategies, duration: 2h -->
* deployment strategies
    * containerization with `Docker`
    * orchestration with `Kubernetes`
    * blue-green deployments
    * canary releases
    * rolling updates
    * feature flags
<!-- chapter: testing-microservices, duration: 2h -->
* testing `microservices`
    * testing pyramid for `microservices`
    * unit testing services
    * integration testing
    * contract testing with Pact
    * end-to-end testing strategies
    * chaos engineering
<!-- chapter: monitoring-and-observability, duration: 1h -->
* monitoring and observability
    * the three pillars: logs, metrics, traces
    * distributed tracing
    * centralized logging
    * health checks and alerting
    * SLI, SLO, and SLA definitions
<!-- chapter: composition-patterns, duration: 1h -->
* composition patterns
    * `API` composition
    * aggregator pattern
    * chained pattern
    * branch pattern
    * service mesh for cross-cutting concerns
<!-- chapter: scaling-microservices, duration: 1h -->
* scaling `microservices`
    * horizontal scaling of individual services
    * auto-scaling based on metrics
    * event-driven scaling
    * scaling data stores independently
    * performance optimization strategies

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
