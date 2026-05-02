---
tags:
  - languages:go
  - concepts:microservices
  - concepts:programming
  - networking:grpc
  - concepts:testing
  - tools:docker
  - infrastructure:kubernetes
level: intermediate
category: language
duration_hours: 16
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: go_for_microservices -->
# Go for `Microservices`

## Description
This course teaches how to build production-ready `microservices` in Go. It covers building `gRPC` and `REST` APIs, containerization with `Docker`, deployment to `Kubernetes`, observability, middleware patterns, dependency injection, database integration, and testing strategies for distributed systems.

## Duration
16 hours / 2 days

## Intended Audience
* Go developers building backend services and APIs
* Teams adopting `microservices` architecture with Go
* Backend engineers moving from monolithic to distributed systems

## Prerequisites
* Working knowledge of Go programming
* Basic understanding of `HTTP` and `REST` concepts

## Required Knowledge
* `Docker` Fundamentals (or equivalent container experience)
* Introduction to `Kubernetes` (or equivalent `Kubernetes` experience)

## Objectives
* Build `gRPC` and `REST API` services in Go
* Containerize Go services with `Docker` and deploy to `Kubernetes`
* Implement observability with structured logging, metrics, and tracing
* Apply middleware, dependency injection, and `clean architecture` patterns
* Write effective tests for `microservices` including integration and end-to-end tests

## Outline
<!-- chapter: rest-api-development, duration: 2h -->
* `REST API` Development
    * Designing `RESTful APIs` in Go
    * The net/`http` standard library
    * Routing with popular routers (chi, gorilla/mux)
    * Request validation and error handling
    * `JSON` serialization and content negotiation
    * `API` versioning strategies
<!-- chapter: grpc-services, duration: 2h -->
* `gRPC` Services
    * Introduction to `gRPC` and `Protocol Buffers`
    * Defining service contracts with .proto files
    * Generating Go code with protoc
    * Unary, server-streaming, client-streaming, and bidirectional RPCs
    * Error handling and status codes in `gRPC`
    * `gRPC` interceptors
    * `gRPC`-Gateway for `REST` compatibility
<!-- chapter: middleware-and-cross-cutting-concerns, duration: 2h -->
* Middleware and Cross-Cutting Concerns
    * `HTTP` middleware patterns in Go
    * Authentication and authorization middleware
    * Rate limiting and throttling
    * Request `ID` propagation
    * CORS handling
    * Graceful shutdown
<!-- chapter: dependency-injection, duration: 1h -->
* Dependency Injection
    * Dependency injection patterns in Go
    * Constructor injection and interface-based design
    * Using wire for compile-time dependency injection
    * Structuring services with `clean architecture`
<!-- chapter: database-integration, duration: 2h -->
* Database Integration
    * Working with database/`sql` and connection pooling
    * Using sqlx for enhanced database operations
    * `ORM` usage with GORM
    * Database migrations
    * Repository pattern
    * Transaction management
<!-- chapter: containerizing-go-services, duration: 1h -->
* Containerizing Go Services
    * Writing optimized Dockerfiles for Go
    * Multi-stage builds for minimal images
    * Building scratch and distroless containers
    * Health checks and container configuration
<!-- chapter: deploying-go-services-to-kubernetes, duration: 2h -->
* Deploying Go Services to `Kubernetes`
    * Deployments and services for Go `microservices`
    * `ConfigMaps` and secrets management
    * Liveness and readiness probes for Go apps
    * Horizontal pod autoscaling
    * Helm charts for Go services
<!-- chapter: observability, duration: 2h -->
* Observability
    * Structured logging with slog
    * Metrics with `Prometheus` and Go client libraries
    * Distributed tracing with `OpenTelemetry`
    * Health check endpoints
    * Dashboarding and alerting basics
<!-- chapter: testing-microservices, duration: 2h -->
* Testing `Microservices`
    * Unit testing service layers
    * Integration testing with test containers
    * End-to-end testing of `gRPC` and `REST` endpoints
    * Mocking external dependencies
    * Contract testing
    * Load testing with `k6` or vegeta

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
