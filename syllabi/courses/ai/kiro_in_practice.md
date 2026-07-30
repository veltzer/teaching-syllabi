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
---
<!-- course: kiro_in_practice -->
# `Kiro` in Practice

## Description
`Kiro` is `AWS`'s agentic IDE, built from the ground up around spec-driven
development: instead of only chatting with an agent, you grow each feature
from a requirements document, a design document and a task list that the
agent then executes. Around that core, `Kiro` adds steering files for
persistent project knowledge, event-driven agent hooks, `MCP` integration
and a supervised-to-autonomous autonomy dial.

This course is a hands-on, tool-specific guide to `Kiro`. It does not
re-teach general `AI`-assisted development — context windows, prompting,
agents and the `MCP` protocol are all assumed known from the Development
Using `AI` course. Spec-driven development as a methodology is likewise
assumed (or picked up in the Spec-Driven Development with `AI` course).
Every topic here answers one question: how do you actually do it in `Kiro`?
Each concept is exercised by configuring or running it on the student's own
machine against a real codebase.

## Duration
8 hours / 1 day

## Intended Audience
* Software developers adopting `Kiro` as their daily IDE
* Team leads deciding how `Kiro` should be configured and shared across a team
* Developers already using another `AI` IDE who want to transfer their workflow to `Kiro`

## Prerequisites
* The Development Using `AI` course or equivalent practical experience with `AI`-assisted development
* Familiarity with spec-driven development concepts is an advantage
* Proficiency in at least one programming language
* Working knowledge of `git`
* A working `Kiro` installation with a logged-in account

## Required Knowledge
* Development Using `AI` (or equivalent experience)

## Objectives
* **Set up** `Kiro` properly: accounts, pricing tiers, imported settings and model selection
* **Choose** deliberately between vibe sessions and spec sessions, and between supervised and autopilot execution
* **Drive** the full spec workflow in `Kiro`: requirements, design, tasks and task-by-task execution
* **Encode** project knowledge in steering files with the right inclusion modes
* **Automate** repetitive agent work with hooks triggered by IDE events
* **Wire** `MCP` servers into `Kiro` and control what the agent may do with them
* **Share** a working `Kiro` configuration across a team through the repository

## Outline
<!-- chapter: orientation-and-setup, duration: 1h -->
* Orientation and Setup
    * What `Kiro` is
        * An agentic IDE, not a plugin: what being a `VS Code` fork buys you
        * The big pieces: specs, steering, hooks, `MCP`, autopilot
        * How `Kiro` relates to `Amazon Q` and the `Kiro` `CLI`
    * Installation and sign-in
        * The sign-in options: Builder `ID`, `Google`, `GitHub`, `IAM` Identity Center
        * Which sign-in your organization wants you to use and why it matters
    * Making `Kiro` feel like home
        * Importing `VS Code` settings and keybindings
        * Extensions via `Open VSX`: what carries over and what does not
    * Pricing and requests
        * The tiers and what a request costs you
        * Vibe requests vs spec requests in the quota
        * Picking the model per session and what it changes
    * The autonomy dial
        * Supervised mode: reviewing every change
        * Autopilot: what it may do without asking
        * Where the boundary actually sits and how to move it
<!-- chapter: chat-completions-and-context, duration: 1h -->
* Chat, Completions and Context
    * Vibe sessions
        * When plain chat is the right tool in a spec-driven IDE
        * Session history and returning to an old conversation
    * Feeding the agent context explicitly
        * `#file`, `#folder`, `#codebase`
        * `#problems`, `#terminal` and `#git` diff
        * Images and screenshots in the prompt
    * Inline completions
        * What `Kiro` completes as you type and how to steer it
        * Turning completions off when they compete with the agent
    * Reviewing what the agent did
        * Reading the change set before accepting
        * Undoing an agent action
        * The execution log as your audit trail
<!-- chapter: specs-in-kiro, duration: 2h -->
* Specs in `Kiro`
    * From prompt to spec
        * Starting a spec session from one paragraph of intent
        * The three generated files: requirements, design, tasks
        * Where they live in the repository and why you commit them
    * The requirements document
        * User stories with `EARS` acceptance criteria as `Kiro` writes them
        * Correcting requirements before any design exists
        * Adding the edge cases `Kiro` did not think of
    * The design document
        * Reviewing proposed architecture, interfaces and data models
        * Pushing back: regenerating design after changing requirements
    * The task list
        * How `Kiro` decomposes the design into ordered tasks
        * Editing, reordering and deleting tasks by hand
    * Executing tasks
        * Running one task at a time and reviewing each diff
        * Letting autopilot run the whole list
        * Task status tracking and resuming after interruption
    * Specs over time
        * Updating a spec when requirements change mid-feature
        * Starting a spec from existing code instead of from scratch
        * When a vibe session should have been a spec, and the reverse
<!-- chapter: steering, duration: 1h -->
* Steering
    * What steering files are in `Kiro`
        * Persistent project knowledge the agent reads every session
        * Steering vs a spec: knowledge vs work
    * The three foundation documents
        * Product, technical stack and project structure
        * Generating them from an existing codebase and correcting the result
    * Custom steering files
        * Writing your own: conventions, forbidden patterns, domain language
        * Inclusion modes: always, by file match, on demand
        * Scoping a steering file to the code it is about
    * Steering discipline
        * Keeping steering short enough to be obeyed
        * Detecting when the agent stopped following a steering rule
        * Reviewing steering files in code review like any other code
<!-- chapter: agent-hooks, duration: 1h -->
* Agent Hooks
    * What a hook is in `Kiro`
        * An agent prompt fired by an IDE event
        * Hooks vs steering: automation vs knowledge
    * Creating hooks
        * Trigger types: file saved, file created, file deleted, manual
        * Writing the hook prompt in natural language
        * Scoping a hook to file patterns
    * Hook recipes that earn their keep
        * Updating the test file when a source file is saved
        * Keeping documentation in sync with code
        * A pre-commit security and secrets scan on demand
        * Updating a translation file when strings change
    * Operating hooks
        * Enabling, disabling and sharing hooks through the repository
        * Watching a hook run and reading its output
        * Hooks that fire too often: cost and noise control
<!-- chapter: mcp-in-kiro, duration: 1h -->
* `MCP` in `Kiro`
    * Where `MCP` configuration lives
        * Workspace level vs user level configuration files
        * Committing workspace `MCP` configuration for the team
    * Adding and running servers
        * Installing a server and verifying its tools appear in chat
        * Servers worth starting with: documentation search, `AWS` tooling, browsers, databases
    * Controlling what the agent may do
        * Per-tool approval at call time
        * The auto-approve list and what belongs on it
        * Disabling a server without deleting its configuration
    * `MCP` in real workflows
        * Specs whose tasks call `MCP` tools
        * Hooks that use `MCP` servers
        * Troubleshooting: logs, restarts and schema mismatches
<!-- chapter: kiro-on-a-team-and-in-the-terminal, duration: 1h -->
* `Kiro` on a Team and in the Terminal
    * The repository as the unit of sharing
        * What to commit: specs, steering, hooks, workspace `MCP` configuration
        * What stays personal and out of the repository
        * Reviewing agent artifacts in pull requests
    * Team conventions
        * Agreeing when a change requires a spec
        * Naming and structuring steering files consistently
        * Onboarding a new developer through the committed `Kiro` setup
    * The `Kiro` `CLI`
        * The agent in the terminal: when it beats the IDE
        * Sharing steering and `MCP` configuration between IDE and `CLI`
        * Scripting the `CLI` in automation
    * Governance and cost
        * Privacy settings: what leaves your machine and opting out of data sharing
        * Watching request consumption across a team
        * A checklist for rolling `Kiro` out to a team

## Installations
Each student should have:

* A laptop running `Linux`, `macOS` or `Windows` with permission to install
    software.
* `Kiro` installed and signed in with a working account before the course
    starts. The free tier is sufficient for the exercises.
* `git` installed and configured.
* `node` and `npm` (or `uv` and a `Python` 3 environment) for running local
    `MCP` servers.
* A real code repository the student is comfortable experimenting with. A
    clone of an open source project is fine if no private repository is
    available.
* Free, wide band, access to the internet with no corporate firewall that
    blocks `Kiro`'s endpoints or `Open VSX`.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
