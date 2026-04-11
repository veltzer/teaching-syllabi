---
tags:
  - data-and-ai:machine-learning
  - practices:devops
  - practices:automation
level: intermediate
category: ai
duration_hours: 32
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: mlops -->
# `MLOps`

## Description
This course provides a comprehensive guide to `MLOps`, the discipline of operationalizing machine
learning models in production environments. Participants will learn how to manage the full `ML`
lifecycle including experiment tracking, data versioning, model registry, serving, monitoring, and
governance. The course covers industry-standard tools such as `MLflow`, `Weights & Biases`, DVC,
`Kubeflow`, and model serving frameworks, with hands-on experience in building robust, automated,
and scalable `ML` pipelines.

## Duration
32 hours / 4 days

## Intended Audience
* software developers building `ML`-powered systems
* data scientists transitioning models from research to production

## Prerequisites
* Proficiency in `Python` programming
* Basic understanding of `machine learning` workflows (training, evaluation, deployment)
* Familiarity with `Docker` and containerization concepts
* Experience with version control (`Git`)
* Basic knowledge of `CI/CD` concepts

## Required Knowledge
* `Docker` Fundamentals (or equivalent experience)
* `Python` Programming (or equivalent experience)

## Objectives
* **Implement experiment tracking and reproducibility** using `MLflow` and `Weights & Biases` for model development workflows
* **Version datasets and manage features** using DVC and feature store patterns for consistent training and serving
* **Package and serve models** using TorchServe, `TensorFlow Serving`, and Triton with containerized deployments
* **Build automated `CI/CD` pipelines** for `ML` systems including testing, validation, and deployment stages
* **Monitor production models** for data drift, concept drift, and performance degradation with alerting and retraining strategies
* **Design scalable `ML` infrastructure** using `Kubernetes`, `Kubeflow`, and `GPU` management with cost optimization

## Outline
<!-- chapter: mlops-lifecycle, duration: 3h -->
* `MLOps` Lifecycle
    * What is `MLOps`
        * Definition and motivation
        * `DevOps` vs `MLOps`
        * `ML` system technical debt
        * Maturity levels of `MLOps`
    * `ML` lifecycle stages
        * Data collection and preparation
        * Model development and training
        * Model evaluation and validation
        * Deployment and serving
        * Monitoring and maintenance
    * `MLOps` principles
        * Reproducibility
        * Automation
        * Continuous integration and delivery
        * Monitoring and feedback
    * Team roles and responsibilities
        * Data engineers
        * `ML` engineers
        * `MLOps` engineers
        * Platform engineers
    * Tool landscape overview
        * Open-source vs commercial
        * End-to-end platforms vs best-of-breed
        * Cloud-native vs cloud-agnostic
<!-- chapter: experiment-tracking, duration: 3h -->
* Experiment Tracking
    * `MLflow`
        * Tracking server setup
        * Logging parameters, metrics, and artifacts
        * Experiment comparison
        * `MLflow` UI
        * `MLflow` Projects
    * `Weights & Biases`
        * Run tracking and visualization
        * Hyperparameter sweeps
        * Artifact management
        * Team collaboration features
        * Report generation
    * Experiment management best practices
        * Naming conventions
        * Tagging and organization
        * Baseline tracking
        * Experiment reproducibility
    * Hyperparameter optimization
        * Grid search and random search
        * Bayesian optimization
        * Early stopping strategies
        * Multi-objective optimization
<!-- chapter: data-versioning, duration: 3h -->
* Data Versioning
    * DVC (Data Version Control)
        * DVC initialization and configuration
        * Tracking data files and directories
        * Remote storage backends (`S3`, `GCS`, `Azure`)
        * DVC pipelines
        * Data and model registry
    * Data lineage and provenance
        * Tracking data transformations
        * Pipeline DAGs
        * Metadata management
        * Audit trails
    * Data validation
        * Schema validation
        * Statistical tests
        * Data quality checks
        * `Great Expectations` integration
    * Dataset management strategies
        * Training/validation/test consistency
        * Data versioning policies
        * Storage optimization
        * Access control
<!-- chapter: feature-stores, duration: 2h -->
* Feature Stores
    * Feature store concepts
        * Online vs offline stores
        * Feature engineering pipelines
        * Feature reuse and sharing
        * Point-in-time correctness
    * Feature store implementations
        * `Feast`
        * `Tecton`
        * Cloud-native feature stores
        * Custom feature store design
    * Feature management
        * Feature discovery and cataloging
        * Feature documentation
        * Feature monitoring
        * Feature deprecation
    * Training-serving consistency
        * Feature transformation parity
        * Skew detection
        * Real-time feature computation
        * Batch vs streaming features
<!-- chapter: model-registry, duration: 2h -->
* Model Registry
    * Model registry fundamentals
        * Model versioning
        * Model metadata
        * Stage transitions (staging, production, archived)
        * Approval workflows
    * `MLflow` Model Registry
        * Model registration
        * Version management
        * Stage transitions
        * Annotations and descriptions
    * Model packaging formats
        * `MLflow` model format
        * `ONNX`
        * TorchScript
        * SavedModel
    * Model governance
        * Model documentation
        * Model cards
        * Lineage tracking
        * Compliance requirements
<!-- chapter: model-packaging-and-serving, duration: 3h -->
* Model Packaging and Serving
    * TorchServe
        * Model archiving
        * Handler implementation
        * Configuration and management
        * Batch inference
    * `TensorFlow Serving`
        * SavedModel format
        * Serving configuration
        * `REST` and `gRPC` endpoints
        * Model versioning
    * Triton Inference Server
        * Multi-framework support
        * Model repository
        * Dynamic batching
        * Ensemble models
    * Serving patterns
        * Online prediction
        * Batch prediction
        * Streaming inference
        * Edge deployment
    * Optimization for serving
        * Model quantization
        * Graph optimization
        * `GPU` memory management
        * Latency optimization
<!-- chapter: containerization-for-ml, duration: 2h -->
* Containerization for `ML`
    * `Docker` for `ML` workloads
        * `ML`-specific Dockerfiles
        * `GPU` support (NVIDIA Container Toolkit)
        * Multi-stage builds
        * Image size optimization
    * Dependency management
        * `Python` environment reproducibility
        * CUDA and driver compatibility
        * Pinning library versions
        * `Conda` vs `pip` environments
    * Container registries
        * Image versioning
        * Vulnerability scanning
        * Registry management
        * Pull policies
    * Container orchestration basics
        * `Docker Compose` for `ML` stacks
        * Service networking
        * Volume management for data
        * Health checks
<!-- chapter: ci-cd-for-ml-pipelines, duration: 3h -->
* `CI/CD` for `ML` Pipelines
    * `ML`-specific `CI/CD` challenges
        * Data dependencies
        * Training time constraints
        * Model validation requirements
        * Environment complexity
    * Pipeline design
        * Data validation stage
        * Training stage
        * Model evaluation stage
        * Integration testing
        * Deployment stage
    * Testing strategies
        * Unit testing `ML` code
        * Data validation tests
        * Model performance tests
        * Integration tests
        * Smoke tests
    * Automation tools
        * `GitHub Actions` for `ML`
        * `GitLab CI` for `ML`
        * `Jenkins` pipelines
        * `Argo Workflows`
    * Deployment strategies
        * Blue-green deployment
        * Canary releases
        * Shadow deployment
        * Rollback procedures
<!-- chapter: model-monitoring, duration: 3h -->
* Model Monitoring
    * Data drift detection
        * Statistical drift tests
        * Feature distribution monitoring
        * PSI (Population Stability Index)
        * KS test and KL divergence
    * Concept drift detection
        * Performance-based detection
        * Window-based methods
        * Drift detection algorithms
        * Adaptive windowing
    * Performance degradation
        * Metric tracking over time
        * Threshold-based alerting
        * Comparative analysis
        * Root cause analysis
    * Monitoring tools and frameworks
        * Evidently
        * WhyLabs
        * `Prometheus` and `Grafana` for `ML`
        * Custom monitoring solutions
    * Retraining strategies
        * Trigger-based retraining
        * Scheduled retraining
        * Active learning
        * Incremental learning
<!-- chapter: a-b-testing-for-models, duration: 2h -->
* A/B Testing for Models
    * Experiment design
        * `Hypothesis` formulation
        * Sample size calculation
        * Traffic splitting strategies
        * Control and treatment groups
    * Implementation patterns
        * Feature flags for models
        * Traffic routing
        * Multi-armed bandit approaches
        * Interleaving experiments
    * Statistical analysis
        * Significance testing
        * Confidence intervals
        * Multiple comparison corrections
        * Bayesian analysis
    * Organizational practices
        * Experiment documentation
        * Result communication
        * Decision frameworks
        * Long-term tracking
<!-- chapter: infrastructure, duration: 2h -->
* Infrastructure
    * `GPU` management
        * `GPU` allocation and scheduling
        * Multi-`GPU` training
        * `GPU` monitoring
        * Spot/preemptible instances
    * `Kubernetes` for `ML`
        * K8s basics for `ML` workloads
        * `GPU` scheduling in K8s
        * Persistent volumes for data
        * Resource quotas and limits
    * `Kubeflow`
        * `Kubeflow` Pipelines
        * KFServing / KServe
        * Katib for hyperparameter tuning
        * Notebooks on `Kubeflow`
    * Cloud `ML` infrastructure
        * `AWS` (SageMaker, `EKS`)
        * `GCP` (`Vertex AI`, `GKE`)
        * `Azure` (`Azure ML`, AKS)
        * Multi-cloud strategies
<!-- chapter: cost-optimization, duration: 2h -->
* Cost Optimization
    * Training cost management
        * Spot instance strategies
        * Efficient resource utilization
        * Training time optimization
        * Mixed precision training
    * Serving cost management
        * Auto-scaling policies
        * Serverless inference
        * Model optimization for cost
        * Batch prediction scheduling
    * Storage cost management
        * Data lifecycle policies
        * Storage tier optimization
        * Artifact cleanup strategies
        * Compression techniques
    * Budgeting and planning
        * Cost estimation models
        * Chargeback and showback
        * ROI measurement
        * Build vs buy analysis
<!-- chapter: governance-and-compliance, duration: 2h -->
* Governance and Compliance
    * Model governance frameworks
        * Model risk management
        * Approval workflows
        * Audit trails
        * Documentation requirements
    * Regulatory compliance
        * `GDPR` considerations
        * Industry-specific regulations
        * Explainability requirements
        * Right to explanation
    * Security practices
        * Model access control
        * Data encryption
        * Secure model serving
        * Adversarial attack mitigation
    * Organizational policies
        * Responsible `AI` frameworks
        * Bias and fairness monitoring
        * Incident response procedures
        * Continuous compliance monitoring

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
