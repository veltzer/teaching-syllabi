---
audience:
  - audiences:managers
  - audiences:team-leads
  - audiences:architects
  - audiences:developers
category: ai
duration_minutes: 120
level: intermediate
tags:
  - concepts:embeddings
  - concepts:lsp
  - concepts:parsing
  - data-and-ai:agents
  - data-and-ai:ai
  - data-and-ai:rag
  - practices:documentation
---

<!-- blurb: code_context_retrieval -->
# Grep, `RAG`, Documentation, or Parsers? How `AI` Agents Find Context in Code

**Technical leadership expert talk.** A side-by-side comparison of the four ways an `AI`
coding agent can learn about a codebase, and how to choose and combine them.

## The Challenge

An `AI` coding agent is only as good as the context it works with. Tools and vendors offer
very different answers to how that context should be found: plain text search, retrieval
over embeddings, hand-written documentation, or real language parsers. Each is promoted as
the solution, each has blind spots, and choosing the wrong one leads to agents that miss
relevant code, drown in irrelevant code, or confidently follow outdated guidance.

## What This Session Covers

A practical, technical comparison of text search, retrieval-augmented generation (`RAG`),
documentation, and language parsers as sources of context for `AI` agents: how each one
works, what it is good and bad at, what it costs to set up and maintain, and how they fit
together in a real development workflow.

## Agenda

* **The Context Problem** (10 min): Why agents need help finding the right code, and the criteria for comparing approaches: precision, recall, freshness, cost, and maintenance.
* **Text Search: `grep` and `ripgrep`** (20 min): Why agents rely on plain search so heavily, where exact matching shines, and where it breaks down on naming variation and conceptual questions.
* **Retrieval-Augmented Generation** (25 min): Embeddings, chunking, and vector search over code; finding code by meaning, and the cost of stale indexes and plausible but wrong matches.
* **Documentation** (20 min): Agent instruction files and architecture notes; capturing intent, conventions, and decisions that no search over the code can recover.
* **Language Parsers** (20 min): Syntax trees, symbol indexes, and language servers (`LSP`); exact definitions, references, and call graphs, and the price of per-language tooling.
* **Choosing and Combining** (15 min): A side-by-side comparison, which approach fits which codebase and question, and how layered strategies work in practice.
* **Key Takeaways and Q&A** (10 min): Actionable next steps for engineering teams.

## Takeaways

* A clear understanding of how text search, `RAG`, documentation, and language parsers each give context to `AI` agents
* The strengths, blind spots, and maintenance costs of each approach
* A practical framework for choosing and combining approaches for your own codebase

## Who Should Attend

* Engineering managers
* Tech leads
* Software architects
* Developers adopting `AI` coding assistants

## Continue the Journey

This talk compares the approaches. A follow-on, hands-on workshop can measure them against
the team's own codebase and set up the combination that fits it best.

## Speaker

Mark Veltzer
