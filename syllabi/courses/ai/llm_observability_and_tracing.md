---
tags:
  - concepts:ai
  - concepts:machine-learning
  - concepts:observability
  - concepts:operations
  - concepts:best-practices
level: advanced
category: ai
duration_hours: 24
audience:
  - audiences:ml-engineers
  - audiences:senior-developers
  - audiences:devops
  - audiences:developers
---
<!-- course: llm_observability_and_tracing -->
# `LLM` Observability and Tracing

## Description
The catalog has `LLM Application Engineering`, `LLM Evaluation and Benchmarking`, `Agentic Systems
Engineering`, and `Working with `LLMs` Securely`. Each touches observability; none is the focused
engineering of making an `LLM`-powered system observable. `LLM` systems break in ways that traditional
`APM` does not capture: a model upgrade silently shifts behavior, a prompt change tanks quality, a
tool call returns garbage and the agent loops on it, the cost per request quietly doubles. The
discipline of observing, tracing, and debugging these systems has consolidated into a small set of
tools and patterns over the past two years.

This three day course covers `LLM` observability as practiced today. It covers the unit of observation
(the trace, not the request), the canonical signals (`token` counts, latency, cost, tool calls,
retrieval results, model identity, prompt template version, evaluation scores), the platforms
(`LangSmith`, Langfuse, Helicone, Phoenix, Braintrust, Honeycomb for `LLMs`, `OpenTelemetry`
`gen_ai` semantic conventions), the local-vs-cloud question, the privacy-and-`PII` story, the prompt
versioning, the evaluation-in-production loop, the agent trajectory observability, the cost-monitoring
discipline, and the patterns that `make` production `LLM` systems debuggable. Examples cover real
production failures: the silent model regression, the prompt-injection that succeeded, the
retrieval-collapsed bug, the agent-cost-runaway. Participants leave able to `make` their `LLM` system
observable enough to debug.

## Duration
24 hours / 3 days

## Intended Audience
* `ML` engineers operating `LLM`-powered features
* senior developers shipping `LLM` integrations
* `DevOps` engineers responsible for `AI` infrastructure
* developers debugging weird `LLM` behavior

## Prerequisites
* practical experience calling at least one `LLM` `API` from code
* exposure to the `LLM Application Engineering` course
* familiarity with the `OpenTelemetry` Deep Dive course is helpful
* basic understanding of distributed tracing

## Objectives
* identify the signals that matter for `LLM` observability
* instrument `LLM` calls with the right metadata
* deploy at least one `LLM` observability platform
* trace agent trajectories
* monitor cost and quality together
* recognize the canonical `LLM` failure modes
* connect `LLM` observability to evaluation

## Outline
<!-- chapter: why-llm-observability-is-its-own-thing, duration: 1h -->
* Why `LLM` observability is its own thing
    * the trace as the unit, not the request
    * the silent regression on model upgrade
    * the prompt change that broke quality
    * cross-reference to the `LLM Application Engineering` course
    * the "our `APM` shows nothing useful" reality
<!-- chapter: the-canonical-signals, duration: 2h -->
* The canonical signals
    * `token` counts (input, output, cache)
    * latency (time-to-first-token, total)
    * cost per request
    * tool calls and their results
    * retrieval results and ranks
    * model identity and version
    * prompt template version
<!-- chapter: opentelemetry-genai-semantic-conventions, duration: 2h -->
* `OpenTelemetry` `gen_ai` semantic conventions
    * the `gen_ai.*` attributes
    * `gen_ai.system`, `gen_ai.request.model`, `gen_ai.usage.*`
    * cross-reference to the `OpenTelemetry` Deep Dive course
    * the "we standardized so we can switch platforms" argument
    * limits of the conventions today
<!-- chapter: langsmith-deep-dive, duration: 2h -->
* `LangSmith` deep dive
    * the `LangSmith` data model
    * trace and run hierarchy
    * dataset and evaluation integration
    * the `LangChain` and non-`LangChain` integrations
    * deployment options
<!-- chapter: langfuse-deep-dive, duration: 2h -->
* `Langfuse` deep dive
    * the open-source self-hostable option
    * the data model
    * scoring and prompt management
    * the cost story
    * when `Langfuse` is the right answer
<!-- chapter: helicone-and-proxy-based-observability, duration: 1h -->
* `Helicone` and proxy-based observability
    * the proxy approach
    * the per-request rate limit and cache
    * the trade-off vs `SDK` instrumentation
    * the "we routed traffic through the proxy and added 50ms" cost
<!-- chapter: phoenix-and-braintrust, duration: 1h -->
* `Phoenix` and `Braintrust`
    * `Arize Phoenix` overview
    * `Braintrust` overview
    * the eval-first orientation
    * the experimentation-loop integration
    * picking among them
<!-- chapter: tracing-agent-trajectories, duration: 3h -->
* Tracing agent trajectories
    * the trajectory as the unit
    * cross-reference to the Agentic Systems Engineering course
    * each tool call as a span
    * the "we know it failed but not where" failure
    * the long-trace problem
    * worked example
<!-- chapter: cost-and-quality-together, duration: 2h -->
* Cost and quality together
    * the cost dashboard
    * the quality dashboard
    * the cost-per-quality-unit metric
    * the alert when cost spikes without quality gain
    * cross-reference to the `LLM Application Engineering` cost chapter
<!-- chapter: production-evaluation-loop, duration: 2h -->
* Production evaluation loop
    * sampled live evaluation
    * `LLM`-as-judge in production
    * the regression-detection alert
    * cross-reference to the `LLM Evaluation and Benchmarking` course
    * the "we had no way to know quality dropped" failure
<!-- chapter: privacy-and-pii-in-traces, duration: 2h -->
* Privacy and `PII` in traces
    * traces contain prompts and responses
    * `PII` redaction
    * customer-data residency
    * the self-hosted argument
    * the "we shipped customer data to a vendor" disaster
<!-- chapter: replay-and-debugging, duration: 1h -->
* Replay and debugging
    * the replay-this-trace primitive
    * the prompt-and-context-snapshot
    * the "what would the new model do on this old trace" experiment
    * the offline-evaluation pipeline
    * the postmortem of an `LLM` regression
<!-- chapter: alerting-on-llm-systems, duration: 1h -->
* Alerting on `LLM` systems
    * cost-based alerts
    * latency-based alerts
    * quality-based alerts
    * tool-call-error-rate alerts
    * the "we paged on `5xx` and missed the silent quality drop" failure
<!-- chapter: putting-it-together, duration: 2h -->
* Putting it together
    * the observability stack for a real `LLM` product
    * the dashboards everyone reads
    * the on-call story
    * the postmortem of a real `LLM` incident
    * recommended reading: `OpenTelemetry GenAI` SIG, LangSmith/`Langfuse` docs

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
