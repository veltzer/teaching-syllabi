---
tags:
  - architecture
  - message-queues
  - scalability
level: intermediate
category: architecture
duration_days: 1
audience:
  - architects
  - developers
---
# Message Queues

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
Message queues are arguably the most important tool in a software architects toolbox. Sadly though they
are not discussed seriously enough in architecting classes and software development courses.
This lecture is intended to fill some knowledge gap and explain when you should use this tool, when you
should not, and what Message Queue features would be of interest to an architect when designing a
scalable, durable and efficient system.

## Duration
1 hour

## Outline
* when to use a message queue from an architecture perspective
    * mq vs `API` vs other queue like features (internet of things messaging)
    * mq across `k8s`
* basic message queue features
    * one to one
    * one to many
    * one to group
    * pub/sub
    * streaming
    * size of message
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
* comparison of different alternatives:
    * `Kafka`, `ActiveMQ`, `RabbitMQ`, `Pulsar`, `Azure` queues.

## Copyright
Mark Veltzer, © 2026
