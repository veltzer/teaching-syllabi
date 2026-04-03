---
tags:
  - languages:javascript
  - concepts:web-development
  - networking:web
level: intermediate
category: language
duration_hours: 16
audience:
  - audiences:developers
---
<!-- course: progressive_web_apps -->
# Progressive Web Apps (PWA)

## Description
This course covers the design and development of Progressive Web Apps (PWA), which combine the reach of the web with the capabilities of native applications. Participants will learn how to build fast, reliable, and installable web experiences using service workers, caching strategies, push notifications, and offline-first architecture. The course includes practical use of the Workbox library and performance auditing with Lighthouse.

## Duration
16 hours / 2 days

## Intended Audience
* Web developers looking to build installable, offline-capable web applications.
* Front-end developers who want to deliver native-like experiences through the browser.

## Prerequisites
* `Solid` web development experience.
* Familiarity with modern `JavaScript` (`ES6`+) and asynchronous programming.

## Required Knowledge
* `HTML` `CSS` `JavaScript` Fundamentals

## Objectives
* Understand the principles and architecture of Progressive Web Apps.
* Implement service workers for offline support and background processing.
* Apply caching strategies appropriate to different application needs.
* Configure Web App Manifest for installability.
* Integrate push notifications and background sync.
* Use Workbox to simplify service worker development.
* Audit and improve PWA quality with Lighthouse.

## Outline
<!-- chapter: introduction-to-progressive-web-apps, duration: 1h -->
* Introduction to Progressive Web Apps
    * What makes a web app progressive
    * PWA vs native apps vs hybrid apps
    * Browser support and progressive enhancement
    * PWA success stories and use cases
<!-- chapter: service-workers, duration: 2h -->
* Service Workers
    * Service worker lifecycle (install, activate, fetch)
    * Registration and scope
    * Intercepting network requests
    * Service worker updates and versioning
    * Debugging service workers in DevTools
<!-- chapter: cache-api-and-caching-strategies, duration: 2h -->
* Cache `API` and Caching Strategies
    * Cache `API` fundamentals
    * Cache-first strategy
    * Network-first strategy
    * Stale-while-revalidate strategy
    * Cache-only and network-only patterns
    * Cache versioning and cleanup
<!-- chapter: offline-first-architecture, duration: 2h -->
* Offline-First Architecture
    * Designing for offline scenarios
    * IndexedDB for client-side data storage
    * Sync patterns for offline data
    * Offline UI/UX best practices
    * Conflict resolution strategies
<!-- chapter: web-app-manifest-and-installability, duration: 2h -->
* Web App Manifest and Installability
    * Manifest `file` structure and properties
    * Icons and splash screens
    * Display modes (standalone, fullscreen, minimal-ui)
    * Install prompts and criteria
    * App shortcuts and share target
<!-- chapter: push-notifications, duration: 2h -->
* Push Notifications
    * Push `API` and Notification `API`
    * Subscription management
    * Server-side push with VAPID
    * Notification design best practices
    * Permission handling and user experience
<!-- chapter: background-sync, duration: 1h -->
* Background Sync
    * Background Sync `API`
    * Periodic background sync
    * Reliable data submission
    * Retry strategies
<!-- chapter: workbox-library, duration: 2h -->
* Workbox Library
    * Workbox modules and architecture
    * Precaching with Workbox
    * Runtime caching strategies
    * Workbox routing and plugins
    * Build integration (webpack, `CLI`)
<!-- chapter: lighthouse-audits-and-performance, duration: 2h -->
* Lighthouse Audits and Performance
    * Running Lighthouse audits
    * PWA audit criteria
    * Performance scoring and optimization
    * Accessibility and best practices
    * Continuous auditing in `CI/CD`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
