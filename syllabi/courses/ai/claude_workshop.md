---
tags:
  - data-and-ai:ai
  - data-and-ai:llm
  - data-and-ai:agents
  - data-and-ai:mcp
  - data-and-ai:rag
  - data-and-ai:prompt-engineering
  - practices:productivity
level: intermediate
category: ai
duration_hours: 8
audience:
  - audiences:developers
  - audiences:senior-developers
  - audiences:devops
---
<!-- course: claude_workshop -->
# Claude Workshop

## Description
This one day workshop is a hands-on, end-to-end tour of working effectively with
Claude, with a focus on `Claude Code` as a daily driver for software engineering work.
The workshop walks through the moving parts that determine how Claude behaves
in practice: how to configure it at the global and per-project level, how its
context window works and what compaction does to long sessions, how to extend
it with skills and agents, how to plug it into external systems via `MCP`
servers, and how to ground its answers with `RAG` over your own data.

The emphasis throughout is practical. Each topic is illustrated by configuring
something on the student's own machine and seeing how that change shows up in
Claude's behavior on a real codebase.

## Duration
8 hours / 1 day

## Intended Audience
* Software developers who already use Claude occasionally and want to use it well
* Senior developers and tech leads evaluating Claude for team adoption
* `DevOps` engineers who want to wire Claude into existing tooling via `MCP`
* Engineers building internal assistants on top of Claude that need to reason
    over private knowledge bases

## Prerequisites
* Comfortable on the command line in a `UNIX`-like environment
* Proficiency in at least one programming language
* Working knowledge of `git` and a real development workflow
* A Claude account with `Claude Code` installed and authenticated

## Objectives
* **Configure** Claude at the global and per-project level, including settings,
    permissions, hooks and environment variables
* **Reason about the context window** and use compaction deliberately rather
    than letting it surprise you in long sessions
* **Extend** Claude with skills for repeatable workflows and sub-agents for
    delegated, isolated work
* **Connect** Claude to external systems via `MCP` servers and understand the
    trust boundary that creates
* **Ground** Claude's answers in your own data using a `RAG` pipeline and know
    when `RAG` is the right tool versus long context or fine tuning

## Outline
<!-- chapter: introduction-and-orientation, duration: 1h -->
* Introduction and Orientation (1 hour)
    * What Claude is and what Claude is not
        * Claude the model vs. Claude the product
        * `Claude Code` as a coding agent
        * Other Claude surfaces (web app, `API`, IDE extensions)
    * The Claude model family at a glance
        * Opus, Sonnet, Haiku and when to reach for each
        * Cost, latency and capability trade-offs
        * Knowledge cutoff and what it means in practice
    * A mental model for working with an `LLM` coding agent
        * Why Claude reads files, runs commands and edits code itself
        * Why prompts are not the whole story any more
        * Where humans still need to stay in the loop
    * Workshop ground rules
        * Working on a real repo throughout the day
        * Capturing prompts, configs and outputs as we go
<!-- chapter: configuring-claude-general-and-per-project, duration: 2h -->
* Configuring Claude: General and Per Project (2 hours)
    * The two layers of configuration
        * User level settings vs. project level settings
        * Where Claude looks and in what order
        * What belongs in each layer
    * Global configuration
        * The user `settings.json`
        * Default model selection
        * Theme, status line and editor integration
        * Global permissions and allowlists
    * Project configuration
        * Project `settings.json` and `settings.local.json`
        * What is checked in vs. local-only
        * Project specific environment variables
        * Sharing configuration across a team
    * `CLAUDE.md` and project memory
        * Writing instructions Claude will actually follow
        * Coding style, conventions and "do not do this" rules
        * Per directory vs. per repo guidance
        * Keeping `CLAUDE.md` small and high signal
    * Permissions and safety
        * Approving and denying tools
        * Allowlisting commands to cut down on prompts
        * Hooks as automation triggers
        * What hooks can and cannot enforce
    * Working with multiple repositories
        * Switching projects without leaking context
        * Per project model and permission choices
<!-- chapter: the-context-window-and-compaction, duration: 1h -->
* The Context Window and Compaction (1 hour)
    * What lives in the context window
        * System prompt, instructions and memory
        * Tool results, file reads and command output
        * The running conversation
    * Token budgets in real sessions
        * Why a "1M context" model still has limits
        * Cost and latency as a function of tokens
        * Reading what is actually in your window
    * How long sessions go wrong
        * Slow degradation of attention to early instructions
        * Tool result spam and how to avoid it
        * The "I forgot what we were doing" failure mode
    * Compaction
        * What compaction does to the conversation
        * When the harness triggers it automatically
        * When to compact deliberately
        * What survives a compaction and what does not
    * Prompt caching
        * Why repeated prefixes are cheap
        * Structuring sessions to keep the cache warm
        * The five minute cache window in practice
    * Working habits for long sessions
        * Starting fresh vs. continuing
        * Using sub-agents to keep the main context clean
        * Writing things down instead of relying on memory
<!-- chapter: skills, duration: 1h -->
* Skills (1 hour)
    * What a skill is
        * A named, reusable instruction set with its own tools
        * How skills differ from plain prompts
        * How skills differ from agents
    * Built in skills
        * Touring the skills shipped with `Claude Code`
        * Reading a skill's description to know when it fires
        * Invoking a skill explicitly via `/<name>`
    * Authoring a skill
        * Anatomy of a skill file
        * Writing a good description that triggers reliably
        * Scoping tools and permissions
        * Versioning and sharing skills across a team
    * Slash commands as a user surface
        * Mapping team workflows to slash commands
        * Common patterns: review, refactor, summarize, audit
    * When not to use a skill
        * One off tasks
        * Cases where a plain prompt is clearer
<!-- chapter: agents-and-sub-agents, duration: 1h -->
* Agents and Sub Agents (1 hour)
    * Why sub-agents exist
        * Protecting the main context window
        * Parallelizing independent work
        * Giving a task a narrow, focused tool set
    * The agent catalog
        * General purpose vs. specialized agents
        * Explore, Plan, code review and friends
        * Choosing the right agent for the task
    * Briefing an agent well
        * The "smart colleague who just walked in" framing
        * What context to hand over, what to leave out
        * Asking for a short report instead of a dump
    * Foreground vs. background agents
        * When to block on a result
        * When to fire and forget
        * Continuing a previous agent vs. starting fresh
    * Trust but verify
        * Agents describe what they meant to do
        * Reading the diff before declaring victory
        * Common failure modes and how to spot them
    * Worktree isolation
        * Running an agent on a throwaway copy of the repo
        * Reviewing and merging the result
<!-- chapter: connecting-to-mcp-servers, duration: 1h -->
* Connecting to `MCP` Servers (1 hour)
    * What `MCP` is and why it exists
        * The Model Context Protocol in one paragraph
        * Tools, resources and prompts as the three primitives
        * Why a standard protocol matters
    * The `MCP` ecosystem
        * Common servers: filesystem, `git`, `GitHub`, databases, browsers
        * Vendor-provided vs. community servers
        * Local servers vs. remote servers
    * Adding an `MCP` server to Claude
        * Configuring a server at the user or project level
        * Authentication and secrets handling
        * Verifying the server is actually wired up
    * Using `MCP` tools in a real workflow
        * Letting Claude query a database directly
        * Driving a browser from a Claude session
        * Reading and writing tickets in an issue tracker
    * The trust boundary
        * Every `MCP` server is code you are running
        * Prompt injection via tool results
        * Auditing what an `MCP` server can do before installing it
    * Writing a small `MCP` server
        * The minimum viable server
        * Exposing one internal tool to Claude
        * When this is worth the effort and when it is not
<!-- chapter: rag-grounding-claude-in-your-data, duration: 1h -->
* `RAG`: Grounding Claude in Your Data (1 hour)
    * The problem `RAG` solves
        * Claude does not know your private data
        * Why "just paste it in" stops working at scale
        * Why fine tuning is usually the wrong answer
    * The anatomy of a `RAG` pipeline
        * Ingestion and chunking
        * Embeddings and the vector store
        * Retrieval at query time
        * Composing the final prompt
    * Choosing the moving parts
        * Embedding model selection
        * Vector store options
        * Chunk size and overlap as practical knobs
    * Retrieval quality
        * Why naive cosine similarity disappoints
        * Hybrid search with `BM25` and re-ranking
        * Evaluating retrieval separately from generation
    * Wiring `RAG` into Claude
        * Exposing retrieval as an `MCP` tool
        * Letting Claude decide when to retrieve
        * Citing sources back to the user
    * `RAG` vs. long context vs. fine tuning
        * When each is the right answer
        * Combining them sensibly
        * Cost and freshness considerations
    * Common failure modes
        * Stale indexes
        * Chunk boundaries that destroy meaning
        * Confident hallucinations on top of bad retrieval
<!-- chapter: putting-it-all-together, duration: 0h -->
* Putting It All Together (wrap up)
    * Reviewing the configuration, skills, agents and servers we installed
    * A checklist for adopting Claude on a team
    * Where to go next: deeper dives into prompt engineering, evaluation and
        agent building

## Installations
Each student should have:

* A laptop running `Linux`, `macOS` or `Windows` with administrator rights to
    install software.
* `Claude Code` installed and logged in to a working Claude account before the
    workshop starts.
* `node` and `npm` (or another runtime as required by the `MCP` servers we will
    install during the day).
* `git` installed and configured.
* A real code repository the student is comfortable experimenting with. A clone
    of an open source project is fine if no private repo is available.
* A modern editor (`VS Code` or similar) with the `Claude Code` integration
    installed.
* Free, wide band, access to the internet with no corporate firewall that blocks
    `Anthropic`'s `API` endpoints, `npm` or pip.
* For the `RAG` section: a working `Python` 3 environment with pip.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
