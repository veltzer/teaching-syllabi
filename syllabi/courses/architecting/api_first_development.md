---
tags:
  - architecture:api-design
  - practices:api-first
  - tools:openapi
  - tools:swagger
  - practices:contract-testing
level: intermediate
category: architecture
duration_hours: 16
audience:
  - audiences:architects
  - audiences:developers
---
<!-- course: api_first_development -->
# `API-First` Development

## Description
`API-First` development is a design philosophy where the `API` contract is defined and agreed upon before any implementation begins, enabling parallel development, better collaboration between teams, and more consistent and well-documented interfaces. This course covers the full `API-First` workflow, from designing APIs using the `OpenAPI 3.x` specification to generating server stubs and client SDKs, setting up mock servers, and enforcing contracts through consumer-driven contract testing. Participants will learn `API` design best practices, versioning strategies, documentation tooling, and how to establish `API` governance processes that scale across large engineering organisations. By the end of the course, participants will be equipped to lead an `API-First` initiative within their teams.

## Duration
16 hours / 2 days

## Intended Audience
* Software architects and technical leads defining `API` strategies
* Backend and full-stack developers building web APIs and integrations
* Platform and developer experience engineers managing internal `API` ecosystems
* Frontend and mobile developers consuming and contributing to `API` contracts
* Teams adopting `microservices` and needing clear service boundaries

## Prerequisites
* Familiarity with `REST API` concepts: `HTTP` methods, status codes, headers, and request/response bodies
* Basic understanding of `JSON` and `YAML` formats
* Experience with at least one programming language (e.g., `Python`, `Java`, `TypeScript`, Go)
* Basic knowledge of software architecture and service-oriented design
* Familiarity with version control using `Git`

## Required Knowledge
* `REST API` Fundamentals (or equivalent experience)

## Objectives
* Understand the principles and benefits of `API-First` development
* Write complete and well-structured `OpenAPI 3.x` specifications
* Apply `API` design best practices for resources, naming, error handling, and pagination
* Generate server stubs and client SDKs from `OpenAPI` specifications
* Run mock servers to enable frontend and consumer development before backend implementation
* Implement consumer-driven contract testing to prevent breaking changes
* Apply and evaluate `API` versioning strategies for evolving interfaces
* Produce rich `API` documentation using `Swagger UI` and `Redoc`
* Establish `API` governance guidelines and style guides for organisational consistency

## Outline
<!-- chapter: introduction-to-api-first-design, duration: 1h -->
* Introduction to `API-First` Design
    * What `API-First` means and how it differs from code-first approaches
    * Benefits: parallel development, early feedback, and contract clarity
    * The role of the `API` contract as a communication tool between teams
    * Overview of the `API-First` development workflow
    * `API` design as a product: consumer-centric thinking
    * Common challenges in adopting `API-First` and how to address them
<!-- chapter: openapi-3x-specification, duration: 3h -->
* `OpenAPI 3.x` Specification
    * Structure of an `OpenAPI` document: info, servers, paths, components
    * Defining paths, operations, `HTTP` methods, and parameters
    * Request bodies: `JSON`, `multipart/form-data`, `application/x-www-form-urlencoded`
    * Response definitions: status codes, headers, and response bodies
    * Reusable components: schemas, parameters, responses, request bodies, headers
    * `JSON Schema` for data validation within `OpenAPI`
    * Authentication and security schemes: `Bearer`, `OAuth2`, `API Keys`
    * Links and callbacks for describing complex `API` interactions
    * Writing clear `summary`, description, and `example` fields
    * Tooling: `Swagger Editor`, `Stoplight Studio`, `VS Code` extensions
<!-- chapter: api-design-best-practices, duration: 2h -->
* `API` Design Best Practices
    * Resource modelling: nouns, collections, and sub-resources
    * `HTTP` method semantics: GET, POST, PUT, PATCH, `DELETE`
    * Naming conventions: pluralisation, casing, and clarity
    * Designing consistent and informative error responses (RFC 7807 Problem Details)
    * Pagination patterns: `cursor`-based, offset-based, and keyset pagination
    * Filtering, sorting, and field selection
    * Designing for idempotency and safe retry behaviour
    * Hypermedia and `HATEOAS`: when and whether to apply it
<!-- chapter: code-generation-from-openapi-specs, duration: 2h -->
* Code Generation from `OpenAPI` Specs
    * Overview of code generation tools: `OpenAPI Generator`, `swagger-codegen`
    * Generating server stubs for `Spring Boot`, `FastAPI`, `Express`, and Go
    * Generating client SDKs for `Python`, `TypeScript`, `Java`, and other languages
    * Customising generator templates for project conventions
    * Integrating code generation into `CI/CD` pipelines
    * Keeping generated code and the `OpenAPI` spec in sync
    * Handling generated code in version control: best practices
    * Validating `OpenAPI` specs as part of the build process
<!-- chapter: mock-servers-and-contract-testing, duration: 2h -->
* Mock Servers and Contract Testing
    * Why mock servers accelerate development: frontend/backend parallelism
    * Running mock servers with Prism, `WireMock`, and `Stoplight Prism`
    * Generating realistic mock data from `OpenAPI` schemas
    * Consumer-driven contract testing: the Pact framework
    * Writing consumer contracts and verifying them against providers
    * Integrating contract tests into `CI/CD` workflows
    * Bi-directional contract testing
    * Managing the contract broker: `Pact Broker` and `PactFlow`
<!-- chapter: api-versioning-strategies, duration: 2h -->
* `API` Versioning Strategies
    * Why `API` versioning is necessary and when to introduce breaking changes
    * URL path versioning: `/v1/`, `/v2/`
    * Header-based versioning: `Accept` header and custom headers
    * Query parameter versioning
    * Semantic versioning for `APIs`
    * Managing backwards compatibility: additive changes vs breaking changes
    * Deprecation policies and sunset headers
    * Maintaining multiple `API` versions simultaneously
<!-- chapter: documentation-with-swagger-ui-and-redoc, duration: 2h -->
* Documentation with `Swagger UI` and `Redoc`
    * The importance of live, accurate `API` documentation
    * Setting up `Swagger UI` as an interactive documentation portal
    * Customising `Swagger UI`: branding, theme, and layout
    * `Redoc`: generating `clean`, three-panel reference documentation
    * Writing developer guides and tutorials alongside reference docs
    * Embedding `API` docs into developer portals
    * Automating documentation generation and publishing in `CI/CD`
    * Measuring documentation quality and gathering developer feedback
<!-- chapter: api-governance-and-style-guides, duration: 2h -->
* `API` Governance and Style Guides
    * What is `API` governance and why it matters at scale
    * Creating and enforcing an `API` style guide
    * Automated linting of `OpenAPI` specs with Spectral
    * `API` review processes: design reviews and approval workflows
    * Managing an internal `API` catalogue and developer portal
    * Metrics for `API` health: usage, error rates, latency, and consumer adoption
    * Deprecating and retiring APIs responsibly
    * Building an `API` platform team and centre of excellence

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
