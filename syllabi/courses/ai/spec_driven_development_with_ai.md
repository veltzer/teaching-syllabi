---
tags:
  - data-and-ai:ai
  - data-and-ai:generative-ai
  - data-and-ai:agents
  - concepts:code-generation
  - practices:methodology
  - practices:productivity
level: intermediate
category: ai
duration_hours: 8
audience:
  - audiences:developers
  - audiences:team-leads
  - audiences:architects
---
<!-- course: spec_driven_development_with_ai -->
# Spec-Driven Development with `AI`

## Description
Prompting a coding agent turn by turn works for small tasks and falls apart
for large ones: the agent forgets earlier decisions, the developer loses
track of what was agreed, and the resulting code matches nobody's intent.
Spec-Driven Development (`SDD`) is the emerging answer: invest in a written,
structured specification first, let the `AI` agent plan and implement
against it, and review the result against the spec rather than against a
vague memory of what you wanted.

This course teaches `SDD` as a practical working method. Participants learn
what makes a specification good enough for an `LLM` to implement from, how
to run the specify-plan-implement loop, how to keep spec and code from
drifting apart, and how to do all of this with today's tooling — `Spec Kit`,
`Kiro` and plain instruction files driving agents such as `Claude Code`,
`GitHub Copilot` and Cursor. The methodology is tool-agnostic; the exercises
use real tools on a real codebase.

The course assumes participants already develop with `AI` assistance day to
day. It does not re-teach prompt engineering or how coding agents work.

## Duration
8 hours / 1 day

## Intended Audience
* Developers who use `AI` coding agents and hit the ceiling of prompt-by-prompt development
* Team leads who want a repeatable, reviewable process around `AI`-generated code
* Architects who want design intent to survive contact with an autonomous coding agent

## Prerequisites
* Practical experience developing with an `AI` coding assistant or agent
* The Development Using `AI` course or equivalent experience
* Proficiency in at least one programming language
* Working knowledge of `git` and pull request workflows

## Required Knowledge
* Development Using `AI` (or equivalent experience)

## Objectives
* **Explain** what Spec-Driven Development is, what problems it solves and how it relates to `TDD`, `BDD` and `DDD`
* **Write** specifications — requirements, technical plans and task breakdowns — that an `AI` agent can implement from reliably
* **Run** the full specify-plan-implement-verify loop with a real coding agent on a real codebase
* **Operate** the current `SDD` toolchain: `Spec Kit`, `Kiro`-style workflows and hand-rolled spec files for any agent
* **Keep** specifications and code in sync over time and integrate specs into team review workflows
* **Judge** when `SDD` pays off and when it is ceremony

## Outline
<!-- chapter: from-vibe-coding-to-specs, duration: 1h -->
* From Vibe Coding to Specs
    * How prompt-by-prompt development fails at scale
        * Decisions made in chat and lost forever
        * The agent that forgets what you agreed on
        * Code that matches the last prompt, not the goal
    * The core idea of `SDD`
        * The specification as the source of truth
        * Iterating on the spec instead of re-prompting
        * Reviewing code against a written contract
    * `SDD` and its relatives
        * `TDD`: tests as spec vs prose as spec
        * `BDD` and Gherkin: precision the agent can use
        * `DDD`: where domain language enters the spec
        * Waterfall fears: why `SDD` is not big design up front
    * Where `SDD` fits in a sprint
        * Specs and user stories
        * Who writes the spec and who reviews it
<!-- chapter: anatomy-of-an-ai-consumable-spec, duration: 2h -->
* Anatomy of an `AI`-Consumable Spec
    * The three artifacts
        * The requirements document: what and why
        * The technical plan: how and with what
        * The task list: implementation in reviewable steps
    * Writing requirements the agent cannot misread
        * User stories with acceptance criteria
        * The `EARS` notation for requirements
        * Making the implicit explicit: edge cases, errors, limits
        * Marking open questions instead of hiding them
    * Writing the technical plan
        * Constraints: stack, architecture, conventions, non-goals
        * Interfaces and data models before code
        * Recording decisions and rejected alternatives
    * The project constitution
        * Ground rules that apply to every feature
        * Constitution vs per-feature spec: what goes where
    * Calibrating the level of detail
        * Under-specification: the agent fills gaps with guesses
        * Over-specification: writing the code in prose
        * What to leave to the agent on purpose
<!-- chapter: the-sdd-workflow, duration: 2h -->
* The `SDD` Workflow
    * The loop end to end
        * Specify: from a one-paragraph idea to a reviewed requirements document
        * Plan: letting the agent draft the technical plan, then correcting it
        * Tasks: decomposing the plan into small, verifiable steps
        * Implement: executing tasks one at a time vs letting the agent run
    * The human review gates
        * Reviewing the spec before any code exists
        * Reviewing each task's diff against its task description
        * Catching spec violations early instead of at the end
    * Verification against the spec
        * Deriving tests from acceptance criteria
        * Asking a second agent to audit code against the spec
        * When the code is right and the spec was wrong
    * Iterating without drift
        * Changing the spec mid-implementation: the re-plan step
        * Amending the spec when reality wins
        * The spec as the pull request's description
    * Failure modes in the loop
        * The agent that ignores the spec
        * The plan that silently contradicts the requirements
        * Recovering a derailed implementation run
<!-- chapter: sdd-tooling-today, duration: 2h -->
* `SDD` Tooling Today
    * `Spec Kit`
        * Installing and initializing a project
        * The constitution, specify, plan, tasks and implement commands
        * The generated directory structure and what to commit
        * Using `Spec Kit` with `Claude Code`, `GitHub Copilot` and Cursor
    * `Kiro` and IDE-native `SDD`
        * Requirements, design and tasks as first-class IDE artifacts
        * Hooks: keeping artifacts in sync automatically
    * `SDD` without a framework
        * Plain `Markdown` specs in the repository
        * Wiring specs into agent instruction files
        * A minimal template that covers the essentials
        * When the do-it-yourself approach beats the frameworks
    * Choosing a toolchain
        * Team constraints: `IDEs`, agents, licenses
        * Migrating between tools: the artifacts are the asset
<!-- chapter: sdd-on-a-real-team, duration: 1h -->
* `SDD` on a Real Team
    * Brownfield reality
        * Specifying a feature inside an unspecified legacy codebase
        * Reverse-engineering a baseline spec from existing code
    * Specs in the team workflow
        * Spec review as a pull request
        * Specs as living documentation and onboarding material
        * Ownership: keeping specs from becoming orphans
    * Pitfalls
        * Spec drift: code moved on, spec did not
        * Ceremony creep: specs for one-line fixes
        * The spec nobody reads because it is too long
    * When not to use `SDD`
        * Exploration, spikes and throwaway prototypes
        * The honest cost-benefit line
    * Adopting `SDD` incrementally
        * Starting with one feature and one template
        * A checklist for the first month

## Installations
Each student should have:

* A laptop with a modern editor (`VS Code` or similar) and permission to
    install software.
* A working `AI` coding agent the student already uses: `Claude Code`,
    `GitHub Copilot` (with agent mode) or Cursor, installed and authenticated.
* `git` installed and configured.
* A `Python` 3 environment with `uv` or pip for installing `Spec Kit`.
* A real code repository the student is comfortable experimenting with. A
    clone of an open source project is fine if no private repository is
    available.
* Free, wide band, access to the internet with no corporate firewall that
    blocks the student's `AI` provider.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
