---
tags:
  - concepts:ai
  - concepts:machine-learning
  - concepts:ethics
  - concepts:security
  - concepts:best-practices
  - concepts:testing
level: advanced
category: ai
duration_hours: 40
audience:
  - audiences:ml-engineers
  - audiences:senior-developers
  - audiences:security-engineers
  - audiences:architects
---
<!-- course: ai_safety_and_alignment -->
# `AI` Safety and Alignment

## Description
Building `AI` systems that are useful is one problem. Building `AI` systems that remain useful, honest and
controllable across the full distribution of inputs they will see in production is a different problem, and a
much harder one. This five day course is the technical complement to the ethics-and-policy material already
in the catalog. It treats `AI` safety and alignment as engineering disciplines.

The course covers the alignment problem precisely (specification, robustness, generalization), the techniques
used to align modern `LLMs` (`RLHF`, `DPO`, Constitutional `AI`, rule-based and reward-modeled training), the
evaluation methodologies that surface harm, deception and capability uplift, the red-teaming and adversarial
practices that stress-test safety, the deployment-level controls (guardrails, monitoring, escalation), and the
operational practices that keep a deployed system safe over time. The course is grounded in
public work from `Anthropic`, `OpenAI`, `Google DeepMind`, `Meta`, and academic alignment research.

## Duration
40 hours / 5 days

## Intended Audience
* `ML` engineers building or deploying `LLM`-powered systems
* security engineers working on model abuse and red-teaming
* senior engineers responsible for production `AI` quality
* architects designing systems with `AI` components in the loop

## Prerequisites
* working knowledge of `LLM` `APIs` and prompts
* basic familiarity with `Python` and at least one `ML` framework
* basic understanding of model training and fine-tuning concepts
* exposure to evaluation and testing in `ML` is helpful

## Objectives
* describe the alignment problem and its three sub-problems precisely
* compare the major alignment techniques and their tradeoffs
* design and run safety evaluations including red-team exercises
* implement deployment-level guardrails and monitoring
* respond to safety regressions in deployed `AI` systems
* contribute to a `responsible AI` deployment program with technical rigor
* read frontier alignment research critically

## Outline
<!-- chapter: the-alignment-problem-precisely, duration: 3h -->
* The alignment problem precisely
    * specification, robustness, generalization
    * the difference between capabilities and alignment
    * outer vs inner alignment
    * the agentic safety problem vs the chat-safety problem
    * what alignment is not (just RLHF, just safety filters)
    * the limits of behavioral alignment
<!-- chapter: harm-categories-and-threat-models, duration: 3h -->
* Harm categories and threat models
    * harmful content categories: violence, `CSAM`, self-harm, illegal goods
    * deception, manipulation and sycophancy
    * privacy, `PII` and re-identification
    * capability uplift for malicious actors (`CBRN`, cyber)
    * model autonomy and tool-use risks
    * indirect harms: hallucination, defamation, mis-citation
<!-- chapter: rlhf-fundamentals, duration: 3h -->
* `RLHF` fundamentals
    * the supervised fine-tuning step
    * preference data collection
    * reward model training
    * `PPO` for `RLHF`
    * reward hacking and over-optimization
    * the limits of `RLHF`
<!-- chapter: post-rlhf-techniques, duration: 3h -->
* Post-`RLHF` techniques
    * `DPO` (`direct preference optimization`)
    * `IPO`, `KTO`, `ORPO`
    * `RLAIF` and `AI`-driven preference data
    * Constitutional `AI` and `RLHF` from principles
    * online vs offline alignment
    * scaling alignment data acquisition
<!-- chapter: constitutional-ai-and-principles-based-alignment, duration: 2h -->
* Constitutional `AI` and principles-based alignment
    * `Anthropic`'s Constitutional `AI` paper
    * the constitution as a specification artifact
    * critique-and-revise training
    * combining constitutional and human feedback
    * the limits of principle-based alignment
<!-- chapter: safety-evaluations, duration: 3h -->
* Safety evaluations
    * the difference between capability evals and safety evals
    * benchmark suites: `Anthropic`'s eval, `OpenAI` evals, `MMLU`-style
    * `harmfulness` evals: `XSTest`, `BeaverTails`, `HarmBench`
    * deception and sycophancy evals
    * jailbreak resistance evals
    * dangerous capability evals: cyber, `CBRN`, autonomy
    * eval rot and gaming
<!-- chapter: red-teaming, duration: 4h -->
* Red-teaming
    * the red-team mandate and scope
    * manual red-teaming methodology
    * automated red-teaming with `LLMs`
    * jailbreak research: `DAN`, `Skeleton Key`, role-play, encoding
    * indirect prompt injection from documents and tools
    * red-teaming agentic systems
    * disclosing red-team findings responsibly
<!-- chapter: dangerous-capability-evaluations, duration: 2h -->
* Dangerous capability evaluations
    * `CBRN` uplift evaluation
    * cyber capability evaluation
    * autonomous-replication evaluation
    * persuasion and influence evaluation
    * the methodology question: what counts as evidence
    * thresholds and responsible scaling policies
<!-- chapter: deployment-time-guardrails, duration: 3h -->
* Deployment-time guardrails
    * input filters: classifiers, regex, allow/deny lists
    * output filters: classifiers, post-processing
    * `Llama Guard`, `NeMo Guardrails`, `Guardrails AI`
    * combining model-level and system-level safety
    * the layered defense model
    * cost and latency of guardrails
<!-- chapter: prompt-injection-defenses, duration: 4h -->
* Prompt injection defenses
    * direct prompt injection
    * indirect prompt injection (documents, tool outputs, web pages)
    * data exfiltration via prompt injection
    * tool-use injection in agents
    * defenses: input scoping, allow-listed tools, capability sandboxing
    * "spotlighting" and structured prompt formats
    * defense-in-depth and the limits of single-layer defense
<!-- chapter: monitoring-deployed-ai, duration: 2h -->
* Monitoring deployed `AI`
    * production-time harm telemetry
    * sampling for human review
    * detecting model drift and silent regressions
    * detecting abuse patterns
    * privacy-aware monitoring
    * the safety-and-quality dashboard
<!-- chapter: incident-response-for-ai, duration: 2h -->
* Incident response for `AI`
    * the `AI` incident: harmful output, jailbreak, data exfiltration
    * containment options: rate-limit, sample-down, swap model, kill switch
    * the relationship to security incident response
    * customer communication after an `AI` incident
    * post-incident model and prompt updates
    * the long-term lesson loop
<!-- chapter: agent-safety, duration: 2h -->
* Agent safety
    * the agentic threat model
    * tool-use risk and capability sandboxing
    * loop detection and budget limits
    * human-in-the-loop checkpoints
    * agent identity and least privilege
    * detecting and stopping runaway agents
<!-- chapter: organizational-and-policy-context, duration: 2h -->
* Organizational and policy context
    * responsible scaling policies
    * `RAI` review boards and gating
    * the relationship to ethics, legal and `PR`
    * external evaluation: `METR`, `Apollo`, `UK AISI`, `US AISI`
    * the deployment policy as a living document
<!-- chapter: case-studies-and-published-incidents, duration: 1h -->
* Case studies and published incidents
    * `Bing` Sydney and the early `LLM` incidents
    * `ChatGPT` jailbreak history
    * agent escapes documented in research papers
    * the Tay precedent and its lessons
<!-- chapter: workshop-and-wrap-up, duration: 1h -->
* Workshop and wrap up
    * red-team a sample deployed `LLM` feature
    * design walkthrough of a safety review for a new `AI` feature
    * recommended reading: `Anthropic`, `OpenAI`, `DeepMind` papers, `Christian`'s book

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
