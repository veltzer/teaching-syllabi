---
tags:
  - languages:rust
  - concepts:web-development
  - networking:web
  - concepts:async-programming
  - concepts:rest-api
level: intermediate
category: language
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: rust_for_web_development -->
# `Rust` for Web Development

## Description
This course teaches web development using the `Rust` programming language. Participants will learn how to build production-ready web applications and `REST` APIs using the leading `Rust` web frameworks `Actix Web` and Axum. The course covers asynchronous programming with `Tokio`, database integration using SQLx and Diesel, authentication, middleware, testing strategies, and deployment considerations.

## Duration
24 hours / 3 days

## Intended Audience
`Rust` developers who want to build web applications and `REST` APIs using modern `Rust` web frameworks and the `async` ecosystem.

## Prerequisites
* `Solid` understanding of `Rust` fundamentals (ownership, borrowing, traits, generics)
* Basic knowledge of `HTTP` and `REST` concepts
* Familiarity with `SQL` and relational databases

## Objectives
* Build `REST` APIs using `Actix Web` and Axum
* Write asynchronous `Rust` code using `Tokio` and `async`/`await`
* Integrate databases using SQLx and Diesel
* Implement authentication and authorization in `Rust` web applications
* Write middleware for cross-cutting concerns
* Test web applications at unit, integration, and end-to-end levels
* Deploy `Rust` `web services` to production environments

## Outline
<!-- chapter: introduction-to-web-development-in-rust, duration: 2h -->
* Introduction to Web Development in `Rust`
    * The `Rust` web ecosystem overview
    * Why `Rust` for web development
    * Comparison of `Rust` web frameworks
    * Project structure and tooling
<!-- chapter: asynchronous-rust-with-tokio, duration: 2h -->
* Asynchronous `Rust` with `Tokio`
    * Understanding `async`/`await` in `Rust`
    * The `Tokio` runtime and task scheduling
    * Futures, streams, and combinators
    * Spawning tasks and managing concurrency
    * Error handling in `async` code
<!-- chapter: building-apis-with-actix-web, duration: 3h -->
* Building APIs with `Actix Web`
    * Setting up an `Actix Web` project
    * Routing and request handling
    * Extractors and request data
    * `JSON` serialization with serde
    * Response types and status codes
    * Application state management
<!-- chapter: building-apis-with-axum, duration: 2h -->
* Building APIs with Axum
    * Setting up an Axum project
    * Router and handler functions
    * Extractors and state management
    * Tower middleware integration
    * Comparing Axum and `Actix Web` patterns
<!-- chapter: middleware-and-cross-cutting-concerns, duration: 3h -->
* Middleware and Cross-Cutting Concerns
    * Logging and tracing with tracing
    * CORS configuration
    * Rate limiting
    * Request validation
    * Error handling middleware
    * Custom middleware implementation
<!-- chapter: database-integration-with-sqlx, duration: 2h -->
* Database Integration with SQLx
    * Setting up SQLx with `PostgreSQL` and `SQLite`
    * Compile-time checked queries
    * Migrations management
    * Connection pooling
    * Transactions and error handling
<!-- chapter: database-integration-with-diesel, duration: 2h -->
* Database Integration with Diesel
    * Setting up Diesel and the Diesel `CLI`
    * Schema definition and migrations
    * Query builder and DSL
    * Associations and joins
    * Comparing Diesel and SQLx approaches
<!-- chapter: authentication-and-authorization, duration: 2h -->
* Authentication and Authorization
    * Password hashing and verification
    * `JWT`-based authentication
    * Session management
    * Role-based access control
    * `OAuth2` integration
<!-- chapter: testing-web-applications, duration: 3h -->
* Testing Web Applications
    * Unit testing handlers and services
    * Integration testing with test servers
    * Database testing strategies
    * Mocking external services
    * Property-based testing for APIs
<!-- chapter: deployment-and-production-readiness, duration: 3h -->
* Deployment and Production Readiness
    * Building optimized release binaries
    * Containerizing `Rust` web applications with `Docker`
    * Health checks and graceful shutdown
    * Configuration management
    * Monitoring and observability
    * `CI/CD` pipeline considerations

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
