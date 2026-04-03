---
tags:
  - languages:c++
  - concepts:programming
  - concepts:optimization
level: advanced
category: language
duration_hours: 24
audience:
  - audiences:developers
  - audiences:embedded-engineers
  - audiences:performance-engineers
---
<!-- course: advanced_cpp -->
# Advanced `C++`

## Description
This course covers the most advanced features of modern `C++`, including `C++17` and `C++20` additions. Participants will gain deep understanding of move semantics, template metaprogramming, concepts, modules, coroutines, and ranges. The course emphasizes practical application of advanced idioms such as CRTP, type erasure, and the Pimpl pattern, enabling developers to write highly performant and expressive `C++` code.

## Duration
24 hours / 3 days

## Intended Audience
* Experienced `C++` developers seeking mastery of modern language features
* Embedded engineers working on performance-critical `C++` systems
* Performance engineers optimizing `C++` codebases

## Prerequisites
* Strong working knowledge of `C++11`/`C++14` features
* Experience with templates and the `STL`
* Familiarity with object-oriented and generic programming in `C++`

## Objectives
* Master move semantics and perfect forwarding for optimal resource management
* Write advanced template code using SFINAE, variadic templates, and fold expressions
* Leverage `C++20` concepts to constrain templates with clear intent
* Understand and use `C++20` modules and coroutines
* Apply the ranges library for composable data transformations
* Implement advanced design idioms including CRTP, type erasure, and Pimpl

## Outline
<!-- chapter: move-semantics-and-perfect-forwarding, duration: 2h -->
* Move Semantics and Perfect Forwarding
    * Rvalue references and value categories
    * Move constructors and move assignment operators
    * std::move and std::forward
    * Perfect forwarding in factory functions
    * Reference collapsing rules
    * Moved-from state guarantees
<!-- chapter: sfinae-and-template-metaprogramming, duration: 2h -->
* SFINAE and Template Metaprogramming
    * Substitution failure is not an error
    * std::enable_if and its patterns
    * decltype and declval
    * Type traits and `<type_traits>`
    * Tag dispatch vs SFINAE
    * `if constexpr` as a modern alternative
<!-- chapter: variadic-templates, duration: 2h -->
* Variadic Templates
    * Parameter packs and pack expansion
    * Recursive template instantiation
    * Fold expressions (`C++17`)
    * Variadic class templates
    * Applying variadic templates to tuple implementations
<!-- chapter: constexpr-and-consteval, duration: 2h -->
* `constexpr` and `consteval`
    * `constexpr` functions and variables
    * `constexpr if` for compile-time branching
    * `consteval` immediate functions (`C++20`)
    * constinit for static initialization (`C++20`)
    * Compile-time containers and algorithms
<!-- chapter: concepts-c-20, duration: 3h -->
* Concepts (`C++20`)
    * Defining and using concepts
    * requires clauses and requires expressions
    * Standard library concepts
    * Constraining auto and template parameters
    * Concept subsumption and overload resolution
    * Refactoring SFINAE to concepts
<!-- chapter: modules-c-20, duration: 2h -->
* Modules (`C++20`)
    * Module units and module partitions
    * Exporting declarations
    * Import declarations
    * Transitioning from headers to modules
    * Build system considerations
<!-- chapter: coroutines-c-20, duration: 2h -->
* Coroutines (`C++20`)
    * Coroutine fundamentals: co_await, co_yield, co_return
    * Promise types and coroutine handles
    * Lazy generators
    * Asynchronous task patterns
    * Coroutine allocator awareness
<!-- chapter: ranges-c-20, duration: 3h -->
* Ranges (`C++20`)
    * Range concepts and views
    * Range adaptors and pipelines
    * Lazy evaluation with views
    * Projections
    * Writing custom views
    * Composing algorithms with ranges
<!-- chapter: type-erasure, duration: 2h -->
* Type Erasure
    * The type erasure pattern
    * std::function internals
    * std::any and std::variant
    * Implementing custom type-erased wrappers
    * Performance implications of type erasure
<!-- chapter: crtp-curiously-recurring-template-pattern, duration: 2h -->
* CRTP (Curiously Recurring Template Pattern)
    * Static polymorphism with CRTP
    * Mixin classes
    * CRTP for interface enforcement
    * CRTP vs virtual dispatch performance
<!-- chapter: pimpl-idiom, duration: 2h -->
* Pimpl Idiom
    * Compilation `firewall` technique
    * `std::unique_ptr` with incomplete types
    * Move semantics and Pimpl
    * ABI stability considerations
    * Trade-offs and alternatives

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
