---
tags:
  - languages:kotlin
  - infrastructure:android
  - concepts:concurrency
level: intermediate
category: language
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: kotlin_for_android -->
# `Kotlin` for `Android`

## Description
This course teaches modern `Android` application development using `Kotlin` and the latest Jetpack libraries. Students will learn how to build robust, maintainable `Android` applications using `Kotlin` coroutines for asynchronous programming, `Jetpack Compose` for declarative UI, Room for local persistence, Hilt for dependency injection, and other essential `Android` architecture components. The course emphasizes best practices, testability, and modern `Android` development patterns.

## Duration
24 hours / 3 days

## Intended Audience
* `Android` developers looking to adopt modern `Kotlin`-based development practices
* Mobile developers transitioning from `Java`-based `Android` development to `Kotlin`
* Developers building production-quality `Android` applications with Jetpack components

## Prerequisites
* Familiarity with mobile application concepts and lifecycle management

## Required Knowledge
* `Kotlin` Programming
* `Android` Application Development

## Objectives
* Use `Kotlin` coroutines, Flow, and StateFlow to manage asynchronous operations
* Build declarative UIs with `Jetpack Compose`
* Implement the recommended `Android` architecture using ViewModel and state management
* Persist data locally with Room database
* Handle navigation, dependency injection, and background work using Jetpack components
* Write effective tests for `Android` applications built with `Kotlin`

## Outline
<!-- chapter: kotlin-coroutines-on-android, duration: 2h -->
* `Kotlin` Coroutines on `Android`
    * Coroutine basics and structured concurrency
    * Coroutine scopes and dispatchers
    * viewModelScope and lifecycleScope
    * Exception handling in coroutines
    * Cancellation and timeouts
<!-- chapter: flow-and-stateflow, duration: 2h -->
* Flow and StateFlow
    * Cold flows vs hot flows
    * Creating and collecting flows
    * Flow operators and transformations
    * StateFlow and SharedFlow
    * Combining and flattening flows
    * Flow lifecycle awareness
<!-- chapter: jetpack-compose-ui, duration: 3h -->
* `Jetpack Compose` UI
    * Composable functions and recomposition
    * State management in Compose
    * Layouts: Column, Row, Box, LazyColumn
    * Theming and `Material Design 3`
    * Modifiers and custom drawing
    * Side effects and effect handlers
    * Interoperability with View-based UI
<!-- chapter: viewmodel-and-architecture, duration: 2h -->
* ViewModel and Architecture
    * ViewModel lifecycle and configuration changes
    * Exposing UI state with StateFlow
    * Unidirectional data flow pattern
    * SavedStateHandle
    * Multi-module architecture considerations
<!-- chapter: room-database, duration: 2h -->
* Room Database
    * Entities, DAOs, and database setup
    * Queries and relationships
    * Room with Flow for reactive data
    * Migrations and schema management
    * Type converters
    * Testing Room databases
<!-- chapter: navigation-component, duration: 3h -->
* Navigation Component
    * Navigation graph and destinations
    * Type-safe navigation with Compose
    * Passing arguments between destinations
    * Deep links
    * Nested navigation graphs
    * Bottom navigation integration
<!-- chapter: hilt-dependency-injection, duration: 3h -->
* Hilt Dependency Injection
    * Hilt setup and annotations
    * Modules and bindings
    * Scoping and component hierarchy
    * Injecting into ViewModel, Activity, and Fragment
    * Assisted injection
    * Testing with Hilt
<!-- chapter: workmanager, duration: 2h -->
* WorkManager
    * Defining work requests
    * Constraints and scheduling
    * Chaining work and observing progress
    * Periodic work
    * Expedited work
<!-- chapter: datastore, duration: 2h -->
* DataStore
    * Preferences DataStore vs Proto DataStore
    * Reading and writing preferences
    * Migrating from SharedPreferences
    * Type-safe data with Proto DataStore
<!-- chapter: testing-android-apps-with-kotlin, duration: 3h -->
* Testing `Android` Apps with `Kotlin`
    * Unit testing coroutines and flows
    * Testing Compose UI with ComposeTestRule
    * Mocking dependencies with Hilt test modules
    * Integration testing with Room
    * Instrumented tests and UI automation
    * Test best practices and patterns

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
