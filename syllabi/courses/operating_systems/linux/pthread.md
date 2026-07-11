---
tags:
  - infrastructure:linux
  - linuxkernel:pthreads
  - concepts:multithreading
  - concepts:concurrency
  - concepts:synchronization
  - practices:debugging
  - languages:c
level: intermediate
category: operating-systems
duration_hours: 24
audience:
  - audiences:developers
  - audiences:devops
---
<!-- course: pthread -->
# Pthreads course

## Description
An in depth course looking at working with the `Linux` pthread library.
The course covers the entire life cycle of a thread, the synchronization
primitives available to it, the memory model that governs what threads
may and may not observe of each other, and the tools used to debug
concurrent code, which is where most of the real difficulty lies.

## Duration
24 hours / 3 days

## Intended Audience
* software developers working on `Linux`-based systems
* system administrators and `DevOps` engineers

## Prerequisites
* knowledge in basic `UNIX` systems programming (`Linux` Fundamentals or equivalent experience).
* hands on familiarity with command line writing, compiling running and debugging on `Linux` and/or `UNIX`.

## Objectives
* understand the `Linux` `threading` model and how it differs from the classic `UNIX` process model
* create, join, detach and cancel threads correctly
* choose the right synchronization primitive (`mutex`, condition variable, `rwlock`, spinlock, barrier, semaphore) for a given problem
* diagnose data races, deadlocks and lost wakeups
* handle signals correctly in a multithreaded program
* control thread stacks, `cpu` affinity and scheduling

## Outline
<!-- chapter: the-linux-threading-model, duration: 1h -->
* the `Linux` `threading` model.
    * the fork `API`
    * the clone `API`
    * threads as scheduling entities sharing an address space
<!-- chapter: creating-threads, duration: 2h -->
* creating threads
    * `pthread_create(3)`
    * the start routine signature and what it may return
    * passing arguments to a thread and getting results back
    * the classic bug: passing the address of a loop variable
    * thread attributes: `pthread_attr_t`
    * compiling and linking with `-pthread`
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
<!-- chapter: thread-termination-and-joining, duration: 1h -->
* thread termination and joining
    * returning from the start routine
    * `pthread_exit(3)`
    * joining a thread and collecting its return value.
    * detaching a thread so it can't be joined.
<!-- chapter: thread-cancellation, duration: 2h -->
* thread cancellation
    * `pthread_cancel(3)`
    * cancellation points
    * `pthread_setcancelstate(3)`, `pthread_setcanceltype(3)`
    * deferred versus asynchronous cancellation.
    * masking cancellation.
    * cleanup function registrations at thread death.
    * why cancellation is hard to get right
<!-- chapter: threads-synchronization-mechanisms, duration: 4h -->
* threads synchronization mechanisms:
    * mutexes
        * how they are implemented: the `futex(2)` system call and the fast uncontended path
        * `mutex` types: normal, recursive, errorcheck
        * `mutex` attributes
    * condition variables
        * why a condition variable always travels with a `mutex`
        * the mandatory predicate loop: always wait in a `while-loop`
        * spurious wakeups
        * lost wakeups
        * signal versus broadcast
    * semaphores
        * `sem_t`, `sem_init(3)`, `sem_wait(3)`, `sem_post(3)`
        * when a semaphore beats a `mutex` plus a condition variable
    * `rwlocks`.
    * spinlocks.
        * when a spinlock is actually appropriate
    * barriers
    * deadlock avoidance and lock ordering
    * priority inversion
<!-- chapter: the-memory-model-and-atomics, duration: 2h -->
* the memory model and atomics
    * what a data race is and why it is undefined behavior
    * the `C11` memory model
    * atomics
    * why `volatile` is not a synchronization mechanism
    * memory ordering
    * why lock free programming is hard
<!-- chapter: debugging-threaded-code, duration: 2h -->
* debugging threaded code
    * `ThreadSanitizer`
    * `valgrind` and `helgrind`
    * threads in `gdb`: info threads, thread apply all bt
    * diagnosing a deadlock from a stuck process
    * why concurrency bugs do not reproduce
<!-- chapter: tls-thread-local-storage, duration: 1h -->
* `TLS` (thread local storage).
    * the pthread way.
    * the `C++` way.
    * other options
<!-- chapter: threads-and-signals, duration: 2h -->
* threads and signals.
    * sending signals to threads.
    * `pthread_kill(3)`
    * what happens when a signal arrives at a thread?
    * signal queues for real time signals.
    * masking signals.
    * `pthread_sigmask(3)` and the dedicated signal handling thread pattern
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
    * `pthread_atfork(3)` hooks
    * `pthread_once(3)`
    * what happens when a thread calls `execve(2)`? all other threads are terminated
        silently; the calling thread survives as the sole thread of the new image
        and takes over the thread group leader's `pid`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
