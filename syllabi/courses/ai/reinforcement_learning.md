---
tags:
  - data-and-ai:machine-learning
  - languages:python
level: advanced
category: ai
duration_hours: 32
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: reinforcement_learning -->
# Reinforcement Learning

## Description
This course provides a deep dive into reinforcement learning, from foundational concepts to modern
deep RL algorithms. Participants will learn the mathematical framework of Markov Decision Processes,
value-based methods, policy gradient methods, and actor-critic architectures. The course covers
practical implementation using `OpenAI Gymnasium` and `Stable Baselines3`, including DQN, PPO,
A2C, and model-based RL, with applications in robotics, games, and recommendation systems.

## Duration
32 hours / 4 days

## Intended Audience
* software developers building intelligent agents and decision systems
* data scientists exploring reinforcement learning techniques

## Prerequisites
* Strong proficiency in `Python` programming
* `Solid` understanding of `machine learning` fundamentals (supervised learning, neural networks)
* Knowledge of probability and statistics
* Familiarity with `PyTorch` or `TensorFlow`
* Basic calculus and linear algebra

## Required Knowledge
* `Python` Programming (or equivalent experience)

## Objectives
* **Formulate sequential decision problems** as Markov Decision Processes with states, actions, and rewards
* **Implement value-based methods** including dynamic programming, Monte Carlo, TD learning, and Q-learning
* **Build Deep Q-Networks** with experience replay, target networks, and advanced DQN variants
* **Apply policy gradient and actor-critic algorithms** including REINFORCE, A2C, A3C, and PPO
* **Train agents in simulated environments** using `OpenAI Gymnasium` and `Stable Baselines3`
* **Design RL solutions** for real-world applications in robotics, games, and recommendation systems

## Outline
<!-- chapter: rl-fundamentals, duration: 2h -->
* RL Fundamentals
    * Introduction to reinforcement learning
        * Agent-environment interaction
        * Rewards and returns
        * Episodes and trajectories
        * Exploration vs exploitation
    * Key components
        * States and observations
        * Actions (discrete and continuous)
        * Policies (deterministic and stochastic)
        * Value functions and action-value functions
    * Types of RL
        * Model-free vs model-based
        * On-policy vs off-policy
        * Value-based vs policy-based
        * Online vs offline RL
<!-- chapter: markov-decision-processes, duration: 2h -->
* Markov Decision Processes
    * MDP formulation
        * State transition probabilities
        * Reward function
        * Discount factor
        * Markov property
    * Bellman equations
        * Bellman expectation equation
        * Bellman optimality equation
        * State-value and action-value forms
    * Optimal policies
        * Policy ordering
        * Existence of optimal policies
        * Multiple optimal policies
<!-- chapter: dynamic-programming, duration: 2h -->
* Dynamic Programming
    * Policy evaluation
        * Iterative policy evaluation
        * Convergence properties
    * Policy improvement
        * Greedy policy improvement
        * Policy improvement theorem
    * Policy iteration
        * Full policy iteration algorithm
        * Convergence guarantees
    * Value iteration
        * Value iteration algorithm
        * Convergence and stopping criteria
    * Limitations of DP
        * Full model requirement
        * Computational complexity
        * Curse of dimensionality
<!-- chapter: monte-carlo-methods, duration: 2h -->
* Monte Carlo Methods
    * Monte Carlo prediction
        * First-visit and every-visit methods
        * Sample-based estimation
        * Convergence properties
    * Monte Carlo control
        * Exploring starts
        * Epsilon-greedy policies
        * On-policy and off-policy Monte Carlo
    * Importance sampling
        * Ordinary importance sampling
        * Weighted importance sampling
        * Variance reduction
<!-- chapter: temporal-difference-learning, duration: 2h -->
* `Temporal` Difference Learning
    * TD prediction
        * `TD(0)` algorithm
        * TD vs Monte Carlo vs DP
        * Bias-variance trade-off
        * `TD(lambda)` and eligibility traces
    * SARSA
        * On-policy TD control
        * Algorithm and convergence
        * Expected SARSA
    * Q-learning
        * Off-policy TD control
        * Q-learning algorithm
        * Convergence guarantees
        * Maximization bias and Double Q-learning
    * N-step methods
        * N-step TD prediction
        * N-step SARSA
        * N-step off-policy methods
<!-- chapter: function-approximation, duration: 2h -->
* Function Approximation
    * Need for approximation
        * Large and continuous state spaces
        * Generalization across states
        * Linear function approximation
    * Neural network approximation
        * Representing value functions with networks
        * Training with gradient descent
        * Stability challenges
    * Feature engineering for RL
        * State representation design
        * Tile coding
        * Radial basis functions
    * Convergence and stability
        * Deadly triad
        * Semi-gradient methods
        * Target networks
<!-- chapter: deep-q-networks, duration: 3h -->
* Deep Q-Networks
    * DQN architecture
        * Network design for Q-values
        * Experience replay
        * Target network
        * Training procedure
    * DQN improvements
        * Double DQN
        * Dueling DQN
        * Prioritized experience replay
        * Noisy networks
    * Rainbow DQN
        * Combining improvements
        * Multi-step learning
        * Distributional RL (C51)
    * Practical considerations
        * Hyperparameter tuning
        * Reward shaping
        * Frame stacking and preprocessing
        * Training stability
<!-- chapter: policy-gradient-methods, duration: 3h -->
* Policy Gradient Methods
    * Policy gradient theorem
        * Score function estimator
        * REINFORCE algorithm
        * Baseline subtraction
        * Variance reduction techniques
    * A2C (Advantage Actor-Critic)
        * Advantage function
        * Synchronous actor-critic
        * Architecture design
    * A3C (Asynchronous Advantage Actor-Critic)
        * Asynchronous training
        * Parallel workers
        * Shared parameters
    * PPO (Proximal Policy Optimization)
        * Clipped surrogate objective
        * PPO-Clip and PPO-Penalty
        * Generalized Advantage Estimation
        * Practical PPO implementation
    * TRPO (Trust Region Policy Optimization)
        * KL divergence constraint
        * Natural gradient
        * Conjugate gradient method
<!-- chapter: actor-critic-methods, duration: 2h -->
* Actor-Critic Methods
    * Actor-critic architecture
        * Separate actor and critic networks
        * Shared representation
        * Training dynamics
    * Continuous action spaces
        * Gaussian policies
        * DDPG (Deep Deterministic Policy Gradient)
        * TD3 (Twin Delayed DDPG)
    * SAC (Soft Actor-Critic)
        * Maximum entropy framework
        * Automatic temperature tuning
        * Continuous and discrete variants
    * Practical considerations
        * Network architecture choices
        * Replay buffer design
        * Exploration strategies
<!-- chapter: model-based-rl, duration: 2h -->
* Model-Based RL
    * World models
        * Learning environment dynamics
        * Planning with learned models
        * Dyna architecture
    * Model predictive control
        * Planning with MPC
        * Cross-entropy method
        * Model ensemble methods
    * Model-based policy optimization
        * MBPO (Model-Based Policy Optimization)
        * Dreamer and world model approaches
        * Sample efficiency comparison
    * Challenges
        * Model error and compounding
        * Exploration in model-based RL
        * `When` to use model-based methods
<!-- chapter: multi-agent-rl, duration: 2h -->
* Multi-Agent RL
    * Multi-agent settings
        * Cooperative environments
        * Competitive environments
        * Mixed cooperative-competitive
    * Multi-agent algorithms
        * Independent learners
        * Centralized training, decentralized execution
        * MAPPO and QMIX
    * Communication in multi-agent systems
        * Learned communication protocols
        * Emergent communication
    * Challenges
        * Non-stationarity
        * Credit assignment
        * Scalability
<!-- chapter: openai-gymnasium-environments, duration: 2h -->
* `OpenAI Gymnasium` Environments
    * Gymnasium fundamentals
        * Environment `API`
        * Observation and action spaces
        * Step and reset interface
        * Rendering and visualization
    * Built-in environments
        * Classic control environments
        * Atari environments
        * MuJoCo environments
        * Box2D environments
    * Custom environments
        * Creating custom environments
        * Environment wrappers
        * Observation and reward wrappers
    * Environment vectorization
        * Synchronous and asynchronous vectorized environments
        * Parallel data collection
<!-- chapter: stable-baselines3, duration: 3h -->
* `Stable Baselines3`
    * SB3 overview
        * Supported algorithms
        * Consistent `API` design
        * Integration with Gymnasium
    * Training agents
        * Algorithm selection and configuration
        * Callback system
        * Custom policies
        * Logging and monitoring
    * Evaluation and benchmarking
        * Evaluation utilities
        * Deterministic evaluation
        * Comparing algorithms
    * Advanced features
        * Custom feature extractors
        * Action and observation normalization
        * Saving and loading models
        * SB3-Contrib extensions
<!-- chapter: applications, duration: 3h -->
* Applications
    * Robotics
        * Sim-to-real transfer
        * Robot manipulation
        * Locomotion control
        * Safety constraints
    * Games
        * Board games
        * Video games
        * Real-time strategy
        * Self-play
    * Recommendation systems
        * Sequential recommendation
        * Exploration-exploitation in recommendations
        * Long-term user satisfaction
    * Other applications
        * Resource allocation
        * Traffic control
        * Portfolio optimization
        * NLP and dialogue systems

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
