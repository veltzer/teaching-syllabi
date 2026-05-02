---
tags:
  - concepts:ai
  - concepts:machine-learning
  - concepts:performance
  - concepts:scalability
  - concepts:best-practices
level: advanced
category: ai
duration_hours: 32
audience:
  - audiences:ml-engineers
  - audiences:senior-developers
  - audiences:performance-engineers
  - audiences:devops
---
<!-- course: inference_optimization_and_serving -->
# Inference Optimization and Serving

## Description
The catalog has `MLOps`, `LLM Application Engineering`, `Multimodal AI Engineering`, and ```LLM``
Fine-tuning and Prompt Engineering`. None of those covers the production-engineering of inference: how
to serve a model with low latency, high throughput, and bounded cost. This is its own discipline. The
people who do it well do not just call a hosted `API` — they understand `KV-cache`, `paged-attention`,
batching, speculative decoding, quantization, the difference between `vLLM`, `TensorRT-LLM`, and
`SGLang`, and the operational reality of `GPU` fleets.

This four day course covers inference optimization and serving as practiced today. It covers the
inference compute pattern (the prefill and decode phases, the `KV-cache`, the per-request memory),
the serving stacks (`vLLM`, `TensorRT-LLM`, SGLang, LMDeploy, `Triton Inference Server`,
`Hugging Face TGI`, `Ollama` for local), the optimization techniques (continuous batching, paged
attention, prefix caching, speculative decoding, quantization in `AWQ`/GPTQ/`FP8`, tensor and
pipeline parallelism), the model selection and serving trade-offs, the autoscaling story, the cold
start problem, the multi-tenant serving question, the cost shape (`GPU`-hours, H100-vs-A100-vs-`L4`,
spot vs reserved), the alternatives (managed serving on `Bedrock`/Vertex/Together/Fireworks/`Groq`),
and the operational realities. Examples include real production deployments. Participants leave able
to serve a model with the right stack at the right cost.

## Duration
32 hours / 4 days

## Intended Audience
* `ML` engineers serving open models in production
* senior developers running inference workloads
* performance engineers optimizing `GPU` utilization
* `DevOps` engineers operating `GPU` fleets

## Prerequisites
* working knowledge of `Python` and at least one deep-learning framework
* exposure to the `MLOps` course
* basic familiarity with `LLMs` and transformers
* working `Linux` and container experience

## Objectives
* explain the inference compute pattern
* pick the right serving stack for the workload
* apply quantization and parallelism correctly
* operate `GPU` autoscaling and the cold-start mitigation
* compute the cost-per-million-tokens of a deployment
* compare self-hosted to managed-inference offerings
* recognize the patterns that lead to wasted `GPU`

## Outline
<!-- chapter: the-inference-compute-pattern, duration: 2h -->
* The inference compute pattern
    * prefill vs decode
    * the `KV-cache`
    * per-request memory
    * the latency budget
    * cross-reference to the `LLM Application Engineering` course
<!-- chapter: continuous-batching, duration: 2h -->
* Continuous batching
    * static batching and its limits
    * iteration-level batching
    * the throughput vs latency curve
    * `vLLM`'s implementation
    * the "we got 5x throughput from one config change" reality
<!-- chapter: paged-attention, duration: 2h -->
* Paged attention
    * the memory-fragmentation problem
    * the analogy to virtual memory
    * the `vLLM` paper
    * what it enables
    * the "we hit `OOM` with half the memory free" failure
<!-- chapter: prefix-caching, duration: 2h -->
* Prefix caching
    * the system prompt that is shared
    * the `RAG` context that is shared
    * cache keys and invalidation
    * the latency win
    * the cost win
<!-- chapter: quantization, duration: 3h -->
* Quantization
    * `FP16`, BF16, FP8, INT8, `INT4`
    * `AWQ` and `GPTQ`
    * weight-only vs activation quantization
    * the quality cost
    * the throughput gain
    * picking the level
<!-- chapter: speculative-decoding, duration: 2h -->
* Speculative decoding
    * the small-model-drafts, big-model-verifies idea
    * accept rate and the speedup
    * `Medusa`, `EAGLE`, target-model-only approaches
    * the "we lost speedup because the draft model was too small" failure
    * when speculative decoding wins
<!-- chapter: tensor-and-pipeline-parallelism, duration: 3h -->
* Tensor and pipeline parallelism
    * tensor parallelism for large models
    * pipeline parallelism for very large models
    * the bandwidth requirement (`NVLink`, `InfiniBand`)
    * `vLLM`'s `tensor_parallel_size`
    * the "we ran multi-`GPU` and saw no speedup" debugging
<!-- chapter: vllm-deep-dive, duration: 2h -->
* `vLLM` deep dive
    * `vLLM` architecture
    * configuration knobs that matter
    * the `OpenAI`-compatible server
    * deployment topology
    * the gotchas
<!-- chapter: tensorrt-llm-and-sglang, duration: 2h -->
* `TensorRT-LLM` and `SGLang`
    * `TensorRT-LLM` for `NVIDIA` deployments
    * `SGLang` and `RadixAttention`
    * `LMDeploy` overview
    * `Triton Inference Server` as the chassis
    * picking among them
<!-- chapter: hugging-face-tgi-and-ollama, duration: 1h -->
* `Hugging Face TGI` and `Ollama`
    * `TGI` overview
    * `Ollama` for local and small-model
    * the development-vs-production distinction
    * the "we ran `Ollama` in production" failure
<!-- chapter: autoscaling-and-cold-start, duration: 2h -->
* Autoscaling and cold start
    * the `GPU` cold-start cost
    * scale-to-zero and the trade-off
    * the warm-pool strategy
    * `Knative` and KServe for `GPU` autoscaling
    * the "we scaled to zero and the first request was 60 seconds" reality
<!-- chapter: multi-tenant-serving, duration: 2h -->
* Multi-tenant serving
    * one model per tenant vs shared model
    * `LoRA` adapters as a multi-tenant strategy
    * the per-tenant cost-allocation question
    * the "the noisy-tenant blew the latency budget" failure
    * cross-reference to the Multi-tenant `SaaS` Architecture course
<!-- chapter: gpu-fleet-operations, duration: 2h -->
* `GPU` fleet operations
    * spot vs on-demand vs reserved
    * `H100`, A100, L4, `MI300X` in practice
    * the `GPU`-utilization metric
    * `DCGM` and `nvidia-smi` exporters
    * the cost-per-million-tokens calculation
<!-- chapter: managed-inference-alternatives, duration: 2h -->
* Managed-inference alternatives
    * `Bedrock`, `Vertex AI`
    * `Together AI`, Fireworks, `Anyscale`
    * `Groq`, Cerebras, `SambaNova` for fast inference
    * the buy-vs-build decision
    * the cost crossover
<!-- chapter: putting-it-together, duration: 3h -->
* Putting it together
    * design walkthrough: serve a `70B` model at high throughput
    * design walkthrough: serve a `7B` model at low latency
    * design walkthrough: serve a multimodal model
    * the cost analysis for each
    * recommended reading: `vLLM` papers, `NVIDIA` inference docs

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
