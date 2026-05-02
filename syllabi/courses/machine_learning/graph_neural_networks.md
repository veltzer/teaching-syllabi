---
tags:
  - data-and-ai:gnn
  - concepts:graph-learning
  - data-and-ai:deep-learning
  - tools:pytorch-geometric
  - tools:dgl
level: advanced
category: machine-learning
duration_hours: 24
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: graph_neural_networks -->
# Graph Neural Networks

## Description
Graph-structured data is ubiquitous in the real world, appearing in social networks, molecules,
knowledge bases, recommendation systems, and financial transaction networks. Graph Neural Networks
(GNNs) extend `deep learning` to this irregular data structure and have produced state-of-the-art
results across a wide range of domains. This course provides a rigorous treatment of the theory and
practice of GNNs, from the mathematical foundations of graph representation through modern
architectures including Graph Convolutional Networks, Graph Attention Networks, and Graph
Autoencoders. Participants will gain extensive hands-on experience implementing GNN models with
`PyTorch Geometric` and `DGL`, and will apply them to practical tasks such as node classification,
link prediction, graph classification, fraud detection, and recommendation.

## Duration
24 hours / 3 days

## Intended Audience
* `ML` engineers and data scientists who work with relational or graph-structured data.
* Researchers and practitioners building models for social networks, molecules, or knowledge graphs.
* Developers seeking to apply `deep learning` to domains where graph structure encodes important information.

## Prerequisites
* Strong `Python` programming skills.
* `Solid` understanding of `deep learning` fundamentals: feedforward networks, backpropagation, and optimisation.
* Familiarity with `PyTorch` and tensor operations.
* Basic linear algebra: matrix multiplication, eigenvalues, and graph Laplacians.

## Required Knowledge
* `Deep Learning` fundamentals (or equivalent experience)
* `PyTorch` (or equivalent experience)

## Objectives
* Represent real-world problems as graphs and reason about their properties.
* Understand the message-passing framework that underlies most GNN architectures.
* Implement and train Graph Convolutional Networks and Graph Attention Networks.
* Apply graph recurrent and autoencoder architectures to appropriate tasks.
* Build knowledge graph embeddings and perform link prediction.
* Use `PyTorch Geometric` and `DGL` to build scalable graph learning pipelines.
* Apply GNNs to real-world problems including fraud detection and recommendation.

## Outline
<!-- chapter: introduction-to-graphs-in-ml, duration: 2h -->
* Introduction to Graphs in `ML`
    * Graph-structured data: social networks, molecules, knowledge graphs, citation networks
    * Why standard `deep learning` fails on graphs
    * Key tasks: node classification, link prediction, graph classification, and graph generation
    * Overview of the GNN landscape and benchmark datasets
    * `NetworkX` for graph manipulation and visualisation
<!-- chapter: graph-representation-and-properties, duration: 2h -->
* Graph Representation and Properties
    * Adjacency matrices, edge lists, and sparse representations
    * Node, edge, and graph-level features
    * Directed, undirected, weighted, and heterogeneous graphs
    * Graph properties: degree distribution, clustering coefficient, and connectivity
    * The graph Laplacian and spectral properties
<!-- chapter: message-passing-framework, duration: 3h -->
* Message Passing Framework
    * The message-passing neural network (MPNN) formalism
    * Aggregation functions: sum, mean, max, and attention
    * Expressiveness of GNNs and the Weisfeiler-Leman test
    * Over-smoothing and over-squashing phenomena
    * Receptive fields and depth in graph networks
<!-- chapter: graph-convolutional-networks, duration: 3h -->
* Graph Convolutional Networks
    * Spectral graph convolution and ChebNet
    * The GCN simplification by Kipf and Welling
    * GraphSAGE: inductive learning with neighbourhood sampling
    * Graph ISOMORPHISM Network (GIN) and its expressiveness
    * Scalable training: mini-batching and neighbourhood sampling strategies
<!-- chapter: graph-attention-networks, duration: 2h -->
* Graph Attention Networks
    * Attention mechanisms in the graph domain
    * GAT: computing multi-head attention over node neighbours
    * GATv2 and improved attention expressiveness
    * `When` attention helps: heterophilic and noisy graph settings
    * Visualising and interpreting attention weights
<!-- chapter: graph-recurrent-networks, duration: 2h -->
* Graph Recurrent Networks
    * Combining GNNs with recurrent architectures for `temporal` graphs
    * Gated Graph Neural Networks (GGNN)
    * Spatio-`temporal` GNNs for traffic and sensor data
    * Dynamic graphs: evolving node and edge sets
<!-- chapter: graph-autoencoders, duration: 2h -->
* Graph Autoencoders
    * Variational Graph Autoencoder (VGAE)
    * Graph generation with deep generative models
    * Molecular graph generation with `JTVAE` and `GraphRNN`
    * Graph-level pooling: DiffPool and hierarchical pooling
    * Applications in drug discovery and material science
<!-- chapter: knowledge-graphs-and-link-prediction, duration: 2h -->
* Knowledge Graphs and Link Prediction
    * Knowledge graph structure: entities, relations, and triples
    * Embedding models: TransE, RotatE, and DistMult
    * R-GCN for multi-relational graphs
    * Link prediction tasks and evaluation metrics
    * Knowledge graph completion and question answering
<!-- chapter: pytorch-geometric-in-practice, duration: 3h -->
* `PyTorch Geometric` in Practice
    * The `PyG` data model: Data, HeteroData, and `DataLoader`
    * Built-in datasets and transforms
    * Implementing custom GNN layers with `MessagePassing`
    * Mini-batch training with `NeighborLoader` and `ClusterLoader`
    * Benchmarking and profiling GNN models
    * `DGL` as an alternative: `API` comparison and interoperability
<!-- chapter: gnn-applications, duration: 3h -->
* Graph Neural Networks for Fraud Detection and Recommendations
    * Fraud detection on transaction graphs: node and edge classification
    * Heterogeneous graphs in e-commerce and social platforms
    * Collaborative filtering with GNNs: PinSage and LightGCN
    * Cold-start and inductive recommendation with graph learning
    * Production deployment considerations for large-scale graphs

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
