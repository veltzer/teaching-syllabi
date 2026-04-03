---
tags:
  - data-and-ai:federated-learning
  - data-and-ai:privacy
  - data-and-ai:machine-learning
  - concepts:differential-privacy
level: advanced
category: ai
duration_hours: 16
audience:
  - audiences:developers
  - audiences:data-scientists
  - audiences:architects
---
<!-- course: federated_learning -->
# Federated Learning

## Description
`Federated Learning` enables `machine learning` models to be trained across many decentralized devices
or data silos without transferring raw data to a central server, making it a foundational technology
for privacy-preserving `AI`. This course provides a thorough grounding in the theory, algorithms, and
engineering challenges of federated systems, from the `Federated Averaging` algorithm through
differential privacy and secure aggregation. Participants will gain hands-on experience with leading
frameworks including `TensorFlow Federated` and `PySyft`, and will study real-world deployment
scenarios in healthcare, mobile, and financial domains. The course also covers the current open
research challenges and practical limitations that practitioners encounter in production.

## Duration
16 hours / 2 days

## Intended Audience
* `ML` engineers and data scientists building privacy-preserving `machine learning` systems.
* Architects designing distributed `machine learning` infrastructure across multiple data owners.
* Developers working in regulated industries such as healthcare, finance, or telecommunications.

## Prerequisites
* Strong `Python` programming skills.
* `Solid` foundation in `machine learning` and neural network training.
* Familiarity with distributed systems concepts and basic networking.
* Understanding of basic probability and statistics.

## Required Knowledge
* `Deep Learning` fundamentals (or equivalent experience)

## Objectives
* Understand the motivations and threat models behind federated learning.
* Implement the `Federated Averaging` algorithm from first principles.
* Apply differential privacy techniques to protect individual training samples.
* Understand and apply secure aggregation protocols.
* Reduce communication overhead in federated training rounds.
* Build and run federated experiments using `TensorFlow Federated` and `PySyft`.
* Assess the practical challenges of deploying federated learning at scale.

## Outline
<!-- chapter: introduction-to-federated-learning, duration: 2h -->
* Introduction to Federated Learning
    * From centralized to federated `machine learning`
    * Cross-device vs. cross-silo federated learning
    * Key challenges: non-IID data, heterogeneous devices, partial participation
    * Federated learning in the wild: Google Gboard, Apple, healthcare consortia
    * Overview of the federated learning research landscape
<!-- chapter: privacy-threats-in-centralized-ml, duration: 1h -->
* Privacy Threats in Centralized `ML`
    * Membership inference attacks
    * Model inversion and attribute inference attacks
    * Data reconstruction from gradients
    * Why moving data to a central server is insufficient
<!-- chapter: federated-averaging-algorithm, duration: 2h -->
* Federated Averaging Algorithm
    * FedSGD and FedAvg: derivation and convergence properties
    * Communication rounds and local epochs
    * Handling non-IID and unbalanced data distributions
    * Variants: FedProx, SCAFFOLD, and FedNova
    * Convergence analysis and practical tuning
<!-- chapter: communication-efficiency, duration: 2h -->
* Communication Efficiency
    * Gradient compression: sparsification and quantization
    * Structured updates and sketched updates
    * Asynchronous federated learning
    * Bandwidth and latency constraints on edge devices
    * Measuring and optimizing communication costs
<!-- chapter: differential-privacy, duration: 2h -->
* Differential Privacy
    * Formal definition of epsilon-differential privacy
    * The Laplace and Gaussian mechanisms
    * DP-SGD: differentially private stochastic gradient descent
    * Privacy accounting: moments accountant and RDP
    * Privacy–utility trade-offs in practice
<!-- chapter: secure-aggregation, duration: 2h -->
* Secure Aggregation
    * Cryptographic primitives: secret sharing and homomorphic encryption
    * The SecAgg protocol for federated settings
    * Trusted execution environments (TEEs)
    * Combining secure aggregation with differential privacy
    * Performance overheads and practical limitations
<!-- chapter: federated-learning-frameworks, duration: 3h -->
* Federated Learning Frameworks
    * `TensorFlow Federated`: architecture and tff.learning `API`
    * Simulating federated experiments with `TFF`
    * `PySyft` and the OpenMined ecosystem
    * Flower framework for framework-agnostic federation
    * Comparing frameworks: feature sets, scalability, and maturity
<!-- chapter: real-world-deployment-challenges, duration: 2h -->
* Real-World Deployment Challenges
    * Client selection and incentive mechanisms
    * Handling device failures and stragglers
    * Model poisoning and Byzantine-robust aggregation
    * Federated evaluation and debugging without centralized data
    * Case studies: mobile keyboard prediction, medical imaging, financial fraud detection

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
