---
tags:
  - languages:javascript
  - languages:typescript
  - practices:mobile
level: intermediate
category: language
duration_hours: 32
audience:
  - audiences:developers
---
<!-- course: react_native -->
# `React Native` Mobile Development

## Description
`React Native` enables developers to build native mobile applications for `iOS` and `Android` using `JavaScript` and React. This course covers the full spectrum of `React Native` development, from core components and navigation to native modules, animations, and deployment. Students will learn to build production-ready mobile applications with modern tooling including Expo, `React Navigation`, Reanimated, and testing frameworks.

## Duration
32 hours / 4 days

## Intended Audience
* `JavaScript` and React developers transitioning to mobile development
* Mobile developers exploring cross-platform solutions
* Full-stack developers adding mobile capabilities to their skill set
* `TypeScript` developers building type-safe mobile applications
* Development teams evaluating cross-platform mobile frameworks

## Prerequisites
* Strong proficiency in `JavaScript` (`ES6`+) and React fundamentals
* Understanding of JSX, component lifecycle, hooks, and state management
* Basic familiarity with `TypeScript` syntax and `type-annotations`
* Knowledge of `REST APIs` and asynchronous programming (async/await, Promises)
* Experience with `npm` or `yarn` package management
* A `macOS` machine is required for `iOS` development and testing

## Required Knowledge
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)
* `TypeScript` Programming (or equivalent experience)

## Objectives
* Build cross-platform mobile applications with `React Native` core components
* Implement navigation flows using `React Navigation`
* Manage application state effectively across screens and components
* Create fluid animations using Reanimated and `Gesture Handler`
* Integrate with device APIs, native modules, and third-party services
* Set up and use Expo for rapid development and simplified workflows
* Write and run tests using Jest and Detox
* Build, sign, and deploy applications to the `App Store` and `Google Play`

## Outline
<!-- chapter: introduction-to-react-native, duration: 3h -->
* Introduction to `React Native`
    * What is `React Native` and how it bridges to native platforms
    * Comparison with other cross-platform frameworks (`Flutter`, Ionic)
    * Development environment setup: `React Native CLI` vs Expo
    * Setting up `Android Studio` and `Xcode`
    * Creating your first `React Native` application
    * Understanding the Metro bundler and project structure
    * Running on simulators, emulators, and physical devices
<!-- chapter: core-components-and-styling, duration: 3h -->
* Core Components and Styling
    * Core components: View, Text, Image, ScrollView, FlatList
    * StyleSheet `API` and `React Native` styling conventions
    * Flexbox layout in `React Native`
    * Platform-specific styling and components
    * Handling different screen sizes and densities
    * Touchable components and pressable interactions
    * SafeAreaView and device notch handling
    * Custom component creation and reusable patterns
<!-- chapter: navigation-with-react-navigation, duration: 3h -->
* Navigation with `React Navigation`
    * Installing and configuring `React Navigation`
    * Stack navigation and screen transitions
    * Tab navigation: bottom tabs and material top tabs
    * Drawer navigation and custom drawer content
    * Passing parameters between screens
    * Nested navigators and complex navigation structures
    * Deep linking and universal links
    * Navigation state persistence and authentication flows
<!-- chapter: state-management, duration: 3h -->
* State Management
    * Local state with useState and useReducer
    * `Context API` for global state sharing
    * State management with Zustand
    * State management with `Redux Toolkit` and `RTK Query`
    * `Async` state and data fetching with `TanStack Query`
    * Persisting state across app restarts
    * State management best practices for mobile applications
<!-- chapter: the-expo-framework, duration: 3h -->
* The Expo Framework
    * Expo architecture and managed vs bare workflows
    * `Expo Router` for file-based navigation
    * Expo modules: camera, location, notifications, file system
    * `EAS Build` and `EAS Submit` for cloud builds
    * Expo configuration and app manifest (app.`json`/app.config.js)
    * Over-the-air updates with `EAS Update`
    * Ejecting from Expo and custom development clients
<!-- chapter: platform-specific-code-and-native-modules, duration: 3h -->
* Platform-Specific Code and Native Modules
    * Platform module and platform-specific file extensions
    * Conditional rendering and logic based on platform
    * Creating native modules for `iOS` (Swift/`Objective-C`)
    * Creating native modules for `Android` (`Kotlin`/`Java`)
    * Using `Turbo Modules` and the new architecture
    * Bridging native UI components with Fabric
    * Consuming third-party native libraries
<!-- chapter: networking-and-data-persistence, duration: 3h -->
* Networking and Data Persistence
    * `Fetch API` and Axios for network requests
    * Handling authentication tokens and refresh flows
    * `WebSocket` connections for real-time communication
    * Local storage with AsyncStorage
    * High-performance storage with MMKV
    * `SQLite` for structured local data
    * `File` system access and media management
    * Offline-first patterns and data synchronization
<!-- chapter: animations-and-gestures, duration: 3h -->
* Animations and Gestures
    * `Animated API` basics and limitations
    * `React Native Reanimated` worklets and shared values
    * Layout animations and entering/exiting transitions
    * `React Native Gesture Handler` for touch interactions
    * Pan, pinch, rotation, and fling gesture recognizers
    * Combining gestures with animations
    * Lottie animations for complex motion graphics
    * Performance considerations for smooth 60fps animations
<!-- chapter: debugging-testing-and-performance, duration: 4h -->
* Debugging, Testing, and Performance
    * Debugging with `React Native Debugger` and Flipper
    * `Chrome DevTools` and `React DevTools` integration
    * Profiling `JavaScript` and native performance
    * Common performance pitfalls and optimization strategies
    * Reducing re-renders and optimizing FlatList performance
    * Unit testing with Jest and `React Native Testing Library`
    * End-to-end testing with Detox
    * Snapshot testing for UI consistency
<!-- chapter: building-and-deploying, duration: 4h -->
* Building and Deploying
    * Code signing for `iOS` and `Android`
    * Building release binaries for the `App Store`
    * Building release binaries for `Google Play`
    * Push notifications with `Firebase Cloud Messaging` and APNs
    * App versioning and release management
    * Crash reporting and analytics integration
    * Continuous integration and `continuous delivery` for mobile
    * Over-the-air updates and staged rollouts

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
