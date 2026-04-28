---
tags:
  - concepts:grpc
  - concepts:api
  - concepts:rest-api
  - concepts:distributed-systems
  - concepts:microservices
  - concepts:networking
level: intermediate
category: networking
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:architects
---
<!-- course: grpc_and_protobuf_deep_dive -->
# `gRPC` and `Protobuf` Deep Dive

## Description
`gRPC` is the default `RPC` framework for service-to-service communication in much of the modern cloud-native ecosystem,
and `Protobuf` is the schema language and serialization format underneath it. This five day course goes well past the
basics of "define a service, call a method" into the parts of `gRPC` that matter once a system goes to production:
streaming patterns, deadlines and cancellation, interceptors, error handling, schema evolution, performance tuning and
operational concerns.

The course is implementation-language-agnostic but uses `Go` and `Python` examples throughout. Participants leave
able to design `gRPC` APIs that survive long-term schema evolution, build resilient clients and servers, debug `gRPC`
in production, and decide where `gRPC` fits relative to `REST`, `GraphQL` and message-based alternatives.

## Duration
40 hours / 5 days

## Intended Audience
* developers building or consuming `gRPC` services in production
* architects designing service-to-service communication patterns
* platform engineers running `gRPC` infrastructure (proxies, gateways, meshes)
* engineers migrating from `REST` to `gRPC` or running both side by side

## Prerequisites
* working knowledge of at least one mainstream programming language (`Go`, `Python`, `Java`, `C++`, `C#`, `TypeScript`)
* basic networking knowledge: `TCP`, `HTTP`, `TLS`
* familiarity with at least one `RPC` or `REST API` style

## Objectives
* design `Protobuf` schemas that evolve cleanly over years
* implement and consume the four `gRPC` call patterns idiomatically
* apply deadlines, cancellation and retry policies correctly
* secure `gRPC` traffic end to end with `TLS`, `mTLS` and token-based auth
* implement and compose interceptors for cross-cutting concerns
* operate `gRPC` services through gateways, load balancers and `service mesh`
* tune `gRPC` performance and diagnose latency issues
* choose between `gRPC`, `gRPC-Web`, `Connect`, `REST` and `GraphQL`

## Outline
<!-- chapter: rpc-history-and-where-grpc-fits, duration: 1h -->
* `RPC` history and where `gRPC` fits
    * brief history: `Sun RPC`, `CORBA`, `Thrift`, `gRPC`
    * `gRPC` design goals
    * `gRPC` vs `REST`, `GraphQL`, `Thrift`, `JSON-RPC`
    * the `gRPC` ecosystem
<!-- chapter: protobuf-language-and-encoding, duration: 4h -->
* `Protobuf` language and encoding
    * proto2 vs proto3
    * scalar types, messages, enums, `oneof`, maps
    * the wire format and tag-length-value encoding
    * varints and zig-zag encoding
    * default values and field presence
    * unknown fields and forward compatibility
    * well-known types (`Timestamp`, `Duration`, `Any`, `Struct`)
<!-- chapter: schema-design-and-evolution, duration: 3h -->
* Schema design and evolution
    * field numbers as the durable contract
    * adding, deprecating and removing fields safely
    * `oneof` evolution
    * enum evolution and `UNKNOWN` defaults
    * service and method evolution
    * linting with `Buf` and `protoc-gen-validate`
    * style guides and naming conventions
<!-- chapter: code-generation-and-toolchain, duration: 2h -->
* Code generation and toolchain
    * `protoc` and the plugin model
    * the `Buf` build system
    * generating `Go`, `Python`, `Java`, `TypeScript` code
    * managing generated code in monorepos vs polyrepos
    * schema registries for `Protobuf`
<!-- chapter: the-four-call-patterns, duration: 3h -->
* The four call patterns
    * unary `RPC`
    * server streaming
    * client streaming
    * bidirectional streaming
    * choosing the right pattern for the use case
    * concurrency models on the server and client side
<!-- chapter: deadlines-cancellation-and-retries, duration: 2h -->
* Deadlines, cancellation and retries
    * deadlines vs timeouts
    * propagating deadlines across services
    * client cancellation and server-side cleanup
    * retry policies in `gRPC`
    * idempotency requirements for retries
    * hedging and the cost of duplicate requests
<!-- chapter: errors-and-status-codes, duration: 2h -->
* Errors and status codes
    * the canonical `gRPC` status codes
    * mapping errors to status codes correctly
    * rich error details with `google.rpc.Status`
    * client-side error handling patterns
    * `error` codes vs application-level errors
<!-- chapter: interceptors-and-middleware, duration: 3h -->
* Interceptors and middleware
    * unary and streaming interceptors
    * client-side and server-side interceptors
    * composing interceptors into chains
    * common interceptors: logging, metrics, tracing, auth
    * interceptors vs `service mesh` cross-cutting concerns
<!-- chapter: authentication-and-security, duration: 3h -->
* Authentication and security
    * channel credentials and call credentials
    * `TLS` and `mTLS` setup
    * `JWT` and `OAuth2` token validation
    * per-call authentication
    * `ALTS` and other transport-level options
    * authorization patterns
<!-- chapter: load-balancing-and-name-resolution, duration: 2h -->
* Load balancing and name resolution
    * proxy load balancing vs client-side load balancing
    * the resolver and balancer plugin model
    * `pick_first`, `round_robin` and custom balancers
    * `xDS`-based load balancing
    * connection management and subchannels
<!-- chapter: grpc-and-http-2, duration: 2h -->
* `gRPC` and `HTTP/2`
    * how `gRPC` rides on `HTTP/2`
    * streams, frames and flow control
    * `HPACK` header compression
    * head-of-line blocking and `HTTP/3`
    * keep-alive and idle connections
<!-- chapter: grpc-web-and-the-browser, duration: 2h -->
* `gRPC-Web` and the browser
    * why browsers cannot speak native `gRPC`
    * the `gRPC-Web` protocol
    * `Envoy` `gRPC-Web` filter
    * `Connect` as a modern alternative
    * client tooling for `TypeScript`
<!-- chapter: grpc-gateway-and-coexistence-with-rest, duration: 2h -->
* `gRPC-Gateway` and coexistence with `REST`
    * generating `REST` endpoints from `Protobuf`
    * `google.api.http` annotations
    * dual-publishing `REST` and `gRPC` from one schema
    * trade-offs of `REST` translation
    * `OpenAPI` generation from `Protobuf`
<!-- chapter: observability-for-grpc, duration: 2h -->
* Observability for `gRPC`
    * `gRPC` `OpenTelemetry` instrumentation
    * standard metrics and what they mean
    * tracing across `gRPC` boundaries
    * structured logging in interceptors
    * `gRPC`-specific dashboards and alerts
<!-- chapter: performance-tuning, duration: 3h -->
* Performance tuning
    * latency budgets and the `gRPC` overhead
    * message size limits and chunking
    * compression options and `when` to use them
    * connection pooling and keep-alive
    * server resource tuning
    * benchmarking with `ghz` and similar tools
    * common performance pitfalls
<!-- chapter: testing-grpc-services, duration: 2h -->
* Testing `gRPC` services
    * unit testing servers and clients
    * the in-process server pattern
    * mocking generated stubs
    * contract testing for `gRPC`
    * integration testing with `Testcontainers`
    * fuzzing `Protobuf` parsers
<!-- chapter: grpc-in-the-service-mesh, duration: 1h -->
* `gRPC` in the `service mesh`
    * `gRPC` traffic management with `Istio` or `Linkerd`
    * mutual `TLS` from the mesh
    * retries and circuit breaking at the mesh layer
    * observability at the mesh layer
    * `when` to push concerns into the mesh and `when` not to
<!-- chapter: case-studies-and-wrap-up, duration: 1h -->
* Case studies and wrap up
    * real-world `gRPC` rollouts and lessons learned
    * comparing `gRPC`, `Connect` and `REST` for several scenarios
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
