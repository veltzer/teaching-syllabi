---
tags:
  - concepts:architecture
  - data-and-ai:message-queues
  - concepts:scalability
level: intermediate
category: architecture
duration_hours: 8
audience:
  - audiences:architects
  - audiences:developers
---
<!-- course: message_queues -->
# Message Queues

## Description
Message queues are arguably the most important tool in a software architects toolbox. Sadly though they
are not discussed seriously enough in architecting classes and software development courses.
This lecture is intended to fill some knowledge gap and explain when you should use this tool, when you
should not, and what Message Queue features would be of interest to an architect when designing a
scalable, durable and efficient system.

## Duration
1 hour

## Intended Audience
* software architects and senior developers
* technical leads making design decisions

## Prerequisites
* several years of software development experience

## Objectives
* understand the core concepts and principles of Message Queues
* gain practical knowledge of when to use a message queue from an architecture perspective
* gain practical knowledge of basic message queue features
* gain practical knowledge of features of message queues

## Outline
<!-- chapter: when-to-use-a-message-queue-from-an-architecture-perspective, duration: 1h -->
* when to use a message queue from an architecture perspective
    * mq vs `API` vs other queue like features (internet of things messaging)
    * mq across k8s
<!-- chapter: basic-message-queue-features, duration: 2h -->
* basic message queue features
    * one to one
    * one to many
    * one to group
    * pub/sub
    * streaming
    * size of message
<!-- chapter: features-of-message-queues, duration: 4h -->
* features of message queues
    * at least one delivery
        * invisibility timeout
        * extending timeout
    * exactly one delivery
    * dead letter queue
    * ordered delivery
    * persistence
    * durability of the queue
    * scalability of the queue
<!-- chapter: comparison-of-different-alternatives, duration: 1h -->
* comparison of different alternatives:
    * `Kafka`, `ActiveMQ`, `RabbitMQ`, Pulsar, `Azure` queues.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
