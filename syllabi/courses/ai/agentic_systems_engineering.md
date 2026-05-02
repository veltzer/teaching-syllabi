---
tags:
  - concepts:ai
  - concepts:machine-learning
  - concepts:observability
  - concepts:operations
  - concepts:performance
  - concepts:best-practices
level: advanced
category: ai
duration_hours: 40
audience:
  - audiences:ml-engineers
  - audiences:senior-developers
  - audiences:developers
  - audiences:architects
---
<!-- course: agentic_systems_engineering -->
# Agentic Systems Engineering

## Description
The catalog has an `AI Agents Development` course that covers the conceptual side of building agents. This
course is the production-engineering complement. Agentic systems behave very differently from chatbots: they
take actions in the world, they fail in compounding ways, they have emergent costs, and the tooling for
operating them in production is still maturing. Most teams shipping agents are figuring this out the hard
way.

This five day course covers agentic systems as their own engineering discipline. It covers the agent loop
and its variants, planning and decomposition, tool design from an agent's perspective, error recovery and
retry semantics, sub-agent orchestration, the cost-and-budget story, observability and debugging, evaluation
specifically for agents, the security model for agentic systems, and the deployment patterns. Examples are
drawn from public work on Claude agents, `OpenAI` Assistants, `LangGraph`, `CrewAI`, `AutoGen`, `Semantic
Kernel`, and the engineering blogs of organizations shipping production agents. Participants leave able to
ship agentic systems that are debuggable, bounded, observable, and safe.

## Duration
40 hours / 5 days

## Intended Audience
* `ML` engineers shipping agentic features in production
* senior developers introducing agents into existing products
* architects designing systems with autonomous components
* engineers responsible for the cost or safety of an agent in production

## Prerequisites
* practical experience calling at least one `LLM` `API` from code
* working knowledge of `Python` (or comparable language)
* exposure to the `LLM` Application Engineering and `LLM` Evaluation courses is helpful
* basic familiarity with prompts, embeddings and tool use

## Objectives
* describe the agent loop and pick a variant for the problem
* design tools so that an agent can use them reliably
* implement budget and recovery semantics for agents
* observe and debug agent behavior in production
* evaluate agents at the trajectory level, not just the answer level
* deploy agents with appropriate safety and security
* recognize the cases where an agent is the wrong tool

## Outline
<!-- chapter: what-an-agent-actually-is, duration: 2h -->
* What an agent actually is
    * the spectrum from prompt to chain to agent
    * the `ReAct` pattern revisited
    * tool-calling agents vs planning agents
    * autonomous vs human-in-the-loop
    * what counts as an agent vs what is just a workflow
    * cross-reference to the existing `AI Agents Development` course
<!-- chapter: the-agent-loop-and-its-variants, duration: 3h -->
* The agent loop and its variants
    * the basic perceive-plan-act loop
    * `ReAct` and reasoning-then-action
    * `Reflexion` and self-correction
    * tree-of-thoughts and planning
    * `Plan-and-Execute` agents
    * the cases for each variant
<!-- chapter: tool-design-for-agents, duration: 4h -->
* Tool design for agents
    * tools as the agent's `API` to the world
    * naming and description: the agent reads them
    * argument schemas and validation
    * deterministic vs non-deterministic tools
    * idempotent tools and the retry semantics
    * cross-reference to the Idempotency course
    * the "tool that does too much" anti-pattern
    * the tool-discoverability problem at high tool counts
<!-- chapter: planning-and-decomposition, duration: 3h -->
* Planning and decomposition
    * step decomposition strategies
    * the plan-then-execute pattern
    * dynamic vs static plans
    * sub-task generation
    * planning errors and how to recover
    * the "agent makes plan that does not match available tools" failure
<!-- chapter: state-and-memory, duration: 3h -->
* State and memory
    * conversation memory
    * task-state memory
    * working-memory vs long-term memory
    * memory storage: vector store, key-value, structured
    * cross-reference to the Vector Databases Engineering course
    * the memory-poisoning attack vector
    * forgetting and the relevance-decay problem
<!-- chapter: error-recovery-and-retry-semantics, duration: 3h -->
* Error recovery and retry semantics
    * tool-call error handling
    * the loop budget and termination conditions
    * compensation: undoing partial work
    * cross-reference to the Idempotency course's `saga` chapter
    * the "agent retries the same thing forever" failure
    * graceful escalation to human
<!-- chapter: sub-agent-orchestration, duration: 3h -->
* Sub-agent orchestration
    * the orchestrator-and-workers pattern
    * specialist sub-agents
    * communication between agents
    * shared state vs message-passing
    * `LangGraph`, `CrewAI`, `AutoGen` for orchestration
    * the "I made it agents all the way down" anti-pattern
<!-- chapter: cost-engineering-for-agents, duration: 3h -->
* Cost engineering for agents
    * the per-loop cost model
    * the cost-explosion failure mode
    * loop budgets and cost limits
    * cheaper-model routing within an agent
    * caching repeated tool calls
    * cross-reference to the `LLM` Application Engineering course's cost chapter
<!-- chapter: observability-for-agents, duration: 3h -->
* Observability for agents
    * the trajectory as the unit of observation
    * structured logging of plans, tool calls, results
    * distributed tracing across agent steps
    * `LangSmith`, Langfuse, Helicone, Phoenix, `Braintrust` for agents
    * the "what was it doing before it broke" requirement
    * cross-reference to the `LLM` Application Engineering course's observability chapter
<!-- chapter: evaluating-agents, duration: 3h -->
* Evaluating agents
    * trajectory evals vs final-answer evals
    * tool-use correctness
    * task completion rate
    * cost-bounded evaluation
    * adversarial scenarios
    * cross-reference to the `LLM` Evaluation and Benchmarking course
    * the public benchmarks: `SWE-bench`, WebArena, AgentBench, `GAIA`
<!-- chapter: deployment-patterns, duration: 3h -->
* Deployment patterns
    * synchronous vs asynchronous agent invocation
    * agents as background workers
    * agents as part of a request handler
    * long-running agents and durable execution
    * Temporal and `Cadence` for agent durability
    * cross-reference to the Workflow course material
<!-- chapter: human-in-the-loop, duration: 2h -->
* Human-in-the-loop
    * approval gates on critical actions
    * the "ask before deleting" pattern
    * progressive autonomy levels
    * the right `UX` for human review
    * the cost-of-human-review economics
<!-- chapter: agent-safety-and-security, duration: 3h -->
* Agent safety and security
    * the agentic threat model revisited
    * cross-reference to the `AI` Safety and Alignment course
    * least-privilege tool access
    * sandboxing tool execution
    * indirect prompt injection from tool outputs
    * the data-exfiltration risk
    * audit trails for agent actions
<!-- chapter: anti-patterns-failure-modes-and-wrap-up, duration: 2h -->
* Anti-patterns, failure modes and wrap up
    * the agent that loops forever
    * the agent that hallucinated a tool
    * the agent that used the right tool wrong
    * the agent that succeeded for the wrong reason
    * the cost runaway
    * the silent regression on model upgrade
    * design walkthrough of a production agent
    * recommended reading: `ReAct`, Reflexion, Voyager, `SWE-agent` papers

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
