---
tags:
  - practices:testing
  - concepts:microservices
  - concepts:api
level: intermediate
category: testing
duration_hours: 16
audience:
  - audiences:developers
  - audiences:testers
  - audiences:architects
---
<!-- course: contract_testing -->
# Contract Testing

## Description
Contract testing ensures that services in a distributed system communicate correctly by verifying that both consumers and providers adhere to a shared contract. This course covers consumer-driven contract testing with Pact, bi-directional contract testing, and contract testing for `REST`, `GraphQL`, and messaging systems. Participants will learn how to integrate contract testing into their workflows and understand `when` to use it versus integration testing.

## Duration
16 hours / 1 day

## Intended Audience
* Backend developers building `microservices` and distributed systems
* QA engineers working with service-oriented architectures
* Full-stack developers consuming and providing APIs
* Technical leads responsible for testing strategy in `microservices`

## Prerequisites
* Experience with `REST APIs` and `HTTP` fundamentals
* Understanding of `microservices` architecture concepts
* Familiarity with at least one programming language (`JavaScript`, `Java`, `Python`, or `Go`)
* Basic understanding of `JSON` and `API` schemas
* Experience with automated testing frameworks

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)

## Objectives
* Understand the principles and value of contract testing
* Implement consumer-driven contract tests using the Pact framework
* Set up and use `Pact Broker` for contract management
* Apply bi-directional contract testing with `Pactflow`
* Test contracts for `REST APIs`, `GraphQL`, and messaging systems
* Validate contracts against `OpenAPI` and AsyncAPI specifications
* Integrate contract testing into `CI/CD` pipelines
* Determine `when` contract testing is appropriate versus integration testing

## Outline
<!-- chapter: contract-testing-concepts, duration: 2h -->
* Contract Testing Concepts
    * What is contract testing and why it matters
    * Consumer-driven contracts explained
    * The problem with end-to-end integration tests at scale
    * Contract testing in the testing pyramid
    * Provider contracts vs consumer contracts
    * Contract testing vs integration testing: trade-offs
    * `When` to use contract testing and `when` not to
<!-- chapter: the-pact-framework, duration: 2h -->
* The Pact Framework
    * Pact overview and supported languages
    * Consumer test workflow: defining expectations
    * Generating pact files from consumer tests
    * Provider verification: replaying pact interactions
    * The Pact specification and versioning
    * Writing consumer tests in `JavaScript`, `Java`, and `Python`
    * Running provider verification tests
    * Handling provider states for test setup
<!-- chapter: pact-broker, duration: 2h -->
* `Pact Broker`
    * What is `Pact Broker` and why it is needed
    * Setting up `Pact Broker` (self-hosted and `Pactflow` `SaaS`)
    * Publishing pacts from consumer builds
    * Retrieving pacts for provider verification
    * Version tagging and environment tracking
    * The can-i-deploy tool for safe deployments
    * Visualizing dependencies with the network diagram
<!-- chapter: bi-directional-contract-testing, duration: 1h -->
* Bi-Directional Contract Testing
    * Bi-directional contract testing concepts
    * Provider-driven contracts with `OpenAPI` specifications
    * Comparing consumer pacts against provider `OpenAPI` specs
    * `Pactflow` bi-directional contract testing workflow
    * Benefits over traditional consumer-driven approach
    * `When` to use bi-directional vs consumer-driven contracts
<!-- chapter: contract-testing-for-rest-apis, duration: 1h -->
* Contract Testing for `REST APIs`
    * Defining `HTTP` interactions in pacts
    * Matching rules: exact, type, regex, and flexible matchers
    * Testing request headers, query parameters, and body
    * Testing response status codes, headers, and body
    * Handling authentication in contract tests
    * Versioning and backwards compatibility verification
<!-- chapter: contract-testing-for-graphql, duration: 1h -->
* Contract Testing for `GraphQL`
    * Challenges of testing `GraphQL` contracts
    * Defining `GraphQL` query and mutation interactions
    * Matching `GraphQL` request and response structures
    * Handling variable inputs and partial responses
    * Tools and techniques for `GraphQL` contract testing
<!-- chapter: contract-testing-for-messaging-and-events, duration: 1h -->
* Contract Testing for Messaging and Events
    * Asynchronous messaging contract challenges
    * Message pacts in Pact
    * Testing event producers and consumers
    * Schema validation for message formats
    * Contract testing with AsyncAPI specifications
    * `Event-driven architecture` contract patterns
<!-- chapter: pending-pacts-and-work-in-progress, duration: 1h -->
* Pending Pacts and Work in Progress
    * The pending pacts feature
    * Work in progress (WIP) pacts
    * Handling new consumers without breaking provider builds
    * Gradual rollout of contract changes
    * Managing contract evolution over time
<!-- chapter: spring-cloud-contract, duration: 1h -->
* `Spring Cloud Contract`
    * Overview of `Spring Cloud Contract`
    * Defining contracts in `Groovy` or `YAML`
    * Auto-generated tests for the provider
    * Stubs for consumer testing
    * Integration with `Spring Boot` test infrastructure
    * Comparing `Spring Cloud Contract` with Pact
<!-- chapter: ci-cd-integration, duration: 2h -->
* `CI/CD` Integration
    * Contract testing in the build pipeline
    * Publishing and verifying contracts automatically
    * Using can-i-deploy as a pipeline gate
    * Webhooks for triggering provider verification
    * Branch and environment-aware contract testing
    * Handling failures and debugging contract mismatches
<!-- chapter: organizational-adoption, duration: 2h -->
* Organizational Adoption
    * Introducing contract testing to a team
    * Starting with critical service boundaries
    * Scaling contract testing across many services
    * Governance and ownership of contracts
    * Monitoring contract test health and coverage
    * Common pitfalls and how to avoid them

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
