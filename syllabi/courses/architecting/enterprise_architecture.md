---
tags:
  - concepts:architecture
  - concepts:distributed-systems
  - concepts:microservices
  - concepts:design-patterns
level: advanced
category: architecture
duration_hours: 24
audience:
  - audiences:architects
  - audiences:team-leads
  - audiences:managers
  - audiences:developers
---
<!-- course: enterprise_architecture -->
# Enterprise Architecture

## Description
Enterprise architecture provides the strategic framework for aligning IT infrastructure with business goals. This course covers major architecture frameworks such as TOGAF and Zachman, integration patterns, service-oriented architecture, `API` management, and cloud migration strategies. Students will learn to `make` and document architecture decisions, establish governance processes, and evaluate technologies for enterprise-scale systems.

## Duration
24 hours / 3 days

## Intended Audience
* Architects designing enterprise-scale systems
* Team leads making technology and integration decisions
* Managers overseeing IT strategy and digital transformation
* Senior developers transitioning to architecture roles

## Prerequisites
* Several years of software development or IT experience
* Familiarity with distributed systems concepts
* Understanding of `web services` and APIs

## Objectives
* Apply architecture frameworks (TOGAF, Zachman) to enterprise planning
* Design integration solutions using enterprise integration patterns
* Evaluate `SOA`, ESB, and `microservices` approaches
* Define `API` management and governance strategies
* Plan cloud migration using proven patterns
* Create and maintain architecture decision records

## Outline
<!-- chapter: architecture-frameworks, duration: 4h -->
* Architecture Frameworks
    * What is enterprise architecture
    * TOGAF (The Open Group Architecture Framework)
        * Architecture Development Method (ADM)
        * Architecture domains (business, data, application, technology)
        * Architecture repository and building blocks
        * Stakeholder management
    * Zachman Framework
        * The classification matrix
        * Perspectives and abstractions
        * Practical application
    * Comparing frameworks
    * Tailoring frameworks to organizational needs
<!-- chapter: enterprise-integration-patterns, duration: 2h -->
* Enterprise Integration Patterns
    * Point-to-point vs hub-and-spoke vs bus
    * Messaging patterns (message channel, message router, message translator)
    * Message construction patterns
    * Routing patterns (content-based router, splitter, aggregator)
    * Transformation patterns
    * Endpoint patterns
    * Idempotent receivers
    * Dead letter channels
<!-- chapter: service-oriented-architecture-soa, duration: 2h -->
* Service-Oriented Architecture (`SOA`)
    * `SOA` principles and design
    * Service contracts and interfaces
    * Service composition and orchestration
    * Service registry and discovery
    * `SOA` governance
    * `SOA` vs `microservices`
<!-- chapter: enterprise-service-bus-esb, duration: 2h -->
* Enterprise Service Bus (ESB)
    * ESB architecture and capabilities
    * Mediation and routing
    * Protocol transformation
    * ESB products overview
    * `When` to use and when to avoid ESB
    * `Event-driven architecture` as an alternative
<!-- chapter: message-brokers, duration: 2h -->
* Message Brokers
    * Message broker architectures
    * `RabbitMQ`, `Apache Kafka`, `ActiveMQ`
    * Pub/sub vs point-to-point
    * Message durability and delivery guarantees
    * `Event sourcing` and `CQRS`
    * Choosing the right broker
<!-- chapter: api-management, duration: 2h -->
* `API` Management
    * `API` strategy and lifecycle
    * `API gateway` patterns
    * Rate limiting and throttling
    * `API` versioning strategies
    * Developer portals and documentation
    * `API` security (`OAuth 2.0`, ```API`` keys`, `JWT`)
    * `API` monetization
<!-- chapter: data-architecture, duration: 2h -->
* Data Architecture
    * Data modeling at enterprise scale
    * Master data management
    * Data governance and quality
    * Data lakes and data warehouses
    * `ETL` vs `ELT` patterns
    * Data mesh concepts
    * Data lineage and cataloging
<!-- chapter: security-architecture, duration: 2h -->
* Security Architecture
    * Security architecture principles
    * Identity and access management (`IAM`)
    * Single sign-on (SSO) and federation
    * Zero trust architecture
    * Encryption strategies
    * Compliance and regulatory requirements
    * Threat modeling
<!-- chapter: cloud-migration-patterns, duration: 2h -->
* Cloud Migration Patterns
    * Migration strategies (rehost, refactor, rearchitect, rebuild, replace)
    * Cloud readiness assessment
    * Hybrid cloud architecture
    * Multi-cloud strategies
    * Landing zone design
    * Cost optimization
    * Migration execution planning
<!-- chapter: architecture-governance, duration: 1h -->
* Architecture Governance
    * Governance frameworks and processes
    * Architecture review boards
    * Compliance monitoring
    * Architecture debt management
    * Standards and guidelines
<!-- chapter: architecture-decision-records, duration: 1h -->
* Architecture Decision Records
    * ADR format and structure
    * Documenting context, decision, and consequences
    * Lightweight ADR practices
    * ADR tooling and management
    * Decision lifecycle
<!-- chapter: technology-radar, duration: 2h -->
* Technology Radar
    * Building a technology radar
    * Assess, trial, adopt, hold categories
    * Technology evaluation criteria
    * Innovation management
    * Communicating technology strategy

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
