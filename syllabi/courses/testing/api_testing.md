---
tags:
  - practices:testing
  - concepts:api
  - concepts:rest
  - concepts:grpc
  - practices:contract-testing
level: intermediate
category: testing
duration_hours: 8
audience:
  - audiences:developers
  - audiences:testers
---
<!-- course: api_testing -->
# `API` Testing

## Description
This course covers the essentials of `API` testing, from manual exploration with `Postman` to automated testing and CI integration. Students will learn how to test `REST` and `gRPC` APIs, apply consumer-driven contract testing with Pact, build test automation frameworks, and integrate `API` tests into continuous integration pipelines for reliable and repeatable quality assurance.

## Duration
8 hours / 1 day

## Intended Audience
* Software developers building and consuming APIs
* QA engineers and test automation specialists
* Backend developers responsible for `API` quality

## Prerequisites
* Basic understanding of `HTTP` protocol and `REST` principles
* Experience with at least one programming language
* Familiarity with `JSON` data format
* Basic command-line experience

## Objectives
* Test `REST` and `gRPC` APIs effectively
* Use `Postman` for `API` exploration, testing, and automation
* Apply consumer-driven contract testing with Pact
* Build automated `API` test suites
* Integrate `API` tests into `CI/CD` pipelines

## Outline
<!-- chapter: api-testing-fundamentals, duration: 1h -->
* `API` Testing Fundamentals
    * What is `API` testing and why it matters
    * `API` testing in the testing pyramid
    * Types of `API` tests: functional, integration, contract, performance
    * `REST` vs `gRPC` testing considerations
    * `API` testing strategy and test plan design
<!-- chapter: testing-rest-apis, duration: 1h -->
* Testing `REST` APIs
    * `HTTP` methods: GET, POST, PUT, PATCH, DELETE
    * Status codes and response validation
    * Headers, query parameters, and path parameters
    * Request and response body validation
    * Authentication and authorization testing
    * Error handling and negative testing
<!-- chapter: testing-grpc-apis, duration: 1h -->
* Testing `gRPC` APIs
    * `gRPC` concepts: `protocol buffers`, services, and methods
    * Unary, server streaming, client streaming, and bidirectional calls
    * `gRPC` testing tools: grpcurl, BloomRPC, `Postman`
    * Request and response validation for `protobuf` messages
    * Error codes and status handling
    * Performance characteristics of `gRPC`
<!-- chapter: postman, duration: 1h -->
* `Postman`
    * Workspaces, collections, and environments
    * Building and organizing requests
    * Variables: global, collection, and environment
    * Writing tests with the `Postman` assertion library
    * Collection runner and data-driven testing
    * `Newman` `CLI` for command-line execution
<!-- chapter: contract-testing-with-pact, duration: 1h -->
* Contract Testing with Pact
    * Consumer-driven contract testing concepts
    * Consumer tests and pact generation
    * Provider verification
    * `Pact Broker` for contract sharing and versioning
    * Contract testing vs integration testing
    * Contract testing in `microservices` architectures
<!-- chapter: test-automation, duration: 1h -->
* Test Automation
    * Designing `API` test automation frameworks
    * Test structure and organization
    * Data-driven and parameterized tests
    * Response validation and schema checks
    * Test data management and cleanup
    * Mocking and stubbing external dependencies
<!-- chapter: ci-integration, duration: 2h -->
* CI Integration
    * Running `API` tests in `CI/CD` pipelines
    * `Newman` integration with `Jenkins`, `GitLab CI`, `GitHub Actions`
    * Test reporting and artifact publishing
    * Environment management for `API` tests
    * Parallel test execution
    * Failing builds on test failures
    * Performance gates and quality thresholds

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
