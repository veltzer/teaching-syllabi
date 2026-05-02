---
tags:
  - tools:msbuild
  - build:dotnet
  - build:csharp
  - languages:csharp
  - practices:build-automation
level: intermediate
category: build-system
duration_hours: 16
audience:
  - audiences:developers
  - audiences:dotnet-developers
---
<!-- course: msbuild -->
# `MSBuild`

## Description
`MSBuild` is the foundational build engine for the entire `.NET` ecosystem, powering `Visual Studio`, the
`dotnet` `CLI`, and enterprise-scale `C#` and `F#` projects. This course demystifies the `MSBuild` project file
format, teaching participants to read, write, and extend `SDK`-style project files, create custom tasks, and
build complex multi-targeted solutions. Participants will learn to leverage `NuGet` integration, implement
multi-platform targeting, and run `MSBuild`-driven pipelines in modern `CI/CD` systems including `Azure DevOps`
and `GitHub Actions`.

## Duration
16 hours / 2 days

## Intended Audience
* `.NET` and `C#` developers who want to move beyond default project templates and understand what happens under the hood.
* Build and release engineers maintaining `.NET` build pipelines.
* Platform engineers responsible for shared `MSBuild` tooling and `NuGet` packages across large solutions.

## Prerequisites
* Working knowledge of `C#` and the `.NET` `SDK`.
* Familiarity with `Visual Studio` or the `dotnet` `CLI`.
* Basic understanding of `XML` syntax.

## Objectives
* Understand the `MSBuild` evaluation model and build execution flow.
* Read and author `SDK`-style and legacy project files.
* Use properties, items, and metadata to control builds.
* Define and compose `MSBuild` targets and tasks.
* Write custom inline tasks and compiled task assemblies.
* Implement multi-targeting for different frameworks and platforms.
* Manage `NuGet` package references and produce `NuGet` packages.
* Integrate `MSBuild` into `CI/CD` pipelines for automated delivery.

## Outline
<!-- chapter: introduction-to-msbuild, duration: 2h -->
* Introduction to `MSBuild`:
    * The role of `MSBuild` in the `.NET` toolchain.
    * `MSBuild` vs the `dotnet` `CLI` vs `Visual Studio` builds.
    * Installing and invoking `MSBuild` from the command line.
    * Build verbosity and diagnostic output.
<!-- chapter: project-file-structure, duration: 2h -->
* Project `File` Structure and `SDK`-Style Projects:
    * Legacy `.csproj` format vs. `SDK`-style projects.
    * The `Microsoft.NET.Sdk` `SDK` and implicit imports.
    * `Directory.Build.props` and `Directory.Build.targets`.
    * Wildcards and implicit item includes.
    * Restoring, building, and publishing from the command line.
<!-- chapter: properties-items-and-metadata, duration: 2h -->
* Properties, Items, and Metadata:
    * Property declaration, evaluation order, and reserved properties.
    * Item types: declaration, transforms, and batching.
    * Well-known and custom item metadata.
    * Property and item functions.
    * Conditions and conditional evaluation.
    * Environment variables and command-line property overrides.
<!-- chapter: targets-and-tasks, duration: 2h -->
* Targets and Tasks:
    * Anatomy of a `Target`: inputs, outputs, and dependencies.
    * Built-in tasks: `Copy`, Exec, Message, Delete, `MakeDir`.
    * Target ordering: `BeforeTargets`, AfterTargets, `DependsOnTargets`.
    * Incremental builds with input/output tracking.
    * Importing shared `.targets` and `.props` files.
<!-- chapter: custom-tasks, duration: 2h -->
* Custom Tasks and Inline Tasks:
    * Implementing `ITask` in a compiled `assembly`.
    * Using `UsingTask` and `TaskFactory`.
    * Inline tasks with `RoslynCodeTaskFactory`.
    * Passing parameters and returning items from tasks.
    * Debugging and testing custom tasks.
<!-- chapter: multi-targeting, duration: 2h -->
* Multi-Targeting and Cross-Platform Builds:
    * `TargetFramework` vs. `TargetFrameworks`.
    * Conditional logic per target framework.
    * Platform and runtime identifiers (`RID`).
    * Publishing self-contained applications.
    * Cross-OS builds and `Docker`-based build environments.
<!-- chapter: nuget-integration, duration: 2h -->
* `NuGet` Integration:
    * `PackageReference` and transitive dependency resolution.
    * Producing `NuGet` packages with `dotnet pack`.
    * Package metadata properties and `nuspec` generation.
    * `Central Package Management` with `Directory.Packages.props`.
    * Publishing to `NuGet.org` and private feeds.
<!-- chapter: cicd-with-msbuild, duration: 2h -->
* `CI/CD` with `MSBuild`:
    * Running `MSBuild` in `Azure DevOps` and `GitHub Actions`.
    * Caching `NuGet` packages and build outputs.
    * Versioning assemblies and packages from the pipeline.
    * Code signing and artifact publishing.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
