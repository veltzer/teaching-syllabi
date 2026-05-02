---
tags:
  - concepts:ai
  - concepts:machine-learning
  - concepts:embeddings
  - concepts:best-practices
level: advanced
category: ai
duration_hours: 32
audience:
  - audiences:ml-engineers
  - audiences:senior-developers
  - audiences:architects
  - audiences:developers
---
<!-- course: multimodal_ai_engineering -->
# Multimodal `AI` Engineering

## Description
The catalog has `LLM Application Engineering`, `Computer Vision with Python`, `Natural Language
Processing`, and `Generative `AI` Applications` courses. None of those covers the production-engineering
of systems that combine modalities — vision plus text, audio plus text, document plus query, image plus
generation. Multimodal systems are now the dominant shape of frontier `AI` features, and they bring
their own engineering reality: token-cost shape per modality, latency, the embedding-alignment problem,
the prompt-injection-from-image attack, the chunking-of-non-text problem, and the evaluation gap when
ground truth is qualitative.

This four day course covers multimodal `AI` from the application engineer's perspective. It covers the
modality choice (when to send the image vs `OCR` it first, when to transcribe vs send audio directly),
the multimodal `LLM` APIs (Claude with images, `GPT-4V`/o/5, Gemini, `Pixtral`), the
embedding side (CLIP, `SigLIP`, multimodal embeddings for retrieval), the production patterns
(document understanding, video understanding, voice agents, generation pipelines), the cost shape per
modality, the latency budget, the multimodal observability story, the multimodal evaluation problem,
and the multimodal security model. Examples are drawn from real production systems for document
processing, voice support, and visual search. Participants leave able to ship a multimodal feature
that is debuggable, bounded, and operates within a known cost envelope.

## Duration
32 hours / 4 days

## Intended Audience
* `ML` engineers shipping multimodal features
* senior developers integrating vision or audio capabilities
* architects designing systems with non-text inputs
* developers asked to "`make` it work with the photo too"

## Prerequisites
* practical experience calling at least one `LLM` `API` from code
* exposure to the `LLM Application Engineering` course
* working knowledge of `Python`
* familiarity with `RAG` is helpful

## Objectives
* choose the right modality strategy for the problem
* call multimodal `LLM` `APIs` correctly across providers
* build retrieval over images, audio, and documents
* design the cost and latency budget per modality
* evaluate multimodal systems with the right methods
* recognize and mitigate multimodal-specific attacks
* operate a multimodal pipeline in production

## Outline
<!-- chapter: what-multimodal-actually-means, duration: 1h -->
* What multimodal actually means
    * input modality vs output modality
    * unified models vs pipelines
    * the spectrum from `OCR`-then-`LLM` to native vision `LLM`
    * cross-reference to the `LLM Application Engineering` course
    * the question this course answers
<!-- chapter: vision-plus-text-the-image-llm, duration: 3h -->
* Vision plus text: the image `LLM`
    * Claude vision
    * `GPT-4V`/`GPT-5` vision
    * Gemini vision
    * `Pixtral` and `Llama` vision
    * the image-encoding cost
    * the resolution-vs-cost knob
<!-- chapter: when-to-ocr-vs-when-to-vision, duration: 2h -->
* `When` to `OCR` vs when to vision
    * the `OCR`-first pipeline
    * the vision-first pipeline
    * the hybrid: `OCR` for text, vision for layout
    * the "the model hallucinated text in the image" failure
    * cost and latency comparison
<!-- chapter: document-understanding, duration: 3h -->
* Document understanding
    * `PDFs` are not text
    * the table-extraction problem
    * the form-extraction problem
    * `Layout-aware` models: LayoutLM, Donut, `Nougat`
    * the production pipeline
<!-- chapter: image-retrieval-and-embeddings, duration: 2h -->
* Image retrieval and embeddings
    * CLIP and `SigLIP`
    * cross-modal retrieval: text-to-image, image-to-image
    * cross-reference to the Vector Databases Engineering course
    * the alignment-quality question
    * the "we used the wrong embedding for the modality" failure
<!-- chapter: audio-plus-text-the-voice-pipeline, duration: 3h -->
* Audio plus text: the voice pipeline
    * `Whisper` and Gemini audio
    * `STT` then `LLM` then `TTS`
    * native-audio models like `GPT-realtime`
    * the latency budget for a voice agent
    * the "transcription was 95 percent and broke everything" reality
<!-- chapter: video-understanding, duration: 2h -->
* Video understanding
    * frame-sampling strategies
    * the Gemini long-video case
    * the "the question was on a frame we did not sample" failure
    * the cost shape of video
    * production patterns
<!-- chapter: generation-pipelines, duration: 2h -->
* Generation pipelines
    * text-to-image: `DALL-E`, `Stable Diffusion`, `Flux`
    * image-to-image and `ControlNet`
    * cross-reference to the Diffusion Models course
    * the prompt-engineering reality for images
    * the safety filter and the false-positive
<!-- chapter: cost-shape-per-modality, duration: 2h -->
* Cost shape per modality
    * the per-token, per-image, per-second-of-audio model
    * the resolution knob and the cost
    * the cache for repeated images
    * the "we sent the same image 10000 times" failure
    * cross-reference to the `LLM Application Engineering` cost chapter
<!-- chapter: latency-and-streaming, duration: 2h -->
* Latency and streaming
    * the time-to-first-token for vision
    * the audio-streaming `API`
    * the partial-frame strategy for video
    * the "the model needed the whole image first" reality
    * the user-perceived-latency design
<!-- chapter: multimodal-rag, duration: 3h -->
* Multimodal `RAG`
    * the document-with-images case
    * the figure-and-caption pairing
    * the multimodal index
    * cross-reference to the `RAG Deep Dive` course
    * the worked example
<!-- chapter: evaluation-of-multimodal-systems, duration: 2h -->
* Evaluation of multimodal systems
    * the ground-truth problem
    * vision-question-answering benchmarks
    * `LLM`-as-judge for visual outputs
    * cross-reference to the `LLM Evaluation and Benchmarking` course
    * the "the eval set did not include the failure mode" failure
<!-- chapter: multimodal-security, duration: 2h -->
* Multimodal security
    * prompt injection from image
    * prompt injection from audio
    * the "image contained text that overrode the system prompt" attack
    * cross-reference to the Working with `LLMs` Securely course
    * the input-sanitization story
<!-- chapter: production-and-operations, duration: 1h -->
* Production and operations
    * observability for non-text inputs
    * sampling and replay
    * the storage cost of input retention
    * the privacy story for images and audio
    * the regulatory story for `PII` in images
<!-- chapter: anti-patterns-and-wrap-up, duration: 2h -->
* Anti-patterns and wrap up
    * the modality-bolted-on architecture
    * the "we sent everything to the most expensive model" cost runaway
    * the silent regression on vision-model upgrade
    * the "we did not log the input image" debugging dead end
    * recommended reading: the `Flamingo`, `BLIP-2`, `LLaVA`, CLIP papers

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
