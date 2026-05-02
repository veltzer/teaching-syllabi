---
tags:
  - languages:powershell
  - practices:automation
  - practices:scripting
level: beginner
category: language
duration_hours: 24
audience:
  - audiences:developers
  - audiences:sysadmins
  - audiences:devops
---
<!-- course: powershell -->
# `PowerShell`

## Description
`PowerShell` is a cross-platform task automation and configuration management framework
consisting of a command-line shell and scripting language built on `.NET`. Unlike traditional
shells that work with text, `PowerShell` operates on objects, making it exceptionally powerful
for system administration, automation, and `DevOps` tasks. This course covers `PowerShell`
from the basics of cmdlets and the pipeline through advanced topics including remote
management, cloud automation for `Azure` and `AWS`, Desired State Configuration, and
cross-platform usage with `PowerShell` Core.
The course includes hands on exercises.

## Duration
24 hours / 3 days

## Intended Audience
* System administrators looking to automate repetitive tasks.
* `DevOps` engineers managing infrastructure with code.
* Developers building automation scripts for `Windows` or cross-platform environments.

## Prerequisites
* Basic familiarity with a command-line interface (`Windows` Command Prompt, Bash, or similar).
* Understanding of fundamental IT concepts (file systems, processes, networking basics).
* No prior scripting experience is required.

## Required Knowledge
* Bash Scripting (or equivalent experience)

## Objectives
* Navigate and use the `PowerShell` console and ISE/`VS Code` effectively
* Write scripts using variables, operators, control flow, and functions
* Leverage the pipeline and object-oriented nature of `PowerShell`
* Manage files, processes, and the `Windows` registry
* Administer remote systems with PSRemoting
* Automate cloud resources in `Azure` and `AWS`
* Write tests with Pester and apply scripting best practices

## Outline
<!-- chapter: introduction-to-powershell, duration: 1h -->
* Introduction to `PowerShell`
    * What is `PowerShell` and its history
    * `PowerShell` vs traditional shells
    * Installing and configuring `PowerShell`
    * The `PowerShell` console, ISE, and `VS Code` integration
    * Getting help: Get-Help, Get-Command, Get-Member
    * Execution policies overview
<!-- chapter: cmdlets-and-the-pipeline, duration: 2h -->
* Cmdlets and the Pipeline
    * Cmdlet naming convention (Verb-Noun)
    * The object pipeline
    * Piping objects between cmdlets
    * Filtering with Where-Object
    * Selecting properties with Select-Object
    * Sorting with Sort-Object
    * Formatting output (Format-Table, Format-List)
<!-- chapter: variables-and-data-types, duration: 1h -->
* Variables and Data Types
    * Variable declaration and assignment
    * Common data types (strings, integers, arrays, hashtables)
    * Type casting and conversion
    * Automatic variables ($_, $PSVersionTable, $Error, etc.)
    * Environment variables
    * Variable scope
<!-- chapter: operators, duration: 1h -->
* Operators
    * Arithmetic operators
    * Comparison operators (-eq, -ne, -gt, -lt, -like, -match)
    * Logical operators (-and, -or, -not)
    * String operators and regular expressions
    * Redirection operators
    * Type operators (-is, -as)
<!-- chapter: control-flow, duration: 1h -->
* Control Flow
    * if / elseif / else
    * `switch-statement`
    * `for-loops`, `foreach-loops`, and `while-loops`
    * do-while and do-until
    * break and continue
    * Pipeline flow control (ForEach-Object, Where-Object)
<!-- chapter: functions-and-scripts, duration: 2h -->
* Functions and Scripts
    * Defining functions
    * Parameters and parameter attributes
    * Advanced functions with CmdletBinding
    * Pipeline input in functions
    * Script files and `dot`-sourcing
    * Script parameters and `param()` blocks
    * Comment-based help
<!-- chapter: modules, duration: 1h -->
* Modules
    * Understanding modules
    * Importing and using modules
    * Finding modules in the `PowerShell` Gallery
    * Creating custom modules
    * Module manifests
    * Module best practices
<!-- chapter: error-handling, duration: 2h -->
* Error Handling
    * Terminating vs non-terminating errors
    * try / catch / finally
    * $ErrorActionPreference and -ErrorAction
    * trap statement
    * Custom error messages and error records
    * Debugging with Set-PSBreakpoint and Write-Debug
<!-- chapter: file-system-and-registry-operations, duration: 2h -->
* `File` System and Registry Operations
    * Navigating the file system with `PowerShell` providers
    * Creating, reading, writing, and deleting files
    * Working with `CSV`, `XML`, and `JSON` files
    * `File` permissions and `ACLs`
    * `Windows` Registry navigation and modification
    * Registry key and value management
<!-- chapter: remote-management, duration: 2h -->
* Remote Management
    * Introduction to PSRemoting
    * Enabling and configuring WinRM
    * Invoke-Command for remote execution
    * Enter-PSSession for interactive sessions
    * Sessions and persistent connections
    * Remoting over `SSH`
    * Security considerations for remoting
<!-- chapter: powershell-for-active-directory, duration: 1h -->
* `PowerShell` for `Active Directory`
    * The ActiveDirectory module
    * Managing users and groups
    * Querying with Get-ADUser and Get-ADGroup
    * Organizational units and group policies
    * Bulk operations and reporting
<!-- chapter: powershell-for-azure, duration: 1h -->
* `PowerShell` for `Azure`
    * The Az module
    * Authentication and context management
    * Managing virtual machines, storage, and networking
    * Resource groups and deployments
    * `Azure` automation runbooks
<!-- chapter: powershell-for-aws, duration: 1h -->
* `PowerShell` for `AWS`
    * The `AWS`.Tools modules
    * Configuring credentials and profiles
    * Managing `EC2`, `S3`, and `IAM` resources
    * Automating `AWS` infrastructure tasks
<!-- chapter: desired-state-configuration-dsc, duration: 1h -->
* Desired State Configuration (DSC)
    * Introduction to DSC
    * Writing DSC configurations
    * Resources and resource modules
    * Push vs pull mode
    * Applying and monitoring configurations
<!-- chapter: testing-with-pester, duration: 2h -->
* Testing with Pester
    * Introduction to Pester
    * Describe, Context, and It blocks
    * Assertions and should operators
    * Mocking and test doubles
    * Test-driven development with `PowerShell`
    * Infrastructure testing with Pester
<!-- chapter: powershell-core-and-cross-platform-usage, duration: 1h -->
* `PowerShell` Core and Cross-Platform Usage
    * `PowerShell` Core vs `Windows` `PowerShell`
    * Running `PowerShell` on `Linux` and `macOS`
    * Cross-platform compatibility considerations
    * `.NET` Core integration
<!-- chapter: scripting-best-practices-and-security, duration: 2h -->
* Scripting Best Practices and Security
    * Code style and formatting conventions
    * Script signing and certificates
    * Execution policies in depth
    * Credential management and SecureString
    * Logging and auditing
    * Performance optimization tips
    * Common scripting patterns and anti-patterns

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
