---
tags:
  - infrastructure:gcp
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
<!-- course: gcp_ai_and_ml -->
# `GCP` `AI` and `Machine Learning`

## Description
This course provides a comprehensive exploration of `AI` and `machine learning` services on the `Google Cloud Platform`. Participants will learn to build, train, and deploy `machine learning` models using `Vertex AI`, leverage pre-trained APIs for vision, language, and speech tasks, and harness the power of generative `AI` with `Gemini` and `Model Garden`. The course covers the full `ML` lifecycle from data preparation through model serving, with emphasis on `MLOps` practices and responsible `AI`.

## Duration
24 hours / 3 days

## Intended Audience
* Developers looking to integrate `AI` and `ML` capabilities into cloud applications
* Data scientists seeking to leverage `GCP` managed `ML` services
* Engineers interested in deploying and managing `ML` models at scale

## Prerequisites
* Basic understanding of `GCP` core services
* Familiarity with `Python` programming
* Basic knowledge of `machine learning` concepts
* Experience with `SQL` and data manipulation

## Objectives
* Understand the `Google Cloud` `AI` and `ML` service landscape
* Build and train custom models using `Vertex AI`
* Use `AutoML` to create models without extensive `ML` expertise
* Leverage pre-trained APIs for natural language, vision, and speech tasks
* Build `ML` models directly in `BigQuery` using `BigQuery ML`
* Design and implement `ML` pipelines with `Vertex AI Pipelines`
* Apply generative `AI` capabilities using `Gemini API` and `Model Garden`
* Implement `MLOps` best practices for model deployment and monitoring
* Apply responsible `AI` principles to `ML` projects on `GCP`

## Outline
<!-- chapter: google-cloud-ai-platform-overview, duration: 1h -->
* `Google Cloud` `AI` Platform Overview
    * `AI` and `ML` services landscape on `GCP`
    * Choosing the right `AI`/`ML` service for your use case
    * `Google Cloud` `AI` principles and responsible `AI`
    * Setting up the `ML` development environment
<!-- chapter: vertex-ai-custom-training, duration: 2h -->
* `Vertex AI` Custom Training
    * `Vertex AI Workbench` for experimentation
    * Custom training jobs and containers
    * Distributed training strategies
    * Hyperparameter tuning
    * Managing training pipelines
<!-- chapter: vertex-ai-automl, duration: 1h -->
* `Vertex AI` `AutoML`
    * `AutoML` for tabular, image, text, and video data
    * Data preparation and labeling
    * Model evaluation and comparison
    * Exporting and deploying `AutoML` models
<!-- chapter: vertex-ai-model-registry-and-serving, duration: 1h -->
* `Vertex AI` Model Registry and Serving
    * Registering and versioning models
    * Online and batch prediction endpoints
    * Model monitoring and drift detection
    * A/B testing and traffic splitting
<!-- chapter: vertex-ai-feature-store, duration: 1h -->
* `Vertex AI` Feature Store
    * Feature engineering best practices
    * Creating and managing feature stores
    * Serving features for online and offline use
    * Feature sharing across teams
<!-- chapter: vertex-ai-pipelines, duration: 1h -->
* `Vertex AI Pipelines`
    * Building `ML` pipelines with `Kubeflow Pipelines`
    * Pipeline components and artifacts
    * Scheduling and automating pipelines
    * Pipeline versioning and reproducibility
<!-- chapter: bigquery-ml, duration: 1h -->
* `BigQuery ML`
    * Creating models with `SQL`
    * Supported model types (linear regression, classification, clustering, time series)
    * Model evaluation and prediction
    * Exporting models to `Vertex AI`
<!-- chapter: natural-language-api, duration: 1h -->
* Natural Language `API`
    * Sentiment analysis and entity recognition
    * Content classification
    * Syntax analysis
    * Custom entity extraction with `AutoML` Natural Language
<!-- chapter: vision-api, duration: 2h -->
* Vision `API`
    * Image labeling and classification
    * Object detection and localization
    * OCR and text detection
    * Face detection and landmark recognition
    * Custom models with `AutoML` Vision
<!-- chapter: speech-to-text-and-text-to-speech, duration: 1h -->
* Speech-to-Text and Text-to-Speech
    * Real-time and batch transcription
    * Language and model selection
    * Speaker diarization
    * `Text-to-Speech` voice synthesis and `SSML`
<!-- chapter: translation-api-and-document-ai, duration: 2h -->
* Translation `API` and `Document AI`
    * Neural Machine Translation
    * Glossary and custom models
    * `Document AI` for form parsing and extraction
    * Custom document processors
<!-- chapter: dialogflow, duration: 2h -->
* `Dialogflow`
    * Building conversational agents
    * Intents, entities, and contexts
    * `Dialogflow CX` for complex flows
    * Integration with messaging platforms
<!-- chapter: generative-ai-on-gcp, duration: 2h -->
* Generative `AI` on `GCP`
    * `Model Garden` overview and model selection
    * `Gemini API` for multimodal generation
    * `PaLM API` for text generation
    * Prompt design and engineering best practices
    * Grounding and retrieval-augmented generation
<!-- chapter: vertex-ai-search-and-conversation, duration: 2h -->
* `Vertex AI` Search and Conversation
    * Building enterprise search applications
    * Conversational `AI` with grounded responses
    * Data connectors and indexing
    * Customizing search and conversation behavior
<!-- chapter: prompt-design-and-tuning, duration: 2h -->
* Prompt Design and Tuning
    * Prompt engineering techniques
    * Few-shot and chain-of-thought prompting
    * Model tuning and adapter tuning
    * Evaluation of generative outputs
<!-- chapter: mlops-on-gcp, duration: 2h -->
* `MLOps` on `GCP`
    * End-to-end `ML` workflow automation
    * `CI/CD` for `ML` models
    * Model monitoring and retraining triggers
    * Logging and experiment tracking
    * Cost management for `AI`/`ML` workloads

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
