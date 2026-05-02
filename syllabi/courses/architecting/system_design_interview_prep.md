---
tags:
  - concepts:architecture
  - concepts:distributed-systems
  - concepts:scalability
  - concepts:databases
  - concepts:design-patterns
  - concepts:best-practices
level: intermediate
category: architecture
duration_hours: 40
audience:
  - audiences:senior-developers
  - audiences:developers
  - audiences:architects
---
<!-- course: system_design_interview_prep -->
# System Design Interview Prep

## Description
The system-design interview at top engineering organizations measures something specific: whether a candidate
can scope an under-defined problem, walk a tradeoff space credibly, and `make` decisions out loud under time
pressure. The general System Design course in the catalog is broader; this five day course is dedicated to
the interview as a focused performance.

The course covers the structure of a typical 45-to-60-minute interview, the framework for scoping and
estimating, the canonical problem walkthroughs (URL shortener, news feed, chat, rate limiter, ride-hailing,
distributed cache, search, recommendation, video streaming, payment), the anti-patterns that fail candidates
who otherwise know the material, and the deliberate-practice methodology for getting better. The course is
grounded in the public material from `Alex Xu`, `Donne Martin`, `Educative`, and the engineering blogs of
the companies that conduct these interviews.

## Duration
40 hours / 5 days

## Intended Audience
* senior developers preparing for staff/principal-level interviews
* developers preparing for senior-engineer interviews at top organizations
* engineers re-entering the job market after years in one role
* engineers giving these interviews who want to calibrate their bar

## Prerequisites
* several years of professional software development experience
* basic familiarity with `HTTP`, databases, caching and load balancing
* exposure to at least one distributed system in production
* working knowledge of the architectural-level material in the System Design course is helpful

## Objectives
* describe the structure and signal of a typical system-design interview
* scope an under-defined problem within the first five minutes
* perform capacity estimation honestly and quickly
* walk through the canonical problem set with confidence
* `make` tradeoffs out loud and defend them under push-back
* recognize and avoid the most common interview anti-patterns
* practice deliberately rather than re-watching solution videos

## Outline
<!-- chapter: what-the-interview-actually-measures, duration: 2h -->
* What the interview actually measures
    * the signals interviewers are calibrated to
    * scoping vs solving vs polishing
    * the difference between senior, staff and principal expectations
    * the rubric across `FAANG` and similar
    * what fails candidates who otherwise know the material
    * the value of "I do not know" said well
<!-- chapter: the-interview-framework, duration: 3h -->
* The interview framework
    * the four-phase structure: scope, estimate, design, drill-down
    * functional vs non-functional requirements
    * `SLO`-style requirement statements
    * back-of-envelope estimation
    * starting at the simplest design and adding complexity
    * the "I would do X first, then if needed Y" cadence
<!-- chapter: capacity-estimation, duration: 3h -->
* Capacity estimation
    * powers of two, powers of ten
    * `QPS`, storage, bandwidth in one minute
    * the "user" as the unit of estimation
    * peak vs average vs `p99`
    * the read-write ratio as a key driver
    * estimation that is honest vs estimation that is theater
<!-- chapter: the-design-toolbox, duration: 3h -->
* The design toolbox
    * load balancers, caches, queues, databases, blob stores, `CDN`
    * relational vs document vs key-value vs wide-column vs time-series
    * sync vs async patterns
    * push vs pull
    * the partial vocabulary every candidate should know
    * cross-reference to the Distributed Systems Tradeoffs course
<!-- chapter: scaling-fundamentals-for-the-interview, duration: 3h -->
* Scaling fundamentals for the interview
    * vertical vs horizontal scaling
    * stateless services and the database as the bottleneck
    * caching tiers
    * sharding and the partition key choice
    * replication for read-heavy workloads
    * `CDN` and edge for latency
    * cross-reference to the Load Balancing course
<!-- chapter: walkthrough-url-shortener, duration: 2h -->
* Walkthrough: `URL` shortener
    * scoping and estimation
    * key generation strategies
    * read-heavy design and cache hit ratio
    * analytics as a stretch
    * the variants the interviewer adds
<!-- chapter: walkthrough-news-feed, duration: 2h -->
* Walkthrough: news feed
    * fan-out-on-write vs fan-out-on-read vs hybrid
    * the celebrity problem
    * ranking as the next layer
    * the "what about edits" follow-up
    * push notifications as a sub-problem
<!-- chapter: walkthrough-chat-and-presence, duration: 2h -->
* Walkthrough: chat and presence
    * `WebSocket` vs polling
    * connection state and the chat-server fleet
    * message storage and the read receipt
    * presence service as its own design
    * group chat at scale
<!-- chapter: walkthrough-rate-limiter, duration: 2h -->
* Walkthrough: rate limiter
    * token bucket vs leaky bucket vs sliding window
    * distributed rate limiting state
    * fairness across tenants
    * the "where does it run" decision
    * cross-reference to the Load Balancing course
<!-- chapter: walkthrough-ride-hailing-or-delivery, duration: 2h -->
* Walkthrough: ride-hailing or delivery
    * geospatial indexing and the cell decomposition
    * the matchmaking design
    * driver location updates and write-throughput
    * the surge-pricing variant
    * eventual consistency in geo systems
<!-- chapter: walkthrough-distributed-cache, duration: 2h -->
* Walkthrough: distributed cache
    * consistent hashing
    * cache eviction policies
    * write-through vs write-back vs write-around
    * the cache-invalidation question that always shows up
    * `Memcached` vs `Redis` cluster
<!-- chapter: walkthrough-search-or-recommendation, duration: 2h -->
* Walkthrough: search or recommendation
    * inverted index design
    * the indexing pipeline
    * relevance and reranking layers
    * personalization features
    * the cold-start problem
<!-- chapter: walkthrough-video-streaming, duration: 2h -->
* Walkthrough: video streaming
    * upload, transcode, package
    * `CDN` and the edge story
    * adaptive bitrate
    * the "live streaming" variant
    * cross-reference to the Edge Computing course
<!-- chapter: walkthrough-payment-or-billing, duration: 2h -->
* Walkthrough: payment or billing
    * idempotency at the `API` boundary
    * the ledger-vs-state debate
    * the `saga pattern` across providers
    * the audit-and-reconcile loop
    * cross-reference to the Idempotency course
<!-- chapter: drill-down-questions-and-tradeoff-defense, duration: 2h -->
* Drill-down questions and tradeoff defense
    * the deep-dive into one component
    * "why did you choose X over Y"
    * the failure-mode question
    * the "what would change at 10x scale" question
    * the "what monitoring would you add" question
    * recovering from a wrong answer
<!-- chapter: anti-patterns-and-failure-modes, duration: 2h -->
* Anti-patterns and failure modes
    * the candidate who jumps to a solution
    * the candidate who lectures
    * the candidate who never picks
    * the candidate who name-drops without depth
    * the candidate who freezes on capacity math
    * the candidate who cannot write a single component in detail
    * how to recognize each in yourself
<!-- chapter: deliberate-practice-and-feedback, duration: 2h -->
* Deliberate practice and feedback
    * solo practice methodology
    * mock interview partners
    * recording and reviewing your own sessions
    * the difference between studying and practicing
    * resources: `Alex Xu`'s books, `Educative`, public engineering blogs
<!-- chapter: workshop-and-wrap-up, duration: 2h -->
* Workshop and wrap up
    * full mock interview with debrief
    * peer review of a designed system
    * recommended reading and continued practice plan

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
