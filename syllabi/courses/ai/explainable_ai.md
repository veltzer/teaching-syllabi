---
tags:
  - data-and-ai:xai
  - data-and-ai:explainability
  - data-and-ai:machine-learning
  - tools:shap
  - tools:lime
level: intermediate
category: ai
duration_hours: 16
audience:
  - audiences:data-scientists
  - audiences:developers
  - audiences:managers
---
<!-- course: explainable_ai -->
# Explainable `AI`

## Description
As `machine learning` models are deployed in high-stakes domains such as healthcare, finance, and
criminal justice, the need to explain and justify model decisions has become critical. This course
covers the theory and practice of `Explainable AI` (XAI), equipping participants with tools and
techniques to open the black box of modern `ML` models. Participants will gain hands-on experience
with leading explainability libraries including `SHAP` and `LIME`, and will learn how to apply
explainability techniques to both classical `ML` models and deep neural networks. The course also
addresses fairness, bias detection, and the growing regulatory landscape around `AI` transparency.

## Duration
16 hours / 2 days

## Intended Audience
* Data scientists and `ML` engineers who need to explain and audit model predictions.
* Managers and technical leads responsible for deploying `AI` in regulated or sensitive environments.
* Developers integrating `ML` models into products where user trust and transparency are required.

## Prerequisites
* `Solid` `Python` programming skills.
* Practical experience training and evaluating `machine learning` models.
* Familiarity with supervised learning concepts such as classification, regression, and tree-based models.

## Required Knowledge
* `Machine Learning` fundamentals (or equivalent experience)

## Objectives
* Understand why model explainability is essential in modern `AI` systems.
* Distinguish between global and local explanation methods.
* Apply model-agnostic methods including `SHAP` and `LIME` to any `ML` model.
* Interpret and visualize feature importance using multiple techniques.
* Apply `GradCAM` and saliency maps to explain `deep learning` model decisions.
* Detect and quantify bias and fairness issues in trained models.
* Understand regulatory requirements such as `GDPR` right-to-explanation and EU `AI` Act obligations.

## Outline
<!-- chapter: introduction-to-explainability, duration: 1h -->
* Introduction to Explainability
    * What is Explainable `AI` and why it matters
    * Interpretability vs. explainability vs. transparency
    * Taxonomy of explanation methods: global vs. local, intrinsic vs. post-hoc
    * Overview of the XAI landscape and major libraries
<!-- chapter: why-models-need-explaining, duration: 1h -->
* Why Models Need Explaining
    * Real-world failures caused by opaque models
    * Stakeholder needs: regulators, end-users, developers, auditors
    * The accuracy–interpretability trade-off
    * Trust, accountability, and the human-in-the-loop
<!-- chapter: model-agnostic-methods, duration: 2h -->
* Model-Agnostic Methods
    * Partial Dependence Plots (PDP) and Individual Conditional Expectation (ICE)
    * Accumulated Local Effects (ALE)
    * Permutation feature importance
    * Comparing model-agnostic approaches across different model types
<!-- chapter: shap-values-deep-dive, duration: 3h -->
* `SHAP` Values Deep Dive
    * Game-theoretic foundations: Shapley values
    * TreeSHAP for gradient boosted models
    * KernelSHAP for model-agnostic explanations
    * DeepSHAP for neural networks
    * Visualizing `SHAP`: summary plots, dependence plots, waterfall charts
    * Aggregating `SHAP` values for global model understanding
<!-- chapter: lime-and-local-explanations, duration: 2h -->
* `LIME` and Local Explanations
    * The `LIME` algorithm: perturbing the input space
    * Text and tabular data explanations with `LIME`
    * Image explanations using superpixels
    * Limitations and stability of `LIME` explanations
<!-- chapter: feature-importance-techniques, duration: 2h -->
* Feature Importance Techniques
    * Impurity-based importance in tree models
    * Permutation importance and its advantages
    * Recursive Feature Elimination (RFE)
    * SAGE and interaction effects
    * Comparing and validating feature importance methods
<!-- chapter: explainability-for-deep-learning, duration: 2h -->
* Explainability for `Deep Learning`
    * Gradient-based attribution methods: vanilla gradients and integrated gradients
    * `GradCAM` and `Grad-CAM++` for convolutional networks
    * Saliency maps and their interpretation
    * Attention visualization in transformer models
    * Limitations of `deep learning` explainability
<!-- chapter: fairness-and-bias-detection, duration: 2h -->
* Fairness and Bias Detection
    * Sources of bias: data, label, and algorithmic bias
    * Fairness metrics: demographic parity, equalized odds, calibration
    * Auditing models with `Fairlearn` and `Aequitas`
    * Mitigation strategies: pre-processing, in-processing, post-processing
    * Case studies in high-stakes domains
<!-- chapter: regulatory-considerations, duration: 1h -->
* Regulatory Considerations
    * `GDPR` Article 22 and right-to-explanation
    * EU `AI` Act requirements for high-risk systems
    * Model cards and datasheets for documentation
    * Building an explainability strategy for production systems

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
