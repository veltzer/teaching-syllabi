---
tags:
  - data-and-ai:ai
  - data-and-ai:generative-ai
  - data-and-ai:agents
  - concepts:code-generation
  - practices:methodology
  - practices:agile
  - practices:user-stories
  - practices:productivity
level: intermediate
category: ai
duration_hours: 16
audience:
  - audiences:developers
  - audiences:team-leads
  - audiences:architects
  - audiences:product-managers
---

<!-- course: bmad_method -->
# The `BMAD` Method

## Description
`BMAD` (Breakthrough Method for Agile `AI`-Driven Development) is an open
source framework for running a software project with a team of specialized
`AI` agents instead of a single all-purpose chat. An analyst, a product
manager, an architect, a scrum master, a developer and a test architect each
come as a persona with its own workflows, templates and checklists, and the
work flows between them through documents: a product brief, a `PRD`, an
architecture document and, finally, self-contained story files that a
developer agent implements one at a time. The method is `IDE` and model
agnostic and installs into `Claude Code`, Cursor, `Windsurf`, `Cline`,
`GitHub Copilot` and others.

This course teaches `BMAD` as a working method, not as a demo. Participants
install the framework, run every phase of it on a real project, learn what
each agent does and why the hand-offs are shaped the way they are, and then
go under the hood: how agents, workflows and templates are defined, how to
customize them for a team and how to build new ones. The course covers both
the widely deployed version 4 layout and the modular version 6 layout and
explains how to tell which one a project is on.

The course assumes participants already develop with `AI` assistance. It
does not re-teach prompting, context windows or how coding agents work.

## Duration
16 hours / 2 days

## Intended Audience
* Developers who use `AI` coding agents and want a structured, repeatable process around them
* Team leads and scrum masters who want `AI` agents to fit an existing agile workflow rather than bypass it
* Architects who want design decisions to survive contact with an autonomous coding agent
* Product managers who will write briefs and requirements that `AI` agents implement from

## Prerequisites
* Practical experience developing with an `AI` coding assistant or agent
* The Development Using `AI` course or equivalent experience
* Proficiency in at least one programming language
* Working knowledge of `git` and pull request workflows
* Familiarity with agile vocabulary: epics, stories, sprints, definition of done

## Required Knowledge
* Development Using `AI` (or equivalent experience)

## Objectives
* **Explain** the `BMAD` philosophy: agent specialization, document-driven context and the planning-to-implementation hand-off
* **Install** and configure `BMAD` in a project and in the `IDE` or `CLI` agent the team already uses
* **Run** the planning phase end to end: brainstorming, product brief, `PRD`, architecture and epic breakdown
* **Run** the implementation loop: drafting stories, implementing them one at a time, reviewing and closing them
* **Use** the test architect agent to gate quality with risk profiles, test designs and traceability
* **Apply** `BMAD` to brownfield codebases and to small changes without drowning them in ceremony
* **Customize** agents, templates and workflows for a team, and build new ones with the builder tooling
* **Judge** where `BMAD` helps, where it is overhead and how it compares to `Spec Kit`, `Kiro` and plain instruction files

## Outline
<!-- chapter: why-bmad, duration: 1h -->
* Why `BMAD`
    * How single-chat development fails on real projects
        * Decisions lost as the context window scrolls away
        * The agent that plans, codes and reviews its own work in one breath
        * Inconsistent output from one feature to the next
    * The two ideas behind `BMAD`
        * Agentic planning: specialized personas that collaborate with the human on documents
        * Context-engineered development: story files that carry everything the coder needs
    * The agent team and the document chain
        * Brief, `PRD`, architecture, epics, stories
        * Who produces what and who consumes it
        * The human as the decision maker at every hand-off
    * `BMAD` in the landscape
        * Relation to Scrum and to classic agile artifacts
        * Relation to spec-driven development
        * What it is not: not a model, not an `IDE`, not an autonomous coder
    * The project and its versions
        * The version 4 layout and the modular version 6 layout
        * Recognising which one a repository uses
<!-- chapter: installing-and-configuring-bmad, duration: 1h -->
* Installing and Configuring `BMAD`
    * Installation
        * The `Node.js` based installer and what it writes into the repository
        * Selecting the target `IDEs` and agents
        * Upgrading and reinstalling without losing customizations
    * What landed in the repository
        * The agent definitions, workflows, tasks, templates and checklists
        * The generated slash commands and rule files per `IDE`
        * The configuration file: document locations, sharding, loading of developer files
    * Choosing where each phase runs
        * Planning in a web chat with bundled agents vs planning inside the `IDE`
        * The cost argument for web bundles and the convenience argument against
        * Model choice per agent: strong models for planning, fast models for implementation
    * Activating an agent and talking to it
        * Agent commands and the help listing
        * Switching agents and starting fresh sessions on purpose
<!-- chapter: the-agents, duration: 2h -->
* The Agents
    * Anatomy of a `BMAD` agent
        * Persona, principles, commands and dependencies
        * How an agent definition becomes a system prompt
        * Why each agent sees only the files it needs
    * The planning agents
        * The analyst: brainstorming, market and competitor research, the product brief
        * The product manager: the `PRD`, epics and story lists
        * The architect: system design, technology choices, the architecture document
        * The user experience expert: front-end specifications and design prompts
    * The implementation agents
        * The scrum master: drafting the next story from epics and architecture
        * The developer: implementing a story and recording what was done
        * The test architect: risk, test design, review and quality gates
        * The product owner: validating artifacts and running the master checklist
    * The meta agents
        * The master agent that can run any task without a persona
        * The orchestrator for switching roles inside one session
        * When the meta agents are convenient and when they defeat the purpose
    * Elicitation and interaction patterns
        * Interactive versus one-shot document generation
        * Advanced elicitation: the numbered refinement menu
        * Party mode: several agents debating one decision
<!-- chapter: analysis-and-planning, duration: 2h -->
* Analysis and Planning
    * From idea to product brief
        * Brainstorming techniques the analyst offers
        * Research tasks and when to bother with them
        * The brief as the contract for the `PRD`
    * The product requirements document
        * Goals, background, functional and non-functional requirements
        * Epics as deliverable increments, stories as sprint-sized units
        * Acceptance criteria that an agent can verify
        * The product manager checklist
    * Reviewing a generated `PRD`
        * Catching invented requirements
        * Calibrating detail: enough for the architect, not pseudo-code
        * Recording open questions instead of guesses
    * Document conventions that make the chain work
        * Section headings the next agent will look for
        * Keeping documents in the repository and under review
<!-- chapter: architecture-and-solution-design, duration: 2h -->
* Architecture and Solution Design
    * The architecture document
        * Tech stack, project structure, data models and `API` contracts
        * Coding standards and testing strategy as agent instructions
        * Deciding what the developer agent must never decide for itself
        * The architect checklist
    * Front-end and full-stack variants
        * The front-end specification from the user experience expert
        * Prompts for `AI` user interface generators
    * Technical preferences
        * Encoding the team's stack and taboos once
        * How preferences flow into every architecture
    * Validation before implementation
        * The product owner master checklist across all documents
        * Fixing the documents, not the code, when the checklist fails
    * Sharding
        * Why big documents must be split before implementation
        * Sharding the `PRD` and the architecture into per-section files
        * What the developer agent actually loads
<!-- chapter: the-implementation-loop, duration: 3h -->
* The Implementation Loop
    * The story file
        * Status, story statement, acceptance criteria, tasks and subtasks
        * The developer notes section: the context the scrum master pulls from the architecture
        * The developer record: what was changed, tested and left open
        * Story status lifecycle from draft to done
    * Drafting a story
        * The scrum master reads the epic, the architecture shards and the previous story
        * The story draft checklist
        * The human approval step and why skipping it hurts
    * Implementing a story
        * The developer agent's order of work: tasks, tests, validations, record
        * Running in a fresh session with only the story loaded
        * Handling a story that turns out to be wrong or too big
        * The definition of done checklist
    * Reviewing a story
        * The test architect review and the quality gate decision
        * Sending a story back versus patching forward
        * Updating the story file as the record of truth
    * Running the loop in practice
        * Sequential stories, branches and pull requests
        * Keeping the architecture document honest as code evolves
        * Retrospectives per epic
    * Failure modes
        * The developer agent that reads the whole repository anyway
        * Context bleed between stories
        * Stories that drift from the `PRD` without anyone noticing
<!-- chapter: quality-and-the-test-architect, duration: 1h -->
* Quality and the Test Architect
    * The test architect's toolkit
        * Risk profiling before implementation
        * Test design: what to test at which level
        * Requirements tracing: acceptance criteria to tests
        * Non-functional requirements assessment
    * The quality gate
        * Pass, concerns, fail and waived
        * Gate files as a reviewable artifact
        * Who may waive and how it is recorded
    * Fitting the gate into existing practice
        * `CI/CD` as the executor of the test architect's design
        * Human code review alongside agent review
<!-- chapter: scaling-the-method, duration: 1h -->
* Scaling the Method Up and Down
    * Project levels
        * From a single atomic change to an enterprise system
        * Which documents each level actually needs
    * The quick path
        * A technical specification instead of the full chain for small work
        * Knowing when a bug fix deserves no ceremony at all
    * Brownfield projects
        * Documenting an existing codebase for the agents
        * Brownfield `PRD` and architecture variants
        * Protecting existing behavior while adding features
    * Big projects
        * Multiple epics in flight and the ordering problem
        * Several developers and several developer agents on one repository
<!-- chapter: customizing-and-extending-bmad, duration: 2h -->
* Customizing and Extending `BMAD`
    * The building blocks
        * Agents, workflows, tasks, templates and checklists as `Markdown` and `YAML`
        * How the pieces reference each other
    * Customizing what is there
        * Overriding an agent's persona and principles without forking the framework
        * Editing templates to match the team's document standards
        * Adding team-specific checklist items
        * Surviving an upgrade with customizations intact
    * Building new components
        * A new agent for a role the team has and `BMAD` does not
        * A new workflow with its own steps and outputs
        * The builder module as the tool for the job
    * Expansion packs and modules
        * The core, the method module and the creative module
        * Game development packs for `Unity`, `Godot` and `Phaser`
        * Infrastructure and `DevOps` packs
        * Writing a pack for a non-software domain
    * Integrating with the rest of the toolchain
        * `MCP` servers available to the agents
        * Issue trackers such as `Jira` as the source of epics
        * Agent instruction files and `BMAD` side by side
<!-- chapter: bmad-on-a-real-team, duration: 1h -->
* `BMAD` on a Real Team
    * Adoption
        * Starting with one feature and the minimal document chain
        * Who owns which document in a real organization
        * Training the product side to review `AI` generated requirements
    * Pitfalls
        * Documents nobody reads because they are too long
        * Ceremony creep on tiny changes
        * Trusting the agents' checklists instead of reading the output
        * The one developer who runs the whole chain alone
    * `BMAD` compared with the alternatives
        * `Spec Kit`: lighter chain, fewer personas
        * `Kiro`: the same ideas built into one `IDE`
        * Hand-rolled instruction files
        * Picking one, or mixing them
    * Keeping up with the project
        * Release cadence, breaking changes and migration between versions
        * The community and where the discussions happen

## Installations
Each student should have:

* A laptop with a modern editor (`VS Code` or similar) and permission to
  install software.
* A working `AI` coding agent the student already uses: `Claude Code`,
  Cursor, `Windsurf`, `Cline` or `GitHub Copilot` with agent mode, installed
  and authenticated with an account that can run long sessions.
* `Node.js` with `npm` installed, for the `BMAD` installer.
* `git` installed and configured.
* A real code repository the student is comfortable experimenting with. A
  clone of an open source project is fine if no private repository is
  available.
* Optionally, access to a web chat such as `ChatGPT`, Gemini or Claude for
  running the planning phase with bundled agents.
* Free, wide band, access to the internet with no corporate firewall that
  blocks the student's `AI` provider or `npm`.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
