---
tags:
  - tools:testcontainers
  - practices:integration-testing
  - tools:docker
  - practices:testing
level: intermediate
category: testing
duration_hours: 16
audience:
  - audiences:developers
---
<!-- course: testcontainers -->
# `Testcontainers`

## Description
This course explores `Testcontainers`, the open-source library that enables developers to run real service dependencies inside `Docker` containers as part of automated integration tests. Students will learn to replace fragile in-memory fakes with production-equivalent databases, message brokers, and other infrastructure, making integration tests reliable and portable across developer machines and CI environments. The course covers `Java`, `Python`, and Go flavours of the library, as well as advanced topics such as network configuration, `Docker` Compose support, and parallelism. Participants will leave with a practical approach to writing integration tests that test the whole stack without shared external environments.

## Duration
16 hours / 2 days

## Intended Audience
* Backend developers writing integration tests for services that depend on databases, queues, or other infrastructure
* Engineers who want to eliminate "it works on my machine" problems in test environments

## Prerequisites
* `Solid` experience in at least one of `Java`, `Python`, or Go
* Familiarity with `Docker` concepts: images, containers, and `docker-compose`
* Basic experience writing integration or unit tests in any language

## Objectives
* Articulate the challenges of integration testing with shared environments and explain how `Testcontainers` solves them
* Understand the `Testcontainers` architecture and its relationship with the `Docker` daemon
* Write integration tests for `Java` applications using `JUnit 5` and `Testcontainers`
* Use pre-built container modules for `PostgreSQL`, `MySQL`, `MongoDB`, and other databases
* Test message-driven applications with `Kafka` and `RabbitMQ` containers
* Create and configure generic and custom containers
* Write `Testcontainers` tests in `Python` and Go
* Configure container networks and multi-container topologies
* Use `Docker` Compose support for complex setups
* Apply parallelism and container reuse to optimise test suite performance
* Integrate `Testcontainers` into `CI/CD` pipelines reliably

## Outline
<!-- chapter: introduction-to-integration-testing-challenges, duration: 1h -->
* Introduction to Integration Testing Challenges
    * The testing pyramid and the role of integration tests
    * Problems with shared test environments: flakiness, data conflicts, version drift
    * In-memory fakes vs real dependencies: trade-offs
    * How `Testcontainers` addresses these challenges
    * Overview of the `Testcontainers` ecosystem and language support
<!-- chapter: testcontainers-architecture, duration: 1h -->
* `Testcontainers` Architecture
    * How `Testcontainers` communicates with the `Docker` daemon
    * The `Ryuk` container and automatic resource cleanup
    * Container lifecycle: start, wait, stop, remove
    * Wait strategies: port, `HTTP`, log, health check
    * Environment requirements: `Docker` on developer machines and CI
    * `Testcontainers Cloud` for environments without local `Docker`
<!-- chapter: getting-started-java-and-junit, duration: 2h -->
* Getting Started: `Java` and `JUnit`
    * Adding `Testcontainers` dependencies to a `Maven` or `Gradle` project
    * The `@Testcontainers` and `@Container` `JUnit` 5 annotations
    * Container lifecycle with `@Container` as a field
    * Static vs instance container fields and their lifecycle implications
    * Accessing container connection properties at runtime
    * Writing a first integration test against a `PostgreSQL` container
<!-- chapter: database-containers, duration: 2h -->
* Database Containers
    * Pre-built modules: `PostgreSQLContainer`, MySQLContainer, MariaDBContainer, `MSSQLServerContainer`
    * Initialising schemas with `SQL` scripts and init files
    * Connecting with `JDBC` and `R2DBC` URL rewriting
    * `MongoDB` container for document store integration tests
    * Flyway and `Liquibase` schema migration in tests
    * Testing repository and DAO layers with real query behaviour
<!-- chapter: message-broker-containers, duration: 2h -->
* Message Broker Containers
    * `KafkaContainer` setup and configuration
    * Producing and consuming messages in integration tests
    * Testing consumer groups, topics, and partitions
    * `RabbitMQContainer` and `AMQP` testing
    * `LocalStackContainer` for `AWS` service simulation
    * Verifying message-driven workflows end to end
<!-- chapter: custom-and-generic-containers, duration: 2h -->
* Custom and Generic Containers
    * `GenericContainer` for images without a dedicated module
    * Setting environment variables, exposed ports, and command overrides
    * Mounting volumes and copying files into containers
    * Building images from a `Dockerfile` with `ImageFromDockerfile`
    * Waiting for custom readiness conditions
    * Reusing custom containers across multiple tests
<!-- chapter: testcontainers-with-python-and-go, duration: 2h -->
* `Testcontainers` with `Python` and Go
    * `testcontainers-python`: installation and basic usage
    * Writing database integration tests in `Python` with `pytest`
    * Container configuration and wait strategies in `Python`
    * `testcontainers-go`: installation and basic usage
    * Integration tests in Go with database and message broker containers
    * Comparing the APIs across `Java`, `Python`, and Go
<!-- chapter: network-and-compose-support, duration: 2h -->
* Network and Compose Support
    * Creating isolated `Docker` networks for multi-container tests
    * Connecting containers to the same network
    * Aliasing containers for inter-container hostname resolution
    * `DockerComposeContainer` for existing Compose files
    * Overriding services and scaling in Compose-based tests
    * Limitations of Compose support and when to use programmatic networks instead
<!-- chapter: performance-and-parallelism, duration: 1h -->
* Performance and Parallelism
    * Container startup overhead and strategies to minimise it
    * Container reuse with `withReuse(true)` and its trade-offs
    * Using `@Container` at class scope to share across tests
    * Parallel test execution and container isolation
    * Pre-pulling images in CI to reduce cold-start times
    * Selecting minimal base images for faster startup
<!-- chapter: cicd-integration, duration: 1h -->
* `CI/CD` Integration
    * Running `Testcontainers` in `GitHub Actions`, `GitLab CI`, and `Jenkins`
    * `Docker`-in-`Docker` vs `Docker` socket mounting in CI
    * Configuring `Testcontainers` via environment variables in CI
    * Handling resource limits and timeout configuration
    * Caching `Docker` images between CI runs
    * `Testcontainers Cloud` as a CI-friendly alternative

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
