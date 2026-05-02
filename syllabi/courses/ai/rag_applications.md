---
tags:
  - data-and-ai:machine-learning
  - data-and-ai:llm
  - languages:python
level: intermediate
category: ai
duration_hours: 24
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: rag_applications -->
# `RAG` Applications

## Description
This course covers the design, implementation, and deployment of Retrieval-Augmented Generation
(`RAG`) applications. Participants will learn how to build systems that ground `LLM` responses in
external knowledge by combining document processing, embedding models, vector databases, and
retrieval strategies. The course includes hands-on work with `LangChain` and `LlamaIndex`,
advanced `RAG` patterns such as multi-hop and self-`RAG`, evaluation techniques, and production
deployment best practices including monitoring, observability, and hallucination mitigation.

## Duration
24 hours / 3 days

## Intended Audience
* software developers building `LLM`-powered applications
* data scientists working on knowledge-intensive `AI` systems

## Prerequisites
* Proficiency in `Python` programming
* Basic understanding of large language models and embeddings
* Familiarity with `REST` APIs and `web services`
* Experience with databases (relational or document-based)

## Required Knowledge
* `Python` Programming (or equivalent experience)

## Objectives
* **Design and implement** end-to-end `RAG` pipelines from document ingestion through retrieval and generation
* **Select and configure** appropriate embedding models, vector databases, and retrieval strategies for different use cases
* **Build `RAG` applications** using `LangChain` and `LlamaIndex` frameworks with effective prompt construction
* **Evaluate `RAG` systems** using faithfulness, relevance, and answer correctness metrics
* **Deploy and monitor** production `RAG` systems with strategies to handle hallucinations, data drift, and performance degradation

## Outline
<!-- chapter: rag-architecture-overview, duration: 2h -->
* `RAG` Architecture Overview
    * What is Retrieval-Augmented Generation
        * Motivation and use cases
        * Limitations of parametric knowledge
        * `RAG` vs fine-tuning
        * `When` to use `RAG`
    * Core components of a `RAG` system
        * Document store
        * Embedding pipeline
        * Vector database
        * Retriever
        * Generator (`LLM`)
    * End-to-end data flow
        * Ingestion pipeline
        * Query pipeline
        * Response generation
        * Feedback loops
    * Architecture patterns
        * Naive `RAG`
        * Advanced `RAG`
        * Modular `RAG`
        * Agentic `RAG`
<!-- chapter: document-loading-and-parsing, duration: 2h -->
* Document Loading and Parsing
    * Document loaders
        * `PDF` parsing (PyPDF, Unstructured, LlamaParse)
        * `HTML` and web scraping
        * Office documents (DOCX, PPTX, XLSX)
        * `Markdown` and plain text
    * Structured data extraction
        * Table extraction
        * Metadata extraction
        * Image and figure handling
        * Code block extraction
    * Data cleaning and normalization
        * Encoding handling
        * Special character removal
        * Language detection
        * Content deduplication
    * Handling diverse data sources
        * Databases and APIs
        * Confluence and wikis
        * Slack and communication tools
        * Code repositories
<!-- chapter: text-chunking-strategies, duration: 2h -->
* Text Chunking Strategies
    * Basic chunking methods
        * Fixed-size chunking
        * Sentence-based chunking
        * Paragraph-based chunking
        * Recursive character splitting
    * Semantic chunking
        * Embedding-based splitting
        * Topic-based segmentation
        * Coherence-aware chunking
    * Chunk size optimization
        * Chunk size vs retrieval quality
        * Overlap strategies
        * Context window considerations
        * Task-specific sizing
    * Advanced chunking techniques
        * Hierarchical chunking (parent-child)
        * Document summary indexing
        * Proposition-based chunking
        * Agentic chunking
<!-- chapter: embedding-models, duration: 2h -->
* Embedding Models
    * `OpenAI` embedding models
        * text-embedding-3-small and text-embedding-3-large
        * Dimensionality reduction
        * Cost considerations
    * Sentence Transformers
        * Open-source embedding models
        * Model selection criteria
        * Fine-tuning embeddings for domain-specific tasks
        * Multi-language support
    * Cohere embeddings
        * Embed `API`
        * Search vs classification embeddings
        * Input types
    * Embedding best practices
        * Normalization
        * Dimensionality trade-offs
        * Batch processing
        * Caching strategies
<!-- chapter: vector-databases, duration: 2h -->
* Vector Databases
    * Pinecone
        * Index management
        * Metadata filtering
        * Namespaces
        * Serverless vs pod-based
    * `Weaviate`
        * Schema definition
        * Hybrid search capabilities
        * Module ecosystem
        * Multi-tenancy
    * Chroma
        * Local development setup
        * Collection management
        * Filtering and querying
        * Persistence options
    * pgvector
        * `PostgreSQL` extension setup
        * Index types (IVFFlat, HNSW)
        * `SQL`-based vector queries
        * Integration with existing databases
    * Choosing a vector database
        * Scalability requirements
        * Managed vs self-hosted
        * Cost comparison
        * Feature comparison
<!-- chapter: retrieval-strategies, duration: 2h -->
* Retrieval Strategies
    * Semantic search
        * Cosine similarity
        * Approximate nearest neighbor algorithms
        * `Top`-k retrieval
        * Similarity thresholds
    * Hybrid search
        * Combining sparse and dense retrieval
        * BM25 integration
        * Reciprocal rank fusion
        * Weighted scoring
    * Re-ranking
        * Cross-encoder re-ranking
        * Cohere Rerank
        * ColBERT
        * Lost-in-the-middle mitigation
    * Advanced retrieval techniques
        * Maximal marginal relevance
        * Query expansion and transformation
        * Hypothetical document embeddings (HyDE)
        * Multi-query retrieval
<!-- chapter: langchain-and-llamaindex-frameworks, duration: 2h -->
* `LangChain` and `LlamaIndex` Frameworks
    * `LangChain` for `RAG`
        * Document loaders and text splitters
        * Retriever interfaces
        * Chain composition
        * LCEL (`LangChain` Expression Language)
    * `LlamaIndex` for `RAG`
        * Index types and abstractions
        * Query engines
        * Response synthesizers
        * Node parsers
    * Framework comparison
        * Strengths and weaknesses
        * Use case fit
        * Extensibility
        * Community and ecosystem
    * Custom pipeline construction
        * Combining framework components
        * Custom retrievers
        * Custom response generators
        * Pipeline orchestration
<!-- chapter: prompt-construction-for-rag, duration: 2h -->
* Prompt Construction for `RAG`
    * Context injection patterns
        * Stuffing context into prompts
        * Map-reduce patterns
        * Refine patterns
        * Tree summarization
    * System prompt design
        * Grounding instructions
        * Citation requirements
        * Fallback behavior
        * Output formatting
    * Dynamic prompt templates
        * Context-aware formatting
        * Metadata inclusion
        * Source attribution
        * Confidence signaling
    * Handling edge cases
        * No relevant documents found
        * Contradictory sources
        * Out-of-scope queries
        * Multi-language contexts
<!-- chapter: evaluation, duration: 2h -->
* Evaluation
    * Faithfulness evaluation
        * Grounding assessment
        * Claim verification
        * Hallucination detection
        * Source alignment
    * Relevance evaluation
        * Context relevance
        * Answer relevance
        * Query-document alignment
        * Retrieval precision and recall
    * Answer correctness
        * Factual accuracy
        * Completeness
        * Consistency
        * Human evaluation protocols
    * Evaluation frameworks
        * RAGAS
        * DeepEval
        * TruLens
        * Custom evaluation pipelines
<!-- chapter: advanced-rag-patterns, duration: 2h -->
* Advanced `RAG` Patterns
    * Multi-hop `RAG`
        * Iterative retrieval
        * Query decomposition
        * Chain-of-retrieval
        * Graph-based retrieval
    * Self-`RAG`
        * Self-reflection tokens
        * Adaptive retrieval
        * Critique and refinement
        * Quality-aware generation
    * Corrective `RAG`
        * Retrieval evaluation
        * Web search fallback
        * Knowledge refinement
        * Confidence-based routing
    * Other advanced patterns
        * RAPTOR (tree-based summarization)
        * Graph `RAG`
        * Multi-modal `RAG`
        * Conversational `RAG` with memory
<!-- chapter: production-deployment, duration: 2h -->
* Production Deployment
    * Architecture for production
        * `Microservices` design
        * Asynchronous processing
        * Queue-based ingestion
        * Caching layers
    * Scaling strategies
        * Horizontal scaling of retrieval
        * `LLM` inference optimization
        * Database sharding
        * Load balancing
    * `API` design
        * Streaming responses
        * Source citation endpoints
        * Feedback collection
        * Rate limiting
    * Infrastructure considerations
        * Containerization with `Docker`
        * `Kubernetes` orchestration
        * Cloud provider selection
        * Cost management
<!-- chapter: monitoring-and-observability, duration: 1h -->
* Monitoring and Observability
    * System metrics
        * Latency tracking (retrieval, generation, end-to-end)
        * Throughput monitoring
        * Error rates
        * Resource utilization
    * Quality monitoring
        * Answer quality over time
        * Retrieval relevance trends
        * User satisfaction tracking
        * Drift detection
    * Logging and tracing
        * Request-level tracing
        * `LLM` call logging
        * Retrieval result logging
        * Cost tracking
    * Alerting and incident response
        * Quality degradation alerts
        * Performance anomaly detection
        * Data freshness monitoring
        * Escalation procedures
<!-- chapter: handling-hallucinations, duration: 1h -->
* Handling Hallucinations
    * Understanding hallucination types
        * Intrinsic hallucinations
        * Extrinsic hallucinations
        * Factual inconsistencies
        * Fabricated citations
    * Prevention strategies
        * Improved retrieval quality
        * Grounding instructions
        * Temperature and sampling control
        * Context sufficiency checks
    * Detection methods
        * Automated fact-checking
        * Cross-reference validation
        * Confidence scoring
        * Semantic entailment checks
    * Mitigation techniques
        * Forced citation generation
        * Abstention when uncertain
        * Human-in-the-loop verification
        * Fallback responses

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
