---
tags:
  - linux
  - pthreads
  - multithreading
  - synchronization
  - c
level: intermediate
category: operating-systems
duration_days: 2
audience:
  - developers
---
# Pthreads course

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
An in depth course looking at working with the `Linux` `pthread` library.

## Duration
16 hours / 2 days

## Intended Audience
* software developers working on Linux-based systems
* system administrators and DevOps engineers

## Prerequisites
* knowledge in basic `UNIX` systems programming.
* hands on familiarity with command line writing, compiling running and debugging on `Linux` and/or `UNIX`.

## Objectives
* understand the core concepts and principles of Pthreads course
* gain practical knowledge of the `Linux` threading model.
* gain practical knowledge of your very first thread.
* gain practical knowledge of seeing thread information on the command line.

## Outline
* the `Linux` threading model.
    * the fork `API`
    * the clone `API`
* your very first thread.
* seeing thread information on the command line.
    * using ps
    * using top
    * using /proc
* thread ids
    * why are there two ids
    * `pthread_self(3)`, `pthread_equal(3)`
    * `gettid(2)`
    * giving names to threads
        `pthread_setname_np(3)`
        `prctl(2)`
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
* `TLS` (thread local storage).
    * the `pthread` way.
    * the C++ way.
    * other options
* threads and signals.
    * sending signals to threads.
    * what happens when a signal arrives at a thread?
    * signal queues for real time signals.
    * masking signals.
* threads synchronization mechanisms:
    * barriers
    * conditions.
    * mutexes (futexes)
    * spinlocks.
    * rwlocks.
* threads and cores
    * knowing on which core you are running.
    * cpu affinity.
        at thread creation time.
        using taskset.
    * yielding the CPU.
    * scheduling classes and priorities.
* threads and time
    * sleeping in threads.
    * pausing in threads.
    * a thread cpu clock.
    * setting the thread cpu clock
* inter-thread communication options.
    * simple implementation of a message queue.
* stacks of threads.
    * controlling the sizes of stacks
    * stack guards
    * knowing if you are close to the edge.
* misc
    * ASLR and how it effects threads.
    * `thread_at_fork` hooks
    * `pthread_once`
    * what happens when a thread does execve? answer: all threads die automatically

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
