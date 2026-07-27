---
tags:
  - languages:c++
  - languages:c++20
  - languages:c++23
  - data-and-ai:ai
  - data-and-ai:llm
  - data-and-ai:agents
  - data-and-ai:prompt-engineering
  - concepts:code-review
  - concepts:design-patterns
  - practices:productivity
  - practices:refactoring
  - practices:testing
  - practices:sanitizers
level: intermediate
category: language
duration_hours: 24
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:systems-programmers
  - audiences:team-leads
  - audiences:architects
---
<!-- course: cpp_in_the_age_of_ai -->
# `C++` in the Age of `AI`

## Description
`AI` coding assistants now write a large fraction of the `C++` that reaches production.
This changes what a `C++` developer's job actually is. It does not remove the need for
`C++` expertise, it relocates it: away from typing out loops and boilerplate, and towards
specifying, constraining, reviewing and verifying code that somebody else, in this case a
machine, produced.

`C++` is a uniquely dangerous language to hand to a generative model. It has manual object
lifetime, `undefined behavior` that compiles cleanly and runs "fine" until it does not, a
forty-year sediment of idioms spanning `C++` 98 to `C++` 23, and an enormous body of public
training data full of code that is obsolete, wrong, or merely old. A model asked for
"a `C++` class that holds a buffer" will happily produce something that would have been
respectable in 2003. It will compile. It may even pass your tests.

This course teaches `C++` as it is practiced when an `AI` writes most of the code. It covers
the division of labor question directly: which decisions you must keep for yourself, which
you can delegate, and how to tell the difference. It covers which subset of `C++` you should
instruct the `AI` to use, and why a narrower, more modern, more `RAII`-centric dialect makes
generated code dramatically safer to accept. It covers the `C++` knowledge that remains
non-negotiable, the knowledge you need precisely because you are reviewing rather than
writing: object lifetime, ownership, `undefined behavior`, the memory model, and the ABI.
Finally it covers the long-term problem that nobody notices in the first month of `AI`
adoption, which is that generated code accumulates into a codebase that is locally plausible
and globally incoherent, and what to do to prevent that.

The course is opinionated by design. It takes the position that `AI` makes `C++` productivity
enormous and `C++` correctness harder, and that closing the resulting gap is now a core
professional skill.

## Duration
24 hours / 3 days

## Intended Audience
* `C++` developers who already use `AI` assistants and are uneasy about how much they are accepting without understanding
* Senior developers and tech leads who must set team policy on `AI`-generated `C++`
* Systems programmers working where `undefined behavior`, lifetime bugs and ABI breaks are expensive
* Architects deciding which parts of a `C++` system may be `AI`-authored and which may not
* Reviewers who now spend more time reading `C++` than writing it

## Prerequisites
* This is not an introductory `C++` course and not an introductory `AI` course
* You must be a working `C++` developer, comfortable with classes, templates, the `STL`, inheritance and `virtual-functions`
* You must be comfortable with pointers, references, and `new-and-delete-operators`
* Exposure to at least `C++` 11 is required, familiarity with `C++` 17 or later is a strong advantage
* Some prior use of any `AI` coding assistant is expected, at the level of having asked it for code and used the answer

## Required Knowledge
* `C++` Basics (or equivalent experience)
* Modern `C++` for C Programmers (or equivalent experience)

## Objectives
* Decide deliberately which `C++` design decisions to retain and which to delegate to an `AI`
* Write specifications and constraints precise enough that generated `C++` is reviewable
* Define and enforce a `C++` subset for `AI` generation that eliminates whole classes of defects by construction
* Recognize the specific failure modes of `LLM`-generated `C++`, especially lifetime, ownership and `undefined behavior` errors
* Review generated `C++` faster and more reliably than by reading it line by line
* Use the compiler, `sanitizers` and static analysis as the primary verification layer for machine-written code
* Keep an `AI`-heavy `C++` codebase readable, consistent and architecturally coherent over time
* Retain and deepen the `C++` knowledge that reviewing demands, rather than letting it erode
* Establish team-level policy, tooling and review practice for `AI`-generated `C++`

## Exercises
Every chapter is paired with hands-on work at the keyboard with a live `AI` assistant.
The exercises are deliberately adversarial: students are repeatedly asked to accept
generated code, then to find what is wrong with it. Several exercises are built around
code that compiles without warnings and passes its tests while still being incorrect.

## Outline
<!-- chapter: what-actually-changed, duration: 2h -->
* What Actually Changed
    * The state of `AI` `C++` generation as of 2026
    * Why `C++` is the hardest mainstream language for a model to get right
        * Manual object lifetime with no runtime safety net
        * `undefined behavior` as a silent, compiling, testable-passing failure
        * Forty years of accumulated idiom in the training data
        * The `C++` 98 gravity problem: why models default to old code
        * Templates, overload resolution and errors that appear far from their cause
    * What models are genuinely good at in `C++`
        * Boilerplate, adapters, glue, serialization
        * `STL` algorithm selection and mechanical loop rewriting
        * Test scaffolding and fixtures
        * Mechanical migration across language versions
        * Explaining unfamiliar code
    * What models are genuinely bad at in `C++`
        * Ownership and lifetime across call boundaries
        * Concurrency and the memory model
        * Anything performance-critical without measurement
        * Architecture that spans more than the `context window`
    * The productivity/correctness gap and why it widens with codebase size
    * Reframing the job: from author to specifier, reviewer and verifier
<!-- chapter: the-division-of-labor, duration: 3h -->
* The Division of Labor: What You Decide, What the `AI` Decides
    * The core principle: delegate mechanism, retain intent
    * Decisions that must remain human
        * Ownership model: who owns what, and for how long
        * Public interfaces, `API` shape and `API` stability
        * The error model: exceptions, error codes, `std::expected`, and mixing them
        * Threading model and shared state boundaries
        * Data layout where it affects performance
        * ABI commitments and compatibility guarantees
        * Dependency choice and the cost of taking a library
        * Anything with a safety, security or regulatory consequence
    * Decisions safely delegated
        * Function bodies whose contract you have already fixed
        * Algorithm and container selection within a stated complexity budget
        * Boilerplate: getters, comparisons, serializers, adapters
        * Test cases against a specification you wrote
        * Mechanical refactoring with a defined end state
        * Documentation of code that already exists
    * The grey zone and how to resolve it
        * Class decomposition, template design, error propagation strategy
        * The heuristic: delegate what you could verify quickly, retain what you could not
    * Specifying before generating
        * Writing the contract first: preconditions, postconditions, ownership, lifetime
        * Header-first workflows: fix the interface, generate the implementation
        * Test-first workflows and why `TDD` fits `AI` generation unusually well
        * Stating the invariants the code must not break
    * Sizing the unit of work so that review stays possible
    * Recognising when you have delegated a decision by accident
<!-- chapter: constraining-the-ai-to-a-cpp-subset, duration: 3h -->
* Constraining the `AI` to a `C++` Subset
    * Why an unconstrained model writes the average of all `C++` ever written
    * Declaring the target: language version, standard library, compiler, platform
    * Features to mandate
        * `RAII` for every resource, without exception
        * `unique_ptr` and `shared_ptr` over raw owning pointers, and `unique_ptr` by default
        * The Rule of Zero, with the Rule of Five only where genuinely required
        * `std::string_view` and `std::span` for non-owning parameters
        * `const` correctness and `constexpr` where it is free
        * Strong types and enum class over bare primitives
        * `std::optional` and `std::expected` over sentinel values
        * `noexcept` where it is actually true
        * `STL` algorithms and ranges over hand-written loops
        * Structured bindings, `auto` used with judgement
        * Concepts to constrain templates and improve diagnostics
    * Features to forbid or fence off
        * Owning raw pointers, `new-and-delete-operators` in application code
        * Manual memory management outside a dedicated, reviewed layer
        * C-style casts and `reinterpret_cast`
        * C string functions and fixed-size buffers
        * Macros where a function, template or constant would do
        * Multiple inheritance of implementation, deep hierarchies
        * Template metaprogramming beyond what the team can maintain
        * `const_cast`, mutable state in supposedly const methods
        * Global mutable state and `Singleton` by reflex
    * Encoding the subset so it is actually applied
        * Project instruction files and system prompts for the assistant
        * Style guides written for a machine reader rather than a human one
        * Providing exemplar code as the pattern to imitate
        * Why showing one good file beats a page of prose rules
    * Mechanically enforcing the subset
        * Compiler flags as policy, warnings as errors
        * `clang-tidy` and static analysis rule sets that encode the subset
        * Formatting and naming enforced in `CI` rather than in review
    * Handling the legacy reality: subsets in a codebase that predates them
<!-- chapter: what-a-cpp-programmer-still-must-know, duration: 5h -->
* What a `C++` Programmer Still Must Know
    * Why reviewing demands deeper knowledge than writing
    * Object lifetime and ownership
        * Storage duration, scope, temporaries and their lifetime
        * Lifetime extension and its limits
        * Dangling references: the single most common generated-code defect
        * Reference and iterator invalidation across the containers
        * `std::string_view` and `std::span` dangling, and why models produce it
        * Ownership across `API` boundaries and across threads
    * `undefined behavior`
        * What `undefined behavior` actually licenses the compiler to do
        * The catalogue: out-of-bounds, use-after-free, signed overflow, strict aliasing,
            uninitialised reads, data races, invalid downcasts, misaligned access
        * Why `undefined behavior` survives testing and shows up in production
        * How optimization turns latent `undefined behavior` into visible misbehavior
    * The memory model and concurrency
        * Data races versus race conditions
        * Happens-before, atomics and memory ordering
        * Why generated concurrent `C++` deserves the most suspicion of all
        * Lock scope, deadlock ordering, and shared state that was never declared shared
    * Value semantics and copying
        * Copy versus move, and when the compiler elides
        * Accidental copies in generated code, especially in loops and lambdas
        * `lambda` capture by reference and the lifetime trap that follows
    * Templates and overload resolution
        * Enough to read generated template code and predict what it instantiates
        * Implicit conversions and the overload that was not the one you meant
        * Reading and surviving template error messages
    * Performance reasoning
        * Cache behavior, allocation cost, indirection cost
        * Why "the `AI` said it is efficient" is not a measurement
        * Reading generated assembly when it matters
    * The build and the ABI
        * Translation units, linkage, the One Definition Rule
        * ABI breaks that compile cleanly and fail at run time
        * Include hygiene and build-time cost of generated headers
    * Knowing the standard library well enough to spot the wrong tool
    * Skill erosion: what atrophies under `AI` use and how to counteract it deliberately
<!-- chapter: reviewing-generated-cpp, duration: 4h -->
* Reviewing Generated `C++`
    * Why line-by-line reading fails at generated-code volume
    * The catalogue of `LLM` `C++` failure modes
        * Confident, plausible, wrong: the characteristic shape of the error
        * Lifetime and dangling defects
        * Silent ownership transfer and double ownership
        * Off-by-one and boundary handling under refactoring
        * Missing error paths and swallowed failures
        * Exception safety abandoned halfway
        * `undefined behavior` introduced during "optimization"
        * Obsolete idioms drawn from old training data
        * Invented APIs and hallucinated library functions
        * Correct-looking concurrency that is not
        * Tests written to match the code rather than the specification
    * A review method for machine-written `C++`
        * Review the specification and the interface before the implementation
        * Ownership and lifetime pass first
        * Error path and failure mode pass second
        * Boundary and edge case pass third
        * Only then read the body for logic
    * Questions to ask of every generated function
        * Who owns this, who frees it, what is its lifetime
        * What happens when this fails, and who observes the failure
        * What is the state of the object if this throws
        * What does this do at zero, one, and maximum
        * What is shared, and with which thread
    * Interrogating the assistant as a review technique
        * Asking it to justify a lifetime or ownership choice
        * Asking it to enumerate failure modes of its own code
        * Asking for the counter-example that breaks it
        * Where its self-review is genuinely useful and where it merely agrees
    * Automation as the first reviewer
        * Warnings-as-errors as a non-negotiable gate
        * `sanitizers`: ASan, UBSan, TSan, MSan in `CI` and what each one catches
        * `Valgrind` where `sanitizers` cannot go
        * Static analysis, `clang-tidy`, and analysis in the assistant's own loop
        * `fuzzing` generated parsers and boundary-heavy code
        * `Godbolt` for checking what the compiler actually emitted
    * Testing machine-written code
        * Why the `AI` must not be the sole author of both code and its tests
        * Specification-derived tests versus implementation-derived tests
        * Property-based testing as a defence against plausible-but-wrong
        * Coverage as a weak signal and what to use instead
    * Calibrating scrutiny to risk: trust boundaries within one codebase
    * When to reject and regenerate rather than fix
<!-- chapter: keeping-ai-written-cpp-readable, duration: 4h -->
* Keeping `AI`-Written `C++` Readable
    * The real long-term risk: locally plausible, globally incoherent code
    * Why generated code drifts
        * Each generation is a fresh start with no memory of your conventions
        * The `context window` cannot hold your architecture
        * Statistically average code is the default output
        * Volume: more code is produced than any human reads carefully
    * The symptoms
        * Five spellings of the same idea in one codebase
        * Duplicated logic that no longer looks duplicated
        * Abstractions invented per-file rather than per-system
        * Comments restating the code instead of explaining the reason
        * Over-engineering: templates, layers and indirection nobody asked for
        * Inconsistent error handling across neighbouring modules
        * Silent growth: functions and files that no longer fit in one screen
    * Readability as an explicit, stated requirement
        * Asking for the simplest thing that satisfies the contract
        * Naming conventions supplied to the assistant, not hoped for
        * Enforcing a complexity budget: function length, nesting, parameter count
        * Demanding the boring solution as the default
    * Anchoring generation to your codebase
        * Exemplar-driven generation: this file is the pattern, follow it
        * Project instruction files as a durable, versioned convention record
        * Keeping architectural decisions written down where the assistant reads them
        * Regenerating against conventions rather than patching towards them
    * Comments and documentation in `AI`-written code
        * Comments that explain intent, invariants and the reason for the choice
        * Deleting comments that merely narrate the code
        * Documenting ownership and lifetime contracts explicitly in headers
        * Recording what was `AI`-generated and what was reviewed
    * Refactoring as a continuous, `AI`-assisted activity
        * Using the assistant to find duplication and inconsistency it created
        * Consolidating divergent implementations of the same idea
        * Periodic coherence review at module and system level
        * Deleting generated code aggressively: it is cheap to regenerate
    * Architecture as the human-owned artifact
        * Keeping the system model in a form the assistant can be handed
        * Module boundaries as the unit of `AI` work
        * Why a coherent architecture makes generation better, not merely safer
    * Readability metrics and review gates that catch drift early
<!-- chapter: workflow-tooling-and-team-practice, duration: 2h -->
* Workflow, Tooling and Team Practice
    * The `AI`-assisted `C++` workflow end to end
        * Specify, constrain, generate, verify, review, integrate
        * Tight loops: compile and test inside the generation cycle
        * Giving the assistant the compiler and the test suite as feedback
        * Working with the build system, `CMake`, and generated build files
    * Tools in practice
        * Inline completion versus chat versus agentic tools for `C++`
        * `GitHub Copilot`, Cursor, `Claude Code` and terminal agents on `C++` codebases
        * Feeding compiler diagnostics, `sanitizers` output and stack traces back to the model
        * Local models and why `C++` work is often the most confidentiality-sensitive
    * Context management for large `C++` codebases
        * Headers, translation units and what is worth putting in context
        * Compilation databases and semantic navigation
        * Templates and macros as context amplifiers
        * Choosing what the model must see and what it must not
    * Team policy
        * Where `AI` generation is permitted, restricted, or forbidden
        * Trust tiers by module: safety-critical, core, peripheral, test
        * Review requirements as a function of tier
        * Provenance: recording what was generated, by what, and who accepted it
        * Licensing and intellectual property of generated `C++`
        * Onboarding juniors without letting them skip the fundamentals
    * Measuring whether it is working
        * Defect rates, review time, `sanitizer` findings, code churn
        * The signals that indicate drift is accumulating
    * Where this is going and how to stay employable in it
<!-- chapter: capstone, duration: 1h -->
* Capstone
    * A specification is given, without an implementation
    * Students define the ownership model, interfaces and error model themselves
    * The implementation is generated under an enforced `C++` subset
    * The result is verified with warnings-as-errors, `sanitizers` and static analysis
    * Each student reviews another student's generated code and reports what they find
    * Group discussion of what was caught, what was missed, and what only the compiler found

## Installations
Each student should have:

* A `Linux` machine, real or virtual, `Ubuntu` 24.04 or later recommended.
* A recent `C++` compiler supporting `C++` 20 or later. `GCC` 13+ or `Clang` 17+.
* `CMake`, `Ninja` or `make`, and a debugger (`GDB` or `LLDB`).
* `clang-tidy`, `clang-format` and `Valgrind` installed.
* A `C++`-capable editor or `IDE`: `vscode` with `clangd`, `CLion`, or `Visual Studio`.
* A working `AI` coding assistant that the student can actually use during the course,
with an account and any corporate access approvals already in place. This is the single
most important prerequisite: a student without a working assistant cannot do the exercises.
* Free, wide band access to the internet from all machines, with no corporate firewall
blocking the `AI` assistant's endpoints. Students should verify this before the course
starts, as this is the most common cause of lost time on day one.
* Username and password of a user with `sudo` privileges on the machine.
* Students who prefer `Windows` or `MacOS` may use them, provided the compiler,
`sanitizers` and assistant all work. Note that `sanitizer` support is weakest on `Windows`
and several exercises depend on it.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
