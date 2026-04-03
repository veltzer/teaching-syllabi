---
tags:
  - tools:temporal
  - practices:workflow-orchestration
  - concepts:distributed-systems
  - practices:microservices
level: intermediate
category: data-engineering
duration_hours: 24
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: temporal -->
# `Temporal` Workflow Orchestration

## Description
`Temporal` is an open-source, durable workflow orchestration platform that enables developers to write long-running, fault-tolerant business processes as ordinary code.
Unlike traditional job schedulers or message queues, `Temporal` automatically persists workflow state, retries failed activities, and resumes execution after crashes — all without any application-level bookkeeping.
Its programming model lets engineers express complex workflows — including timers, signals, child workflows, and compensating transactions — using familiar control flow in `Go`, `Java`, `Python`, `TypeScript`, or `PHP`.
This course takes developers from `Temporal` fundamentals through advanced workflow patterns, testing strategies, and production deployment.

## Duration
24 hours / 3 days

## Intended Audience
* Backend developers building long-running or multi-step business processes
* Architects designing reliable distributed systems and microservice orchestration
* Engineers replacing fragile cron jobs, queues, or ad-hoc retry logic with durable workflows

## Prerequisites
* `Solid` experience in at least one of `Go`, `Java`, `Python`, or `TypeScript`
* Familiarity with distributed systems and `microservices` concepts
* Basic understanding of message queues and `async` processing

## Objectives
* Understand `Temporal`'s durable execution model and how it differs from queues and schedulers
* Write workflows and activities using the `Temporal` `SDK`
* Model complex long-running processes with signals, queries, and timers
* Implement child workflows and the `saga` pattern for distributed transactions
* Test `Temporal` workflows with the test server and replay testing
* Deploy and operate a `Temporal` cluster
* Monitor workflows using `Temporal` UI and metrics

## Outline
<!-- chapter: introduction-to-workflow-orchestration, duration: 2h -->
* Introduction to Workflow Orchestration
    * The problem with ad-hoc distributed coordination
    * Queues, sagas, and state machines — limitations
    * Durable execution — the `Temporal` mental model
    * `Temporal` vs `Apache Airflow` vs `AWS Step Functions`
    * Key concepts — workflows, activities, workers, task queues

<!-- chapter: temporal-architecture, duration: 2h -->
* `Temporal` Architecture
    * `Temporal` Server components — frontend, history, matching, worker
    * Persistence backends — `Cassandra`, `PostgreSQL`, `MySQL`
    * Namespace isolation
    * Event history and the execution journal
    * How `Temporal` guarantees durability

<!-- chapter: workflows-and-activities, duration: 3h -->
* Workflows and Activities
    * Writing your first workflow
    * Defining and implementing activities
    * Activity options — retry policies, timeouts, heartbeating
    * Determinism constraints in workflow code
    * Workflow input and output serialisation

<!-- chapter: workflow-execution-and-history, duration: 2h -->
* Workflow Execution and History
    * How the workflow history is replayed
    * Non-determinism errors and how to avoid them
    * Side effects and `workflow.SideEffect`
    * Versioning workflows with `GetVersion`
    * Inspecting history in the `Temporal` UI

<!-- chapter: workers-and-task-queues, duration: 2h -->
* Workers and Task Queues
    * Worker process architecture
    * Task queue routing strategies
    * Worker tuning — concurrency and pollers
    * Sticky execution
    * Worker versioning

<!-- chapter: signals-queries-and-updates, duration: 3h -->
* Signals, Queries and Updates
    * Sending signals to running workflows
    * Signal handlers and buffering
    * Querying workflow state
    * `Temporal` Updates (synchronous request/response)
    * External events and wait conditions

<!-- chapter: error-handling-and-retries, duration: 2h -->
* Error Handling and Retries
    * Activity failure types
    * Retry policies — initial interval, backoff, max attempts
    * Non-retryable errors
    * Application errors vs `Temporal` errors
    * Workflow cancellation and termination

<!-- chapter: testing-temporal-workflows, duration: 2h -->
* Testing `Temporal` Workflows
    * The `Temporal` test server
    * Unit testing workflows with mocked activities
    * Time-skipping in tests
    * Replay testing from production history
    * Integration testing strategies

<!-- chapter: child-workflows-and-timers, duration: 2h -->
* Child Workflows and Timers
    * Spawning child workflows
    * Parent close policy
    * Continue-as-new for long-running workflows
    * Durable timers and `workflow.Sleep`
    * Implementing the `saga` pattern with compensation

<!-- chapter: visibility-and-monitoring, duration: 2h -->
* Visibility and Monitoring
    * `Temporal` UI — workflow search and inspection
    * Custom search attributes
    * Metrics with `Prometheus` and `Grafana`
    * Alerting on workflow failures
    * Audit logging

<!-- chapter: deployment-and-scaling, duration: 2h -->
* Deployment and Scaling
    * Running `Temporal` with `Docker Compose`
    * `Kubernetes` deployment with `Helm`
    * Scaling workers independently
    * Namespace quotas and rate limiting
    * `Temporal` Cloud — managed offering overview

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
