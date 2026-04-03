---
tags:
  - data-and-ai:generative-ai
  - data-and-ai:diffusion-models
  - data-and-ai:deep-learning
  - tools:diffusers
  - concepts:stable-diffusion
level: advanced
category: machine-learning
duration_hours: 24
audience:
  - audiences:developers
  - audiences:data-scientists
---
<!-- course: diffusion_models -->
# Diffusion Models

## Description
Diffusion models have rapidly become the dominant paradigm in generative `AI`, powering breakthrough
systems such as `Stable Diffusion`, `DALL-E`, and `Sora`. This course provides a thorough treatment
of the mathematics, architectures, and practical engineering of diffusion models, from the original
`DDPM` formulation through score-based methods and latent diffusion to state-of-the-art
text-conditional image generation. Participants will develop a deep understanding of how these models
learn to reverse a noise process, and will gain hands-on experience implementing and fine-tuning
models using the `Hugging Face Diffusers` library. The course also covers emerging applications in
video and audio generation, and addresses the important ethical, safety, and intellectual property
considerations that practitioners must navigate `when` deploying generative systems.

## Duration
24 hours / 3 days

## Intended Audience
* `ML` engineers and data scientists who want to understand and work with state-of-the-art generative models.
* Researchers looking to build on diffusion model foundations for novel applications.
* Developers building products powered by image, video, or audio generation.

## Prerequisites
* Strong `Python` programming skills.
* `Solid` understanding of `deep learning` fundamentals including convolutional networks and transformers.
* Familiarity with `PyTorch` and experience training neural networks.
* Comfort with probability and statistics: Gaussian distributions, KL divergence, and Markov chains.

## Required Knowledge
* `Deep Learning` fundamentals (or equivalent experience)
* `PyTorch` (or equivalent experience)

## Objectives
* Understand the mathematical foundations of diffusion models and the forward/reverse process.
* Implement Denoising Diffusion Probabilistic Models (`DDPM`) from first principles.
* Understand score-based generative modelling and its connection to diffusion.
* Explain the latent diffusion architecture and its efficiency advantages.
* Describe the `Stable Diffusion` architecture and its key components.
* Generate images from text prompts and implement classifier-free guidance.
* Fine-tune diffusion models with `DreamBooth` and `LoRA` for custom subjects and styles.
* Use the `Hugging Face Diffusers` library for inference and training pipelines.
* Apply diffusion models to video and audio domains.
* Reason about the safety, ethical, and copyright implications of generative `AI` systems.

## Outline
<!-- chapter: introduction-to-generative-models, duration: 2h -->
* Introduction to Generative Models
    * The generative modelling landscape: VAEs, GANs, normalising flows, and diffusion
    * Likelihood-based vs. implicit generative models
    * What makes diffusion models special: quality, diversity, and controllability
    * Overview of landmark diffusion systems: `DDPM`, `DALL-E 2`, `Stable Diffusion`, `Imagen`
    * Setting up the development environment with `PyTorch` and `Diffusers`
<!-- chapter: denoising-diffusion-probabilistic-models, duration: 3h -->
* Denoising Diffusion Probabilistic Models
    * The forward diffusion process: gradually adding Gaussian noise
    * The variational lower bound and the ELBO objective
    * The reverse process: learning to denoise
    * The simplified training objective and noise prediction
    * U-Net architecture for the denoising network
    * `DDPM` vs. DDIM sampling and accelerated inference
<!-- chapter: score-based-generative-models, duration: 2h -->
* Score-Based Generative Models
    * Score functions and Stein's identity
    * Denoising score matching
    * Stochastic differential equations (SDEs) for continuous-time diffusion
    * The probability flow ODE and deterministic sampling
    * Unifying `DDPM` and score-based models under the SDE framework
<!-- chapter: latent-diffusion-models, duration: 3h -->
* Latent Diffusion Models
    * Motivation: diffusion in pixel space is computationally expensive
    * Variational autoencoders as compression backbones
    * Diffusion in the latent space of a pre-trained VAE
    * Cross-attention mechanisms for conditioning
    * The `LDM` training procedure and inference pipeline
    * Perceptual quality vs. computational cost trade-offs
<!-- chapter: stable-diffusion-architecture, duration: 2h -->
* `Stable Diffusion` Architecture
    * The three components: `VAE`, `U-Net`, and text encoder
    * `CLIP` text encoder and text-to-image alignment
    * The `U-Net` with time embeddings and cross-attention
    * Classifier-free guidance (CFG) and the guidance scale
    * Noise schedulers: DDIM, PNDM, and DPM-Solver
    * Inpainting and image-to-image variants
<!-- chapter: text-conditional-image-generation, duration: 2h -->
* Text-Conditional Image Generation
    * Prompt engineering for diffusion models
    * Negative prompts and their effect on sampling
    * ControlNet: conditioning on edges, depth, and pose
    * `IP`-Adapter and image prompt conditioning
    * Composing multiple conditions and concepts
<!-- chapter: fine-tuning-with-dreambooth-and-lora, duration: 3h -->
* Fine-Tuning with `DreamBooth` and `LoRA`
    * `When` and why to fine-tune a diffusion model
    * Textual Inversion: learning new concepts in embedding space
    * `DreamBooth`: few-shot fine-tuning for subject-driven generation
    * `LoRA` for parameter-efficient fine-tuning of diffusion models
    * Training setup, hyperparameter selection, and overfitting avoidance
    * Sharing and distributing fine-tuned models on `Hugging Face Hub`
<!-- chapter: video-and-audio-diffusion, duration: 2h -->
* Video and Audio Diffusion
    * Extending diffusion to the `temporal` domain
    * Video diffusion models: `VideoLDM` and `ModelScope`
    * `Sora` architecture overview and world-model capabilities
    * Audio generation with `AudioLDM` and `MusicGen`
    * Challenges: consistency, memory, and computational cost at scale
<!-- chapter: hugging-face-diffusers-library, duration: 3h -->
* `Hugging Face Diffusers` Library
    * The `DiffusionPipeline` abstraction and built-in pipelines
    * Schedulers, models, and the pipeline composition `API`
    * Running inference on `CPU` and `GPU` efficiently
    * Training with `Accelerate` and distributed setups
    * The `AutoPipeline` `API` and model hub integration
    * Building custom pipelines and extending `Diffusers`
<!-- chapter: safety-ethics-and-copyright, duration: 2h -->
* Safety, Ethics, and Copyright
    * Harmful content generation and safety filters
    * Watermarking and detecting `AI`-generated images
    * Training data transparency and copyright concerns
    * Model misuse: deepfakes, misinformation, and non-consensual imagery
    * Responsible deployment: content policies and governance frameworks

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
