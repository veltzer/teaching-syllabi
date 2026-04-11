---
tags:
  - languages:swift
  - practices:mobile
  - concepts:programming
level: intermediate
category: language
duration_hours: 32
audience:
  - audiences:developers
---
<!-- course: macos_development -->
# `macOS` Development with `Swift`

## Description
This course teaches developers how to build native `macOS` applications using `Swift`. Students
will learn both AppKit and SwiftUI approaches to `macOS` development, covering everything
from window management and menus to `file` system access, networking, and distribution.
The course emphasizes modern `macOS` development practices including sandboxing, notarization,
and system integration.

## Duration
32 hours / 4 days

## Intended Audience
* Developers who want to build native `macOS` applications.
* `iOS` developers expanding to `macOS` development.
* Developers interested in Apple platform development with `Swift`.

## Prerequisites
* Working knowledge of `Swift` programming.
* Basic understanding of object-oriented programming concepts.
* Access to a Mac with `Xcode` installed.

## Objectives
* understand the core concepts and principles of `macOS` development
* gain practical knowledge of AppKit and SwiftUI for `macOS`
* gain practical knowledge of application distribution and notarization
* gain practical knowledge of system integration and accessibility

## Outline
<!-- chapter: macos-development-overview, duration: 1h -->
* `macOS` Development Overview
    * The `macOS` application model
    * `macOS` vs `iOS` development
    * Application lifecycle
    * `macOS` frameworks overview
    * Human Interface Guidelines
<!-- chapter: xcode-ide, duration: 2h -->
* `Xcode` IDE
    * Project setup and configuration
    * Interface Builder and Storyboards
    * `Xcode` previews for SwiftUI
    * Build settings and schemes
    * Instruments and profiling
<!-- chapter: swift-for-macos, duration: 1h -->
* `Swift` for `macOS`
    * `Swift` features relevant to `macOS`
    * Concurrency with `async`/`await`
    * Memory management (ARC)
    * Interoperability with `Objective-C`
<!-- chapter: appkit-fundamentals, duration: 2h -->
* AppKit Fundamentals
    * `Windows` and window controllers
    * Views and view controllers
    * Auto Layout
    * `Responder` chain
    * Custom drawing
<!-- chapter: swiftui-for-macos, duration: 2h -->
* SwiftUI for `macOS`
    * SwiftUI application structure
    * `macOS`-specific views and modifiers
    * Navigation and split views
    * Settings `windows`
    * Mixing SwiftUI and AppKit
<!-- chapter: menus-and-toolbars, duration: 2h -->
* Menus and Toolbars
    * Main menu customization
    * Contextual menus
    * Toolbar items and configuration
    * Touch Bar support
    * Menu bar extras (status items)
<!-- chapter: document-based-apps, duration: 2h -->
* Document-Based Apps
    * Document architecture
    * `File` reading and writing
    * Undo and redo
    * Auto-save and versioning
    * Recent documents
<!-- chapter: file-system-access, duration: 2h -->
* `File` System Access
    * `File` system APIs
    * Open and save panels
    * Bookmarks and security-scoped URLs
    * `File` coordination
    * Spotlight integration
<!-- chapter: sandboxing-and-entitlements, duration: 2h -->
* Sandboxing and Entitlements
    * App Sandbox overview
    * Entitlements configuration
    * Temporary exceptions
    * Container directories
    * XPC services
<!-- chapter: networking, duration: 2h -->
* Networking
    * URLSession for `HTTP` requests
    * `WebSocket` connections
    * Bonjour and local networking
    * Network framework
    * Background transfers
<!-- chapter: core-data, duration: 2h -->
* `Core Data`
    * Data model design
    * Managed object contexts
    * Fetch requests and predicates
    * CloudKit integration
    * Migration strategies
<!-- chapter: combine-framework, duration: 2h -->
* Combine Framework
    * Publishers and subscribers
    * Operators and transformations
    * Integrating Combine with SwiftUI
    * Error handling in Combine
    * Replacing delegation with Combine
<!-- chapter: distributing-apps, duration: 2h -->
* Distributing Apps
    * App Store distribution
    * Developer `ID` signing
    * Notarization process
    * Direct distribution outside the App Store
    * Packaging and DMG creation
<!-- chapter: testing, duration: 2h -->
* Testing
    * Unit testing with XCTest
    * UI testing
    * Performance testing
    * Test plans and coverage
    * Snapshot testing
<!-- chapter: accessibility, duration: 2h -->
* Accessibility
    * Accessibility APIs
    * VoiceOver support
    * Accessibility inspector
    * Dynamic Type
    * Accessible custom controls
<!-- chapter: keyboard-shortcuts-and-responder-chain, duration: 1h -->
* Keyboard Shortcuts and `Responder` Chain
    * Key equivalents for menu items
    * Custom keyboard shortcuts
    * `Responder` chain in depth
    * First `responder` management
<!-- chapter: drag-and-drop, duration: 1h -->
* Drag and Drop
    * Drag sources and destinations
    * Pasteboard and UTI types
    * Drag and drop in SwiftUI
    * Promised files
<!-- chapter: system-integration, duration: 2h -->
* System Integration
    * Notifications (user and push)
    * Sharing extensions
    * Spotlight indexing
    * Widgets with WidgetKit
    * Shortcuts and Intents

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
