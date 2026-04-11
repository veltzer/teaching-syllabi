---
tags:
  - languages:java
  - tools:spring
  - concepts:web-development
level: intermediate
category: language
duration_hours: 32
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: spring_boot -->
# `Spring Boot` Development

## Description
This course provides a comprehensive guide to building enterprise-grade applications with `Spring Boot`. Starting from auto-configuration and the `Spring` core concepts of dependency injection and bean lifecycle, the course covers `REST API` development, data persistence with `Spring Data JPA`, security with `Spring Security`, configuration management, testing, and deployment. Students will gain the skills to build robust, production-ready `Java` applications.

## Duration
32 hours / 4 days

## Intended Audience
* `Java` developers building backend applications and `microservices`
* Software engineers transitioning to the `Spring` ecosystem
* Backend developers looking to adopt modern `Java` development practices
* Full-stack developers who need robust server-side application frameworks
* Architects evaluating `Spring Boot` for enterprise applications

## Prerequisites
* Intermediate proficiency in `Java` programming (classes, interfaces, generics, annotations)
* Understanding of object-oriented programming principles
* Basic knowledge of `HTTP` protocol and `REST API` concepts
* Familiarity with build tools (`Maven` or `Gradle`)
* Basic understanding of relational databases and `SQL`
* Experience with an IDE such as `IntelliJ IDEA` or `Eclipse`
* Command-line interface usage and basic terminal operations

## Objectives
* Understand `Spring Boot` auto-configuration, starters, and embedded servers
* Apply `Spring` core concepts: dependency injection, bean lifecycle, and component scanning
* Build `RESTful APIs` with proper request handling, validation, and error responses
* Implement data persistence using `Spring Data JPA` with repositories, queries, and pagination
* Secure applications with `Spring Security`, `OAuth2`, and `JWT` authentication
* Manage application configuration using properties, profiles, and externalized config
* Monitor applications with `Spring Boot Actuator`
* Write comprehensive tests using MockMvc and TestRestTemplate
* Deploy `Spring Boot` applications with `Docker` and production-ready practices

## Outline
<!-- chapter: introduction-to-spring-boot, duration: 3h -->
* Introduction to `Spring Boot`
    * Overview of the `Spring` ecosystem and `Spring Boot`
    * Auto-configuration and the opinionated defaults philosophy
    * `Spring Boot` starters and dependency management
    * Embedded servers: `Tomcat`, `Jetty`, and Undertow
    * Creating a project with `Spring Initializr`
    * Project structure and the main application class
    * Running and debugging `Spring Boot` applications
<!-- chapter: spring-core-concepts, duration: 3h -->
* `Spring` Core Concepts
    * The `IoC` container and application context
    * Dependency injection: constructor, setter, and field injection
    * Bean lifecycle and scopes
    * Component scanning and stereotype annotations (@Component, @Service, @Repository, @Controller)
    * Configuration classes and @Bean methods
    * Profiles and conditional bean registration
    * SpEL (`Spring` Expression Language)
<!-- chapter: building-rest-apis, duration: 4h -->
* Building `REST` APIs
    * @RestController and request mapping annotations
    * Path variables, query parameters, and request body handling
    * Response entities and status codes
    * Content negotiation and `JSON` serialization with Jackson
    * Request validation with `Bean Validation` (@Valid, @NotNull, @Size)
    * Custom validators and validation groups
    * `HATEOAS` and hypermedia-driven APIs
    * `API` documentation with `SpringDoc OpenAPI`
<!-- chapter: spring-data-jpa, duration: 4h -->
* `Spring Data JPA`
    * Introduction to `JPA` and `Hibernate` with `Spring Boot`
    * Entity mapping: annotations, relationships, and inheritance
    * Repository interfaces and derived query methods
    * Custom queries with JPQL and native `SQL`
    * Pagination and sorting
    * Specifications and dynamic queries
    * Auditing and entity lifecycle callbacks
    * Database migrations with `Flyway` and `Liquibase`
    * Transaction management and propagation
<!-- chapter: spring-security, duration: 4h -->
* `Spring Security`
    * Introduction to `Spring Security` architecture
    * Security filter chain and configuration
    * Authentication: in-memory, database, and custom providers
    * Password encoding with BCrypt
    * Authorization: role-based and method-level security
    * `OAuth2` and `OpenID Connect` integration
    * `JWT` token authentication and stateless sessions
    * CORS and `CSRF` configuration
    * Security headers and best practices
<!-- chapter: configuration-and-externalization, duration: 3h -->
* Configuration and Externalization
    * Application properties and `YAML` configuration
    * Configuration properties binding with @ConfigurationProperties
    * Profiles for environment-specific configuration
    * Externalized configuration: environment variables, command-line arguments
    * Property sources and configuration precedence
    * Secrets management strategies
<!-- chapter: actuator-monitoring-and-logging, duration: 3h -->
* Actuator, Monitoring, and Logging
    * `Spring Boot Actuator` endpoints and configuration
    * Health checks and readiness/liveness probes
    * Metrics collection and exposure
    * Integration with `Prometheus` and `Grafana`
    * Logging with SLF4J and Logback
    * Log levels, patterns, and `file` appenders
    * Structured logging for production environments
<!-- chapter: exception-handling-and-validation, duration: 2h -->
* Exception Handling and Validation
    * Global exception handling with @ControllerAdvice
    * Custom error responses and problem details
    * Exception handling strategies and best practices
    * Input validation and error message customization
    * Handling constraint violations and data integrity errors
<!-- chapter: testing-spring-boot-applications, duration: 3h -->
* Testing `Spring Boot` Applications
    * Testing with @SpringBootTest and test slices
    * Unit testing services and repositories
    * Testing `REST` controllers with MockMvc
    * Integration testing with TestRestTemplate and WebTestClient
    * Mocking dependencies with `Mockito`
    * Test containers for database integration testing
    * Test configuration and profiles
<!-- chapter: deployment-and-production-readiness, duration: 3h -->
* Deployment and Production Readiness
    * Building executable JAR and WAR files
    * `Docker` containerization of `Spring Boot` applications
    * Multi-stage `Docker` builds for optimized images
    * Graceful shutdown and lifecycle management
    * Database migration strategies for production
    * Performance tuning: connection pools, thread pools, and caching
    * Deploying to cloud platforms and container orchestrators

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
