---
tags:
  - concepts:architecture
  - concepts:microservices
  - concepts:best-practices
level: advanced
category: architecture
duration_hours: 24
audience:
  - audiences:developers
  - audiences:architects
  - audiences:managers
---
<!-- course: legacy_modernization -->
# Legacy Modernization

## Description
This course provides a comprehensive guide to modernizing legacy systems. Participants will learn how to assess legacy systems, choose appropriate modernization strategies, and apply proven patterns such as strangler fig, anti-corruption layer, and branch by abstraction. The course covers technical, organizational, and risk management aspects of modernization, including testing strategies for legacy code, database decomposition, and incremental migration approaches. Real-world case studies illustrate both successes and pitfalls.

## Duration
24 hours / 3 days

## Intended Audience
* Software developers working with or replacing legacy systems
* Software architects planning modernization initiatives
* Engineering managers responsible for modernization budgets and timelines
* Technical leads guiding teams through large-scale system transitions
* Decision-makers evaluating modernization options

## Prerequisites
* Several years of professional software development experience
* Understanding of distributed systems and `microservices` concepts
* Familiarity with common architectural patterns (layered, service-oriented)
* Experience working with at least one large or aging codebase
* Basic understanding of database design and data migration concepts

## Objectives
* Assess legacy systems to determine their modernization readiness and risk profile
* Select the appropriate modernization strategy from the 7 Rs (retain, rehost, replatform, refactor, rearchitect, rebuild, replace)
* Apply the strangler fig pattern for incremental replacement of legacy functionality
* Use anti-corruption layers and branch by abstraction to decouple new code from legacy systems
* Decompose monolithic databases alongside application modernization
* Develop testing strategies for legacy code including characterization tests and golden master testing
* Manage risk, measure progress, and handle organizational challenges during modernization

## Outline
<!-- chapter: legacy-system-assessment, duration: 2h -->
* Legacy System Assessment
    * Defining legacy: what makes a system legacy
    * Assessing business value vs technical quality
    * Technical debt inventory and prioritization
    * Dependency mapping and system analysis
    * Risk and complexity evaluation
    * Stakeholder alignment and expectations
<!-- chapter: modernization-strategies-the-7-rs, duration: 3h -->
* Modernization Strategies: The 7 Rs
    * Retain: keeping the system as is
    * Rehost: lift and shift to new infrastructure
    * Replatform: move with minor optimizations
    * Refactor: restructure code without changing behavior
    * Rearchitect: redesign the system architecture
    * Rebuild: rewrite from scratch with new technology
    * Replace: switch to a commercial or open-source solution
    * Choosing the right strategy for each component
<!-- chapter: the-strangler-fig-pattern, duration: 2h -->
* The Strangler Fig Pattern
    * Concept and motivation
    * Routing and traffic splitting
    * Incremental feature replacement
    * Coexistence of old and new systems
    * Monitoring and validating parity
    * Completing the migration and decommissioning
<!-- chapter: branch-by-abstraction, duration: 1h -->
* Branch by Abstraction
    * Introducing abstraction layers over legacy code
    * Gradual replacement behind abstractions
    * Managing multiple implementations
    * Switching strategies and feature flags
<!-- chapter: anti-corruption-layer, duration: 1h -->
* Anti-Corruption Layer
    * Protecting new systems from legacy models
    * Translation and adaptation patterns
    * Bidirectional vs unidirectional anti-corruption
    * Evolving the anti-corruption layer over time
<!-- chapter: database-decomposition, duration: 2h -->
* Database Decomposition
    * Challenges of shared databases
    * Database wrapping and `API` exposure
    * Data synchronization strategies
    * Event-driven data migration
    * Handling referential integrity across boundaries
    * Schema migration and versioning
<!-- chapter: event-interception-and-api-wrapping, duration: 1h -->
* Event Interception and `API` Wrapping
    * Intercepting events from legacy systems
    * Wrapping legacy functionality with modern APIs
    * Message queues as integration bridges
    * Gradual traffic migration
<!-- chapter: testing-strategies-for-legacy-code, duration: 2h -->
* Testing Strategies for Legacy Code
    * Characterization tests: capturing existing behavior
    * Golden master testing
    * Approval testing techniques
    * Building a safety net before refactoring
    * Contract testing between old and new components
    * Performance baseline comparison
<!-- chapter: working-with-legacy-databases, duration: 1h -->
* Working with Legacy Databases
    * Understanding undocumented schemas
    * Identifying hidden business rules in stored procedures
    * Data quality assessment and cleanup
    * Migration tooling and automation
<!-- chapter: incremental-migration-and-risk-management, duration: 2h -->
* Incremental Migration and Risk Management
    * Phased migration planning
    * Rollback strategies and safety nets
    * Feature flags for migration control
    * Parallel running and shadow testing
    * Managing data consistency during migration
    * Communication and change management
<!-- chapter: organizational-considerations, duration: 2h -->
* Organizational Considerations
    * Team structure and skills assessment
    * Training and knowledge transfer
    * Managing stakeholder expectations
    * Balancing feature delivery with modernization
    * Building organizational support for long-term investment
<!-- chapter: measuring-progress, duration: 2h -->
* Measuring Progress
    * Defining modernization metrics and KPIs
    * Tracking technical debt reduction
    * Monitoring system health during transition
    * Velocity and quality indicators
    * Reporting progress to stakeholders
<!-- chapter: case-studies, duration: 1h -->
* Case Studies
    * Successful modernization examples
    * Common failure patterns and lessons learned
    * Industry-specific considerations
<!-- chapter: when-not-to-modernize, duration: 2h -->
* `When` Not to Modernize
    * Recognizing systems that should be left alone
    * Cost-benefit analysis pitfalls
    * The sunk cost fallacy in modernization
    * Acceptable technical debt

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
