---
tags:
  - languages:java
  - concepts:api
  - concepts:rest
  - networking:web
level: intermediate
category: language
duration_hours: 16
audience:
  - audiences:developers
---
<!-- course: java_web_services -->
# `Java` `Web Services`

## Description
This course covers building and consuming `web services` in `Java` using both `REST` and
`SOAP` approaches. Participants will learn to create `RESTful APIs` with JAX-RS, work with
`SOAP` services using JAX-WS, handle `JSON` and `XML` data formats, and apply best
practices for authentication, error handling, and `API` design including `HATEOAS` and
`OpenAPI`/Swagger documentation.

## Duration
16 hours / 2 days

## Intended Audience
* `Java` developers who need to build or consume `web services`.
* Backend developers transitioning to service-oriented architectures.

## Prerequisites
* `Solid` experience in `Java` programming.
* Basic understanding of `HTTP` and web concepts.

## Objectives
* Participants will gain the ability to
    * Build RESTful `web services` using JAX-RS.
    * Create and consume `SOAP` services with JAX-WS.
    * Process `JSON` and `XML` data in `Java`.
    * Implement authentication and security for `web services`.
    * Design well-structured APIs with versioning and `HATEOAS`.
    * Document APIs using `OpenAPI`/Swagger.

## Outline
<!-- chapter: introduction-to-web-services, duration: 2h -->
* Introduction to `Web Services`
    * `REST` vs `SOAP` paradigms
    * `HTTP` methods and status codes
    * Content negotiation
    * Service-oriented architecture overview
<!-- chapter: restful-services-with-jax-rs, duration: 2h -->
* RESTful Services with JAX-RS
    * JAX-RS annotations and resource classes
    * Path parameters, query parameters, and headers
    * Request and response handling
    * Content types and media type negotiation
    * Jersey framework
    * CXF framework
<!-- chapter: soap-services-with-jax-ws, duration: 2h -->
* `SOAP` Services with JAX-WS
    * `SOAP` message structure
    * WSDL definitions
    * Creating `SOAP` endpoints
    * Generating clients from WSDL
    * `SOAP` faults and exception handling
<!-- chapter: json-and-xml-processing, duration: 2h -->
* `JSON` and `XML` Processing
    * `JSON` processing with `JSON`-P and `JSON`-B
    * Jackson for `JSON` serialization
    * JAXB for `XML` binding
    * Schema validation
<!-- chapter: authentication-and-security, duration: 2h -->
* Authentication and Security
    * Basic and digest authentication
    * Token-based authentication
    * `OAuth` 2.0 integration
    * Transport layer security (`TLS`)
    * Role-based access control
<!-- chapter: error-handling, duration: 2h -->
* Error Handling
    * Exception mappers
    * Standard error response formats
    * Validation and error reporting
    * Circuit breaker patterns
<!-- chapter: api-design-best-practices, duration: 2h -->
* `API` Design Best Practices
    * `API` versioning strategies
    * `HATEOAS` — Hypermedia as the Engine of Application State
    * Pagination and filtering
    * Rate limiting
<!-- chapter: api-documentation, duration: 2h -->
* `API` Documentation
    * `OpenAPI` specification
    * Swagger tooling
    * Generating documentation from code
    * Interactive `API` exploration

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
