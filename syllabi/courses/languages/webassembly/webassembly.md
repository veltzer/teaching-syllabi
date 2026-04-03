---
tags:
  - languages:webassembly
  - concepts:programming
  - concepts:web-development
level: advanced
category: language
duration_hours: 16
audience:
  - audiences:developers
---
<!-- course: webassembly -->
# WebAssembly

## Description
WebAssembly (Wasm) is a portable binary instruction format that enables near-native
performance for web applications and beyond. This course provides an in-depth exploration
of WebAssembly, from its binary and text formats to compilation toolchains, `JavaScript`
interop, and emerging standards like WASI and the component model. Students will learn
to leverage Wasm for performance-critical applications on the web, server side, and edge.

## Duration
16 hours / 2 days

## Intended Audience
* Developers who want to use WebAssembly for performance-critical web applications.
* Systems programmers interested in Wasm as a portable compilation target.
* Backend developers exploring server-side and edge WebAssembly use cases.

## Prerequisites
* Strong programming skills in at least one language (`C`, `C++`, `Rust`, or `JavaScript`).
* Familiarity with web development basics (`HTML`, `JavaScript`).
* Understanding of compilation and linking concepts.

## Required Knowledge
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)
* `Rust` Programming (or equivalent experience)

## Objectives
* understand the core concepts and principles of WebAssembly
* gain practical knowledge of compiling to Wasm from multiple source languages
* gain practical knowledge of `JavaScript` and Wasm interoperability
* gain practical knowledge of WASI and server-side WebAssembly

## Outline
<!-- chapter: webassembly-concepts-and-motivation, duration: 1h -->
* WebAssembly Concepts and Motivation
    * Why WebAssembly exists
    * Performance vs `JavaScript`
    * Portability and sandboxing
    * The WebAssembly ecosystem
    * History and standardization
<!-- chapter: wasm-binary-format-and-text-format, duration: 1h -->
* Wasm Binary Format and Text Format
    * Binary format (.wasm) structure
    * Text format (WAT) syntax
    * Modules, functions, and types
    * Linear memory model
    * Tables and indirect calls
    * Converting between binary and text formats
<!-- chapter: compiling-to-wasm, duration: 1h -->
* Compiling to Wasm
    * `C`/`C++` with Emscripten
    * `Rust` with wasm-pack
    * AssemblyScript
    * Other source languages
    * Build configuration and optimization flags
    * Code size optimization techniques
<!-- chapter: javascript-interop, duration: 1h -->
* `JavaScript` Interop
    * Imports and exports
    * Memory sharing between `JavaScript` and Wasm
    * Tables and function references
    * Passing complex data types
    * The WebAssembly `JavaScript` `API`
    * Streaming compilation and instantiation
<!-- chapter: wasi-webassembly-system-interface, duration: 2h -->
* WASI (WebAssembly System Interface)
    * Motivation and design principles
    * Capability-based security model
    * `File` system access
    * Environment variables and arguments
    * Sockets and networking (preview)
    * Running WASI modules
<!-- chapter: component-model, duration: 1h -->
* Component Model
    * The component model proposal
    * Interface types
    * WIT (Wasm Interface Type) definitions
    * Composing components
    * Language-agnostic interoperability
<!-- chapter: threading, duration: 1h -->
* `Threading`
    * SharedArrayBuffer and atomics
    * Wasm threads proposal
    * Shared memory and synchronization
    * pthreads via Emscripten
    * Web Workers integration
<!-- chapter: simd, duration: 1h -->
* SIMD
    * Wasm SIMD instructions
    * Fixed-width 128-bit SIMD
    * Use cases for SIMD in Wasm
    * Compiler auto-vectorization
    * Relaxed SIMD proposal
<!-- chapter: garbage-collection-proposal, duration: 1h -->
* Garbage Collection Proposal
    * GC proposal overview
    * Struct and `array` types
    * Language support (managed languages targeting Wasm)
    * Status and adoption
<!-- chapter: use-cases, duration: 2h -->
* Use Cases
    * Performance-critical web applications
    * Image and video processing
    * Server-side Wasm (with WASI)
    * Edge computing and CDN workers
    * Plugin systems and extensibility
    * Game engines and multimedia
<!-- chapter: tooling, duration: 2h -->
* Tooling
    * wasm-tools suite
    * wasmtime runtime
    * Wasmer runtime
    * wasm-opt (Binaryen)
    * Browser developer tools for Wasm
    * wasm-bindgen for `Rust`
<!-- chapter: debugging, duration: 1h -->
* Debugging
    * Source maps for Wasm
    * DWARF debug info
    * Browser debugging support
    * Debugging WASI applications
    * Logging and tracing strategies
<!-- chapter: performance-profiling, duration: 1h -->
* Performance Profiling
    * Profiling Wasm in browsers
    * Benchmarking methodologies
    * Memory profiling
    * Identifying performance bottlenecks
    * Comparing Wasm vs native performance

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
