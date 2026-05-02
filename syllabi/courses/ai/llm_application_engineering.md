---
tags:
  - concepts:ai
  - concepts:machine-learning
  - concepts:prompt-engineering
  - concepts:rag
  - concepts:observability
  - concepts:performance
  - concepts:cloud-economics
level: intermediate
category: ai
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:ml-engineers
  - audiences:architects
---
<!-- course: llm_application_engineering -->
# `LLM` Application Engineering

## Description
A surprising number of `LLM` projects `make` it from prototype to production and then quietly fall apart. They are slow,
expensive, hard to debug, drift over time, and break in ways that the original developers never imagined.
This five day course is about everything that happens after a working prototype: the engineering discipline required
to operate `LLM`-powered applications reliably and economically at production scale.

The course assumes participants already know the basics of prompts, embeddings and `RAG`. It focuses instead on
evaluation harnesses, observability, regression detection, latency and cost optimization, guardrails and safety,
deployment topologies, A/B testing and gradual rollouts, fallback strategies, and the operational discipline that
turns an `LLM` app into a real product. Where useful, the course contrasts choices specific to closed-`API` providers
(`Anthropic`, `OpenAI`, `Google`) with self-hosted open-weight models.

## Duration
40 hours / 5 days

## Intended Audience
* developers who have shipped an `LLM` prototype and need to take it to production
* senior engineers and tech leads owning `LLM`-backed features
* `ML` engineers operating `LLM` systems alongside traditional `ML` pipelines
* architects designing systems that incorporate `LLM` calls

## Prerequisites
* practical experience calling at least one `LLM` `API` from code
* basic familiarity with prompts, tokens and embeddings
* working knowledge of one general-purpose programming language, ideally `Python` or `TypeScript`
* basic understanding of cloud deployment

## Objectives
* design `LLM` applications that can be evaluated, monitored and improved over time
* build evaluation harnesses with golden sets and automated graders
* instrument `LLM` calls for observability and cost attribution
* detect and respond to model and prompt regressions
* optimize latency and cost without sacrificing quality
* implement guardrails for safety, accuracy and policy
* deploy `LLM` applications with sensible rollout and fallback strategies
* manage prompt and model lifecycle as you would any other software artifact

## Outline
<!-- chapter: from-prototype-to-production, duration: 2h -->
* From prototype to production
    * why most `LLM` prototypes fail in production
    * the production checklist: evals, observability, fallback, cost
    * shapes of `LLM` applications: chatbot, agent, `copilot`, pipeline, batch
    * the engineering surface area you actually own
<!-- chapter: prompt-and-context-design-revisited, duration: 2h -->
* Prompt and context design revisited
    * structured vs unstructured prompts
    * system, user and assistant role design
    * tool use and structured outputs
    * `JSON` mode and schema-constrained generation
    * prompt management as code: storing, versioning, testing
    * prompt size, context `windows` and what to include
<!-- chapter: evaluation-fundamentals, duration: 3h -->
* Evaluation fundamentals
    * why human spot-checks do not scale
    * the four kinds of `LLM` eval: reference-based, reference-free, pairwise, rubric
    * golden sets and how to build them
    * adversarial sets and out-of-distribution inputs
    * eval drift over time
    * the difference between evaluating a model and evaluating an application
<!-- chapter: building-an-eval-harness, duration: 3h -->
* Building an eval harness
    * eval as a first-class engineering artifact
    * eval frameworks: `OpenAI Evals`, Promptfoo, Langfuse, `Braintrust`, custom
    * `LLM`-as-judge: setup, calibration, pitfalls
    * code-based graders for structured outputs
    * eval reproducibility and seeding
    * incorporating evals into `CI`
<!-- chapter: rag-evaluation-and-tuning, duration: 2h -->
* `RAG` evaluation and tuning
    * recall, precision and faithfulness
    * answer relevance vs context relevance
    * `RAGAS`, `TruLens` and similar tools
    * tuning chunking, retrieval and re-ranking against evals
    * detecting hallucination
<!-- chapter: agent-evaluation, duration: 2h -->
* Agent evaluation
    * trajectory evaluation vs final-answer evaluation
    * tool-use correctness
    * loop detection and runaway behavior
    * cost-bounded agent evaluation
    * red-teaming agents
<!-- chapter: observability-for-llm-apps, duration: 3h -->
* Observability for `LLM` apps
    * the three pillars in an `LLM` context
    * tracing across model calls, retrievals, tool calls
    * `OpenTelemetry` for `LLM` workloads and `OpenLLMetry`
    * `Langfuse`, Helicone, Phoenix, `LangSmith`
    * structured logging of prompts and outputs
    * privacy-aware logging
<!-- chapter: cost-and-latency-engineering, duration: 4h -->
* Cost and latency engineering
    * the cost model: input tokens, output tokens, cache, tools
    * prompt caching and context reuse
    * batching strategies
    * model cascades and routing to cheaper models
    * speculative decoding and parallel sampling
    * streaming responses for perceived latency
    * cost dashboards and per-feature attribution
<!-- chapter: guardrails-and-safety, duration: 4h -->
* Guardrails and safety
    * input guardrails: filtering, classification, redaction
    * output guardrails: validation, refusal detection, policy checks
    * `Guardrails`, `NeMo Guardrails`, `Llama Guard`
    * prompt injection and indirect prompt injection
    * data exfiltration through prompts
    * jailbreak resistance and abuse handling
    * safe defaults vs strict modes
<!-- chapter: structured-outputs-and-tool-use, duration: 2h -->
* Structured outputs and tool use
    * function calling vs structured output schemas
    * validating and repairing structured outputs
    * partial output handling and streaming `JSON`
    * tool design for reliability
    * deterministic post-processing where possible
<!-- chapter: deployment-topologies, duration: 2h -->
* Deployment topologies
    * client-side vs server-side `LLM` calls
    * proxy and gateway patterns
    * `LLM` gateways: LiteLLM, `Portkey`, custom
    * self-hosted vs hosted models
    * `vLLM`, `TGI` and inference servers
    * `GPU` capacity planning at a high level
<!-- chapter: rollout-and-experimentation, duration: 2h -->
* Rollout and experimentation
    * shadow mode for new prompts and models
    * A/B testing `LLM` features
    * canary releases for prompts
    * gradual model migrations (`Claude 4.6` to `Claude 4.7`, etc.)
    * holdback groups for long-term quality measurement
<!-- chapter: regression-detection-and-drift, duration: 2h -->
* Regression detection and drift
    * model upgrades as silent regressions
    * eval-driven model selection
    * monitoring quality metrics in production
    * user-feedback signals: thumbs, edits, retries
    * detecting drift in inputs and outputs
<!-- chapter: caching-and-determinism, duration: 2h -->
* Caching and determinism
    * what is cacheable in an `LLM` system
    * prompt caching and prefix caching
    * semantic caching with embeddings
    * temperature, top-`p`, seed and reproducibility
    * cache invalidation strategies
<!-- chapter: data-and-feedback-loops, duration: 2h -->
* Data and feedback loops
    * collecting user feedback responsibly
    * building a labeled dataset from production traffic
    * fine-tuning vs prompt-engineering vs `RAG` for a given problem
    * synthetic data generation for evals
    * privacy and compliance for production traces
<!-- chapter: failure-modes-and-fallback-strategies, duration: 2h -->
* Failure modes and fallback strategies
    * model `API` outages
    * rate limits and quota exhaustion
    * timeout and retry policies for `LLM` calls
    * graceful degradation: smaller model, cached answer, deterministic path
    * multi-provider strategies and lock-in
<!-- chapter: case-studies-and-wrap-up, duration: 1h -->
* Case studies and wrap up
    * walkthrough of two production `LLM` applications
    * common organizational patterns
    * recommended reading and tooling

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
