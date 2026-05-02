---
tags:
  - concepts:databases
  - concepts:similarity-search
  - concepts:embeddings
  - concepts:performance
  - concepts:scalability
  - concepts:rag
level: intermediate
category: database
duration_hours: 40
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:ml-engineers
  - audiences:data-engineers
  - audiences:architects
---
<!-- course: vector_databases_engineering -->
# Vector Databases Engineering

## Description
The catalog has a `vector_databases` directory of tool-specific overviews. This course is the engineering
companion: how vector search actually works, how to engineer it for production, and how to operate it at
scale. It is the course you wish you had read before shipping your `RAG` prototype.

The course covers the mathematics and intuitions behind embeddings and similarity, the major index types
(`HNSW`, IVF, `IVF-PQ`, ScaNN, `DiskANN`), the engineering tradeoffs of recall vs latency vs cost vs
memory, the production stack (`pgvector`, Pinecone, `Weaviate`, `Qdrant`, `Milvus`, `Vespa`,
`Elasticsearch`/OpenSearch vector mode, `Redis`), hybrid search and reranking, multi-tenant vector workloads,
sharding and scaling, evaluation, and the cost story. Examples are drawn from production `RAG`, search,
recommendation, and deduplication systems. Participants leave able to design, ship, and operate a
production vector-search system.

## Duration
40 hours / 5 days

## Intended Audience
* developers and `ML` engineers shipping `RAG`, search, or recommendation systems
* data engineers integrating vector search into existing platforms
* architects choosing among vector-database options
* engineers operating an existing vector workload at scale

## Prerequisites
* working knowledge of `Python` or another mainstream language
* basic familiarity with embeddings and `LLM`/`ML` APIs
* exposure to at least one classical search system or relational database
* basic linear-algebra intuition is helpful

## Objectives
* describe the major `ANN` index families and their tradeoffs
* design a vector-search system with appropriate recall, latency and cost
* implement hybrid search and reranking correctly
* choose between vector databases and `pgvector`-style integrations
* operate a vector workload at scale with appropriate observability
* evaluate a vector-search system honestly
* avoid the most common production vector-search mistakes

## Outline
<!-- chapter: embeddings-and-similarity-fundamentals, duration: 3h -->
* Embeddings and similarity fundamentals
    * what an embedding actually represents
    * cosine, `dot` product, euclidean distance
    * normalization and when it matters
    * dense vs sparse representations
    * the curse of dimensionality
    * embedding-model choice and quality
<!-- chapter: brute-force-and-when-it-is-fine, duration: 2h -->
* Brute force and when it is fine
    * exact `kNN` complexity
    * the "10k vectors and a `numpy` `dot` product" baseline
    * `GPU` brute force at million-scale
    * the cases where you do not need an `ANN` index
<!-- chapter: ann-the-hnsw-family, duration: 3h -->
* `ANN`: the `HNSW` family
    * the `HNSW` graph structure
    * `M`, efConstruction, `efSearch`
    * recall vs latency tradeoff curve
    * memory cost
    * `nmslib`, `hnswlib`
    * `HNSW` with filters and the filter problem
<!-- chapter: ann-the-ivf-and-pq-family, duration: 3h -->
* `ANN`: the IVF and `PQ` family
    * inverted file (`IVF`) indexes
    * product quantization (`PQ`)
    * `IVF-PQ` and disk-friendly indexes
    * `OPQ` and friends
    * `Faiss`, `ScaNN`
    * recall, latency and memory tradeoffs
<!-- chapter: disk-based-and-large-scale-anns, duration: 2h -->
* Disk-based and large-scale `ANNs`
    * `DiskANN`, Vamana, `SPANN`
    * `SSD`-friendly indexes
    * the billion-scale design point
    * cold-start and warm-up
<!-- chapter: filtering-and-the-filter-problem, duration: 3h -->
* Filtering and the filter problem
    * pre-filter vs post-filter vs in-index filter
    * cardinality and selectivity tradeoffs
    * `HNSW` with metadata filters
    * `IVF` with metadata filters
    * the slow-filter and empty-filter failure modes
    * tenant-scoped filtering
<!-- chapter: hybrid-search, duration: 3h -->
* Hybrid search
    * dense plus `BM25` lexical search
    * `RRF` (reciprocal rank fusion)
    * weighted score fusion
    * sparse vectors (`SPLADE`, `BM25`-style)
    * the cases where hybrid clearly wins
    * implementing hybrid in `Elasticsearch`/OpenSearch, Vespa, `Weaviate`
<!-- chapter: reranking, duration: 2h -->
* Reranking
    * cross-encoder reranking
    * `Cohere Rerank`, `BGE Reranker`, `Voyage Rerank`
    * latency budget for rerank
    * the recall-then-precision pipeline
    * reranking with `LLM`-as-judge
<!-- chapter: pgvector-and-postgres-as-a-vector-store, duration: 3h -->
* `pgvector` and `Postgres` as a vector store
    * `pgvector` index types: IVFFlat, `HNSW`
    * combining vector with relational and `JSONB`
    * the "do not move data" argument
    * scaling `pgvector` and where it stops
    * `pgvecto.rs` and other extensions
    * cross-reference to the Database Internals course
<!-- chapter: dedicated-vector-databases, duration: 3h -->
* Dedicated vector databases
    * Pinecone, `Weaviate`, `Qdrant`, `Milvus`, `Vespa`
    * `Elasticsearch`/`OpenSearch` vector mode
    * `Redis` vector search
    * `Chroma` and embedded options
    * the build vs buy story
    * choosing a vector database from real requirements
<!-- chapter: indexing-pipelines, duration: 3h -->
* Indexing pipelines
    * embedding generation pipelines
    * incremental updates vs full rebuilds
    * deduplication
    * the freshness vs throughput tradeoff
    * `CDC` from a primary store into the vector index
    * cross-reference to the Streaming Data Systems course
<!-- chapter: multi-tenant-vector-workloads, duration: 2h -->
* Multi-tenant vector workloads
    * partition-per-tenant vs shared-index-with-filter
    * isolation guarantees
    * cardinality concerns at high tenant counts
    * cross-reference to the Multi-Tenant `SaaS` Architecture course
<!-- chapter: scaling-vector-search, duration: 3h -->
* Scaling vector search
    * sharding strategies
    * read replicas and the consistency model
    * `GPU` acceleration
    * cost per million queries
    * the "model upgrade re-embed" problem
    * data residency for vector workloads
<!-- chapter: evaluating-vector-search, duration: 3h -->
* Evaluating vector search
    * recall@k, `nDCG`, `MRR`
    * golden datasets for retrieval
    * the recall-vs-business-metric gap
    * cross-reference to the `LLM` Evaluation course
    * online eval and click feedback
<!-- chapter: rag-specific-engineering-and-wrap-up, duration: 2h -->
* `RAG`-specific engineering and wrap up
    * chunking strategies
    * the long-context-window argument and its limits
    * embedding-cache pattern
    * the "lost in the middle" effect
    * cross-reference to the `LLM` Application Engineering course
    * design walkthrough of a production vector-search system
    * recommended reading: `Faiss` papers, `HNSW` paper, vector-database engineering blogs

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
