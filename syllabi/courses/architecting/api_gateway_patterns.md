---
tags:
  - concepts:api
  - concepts:architecture
  - concepts:microservices
  - networking:web
level: intermediate
category: architecture
duration_hours: 16
audience:
  - audiences:architects
  - audiences:developers
  - audiences:devops
---
<!-- course: api_gateway_patterns -->
# `API Gateway` Patterns

## Description
This course covers the design and implementation of `API gateway` patterns in modern distributed
architectures. Participants will explore different gateway architectures, work with popular gateway
solutions such as Kong and `AWS API Gateway`, and learn how to implement cross-cutting concerns
including rate limiting, throttling, authentication, authorization, request transformation, caching,
and monitoring. The course provides practical guidance for selecting and configuring `API` gateways
in `microservices` environments.

## Duration
16 hours / 1 day

## Intended Audience
* software architects designing `API` strategies
* backend developers building `microservices`
* `DevOps` engineers managing `API` infrastructure

## Prerequisites
* experience with `REST` APIs and `HTTP` protocols
* familiarity with `microservices` architecture
* basic understanding of authentication and authorization concepts

## Objectives
* understand the role and responsibilities of an `API gateway`
* compare and evaluate different gateway architectures and products
* implement rate limiting, throttling, and traffic management policies
* configure authentication and authorization at the gateway level
* apply request transformation and response aggregation patterns
* set up caching strategies and monitoring for `API` gateways

## Outline
<!-- chapter: introduction-to-api-gateways, duration: 1h -->
* introduction to `API` gateways
    * the role of an `API gateway` in `microservices`
    * `API gateway` vs reverse proxy vs load balancer
    * edge gateway vs internal gateway patterns
    * backends for frontends (BFF) pattern
<!-- chapter: gateway-architectures, duration: 1h -->
* gateway architectures
    * centralized vs distributed gateway models
    * sidecar proxy and service mesh integration
    * gateway as a single point of entry
    * multi-gateway and federated gateway patterns
<!-- chapter: kong-api-gateway, duration: 1h -->
* Kong `API gateway`
    * Kong architecture and deployment models
    * plugin ecosystem overview
    * declarative configuration with decK
    * custom plugin development
<!-- chapter: aws-api-gateway, duration: 1h -->
* `AWS API Gateway`
    * `REST` APIs vs `HTTP` APIs vs `WebSocket` APIs
    * integration with `AWS Lambda` and backend services
    * stages, deployments, and canary releases
    * usage plans and `API` keys
<!-- chapter: rate-limiting-and-throttling, duration: 2h -->
* rate limiting and throttling
    * rate limiting algorithms (token bucket, sliding window)
    * per-client and per-endpoint throttling
    * burst handling and graceful degradation
    * distributed rate limiting across gateway instances
<!-- chapter: api-versioning, duration: 2h -->
* `API` versioning
    * versioning strategies (URL path, header, query parameter)
    * backward compatibility and deprecation policies
    * version routing at the gateway level
    * managing multiple `API` versions simultaneously
<!-- chapter: authentication-and-authorization, duration: 2h -->
* authentication and authorization
    * `OAuth 2.0` and `OpenID Connect` integration
    * `JWT` validation at the gateway
    * `API` key management
    * mutual `TLS` and certificate-based authentication
    * fine-grained authorization policies
<!-- chapter: request-transformation, duration: 2h -->
* request transformation
    * request and response mapping
    * header manipulation and enrichment
    * payload transformation and protocol translation
    * request aggregation and response composition
<!-- chapter: caching, duration: 2h -->
* caching
    * gateway-level caching strategies
    * cache invalidation approaches
    * conditional requests and ETags
    * caching considerations for personalized content
<!-- chapter: monitoring-and-observability, duration: 2h -->
* monitoring and observability
    * access logging and audit trails
    * metrics collection and dashboards
    * distributed tracing through the gateway
    * alerting on error rates and latency

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
