---
tags:
  - data-and-ai:nlp
  - data-and-ai:deep-learning
  - data-and-ai:machine-learning
  - languages:python
level: advanced
category: machine-learning
duration_hours: 24
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: nlp_with_transformers -->
# NLP with Transformers

## Description
This course provides an in-depth exploration of modern Natural Language Processing using
transformer-based architectures and the `Hugging Face` ecosystem. Participants will learn how
`BERT`, `GPT`, and related models work under the hood, and gain practical experience with
tokenization, fine-tuning pre-trained models, and applying them to real-world tasks such as
text classification, named entity recognition, summarization, and question answering. The
course also covers transfer learning strategies, model evaluation techniques, and deployment
using `ONNX` for production environments.

## Duration
24 hours / 3 days

## Intended Audience
* Data scientists building NLP pipelines with transformer models
* Developers integrating language understanding into applications

## Prerequisites
* `Solid` understanding of linear algebra and calculus fundamentals
* Experience with `machine learning` workflows (training, evaluation, hyperparameter tuning)

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `Deep Learning` Fundamentals (or equivalent experience)

## Objectives
* **Understand transformer architectures** including `BERT` and `GPT` and their internal mechanisms
* **Apply tokenization strategies** appropriate for different transformer models and NLP tasks
* **Fine-tune pre-trained models** from the `Hugging Face` model hub for downstream tasks
* **Build NLP pipelines** for text classification, named entity recognition, summarization, and question answering
* **Evaluate model performance** using appropriate metrics for each NLP task
* **Deploy transformer models** to production using `ONNX` and optimization techniques

## Outline
<!-- chapter: introduction-to-transformers, duration: 2h -->
* Introduction to Transformers
    * Evolution from RNNs to transformers
    * Self-attention mechanism
    * Multi-head attention
    * Positional encoding
    * Encoder and decoder architectures
    * Pre-training objectives (masked language modeling, causal language modeling)
<!-- chapter: tokenization, duration: 2h -->
* Tokenization
    * Word-level, character-level, and subword tokenization
    * WordPiece tokenization
    * Byte-Pair Encoding (BPE)
    * SentencePiece and Unigram models
    * Tokenizer configuration and vocabulary management
    * Handling special tokens and padding
<!-- chapter: bert-architecture, duration: 2h -->
* `BERT` Architecture
    * `BERT` pre-training and architecture
    * Masked language modeling and next sentence prediction
    * `BERT` variants (RoBERTa, ALBERT, DistilBERT, ELECTRA)
    * Input representation and embeddings
    * Contextual word representations
<!-- chapter: gpt-architecture, duration: 2h -->
* `GPT` Architecture
    * Autoregressive language modeling
    * `GPT`-2 and `GPT`-3 architecture overview
    * Causal attention masking
    * Text generation strategies (greedy, beam search, top-k, top-p sampling)
    * Prompt engineering fundamentals
<!-- chapter: hugging-face-ecosystem, duration: 2h -->
* `Hugging Face` Ecosystem
    * Transformers library overview
    * Model hub and model cards
    * AutoModel and AutoTokenizer classes
    * Pipeline `API` for rapid prototyping
    * Datasets library for data loading and preprocessing
    * Trainer `API` and training arguments
<!-- chapter: transfer-learning-for-nlp, duration: 2h -->
* Transfer Learning for NLP
    * Pre-training and fine-tuning paradigm
    * Feature extraction vs full fine-tuning
    * Domain adaptation strategies
    * Few-shot and zero-shot learning
    * Learning rate scheduling and warmup
    * Catastrophic forgetting and mitigation strategies
<!-- chapter: text-classification, duration: 2h -->
* Text Classification
    * Sequence classification with transformers
    * Single-label and multi-label classification
    * Sentiment analysis
    * Topic classification
    * Data preparation and label encoding
    * Handling class imbalance
<!-- chapter: named-entity-recognition, duration: 2h -->
* Named Entity Recognition
    * Token classification with transformers
    * IOB and BIO tagging schemes
    * Fine-tuning for custom entity types
    * Entity extraction pipelines
    * Handling subword tokenization alignment
    * Evaluation with entity-level metrics
<!-- chapter: text-summarization, duration: 2h -->
* Text Summarization
    * Extractive vs abstractive summarization
    * Encoder-decoder models for summarization
    * Fine-tuning BART and T5 for summarization
    * Controlling summary length and style
    * ROUGE metrics for evaluation
<!-- chapter: question-answering, duration: 2h -->
* Question Answering
    * Extractive question answering
    * Span extraction with transformer models
    * SQuAD-style fine-tuning
    * Handling unanswerable questions
    * Open-domain question answering overview
    * Retrieval-augmented generation (`RAG`) concepts
<!-- chapter: model-evaluation, duration: 2h -->
* Model Evaluation
    * Task-specific evaluation metrics
    * Precision, recall, F1 for classification and NER
    * ROUGE and BLEU for generation tasks
    * Exact match and F1 for question answering
    * Cross-validation strategies for NLP
    * Error analysis and model interpretability
<!-- chapter: deployment-with-onnx, duration: 2h -->
* Deployment with `ONNX`
    * Exporting transformer models to `ONNX` format
    * `ONNX` Runtime for inference optimization
    * Model quantization and pruning
    * Latency and throughput optimization
    * Serving models with `REST` APIs
    * Production monitoring and model versioning

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
