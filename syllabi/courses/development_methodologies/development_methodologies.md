---
tags:
  - practices:methodology
  - practices:productivity
  - concepts:best-practices
level: intermediate
category: methodology
duration_hours: 24
audience:
  - audiences:developers
  - audiences:managers
  - audiences:testers
---
<!-- course: development_methodologies -->
# Development Methodologies from the professionals

## Description
Ever wonder why there is one developer who can do the work of 5 others? What do they know that you don't?
This one day course is all about those things that you don't want to hear but which will `make` you a better
developer and your development environment more productive.

## Duration
24 hours (1 day)

## Intended Audience
* Anyone doing development
* Programmers, QA people, team leaders, managers.

## Prerequisites
* Some development background

## Objectives
* understand the core concepts and principles of Development Methodologies from the professionals
* gain practical knowledge of Script everything
* gain practical knowledge of Writing code
* gain practical knowledge of Documentation

## Outline
<!-- chapter: script-everything, duration: 1h -->
* Script everything
    * This means even things you do once every year
    * The practice will `make` you better at it
    * Use templating engines to tie systems together.
    * Use secrets storage solutions to not put secrets in your code.
<!-- chapter: writing-code, duration: 2h -->
* Writing code
    * Reward developers who remove code more than those who add code
    * Avoid "it's working so don't touch it" attitude
    * Allow developers to rebuild everything, fast!
    * Reward developers who manage to redesign your code - they are the true heroes.
    * Agile works, rewriting doesn't.
    * Keep it simple, Stupid! (your codes architecture that is).
    * Use simple text or MD drawings to document your systems, avoid GUI tools.
    * Have good taste.
    * Lint with tons of tools. Don't allow any unlinted code in.
<!-- chapter: documentation, duration: 1h -->
* Documentation
    * Don't use fancy tools, use text tools
    * Use `git` to maintain the docs.
    * Document the hard parts in your code, don't document the simple
    * Must be accurate
    * Must be fast
<!-- chapter: debugging, duration: 1h -->
* Debugging
    * [do not use a debugger](`https`://lemire.me/blog/2016/06/21/i-do-not-use-a-debugger/)
    * Heisenbugs.
    * Alternatives to debugging
        * reading your code
        * infrastructure for visibility
        * configurable logging
    * Debugging cycles should be fast (see building your code fast above).
<!-- chapter: do-not-use-user-interfaces, duration: 1h -->
* Do not use user interfaces
    * Not reproducible
    * Not scriptable
    * Always changing
    * GUI pull you to manual instead of automatic work
    * Don't let fancy GUI tempt you to the dark side, the fancier the worst it is
    * Disable GUI whenever you can
<!-- chapter: do-not-write-code-which-is-not-your-main-business, duration: 1h -->
* Do not write code which is not your main business
    * You are not good at it
    * You don't want to maintain it
    * Get open source alternatives or any other alternative
    * Anything which is not your main business should be open sourced
<!-- chapter: your-development-environment, duration: 1h -->
* Your development environment
    * Keep yourself `agile` regarding your tools
    * Use as few tools as possible
    * Be sure about why you use all of these tools
    * Drop tools you no longer need to simplify your environment.
    * Allow developers to enter password or MFA easily and keep security out of their way
    * Dump as much as possible on automated cloud services
    * Keep it simple, Stupid! (your development environment, that is)
<!-- chapter: configuring-software-that-you-use, duration: 1h -->
* Configuring software that you use:
    * Why keeping the default configuration is the best
    * If you can't use the default, change the configuration as little as possible.
    * Make sure your entire team uses the same configuration
    * Keep it simple, Stupid! (your configuration that is)
<!-- chapter: allowing-to-run-your-software-in-many-ways, duration: 1h -->
* Allowing to run your software in many ways
    * Allow to run it as library
    * Allow to run as command line tool
    * Allow auto-completion on the command line
    * Allow to override any option with environment variables.
    * Allow configuration files: per user, per system
    * Always follow convention over configuration
<!-- chapter: separate-systems-that-should-be-separate, duration: 1h -->
* Separate systems that should be separate
    * Prefer multi-process to multi-thread
    * Micro-services
    * Different code repos
    * Everything in computing is about separation.
<!-- chapter: zero-aural-traditions, duration: 1h -->
* Zero aural traditions
    * No special URLs, users, passwords, tools, that people need to gather: everything in one clear page.
    * The test of building and running your code from `git`
    * Script bootstrapping your code
    * Script installing all dependencies
    * Script everything!
<!-- chapter: proper-logging, duration: 1h -->
* Proper logging
    * Every tool you run should be run quietly, and if the tool does not know how to be quiet, teach it.
    * Long log files in the command line or from `CI/CD` are from the devil.
    * Make it easy to see more info when you need to.
    * Warnings should not be shown either because every warning should be treated as error.
<!-- chapter: test-test-test, duration: 1h -->
* Test, test, test
    * Test especially the things which failed in the past
    * Developers should write tests, not QA people. Fire them!
    * Reward new tests which pass, never settle for failing tests.
<!-- chapter: microservices, duration: 1h -->
* `Microservices`
    * You are doing it wrong
    * The most important part of Micro-services is that they are **Independently Deployable**.
<!-- chapter: stop-using-ms-windows, duration: 1h -->
* Stop using MS-`Windows`!
    * Why `Linux` is better for developers and facilitates all of the above
    * Why using `windows` is making your developers bad developers.
<!-- chapter: philosophy-is-more-important-than-practical-knowledge, duration: 1h -->
* Philosophy is more important than practical knowledge
    * Don't remember all the details, you'll never remember them anyway.
    * Being able to explain why you are using every tool you are using
    * `When` studying tools, learn their philosophy
    * `When` using each tool check if you are using it according to it's philosophy
    * Avoid abusing tools - meaning stop using them against their philosophy or not in line with it.
<!-- chapter: when-to-use-outside-help-or-consultants, duration: 1h -->
* `When` to use outside help or consultants
    * `When` you are afraid to do it yourself
    * `When` you are using a new technology and you have no in-house people
<!-- chapter: when-not-to-use-outside-help-or-consultants, duration: 1h -->
* `When` not to use outside help or consultants
    * `When` it has to do with your core business
    * `When` you should have people that know this shit
<!-- chapter: how-to-use-your-browser-correctly, duration: 1h -->
* How to use your browser correctly
    * Never use too many tabs
    * Always use bookmarks to your favorite places, this is a tricky art.
<!-- chapter: how-to-use-docker-correctly, duration: 1h -->
* How to use `Docker` correctly
    * Always use one `Docker` image! that's the whole point of `Docker`!
    * Don't abuse the technology.
<!-- chapter: fail-often-fail-soon, duration: 1h -->
* Fail often, fail soon
    * Why fast failure is better than slow failure
    * How to structure your systems for early failure detection
<!-- chapter: focus-focus-focus, duration: 1h -->
* Focus, focus, focus
    * Avoid context switching
    * Reduce distractions in your development workflow
<!-- chapter: basic-engineering-principles, duration: 1h -->
* Basic engineering principles
    * Isolation
    * Redundancy
    * Simplicity

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
