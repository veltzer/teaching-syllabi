---
tags:
  - concepts:domain-driven-design
  - concepts:architecture
  - concepts:design-patterns
level: advanced
category: architecture
duration_hours: 24
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: domain_driven_design -->
# `Domain-Driven Design`

## Description
This course provides a thorough exploration of `Domain-Driven Design` (`DDD`) as a methodology for tackling complexity in software systems. Participants will learn both strategic and tactical `DDD` patterns, from defining bounded contexts and ubiquitous language to implementing entities, aggregates, and domain events. The course also covers event storming as a collaborative modeling technique, advanced patterns like `CQRS` and `event sourcing`, and practical guidance on applying `DDD` within `microservices` and hexagonal architectures.

## Duration
24 hours / 3 days

## Intended Audience
* Senior software developers building complex business applications
* Software architects designing service boundaries and domain models
* Technical leads responsible for system decomposition decisions
* Development team members adopting `DDD` practices
* Engineers working with or transitioning to `microservices` architectures

## Prerequisites
* Several years of experience in software development
* `Solid` understanding of object-oriented programming principles
* Familiarity with common `design patterns` (factory, repository, strategy)
* Basic understanding of distributed systems concepts
* Experience with at least one web framework and database technology

## Objectives
* Apply strategic `DDD` to identify bounded contexts, subdomains, and context mappings
* Establish and maintain a ubiquitous language within development teams
* Implement tactical `DDD` building blocks: entities, value objects, aggregates, and domain services
* Facilitate event storming workshops to discover domain knowledge collaboratively
* Design systems using `CQRS` and `event sourcing` patterns
* Apply the `saga` pattern for managing distributed business processes
* Integrate `DDD` with microservices and `hexagonal architecture`
* Refactor existing codebases toward deeper domain insight

## Outline
<!-- chapter: strategic-domain-driven-design, duration: 3h -->
* Strategic `Domain-Driven Design`
    * Introduction to `DDD` and the problem of software complexity
    * The role of the domain model as a communication and design tool
    * Ubiquitous language: building a shared vocabulary between developers and domain experts
    * Identifying subdomains: core, supporting, and generic
    * Bounded contexts: defining explicit boundaries for models
    * Context mapping patterns: shared kernel, customer-supplier, conformist, and anticorruption layer
    * Published language and open host service patterns
    * Organizing teams around bounded contexts
<!-- chapter: event-storming-and-domain-discovery, duration: 3h -->
* Event Storming and Domain Discovery
    * Event storming as a collaborative domain exploration technique
    * Facilitating big-picture event storming sessions
    * Identifying domain events, commands, and aggregates from event storming
    * Process modeling and design-level event storming
    * From event storming to bounded context boundaries
    * Capturing business rules and policies
    * Documenting and communicating event storming results
<!-- chapter: tactical-ddd-building-blocks, duration: 4h -->
* Tactical `DDD` Building Blocks
    * Entities: identity, lifecycle, and equality
    * Value objects: immutability, equality by value, and self-validation
    * Aggregates: consistency boundaries, aggregate roots, and invariant enforcement
    * Designing aggregate boundaries for performance and consistency
    * Repositories: abstracting persistence and collection-oriented vs persistence-oriented styles
    * Domain services: encapsulating logic that does not belong to a single entity
    * Factories: encapsulating complex creation logic
    * Domain events: capturing meaningful state changes within the domain
    * Specification pattern for expressing business rules
<!-- chapter: cqrs-and-event-sourcing, duration: 4h -->
* `CQRS` and `Event Sourcing`
    * Command Query Responsibility Segregation (`CQRS`) principles and motivation
    * Separating read and write models
    * Designing command handlers and query handlers
    * `Event sourcing`: storing state as a sequence of events
    * Event store design and implementation considerations
    * Projections: building read models from event streams
    * Snapshotting for performance optimization
    * Eventual consistency and its implications for user experience
    * `When` to use and when to avoid `CQRS` and `event sourcing`
<!-- chapter: saga-pattern-and-distributed-processes, duration: 3h -->
* `Saga Pattern` and Distributed Processes
    * Managing distributed transactions without two-phase commit
    * Saga pattern: orchestration vs choreography
    * Designing compensating actions for failure recovery
    * Implementing orchestration-based sagas with a `saga` coordinator
    * Implementing choreography-based sagas with domain events
    * Idempotency in `saga` participants
    * Monitoring and debugging distributed sagas
    * Process managers vs sagas
<!-- chapter: ddd-with-microservices-and-hexagonal-architecture, duration: 3h -->
* `DDD` with `Microservices` and `Hexagonal Architecture`
    * Aligning microservice boundaries with bounded contexts
    * Anti-corruption layer for integrating with legacy systems
    * Shared kernel: when and how to share domain concepts
    * `Hexagonal architecture` (ports and adapters) as a foundation for `DDD`
    * Application services and the role of the application layer
    * Infrastructure layer: adapters for persistence, messaging, and external services
    * Testing domain models: unit testing aggregates and domain services
    * Integration testing across bounded contexts
<!-- chapter: refactoring-toward-deeper-insight, duration: 4h -->
* Refactoring Toward Deeper Insight
    * Recognizing implicit concepts in the domain
    * Making implicit concepts explicit in the model
    * Supple design: intention-revealing interfaces, side-effect-free functions, and assertions
    * Refactoring toward deeper models through iterative learning
    * Working with domain experts to refine the model
    * Dealing with large-scale structural changes
    * Common `DDD` pitfalls and anti-patterns
    * Building a culture of continuous domain modeling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
