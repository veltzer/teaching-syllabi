---
tags:
  - architecture:clean-architecture
  - architecture:hexagonal
  - concepts:ports-and-adapters
  - practices:solid
level: advanced
category: architecture
duration_hours: 16
audience:
  - audiences:architects
  - audiences:senior-developers
---
<!-- course: clean_and_hexagonal_architecture -->
# `Clean Architecture` and `Hexagonal Architecture`

## Description
`Clean Architecture` and `Hexagonal Architecture` (also known as `Ports and Adapters`) are two closely related architectural patterns that promote the design of software systems where business logic is independent of frameworks, databases, user interfaces, and external services. This course explores the foundational principles behind both patterns, including the dependency rule, layer separation, ports and adapters, and the role of dependency injection in keeping the core domain decoupled from infrastructure concerns. Participants will learn to apply `SOLID` principles in the context of these architectures, implement each layer in a real application, and write highly testable code. The course also examines how Clean and `Hexagonal Architecture` compare with layered, onion, and other common patterns.

## Duration
16 hours / 2 days

## Intended Audience
* Software architects designing maintainable and testable systems
* Senior developers working to improve the structure of complex applications
* Technical leads introducing architectural standards across engineering teams
* Backend engineers seeking to decouple business logic from frameworks and infrastructure
* Developers refactoring legacy codebases toward cleaner designs

## Prerequisites
* `Solid` proficiency in at least one object-oriented language (e.g., `Java`, `C#`, `Python`, `TypeScript`)
* Familiarity with `SOLID` principles and object-oriented design
* Experience with layered or `MVC` architectures in production systems
* Basic understanding of dependency injection and inversion of control
* Familiarity with unit testing and test-driven development concepts

## Required Knowledge
* Object-Oriented Design Fundamentals (or equivalent experience)
* Software Architecture Fundamentals (or equivalent experience)

## Objectives
* Understand the goals and principles behind `Clean Architecture` and `Hexagonal Architecture`
* Apply the dependency rule to enforce separation between domain and infrastructure layers
* Design entities, use cases, and interface adapters for a real application
* Implement ports and adapters to decouple business logic from external systems
* Use dependency injection to wire application layers without coupling
* Write comprehensive unit and integration tests for each architectural layer
* Evaluate the trade-offs of Clean and `Hexagonal Architecture` vs alternative patterns
* Refactor existing code toward a cleaner, more maintainable architectural structure

## Outline
<!-- chapter: introduction-to-clean-architecture, duration: 2h -->
* Introduction to `Clean Architecture`
    * The origins and goals of `Clean Architecture` (Robert C. Martin)
    * Problems that `Clean Architecture` solves: framework lock-in, untestability, rigidity
    * The concentric circles model: entities, use cases, interface adapters, frameworks
    * The dependency rule: source code dependencies must point inward
    * What should and should not cross layer boundaries
    * Comparing `Clean Architecture` with traditional layered (`N-tier`) architecture
    * Real-world examples of applications following `Clean Architecture`
    * Common misunderstandings and pitfalls
<!-- chapter: dependency-rule-and-layer-separation, duration: 2h -->
* Dependency Rule and Layer Separation
    * Enforcing the dependency rule in code: techniques and patterns
    * Domain layer isolation: no dependencies on frameworks or infrastructure
    * Application layer: orchestrating use cases without exposing domain internals
    * Infrastructure layer: persistence, messaging, external APIs as implementation details
    * Crossing layer boundaries: data transfer objects and mappers
    * Dependency inversion principle applied to architecture
    * Package and module structure reflecting architectural boundaries
    * Code organization strategies for `Clean Architecture` projects
<!-- chapter: entities-and-use-cases, duration: 2h -->
* Entities and Use Cases
    * Entities: encapsulating enterprise-wide business rules
    * Value objects and their role in the domain model
    * Designing rich domain models vs anemic domain models
    * Use cases (interactors): representing application-specific business rules
    * Input and output ports: defining use case contracts
    * Request and response models for use case boundaries
    * Use case composition and shared domain logic
    * Validating business rules within entities and use cases
<!-- chapter: interface-adapters, duration: 2h -->
* Interface Adapters
    * The role of interface adapters in `Clean Architecture`
    * Controllers: translating `HTTP` requests into use case inputs
    * Presenters and view models: formatting output for delivery mechanisms
    * Gateways and repository interfaces: abstracting data access
    * Implementing repository interfaces with `SQL`, `NoSQL`, and in-memory stores
    * Mapping between domain models and persistence models
    * `REST`, `GraphQL`, and `gRPC` adapters as delivery mechanisms
    * Handling cross-cutting concerns: logging, authentication, error handling
<!-- chapter: ports-and-adapters-hexagonal-architecture, duration: 2h -->
* Ports and Adapters: `Hexagonal Architecture`
    * Origins of `Hexagonal Architecture` (Alistair Cockburn)
    * The hexagon metaphor: application at the center, adapters at the edges
    * Driving (primary) ports: `API`, `CLI`, message consumer interfaces
    * Driven (secondary) ports: repository, email, external service interfaces
    * Primary adapters: `REST` controllers, `CLI` runners, message consumers
    * Secondary adapters: database repositories, `SMTP` clients, `HTTP` clients
    * Comparing `Hexagonal Architecture` with `Clean Architecture`
    * Implementing `Hexagonal Architecture` in a complete application example
<!-- chapter: dependency-injection-in-practice, duration: 2h -->
* Dependency Injection in Practice
    * Dependency injection as the mechanism for wiring layers together
    * Constructor injection vs property injection vs method injection
    * `DI` containers and frameworks: Spring, `Guice`, `Autofac`, `FastAPI Depends`
    * Composition root: where to wire the application together
    * Managing object lifecycles: singleton, scoped, transient
    * Avoiding the service locator anti-pattern
    * Testing with `DI`: swapping real adapters for test doubles
    * Structuring `DI` configuration for large applications
<!-- chapter: testing-clean-architecture, duration: 2h -->
* Testing `Clean Architecture`
    * Testing philosophy aligned with `Clean Architecture`
    * Unit testing entities and use cases in isolation
    * Mocking ports and adapters for fast, deterministic tests
    * Integration testing adapters against real infrastructure
    * End-to-end testing across all layers
    * Test pyramid strategy for `Clean Architecture` projects
    * Contract testing for ports: ensuring adapters honor port contracts
    * Refactoring toward testability using the dependency rule
<!-- chapter: comparing-clean-and-hexagonal-with-other-patterns, duration: 2h -->
* Comparing Clean and `Hexagonal` with Other Patterns
    * Revisiting layered (N-tier) architecture: strengths and weaknesses
    * Onion architecture: similarities and differences with `Clean Architecture`
    * `CQRS` and `Event Sourcing` alongside `Clean Architecture`
    * `Domain-Driven Design` and its relationship to `Clean Architecture`
    * `Microservices` architecture and applying `Clean Architecture` within services
    * `When` Clean or `Hexagonal Architecture` is the right choice
    * Incremental migration strategies for existing codebases
    * Governance and team adoption: enforcing architectural boundaries at scale

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
