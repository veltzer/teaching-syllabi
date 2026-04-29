---
tags:
  - concepts:architecture
  - concepts:api
  - concepts:distributed-systems
  - concepts:best-practices
level: intermediate
category: architecture
duration_hours: 16
audience:
  - audiences:senior-developers
  - audiences:developers
  - audiences:architects
  - audiences:team-leads
---
<!-- course: webhooks_engineering -->
# Webhooks Engineering

## Description
Webhooks are how a `SaaS` product tells its customers that something happened. They look like a small
detail and they are not. The catalog covers `API` design, `API` gateways, message queues, event-driven
architecture, and idempotency, but does not cover the specific engineering of producing and consuming
webhooks. A bad webhook system is one of the `top` reasons enterprise customers churn from a `SaaS`
product. A bad webhook consumer is one of the `top` reasons production systems get stuck behind a queue
of redeliveries.

This two day course covers webhooks from both sides: the producer (`Stripe`, `GitHub`, `Slack` are the
gold standards) and the consumer (the customer integrating with one of those). It covers the reliability
contract (at-least-once with retries), the security contract (signing, replay protection, secret
rotation), the delivery model (synchronous-from-an-event vs queued-and-delivered), the customer-facing
features (event filters, replay, dead-letter queues), the consumer-side patterns (idempotent handlers,
verification, backpressure), the observability story for both sides, and the failure modes (the
customer that goes silent, the producer that delivers a million events at once, the secret that
leaked). Examples are drawn from `Stripe`'s, `GitHub`'s, and `Slack`'s webhook systems and the
documented engineering posts about building them. Participants leave able to design either side of a
webhook system.

## Duration
16 hours / 2 days

## Intended Audience
* senior developers building a `SaaS` webhook system
* developers integrating with a third-party webhook
* architects designing event-out interfaces
* team leads accountable for an `API` product

## Prerequisites
* working experience with `HTTP` `APIs`
* exposure to the `API` Design Best Practices course
* familiarity with the Idempotency course is helpful
* basic understanding of message queues

## Objectives
* design a webhook system end-to-end
* secure webhooks with signing and replay protection
* implement reliable delivery with retries
* build a consumer that survives the producer's worst day
* operate webhooks in production
* recognize the failure modes
* compare webhooks to alternatives (`SSE`, polling, queues)

## Outline
<!-- chapter: what-a-webhook-actually-is, duration: 1h -->
* What a webhook actually is
    * a `POST` from the producer to the consumer's `URL`
    * the difference from polling
    * the difference from message queues
    * the difference from `SSE` and `WebSocket`
    * cross-reference to the `WebSocket` Programming course
<!-- chapter: the-delivery-contract, duration: 2h -->
* The delivery contract
    * at-least-once is the practical reality
    * the retry policy
    * the back-off curve
    * the timeout for the consumer
    * the giveup-and-park policy
<!-- chapter: webhook-security, duration: 2h -->
* Webhook security
    * `HMAC`-signed payloads
    * the `Stripe-Signature` header pattern
    * timestamp-bound signing for replay protection
    * the secret-rotation procedure
    * cross-reference to the Cryptographic Engineering course
    * the "we used the same secret for every customer" failure
<!-- chapter: producer-side-architecture, duration: 2h -->
* Producer-side architecture
    * the event source
    * the per-customer webhook configuration
    * the delivery worker pool
    * the per-customer queue
    * the "one slow customer blocked the whole pool" failure
<!-- chapter: customer-facing-features, duration: 2h -->
* Customer-facing features
    * event filters
    * replay of past events
    * the dead-letter queue
    * the per-event delivery log
    * the "we did not log it and the customer asked us to prove it" disaster
<!-- chapter: consumer-side-patterns, duration: 2h -->
* Consumer-side patterns
    * verify first, then process
    * the idempotent handler
    * cross-reference to the Idempotency and Distributed Consistency course
    * the queue-on-receipt pattern
    * the "we processed inline, timed out, and got the event 100 times" failure
<!-- chapter: scale-and-fan-out, duration: 1h -->
* Scale and fan-out
    * a million events at once
    * the per-customer rate limit
    * cross-reference to the `API` Rate Limiting and Quota Systems course
    * the "we sent everything in 30 seconds and crashed every customer" reality
    * back-pressure from the consumer
<!-- chapter: observability-of-webhooks, duration: 1h -->
* Observability of webhooks
    * delivery success rate
    * delivery latency
    * per-customer health
    * the "the customer's endpoint has been failing for a week" alert
    * the consumer-side observability
<!-- chapter: testing-webhooks, duration: 1h -->
* Testing webhooks
    * `ngrok`, `Smee.io`, `webhook.site`
    * the test-event endpoint
    * the staging environment of a producer
    * the contract test for webhooks
    * cross-reference to the Contract Testing course
<!-- chapter: alternatives-to-webhooks, duration: 1h -->
* Alternatives to webhooks
    * `polling` for the simple case
    * `SSE` and `WebSocket` for the live case
    * `EventBridge`-style event buses for the in-cloud case
    * the customer-pulls-from-our-queue pattern
    * picking among them
<!-- chapter: case-studies, duration: 1h -->
* Case studies
    * `Stripe` webhooks walkthrough
    * `GitHub` webhooks walkthrough
    * `Slack` events `API` walkthrough
    * the design choices each made
    * recommended reading: `Stripe` engineering blog, `Webhooks.fyi`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
