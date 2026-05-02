---
tags:
  - security:security
  - infrastructure:android
  - practices:reverse-engineering
  - security:exploitation
level: advanced
category: security
duration_hours: 16
audience:
  - audiences:security-professionals
  - audiences:developers
  - audiences:testers
---
<!-- course: android_reverse_engineering -->
# `Android` Reverse Engineering

## Description
This course covers the techniques and tools used to reverse engineer `Android` applications. Participants
will learn to decompile, instrument, and analyze `Android` apps for security research, vulnerability
assessment, and malware analysis purposes.

## Duration
16 hours / 2 days

## Intended Audience
* Security professionals performing mobile application assessments
* Developers seeking to understand how their apps can be reverse engineered
* Testers conducting security testing on `Android` applications

## Prerequisites
* Familiarity with `Android` application development
* Basic understanding of `Java` or `Kotlin`
* Experience with command-line tools
* Basic knowledge of security concepts

## Required Knowledge
* `Kotlin` Programming (or equivalent experience)

## Objectives
* Understand APK structure and the `Android` build process
* Decompile and analyze `Android` applications using industry tools
* Read and modify smali bytecode
* Perform dynamic instrumentation with Frida
* Intercept and analyze network traffic from `Android` apps
* Bypass common anti-tampering and certificate pinning protections
* Conduct malware analysis on `Android` samples

## Outline
<!-- chapter: apk-structure, duration: 2h -->
* APK Structure
    * APK file format and contents
    * AndroidManifest.`xml` analysis
    * DEX file format and `Dalvik` bytecode
    * Resource files and asset extraction
    * Native libraries and JNI interface
    * Multidex applications
<!-- chapter: decompilation-tools, duration: 1h -->
* Decompilation Tools
    * jadx for `Java` source recovery
    * apktool for resource decoding and rebuilding
    * dex2jar and JD-GUI
    * `Ghidra` for native library analysis
    * Comparing decompiler outputs
<!-- chapter: smali-code, duration: 1h -->
* Smali Code
    * `Dalvik` bytecode fundamentals
    * Smali syntax and instruction set
    * Reading and understanding smali code
    * Modifying smali for behavior changes
    * Reassembling and signing modified APKs
<!-- chapter: frida-dynamic-instrumentation, duration: 1h -->
* Frida Dynamic Instrumentation
    * Frida architecture and setup
    * Writing Frida scripts in `JavaScript`
    * Attaching to running processes
    * Enumerating classes and methods
    * Modifying `return-values` and arguments at runtime
<!-- chapter: hooking-methods, duration: 1h -->
* Hooking Methods
    * `Java` method hooking with Frida
    * Native function hooking
    * Constructor and overloaded method hooks
    * Tracing method calls and arguments
    * Building reusable hooking scripts
<!-- chapter: traffic-interception, duration: 2h -->
* Traffic Interception
    * Setting up proxy environments
    * `Burp Suite` and mitmproxy configuration
    * Intercepting `HTTPS` traffic
    * Analyzing `API` calls and data flows
    * `WebSocket` and custom protocol interception
<!-- chapter: debugging-release-builds, duration: 2h -->
* Debugging Release Builds
    * Enabling debugging on release APKs
    * `Android` Debug Bridge (ADB) techniques
    * JDWP debugging of `Android` apps
    * Memory inspection and heap analysis
    * `Logcat` analysis and hidden debug outputs
<!-- chapter: anti-tampering-bypass, duration: 2h -->
* Anti-Tampering Bypass
    * Root detection bypass techniques
    * Emulator detection bypass
    * Integrity check circumvention
    * SafetyNet and `Play Integrity` bypass
    * Debugger detection evasion
<!-- chapter: certificate-pinning-bypass, duration: 2h -->
* Certificate Pinning Bypass
    * Understanding pinning implementations
    * Frida scripts for pinning bypass
    * Objection framework for automated bypass
    * Network security config manipulation
    * Handling custom pinning implementations
<!-- chapter: malware-analysis-workflow, duration: 2h -->
* Malware Analysis Workflow
    * Setting up a safe analysis environment
    * Static analysis triage process
    * Behavioral analysis and sandboxing
    * Identifying command and control communication
    * Extracting indicators of compromise
    * Documenting and reporting findings

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
