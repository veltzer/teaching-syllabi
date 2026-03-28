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
# Coding securely in C

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This course was designed for users of the clang tool-chain.
For `GCC` modifications need to be made.

## Duration
24 hours / 3 days

## Intended Audience
* C programmers
* embedded and systems software developers

## Prerequisites
* solid experience with C programming

## Objectives
* understand the core concepts and principles of Coding securely in C
* gain practical knowledge of Motivation for Secure Programming
* gain practical knowledge of Machine-Level Representation of C programs
* gain practical knowledge of Integer security

## Outline
* Motivation for Secure Programming
    * In User Space/Kernel Space systems
    * In Monolithic systems
* Machine-Level Representation of C programs
    * Tour of `Assembly` Language
* Integer security
    * Int / Double overflows
    * Integer conversion rules
    * Signed and unsigned problems
    * Safe integer usage
    * Enforcing limits on integer values
    * Preventing lost or misinterpreted data due to conversion
    * Using secure integer libraries
* Strings and Buffers
    * Formatting vulnerabilities
    * Better ways to manipulate strings and buffers
    * Using the 'n' functions correctly
* Stack-based Buffer Overflow
    * Function calls and Stack Layout
    * Representation of buffers at the assembly level
    * Smashing the stack
    * Stack guards
    * Extra parameters
    * Isolating stacks of threads
    * Stack layout of variadic functions
* Data Pointer and Function Pointer Vulnerabilities
    * Smashing the stack by exploiting pointers
    * Dynamic memory allocation and security
* Advanced Buffer Overflow Attacks
    * By-passing non-executable stack
    * Jumping to EAX, ESP, and EMP exploit
* Other attacks
    * Heap overflow attacks
    * Array indexing attacks
* Linking
    * Load-time exploitation
    * Basics of static and dynamic linking
    * Load time randomization
* File I/O Security
    * Path Traversal Vulnerabilities
    * File I/O Race Conditions
* Concurrency
    * Multi threads
    * Deadlock and vulnerabilities
* CPU vulnerabilities
    * Spectre and meltdown analysis
* General protection mechanisms
    * Parameter checking
    * Stack checking
    * Writing generic layers of protection
* Clang tool-chain
    * Compiler checks
    * Compiler randomization
* Secure Memory Usage
    * Secure memory handling
    * Erasing Data
    * Secure pointer usage
    * Memory Dumps
    * Use smart pointers for resource management
    * Ensure pointer arithmetic
    * Avoid null pointer de-referencing
    * Ensure sensitive data is not paged to disk
* Safe `APIs`
    * Dangerous and banned `APIs`
    * Real-World Risks
    * Using safe `APIs`
    * The "n" Functions
    * Detecting Dangerous `APIs`
    * Alternatives
    * StrSafe
* Secure File Handling
    * Directory Traversal attacks
    * File canonicalization attacks
    * Creating files with correct ACLs
    * Ensure files are closed when no longer needed
    * Insecure usage of shared directories

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
