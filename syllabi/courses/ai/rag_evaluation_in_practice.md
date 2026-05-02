---
tags:
  - concepts:ai
  - concepts:rag
  - concepts:testing
  - concepts:best-practices
level: advanced
category: ai
duration_hours: 16
audience:
  - audiences:ml-engineers
  - audiences:senior-developers
  - audiences:developers
  - audiences:qa-engineers
---
<!-- course: rag_evaluation_in_practice -->
# `RAG` Evaluation in Practice

## Description
The catalog has `RAG Applications`, `RAG Deep Dive`, `LLM Evaluation and Benchmarking`, and `Vector
Databases Engineering`. None is the focused course on the specific discipline of evaluating a ``RAG``
system in production. `RAG` evaluation is harder than general `LLM` evaluation because the failure can
be in retrieval (the wrong chunks were returned) or in generation (the right chunks were returned but
the model still hallucinated) or in the seam between them, and the team has to know which. Most teams
ship `RAG` and never measure either side until users complain.

This two day course covers `RAG` evaluation as practiced today. It covers the two-axis decomposition
(retrieval and generation), the metrics for each axis (`recall@k`, MRR, `nDCG` for retrieval;
`groundedness`, faithfulness, `answer relevance`, `context relevance` for generation), the canonical
frameworks (`Ragas`, TruLens, DeepEval, Phoenix, `LangSmith`), the dataset construction (golden
sets, synthetic evaluation sets, the labelling effort), the offline-vs-online evaluation, the
production sampling approach, the regression-detection workflow, the cost shape of evaluation, and the
patterns that `make` `RAG` evaluation succeed. Examples include real production `RAG` systems and the
specific failures their evaluation caught. Participants leave able to set up a `RAG` evaluation system
that catches regressions before users do.

## Duration
16 hours / 2 days

## Intended Audience
* `ML` engineers shipping a `RAG` feature
* senior developers maintaining a `RAG` pipeline
* `QA` engineers extending evaluation to `RAG`
* developers debugging weird `RAG` answers

## Prerequisites
* practical experience with `RAG`
* exposure to the `RAG Applications` or `RAG Deep Dive` course
* familiarity with the `LLM Evaluation and Benchmarking` course
* working knowledge of `Python`

## Objectives
* decompose `RAG` failure into retrieval vs generation
* compute retrieval metrics (`recall@k`, MRR, `nDCG`)
* compute generation metrics (groundedness, faithfulness)
* construct a golden set the team can maintain
* run online evaluation in production
* detect regressions before users do
* recognize the patterns that doom `RAG` evaluation

## Outline
<!-- chapter: why-rag-evaluation-is-its-own-thing, duration: 1h -->
* Why `RAG` evaluation is its own thing
    * the two-axis problem
    * the failure-attribution question
    * cross-reference to the `RAG Deep Dive` course
    * cross-reference to the `LLM Evaluation and Benchmarking` course
    * the "users complained but our `LLM` evals passed" reality
<!-- chapter: the-two-axes, duration: 1h -->
* The two axes
    * retrieval: did we get the right chunks
    * generation: did we use the chunks we got
    * the seam: did we ground correctly
    * the "the chunk had the answer and the model ignored it" failure
    * the "the chunk did not have the answer and the model invented one" failure
<!-- chapter: retrieval-metrics, duration: 2h -->
* Retrieval metrics
    * `recall@k`
    * `precision@k`
    * `MRR` (mean reciprocal rank)
    * `nDCG` (normalized discounted cumulative gain)
    * `hit rate`
    * picking the metric for the system
<!-- chapter: generation-metrics, duration: 2h -->
* Generation metrics
    * groundedness / faithfulness
    * answer relevance
    * context relevance
    * the `LLM`-as-judge approach
    * the "the judge had the same biases as the model" failure
<!-- chapter: ragas-deep-dive, duration: 2h -->
* `Ragas` deep dive
    * the `Ragas` metrics suite
    * the `Ragas` evaluation pipeline
    * dataset construction with `Ragas`
    * the gotchas at scale
    * the cost story
<!-- chapter: trulens-deepeval-and-phoenix, duration: 1h -->
* `TruLens`, DeepEval, and `Phoenix`
    * `TruLens` overview
    * `DeepEval` overview
    * `Arize Phoenix` evals
    * `LangSmith` evals integration
    * picking among them
<!-- chapter: golden-sets, duration: 2h -->
* Golden sets
    * the questions-and-correct-answers list
    * the labelling effort
    * the domain-expert review
    * the "we used 20 questions and called it a day" failure
    * the per-feature golden set
<!-- chapter: synthetic-evaluation-sets, duration: 1h -->
* Synthetic evaluation sets
    * `LLM`-generated `Q/A` from documents
    * the diversity-and-difficulty knobs
    * the validation against humans
    * the "the synthetic set looked good but missed real failures" trap
    * combining synthetic and golden
<!-- chapter: offline-evaluation, duration: 1h -->
* Offline evaluation
    * the `CI`-time evaluation
    * the threshold-gate
    * the per-`PR` evaluation
    * the cost budget for offline eval
    * the "evaluation took 4 hours so we turned it off" failure
<!-- chapter: online-evaluation, duration: 1h -->
* Online evaluation
    * sampled live evaluation
    * the implicit feedback signals (thumbs up/down, follow-up question)
    * cross-reference to the `LLM` Observability and Tracing course
    * the regression-detection alert
    * the "we missed the regression for two weeks" reality
<!-- chapter: regression-detection-and-the-workflow, duration: 1h -->
* Regression detection and the workflow
    * the per-axis trend
    * the per-segment trend (this customer, this question type)
    * the alert
    * the on-call workflow when the alert fires
    * the postmortem of a `RAG` regression
<!-- chapter: when-rag-evaluation-cannot-help, duration: 1h -->
* `When` `RAG` evaluation cannot help
    * the "the corpus does not contain the answer" reality
    * the question outside the trained domain
    * the policy decision that the model should refuse
    * the "we evaluated answers, not refusals" gap
    * the bigger system-design problem

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
