---
tags:
  - concepts:architecture
  - concepts:distributed-systems
  - concepts:microservices
  - concepts:api
  - concepts:rest
  - concepts:service-mesh
  - concepts:data-integration
level: intermediate
category: architecture
duration_hours: 40
audience:
  - audiences:developers
  - audiences:architects
  - audiences:team-leads
---
<!-- course: service_oriented_architecture -->
# `Service-Oriented Architecture`

## Description
This course is a comprehensive five day introduction to `Service-Oriented Architecture` (`SOA`).
`SOA` is an architectural style in which business capabilities are exposed as reusable, contract-based services that
are composed to form larger systems. Although `microservices` have largely succeeded `SOA` as the dominant style for
new green-field systems, `SOA` remains the backbone of countless enterprise systems and many of its principles, patterns
and pitfalls are directly applicable to today's distributed architectures.

The course covers the principles of service orientation, service modeling and contract design, the classical `SOA` technology
stack (`SOAP`, `WSDL`, `WS-*`, `ESB`, `BPEL`), the more modern `RESTful` and event-driven approaches, governance and security,
and the relationship between `SOA` and `microservices`. Participants will leave able to design, govern and evolve
service-oriented systems, integrate them with legacy assets, and `make` informed decisions about `when` `SOA`, `microservices`
or a hybrid is the appropriate choice.

## Duration
40 hours / 5 days

## Intended Audience
* software architects designing or evolving service-oriented systems
* developers building or consuming enterprise services
* integration engineers responsible for connecting heterogeneous systems
* team leads and technical managers overseeing `SOA` initiatives
* engineers planning a migration from `SOA` to `microservices` or a hybrid landscape

## Prerequisites
* several years of software development experience
* familiarity with at least one general purpose programming language
* basic understanding of `HTTP`, `XML` and `JSON`
* basic understanding of distributed systems concepts is an advantage

## Objectives
* understand the principles, motivations and history of `Service-Oriented Architecture`
* model business capabilities as well-bounded, reusable services
* design service contracts using both `SOAP`/`WSDL` and `RESTful` styles
* apply the classical `SOA` integration patterns and understand the role of an `ESB`
* orchestrate and choreograph services to implement business processes
* secure services using `WS-Security`, `OAuth2`, `OIDC` and transport-level mechanisms
* govern a service portfolio with a service registry, repository and lifecycle process
* compare `SOA` to `microservices` and plan a transition between the two
* identify and avoid the most common `SOA` anti-patterns and failure modes

## Outline
<!-- chapter: introduction-to-soa, duration: 3h -->
* Introduction to `SOA`
    * what is a service
    * the business case for service orientation
    * brief history: from `RPC` and `CORBA` to `SOA` and beyond
    * `SOA` vs `monolith` vs `microservices`
    * `when` `SOA` is the right choice and `when` it is not
    * common myths and misconceptions about `SOA`
<!-- chapter: principles-of-service-orientation, duration: 3h -->
* Principles of service orientation
    * service contract
    * loose coupling
    * service abstraction
    * service reusability
    * service autonomy
    * service statelessness
    * service discoverability
    * service composability
    * how the principles interact and trade off against each other
<!-- chapter: service-modeling-and-identification, duration: 3h -->
* Service modeling and identification
    * `top`-down, bottom-up and meet-in-the-middle approaches
    * decomposition by business capability
    * decomposition by subdomain and bounded context
    * service taxonomy: entity, task, utility and process services
    * granularity and the cost of getting it wrong
    * identifying candidate services from existing systems
<!-- chapter: service-contract-design, duration: 3h -->
* Service contract design
    * contract-first design and the alternative code-first approach
    * data contracts and canonical data models
    * versioning strategies and backward compatibility
    * idempotency and safety of operations
    * documenting and publishing contracts
    * contract-driven development workflows
<!-- chapter: soap-wsdl-and-the-ws-stack, duration: 4h -->
* `SOAP`, `WSDL` and the `WS-*` stack
    * the `SOAP` envelope, headers and body
    * `WSDL` structure: types, messages, port types, bindings, services
    * `XML Schema` for service contracts
    * `UDDI` and historical service registries
    * the `WS-*` family: `WS-Addressing`, `WS-ReliableMessaging`, `WS-Policy`, `WS-AtomicTransaction`
    * tooling and code generation from `WSDL`
    * strengths and weaknesses of the classical stack
<!-- chapter: restful-services-and-modern-soa, duration: 2h -->
* `RESTful` services and modern `SOA`
    * resources, representations and uniform interface
    * `HTTP` verbs and status codes as contract elements
    * `HATEOAS` and richness of `REST`
    * `OpenAPI` and contract specification
    * `gRPC` as a modern alternative
    * `GraphQL` for service composition
    * comparing `SOAP` and `REST` for `SOA` workloads
<!-- chapter: enterprise-integration-patterns, duration: 3h -->
* Enterprise integration patterns
    * messaging vs `RPC` style integration
    * channels, endpoints, routers, translators and transformers
    * content-based routing and message filtering
    * message enrichment and claim `check`
    * scatter-gather and aggregation
    * dead letter channels and guaranteed delivery
    * idempotent receivers and deduplication
<!-- chapter: the-enterprise-service-bus, duration: 3h -->
* The `Enterprise Service Bus`
    * what an `ESB` is and what it is not
    * mediation, transformation and routing in the `ESB`
    * adapters and protocol bridging
    * canonical message formats
    * `ESB` topologies: hub-and-spoke, federated, distributed
    * representative products: `Mule`, `WSO2`, `IBM Integration Bus`, `Apache Camel`
    * the "smart pipes, dumb endpoints" critique and lessons learned
<!-- chapter: orchestration-and-choreography, duration: 3h -->
* Orchestration and choreography
    * defining business processes across services
    * `BPEL` and process engines
    * `BPMN` for process modeling
    * orchestration vs choreography trade-offs
    * the `saga` pattern for long running transactions
    * compensation and recovery
    * modern orchestrators and workflow engines
<!-- chapter: messaging-events-and-asynchronous-soa, duration: 3h -->
* Messaging, events and asynchronous `SOA`
    * `JMS` and message brokers
    * publish/subscribe vs point-to-point
    * event-driven `SOA` and event notification
    * event-carried state transfer
    * the role of `Kafka` and modern streaming platforms
    * delivery guarantees: at-most-once, at-least-once, exactly-once
    * back pressure and flow control
<!-- chapter: security-for-services, duration: 3h -->
* Security for services
    * threat model for service-oriented systems
    * transport-level security with `TLS` and `mTLS`
    * `WS-Security`, `SAML` tokens and message-level security
    * `OAuth2` and `OIDC` for `RESTful` services
    * `API` keys, `JWT` and token validation
    * authorization patterns: `RBAC`, `ABAC`, policy engines
    * auditing and non-repudiation
<!-- chapter: governance-registry-and-lifecycle, duration: 2h -->
* Governance, registry and lifecycle
    * design-time vs run-time governance
    * service registry and service repository
    * service lifecycle: propose, design, build, deploy, deprecate, retire
    * service-level agreements and contracts
    * change management and impact analysis
    * organizational structures that support `SOA`
<!-- chapter: quality-of-service-and-observability, duration: 2h -->
* Quality of service and observability
    * defining `SLI`, `SLO` and `SLA` for services
    * monitoring services and the bus
    * distributed tracing across service boundaries
    * centralized logging and correlation `IDs`
    * health checks, heartbeats and liveness probes
    * capacity planning and performance budgets
<!-- chapter: from-soa-to-microservices, duration: 2h -->
* From `SOA` to `microservices`
    * what `microservices` kept and what they discarded
    * smart endpoints and dumb pipes
    * decentralized data and decentralized governance
    * `service mesh` as a successor to the `ESB`
    * hybrid landscapes during migration
    * planning a stepwise migration without big-bang rewrites
<!-- chapter: anti-patterns-case-studies-and-wrap-up, duration: 1h -->
* Anti-patterns, case studies and wrap up
    * the distributed `monolith`
    * the `ESB` as application server
    * the canonical model that ate the enterprise
    * shared database between services
    * chatty services and the latency tax
    * lessons from real `SOA` programs that succeeded and failed
    * end-to-end design walkthrough on a sample enterprise scenario
    * recommended reading and further study

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
