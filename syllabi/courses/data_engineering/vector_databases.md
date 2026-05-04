---
tags:
  - databases:vector
  - concepts:embeddings
  - concepts:databases
  - concepts:operations
  - concepts:best-practices
level: advanced
category: data-engineering
duration_hours: 24
audience:
  - audiences:data-engineers
  - audiences:ml-engineers
  - audiences:senior-developers
  - audiences:devops
---
<!-- course: vector_databases -->
# Vector Databases Engineering

## Description
Vector databases store embeddings and answer "which vectors are closest to this one?" at low latency.
Every modern `RAG` system, semantic search engine, recommendation system, and multimodal application
depends on one. The catalog has `RAG Applications`, `LLM Application Engineering`, and
`Generative AI Applications` courses, but each treats the vector database as an opaque dependency. None
covers the engineering of the vector database itself: the index choice, the recall-vs-latency curve,
the dimensionality and quantization trade-offs, the hybrid search problem, the metadata filtering
problem, the freshness story, and the operational realities of serving similarity search at production
scale.

This three day course covers the vector database as its own system. It covers the index families
(`HNSW`, `IVF`, `IVF-PQ`, `DiskANN`), the canonical implementations (Pinecone, `Weaviate`,
`Qdrant`, `Milvus`, `pgvector`, `Vespa`, `Elastic`/`OpenSearch` k-NN), the embedding pipeline,
the hybrid-search question (sparse plus dense), the metadata-filtering question (pre-filter vs
post-filter), the multi-tenancy story, and the operational realities of recall measurement, index
rebuilding, and cost at scale. Participants leave able to choose between buy and build, design the
indexing and serving sides correctly, measure recall honestly, and operate a vector database under
load.

## Duration
24 hours / 3 days

## Intended Audience
* data engineers introducing a vector database into an organization
* `ML` engineers building `RAG`, semantic search, or recommendation systems
* backend engineers asked to "just add semantic search"
* platform engineers building paved roads for `AI` applications

## Prerequisites
* working knowledge of `SQL` and at least one operational database
* basic linear algebra: dot product, cosine similarity, Euclidean distance
* exposure to embeddings (the `LLM Application Engineering` or `RAG Applications` course is helpful)

## Objectives
* explain why a vector database is necessary and when a regular database suffices
* choose between `HNSW`, `IVF`, `IVF-PQ`, and `DiskANN` based on recall, latency, and memory budgets
* design the embedding pipeline without skew between indexing and querying
* solve the hybrid-search problem combining lexical and semantic relevance
* solve the metadata-filtering problem without recall collapse
* measure recall and latency honestly, not just QPS
* operate a vector database at low latency under load
* choose between Pinecone, `Qdrant`, `Weaviate`, `Milvus`, `pgvector`, and a managed offering

## Outline
<!-- chapter: what-a-vector-database-actually-is, duration: 2h -->
* What a vector database actually is
    * the similarity-search problem and why it is not a `SQL` `WHERE` clause
    * dense embeddings, the high-dimensional curse, and approximate nearest neighbour
    * what a vector database is not: a feature store, a search engine, a key-value store
    * cross-reference to the `Feature Store Engineering` course
    * the use cases that justify one and the ones that do not
<!-- chapter: distance-metrics-and-the-embedding-model, duration: 2h -->
* Distance metrics and the embedding model
    * cosine, dot product, Euclidean, and when each is correct
    * the model decides the metric, not the database
    * the "we changed the embedding model and recall collapsed" failure
    * normalised vs unnormalised vectors
    * the dimension-and-precision question
<!-- chapter: index-families, duration: 3h -->
* Index families
    * brute-force flat: when it is the right answer
    * `IVF`: inverted file index, the `nprobe` knob, the recall curve
    * `HNSW`: hierarchical navigable small world, the `M` and `efSearch` knobs
    * `IVF-PQ` and product quantization: memory savings, recall cost
    * `DiskANN` and `SPANN`: when the index does not fit in memory
    * the recall-vs-latency-vs-memory triangle
<!-- chapter: recall-and-the-honest-benchmark, duration: 2h -->
* Recall and the honest benchmark
    * recall@k, the only metric that matters
    * how to measure recall: ground truth via brute-force flat
    * the QPS-vs-recall curve and the operating point
    * the "vendor benchmark at recall 0.7 looks great" trap
    * load testing under realistic distributions
<!-- chapter: hybrid-search, duration: 2h -->
* Hybrid search
    * dense alone misses keyword matches
    * sparse alone misses paraphrase
    * `BM25` plus dense, reciprocal rank fusion, learned fusion
    * `SPLADE` and learned sparse retrieval
    * the architecture: two indexes, one query, one merge
    * cross-reference to the `RAG Applications` course
<!-- chapter: metadata-filtering, duration: 2h -->
* Metadata filtering
    * the multi-tenant filter (`tenant_id == X`)
    * pre-filter vs post-filter and the recall-collapse failure
    * filter selectivity and the index implications
    * partitioned indexes vs single index with filter
    * the "tenant has ten vectors and recall is zero" failure
<!-- chapter: pinecone-and-managed-offerings, duration: 2h -->
* Pinecone and managed offerings
    * the Pinecone architecture and pod model
    * the namespace as the multi-tenant unit
    * pricing model and the operating cost at scale
    * `Vertex AI` Vector Search, `OpenSearch` Serverless k-NN
    * `MongoDB` Atlas Vector Search, `Azure AI Search`
    * the buy-vs-build decision
<!-- chapter: qdrant-weaviate-milvus-deep-dive, duration: 3h -->
* `Qdrant`, `Weaviate`, and `Milvus` deep dive
    * `Qdrant`: the operational sweet spot
    * `Weaviate`: the schema-and-modules model
    * `Milvus`: the high-scale architecture
    * collections, partitions, segments, shards
    * the operational model: ingest, snapshot, replicate
    * gotchas at production scale
<!-- chapter: pgvector-and-the-postgres-question, duration: 2h -->
* `pgvector` and the `Postgres` question
    * `pgvector`: when it is enough
    * `IVFFlat` and `HNSW` inside `Postgres`
    * the operational win of staying in `Postgres`
    * the scale ceiling: when to leave
    * `pg_embedding`, `Lantern`, and the alternatives
    * cross-reference to the `Postgres Internals` course
<!-- chapter: the-embedding-pipeline, duration: 1h -->
* The embedding pipeline
    * batch indexing vs streaming indexing
    * the embedding model as a dependency
    * versioning embeddings: the model-change re-index
    * the dual-pipeline anti-pattern
    * cross-reference to the `Feature Store Engineering` course on embedding features
    * idempotency and re-indexing safely
<!-- chapter: serving-at-scale, duration: 1h -->
* Serving at scale
    * the read-path latency budget
    * caching: query cache, vector cache, result cache
    * the multi-vector query and the batched search
    * the cold-shard problem
    * cost of the index at scale
<!-- chapter: operating-a-vector-database, duration: 2h -->
* Operating a vector database
    * monitoring recall in production via shadow ground truth
    * monitoring latency percentiles, not averages
    * monitoring index drift across the embedding-model lifecycle
    * the on-call story: the cluster is up but recall is wrong
    * the migration story when you replace the vector database
    * the "we re-embedded everything and it took two weeks" failure

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
