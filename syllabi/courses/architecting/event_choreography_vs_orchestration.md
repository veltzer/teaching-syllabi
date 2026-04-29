---
tags:
  - concepts:architecture
  - concepts:distributed-systems
  - concepts:design-patterns
  - concepts:best-practices
level: advanced
category: architecture
duration_hours: 16
audience:
  - audiences:architects
  - audiences:senior-developers
  - audiences:developers
  - audiences:team-leads
---
<!-- course: event_choreography_vs_orchestration -->
# Event Choreography vs Orchestration

## Description
The catalog has `Event-Driven Architecture`, `Event-Driven Architecture with Kafka`, `Saga Pattern`,
`Event Sourcing in Practice`, and `Event Storming and Domain Modeling`. None of those addresses the
specific architectural decision that any team building a multi-service workflow has to `make`: do the
services `react` to events from each other (`choreography`), or does a separate orchestrator tell them
what to do (`orchestration`). The choice is consequential. Choreography is loosely coupled but harder
to reason about, change, and recover from. Orchestration is easy to reason about but introduces a
component that can become a bottleneck or a single point of failure.

This two day course is the focused decision-support course for that choice. It covers the canonical
shapes of each, the reasoning model (how do you understand the system in each), the failure model
(what happens `when` a step fails), the change model (what happens `when` the workflow needs to change),
the observability model (how do you debug a failed flow), the technologies that support each
(`Temporal`, `Camunda`, `Cadence`, `Conductor`, `Step Functions` for orchestration; `Kafka`, `EventBridge`,
`NATS` for choreography), and the patterns where mixing the two is the right answer. Examples include
the canonical e-commerce checkout flow, the airline-reservation flow, the loan-application flow, and
the `data` pipeline flow. Participants leave able to `make` the decision for their next workflow.

## Duration
16 hours / 2 days

## Intended Audience
* architects designing service-to-service workflows
* senior developers building distributed transactions
* developers writing the next workflow in a `microservices` system
* team leads picking the workflow technology

## Prerequisites
* exposure to the `Event-Driven Architecture` course
* exposure to the `Saga Pattern` course
* working experience with at least one message system
* familiarity with `microservices` concepts

## Objectives
* recognize choreography vs orchestration in existing systems
* design a workflow in either style and explain why
* pick the right technology for the chosen style
* design the failure-and-compensation story
* observe and debug each style
* recognize `when` to mix the two
* avoid the anti-patterns of each

## Outline
<!-- chapter: the-distinction, duration: 1h -->
* The distinction
    * choreography: services `react` to events
    * orchestration: a coordinator tells services what to do
    * cross-reference to the `Event-Driven Architecture` course
    * cross-reference to the `Saga Pattern` course
    * the canonical examples
<!-- chapter: choreography-in-depth, duration: 2h -->
* Choreography in depth
    * the publish-subscribe shape
    * the choreographed `saga`
    * each service knows its own role and its own next step
    * the "no central authority" property
    * the example: order placed → payment authorized → shipment scheduled
<!-- chapter: orchestration-in-depth, duration: 2h -->
* Orchestration in depth
    * the workflow as a first-class object
    * the orchestrator as the coordinator
    * the workflow definition as code or as a graph
    * `Temporal`, `Cadence`, `Camunda`, `Conductor`, `Step Functions`
    * the example: same order flow, in `Temporal`
<!-- chapter: reasoning-about-each-style, duration: 2h -->
* Reasoning about each style
    * choreography: read every service's event handlers
    * orchestration: read the workflow definition
    * the "we cannot understand what the system does" failure of choreography
    * the "the orchestrator is the system" risk
    * which one a new engineer can understand faster
<!-- chapter: failure-handling, duration: 2h -->
* Failure handling
    * the `saga`'s compensating action
    * the orchestration retry-and-compensate primitive
    * the "we forgot to compensate the third step" choreography failure
    * the durable-execution argument
    * cross-reference to the Idempotency course
<!-- chapter: change-management, duration: 1h -->
* Change management
    * adding a step to a choreographed flow
    * adding a step to an orchestrated flow
    * the "we changed the event and broke five services" reality
    * versioning the workflow
    * which is easier to change in practice
<!-- chapter: observability-and-debugging, duration: 2h -->
* Observability and debugging
    * tracing a choreographed flow
    * the orchestrator as the timeline
    * cross-reference to the Distributed Tracing in Practice course
    * the "we have no idea where the flow stuck" failure
    * the visualization argument for orchestration
<!-- chapter: technologies-for-each, duration: 2h -->
* Technologies for each
    * orchestration: `Temporal`, `Cadence`, `Camunda`, `Conductor`, `Step Functions`, `Argo Workflows`
    * choreography: `Kafka`, `EventBridge`, `NATS`, `RabbitMQ`
    * the cost-and-operations shape of each
    * cross-reference to the `Temporal` course
    * picking
<!-- chapter: when-to-mix, duration: 1h -->
* `When` to mix
    * the orchestrated `saga` over a choreographed substrate
    * the choreographed broadcast outside an orchestrated flow
    * the "we used both, deliberately" pattern
    * the "we used both, accidentally" failure
    * worked example
<!-- chapter: making-the-decision, duration: 1h -->
* Making the decision
    * the questions to ask
    * the team's understanding of the workflow
    * the change frequency
    * the failure-recovery cost
    * the "we picked one because the conference talk said to" anti-pattern

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
