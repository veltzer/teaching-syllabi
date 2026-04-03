---
tags:
  - concepts:feature-engineering
  - data-and-ai:machine-learning
  - tools:feast
  - tools:tecton
  - concepts:feature-store
level: intermediate
category: machine-learning
duration_hours: 24
audience:
  - audiences:data-scientists
  - audiences:developers
  - audiences:data-engineers
---
<!-- course: feature_engineering -->
# Feature Engineering for `Machine Learning`

## Description
The quality of features fed into a `machine learning` model is often more consequential than the
choice of algorithm, making feature engineering one of the most impactful skills a data practitioner
can develop. This course provides a systematic, hands-on treatment of the full feature engineering
workflow, from handling messy raw data through advanced transformation techniques for tabular, text,
and time-series data. Participants will learn principled methods for encoding categorical variables,
engineering time-aware features, generating text embeddings, and selecting the most informative
feature subsets. The course concludes with a practical introduction to feature stores using `Feast`
and `Tecton`, covering the operational challenges of building and monitoring production feature
pipelines.

## Duration
24 hours / 3 days

## Intended Audience
* Data scientists who want to move beyond default feature representations and build higher-quality `ML` models.
* `ML` engineers responsible for building reliable, reusable feature pipelines for production systems.
* Data engineers designing data platforms that serve features to downstream `ML` workloads.

## Prerequisites
* `Solid` `Python` programming skills.
* Working knowledge of `pandas` and `numpy`.
* Familiarity with supervised `machine learning` concepts such as cross-validation and model evaluation.
* Basic `SQL` skills are beneficial.

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `Machine Learning` fundamentals (or equivalent experience)

## Objectives
* Apply systematic strategies for diagnosing and handling missing data.
* Encode categorical variables using techniques matched to their cardinality and distribution.
* Apply numerical transformations including scaling, binning, and power transforms.
* Engineer informative features from time-series and datetime data.
* Generate and select text features and dense embeddings.
* Select the most informative features using filter, wrapper, and embedded methods.
* Understand the architecture and benefits of feature stores.
* Build and serve features with `Feast` and `Tecton`.
* Monitor feature distributions for drift in production pipelines.

## Outline
<!-- chapter: introduction-to-feature-engineering, duration: 2h -->
* Introduction to Feature Engineering
    * The role of features in `ML` model performance
    * The feature engineering workflow: discovery, transformation, validation
    * Structured vs. unstructured vs. time-series data
    * Common pitfalls: target leakage, train-test contamination
    * Tools overview: `pandas`, `scikit-learn` pipelines, `Feature-engine`
<!-- chapter: handling-missing-data, duration: 2h -->
* Handling Missing Data
    * Types of missingness: MCAR, MAR, MNAR
    * Univariate imputation: mean, median, mode, and constant fill
    * Multivariate imputation with `IterativeImputer` and `KNNImputer`
    * Missing indicator features
    * Evaluating the impact of imputation strategies on downstream models
<!-- chapter: encoding-categorical-variables, duration: 2h -->
* Encoding Categorical Variables
    * Ordinal encoding and label encoding
    * One-hot encoding and managing high cardinality
    * Target encoding, leave-one-out encoding, and smoothing
    * Frequency and count encoding
    * Hashing tricks for very high-cardinality features
    * Handling unseen categories at inference time
<!-- chapter: numerical-transformations, duration: 2h -->
* Numerical Transformations
    * Standard scaling, min-max normalisation, and robust scaling
    * Log, Box-Cox, and Yeo-Johnson power transforms
    * Discretisation: equal-width, equal-frequency, and decision-tree binning
    * Interaction features and polynomial features
    * Handling outliers: capping, flooring, and Winsorisation
<!-- chapter: time-series-features, duration: 3h -->
* Time-Series Features
    * Datetime decomposition: year, month, day-of-week, hour, and cyclical encoding
    * Lag features and window statistics: rolling mean, std, and percentiles
    * Expanding window and exponentially weighted features
    * Trend, seasonality, and residual decomposition
    * Calendar features: holidays, working days, and event flags
    * Feature engineering for demand forecasting and anomaly detection
<!-- chapter: text-features-and-embeddings, duration: 3h -->
* Text Features and Embeddings
    * Bag-of-words and TF-IDF representations
    * N-gram features and vocabulary management
    * Word embeddings: `Word2Vec`, `GloVe`, and `FastText`
    * Sentence and document embeddings with `sentence-transformers`
    * Fine-tuned embeddings from `BERT` and other transformer models
    * Dimensionality reduction for high-dimensional text features
<!-- chapter: feature-selection-methods, duration: 3h -->
* Feature Selection Methods
    * Filter methods: variance threshold, mutual information, and correlation analysis
    * Wrapper methods: recursive feature elimination and forward/backward selection
    * Embedded methods: Lasso regularisation and tree-based importance
    * Stability selection and permutation importance
    * The curse of dimensionality and `when` to apply selection
    * Evaluating feature selection with cross-validation
<!-- chapter: feature-stores-concepts, duration: 2h -->
* Feature Store Concepts
    * The feature store architecture: offline store, online store, and feature registry
    * Point-in-time correctness and avoiding training-serving skew
    * Feature sharing, discovery, and reuse across teams
    * Comparing feature store solutions: `Feast`, `Tecton`, `Hopsworks`, `Vertex AI Feature Store`
<!-- chapter: feast-feature-store, duration: 2h -->
* `Feast` Feature Store
    * Installing and configuring `Feast`
    * Defining feature views, entities, and data sources
    * Materialising features to the online store
    * Retrieving historical features for training datasets
    * Serving real-time features with the `Feast` online store
    * Integrating `Feast` with `Redis`, `BigQuery`, and `Snowflake`
<!-- chapter: production-feature-pipelines, duration: 2h -->
* Production Feature Pipelines
    * Orchestrating feature pipelines with `Airflow` and `Prefect`
    * Incremental vs. full materialisation strategies
    * Testing feature transformations: unit tests and integration tests
    * Versioning features and managing breaking changes
    * Backfilling historical features for model retraining
<!-- chapter: feature-monitoring-and-drift, duration: 1h -->
* Feature Monitoring and Drift
    * Statistical tests for distribution shift: KS test, PSI, and Jensen-Shannon divergence
    * Data quality checks with `Great Expectations`
    * Setting up feature drift alerting in production
    * Root-cause analysis `when` model performance degrades

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
