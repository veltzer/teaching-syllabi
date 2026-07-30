---
tags:
  - data-and-ai:ai
  - data-and-ai:generative-ai
  - concepts:code-generation
  - tools:github
  - practices:productivity
level: intermediate
category: ai
duration_hours_short: 8
duration_hours_long: 16
duration_hours: 16
audience:
  - audiences:developers
  - audiences:team-leads
  - audiences:devops
---
<!-- course: github_copilot_in_practice -->
# `GitHub Copilot` in Practice

## Description
This course is a hands-on, tool-specific guide to `GitHub Copilot`. It does not
re-teach the general theory of `AI`-assisted development — context windows,
prompt engineering, verification discipline and the limitations of `LLMs` are
all assumed known from the Development Using `AI` course. Instead, every topic
in this course answers one question: how do you actually do it in Copilot?

Participants will drive Copilot through all of its surfaces: inline
completions, chat in the IDE, multi-file edit mode, autonomous agent mode,
the coding agent on `GitHub` itself, code review and the `CLI`. Along the way
they will customize Copilot for their own repositories with instruction
files and prompt files, wire it to external tools via `MCP` servers, and see
which Copilot feature is the right one for each kind of task.

The short version of the course covers working inside the IDE. The long
version adds the autonomous side of Copilot — agent mode with `MCP`, the
coding agent on `GitHub`, code review — and administration of Copilot in
an organization.

## Duration
* Short: 8 hours / 1 day
* Long: 16 hours / 2 days

## Intended Audience
* Software developers who have a Copilot license and want to use every part of it well
* Team leads who need to decide how Copilot should be configured and customized for their repositories
* `DevOps` engineers who want to integrate Copilot with their tooling and `CI` workflows

## Prerequisites
* The Development Using `AI` course or equivalent practical experience with `AI`-assisted development
* Proficiency in at least one programming language
* Working knowledge of `git` and `GitHub` (branches, pull requests, issues)
* A working `GitHub Copilot` license (any paid plan; the free plan works with reduced limits)

## Required Knowledge
* Development Using `AI` (or equivalent experience)

## Objectives
* **Drive** all Copilot surfaces fluently: completions, chat, edit mode, agent mode and the `CLI`
* **Customize** Copilot per repository with custom instructions, path-scoped instruction files and reusable prompt files
* **Extend** agent mode with `MCP` servers and control what tools it may use
* **Delegate** whole tasks to the Copilot coding agent on `GitHub` and review its pull requests effectively
* **Choose** the right Copilot feature for each task instead of using one hammer for everything
* **Administer** Copilot in an organization: policies, content exclusion and usage metrics

## Outline
<!-- chapter: orientation-and-setup, duration: 1h -->
* Orientation and Setup
    * The Copilot product family
        * Completions, chat, edits, agents — one license, many surfaces
        * Where Copilot runs: `VS Code`, `JetBrains` `IDEs`, `Visual Studio`, `Neovim`, `Xcode`, the `GitHub` website, the `CLI`
        * What this course uses and why (`VS Code` as the reference IDE)
    * Plans and what they unlock
        * Free, Pro, Pro+, Business and Enterprise in practice
        * Premium requests and model multipliers
        * Which features require which plan
    * Getting signed in and verified
        * Seat assignment in an organization
        * Confirming completions and chat actually work
        * Organization policies that silently change what you see
    * The model picker
        * Switching models for completions vs chat
        * Choosing a model per task: fast vs deep
        * Watching your premium request budget
<!-- chapter: code-completions-in-practice, duration: 2h -->
* Code Completions in Practice
    * Ghost text mechanics
        * Accepting, rejecting, accepting by word and by line
        * Cycling through alternative suggestions
        * The keyboard shortcuts worth internalizing
    * Next edit suggestions
        * Completions that follow your edit, not just your cursor
        * Accepting a chain of related edits across a file
    * Steering completions without chat
        * Open files and neighboring tabs as context Copilot actually sees
        * Names, types and signatures as steering wheels
        * Comment-driven completion and when it beats chat
        * Giving Copilot an example to imitate
    * When completions get in the way
        * Disabling per language, per workspace, temporarily
        * Snoozing suggestions during focused typing
    * Code matching and exclusions
        * The public code matching filter and code referencing
        * Content exclusions from the developer's point of view: what Copilot will not see
<!-- chapter: copilot-chat-in-the-ide, duration: 2h -->
* Copilot Chat in the IDE
    * The three chat surfaces
        * The chat view, inline chat and quick chat
        * Which surface for which kind of question
    * Chat participants
        * `@workspace` for questions about your codebase
        * `@terminal`, `@vscode` and `@github`
        * How participants change what context is gathered
    * Slash commands
        * `/explain`, `/fix`, `/tests`, `/doc`, `/new`
        * Fixing a failing test directly from the test explorer
    * Controlling context explicitly
        * `#file`, `#selection`, `#codebase` and friends
        * Dragging files and folders into the prompt
        * Attaching images and screenshots
        * How workspace indexing works and why it matters for `@workspace`
    * Getting answers into your code
        * Applying code blocks into the editor and the terminal
        * Smart actions from the editor context menu
    * Verifying chat answers
        * Making Copilot show which files it used
        * Spotting answers that ignored your codebase
<!-- chapter: customizing-copilot, duration: 2h -->
* Customizing Copilot for Your Repository
    * Repository custom instructions
        * The `copilot-instructions.md` file: location, format, scope
        * What to put in it: conventions, build commands, "never do this" rules
        * What Copilot ignores no matter how nicely you ask
    * Path-scoped instruction files
        * Instruction files with `applyTo` globs
        * Different rules for tests, frontend code and generated code
        * Layering: repository, path and personal instructions together
    * Personal custom instructions
        * Preferences that follow you across repositories
        * Keeping personal and team instructions from fighting
    * Prompt files
        * Reusable, parameterized prompts checked into the repository
        * Turning a team workflow into a runnable prompt
        * Prompt files vs custom instructions: which content goes where
    * Custom chat modes
        * Packaging a persona, tool set and instructions into a named mode
    * Verifying customization works
        * Seeing which instruction files a response actually used
        * Debugging instructions that are not being picked up
<!-- chapter: edit-mode-and-agent-mode, duration: 1h -->
* Edit Mode and Agent Mode
    * Edit mode
        * Multi-file edits from a single prompt
        * Managing the working set of files
        * Reviewing, accepting and rejecting per file
    * Agent mode
        * What it adds: running commands, reading output, iterating on failures
        * Approving terminal commands and tools
        * Auto-approval settings and their risks
        * Checkpoints and undoing what the agent did
    * Choosing the right surface
        * Completion vs chat vs edit vs agent — a practical decision guide
        * Recognizing a task that is too big for one agent run
<!-- chapter: agent-mode-deep-dive-and-mcp-long, duration: 2h -->
* Agent Mode Deep Dive and `MCP` [long]
    * How agent mode uses tools
        * The built-in tool set: files, terminal, tests, search
        * Watching an agent session step by step
    * Adding `MCP` servers
        * Workspace vs user level `MCP` configuration
        * Installing and starting a server, verifying its tools appear
        * The `GitHub` `MCP` server: issues, pull requests and `CI` from chat
        * Browser automation and database servers in an agent workflow
    * Controlling the blast radius
        * Enabling and disabling individual tools
        * Tool approval prompts and when not to auto-approve
        * Prompt injection through tool results: the practical precautions
    * Instructions and agents together
        * `AGENTS.md` and repository instructions in agent mode
        * Making agent runs reproducible for teammates
    * Agent workflows that work
        * Fixing a failing build end to end
        * Scaffolding a feature across multiple files
        * Knowing when to stop the agent and take over
<!-- chapter: the-copilot-coding-agent-on-github-long, duration: 2h -->
* The Copilot Coding Agent on `GitHub` [long]
    * What the coding agent is
        * Assigning an issue to Copilot and getting a pull request back
        * How it differs from agent mode in the IDE
    * Delegating work
        * From an issue, from chat, from the IDE
        * Writing issues an agent can actually implement
    * Following and steering a session
        * Reading the session log
        * Steering with pull request review comments
        * Iterating until the pull request is mergeable
    * Preparing a repository for the agent
        * The setup steps workflow file: installing dependencies before the agent starts
        * Custom instructions the agent will read
        * The firewall: what the agent can and cannot reach
        * `MCP` servers for the coding agent
    * Economics and fit
        * Premium requests and `GitHub Actions` minutes it consumes
        * Task shapes that succeed and task shapes that waste money
<!-- chapter: copilot-on-the-github-website-and-the-cli-long, duration: 2h -->
* Copilot on the `GitHub` Website and the `CLI` [long]
    * Pull request features
        * Generated pull request summaries
        * Copilot code review: requesting a review on demand
        * Automatic review rules for a repository or organization
        * Steering review with coding guidelines and instructions
        * Treating Copilot review as a first pass, not a verdict
    * Copilot chat on the website
        * Asking questions about any repository, issue or pull request
        * Spaces: grounding chat in a curated bundle of context
        * Knowledge bases on the Enterprise plan
    * Copilot in the `CLI`
        * Explaining and suggesting shell commands
        * Running Copilot as an agent from the terminal
    * Small conveniences that add up
        * Commit message generation in the IDE
        * Explaining a failed `CI` run
<!-- chapter: administering-copilot-in-an-organization-long, duration: 2h -->
* Administering Copilot in an Organization [long]
    * Seats and access
        * Assigning seats by team
        * Handling contractors and short-lived access
    * Policies
        * Feature-by-feature enablement: chat, agents, models, previews
        * The public code matching policy and its legal background
        * Data retention and model training: what leaves your organization
    * Content exclusion
        * Excluding files and repositories from Copilot's view
        * What exclusion protects against and what it does not
    * Auditing and metrics
        * Copilot events in the audit log
        * The usage metrics `API` and adoption dashboards
        * Metrics that mean something vs vanity acceptance rates
    * Rolling Copilot out
        * Pilots, champions and internal training
        * A checklist of decisions every organization must make

## Installations
Each student should have:

* A laptop with `VS Code` installed and permission to install extensions.
    Students who prefer a `JetBrains` IDE may use one, but some agent-related
    features will be demonstrated in `VS Code` only.
* A `GitHub` account with an active `GitHub Copilot` subscription (any paid
    plan; for the long version of the course a Business or Enterprise plan is
    required for the administration chapter to be exercised, otherwise it is
    demonstrated by the instructor).
* `git` installed and configured, and permission to create repositories on
    `GitHub`.
* A real code repository the student is comfortable experimenting with. A
    clone of an open source project is fine if no private repository is
    available.
* `node` and `npm` installed for running local `MCP` servers.
* Free, wide band, access to the internet with no corporate firewall that
    blocks `GitHub` or the Copilot endpoints.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
