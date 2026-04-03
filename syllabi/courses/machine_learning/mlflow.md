---
tags:
  - tools:mlflow
  - data-and-ai:mlops
  - practices:experiment-tracking
  - concepts:model-registry
  - data-and-ai:machine-learning
level: intermediate
category: machine-learning
duration_hours: 16
audience:
  - audiences:developers
  - audiences:data-scientists
  - audiences:devops
---
<!-- course: mlflow -->
# `MLflow` for `ML` Lifecycle Management

## Description
`MLflow` is the leading open-source platform for managing the end-to-end `machine learning` lifecycle,
from experiment tracking and reproducibility through model versioning and deployment. This course
provides comprehensive, hands-on coverage of every major `MLflow` component, enabling teams to
bring discipline and reproducibility to their `ML` workflows. Participants will learn to instrument
training code with the `MLflow` Tracking `API`, register and version models in the `MLflow` Model
Registry, serve models via `REST` endpoints, and integrate `MLflow` with cloud platforms and
big-data tools. By the end of the course, participants will be equipped to establish production-grade
`ML` lifecycle management practices in their organisations.

## Duration
16 hours / 2 days

## Intended Audience
* `ML` engineers and data scientists who want to bring reproducibility and governance to their experiments.
* `MLOps` and `DevOps` engineers responsible for deploying and monitoring `machine learning` models.
* Data science teams seeking a unified platform for experiment management and model delivery.

## Prerequisites
* `Solid` `Python` programming skills.
* Practical experience training `machine learning` or `deep learning` models.
* Basic familiarity with `Docker` and `REST` APIs is beneficial.

## Required Knowledge
* `Python` Programming (or equivalent experience)
* `Machine Learning` fundamentals (or equivalent experience)

## Objectives
* Understand the `ML` lifecycle and where `MLflow` fits within the broader `MLOps` ecosystem.
* Instrument training code to log parameters, metrics, and artefacts with `MLflow` Tracking.
* Package `ML` projects for reproducibility using `MLflow` Projects.
* Register, version, and manage models through the `MLflow` Model Registry.
* Serve `MLflow` models as `REST` endpoints and batch inference pipelines.
* Deploy `MLflow` on cloud platforms including `AWS`, `Azure`, and `GCP`.
* Extend `MLflow` with custom model flavours and plugins.
* Integrate `MLflow` with `Apache Spark` and `Delta Lake` for large-scale workflows.

## Outline
<!-- chapter: introduction-to-mlflow-and-ml-lifecycle, duration: 1h -->
* Introduction to `MLflow` and the `ML` Lifecycle
    * Challenges of managing `ML` experiments without tooling
    * The four components of `MLflow`: Tracking, Projects, Models, Registry
    * `MLflow` architecture and deployment modes
    * Installing and configuring `MLflow` locally and with a remote tracking server
<!-- chapter: mlflow-tracking, duration: 3h -->
* `MLflow` Tracking
    * Runs, experiments, and the tracking `API`
    * Logging parameters, metrics, tags, and artefacts
    * Autologging with `scikit-learn`, `PyTorch`, `TensorFlow`, and `XGBoost`
    * Comparing runs with the `MLflow` UI
    * Querying runs programmatically with the `MlflowClient`
    * Organising large numbers of experiments at scale
<!-- chapter: projects-and-reproducibility, duration: 2h -->
* Projects and Reproducibility
    * The `MLproject` `file` format
    * Defining entry points and parameter schemas
    * `Conda` and `Docker` environments for reproducible runs
    * Running projects locally, remotely, and on `Kubernetes`
    * Chaining projects into multi-step pipelines
<!-- chapter: model-registry, duration: 2h -->
* Model Registry
    * Model registration and the model lifecycle: Staging, Production, Archived
    * Versioning models and tracking lineage to training runs
    * Webhooks and automated promotion workflows
    * Access control and governance in team environments
    * Searching and comparing registered model versions
<!-- chapter: model-serving-with-mlflow, duration: 2h -->
* Model Serving with `MLflow`
    * The `mlflow models serve` command and `REST API`
    * Batch scoring with `mlflow models predict`
    * Deploying to `AWS SageMaker`, `Azure ML`, and `Vertex AI`
    * Online vs. batch inference patterns
    * A/B testing and canary deployments with the model registry
<!-- chapter: mlflow-with-cloud-platforms, duration: 2h -->
* `MLflow` with Cloud Platforms
    * Managed `MLflow` on `Databricks`
    * Remote tracking servers on `AWS`, `Azure`, and `GCP`
    * Artefact storage with `S3`, `Azure Blob Storage`, and `GCS`
    * Authentication, secrets management, and network security
    * Scaling the tracking server for high-concurrency teams
<!-- chapter: custom-models-and-flavors, duration: 2h -->
* Custom Models and Flavors
    * The `MLflow` model format and `MLmodel` specification
    * Built-in flavours: `Python function`, `scikit-learn`, `PyTorch`, `TensorFlow`
    * Creating custom `Python` model classes
    * Packaging pre- and post-processing logic with a model
    * Adding custom flavours and plugins
<!-- chapter: integration-with-spark-and-delta-lake, duration: 1h -->
* Integration with `Spark` and `Delta Lake`
    * Logging `Spark` `ML` pipelines with `MLflow`
    * Feature engineering pipelines and `Delta Lake` versioning
    * Distributed hyperparameter tuning with `Hyperopt` and `MLflow`
    * Reading and writing artefacts from `Spark` workers
<!-- chapter: mlflow-in-production, duration: 1h -->
* `MLflow` in Production
    * `CI/CD` pipelines for model training and registration
    * Model monitoring and detecting drift with `MLflow` metrics
    * Cost and performance considerations for large deployments
    * Integrating `MLflow` with `Airflow`, `Prefect`, and `Kubeflow`
    * Organisational best practices for `ML` lifecycle governance

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
