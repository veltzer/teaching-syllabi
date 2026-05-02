---
tags:
  - languages:kotlin
  - practices:mobile
  - concepts:architecture
level: intermediate
category: language
duration_hours: 24
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: kotlin_multiplatform -->
# `Kotlin Multiplatform` Development

## Description
`Kotlin Multiplatform` (KMP) allows developers to share business logic across `Android`, `iOS`, desktop, and web platforms while maintaining native user experiences. This course covers the full KMP ecosystem, from shared code architecture with expect/actual declarations to `Compose Multiplatform` for shared UI, networking with Ktor, and deploying to multiple targets. Students will learn to build and maintain production-grade multiplatform projects.

## Duration
24 hours / 3 days

## Intended Audience
* `Kotlin` developers looking to expand beyond `Android` to multiple platforms
* `Android` developers seeking to share code with `iOS` teams
* Mobile development teams evaluating cross-platform strategies
* Backend `Kotlin` developers interested in full-stack multiplatform development
* Software architects designing shared codebases for multiple targets

## Prerequisites
* `Solid` proficiency in `Kotlin` programming (classes, functions, coroutines, extensions)
* Experience with `Android` development using `Kotlin` and `Jetpack Compose`
* Basic understanding of `iOS` development concepts and `Xcode`
* Familiarity with `Gradle` build system and dependency management
* Understanding of `REST APIs` and `JSON` data formats
* Knowledge of coroutines and asynchronous programming in `Kotlin`

## Objectives
* Architect `Kotlin Multiplatform` projects with effective shared code strategies
* Use expect/actual declarations for platform-specific implementations
* Build shared UI with `Compose Multiplatform` across `Android`, `iOS`, and desktop
* Implement networking and serialization with Ktor and kotlinx.serialization
* Manage asynchronous operations with `Kotlin` coroutines in shared code
* Set up dependency injection with Koin in multiplatform projects
* Test shared code and platform-specific implementations
* Build and deploy applications targeting `Android`, `iOS`, desktop, and web

## Outline
<!-- chapter: introduction-to-kotlin-multiplatform, duration: 2h -->
* Introduction to `Kotlin Multiplatform`
    * The KMP vision: shared logic with native UI
    * How KMP compiles to `JVM`, native (`iOS`/desktop), and `JavaScript`
    * Comparison with `Flutter`, `React Native`, and other cross-platform approaches
    * Setting up the development environment: `Android Studio`, `Xcode`, KMP plugin
    * Creating a new KMP project with the KMP wizard
    * Understanding the project structure: commonMain, androidMain, iosMain
    * `Gradle` configuration for multiplatform projects
<!-- chapter: shared-code-architecture, duration: 2h -->
* Shared Code Architecture
    * expect and actual declarations for platform abstractions
    * Common source sets and platform-specific source sets
    * Intermediate source sets for grouping platforms
    * Sharing interfaces, data classes, and business logic
    * Platform-specific implementations for `Android` and `iOS`
    * Dependency management across source sets
    * Designing APIs that work well across all platforms
<!-- chapter: compose-multiplatform-for-shared-ui, duration: 3h -->
* `Compose Multiplatform` for Shared UI
    * Introduction to `Compose Multiplatform` and its relationship to `Jetpack Compose`
    * Setting up `Compose Multiplatform` in a KMP project
    * Building shared UI components with Compose
    * Theming and styling across platforms
    * Navigation in `Compose Multiplatform`
    * Platform-specific UI adaptations and interop
    * Handling platform differences in rendering and behavior
    * Resource management: images, strings, and fonts
<!-- chapter: networking-with-ktor, duration: 3h -->
* Networking with Ktor
    * Introduction to Ktor client for multiplatform networking
    * Configuring Ktor engines for each platform
    * Making `HTTP` requests: GET, POST, PUT, DELETE
    * Request and response handling with content negotiation
    * Authentication and token management
    * `WebSocket` support for real-time communication
    * Error handling and retry strategies
    * Logging and debugging network requests
<!-- chapter: serialization-and-data-handling, duration: 2h -->
* Serialization and Data Handling
    * kotlinx.serialization for multiplatform `JSON` processing
    * Defining serializable data classes
    * Custom serializers and polymorphic serialization
    * Working with different `JSON` configurations
    * `Protocol Buffers` and other serialization formats
    * Data transfer objects and domain model mapping
<!-- chapter: asynchronous-programming-with-coroutines, duration: 3h -->
* Asynchronous Programming with Coroutines
    * `Kotlin` coroutines in the multiplatform context
    * kotlinx.coroutines common and platform-specific dispatchers
    * Structured concurrency in shared code
    * Flow for reactive data streams across platforms
    * Bridging coroutines with `iOS` concurrency (Swift async/await)
    * Error handling and cancellation in multiplatform coroutines
    * Testing asynchronous shared code
<!-- chapter: dependency-injection-and-local-storage, duration: 3h -->
* Dependency Injection and Local Storage
    * Setting up Koin for multiplatform dependency injection
    * Defining modules and dependencies in common code
    * Platform-specific Koin modules and initialization
    * Scoping and lifecycle management across platforms
    * Local storage options: Settings (multiplatform-settings)
    * SQLDelight for multiplatform database access
    * `File` system access and data caching strategies
<!-- chapter: testing-shared-code, duration: 3h -->
* Testing Shared Code
    * `kotlin`.test framework for multiplatform testing
    * Writing tests in commonTest source set
    * Platform-specific tests in androidTest and iosTest
    * Mocking and faking dependencies in shared tests
    * Testing coroutines and Flow in common code
    * Integration testing strategies for multiplatform modules
    * Running tests across all target platforms
<!-- chapter: building-and-deploying-for-multiple-targets, duration: 3h -->
* Building and Deploying for Multiple Targets
    * Building for `Android`: AAR generation and `Play Store` distribution
    * Building for `iOS`: XCFramework generation and `Xcode` integration
    * Building for desktop: `JVM`-based distribution for `Windows`, `macOS`, `Linux`
    * Building for web: `Kotlin`/JS and `Kotlin`/Wasm targets
    * `CI/CD` pipelines for KMP projects with `GitHub Actions`
    * Managing platform-specific versions and releases
    * Automating builds and tests across all targets
    * Publishing shared libraries and managing artifact distribution

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
