---
tags:
  - languages:c
  - security:security
  - security:secure-coding
level: intermediate
category: language
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: c_secure_coding -->
# Coding securely in C

## Description
This course was designed for users of the `clang` tool-chain.
For `GCC` modifications need to be made.

## Duration
24 hours / 3 days

## Intended Audience
* C programmers
* embedded and systems software developers

## Prerequisites
* `solid` experience with C programming

## Objectives
* understand the core concepts and principles of Coding securely in C
* gain practical knowledge of Motivation for Secure Programming
* gain practical knowledge of Machine-Level Representation of C programs
* gain practical knowledge of Integer security

## Outline
<!-- chapter: motivation-for-secure-programming, duration: 1h -->
* Motivation for Secure Programming
    * In User Space/Kernel Space systems
    * In Monolithic systems
<!-- chapter: machine-level-representation-of-c-programs, duration: 1h -->
* Machine-Level Representation of C programs
    * Tour of `Assembly` Language
<!-- chapter: integer-security, duration: 2h -->
* Integer security
    * `Int` / Double overflows
    * Integer conversion rules
    * Signed and unsigned problems
    * Safe integer usage
    * Enforcing limits on integer values
    * Preventing lost or misinterpreted data due to conversion
    * Using secure integer libraries
<!-- chapter: strings-and-buffers, duration: 1h -->
* Strings and Buffers
    * Formatting vulnerabilities
    * Better ways to manipulate strings and buffers
    * Using the 'n' functions correctly
<!-- chapter: stack-based-buffer-overflow, duration: 2h -->
* Stack-based Buffer Overflow
    * Function calls and Stack Layout
    * Representation of buffers at the `assembly` level
    * Smashing the stack
    * Stack guards
    * Extra parameters
    * Isolating stacks of threads
    * Stack layout of variadic functions
<!-- chapter: data-pointer-and-function-pointer-vulnerabilities, duration: 1h -->
* Data Pointer and Function Pointer Vulnerabilities
    * Smashing the stack by exploiting pointers
    * Dynamic memory allocation and security
<!-- chapter: advanced-buffer-overflow-attacks, duration: 1h -->
* Advanced Buffer Overflow Attacks
    * By-passing non-executable stack
    * Jumping to EAX, ESP, and EMP exploit
<!-- chapter: other-attacks, duration: 1h -->
* Other attacks
    * Heap overflow attacks
    * `Array` indexing attacks
<!-- chapter: linking, duration: 1h -->
* Linking
    * Load-time exploitation
    * Basics of static and dynamic linking
    * Load time randomization
<!-- chapter: file-i-o-security, duration: 1h -->
* `File` `I/O` Security
    * Path Traversal Vulnerabilities
    * `File` `I/O` Race Conditions
<!-- chapter: concurrency, duration: 1h -->
* Concurrency
    * Multi threads
    * Deadlock and vulnerabilities
<!-- chapter: cpu-vulnerabilities, duration: 1h -->
* `CPU` vulnerabilities
    * Spectre and meltdown analysis
<!-- chapter: general-protection-mechanisms, duration: 1h -->
* General protection mechanisms
    * Parameter checking
    * Stack checking
    * Writing generic layers of protection
<!-- chapter: clang-tool-chain, duration: 1h -->
* `Clang` tool-chain
    * Compiler checks
    * Compiler randomization
<!-- chapter: secure-memory-usage, duration: 3h -->
* Secure Memory Usage
    * Secure memory handling
    * Erasing Data
    * Secure pointer usage
    * Memory Dumps
    * Use smart pointers for resource management
    * Ensure pointer arithmetic
    * Avoid null pointer de-referencing
    * Ensure sensitive data is not paged to disk
<!-- chapter: safe-apis, duration: 3h -->
* Safe APIs
    * Dangerous and banned APIs
    * Real-World Risks
    * Using safe APIs
    * The "n" Functions
    * Detecting Dangerous APIs
    * Alternatives
    * StrSafe
<!-- chapter: secure-file-handling, duration: 2h -->
* Secure `File` Handling
    * Directory Traversal attacks
    * `File` canonicalization attacks
    * Creating files with correct `ACLs`
    * Ensure files are closed when no longer needed
    * Insecure usage of shared directories

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
