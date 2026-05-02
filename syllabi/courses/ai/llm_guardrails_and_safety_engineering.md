---
tags:
  - concepts:ai
  - concepts:security
  - concepts:best-practices
  - concepts:operations
level: advanced
category: ai
duration_hours: 24
audience:
  - audiences:ml-engineers
  - audiences:senior-developers
  - audiences:security-engineers
  - audiences:developers
---
<!-- course: llm_guardrails_and_safety_engineering -->
# `LLM` Guardrails and Safety Engineering

## Description
The catalog has `AI Safety and Alignment` (the research-and-policy course), ```AI`` Ethics and Responsible
`AI``, `Working with `LLMs` Securely`, and ``LLM` Application Engineering`. None of those covers the
day-to-day engineering of putting guardrails on an `LLM`-powered product: input validation, output
validation, jailbreak resistance, `PII` handling at the boundary, content filtering, refusal-policy
enforcement, and the operational reality of running a moderation pipeline in production. Guardrails
are now a separate engineering layer with its own libraries (`Llama Guard`, `Guardrails AI`,
`NeMo Guardrails`, Lakera, `Protect AI`), its own evaluation methodology, and its own failure modes.

This three day course covers `LLM` guardrails as a focused engineering practice. It covers the
threat-model of an `LLM` product (jailbreak, prompt injection, data exfiltration, harmful generation,
`PII` leak), the input-side guardrails (`PII` redaction, prompt-injection detection, topic
classification, length and rate limits), the output-side guardrails (toxicity, bias, hallucination,
`PII` leak from training data, brand-safety), the policy-engine approach (`NeMo Guardrails`'s `Colang`,
`Guardrails AI` validators), the off-the-shelf models (`Llama Guard`, `Prompt Guard`, `Lakera Guard`,
`Azure AI Content Safety`), the evaluation methodology, the latency and cost cost of guardrails, the
red-team workflow, and the patterns that `make` guardrails work without making the product unusable.
Examples include real production deployments. Participants leave able to design and operate the
guardrail layer for an `LLM` product.

## Duration
24 hours / 3 days

## Intended Audience
* `ML` engineers building consumer-facing `LLM` features
* senior developers responsible for `AI` product safety
* security engineers reviewing `LLM` systems
* developers shipping `LLM`-powered features in regulated industries

## Prerequisites
* practical experience calling at least one `LLM` `API` from code
* exposure to the `LLM Application Engineering` course
* familiarity with the Working with `LLMs` Securely course
* basic understanding of content moderation

## Objectives
* threat-model an `LLM` product
* design input-side guardrails
* design output-side guardrails
* deploy at least one off-the-shelf guardrail model
* evaluate the guardrail layer
* operate guardrails in production
* recognize when guardrails are over-engineered

## Outline
<!-- chapter: the-threat-model, duration: 2h -->
* The threat model
    * jailbreak attempts
    * prompt injection (direct and indirect)
    * data exfiltration
    * harmful generation
    * `PII` leak from training data
    * brand-safety violation
    * cross-reference to the Working with `LLMs` Securely course
<!-- chapter: input-side-guardrails, duration: 3h -->
* Input-side guardrails
    * `PII` detection and redaction
    * prompt-injection detection
    * topic classification (allowed vs disallowed)
    * length and rate limits
    * the "we sanitized for `SQL` injection but not prompt injection" failure
    * cross-reference to the Multimodal `AI` Engineering course (image and audio injection)
<!-- chapter: output-side-guardrails, duration: 3h -->
* Output-side guardrails
    * toxicity classification
    * `PII` detection in outputs
    * brand-safety filters
    * hallucination detection (citation-grounded check)
    * the "the model said something that violated policy" incident
    * the "we filtered legitimate output" false-positive rate
<!-- chapter: llama-guard-and-prompt-guard, duration: 2h -->
* `Llama Guard` and `Prompt Guard`
    * `Llama Guard` overview
    * the policy taxonomy
    * `Prompt Guard` for injection detection
    * deployment options
    * the cost shape
<!-- chapter: nemo-guardrails-and-colang, duration: 2h -->
* `NeMo Guardrails` and `Colang`
    * the dialogue-flow approach
    * `Colang` as the policy language
    * input rails, dialogue rails, output rails
    * worked example
    * when `NeMo Guardrails` is the right answer
<!-- chapter: guardrails-ai, duration: 1h -->
* `Guardrails AI`
    * the validator-based approach
    * the validator library
    * `RAIL` specifications
    * deployment as a sidecar
    * the trade-offs vs `NeMo Guardrails`
<!-- chapter: managed-guardrail-services, duration: 1h -->
* Managed guardrail services
    * `Lakera Guard`
    * `Azure AI Content Safety`
    * `AWS Bedrock Guardrails`
    * `Protect AI`
    * the buy-vs-build decision
<!-- chapter: pii-and-data-classification, duration: 2h -->
* `PII` and data classification
    * what counts as `PII`
    * `Microsoft Presidio` for `PII` detection
    * the per-jurisdiction question
    * cross-reference to the `GDPR` and Compliance course
    * the "we redacted `PII` and broke the conversation" failure
<!-- chapter: refusal-policy-engineering, duration: 2h -->
* Refusal policy engineering
    * what the model should refuse
    * how to refuse without being unhelpful
    * the over-refusal vs under-refusal trade-off
    * the "we refused everything and users left" failure
    * tuning the policy
<!-- chapter: evaluating-guardrails, duration: 2h -->
* Evaluating guardrails
    * the attack-success rate
    * the false-positive rate
    * the latency cost
    * red-teaming the guardrails
    * cross-reference to the Red Team Operations course
<!-- chapter: latency-and-cost, duration: 1h -->
* Latency and cost
    * each guardrail adds latency
    * the parallelization opportunity
    * the streaming-output guardrail challenge
    * the "guardrails doubled our cost" reality
    * picking the budget
<!-- chapter: production-operations, duration: 2h -->
* Production operations
    * monitoring guardrail trips
    * the alert when attack rate spikes
    * the human-review queue
    * the policy-update cadence
    * the postmortem of a guardrail miss
<!-- chapter: when-guardrails-are-over-engineered, duration: 1h -->
* `When` guardrails are over-engineered
    * the internal-only system
    * the trusted-user system
    * the "guardrails everywhere" cost
    * the user-facing-product reality
    * picking the right level

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
