---
tags:
  - infrastructure:linux
  - linuxkernel:pthreads
  - concepts:multithreading
  - concepts:synchronization
  - languages:c
level: intermediate
category: operating-systems
duration_hours: 16
audience:
  - audiences:developers
  - audiences:devops
---
<!-- course: pthread -->
# Pthreads course

## Description
An in depth course looking at working with the `Linux` pthread library.

## Duration
16 hours / 2 days

## Intended Audience
* software developers working on `Linux`-based systems
* system administrators and `DevOps` engineers

## Prerequisites
* knowledge in basic `UNIX` systems programming.
* hands on familiarity with command line writing, compiling running and debugging on `Linux` and/or `UNIX`.

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* understand the core concepts and principles of Pthreads course
* gain practical knowledge of the `Linux` `threading` model.
* gain practical knowledge of your very first thread.
* gain practical knowledge of seeing thread information on the command line.

## Outline
<!-- chapter: the-linux-threading-model, duration: 1h -->
* the `Linux` `threading` model.
    * the fork `API`
    * the clone `API`
<!-- chapter: your-very-first-thread, duration: 1h -->
* your very first thread.
<!-- chapter: seeing-thread-information-on-the-command-line, duration: 1h -->
* seeing thread information on the command line.
    * using ps
    * using top
    * using /proc
<!-- chapter: thread-ids, duration: 1h -->
* thread `ids`
    * why are there two `ids`
    * `pthread_self(3)`, `pthread_equal(3)`
    * `gettid(2)`
    * giving names to threads
        `pthread_setname_np(3)`
        `prctl(2)`
<!-- chapter: thread-death, duration: 3h -->
* thread death
    * suspending a thread.
    * `pthread_exit(3)`
    * `pthread_kill(3)`
    * `pthread_cancel(3)`
    * `pthread_setcancelstate(3)`, `pthread_setcanceltype(3)`
    * thread cancellation.
    * masking cancellation.
    * joining a thread.
    * detaching a thread so it can't be joined.
    * cleanup function registrations at thread death.
<!-- chapter: tls-thread-local-storage, duration: 1h -->
* `TLS` (thread local storage).
    * the pthread way.
    * the `C++` way.
    * other options
<!-- chapter: threads-and-signals, duration: 1h -->
* threads and signals.
    * sending signals to threads.
    * what happens when a signal arrives at a thread?
    * signal queues for real time signals.
    * masking signals.
<!-- chapter: threads-synchronization-mechanisms, duration: 2h -->
* threads synchronization mechanisms:
    * barriers
    * conditions.
    * mutexes (futexes)
    * spinlocks.
    * rwlocks.
<!-- chapter: threads-and-cores, duration: 1h -->
* threads and cores
    * knowing on which core you are running.
    * `cpu` affinity.
        at thread creation time.
        using taskset.
    * yielding the `CPU`.
    * scheduling classes and priorities.
<!-- chapter: threads-and-time, duration: 1h -->
* threads and time
    * sleeping in threads.
    * pausing in threads.
    * a thread `cpu` clock.
    * setting the thread `cpu` clock
<!-- chapter: inter-thread-communication-options, duration: 1h -->
* inter-thread communication options.
    * simple implementation of a message queue.
<!-- chapter: stacks-of-threads, duration: 1h -->
* stacks of threads.
    * controlling the sizes of stacks
    * stack guards
    * knowing if you are close to the edge.
<!-- chapter: misc, duration: 1h -->
* misc
    * `ASLR` and how it effects threads.
    * thread_at_fork hooks
    * pthread_once
    * what happens when a thread does execve? answer: all threads die automatically

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
