---
tags:
  - architecture:saga
  - architecture:distributed-transactions
  - concepts:microservices
  - concepts:eventual-consistency
level: advanced
category: architecture
duration_hours: 8
audience:
  - audiences:architects
  - audiences:senior-developers
---
<!-- course: saga_pattern -->
# `Saga Pattern`

## Description
Distributed transactions are one of the most challenging problems in `microservices` architecture, and the `Saga` pattern is the industry-accepted solution for managing long-running business processes that span multiple services without using two-phase commit. This course provides a deep understanding of the `Saga` pattern, covering both choreography-based and orchestration-based approaches, their trade-offs, and `when` to apply each. Participants will learn to design compensating transactions, model failure scenarios, and build reliable distributed workflows that maintain data consistency under eventual consistency guarantees. The course includes practical guidance on tooling, testing, and debugging sagas in production.

## Duration
8 hours / 1 day

## Intended Audience
* Software architects designing distributed `microservices` systems
* Senior developers implementing cross-service business processes
* Technical leads evaluating distributed transaction strategies
* Backend engineers working with event-driven architectures and message brokers
* Engineers migrating from monoliths to `microservices` with shared data concerns

## Prerequisites
* `Solid` understanding of `microservices` architecture principles
* Familiarity with message brokers such as `Kafka` or `RabbitMQ`
* Experience with `event-driven architecture` and asynchronous communication
* Basic understanding of ACID transactions and distributed systems challenges
* Experience with at least one backend programming language (e.g., `Java`, `Python`, `C#`, `Go`)

## Required Knowledge
* `Microservices` Architecture (or equivalent experience)
* `Event-Driven Architecture` Fundamentals (or equivalent experience)

## Objectives
* Understand why distributed transactions fail and why two-phase commit is impractical in `microservices`
* Explain the `Saga` pattern and its role in maintaining eventual consistency
* Design choreography-based sagas using domain events and reactive participation
* Design orchestration-based sagas using a central coordinator or state machine
* Implement compensating transactions to reverse completed steps on failure
* Model and handle partial failures, timeouts, and out-of-order events
* Select the appropriate `saga` style based on system complexity and team structure
* Test and debug sagas in development and production environments

## Outline
<!-- chapter: distributed-transactions-problem, duration: 1h -->
* The Distributed Transactions Problem
    * ACID transactions and their limitations across service boundaries
    * Two-phase commit (2PC): how it works and why it is problematic in `microservices`
    * CAP theorem and the trade-off between consistency and availability
    * Eventual consistency: definition, implications, and user experience challenges
    * The need for long-running process management in distributed systems
    * Business process modeling across multiple bounded contexts
    * Why the `Saga` pattern is the accepted alternative to distributed transactions
<!-- chapter: saga-pattern-fundamentals, duration: 1h -->
* `Saga` Pattern Fundamentals
    * What is a `Saga`: a sequence of local transactions with compensations
    * The structure of a `saga`: steps, local transactions, and compensating transactions
    * Forward recovery vs backward recovery strategies
    * `Saga` failure semantics: semantic rollback vs ACID rollback
    * State management: where to store `saga` state
    * Idempotency requirements for `saga` participants
    * Overview of choreography vs orchestration approaches
    * Choosing the right `saga` style for a given business process
<!-- chapter: choreography-based-sagas, duration: 2h -->
* Choreography-Based Sagas
    * How choreography works: participants `react` to events and emit new events
    * Designing the event flow for a business process
    * Event contracts and schema ownership among participating services
    * Handling failures in choreography: reactive compensation through events
    * Avoiding cyclic dependencies and event spaghetti
    * Tracking `saga` progress without a central coordinator
    * Debugging and tracing choreography-based sagas with correlation `IDs`
    * Practical example: order fulfillment `saga` using choreography
<!-- chapter: orchestration-based-sagas, duration: 2h -->
* Orchestration-Based Sagas
    * How orchestration works: a central `saga` orchestrator directs participants
    * Designing the `saga` orchestrator as a state machine
    * Communication patterns: synchronous commands vs asynchronous command events
    * Orchestrator persistence: storing `saga` state across restarts and failures
    * Handling timeouts and retry logic in the orchestrator
    * Centralized visibility and monitoring of `saga` progress
    * Workflow engines for `saga` orchestration: `Temporal`, `Conductor`, `Camunda`
    * Practical example: order fulfillment `saga` using orchestration
<!-- chapter: compensating-transactions, duration: 1h -->
* Compensating Transactions
    * What is a compensating transaction and how it differs from a rollback
    * Designing semantically correct compensations for each `saga` step
    * Non-compensatable steps: identifying and managing them
    * Pivot transactions and the point of no return
    * Partial compensation strategies for idempotent operations
    * Handling failures during compensation (nested failures)
    * Communicating compensations to end users
    * Testing compensating transactions in isolation and end-to-end
<!-- chapter: testing-and-debugging-sagas, duration: 1h -->
* Testing and Debugging Sagas
    * Unit testing `saga` orchestrators and choreography participants
    * Simulating failure scenarios and partial execution
    * Integration testing `saga` flows with real message brokers
    * Contract testing between `saga` participants
    * Distributed tracing for `saga` visibility: `OpenTelemetry`, `Jaeger`, `Zipkin`
    * `Saga` monitoring dashboards and alerting on stuck sagas
    * Common `saga` anti-patterns: long sagas, missing compensations, state explosion
    * Production debugging: replaying events and manual `saga` intervention

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
