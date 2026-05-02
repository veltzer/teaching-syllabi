---
tags:
  - networking:grpc
  - networking:protocols
  - concepts:api
  - concepts:microservices
level: intermediate
category: networking
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: grpc -->
# `gRPC` Development

## Description
`gRPC` is a high-performance, open-source remote procedure call framework built on `HTTP`/2 and `Protocol Buffers`. This course covers the full range of `gRPC` development, from defining services with `protobuf` to implementing all four communication patterns (unary, server streaming, client streaming, bidirectional streaming). Participants will learn about advanced topics including interceptors, authentication, load balancing, `gRPC`-Web, and `gRPC`-Gateway for `REST` transcoding.

## Duration
24 hours / 2 days

## Intended Audience
* Backend developers building `microservices` and distributed systems
* Software engineers designing inter-service communication
* Platform engineers evaluating RPC frameworks
* Full-stack developers working with `API` layers

## Prerequisites
* Proficiency in at least one programming language (Go, `Python`, `Java`, `C++`, or `C#`)
* Understanding of client-server architecture and networking fundamentals
* Familiarity with `REST APIs` and `HTTP` protocol
* Basic understanding of serialization formats (`JSON`, `XML`)
* Command-line experience

## Required Knowledge
* `Python` Programming (or equivalent experience)

## Objectives
* Understand `gRPC` fundamentals and the role of `HTTP`/2 and `Protocol Buffers`
* Define services and messages using `protobuf` syntax
* Implement unary, server streaming, client streaming, and bidirectional streaming RPCs
* Handle errors, deadlines, and cancellation in `gRPC` services
* Implement client and server interceptors for cross-cutting concerns
* Secure `gRPC` services with `TLS` and token-based authentication
* Configure load balancing and health checking
* Use `gRPC`-Web and `gRPC`-Gateway to expose services to web clients and `REST` consumers

## Outline
<!-- chapter: grpc-fundamentals, duration: 2h -->
* `gRPC` Fundamentals
    * What is `gRPC` and its design goals
    * `gRPC` architecture and communication model
    * The role of `HTTP`/2: multiplexing, binary framing, header compression
    * `Protocol Buffers` as the interface definition language and serialization format
    * `gRPC` vs `REST` vs `GraphQL` comparison
    * Supported languages and platforms
    * The `gRPC` ecosystem and tooling
<!-- chapter: protocol-buffers-syntax, duration: 2h -->
* `Protocol Buffers` Syntax
    * proto3 syntax overview
    * Defining messages: scalar types, nested messages
    * Enums and default values
    * oneof fields for union types
    * Maps for key-value pairs
    * Repeated fields for lists
    * Importing and packaging .proto files
    * Reserved fields and backward compatibility
    * Well-known types: Timestamp, Duration, Any, Struct
<!-- chapter: service-definition-and-code-generation, duration: 1h -->
* Service Definition and Code Generation
    * Defining RPC services in .proto files
    * The four RPC types: unary, server streaming, client streaming, bidirectional
    * Code generation with protoc compiler
    * Language-specific plugins: Go, `Python`, `Java`, `C++`
    * Generated code structure and usage patterns
    * Managing .proto files across teams and repositories
<!-- chapter: unary-rpcs, duration: 1h -->
* Unary RPCs
    * Implementing a unary RPC server
    * Creating a unary RPC client
    * Request and response message handling
    * Synchronous vs asynchronous client calls
    * Simple request-response patterns and use cases
<!-- chapter: server-streaming-rpcs, duration: 1h -->
* Server Streaming RPCs
    * Server streaming service definition
    * Implementing server-side streaming
    * Client-side handling of streaming responses
    * Use cases: real-time feeds, large data transfers, progress updates
    * Flow control and backpressure
<!-- chapter: client-streaming-rpcs, duration: 1h -->
* Client Streaming RPCs
    * Client streaming service definition
    * Implementing client-side streaming
    * Server-side handling of streaming requests
    * Use cases: file uploads, batch processing, telemetry
    * Completing and receiving the response
<!-- chapter: bidirectional-streaming-rpcs, duration: 1h -->
* Bidirectional Streaming RPCs
    * Bidirectional streaming service definition
    * Implementing full-duplex communication
    * Independent read and write streams
    * Use cases: chat, interactive sessions, real-time collaboration
    * Managing stream lifecycle
<!-- chapter: metadata-and-headers, duration: 1h -->
* Metadata and Headers
    * Sending and receiving metadata
    * Initial metadata vs trailing metadata
    * Common metadata patterns: request `IDs`, tracing, authentication tokens
    * Custom metadata for cross-cutting concerns
<!-- chapter: error-handling-and-status-codes, duration: 1h -->
* Error Handling and Status Codes
    * `gRPC` status codes: OK, CANCELLED, INVALID_ARGUMENT, NOT_FOUND, INTERNAL, etc.
    * Returning errors from server implementations
    * Rich error details and error model
    * Client-side error handling
    * Mapping `gRPC` status codes to `HTTP` status codes
<!-- chapter: deadlines-and-cancellation, duration: 2h -->
* Deadlines and Cancellation
    * Setting deadlines on RPC calls
    * Deadline propagation across services
    * Detecting and handling deadline exceeded
    * Client-side cancellation
    * Server-side cancellation detection
    * Best practices for timeout management
<!-- chapter: interceptors, duration: 2h -->
* Interceptors
    * Client-side interceptors (unary and streaming)
    * Server-side interceptors (unary and streaming)
    * Implementing logging, metrics, and tracing interceptors
    * Authentication and authorization interceptors
    * Chaining multiple interceptors
    * Error handling in interceptors
<!-- chapter: authentication-and-security, duration: 2h -->
* Authentication and Security
    * `TLS` configuration for `gRPC` servers and clients
    * Mutual `TLS` (mTLS) authentication
    * Token-based authentication with `JWT`
    * Per-RPC credentials
    * `OAuth2` integration
    * Channel credentials vs call credentials
<!-- chapter: load-balancing-and-service-discovery, duration: 2h -->
* Load Balancing and Service Discovery
    * Client-side load balancing strategies
    * Round-robin, pick-first, and custom policies
    * Proxy-based load balancing with Envoy
    * `DNS`-based service discovery
    * Integration with service meshes
    * Connection management and keepalive
<!-- chapter: health-checking-and-reflection, duration: 1h -->
* Health Checking and Reflection
    * The `gRPC` health checking protocol
    * Implementing health check services
    * Load balancer and `Kubernetes` health probe integration
    * `gRPC` server reflection for dynamic discovery
    * Tools: grpcurl, grpc_cli, Evans
<!-- chapter: grpc-web, duration: 1h -->
* `gRPC`-Web
    * `gRPC`-Web overview and browser limitations
    * `gRPC`-Web proxy with Envoy
    * Client-side `gRPC`-Web usage in `JavaScript` and `TypeScript`
    * Supported RPC types in `gRPC`-Web
    * Deployment architectures
<!-- chapter: grpc-gateway-and-rest-transcoding, duration: 1h -->
* `gRPC`-Gateway and `REST` Transcoding
    * `gRPC`-Gateway overview and use cases
    * Annotating .proto files with `HTTP` bindings
    * Generating `REST` endpoints from `gRPC` services
    * `OpenAPI` specification generation
    * Running `gRPC` and `REST` on the same service
<!-- chapter: testing-and-performance, duration: 2h -->
* Testing and Performance
    * Unit testing `gRPC` services
    * Integration testing with in-process servers
    * Mocking `gRPC` clients and servers
    * Performance benchmarking and profiling
    * Optimizing `protobuf` message size
    * Connection pooling and channel reuse
    * `gRPC` vs `REST` performance comparison

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
