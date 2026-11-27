---
audience:
  - audiences:architects
  - audiences:developers
  - audiences:managers
  - audiences:team-leads
category: architecture
duration_minutes: 120
level: intermediate
tags:
  - architecture:api-design
  - architecture:distributed-systems
  - architecture:microservices
  - data-and-ai:agents
  - data-and-ai:ai
  - practices:contract-testing
  - practices:observability
---

<!-- blurb: microservices_in_the_age_of_ai -->
# `Microservices` in the Age of `AI`

**Technical leadership expert talk.** How `AI` coding agents change the case for
microservices - what they make easier, what they make harder, and how to design services
that both people and agents can work with.

## The Challenge

`Microservices` were adopted to let many teams build and deploy independently, at the price of
distributed-systems complexity. `AI` coding agents shift that trade-off in both directions.
A small, well-bounded service fits neatly into an agent's context, while a change that cuts
across ten services is exactly where agents lose track. Architectures designed only for human
teams leave much of the value of `AI` on the table - and some of the old reasons for splitting
a system no longer apply.

## What This Session Covers

A practical, technical look at microservice architecture when much of the code is written,
tested, and operated with the help of `AI` agents: service boundaries as context boundaries,
contracts as the agent's interface, cross-service changes, testing and operations, and a fresh
look at the monolith-versus-microservices decision.

## Agenda

* **`Microservices` Revisited** (10 min): Why we split systems into services in the first place, and which of those reasons `AI` strengthens or weakens.
* **Services as Context Boundaries** (20 min): Why small, well-bounded services with clear ownership are the ideal unit of work for an `AI` agent, and how to size them.
* **Contracts as the Agent's Interface** (15 min): `OpenAPI`, `gRPC`, and `JSON Schema` specifications as the source of truth agents can rely on instead of reading other services' code.
* **Changes That Cross Service Boundaries** (20 min): Coordinating multi-service changes with agents; versioning, backward compatibility, and rollout order.
* **Testing Distributed Systems with `AI`** (15 min): Contract tests, generated test suites, and reproducible local environments that let agents verify their own changes.
* **Operating and Debugging with `AI`** (15 min): Logs, traces, and `OpenTelemetry` as context for agents investigating incidents across services.
* **Monolith or `Microservices`, Now?** (15 min): When a modular monolith serves agents better, when services still win, and how to decide for your own system.
* **Key Takeaways and Q&A** (10 min): Actionable next steps for architects and engineering teams.

## Takeaways

* A clear understanding of how `AI` agents change the trade-offs of microservice architecture
* Design principles for services, contracts, and boundaries that work well with `AI` agents
* A practical framework for revisiting the architecture of your own system

## Who Should Attend

* Software architects
* Engineering managers
* Tech leads
* Developers building or maintaining microservice systems

## Continue the Journey

This talk examines the architecture. A follow-on, hands-on workshop can review the team's own
services, contracts, and workflows and adapt them for effective work with `AI` agents.

## Speaker

Mark Veltzer
