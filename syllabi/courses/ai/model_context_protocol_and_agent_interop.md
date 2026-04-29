---
tags:
  - concepts:ai
  - concepts:api
  - concepts:best-practices
  - concepts:design-patterns
level: intermediate
category: ai
duration_hours: 16
audience:
  - audiences:ml-engineers
  - audiences:senior-developers
  - audiences:developers
  - audiences:architects
---
<!-- course: model_context_protocol_and_agent_interop -->
# Model Context Protocol and Agent Interoperability

## Description
The Model Context Protocol (`MCP`), introduced by `Anthropic` in late 2024 and rapidly adopted, is the
emerging standard for how `LLM` applications expose tools, resources, and prompts to model clients in a
language-and-vendor-neutral way. Around it, a small ecosystem of related interop standards has grown
(`OpenAI`'s tool-call and `Responses` `API`, `Google`'s `Agent2Agent` protocol, the `LangChain` and
`LlamaIndex` adapters). The catalog covers `LLM Application Engineering`, `Agentic Systems
Engineering`, and ``AI` Agents Development`. None of those is the focused course on the protocols that
`let` agents and tools interoperate across vendors.

This two day course covers `MCP` and the broader agent-interop landscape from a developer's perspective.
It covers the `MCP` architecture (host, client, server, transport), the resource/tool/prompt primitives,
the security model, the canonical server implementations (`filesystem`, `Postgres`, `GitHub`, `Slack`),
the canonical clients (`Claude` Desktop, `Claude` Code, `Cursor`, `VS Code`), the relationship to
`OpenAI` `function-calling` and the `Responses API`, the `Agent2Agent` protocol for agent-to-agent
communication, the practical question of building an `MCP` server, the practical question of building
an `MCP` host, the security considerations (the `MCP` server has the trust of the client), and the
patterns that are emerging. Examples include real `MCP` servers and real cross-vendor integrations.
Participants leave able to build an `MCP` server, integrate one into a host, and reason about
agent-interop choices.

## Duration
16 hours / 2 days

## Intended Audience
* `ML` engineers building agent-tool integrations
* senior developers exposing systems to `LLMs`
* developers integrating `MCP` servers into their products
* architects evaluating agent-interop standards

## Prerequisites
* practical experience calling at least one `LLM` `API` from code
* exposure to the `LLM Application Engineering` course
* working knowledge of `Python` or `TypeScript`
* familiarity with `JSON-RPC` is helpful

## Objectives
* explain the `MCP` architecture and its primitives
* build an `MCP` server in `Python` or `TypeScript`
* integrate an `MCP` server into a host
* reason about the security boundary
* compare `MCP` to `OpenAI` `Responses API` and `Agent2Agent`
* recognize the patterns that work and the ones that do not

## Outline
<!-- chapter: what-mcp-actually-is, duration: 1h -->
* What `MCP` actually is
    * the open-protocol idea
    * client, host, server, transport
    * `JSON-RPC` over `stdio` or `HTTP`
    * cross-reference to the `LLM Application Engineering` course
    * who is using it and why
<!-- chapter: the-mcp-primitives, duration: 2h -->
* The `MCP` primitives
    * `Tools`: functions the model can call
    * `Resources`: data the model can read
    * `Prompts`: templates the host can offer
    * `Sampling`: model calls back to the host
    * `Roots` and `Logging`
    * picking the right primitive
<!-- chapter: building-an-mcp-server-python, duration: 3h -->
* Building an `MCP` server in `Python`
    * the `mcp` `Python` `SDK`
    * declaring tools and resources
    * `stdio` vs `HTTP` transport
    * testing the server with `Claude` Desktop
    * publishing the server
<!-- chapter: building-an-mcp-server-typescript, duration: 2h -->
* Building an `MCP` server in `TypeScript`
    * the `mcp` `TypeScript` `SDK`
    * differences from the `Python` `SDK`
    * deployment as a `Node` process
    * the testing flow
    * worked example
<!-- chapter: canonical-mcp-servers, duration: 1h -->
* Canonical `MCP` servers
    * the `filesystem` server
    * the `Postgres` server
    * the `GitHub` server
    * the `Slack` server
    * the open-source server registry
<!-- chapter: integrating-mcp-into-a-host, duration: 2h -->
* Integrating `MCP` into a host
    * connecting to a server
    * advertising the server's tools to the model
    * handling the tool-call response
    * the multi-server case
    * the "we connected to a server and it broke our agent" failure
<!-- chapter: mcp-security, duration: 2h -->
* `MCP` security
    * the server has the trust of the client
    * the prompt-injection-via-resource attack
    * the credential-exfiltration risk
    * `Anthropic`'s `MCP` security guidance
    * cross-reference to the Working with `LLMs` Securely course
    * the "we installed a malicious `MCP` server" disaster
<!-- chapter: comparing-with-openai-responses, duration: 1h -->
* Comparing with `OpenAI` `Responses API`
    * `OpenAI`'s tool-calling model
    * the `Responses API` and the `Assistants API`
    * the connector ecosystem
    * the differences from `MCP`
    * picking
<!-- chapter: agent-to-agent-protocols, duration: 1h -->
* Agent-to-agent protocols
    * `Google`'s `A2A` protocol
    * `LangGraph`'s agent communication
    * the not-yet-standard nature of this space
    * the "we built our own protocol" reality
    * the future of agent interop
<!-- chapter: patterns-and-anti-patterns, duration: 1h -->
* Patterns and anti-patterns
    * the small-tool, single-purpose `MCP` server
    * the "we crammed everything into one server" anti-pattern
    * the per-customer credential-isolation pattern
    * the dynamic-tool-discovery pattern
    * the read-only-by-default pattern

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
