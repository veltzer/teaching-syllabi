---
tags:
  - data-and-ai:rag
  - data-and-ai:llm
  - data-and-ai:ai
  - languages:python
  - data-and-ai:search
level: advanced
category: ai
duration_hours: 16
audience:
  - audiences:developers
  - audiences:data-engineers
  - audiences:architects
---
<!-- course: rag_deep_dive -->
# `RAG` Deep Dive

## Description
This two day advanced course provides a comprehensive exploration of Retrieval-Augmented Generation (`RAG`) systems. Students will master chunking strategies, embedding models, vector databases, hybrid search, reranking, query transformation, and evaluation metrics. The course culminates in building production-grade `RAG` pipelines that deliver accurate and reliable results.

## Duration
16 hours / 2 days

## Intended Audience
* Software developers building `LLM`-powered applications
* Data engineers designing search and retrieval systems
* Software architects planning `RAG`-based solutions

## Prerequisites
* Strong proficiency in `Python` programming
* Working knowledge of `LLMs` and their APIs
* Basic understanding of NLP concepts and embeddings
* Familiarity with basic `RAG` concepts

## Required Knowledge
* `Python` Programming (or equivalent experience)

## Objectives
* Design and implement effective chunking strategies for diverse document types.
* Select and fine-tune embedding models for domain-specific use cases.
* Deploy and query vector databases in production environments.
* Implement hybrid search and reranking for improved retrieval quality.
* Evaluate `RAG` systems using quantitative metrics.
* Build end-to-end production `RAG` pipelines.

## Outline
<!-- chapter: foundations-of-rag-architecture, duration: 2h -->
* Foundations of `RAG` Architecture
    * `RAG` system components and data flow
    * Naive `RAG` vs. advanced `RAG` vs. modular `RAG`
    * `When` to use `RAG` vs. fine-tuning
    * Current landscape and state of the art
<!-- chapter: chunking-strategies, duration: 2h -->
* Chunking Strategies
    * Fixed-size vs. semantic chunking
    * Recursive character and token-based splitting
    * Document-aware chunking for structured formats
    * Chunk size optimization and overlap strategies
    * Parent-child and hierarchical chunking
<!-- chapter: embedding-models, duration: 2h -->
* Embedding Models
    * Embedding model architectures and comparison
    * Sentence transformers and `OpenAI` embeddings
    * Domain-specific and fine-tuned embeddings
    * Dimensionality reduction and quantization
    * Benchmarking embedding quality
<!-- chapter: vector-databases, duration: 2h -->
* Vector Databases
    * Pinecone: managed vector search at scale
    * `Weaviate`: hybrid search and multi-tenancy
    * `ChromaDB`: lightweight and developer-friendly
    * Indexing strategies and performance tuning
    * Metadata filtering and namespace management
<!-- chapter: hybrid-search-and-reranking, duration: 2h -->
* Hybrid Search and Reranking
    * Keyword search vs. semantic search
    * Combining BM25 with dense retrieval
    * Cross-encoder reranking models
    * Reciprocal rank fusion
    * Relevance score calibration
<!-- chapter: query-transformation, duration: 2h -->
* Query Transformation
    * Query decomposition and expansion
    * Hypothetical document embeddings (HyDE)
    * Multi-query retrieval
    * Step-back prompting for complex queries
    * Query routing and intent classification
<!-- chapter: evaluation-metrics, duration: 2h -->
* Evaluation Metrics
    * Retrieval metrics: precision, recall, MRR, NDCG
    * Generation metrics: faithfulness, relevance, completeness
    * End-to-end evaluation with RAGAS and DeepEval
    * Building evaluation datasets
    * Continuous evaluation in production
<!-- chapter: production-rag-pipelines, duration: 2h -->
* Production `RAG` Pipelines
    * Pipeline orchestration and workflow design
    * Caching and latency optimization
    * Handling document updates and index refresh
    * Monitoring, observability, and debugging
    * Scaling and cost management

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
