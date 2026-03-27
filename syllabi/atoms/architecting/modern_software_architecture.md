---
tags:
  - architecture
  - microservices
  - cloud-native
  - domain-driven-design
  - distributed-systems
level: advanced
category: architecture
duration_days: 5
audience:
  - developers
  - architects
  - devops
---
# Modern Software Architecture

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This course provides a comprehensive overview of modern software architecture principles and patterns.
It covers the transition from monolithic to microservices-based systems, distributed systems theory,
domain-driven design, cloud-native architecture, and the operational practices that support them.
Participants will learn how to evaluate architectural trade-offs, apply established design patterns,
and architect systems for resiliency, observability, and continuous delivery.

## Duration
40 hours / 5 days

## Intended Audience
* Seasoned developers who are transitioning into an architect role.
* Technical leads responsible for system design and architectural decisions.
* Software architects who want to update their knowledge of modern patterns and practices.
* `DevOps` engineers who want a deeper understanding of the architectures they support.

## Prerequisites
* Several years of experience in software development.
* Familiarity with web services, `REST` `APIs`, and basic networking concepts.
* Basic understanding of containers and cloud computing.

## Objectives
* Understand the principles behind modern distributed system architectures
* Evaluate trade-offs between different architectural styles and communication patterns
* Apply Domain-Driven Design to define service boundaries
* Identify and use common microservices design patterns
* Design cloud-native applications following the 12-Factor App methodology
* Architect systems for resiliency, observability, and continuous delivery

## Exercises
* This is a theoretical course, it does not include exercises.

## Outline
* Foundations and Communication Patterns
    * Introduction to Modern Software Architecture
        * The transition from Monoliths to Microservices
        * Architectural drivers and Quality Attributes
        * Evaluating trade-offs in modern design
    * Distributed Systems Theory
        * The CAP Theorem and its practical implications
        * Fallacies of distributed computing
        * High availability and fault tolerance strategies
    * Communication Patterns
        * Synchronous vs Asynchronous communication
        * `RESTful` `API` design and best practices
        * `gRPC` and `Protocol Buffers` for high performance
        * Message brokers and Event-Driven Architecture (EDA)
* Domain Driven Design and Microservices Patterns
    * Domain Driven Design (DDD)
        * Strategic design involving Bounded Contexts and Ubiquitous Language
        * Tactical design focusing on Entities, Value Objects, Aggregates, and Services
        * Mapping domains to microservice boundaries
    * Microservices Design Patterns
        * `API` Gateway and Backend for Frontends (BFF)
        * Service Discovery and Load Balancing
        * Data Management strategies including Database per Service and Shared Database
        * Saga Pattern for distributed transactions
        * `CQRS` and Event Sourcing
* Cloud Native Architecture and Container Recap
    * Cloud Native Principles
        * The 12-Factor App methodology
        * Stateless vs Stateful services
        * Designing for elasticity and scalability
    * Containerization Recap (Brief Overview)
        * `Docker` ecosystem refresher
        * Optimizing container images for production
        * Best practices for containerized deployments
    * Orchestration with `Kubernetes` (Brief Overview)
        * Core components including Pods, Services, Deployments, and ConfigMaps
        * Managing configurations and secrets
        * Health checks and self-healing mechanisms
* Resiliency, Observability, and `DevOps`
    * Architecting for Resiliency
        * Circuit Breakers, Retries, and Timeouts
        * Bulkheads and rate limiting
        * Chaos Engineering concepts
    * Monitoring and Observability
        * Role of Observability in modern architecture
        * The Three Pillars including Metrics, Logging, and Tracing
        * Distributed Tracing with `OpenTelemetry`
        * Monitoring tools and health check strategies
    * `DevOps` and `CI/CD` for Architects
        * Infrastructure as Code (`IaC`) principles
        * Deployment strategies including Blue/Green, Canary, and Rolling updates
        * The role of the Architect in the `DevOps` lifecycle

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
