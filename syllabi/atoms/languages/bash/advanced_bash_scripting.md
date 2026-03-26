---
tags:
  - bash
  - scripting
  - linux
  - automation
level: advanced
category: language
duration_days: 5
audience:
  - developers
  - devops
  - sysadmins
---
# Advanced `Bash` Scripting

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This advanced course is designed for engineers, `DevOps` professionals, and system administrators with strong `Bash` scripting experience. The course covers sophisticated `Bash` scripting techniques, performance optimization, error handling mastery, and integration with modern tools and `APIs`. Students will learn to write enterprise-grade scripts that are maintainable, efficient, and production-ready.

## Duration
40 hours / 5 days

## Intended Audience
* Engineers/DevOps professionals
* System Administrators with strong `Bash` scripting experience
* Graduates of Course 871 or equivalent

## Prerequisites
* Proficient in `Bash` scripting
* Strong knowledge of regular expressions
* Experience with `Linux` command-line utilities

## Objectives
Upon completion, delegates will be able to:
* Write advanced `Bash` scripts using sophisticated techniques like arrays, parameter expansion, and process substitution
* Implement robust error handling and debugging strategies in production scripts
* Optimize script performance and avoid common pitfalls
* Create modular, reusable code using functions and libraries
* Master advanced text processing with sed, awk, jq, and yq
* Automate complex workflows and integrate `Bash` with external tools and `APIs`
* Develop enterprise-grade scripts suitable for production environments

## Exercises
* Building a backup & restore automation tool
* Creating a log monitoring and alerting system
* Writing a deployment automation script
* Developing a CLI utility for `REST` `API` interaction

## Outline
* Advanced `Bash` Scripting Techniques
    * Recap: Key `Bash` features (brief refresher)
    * Arrays (Indexed and Associative)
    * Advanced parameter expansion
        * String manipulation
        * Default values
        * Error handling
        * Substring extraction
    * Indirect references and dynamic variable names
    * Process substitution (`<(...)` and `>(...)`)
    * Brace expansion advanced uses
* Shell Functions and Libraries
    * Writing modular and reusable `Bash` code
    * Functions with local variables
    * Returning values from functions
    * Creating and using `Bash` libraries
    * Source (.) and environment inheritance
* Error Handling & Debugging Mastery
    * Trap and handle signals (trap, ERR, EXIT)
    * Advanced exit codes and error propagation
    * Strict mode: `set -euo pipefail`
    * Using `bash -x`, `set -v`, and PS4 debugging
    * Logging strategies for scripts
    * Unit testing `Bash` scripts (using bats or shunit2)
* Performance & Optimization
    * Profiling scripts (using time, strace, and bash -x)
    * Avoiding common pitfalls (forking, subshells, I/O bottlenecks)
    * Using built-in `Bash` features vs external commands for efficiency
    * Handling large files and streams effectively
* Advanced Text Processing
    * Mastering sed and awk (beyond basics)
        * Multi-line editing
        * Complex pattern matching
        * Awk scripting (control structures, functions, arrays)
    * jq for `JSON` parsing
    * yq for `YAML` parsing
    * Combining tools in pipelines (jq+awk+sed)
* `Bash` Automation Patterns
    * Scheduling and automation (cron, at, systemd timers)
    * Writing daemon-like scripts
    * Interactive and non-interactive scripts
    * Handling user input securely
    * Using expect for automating interactive programs
* Integrating `Bash` with Other Tools
    * Calling `REST` `APIs` with curl and parsing `JSON`
    * `SSH` automation and remote script execution
    * Combining `Bash` with `Python` or Perl
    * Writing CLI tools with getopt/argparse

## References
* [`Bash` Manual](https://www.gnu.org/software/bash/manual/)
* [Advanced `Bash`-Scripting Guide](https://tldp.org/LDP/abs/html/)
* [jq Manual](https://stedolan.github.io/jq/manual/)
* [Bats: `Bash` Automated Testing System](https://github.com/bats-core/bats-core)
* [shunit2 Testing Framework](https://github.com/kward/shunit2)
* [systemd Timers](https://www.freedesktop.org/software/systemd/man/systemd.timer.html)
