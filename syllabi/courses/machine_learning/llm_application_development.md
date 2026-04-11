---
tags:
  - data-and-ai:llm
  - data-and-ai:ml
  - data-and-ai:nlp
  - languages:python
  - concepts:prompt-engineering
  - concepts:rag
level: intermediate
category: machine-learning
duration_hours: 16
audience:
  - audiences:developers
  - audiences:data-scientists
  - audiences:architects
---
<!-- course: llm_application_development -->
# `LLM` Application Development

## Description
This course teaches developers how to build production-ready applications powered by large language
models. Participants will learn prompt engineering techniques, retrieval-augmented generation (`RAG`),
working with embeddings and vector databases, fine-tuning strategies, and how to build autonomous
agents with function calling. The course also covers evaluation methodologies to ensure `LLM`-powered
applications are reliable and effective.

## Duration
16 hours / 2 days

## Intended Audience
* Software developers who want to integrate `LLM` capabilities into their applications.
* Data scientists and `ML` engineers looking to build `LLM`-powered products.
* Technical leads evaluating `LLM` application architectures.

## Prerequisites
* `Solid` `Python` programming skills.
* Basic understanding of `machine learning` and natural language processing concepts.
* Familiarity with `REST` APIs and `web services`.

## Required Knowledge
* `Python` Programming (or equivalent experience)

## Objectives
* Apply effective prompt engineering techniques for reliable `LLM` outputs.
* Build `RAG` pipelines using embeddings and vector databases.
* Understand and apply fine-tuning approaches for `LLMs`.
* Develop agents with function calling and tool use capabilities.
* Evaluate `LLM` application quality using appropriate metrics and frameworks.

## Outline
<!-- chapter: introduction-to-llms, duration: 2h -->
* Introduction to `LLMs`
    * How large language models work
    * Tokenization and context `windows`
    * `LLM` `API` landscape: `OpenAI`, Anthropic, open-source models
    * Cost, latency, and model selection considerations
<!-- chapter: prompt-engineering, duration: 3h -->
* Prompt Engineering
    * Prompting fundamentals and best practices
    * Zero-shot, few-shot, and chain-of-thought prompting
    * System prompts and role-based prompting
    * Structured output and output parsing
    * Prompt templates and management
    * Handling edge cases and guardrails
<!-- chapter: embeddings-and-vector-databases, duration: 2h -->
* Embeddings and Vector Databases
    * Text embeddings and semantic similarity
    * Embedding models and their tradeoffs
    * Vector database fundamentals: `Pinecone`, `ChromaDB`, `Weaviate`
    * Indexing strategies and search optimization
    * Hybrid search: combining vector and keyword search
<!-- chapter: retrieval-augmented-generation-rag, duration: 2h -->
* Retrieval-Augmented Generation (`RAG`)
    * `RAG` architecture and `design patterns`
    * Document loading, chunking, and preprocessing
    * Retrieval strategies and reranking
    * Handling multiple document types
    * Advanced `RAG` patterns: multi-step retrieval, query transformation
<!-- chapter: fine-tuning-llms, duration: 2h -->
* Fine-Tuning `LLMs`
    * `When` to fine-tune vs prompt engineering
    * Data preparation for fine-tuning
    * Fine-tuning techniques: full, `LoRA`, QLoRA
    * Evaluation of fine-tuned models
<!-- chapter: agents-and-function-calling, duration: 2h -->
* Agents and Function Calling
    * Agent architectures and reasoning patterns
    * Function calling and tool use
    * Multi-step agent workflows
    * Agent frameworks: `LangChain`, `LlamaIndex`
    * Error handling and recovery in agent systems
<!-- chapter: evaluation-and-production, duration: 3h -->
* Evaluation and Production
    * `LLM` evaluation metrics and benchmarks
    * Human evaluation strategies
    * Automated evaluation with `LLM`-as-a-judge
    * Monitoring and observability in production
    * Safety, bias, and responsible `AI` considerations

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
