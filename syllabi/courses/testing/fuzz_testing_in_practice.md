---
tags:
  - concepts:testing
  - concepts:security
  - concepts:test-quality
  - concepts:best-practices
level: advanced
category: testing
duration_hours: 24
audience:
  - audiences:senior-developers
  - audiences:security-engineers
  - audiences:qa-engineers
  - audiences:developers
---
<!-- course: fuzz_testing_in_practice -->
# Fuzz Testing in Practice

## Description
Fuzz testing is the practice of feeding programs malformed, random, or generated input to `find` bugs that
reviewers, unit tests, and even property-based tests miss. The catalog has a `Property Based Testing`
course; fuzzing is the related but distinct discipline that has graduated from a security tool into a
mainstream engineering practice. Modern fuzzers are coverage-guided, run continuously in `CI`, and
catch crashes, hangs, memory errors, and logic bugs in services that were considered well-tested.

This three day course covers fuzzing as practiced today. It covers the theory of coverage-guided
fuzzing (`AFL`, `libFuzzer`, `honggfuzz`), structure-aware fuzzing for protocols and parsers, fuzzing
language `runtimes` (`go-fuzz`, `cargo-fuzz`, native `Go` 1.18+ fuzzing, native `Rust` fuzzing,
`Atheris` for `Python`, `Jazzer` for `JVM`), continuous fuzzing in `CI` (`OSS-Fuzz`, `ClusterFuzz`,
`ClusterFuzzLite`), differential fuzzing, the corpus management problem, the deduplication problem, the
triage workflow, the harness as the most important code in the project, and the relationship between
fuzzing and security. Participants leave able to add a fuzz target to a project and keep it running.

## Duration
24 hours / 3 days

## Intended Audience
* senior developers writing parsers, protocols, or anything that takes external input
* security engineers integrating fuzzing into the `SDLC`
* `QA` engineers ready to graduate beyond example-based testing
* developers maintaining libraries that are fuzzed downstream

## Prerequisites
* working experience in at least one of `C/C++`, `Go`, `Rust`, `Python`, or `Java`
* exposure to the `Property Based Testing` course is helpful
* basic familiarity with `CI` pipelines

## Objectives
* explain coverage-guided fuzzing
* write a high-quality fuzz harness
* run fuzzing locally and continuously in `CI`
* manage corpora and seeds
* triage and deduplicate crashes
* recognize `when` fuzzing is the right tool and `when` it is not
* connect fuzzing to the security review

## Outline
<!-- chapter: what-fuzzing-actually-does, duration: 1h -->
* What fuzzing actually does
    * input generation, execution, observation
    * the difference from unit testing, property testing, and randomized testing
    * cross-reference to the Property Based Testing course
    * the bug classes fuzzing finds well
    * the bug classes fuzzing misses
<!-- chapter: coverage-guided-fuzzing, duration: 2h -->
* Coverage-guided fuzzing
    * the feedback loop
    * `AFL` and the genetic-algorithm idea
    * `libFuzzer` and in-process fuzzing
    * `honggfuzz` and the alternatives
    * sanitizers as the bug-detection mechanism
<!-- chapter: the-harness-as-the-most-important-code, duration: 2h -->
* The harness as the most important code
    * the harness contract
    * idempotence, statelessness, side-effect freedom
    * the "the harness has the bug" failure
    * harness for parsers
    * harness for stateful protocols
<!-- chapter: native-language-fuzzers, duration: 3h -->
* Native language fuzzers
    * `Go` 1.18+ native fuzzing
    * `cargo-fuzz` and `Rust`
    * `Atheris` and `Python`
    * `Jazzer` and the `JVM`
    * `libFuzzer` and `C/C++`
    * picking the fuzzer for the language
<!-- chapter: structure-aware-fuzzing, duration: 2h -->
* Structure-aware fuzzing
    * fuzzing valid-looking input
    * grammar-based fuzzing
    * `protobuf` fuzzing
    * the "fuzzer never hit the parser, only the input validator" failure
    * tools: `fuzz-protocol-buffers`, `Peach`
<!-- chapter: corpus-and-seed-management, duration: 2h -->
* Corpus and seed management
    * the seed corpus as the starting point
    * corpus minimization
    * the corpus as part of the repository
    * corpus pollution
    * the "corpus grew to a million files and `CI` died" failure
<!-- chapter: continuous-fuzzing-in-ci, duration: 3h -->
* Continuous fuzzing in `CI`
    * `OSS-Fuzz` and the open-source case
    * `ClusterFuzz` and `ClusterFuzzLite`
    * fuzzing time budget per run
    * the regression-fuzzing pattern
    * the "fuzzing only ran for 60 seconds" failure
<!-- chapter: triage-and-deduplication, duration: 2h -->
* Triage and deduplication
    * the crash signature
    * call-stack-based deduplication
    * the duplicate that is not actually a duplicate
    * the assigned-owner workflow
    * the "we have a thousand crashes and ignore them all" failure
<!-- chapter: differential-fuzzing, duration: 2h -->
* Differential fuzzing
    * two implementations, one input
    * finding spec ambiguities
    * `JSON` parser differentials
    * `crypto` library differentials
    * worked example
<!-- chapter: sanitizers-and-bug-detection, duration: 2h -->
* Sanitizers and bug detection
    * `ASAN`, `UBSAN`, `MSAN`, `TSAN`
    * the performance cost
    * the "fuzzer found nothing because no sanitizer was on" failure
    * detecting logic bugs without sanitizers
    * cross-reference to the `Linux` Debugging course
<!-- chapter: fuzzing-and-security, duration: 2h -->
* Fuzzing and security
    * fuzzing as a `SAST`/`DAST` complement
    * cross-reference to the `SAST`/`DAST` and Modern AppSec course
    * the responsible-disclosure path for fuzzing finds
    * the "we found a `CVE` in our dependency" workflow
<!-- chapter: when-fuzzing-is-not-the-answer, duration: 1h -->
* `When` fuzzing is not the answer
    * pure-business-logic code
    * code without a clear input
    * the case for property-based testing instead
    * the case for example-based testing instead
    * the cost of running a fuzzer the team will not look at

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
