---
tags:
  - infrastructure:android
  - languages:java
  - practices:mobile
  - tools:android-studio
  - tools:sqlite
level: beginner
category: operating-systems
duration_hours_short: 40
duration_hours_long: 48
audience:
  - audiences:developers
duration_hours: 56
---
<!-- course: developing_android_applications_with_java -->
# Developing `Android` Applications with `Java`

## Description
This is a technical course that introduces programming `Android` applications. It is suitable for
programmers starting new projects on `Android`, or for those maintaining existing applications.
Based on `Linux`, `Android` has rapidly emerged as the platform of choice for a wide range of
mobile devices. In the short time since its first distribution in 2007, it has become one of the
most widely used and prolific operating systems. Applications for `Android` are mostly written in
the popular programming language `Java`, and a well-developed `SDK` is provided by Google,
together with an emulator for development on the desktop.
This is an instructor-led presentation with hands-on exercises course using the `Android`
development environment on Microsoft `Windows`, but is equally applicable to other platforms,
such as `macOS` or `Linux`.

This course is intended for `Java` programmers and teaches the `Java` APIs of `Android`.

## Duration
* Short: 40 hours / 5 days (assumes `Java` experience)
* Long: 48 hours / 6 days (includes `Java` programming intro)

## Intended Audience
* Object-oriented developers who would like to learn how to write `Android` applications using the `Java` programming language.

## Prerequisites
* Some knowledge of `XML` is required
* For the short version, previous knowledge and experience of `Java` is assumed
* Experience of using `Android` at a user level is not assumed but will be an advantage, as
will previous experience of `Android` Studio

## Objectives
* Use `Android` Studio with the `Android` emulator as a productive development environment
* Learn how to write and run `Android` applications
* Understand `Android` features
* Exploit the `Android` developer's `SDK`
* Appreciate the differences between versions of `Android`
* Design and write effective user interfaces for `Android` applications
* Exploit hardware features available on a variety of devices
* Effectively use external services and resources

## Outline
<!-- chapter: java-programming-long, duration: 2h -->
* `Java` Programming [long]
    * Basic Syntax
    * `OOP`
    * Collections
    * Exceptions
    * Multitasking
<!-- chapter: introduction-to-android, duration: 4h -->
* Introduction to `Android`
    * Copyrights and legal stuff
    * Rationale and history
    * Hardware
    * Software versions
    * Architecture
    * The `Android` Runtime (ART)
    * Apps!
    * Current `Android` platforms
    * Telephone, tablet and other variants
<!-- chapter: the-development-environment, duration: 2h -->
* The Development Environment
    * The emulator environment
    * A first project from `Android` Studio
    * Creating the AVD from `Android` Studio
    * Running our project
<!-- chapter: use-of-java-in-android, duration: 3h -->
* Use of `Java` in `Android`
    * `OO` concepts review
    * `Java` language review
    * Introduction to `Android` classes
    * `Android` components
    * Other `Android` classes
    * Application security
    * The Manifest `File` - Public `API`
<!-- chapter: developer-tools, duration: 4h -->
* Developer Tools
    * `SDK` tools
    * `Android` Debug bridge - adb
    * `Android` Device Monitor
    * The shell
    * `logcat`
    * `Android` lint
    * SD card
    * What about a real device?
    * `Android` Device Chooser
<!-- chapter: ui-layouts-and-views-in-xml, duration: 3h -->
* UI - Layouts and Views in `XML`
    * Activities
    * Views
    * Layouts
    * Use of `XML` for UI components
    * Widgets
    * Storing and using literal values
<!-- chapter: ui-layouts-and-views-in-java, duration: 3h -->
* UI - Layouts and Views in `Java`
    * Layouts, Widget `ids` and R.`java`
    * Using literal values (revisited)
    * Handling events
    * Getting and setting view values
    * RecyclerView
<!-- chapter: ui-menus, duration: 2h -->
* UI - Menus
    * Menus
    * Menus in `XML`
    * The code for option menus
    * The code for context menus
<!-- chapter: ui-activity-life-cycles, duration: 3h -->
* UI - Activity life-cycles
    * The 'back stack'
    * Activity life-cycles and call-backs
    * Saving state
    * Persisting state
    * Launching a new activity
    * Declaring activities in the manifest file
<!-- chapter: services-and-receivers, duration: 3h -->
* Services and Receivers
    * What is a Service?
    * The IntentService class
    * Declaring Services in the manifest file
    * Status Bar and notifications
    * Broadcasts and Broadcast Receivers
<!-- chapter: content-providers, duration: 3h -->
* Content Providers
    * Standard providers
    * Querying and changing data
    * Use of URIs
    * The `query()` method
    * Inserting, deleting and updating data
    * Querying and retrieving data on another thread
    * Writing your own content provider
<!-- chapter: network-access, duration: 3h -->
* Network Access
    * Overview
    * Checking connectivity
    * Internet access
    * `Bluetooth`
    * Introduction to Wi-Fi Direct and NFC
<!-- chapter: data-access, duration: 2h -->
* Data Access
    * Internal Storage - private data
    * External Storage - public data
    * Persisting state with SharedPreferences
<!-- chapter: sqlite, duration: 4h -->
* `SQLite`
    * What is `SQLite`?
    * `SQLite` data-types
    * `SQLite` table definitions
    * `SQLite` data manipulation
    * Using `SQLite` in `Android`
    * Using `SQLite`
    * Using `SQLite` with a Content Provider
    * Using ADB and sqlite3
<!-- chapter: devices-and-external-services, duration: 2h -->
* Devices and External Services
    * Telephony
    * Using a camera
    * Location, location, location: GPS (and friends)
    * Introduction to Google Maps
<!-- chapter: further-ui-topics, duration: 2h -->
* Further UI Topics
    * Designing for hardware variety
    * Using multiple layouts
    * Fragments
    * The Action Bar
<!-- chapter: testing, duration: 3h -->
* Testing
    * What should I test?
    * Testing platforms
    * `Android` `JUnit` extensions
    * UI Application Exerciser Monkey
    * monkeyrunner
    * Other tools
<!-- chapter: publishing, duration: 3h -->
* Publishing
    * The publishing process
    * Signing
    * The `Android` Studio Export Wizard
    * ProGuard
    * Versioning
    * Google Play
    * The `Android` Developer Console
<!-- chapter: beyond-java, duration: 5h -->
* Beyond `Java`
    * Other development techniques
    * Native Code
    * Native Development Kit - `NDK`
    * Mono - `C#`
    * Scripting Layer for `Android` - SL4A

## Installations
* `Android` Studio is required and installation instructions are [`android`-studio-install](`https`://developer.`android`.com/studio/install)
* There is no need to install this before the course and it is usually installed at the start of the course with the help of the instructor.
* Latest version is usually preferred.
* No need to install `Java` before either.
* The course uses the emulator to run the applications so no need for a physical device although the students may use their phone to run the applications they write.

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
