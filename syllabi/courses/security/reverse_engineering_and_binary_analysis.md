---
tags:
  - security:security
  - security:penetration-testing
  - concepts:systems-programming
level: advanced
category: security
duration_hours: 40
audience:
  - audiences:security-professionals
  - audiences:testers
---
<!-- course: reverse_engineering_and_binary_analysis -->
# Reverse Engineering and Binary Analysis

## Description
This course provides an in-depth exploration of reverse engineering and binary analysis techniques used by security professionals. Participants will learn to analyze compiled binaries across multiple platforms, use industry-standard disassembly and debugging tools, and apply both static and dynamic analysis methodologies. The course covers anti-reverse engineering countermeasures, vulnerability discovery, exploit development fundamentals, and malware analysis workflows, culminating in hands-on CTF-style challenges.

## Duration
40 hours / 5 days

## Intended Audience
* Security researchers and analysts
* Penetration testers and red team operators
* Malware analysts and incident responders
* Software engineers working on security tooling
* Embedded systems engineers concerned with firmware security

## Prerequisites
* `Solid` understanding of operating system concepts (processes, memory management, `file` systems)
* Basic knowledge of `C` and `C++` programming
* Familiarity with command-line tools on `Linux` and `Windows`
* Understanding of computer architecture fundamentals (registers, stack, heap)
* Basic networking knowledge

## Required Knowledge
* `Linux` Fundamentals (or equivalent experience)

## Objectives
* Analyze binary formats including `ELF`, `PE`, and Mach-O structures
* Read and interpret `x86`/`x64` `assembly` code fluently
* Use disassemblers and decompilers such as `Ghidra`, IDA, and `Binary Ninja` effectively
* Apply static and dynamic analysis techniques to understand binary behavior
* Identify and defeat anti-reverse engineering protections including obfuscation and packing
* Discover vulnerabilities in compiled binaries and develop basic exploits
* Perform structured malware analysis using established methodologies
* Analyze firmware images and extract embedded components

## Outline
<!-- chapter: binary-formats-and-assembly-foundations, duration: 5h -->
* Binary Formats and `Assembly` Foundations
    * Overview of executable binary formats
    * `ELF` format structure: headers, sections, segments, and symbol tables
    * `PE` format structure: DOS header, `PE` header, sections, and import/export tables
    * Mach-O format structure and universal binaries
    * `x86`/`x64` `assembly` review: registers, calling conventions, and instruction set
    * Stack frames, function prologues, and epilogues
    * System calls and ABI conventions across platforms
<!-- chapter: disassembly-and-static-analysis, duration: 6h -->
* Disassembly and Static Analysis
    * Introduction to disassembly tools and workflows
    * Working with `Ghidra`: project setup, navigation, and analysis features
    * Working with IDA: interface, shortcuts, and plugin ecosystem
    * Working with `Binary Ninja`: `API`, intermediate representations, and automation
    * Control flow analysis: reconstructing program logic from `assembly`
    * Data flow analysis: tracking variable usage and data transformations
    * Cross-referencing, renaming, and annotating for comprehension
    * Decompilation techniques and limitations
    * Identifying compiler patterns and standard library functions
<!-- chapter: dynamic-analysis-and-debugging, duration: 6h -->
* Dynamic Analysis and Debugging
    * Dynamic analysis fundamentals and environment setup
    * Debugging with `GDB`: breakpoints, watchpoints, and scripting with `Python`
    * Tracing system calls with `strace` and library calls with `ltrace`
    * Runtime memory inspection and modification
    * Analyzing network behavior and `file` system interactions
    * Snapshot and diff analysis techniques
    * Using `QEMU` for cross-architecture analysis
    * Combining static and dynamic analysis for comprehensive understanding
<!-- chapter: anti-reverse-engineering-and-countermeasures, duration: 6h -->
* Anti-Reverse Engineering and Countermeasures
    * Code obfuscation techniques: control flow flattening, opaque predicates, and junk code
    * Packing and compression: common packers and their signatures
    * Anti-debugging techniques: timing checks, debugger detection, and integrity verification
    * Anti-disassembly tricks: overlapping instructions and misaligned code
    * Virtual machine-based protection schemes
    * Manual and automated unpacking strategies
    * Defeating anti-debugging protections
    * Identifying and bypassing integrity checks
<!-- chapter: vulnerability-discovery-and-exploit-development, duration: 6h -->
* Vulnerability Discovery and Exploit Development
    * Common vulnerability classes in compiled code
    * Buffer overflows: stack-based and heap-based exploitation
    * Format string vulnerabilities and exploitation
    * Use-after-free and double-free vulnerabilities
    * Integer overflow and type confusion issues
    * Modern exploit mitigations: `ASLR`, DEP/NX, stack canaries, and CFI
    * Return-oriented programming (ROP) and code reuse attacks
    * Writing proof-of-concept exploits
<!-- chapter: malware-analysis-methodology, duration: 6h -->
* Malware Analysis Methodology
    * Setting up a safe malware analysis lab
    * Triage and initial classification techniques
    * Behavioral analysis: sandbox execution and monitoring
    * Code analysis: identifying malware capabilities and communication protocols
    * String extraction and indicator identification
    * Analyzing command and control (`C2`) mechanisms
    * Malware persistence mechanisms and evasion techniques
    * Writing analysis reports and documenting findings
<!-- chapter: firmware-analysis-and-ctf-challenges, duration: 5h -->
* Firmware Analysis and CTF Challenges
    * Firmware acquisition: dumping and extraction techniques
    * Firmware `file` system extraction and analysis
    * Identifying embedded OS components and custom code
    * Hardware interface analysis basics
    * Emulating firmware for dynamic analysis
    * CTF challenge methodology and problem-solving strategies
    * Applying reverse engineering skills to capture-the-flag scenarios

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
