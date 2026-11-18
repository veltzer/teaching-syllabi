---
tags:
  - data-and-ai:agents
  - data-and-ai:ai
  - data-and-ai:llm
  - data-and-ai:mcp
  - data-and-ai:tools
  - architecture:api-design
  - architecture:system-design
  - concepts:ui
  - concepts:web-development
  - practices:accessibility
  - practices:security
level: intermediate
category: ai
duration_minutes: 120
audience:
  - audiences:managers
  - audiences:team-leads
  - audiences:architects
  - audiences:developers
  - audiences:frontend-developers
  - audiences:product-managers
---

<!-- blurb: delete_your_frontend -->
# Delete Your Frontend: Nobody Wants to Learn Your Website

**A provocative technical leadership talk.** Menus, forms, wizards, and dashboards were a
workaround for computers that could not understand people. Now they can. What happens to the
site when the user can simply say what they want?

## The Challenge
Every screen in a web application is a small language the user has to learn: where the
feature lives, what the fields mean, which of the forty filters matters. Teams spend most of
their budget building and maintaining that language, and users spend their patience decoding
it - then call support anyway. A graphical interface forces the user to translate a goal into
clicks. An `LLM` with access to the same backend can do that translation for them. The hard
part is no longer the conversation; it is building a backend that a model can operate safely,
and knowing where a chat box is genuinely better and where it is a regression.

## What This Session Covers
A deliberately provocative, but practical, look at the conversational interface as a
replacement for the complicated site: why stating intent beats navigating, how to build the
chat front and the tool-based backend behind it, how to keep a model that acts on behalf of
users inside its permissions, and the honest list of cases where the old interface still wins.

## Agenda
* **The Provocation** (10 min): The graphical interface as a forty-year workaround; every menu is a question the user was forced to answer in the designer's vocabulary.
* **Why Intent Beats Navigation** (15 min): No learning curve, no discovery problem, one sentence instead of nine screens; what this does for occasional users, accessibility, and support load.
* **Anatomy of a Chat-First Product** (15 min): The conversation loop, the model, the tool layer, and the systems of record; what replaces the page, the route, and the form.
* **The Backend Is a Set of Tools** (20 min): Turning business operations into narrow, well-described, typed tools; `MCP` as the contract, and why a `CRUD` `API` built for screens makes a poor tool set.
* **Trust, Identity, and Guardrails** (20 min): The model acts with the user's permissions and never more; authorization enforced in the backend, confirmation before irreversible actions, prompt injection, and audit trails.
* **Not Only Text** (10 min): Answers rendered as tables, charts, forms, and buttons inside the conversation; generated interface on demand instead of designed screens in advance.
* **Where the Chatbot Loses** (10 min): Dense monitoring views, bulk editing, browsing without a goal, latency, cost per request, and the blank-prompt problem; when to keep the screen.
* **Getting There** (10 min): Putting a conversation in front of the existing `API`, measuring what users ask for, evaluating answers and actions, and retiring screens by evidence.
* **Debate and Q&A** (10 min): An open challenge to the audience - defend the screen you would never give up.

## Takeaways
* A clear argument for when a conversational interface is simpler for users than a site, and when it is not
* A reference architecture for a chat-first product: conversation loop, model, tools, and systems of record
* Practical rules for designing backend tools that an `LLM` can use correctly
* A security model in which the backend, not the model, enforces what each user may do
* An incremental path from an existing site to a conversational one

## Who Should Attend
* Engineering managers
* Tech leads
* Software architects
* Product managers
* Frontend and backend developers wondering what they will be building next year

## Continue the Journey
This talk challenges the old model. A follow-on, hands-on workshop can take one painful flow
in the team's own product, expose its backend as tools, and put a working conversational
interface in front of it.

## Speaker
Mark Veltzer
