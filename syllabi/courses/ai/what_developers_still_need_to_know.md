---
tags:
  - data-and-ai:ai
  - concepts:programming
  - concepts:best-practices
  - concepts:test-quality
  - practices:productivity
level: intermediate
category: ai
duration_hours: 24
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:architects
  - audiences:team-leads
---
<!-- course: what_developers_still_need_to_know -->
# What Developers Using `AI` Still Need to Know About Programming

## Description
`AI` coding assistants can now write functions, whole modules, tests and even
architectures on demand. This has led many developers to believe that the
fundamentals no longer matter. The opposite is true. The moment the machine
produces code faster than you can read it, the bottleneck moves from *writing*
code to *judging* code, and judgment rests entirely on knowledge the `AI` cannot
supply for you.

This course is about that knowledge. It is not a course about how to prompt an
`AI`, nor about which assistant to buy. It is a course about the programming,
design, and engineering understanding you must still carry in your own head in
order to use an `AI` well: how to tell a good suggestion from a plausible-looking
bad one, how to reason about correctness, performance, concurrency and design
when the code was written by something that does not understand any of them, and
how to build a safety net of tests strong enough that you can let the `AI` run
wild without fear.

The course is opinionated. It argues that `AI` changes not only how we write code
but how we should organize the work around it — including retiring much of the
ceremony of Agile in favor of tight, test-anchored iteration.

## Duration
24 hours / 3 days

## Intended Audience
* Developers who use `AI` assistants daily and want to use them safely rather than blindly.
* Senior developers responsible for the quality of `AI`-generated code they review or merge.
* Architects who must make design decisions that an `AI` will implement but cannot make.
* Team leads deciding how to reshape their process now that most code is machine-drafted.

## Prerequisites
* Real programming experience in at least one language (`Python`, `Java`, `C#`, C/`C++`, Go, `JavaScript` or similar).
* Day-to-day experience using an `AI` coding assistant.
* Familiarity with version control, testing and debugging.

## Objectives
* Understand which parts of programming knowledge `AI` genuinely offloads and which it cannot.
* Evaluate `AI` suggestions critically for correctness, performance, security and design fit.
* Reason about algorithmic complexity, data structures, memory and concurrency well enough to catch machine mistakes.
* Design systems and make architectural trade-offs that an `AI` will implement but must not decide.
* Build test suites strong enough to let the `AI` refactor and rewrite aggressively without risk.
* Reshape the development process around `AI`, including moving away from ceremony-heavy Agile.

## Exercises
* Hands-on throughout, using the student's own `AI` assistant against real code, both reviewing machine output and building the tests and design constraints that keep it honest.

## Outline
<!-- chapter: what-changed-and-what-did-not, duration: 2h -->
* What `AI` changed and what it did not
    * The shift from writing code to judging code
    * What the `AI` actually is: a very good pattern completer, not an engineer
    * Why "it compiles and the tests pass" is not the same as "it is correct"
    * The confidence trap: fluent output that is subtly wrong
    * Where the responsibility still lands — on you
    * The skills that quietly became *more* valuable, not less
        * Reading code fast and critically
        * Knowing what correct looks like
        * Smelling a bad design before it spreads
<!-- chapter: evaluating-ai-suggestions, duration: 4h -->
* Evaluating `AI` suggestions
    * Reading generated code as a reviewer, not an author
    * The failure modes of `AI` code
        * Plausible but wrong algorithms
        * Silent edge-case omissions (empty input, off-by-one, overflow, `null`)
        * Hallucinated `APIs` and non-existent library functions
        * Outdated or deprecated patterns
        * Copied-in security holes
    * Asking the right question: "how would this break?"
    * Cross-checking the `AI` against itself and against documentation
    * When a suggestion is fine, when to fix it, and when to throw it away
    * Cost of accepting bad code now versus later
    * Keeping the `AI` on a short leash: small, verifiable steps over giant leaps
<!-- chapter: correctness-you-must-still-own, duration: 3h -->
* Correctness you must still own
    * Specifying the problem precisely enough that "correct" means something
    * Invariants, pre-conditions and post-conditions
    * Reasoning about edge cases the `AI` glossed over
    * Off-by-one, boundary and empty-collection thinking
    * Numeric pitfalls: integer overflow, floating point, precision
    * Why you must be able to trace a function by hand
    * Verifying the `AI`'s claims instead of trusting its explanations
<!-- chapter: data-structures-and-algorithms, duration: 3h -->
* Data structures and algorithms that `AI` will not choose for you
    * Why the `AI` reaches for the obvious structure, not the right one
    * Complexity that matters: recognizing accidental O(n²) and worse
    * Choosing the data structure from the access pattern, not the syntax
        * Arrays, lists, hash maps, trees, sets — when each wins
        * The cost of the wrong choice at scale
    * Memory: allocation, copying, locality, and why it is invisible to the `AI`
    * Spotting a plausible algorithm that is quietly quadratic
    * Benchmarking and measuring instead of guessing
<!-- chapter: concurrency-multi-core-and-multi-threading, duration: 4h -->
* Concurrency, multi-core and multi-`threading`
    * Why concurrency is where `AI` code is most dangerous
    * The problem the `AI` cannot see: shared mutable state
    * Race conditions, data races and why the tests pass anyway
    * Deadlocks, livelocks and lock ordering
    * Atomicity and why "just add a lock" is usually wrong
    * Memory models and visibility across cores
    * Threads versus processes versus async — choosing correctly
    * Immutability and message passing as ways to make correctness reviewable
    * Why a passing run proves nothing about a concurrent program
    * Reviewing `AI`-generated concurrent code with real suspicion
<!-- chapter: design-and-architecture-judgment, duration: 3h -->
* Design and architecture judgment
    * The decisions the `AI` will implement but must never make for you
    * Cohesion, coupling and why the `AI` does not feel them
    * Abstractions: the good, the leaky, and the premature
    * Naming, boundaries and module shape
    * When machine-generated code quietly rots the architecture
    * Design patterns as vocabulary, not as goals
    * Trade-offs: simplicity versus flexibility, now versus later
    * Keeping a system coherent when most of its code was drafted by a machine
    * Making design intent explicit so the `AI` stays inside it
<!-- chapter: tests-strong-enough-to-let-the-ai-run-wild, duration: 3h -->
* Tests strong enough to let the `AI` run wild
    * The core idea: tests are the leash that lets you let go
    * Why you can only trust `AI` refactoring as far as your tests reach
    * What a good test actually asserts (behaviour, not implementation)
    * Coverage that means something versus coverage that lies
    * Characterization tests to pin down code before you let the `AI` change it
    * Property-based testing to catch what example tests miss
    * Making the `AI` write tests without letting it grade its own homework
    * Fast, deterministic, isolated tests as the precondition for aggressive change
    * The workflow: lock behaviour with tests, then let the `AI` rewrite freely
<!-- chapter: debugging-and-understanding-what-you-shipped, duration: 1h -->
* Debugging and understanding what you shipped
    * You still have to fix it when it breaks at 3am
    * Reading a stack trace the `AI` has never seen
    * The scientific method of debugging when you did not write the code
    * Understanding machine-generated code well enough to own it
    * Avoiding the "I don't know why it works" codebase
<!-- chapter: rethinking-process-beyond-agile, duration: 1h -->
* Rethinking process — beyond Agile
    * Why Agile ceremony was a response to slow, expensive change
    * What changes when a working draft is minutes away, not sprints away
    * Retiring the rituals: standups, story points, estimation theatre
    * Tests and working software as the unit of progress, not tickets
    * Tight loops: specify, generate, verify, integrate
    * Keeping direction and design ownership while accelerating the mechanics
    * What to keep from Agile and what to let go
    * A working model for `AI`-era teams

## Installations
Each student should have:

* A working development environment for their primary language, on `Linux`, `Windows` or `MacOS`.
* Their `AI` coding assistant of choice installed and working (Copilot, Cursor, Claude, or similar).
* Free, wide-band internet access from all machines with no corporate firewall blocking `AI` tools or package installation.
* A test runner and version control set up and working.
* A real codebase they can experiment on is a strong advantage.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
