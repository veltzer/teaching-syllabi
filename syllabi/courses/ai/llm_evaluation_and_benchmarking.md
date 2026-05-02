---
tags:
  - concepts:ai
  - concepts:machine-learning
  - concepts:testing
  - concepts:test-quality
  - concepts:observability
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
<!-- course: llm_evaluation_and_benchmarking -->
# `LLM` Evaluation and Benchmarking

## Description
The hardest part of shipping `LLM`-powered features is not building the prompt. It is knowing whether a change
made the system better or worse, and being able to detect a regression before users do. Evaluation is the
discipline that answers those questions, and most teams shipping `LLM` apps have not learned it yet.

This five day course is dedicated to evaluation as the central engineering discipline for `LLM` systems. It is
the focused complement to the broader `LLM` Application Engineering course. It covers the taxonomy of evals
(reference-based, reference-free, pairwise, rubric-driven, agent-trajectory), the construction of golden
datasets and adversarial sets, `LLM`-as-judge methodology and its calibration, the major public benchmarks
and their limits, regression detection in production, eval-driven development for prompts and models, and
the eval frameworks (`OpenAI Evals`, Promptfoo, Langfuse, Braintrust, `Inspect`, custom). Participants
leave able to design eval suites that catch regressions, defend prompt and model changes with data, and avoid
the eval traps that have produced misleading public benchmark results.

## Duration
40 hours / 5 days

## Intended Audience
* `ML` engineers and developers shipping `LLM`-powered features
* engineers responsible for `LLM` quality in production
* senior engineers introducing eval discipline on a team
* architects evaluating models and prompts for procurement

## Prerequisites
* practical experience calling at least one `LLM` `API` from code
* working knowledge of `Python` (or comparable language)
* basic familiarity with prompts, embeddings and `RAG`
* exposure to traditional `ML` evaluation is helpful

## Objectives
* describe the taxonomy of `LLM` evaluations and pick the right kind
* build and maintain golden datasets and adversarial sets
* calibrate `LLM`-as-judge against human raters
* read public benchmarks critically
* set up production-time eval and regression detection
* run eval-driven development for prompts and models
* avoid the major eval mistakes that produce misleading results

## Outline
<!-- chapter: why-evaluation-is-the-hard-part, duration: 2h -->
* Why evaluation is the hard part
    * the absence of a loss function in the prompt-engineering loop
    * why "looks good in the demo" is dangerous
    * silent regressions on model upgrades
    * the cost of eval done badly: confident wrongness
    * the relationship between eval and observability
    * what evals are not
<!-- chapter: the-taxonomy-of-llm-evals, duration: 3h -->
* The taxonomy of `LLM` evals
    * reference-based evals
    * reference-free evals
    * pairwise comparison evals
    * rubric-driven evals
    * agent-trajectory evals
    * task-completion evals for tool-using systems
    * choosing the right kind for your problem
<!-- chapter: golden-datasets-the-foundation, duration: 3h -->
* Golden datasets: the foundation
    * what makes a golden set golden
    * size: how many examples are enough
    * coverage: what to include and what to leave out
    * collecting from production carefully
    * the role of synthetic data
    * privacy and `PII` in golden sets
    * versioning a golden set
    * the golden-set rot problem
<!-- chapter: adversarial-and-edge-case-sets, duration: 2h -->
* Adversarial and edge-case sets
    * out-of-distribution inputs
    * jailbreak and prompt-injection sets
    * known-difficult cases collected from production failures
    * regression-test cases tied to closed bugs
    * the "if I show this to leadership it had better work" set
    * curation discipline for adversarial sets
<!-- chapter: code-based-graders, duration: 2h -->
* Code-based graders
    * exact match, regex, schema validation
    * structured-output validators
    * reference-implementation comparison
    * deterministic evaluators for tool calls
    * code-based graders for `JSON` and `XML` outputs
    * the cases where code-based grading is enough
<!-- chapter: llm-as-judge, duration: 4h -->
* `LLM`-as-judge
    * the method and its appeal
    * choosing a judge model
    * pairwise vs single-rating judging
    * rubric design for judges
    * calibration against human raters
    * judge bias: position, length, sycophancy, self-preference
    * sample-efficient judging
    * the cost of judging at scale
<!-- chapter: human-evaluation, duration: 2h -->
* Human evaluation
    * when human eval is non-negotiable
    * inter-annotator agreement
    * the rubric as the unit of human eval
    * crowd-sourced vs in-house raters
    * sampling and stratification for human eval
    * the cost-vs-quality curve
<!-- chapter: rag-evaluation, duration: 3h -->
* `RAG` evaluation
    * answer relevance, context relevance, faithfulness
    * `RAGAS` and `TruLens`
    * decomposing `RAG` into retrieval-eval and generation-eval
    * end-to-end vs component-level evaluation
    * cross-reference to the `LLM` Application Engineering course
    * detecting hallucination programmatically
<!-- chapter: agent-and-tool-use-evaluation, duration: 3h -->
* Agent and tool-use evaluation
    * trajectory evaluation
    * tool-use correctness
    * task completion vs final-answer evaluation
    * loop and runaway detection
    * cost-bounded agent evals
    * the "did the agent take a dangerous action" eval
<!-- chapter: public-benchmarks-and-their-limits, duration: 3h -->
* Public benchmarks and their limits
    * `MMLU`, `MMLU-Pro`, `GPQA`
    * `HumanEval`, MBPP, `LiveCodeBench`
    * `MT-Bench`, `Arena-Hard`, `Chatbot Arena`
    * `IFEval` and instruction-following
    * `BIG-Bench`, `BBH`
    * benchmark contamination and leakage
    * benchmark gaming and the saturation problem
    * how to read a benchmark report critically
<!-- chapter: building-an-eval-harness, duration: 3h -->
* Building an eval harness
    * the harness as a first-class engineering artifact
    * eval frameworks: `OpenAI Evals`, Promptfoo, Langfuse, Braintrust, `Inspect`
    * custom harnesses with `pytest` and similar
    * deterministic seeding and reproducibility
    * cost control in the harness
    * `CI` integration and pull-request gating
<!-- chapter: regression-detection-in-production, duration: 3h -->
* Regression detection in production
    * online evals on production traffic
    * shadow traffic and pre-deploy evals
    * sampling for human review
    * thumbs/edits/retries as feedback signals
    * model upgrade as a silent regression
    * cross-reference to the `LLM` Application Engineering course
<!-- chapter: eval-driven-development, duration: 3h -->
* Eval-driven development
    * starting from evals before writing prompts
    * the test-driven analogy and where it breaks
    * iterating prompts against the eval suite
    * the eval-as-spec pattern
    * regression-tracking dashboards
    * keeping evals fresh as the product changes
<!-- chapter: model-procurement-and-comparison, duration: 2h -->
* Model procurement and comparison
    * picking a model from your eval suite, not from public benchmarks
    * latency and cost as eval dimensions
    * pricing-per-quality curves
    * cross-vendor procurement (`Anthropic`, `OpenAI`, `Google`, open weights)
    * fine-tuned vs base models on your evals
    * the model-bake-off as an engineering exercise
<!-- chapter: eval-anti-patterns-and-wrap-up, duration: 2h -->
* Eval anti-patterns and wrap up
    * the eval set that became the prompt training set
    * the eval that always passes
    * the judge that always agrees
    * the benchmark that became a leaderboard
    * the demo-driven eval
    * the eval that nobody owns
    * group review of a sample eval suite
    * recommended reading: `Anthropic`, `OpenAI`, `Google DeepMind` evaluation papers

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
