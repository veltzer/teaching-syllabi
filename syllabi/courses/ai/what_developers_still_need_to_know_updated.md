---
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:architects
  - audiences:team-leads
category: ai
duration_hours: 8
level: intermediate
tags:
  - data-and-ai:ai
  - data-and-ai:llm
  - data-and-ai:agents
  - concepts:best-practices
  - concepts:architecture
  - practices:development-workflow
  - practices:documentation
  - practices:testing
  - databases:choosing
---

<!-- course: what_developers_still_need_to_know_updated -->
# What Every Developer Needs to Know About Working with `AI` (Updated)

## Description

`AI` coding agents no longer complete the line you are typing. They read the
repository, run the build, query the database, write the code, write the tests
and open the pull request. The developer's job has moved accordingly: from
writing code to setting up the conditions under which a machine writes good
code, and to judging what comes back.

This one-day lecture is about those conditions. It is not a tour of products
and not a prompt-writing class. It covers the things that decide whether `AI`
makes a team faster or just makes it produce mistakes faster: what the machine
can actually see (the context window), what it is told (documentation), how it
knows it is done (tests), what it is not allowed to do (guardrails), how it
meets your data, and what kind of architecture it can work in without slowly
wrecking it.

The lecture is opinionated and practical. Every topic is presented as something
you can change in your own repository the next morning.

## Duration

8 hours / 1 day

## Intended Audience

* Developers who use `AI` assistants or agents daily and want predictable results from them.
* Senior developers who review and merge machine-written code and are accountable for it.
* Architects who need to know what `AI` changes in design decisions and what it does not.
* Team leads deciding how their repositories, pipelines and habits should adapt to `AI`.

## Prerequisites

* Real programming experience in at least one language.
* Some hands-on experience with an `AI` coding assistant or agent.
* Familiarity with version control, automated tests and a relational database.

## Objectives

* Understand the context window and manage it deliberately instead of fighting it.
* Write documentation that an `AI` reads, follows and keeps up to date.
* Use tests as the machine-checkable definition of done.
* Put guardrails in place that hold even when the `AI` ignores its instructions.
* Show data to an `AI` safely and cheaply, and use `AI` to create, clean and move data.
* Use `AI` to help choose and design databases without inheriting its biases.
* Make architectural decisions with `AI` and shape systems that `AI` can work in.

## Exercises

* Short guided demonstrations and discussions throughout the day; students who bring a laptop can follow along with their own `AI` agent on their own repository.

## Outline

<!-- chapter: what-changed-for-developers, duration: 1h -->
* What changed for developers
    * From autocomplete to agents: what the tools do today
    * The shift from writing code to specifying, steering and judging it
    * What the model is and is not
        * A colleague with tools and memory, not an autocomplete
        * Knowledge frozen at a training cutoff
        * Fluent, confident and sometimes wrong
    * The failure modes worth knowing by name
        * Hallucinated `APIs`, packages and facts
        * Plausible code that misses the edge cases
        * Solving a different problem than the one you had
        * Making the check pass instead of making the code right
    * Responsibility does not move: you own what you merge
    * The three levers you control: context, feedback and limits
<!-- chapter: how-to-work-with-ai, duration: 3h -->
* How to work with `AI`
    * The context window
        * The context window is everything the model knows about your project
        * What fills it: instructions, files, tool output, conversation history
        * Tokens, limits and cost
        * Memory between sessions
            * What the agent remembers: preferences, corrections, project facts
            * Where memory lives and how it is loaded back into the window
            * Reading, correcting and deleting what the agent remembers
            * Stale and wrong memories, and why memory is not shared with your team
        * Why quality drops as the window fills up
        * Compaction and summarization, and what gets lost
        * Managing context deliberately
            * One task per session
            * Pointing at files instead of pasting them
            * Sub-agents as a way to isolate context
            * Quiet builds and terse tool output
        * Recognizing a session that should be restarted rather than corrected
    * Documentation
        * Documentation is the memory the whole team shares, human and `AI`
        * Agent memory versus documentation: private and automatic versus reviewed and versioned
        * Instruction files in the repository and what belongs in them
            * How to build, test and run
            * Conventions the code does not make obvious
            * Things that must never be done
        * Writing the reason next to the rule
        * Keeping instruction files short, and why long ones get ignored
        * If it is not in the repository, it does not exist
        * Specifications, plans and decision records as files the `AI` can read
        * Plan first, code second: reviewing a plan is cheaper than reviewing a diff
        * Letting the `AI` write and maintain documentation
        * Stale documentation is now a bug: the `AI` believes what it reads
    * Tests
        * Tests as the definition of done that a machine can check by itself
        * The feedback loop: the `AI` must be able to run the tests alone
        * One command, fast, deterministic, loud on failure
        * Pinning down existing behavior before letting the `AI` change it
        * Letting the `AI` write tests without letting it grade its own homework
        * Warning signs
            * Tests that assert what the code does rather than what it should do
            * Tests weakened, skipped or deleted to get to green
            * Mocks that test the mock
        * Reviewing the tests more carefully than the code
        * Property-based and mutation testing as a check on the tests themselves
    * Guardrails
        * Instructions are requests; checks are rules
        * Deterministic checks: compilers, type checkers, linters, formatters
        * Strict by default: checks fail loudly and are never switched off to pass
        * The pipeline as the last gate that the `AI` cannot talk its way past
        * Limiting what the agent can do
            * Permissions and allow lists
            * Sandboxes and containers
            * Hooks that run before and after the agent acts
        * Secrets: what the `AI` must never see or write
        * Irreversible actions need a human: pushing, deleting, deploying, migrating
        * Prompt injection: untrusted text that the `AI` reads as instructions
        * Invented dependencies and the supply chain
        * Version control as the undo button: small commits, branches, worktrees
    * The working loop
        * Explore, plan, implement, verify
        * Small verifiable steps over giant leaps
        * Reading a diff you did not write
        * Running several agents in parallel and what it costs in review
        * Turning every repeated correction into documentation or a check
<!-- chapter: ai-and-data, duration: 2h -->
* `AI` and data
    * Showing data to the `AI`
        * Data does not fit in the context window, and should not try to
        * Show the shape, not the rows: schema, samples, statistics
        * Formats and what they cost in tokens
        * Let the `AI` write the query instead of reading the table
        * Natural language to `SQL`: where it works and where it quietly lies
        * Giving an agent database access
            * Read-only roles and replicas
            * Limits on rows, time and cost
            * Never production credentials
        * The schema as documentation: names, comments, constraints, a data dictionary
        * Privacy: personal data, masking, and what leaves your network
        * Documents and unstructured data: search, embeddings and retrieval in brief
    * Creating data with `AI`
        * Test data and fixtures on demand
        * Ask for a generator, not for rows
        * Realistic versus merely plausible: distributions, relations and edge cases
        * Reproducibility: seeds and generators kept in the repository
        * Extracting structured data from free text and documents
        * Validating every extraction against a schema
        * Cleaning, classifying and labeling at scale
        * Sampling and measuring quality instead of trusting it
        * Transformations and migrations written by `AI`
        * Reconciliation: counts, checksums and round trips
    * Choosing databases with `AI`
        * The `AI` as a research assistant, not as an oracle
        * Its biases: the popular, the old, and whatever you hinted at
        * Describing the workload first: access patterns, volume, consistency, growth
        * Asking for trade-offs and for the case against each option
        * Prototyping and benchmarking are now cheap, so do them
        * How well the `AI` knows a technology as a selection criterion
        * Why boring relational databases gained from `AI`
        * Schema design with `AI`: normalization, indexes, constraints
        * Reading query plans together with the `AI`
        * Vector search: a feature of your database or a product of its own
        * Schema changes as reviewed, versioned, reversible code
<!-- chapter: architecture-with-ai, duration: 2h -->
* Architecture with `AI`
    * What `AI` changes in architecture and what it does not
        * Code became cheap; wrong boundaries did not
        * Decisions that are hard to reverse stay human decisions
    * Designing with the `AI`
        * The `AI` as a sparring partner: alternatives, trade-offs, objections
        * Making it argue against your preferred design
        * Recording decisions and their reasons where the `AI` will find them
        * Diagrams and documentation generated from the code
    * Architecture that `AI` can work in
        * Modules small enough to fit in a context window
        * Explicit interfaces, types and contracts
        * Consistency over cleverness: one way to do each thing
        * Locality: a change should touch few files
        * Mainstream technology the model already knows well
        * Fast builds and fast tests as an architectural requirement
        * One repository or many, from the agent's point of view
    * Enforcing architecture mechanically
        * Dependency rules and layering checked by tools
        * Architecture tests and fitness functions
        * Why a described rule drifts and a checked rule holds
    * How the economics shift
        * Build versus buy when building is cheap
        * Fewer dependencies, more owned code
        * Disposable prototypes and cheap rewrites
        * Duplication versus abstraction, reconsidered
    * Architectural drift
        * Locally reasonable changes that add up to a mess
        * Duplicated logic and parallel implementations
        * Periodic audits, with the `AI` doing the reading
    * Legacy systems
        * Using `AI` to understand code nobody remembers
        * Tests first, then modernization in small steps
    * Putting a model inside the system
        * A component that is slow, costly and not deterministic
        * Evaluation instead of unit tests
        * Fallbacks, limits and observability
        * When ordinary code is the better choice
    * What to change in your repository tomorrow morning

## Installations

This is a lecture; no installation is required. Students who want to follow the demonstrations should have:

* A laptop with a working development environment for their primary language.
* An `AI` coding agent of their choice installed and working.
* Internet access with no corporate firewall blocking `AI` tools.
* A repository with a build and tests that they are allowed to experiment on.

## Copyright

Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
