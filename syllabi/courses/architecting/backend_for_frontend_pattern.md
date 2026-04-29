---
tags:
  - concepts:architecture
  - concepts:api
  - concepts:microservices
  - concepts:design-patterns
  - concepts:best-practices
level: intermediate
category: architecture
duration_hours: 16
audience:
  - audiences:architects
  - audiences:senior-developers
  - audiences:developers
  - audiences:team-leads
---
<!-- course: backend_for_frontend_pattern -->
# Backend for Frontend (`BFF`) Pattern

## Description
The catalog covers `API` design, `API` gateway patterns, and `microservices` architecture. None of those are
the same conversation as the `BFF` pattern. The `BFF` pattern sits between a single client (a mobile app,
a web `SPA`, a desktop client) and the `rest` of the system. It exists because a generic `API` is rarely the
right `API` for a specific client, and because the alternative — push the orchestration into the client —
is consistently a bad idea.

This two day course covers the `BFF` pattern in depth. It covers the motivation, the right and wrong
shapes, the anti-patterns (the most common being a `BFF` that grows into a generic gateway), the
relationship to `GraphQL` and `tRPC`, the testing model, the deployment model, the team-ownership
question (is the `BFF` owned by the client team or the platform team?), and the operational reality of
running per-client `BFF` services. Examples are drawn from public engineering writing by `SoundCloud`,
`Spotify`, `Netflix`, and the `BFF` pattern as documented by `Sam Newman`. Participants leave able to
decide `when` to introduce a `BFF`, who should own it, and how to keep it from collapsing into a `monolith`.

## Duration
16 hours / 2 days

## Intended Audience
* architects designing client-server systems with multiple distinct clients
* senior developers building or maintaining a `BFF`
* tech leads navigating the team-ownership question
* developers asked to "just add it to the gateway"

## Prerequisites
* working knowledge of `REST` or `GraphQL`
* exposure to `microservices` architecture concepts
* familiarity with at least one frontend platform (web, mobile)

## Objectives
* explain `when` a `BFF` is the right pattern and `when` it is not
* design a `BFF` that does not become a generic gateway
* assign ownership of a `BFF` to the right team
* test and deploy a `BFF` independently of the clients
* avoid the common anti-patterns
* compare the `BFF` pattern to `GraphQL` federation

## Outline
<!-- chapter: what-the-bff-pattern-is, duration: 1h -->
* What the `BFF` pattern is
    * the canonical Sam `Newman` article
    * "one backend per experience"
    * the difference from a `general API` gateway
    * cross-reference to the `API` Gateway Patterns course
    * what it solves and what it does not
<!-- chapter: the-motivation, duration: 1h -->
* The motivation
    * different clients have different needs
    * the chatty-mobile-client problem
    * the over-fetching problem
    * the under-fetching problem
    * the "client does the join" anti-pattern
<!-- chapter: where-the-bff-sits, duration: 1h -->
* Where the `BFF` sits
    * client → `BFF` → backend services
    * the `BFF` is not the only path
    * the `BFF` is not the security boundary
    * authentication and the `BFF`
    * cross-reference to the `OAuth2` and `OIDC` course
<!-- chapter: shapes-of-bff, duration: 2h -->
* Shapes of `BFF`
    * one `BFF` per client platform
    * one `BFF` per experience
    * one `BFF` per team
    * the wrong shape: a single `BFF` for all clients
    * worked examples
<!-- chapter: bff-and-graphql, duration: 2h -->
* `BFF` and `GraphQL`
    * `GraphQL` as a `BFF` style
    * `GraphQL` federation as an alternative
    * `tRPC` as a `BFF` style
    * the "is `GraphQL` a `BFF` killer" question
    * cross-reference to the `GraphQL` course
<!-- chapter: ownership-and-teams, duration: 2h -->
* Ownership and teams
    * client team owns the `BFF`
    * platform team owns the `BFF`
    * the case for each
    * the "two teams own one `BFF`" failure
    * Conway's law applied
<!-- chapter: testing-a-bff, duration: 1h -->
* Testing a `BFF`
    * contract tests with the backend services
    * contract tests with the client
    * cross-reference to the Contract Testing course
    * the "we mocked everything and tested nothing" failure
    * end-to-end tests through the `BFF`
<!-- chapter: deployment-and-operations, duration: 1h -->
* Deployment and operations
    * deployment cadence with the client
    * version skew between client and `BFF`
    * blue-green of a `BFF`
    * observability of a `BFF`
    * the on-call story
<!-- chapter: anti-patterns, duration: 2h -->
* Anti-patterns
    * the `BFF` that became a generic gateway
    * the `BFF` that contains business logic
    * the `BFF` per microservice
    * the shared `BFF` for unrelated clients
    * the `BFF` that talks to the database directly
    * the "client team does not own the `BFF`" deadlock
<!-- chapter: when-not-to-use-a-bff, duration: 1h -->
* `When` not to use a `BFF`
    * the single-client system
    * the system where backend `APIs` already match client needs
    * the team that cannot operate one more service
    * the "we added a `BFF` because the article said so" failure
<!-- chapter: a-real-bff-walkthrough, duration: 2h -->
* A real `BFF` walkthrough
    * design walkthrough of a mobile `BFF`
    * design walkthrough of a web `BFF`
    * the migration from no-`BFF` to `BFF`
    * the migration from one-big-`BFF` to per-experience-`BFF`
    * recommended reading: `Newman`'s `BFF` writing, the `SoundCloud` and `Netflix` posts

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
