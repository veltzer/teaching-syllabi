---
tags:
  - infrastructure:azure
  - infrastructure:cloud
  - concepts:ai
  - concepts:machine-learning
level: intermediate
category: cloud
duration_hours: 24
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: azure_ai_services -->
# `Azure` `AI` Services

## Description
This course provides a comprehensive overview of artificial intelligence and `machine learning` services on `Microsoft Azure`. Participants will learn to build intelligent applications using `Azure OpenAI Service`, `Azure Machine Learning`, `Azure Cognitive Services`, and `Azure AI Search`. The course covers practical implementation of generative `AI` patterns including `RAG` (Retrieval-Augmented Generation), prompt engineering, and responsible `AI` practices, equipping participants to integrate `AI` capabilities into production applications.

## Duration
24 hours / 3 days

## Intended Audience
* Developers building `AI`-powered applications on `Azure`
* Data scientists deploying models on `Azure` infrastructure

## Prerequisites
* Basic understanding of `Azure` services and the `Azure` portal
* Programming experience in `Python`
* Familiarity with basic `machine learning` concepts
* Understanding of `REST` APIs and `JSON`

## Objectives
* Build generative `AI` applications using `Azure OpenAI Service`
* Train and deploy `machine learning` models with `Azure Machine Learning`
* Integrate `Azure Cognitive Services` for vision, speech, and language capabilities
* Implement search solutions with `Azure AI Search`
* Apply responsible `AI` principles and tools
* Design `RAG`-based applications on `Azure`

## Outline
<!-- chapter: azure-ai-platform-overview, duration: 1h -->
* `Azure` `AI` Platform Overview
    * `AI` services landscape on `Azure`
    * Choosing the right `AI` service for your use case
    * `AI` service authentication and security
    * Regional availability and pricing models
<!-- chapter: azure-openai-service, duration: 3h -->
* `Azure OpenAI Service`
    * `GPT` models (capabilities, model selection, token management)
    * Embeddings (text embeddings, similarity search)
    * `DALL-E` (image generation and editing)
    * Chat completions `API` and system messages
    * Function calling and tool use
    * Fine-tuning `Azure OpenAI` models
    * Content filtering and safety features
    * Quota management and rate limiting
<!-- chapter: azure-ai-studio, duration: 2h -->
* `Azure AI Studio`
    * Studio workspace and project setup
    * Model catalog and model benchmarks
    * Prompt flow for orchestration
    * Evaluation and testing of `AI` applications
    * Deployment from `AI Studio`
<!-- chapter: azure-machine-learning, duration: 3h -->
* `Azure Machine Learning`
    * Workspaces, data stores, and datasets
    * Compute targets (compute instances, clusters, serverless)
    * Experiments and run tracking
    * `ML` pipelines (designer and `SDK`)
    * Automated `ML` (`AutoML`)
    * `MLflow` integration for experiment tracking
    * Model registry and versioning
    * Responsible `AI` dashboard
<!-- chapter: azure-cognitive-services, duration: 2h -->
* `Azure Cognitive Services`
    * `Vision` (image analysis, OCR, face detection, custom vision)
    * `Speech` (speech-to-text, text-to-speech, speech translation, speaker recognition)
    * `Language` (sentiment analysis, key phrase extraction, entity recognition, question answering)
    * `Decision` (content moderator, `Personalizer`)
    * Multi-service resource deployment
<!-- chapter: azure-ai-search, duration: 2h -->
* `Azure AI Search`
    * Index creation and schema design
    * Indexers and data sources
    * Skill sets and `AI` enrichment
    * Semantic ranking and vector search
    * Hybrid search strategies
    * Integration with `Azure OpenAI` for `RAG`
<!-- chapter: responsible-ai, duration: 2h -->
* Responsible `AI`
    * Microsoft Responsible `AI` principles
    * Fairness, transparency, and accountability
    * Content safety and filtering
    * Responsible `AI` tooling in `Azure Machine Learning`
    * Bias detection and mitigation
<!-- chapter: model-deployment-and-endpoints, duration: 2h -->
* Model Deployment and Endpoints
    * Real-time endpoints (managed online endpoints)
    * Batch endpoints for large-scale inference
    * Blue-green deployment strategies
    * Autoscaling and monitoring endpoints
    * Edge deployment with `ONNX` runtime
<!-- chapter: azure-bot-service, duration: 1h -->
* `Azure Bot Service`
    * Bot Framework `Composer`
    * Power Virtual Agents integration
    * Channel integration (Teams, web chat, Slack)
    * Conversational `AI` `design patterns`
<!-- chapter: azure-ai-document-intelligence, duration: 1h -->
* `Azure AI Document Intelligence`
    * Pre-built models (invoices, receipts, `ID` documents)
    * Custom models and training
    * Layout and document analysis
    * Integration with business workflows
<!-- chapter: prompt-engineering-best-practices, duration: 2h -->
* Prompt Engineering Best Practices
    * Prompt `design patterns` and techniques
    * System messages and persona crafting
    * Few-shot and chain-of-thought prompting
    * Handling hallucinations and grounding
    * Prompt evaluation and iteration
<!-- chapter: rag-patterns-with-azure, duration: 2h -->
* `RAG` Patterns with `Azure`
    * `RAG` architecture on `Azure`
    * Document chunking and embedding strategies
    * Vector stores and `Azure AI Search` integration
    * Orchestration with `Semantic Kernel` and `LangChain`
    * Evaluation of `RAG` quality
    * Scaling `RAG` applications
<!-- chapter: cost-management-for-ai-workloads, duration: 1h -->
* Cost Management for `AI` Workloads
    * Understanding `Azure OpenAI` pricing (tokens, models)
    * Optimizing `ML` compute costs
    * Provisioned throughput vs. pay-as-you-`go`
    * Monitoring and budgeting for `AI` services

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
