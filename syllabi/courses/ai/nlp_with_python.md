---
tags:
  - data-and-ai:machine-learning
  - data-and-ai:nlp
  - languages:python
level: intermediate
category: ai
duration_hours: 32
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: nlp_with_python -->
# NLP with `Python`

## Description
This course provides a comprehensive guide to Natural Language Processing using `Python`. Participants
will progress from classical text processing techniques through modern transformer-based models,
covering tokenization, embeddings, text classification, named entity recognition, sequence models,
the attention mechanism, and the `Hugging Face` ecosystem. The course includes hands-on work with
`spaCy`, `NLTK`, and transformer models for tasks such as sentiment analysis, summarization, question
answering, and text generation.

## Duration
32 hours / 4 days

## Intended Audience
* software developers building text and language applications
* data scientists working with textual data

## Prerequisites
* Proficiency in `Python` programming
* Basic understanding of `machine learning` concepts (training, evaluation, loss functions)
* Familiarity with `NumPy` and `pandas`
* Basic linear algebra knowledge

## Objectives
* **Preprocess and represent text data** using tokenization, stemming, lemmatization, and vectorization techniques
* **Build text classification models** for sentiment analysis and document categorization using classical and `deep learning` methods
* **Implement named entity recognition and part-of-speech tagging** pipelines using `spaCy` and custom models
* **Understand and apply transformer architectures** including `BERT` and its variants for downstream NLP tasks
* **Leverage the `Hugging Face` ecosystem** for fine-tuning, inference, and model sharing
* **Deploy NLP models** for production text processing applications

## Outline
<!-- chapter: nlp-fundamentals, duration: 3h -->
* NLP Fundamentals
    * Text preprocessing
        * Tokenization (word, subword, character)
        * Sentence segmentation
        * Lowercasing and normalization
        * Removing stop words and punctuation
    * Stemming and lemmatization
        * Porter and Snowball stemmers
        * WordNet lemmatizer
        * Comparing stemming and lemmatization
    * Regular expressions for text
        * Pattern matching in text
        * Text extraction and cleaning
        * Common NLP regex patterns
    * Text data exploration
        * Word frequency analysis
        * N-gram analysis
        * `Zipf's` law
        * Corpus statistics
<!-- chapter: text-representation, duration: 3h -->
* Text Representation
    * Bag of words
        * Count vectorization
        * Vocabulary construction
        * Sparse matrix representation
    * TF-IDF
        * Term frequency computation
        * Inverse document frequency
        * TF-IDF vectorization
        * Applications and limitations
    * Word embeddings
        * `Word2Vec` (Skip-gram and CBOW)
        * `GloVe` (Global Vectors)
        * `FastText` (subword embeddings)
        * Training custom embeddings
    * Working with embeddings
        * Word similarity and analogy
        * Embedding visualization (t-SNE, PCA)
        * Pre-trained embedding models
        * Out-of-vocabulary handling
<!-- chapter: text-classification, duration: 3h -->
* Text Classification
    * Classical approaches
        * Naive Bayes classifier
        * Support Vector Machines for text
        * Logistic regression for text
        * Feature engineering for classification
    * Sentiment analysis
        * Binary and multi-class sentiment
        * Aspect-based sentiment analysis
        * Lexicon-based approaches
        * Domain adaptation
    * Spam detection
        * Feature extraction for spam
        * Model training and evaluation
        * Handling imbalanced datasets
    * Evaluation metrics
        * Accuracy, precision, recall, F1
        * Confusion matrix for text tasks
        * ROC curves
        * Cross-validation strategies
<!-- chapter: named-entity-recognition, duration: 2h -->
* Named Entity Recognition
    * NER fundamentals
        * Entity types and standards
        * IOB tagging scheme
        * Sequence labeling formulation
    * NER with `spaCy`
        * Pre-trained NER models
        * Custom entity recognition
        * Training NER pipelines
        * Rule-based matching
    * `Deep learning` for NER
        * BiLSTM-CRF architecture
        * Transformer-based NER
        * Fine-tuning for custom entities
    * Evaluation
        * Entity-level metrics
        * Partial matching evaluation
        * Error analysis
<!-- chapter: part-of-speech-tagging, duration: 2h -->
* Part-of-Speech Tagging
    * POS tagging concepts
        * Universal POS tag set
        * Fine-grained tag sets
        * Tagging as sequence labeling
    * POS taggers
        * `spaCy` POS tagger
        * `NLTK` taggers
        * Hidden Markov Models
    * Dependency parsing
        * Dependency relations
        * Parse tree visualization
        * Information extraction from parses
<!-- chapter: sequence-models, duration: 2h -->
* Sequence Models
    * Recurrent Neural Networks
        * `RNN` architecture
        * Vanishing gradient problem
        * Bidirectional RNNs
    * `LSTM` (Long Short-Term Memory)
        * `LSTM` cell architecture
        * Gates (input, forget, output)
        * Sequence-to-sequence with `LSTM`
    * GRU (Gated Recurrent Unit)
        * GRU cell architecture
        * GRU vs `LSTM` comparison
        * Practical considerations
    * Applications
        * Text classification with RNNs
        * Sequence labeling
        * Language modeling
<!-- chapter: attention-and-transformers, duration: 2h -->
* Attention and Transformers
    * Attention mechanism
        * Attention intuition
        * Scaled `dot`-product attention
        * Multi-head attention
        * Self-attention
    * Transformer architecture
        * Encoder and decoder blocks
        * Positional encoding
        * Feed-forward layers
        * Layer normalization
    * Pre-training objectives
        * Masked language modeling
        * Next sentence prediction
        * Causal language modeling
        * Denoising objectives
<!-- chapter: bert-and-transformer-models, duration: 2h -->
* `BERT` and Transformer Models
    * `BERT`
        * `BERT` architecture and pre-training
        * `BERT` tokenizer (WordPiece)
        * Fine-tuning `BERT` for downstream tasks
        * `BERT` variants (RoBERTa, ALBERT, DistilBERT)
    * Other transformer models
        * `GPT` family overview
        * T5 (Text-to-Text Transfer Transformer)
        * XLNet and ELECTRA
        * Multilingual models (mBERT, XLM-RoBERTa)
    * Practical fine-tuning
        * Task-specific heads
        * Learning rate strategies
        * Handling long documents
        * Few-shot and zero-shot approaches
<!-- chapter: hugging-face-ecosystem, duration: 3h -->
* `Hugging Face` Ecosystem
    * Transformers library
        * Model hub and model cards
        * Pipeline `API` for quick inference
        * AutoModel and AutoTokenizer
        * Loading and saving models
    * Datasets library
        * Loading and processing datasets
        * Dataset streaming
        * Custom dataset creation
    * Training with `Hugging Face`
        * Trainer `API`
        * Training arguments and configuration
        * Custom training loops
        * Distributed training
    * Model sharing
        * Publishing models to the hub
        * Model versioning
        * Community collaboration
<!-- chapter: text-generation, duration: 2h -->
* Text Generation
    * Language modeling
        * Autoregressive generation
        * Decoding strategies (greedy, beam search, sampling)
        * Temperature and top-k/top-p sampling
    * Controlled generation
        * Prompt engineering
        * Constrained decoding
        * Guided generation techniques
    * Evaluation of generated text
        * Perplexity
        * BLEU and ROUGE scores
        * Human evaluation
<!-- chapter: summarization, duration: 2h -->
* Summarization
    * Extractive summarization
        * Sentence scoring methods
        * Graph-based methods (TextRank)
        * Selecting representative sentences
    * Abstractive summarization
        * Sequence-to-sequence models
        * Transformer-based summarization
        * Fine-tuning for summarization
    * Evaluation
        * ROUGE metrics
        * BERTScore
        * Human evaluation criteria
<!-- chapter: question-answering, duration: 2h -->
* Question Answering
    * Extractive question answering
        * Span extraction models
        * SQuAD-style QA
        * Fine-tuning for QA
    * Retrieval-augmented approaches
        * Document retrieval
        * `RAG` overview
        * Dense passage retrieval
    * Open-domain question answering
        * Pipeline architecture
        * Knowledge-grounded answers
        * Evaluation metrics (EM, F1)
<!-- chapter: spacy-and-nltk, duration: 2h -->
* `spaCy` and `NLTK`
    * `spaCy`
        * Language models and pipelines
        * Tokenization and linguistic features
        * Custom pipeline components
        * Rule-based matching
    * `NLTK`
        * Corpus readers and resources
        * WordNet integration
        * Concordance and collocations
        * `NLTK` for education and prototyping
    * Choosing the right tool
        * `spaCy` vs `NLTK` strengths
        * Production vs research
        * Integration considerations
<!-- chapter: deployment-of-nlp-models, duration: 2h -->
* Deployment of NLP Models
    * Model optimization
        * Model distillation
        * Quantization
        * `ONNX` Runtime
        * Pruning
    * Serving infrastructure
        * `REST` `API` deployment (`FastAPI`, Flask)
        * Batch processing pipelines
        * `GPU` vs `CPU` inference
    * Production considerations
        * Latency optimization
        * Handling variable-length inputs
        * Model versioning and updates
        * Monitoring model performance

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
