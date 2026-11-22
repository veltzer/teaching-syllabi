---
tags:
  - data-and-ai:ai
  - data-and-ai:agents
  - data-and-ai:llm
  - data-and-ai:rag
  - concepts:evaluation
  - practices:cost-optimization
  - practices:observability
  - practices:production
  - practices:reliability
  - practices:security
level: intermediate
category: ai
duration_minutes: 120
audience:
  - audiences:managers
  - audiences:team-leads
  - audiences:architects
  - audiences:developers
  - audiences:sres
---

<!-- blurb: ai_in_production -->
# `AI` in Production: From Impressive Demo to Dependable System

**Technical leadership expert talk.** What it takes to run `LLM`-powered features in front of
real users: measured, guarded, observable, and affordable.

## The Challenge

An `AI` demo takes an afternoon; an `AI` feature that survives production takes engineering.
The model's output is non-deterministic, its failures look like plausible answers rather than
stack traces, its bill grows with every request, and the provider can change its behavior
under you. Teams that ship the demo as-is discover these properties from their users, their
invoice, or their security team - after release instead of before it.

## What This Session Covers

A practical, technical walk through the engineering that separates a prototype from a
production `AI` system: how to evaluate output you cannot predict, how to contain a component
that can be talked into misbehaving, how to see what it is doing, and how to keep it fast,
affordable, and stable as models and prompts change.

## Agenda

* **Why Production Is Different** (10 min): Non-determinism, silent failures, and external dependencies; why the practices that work for ordinary services are necessary but not sufficient.
* **Choosing and Integrating Models** (15 min): Hosted versus self-hosted models, when retrieval-augmented generation (`RAG`) or agents are justified, and keeping the application independent of a single provider.
* **Evaluation Before and After Release** (20 min): Building evaluation sets from real cases, automated and human grading, regression gates in the release pipeline, and measuring quality on live traffic.
* **Guardrails and Security** (20 min): Prompt injection, data leakage, and excessive agent permissions; input and output validation, least privilege for tools, and keeping a human in the loop where it matters.
* **Observability and Monitoring** (15 min): Tracing prompts, responses, and tool calls; the quality, drift, and usage signals worth alerting on; handling logged user data responsibly.
* **Cost and Latency** (15 min): Token budgets, caching, model routing, streaming, and batching; trading quality against price and response time with numbers instead of guesses.
* **Reliability and Change Management** (15 min): Timeouts, retries, fallbacks, and rate limits; versioning prompts and models, staged rollouts, and rolling back a behavior change.
* **Key Takeaways and Q&A** (10 min): A production-readiness checklist for teams about to ship an `AI` feature.

## Takeaways

* A clear understanding of how `AI` components fail in production and why those failures are easy to miss
* A practical approach to evaluation, guardrails, and observability for `LLM`-powered features
* Concrete techniques for controlling cost, latency, and the risk of model and prompt changes
* A production-readiness checklist to apply before the next `AI` release

## Who Should Attend

* Engineering managers
* Tech leads
* Software architects
* Developers building `AI`-powered features
* Site reliability engineers operating them

## Continue the Journey

This talk maps the territory. A follow-on, hands-on workshop can take one of the team's own
`AI` features and put an evaluation suite, guardrails, tracing, and a rollout plan around it.

## Speaker

Mark Veltzer
