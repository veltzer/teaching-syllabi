---
tags:
  - concepts:api
  - concepts:rest
  - concepts:rest-api
  - concepts:architecture
  - concepts:best-practices
  - concepts:migration
level: intermediate
category: architecture
duration_hours: 40
audience:
  - audiences:developers
  - audiences:architects
  - audiences:team-leads
---
<!-- course: api_evolution_and_versioning -->
# `API` Evolution and Versioning

## Description
Public and internal APIs are contracts. Once a client depends on an `API`, every change becomes a coordination problem
between teams, organizations and sometimes thousands of unknown consumers. This five day course is dedicated entirely
to the discipline of evolving APIs over time without breaking the people who depend on them.

The course covers the theoretical underpinnings of compatibility (what counts as breaking, what does not, and why these
definitions are different for `REST`, `gRPC`, `GraphQL` and message-based APIs), the toolchain used to detect, prevent
and communicate breakage, and the organizational practices that turn `API` evolution from a recurring crisis into a
predictable engineering process. Participants leave with a toolkit they can apply to greenfield APIs, to mature public
APIs with many consumers, and to the painful job of stabilizing a sprawling, inconsistent internal `API` landscape.

## Duration
40 hours / 5 days

## Intended Audience
* developers building or maintaining APIs that other teams or customers depend on
* architects responsible for `API` strategy across an organization
* platform and developer-experience teams running internal `API` programs
* team leads coordinating client and server release cadences

## Prerequisites
* `solid` working knowledge of `HTTP` and at least one `API` style (`REST`, `gRPC` or `GraphQL`)
* basic understanding of `JSON` and `JSON Schema` or `Protobuf`
* experience consuming or producing at least one `API` in production

## Objectives
* precisely define what is and is not a breaking change for each major `API` style
* design `API` contracts that are easy to evolve from day one
* apply versioning strategies (`URL`, header, media type, schema-based) and judge their trade-offs
* operate dual-stack and migration `windows` for live traffic
* detect breakage automatically using contract diffing and consumer-driven contracts
* deprecate and retire `API` surfaces without breaking unknown consumers
* communicate change to internal and external consumers effectively
* govern an `API` portfolio with style guides, review boards and tooling

## Outline
<!-- chapter: why-api-evolution-is-hard, duration: 2h -->
* Why `API` evolution is hard
    * APIs as durable contracts
    * the cost of a single breaking change at scale
    * Hyrum's law and accidental contracts
    * why "just version it" is not a strategy
    * the difference between technical compatibility and behavioral compatibility
<!-- chapter: defining-breaking-and-non-breaking-change, duration: 3h -->
* Defining breaking and non-breaking change
    * additive vs subtractive changes
    * structural vs semantic breakage
    * compatibility from the producer side and from the consumer side
    * formal definitions for `JSON`, Protobuf and `GraphQL` schemas
    * the "robustness principle" and its limits
<!-- chapter: rest-api-compatibility-rules, duration: 3h -->
* `REST` `API` compatibility rules
    * adding fields to responses safely
    * adding fields to requests safely
    * status code changes and their consequences
    * header changes and content negotiation
    * pagination and `URL` shape changes
    * error response evolution
<!-- chapter: grpc-and-protobuf-evolution, duration: 3h -->
* `gRPC` and `Protobuf` evolution
    * field numbers as the real contract
    * adding, deprecating and removing fields
    * `oneof` evolution
    * enum evolution and `UNKNOWN` defaults
    * service and method evolution
    * `Buf` and `protobuf` linting tools
<!-- chapter: graphql-evolution, duration: 2h -->
* `GraphQL` evolution
    * the schema as a single shared `API` surface
    * additive evolution by default
    * field deprecation with the `@deprecated` directive
    * removing fields safely with usage analytics
    * input type evolution
    * federation and breaking changes across subgraphs
<!-- chapter: event-and-message-schema-evolution, duration: 2h -->
* Event and message schema evolution
    * event-carried state transfer and the schema problem
    * `Avro`, Protobuf and `JSON Schema` for events
    * forward, backward and full compatibility
    * schema registries and compatibility modes
    * versioning topics vs versioning messages
<!-- chapter: versioning-strategies, duration: 3h -->
* Versioning strategies
    * `URL` path versioning
    * media type and content negotiation versioning
    * header-based versioning
    * `GraphQL` and the no-version philosophy
    * additive evolution as the default strategy
    * date-based and calendar versioning for `SaaS` APIs
    * choosing the right strategy for your context
<!-- chapter: contract-first-development, duration: 2h -->
* Contract-first development
    * specification as source of truth
    * `OpenAPI`, AsyncAPI, Protobuf and `GraphQL SDL`
    * generating server stubs and client SDKs from specs
    * keeping documentation, code and contract in sync
    * pull-request workflows for spec changes
<!-- chapter: contract-diffing-and-breaking-change-detection, duration: 3h -->
* Contract diffing and breaking change detection
    * automated contract diff tools
    * `oasdiff`, `buf breaking`, `graphql-inspector`
    * integrating diff checks into CI
    * classifying changes by severity
    * approval workflows for intentional breaking changes
<!-- chapter: consumer-driven-contracts, duration: 2h -->
* Consumer-driven contracts
    * `Pact` and the consumer-driven model
    * recording client expectations as tests
    * the broker as a coordination point
    * pre-deploy verification gates
    * limits of consumer-driven contracts
<!-- chapter: dual-stack-and-migration-windows, duration: 3h -->
* Dual-stack and migration `windows`
    * running v1 and v2 side by side
    * traffic mirroring for verification
    * shadow reads and shadow writes
    * gradual cutover with feature flags
    * sunset headers and deprecation timelines
    * planning a migration that takes months without losing nerve
<!-- chapter: deprecation-and-retirement, duration: 2h -->
* Deprecation and retirement
    * why deprecation is the hardest part
    * the `Deprecation` and Sunset `HTTP` headers (RFC 8594, RFC 9745)
    * tracking remaining consumers
    * usage telemetry as a precondition for removal
    * forced retirement and brownouts
    * post-retirement support `windows` for paying customers
<!-- chapter: api-style-guides-and-design-reviews, duration: 2h -->
* `API` style guides and design reviews
    * the role of an `API` style guide
    * style guides at scale: Microsoft, Google, `Zalando`
    * automated style guide enforcement with Spectral
    * design review boards
    * lightweight review for internal APIs
<!-- chapter: communicating-change-to-consumers, duration: 2h -->
* Communicating change to consumers
    * changelogs that humans actually read
    * release notes vs upgrade guides
    * email, banner and in-product deprecation notifications
    * developer relations and `API` change
    * status pages, RSS feeds and webhooks for `API` change events
<!-- chapter: governance-and-portfolio-management, duration: 2h -->
* Governance and portfolio management
    * inventorying your `API` portfolio
    * categorizing APIs by audience and stability
    * stability tiers: experimental, beta, stable, deprecated
    * `API` review boards
    * `SLO` per `API` tier
<!-- chapter: case-studies-and-anti-patterns, duration: 2h -->
* Case studies and anti-patterns
    * Stripe's versioned `API` model
    * `GitHub`'s media-type versioning history
    * `Google` cloud `API` stability promises
    * Twitter's deprecations
    * the "`v2`-forever" anti-pattern
    * accidental breakage stories and how they were detected
<!-- chapter: workshop-and-wrap-up, duration: 2h -->
* Workshop and wrap up
    * end-to-end design walkthrough on a sample multi-team `API`
    * discussion of attendee real-world `API` problems
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
