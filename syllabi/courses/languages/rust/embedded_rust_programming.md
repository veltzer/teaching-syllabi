---
tags:
  - languages:rust
  - hardware-and-embedded:embedded
  - hardware-and-embedded:bare-metal
  - languages:c
  - languages:c++
level: advanced
category: language
duration_hours: 8
audience:
  - audiences:developers
  - audiences:embedded-engineers
---
<!-- course: embedded_rust_programming -->
# Embedded `Rust` Programming

## Description
This course is intended for `Rust` developers who wish to delve deeper into `Rust` because they are using `Rust` in an embedded context. This course covers topics such as how to use `Rust` in a "bare-metal" or "no-os" context, how to embed `rust` code in a `C`/`C++` program/context and how to call `C`/`C++` code from a `Rust` context

## Duration
8 hours / 1 days

## Intended Audience
* `C` programmers who need to interface with `Rust` code
* `Rust` programmers who need to interface with `C` code
* Bare-metal or no-os developers

## Prerequisites
* Prior programming experience in `C` and `Rust` is required

## Objectives
* Learn how to write and use `#![no_std]` crates
* Learn how to call `C` libraries from `Rust` code
* Learn how to call `Rust` code from `C` code
* Learn some of the pitfalls `when` mixing and matching `C` and `Rust`

## Outline
<!-- chapter: calling-rust-from-c, duration: 1h -->
* Calling `Rust` from `C`
    * types
    * Concurrency
<!-- chapter: calling-c-from-rust, duration: 3h -->
* Calling `C` from `Rust`
    * bindgen
    * specifying which libraries to link with
    * `Makefile`/`cmake` integration
    * Preprocessor issues
    * Using opaque pointers
    * Const correctness
<!-- chapter: no-std, duration: 4h -->
* `#![no_std]`
    * What crates are not available?
    * What crates are available?
    * What do you have `when` using `#![no_std]`?
    * Accessing Memory Mapped registers from `Rust` code.
    * Memory barriers

## References
* [Embedded `Rust`](`https`://docs.`rust`-embedded.org/)
* [Embedded `Rust` Book](`https`://docs.`rust`-embedded.org/book/index.`html`)
* [`Rust` for `C` developers](`https`://opentitan.org/book/doc/rust_for_c_devs.`html`)
* [Using `C` libraries in `Rust`](`https`://medium.com/dwelo-`r`-d/using-`c`-libraries-in-`rust`-13961948c72a)

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
