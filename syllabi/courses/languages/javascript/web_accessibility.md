---
tags:
  - concepts:web-development
  - concepts:best-practices
level: intermediate
category: language
duration_hours: 16
audience:
  - audiences:developers
  - audiences:architects
---
<!-- course: web_accessibility -->
# Web Accessibility

## Description
Web accessibility ensures that websites and web applications are usable by everyone, including people with disabilities. This course provides a comprehensive understanding of accessibility principles, standards, and practical techniques for building inclusive web experiences. It covers `WCAG 2.2` guidelines, ARIA specifications, assistive technology compatibility, testing strategies, and legal requirements, with hands-on application in modern front-end frameworks.

## Duration
16 hours / 2 days

## Intended Audience
* Front-end developers building accessible web applications
* Full-stack developers responsible for user-facing interfaces
* QA engineers testing for accessibility compliance
* UX designers collaborating with development teams on inclusive design
* Team leads and architects establishing accessibility standards for projects
* Developers working on applications subject to accessibility regulations

## Prerequisites
* `Solid` understanding of `HTML`, `CSS`, and `JavaScript`
* Experience building web applications with at least one modern framework (`React`, Vue, or `Angular`)
* Basic knowledge of the DOM and browser developer tools
* Understanding of form elements and user input handling
* Familiarity with semantic `HTML` elements and their purposes

## Required Knowledge
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)
* `React` (or equivalent experience)
* `Angular` (or equivalent experience)

## Objectives
* Understand the four principles of `WCAG 2.2` and their success criteria
* Implement ARIA roles, attributes, and states to enhance accessibility
* Build keyboard-navigable interfaces with proper focus management
* Create accessible forms, tables, images, and media content
* Test applications using automated tools and assistive technologies
* Understand legal requirements including ADA, `Section 508`, and the EAA
* Apply accessibility best practices in `React`, Vue, and `Angular` applications
* Establish accessibility workflows and standards within development teams

## Outline
<!-- chapter: introduction-to-web-accessibility, duration: 1h -->
* Introduction to Web Accessibility
    * What is web accessibility and why it matters
    * The diversity of user needs and assistive technologies
    * Overview of `WCAG 2.2` guidelines and conformance levels (A, AA, AAA)
    * The four principles: perceivable, operable, understandable, robust
    * The accessibility tree and how browsers expose content
    * Business case and legal landscape for accessibility
<!-- chapter: semantic-html-and-document-structure, duration: 2h -->
* Semantic `HTML` and Document Structure
    * The role of semantic `HTML` in accessibility
    * Landmark elements: `<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>`
    * Heading hierarchy and document outline
    * Lists, definitions, and structural grouping
    * Language attributes and text direction
    * Page titles and meaningful link text
    * `When` to use native elements vs ARIA augmentation
<!-- chapter: aria-roles-attributes-and-states, duration: 2h -->
* ARIA Roles, Attributes, and States
    * Introduction to WAI-ARIA specification
    * Landmark roles: banner, navigation, main, complementary, contentinfo
    * Widget roles: button, dialog, tablist, menu, alert
    * aria-label, aria-labelledby, and aria-describedby
    * aria-live regions for dynamic content updates
    * aria-expanded, aria-selected, aria-checked, and other states
    * aria-hidden and managing visibility for assistive technologies
    * Common ARIA anti-patterns and mistakes to avoid
<!-- chapter: keyboard-navigation-and-focus-management, duration: 2h -->
* Keyboard Navigation and Focus Management
    * Keyboard accessibility requirements and expectations
    * Tab order and the tabindex attribute
    * Focus indicators and visible focus styling
    * Managing focus in single-page applications
    * Focus trapping for modal dialogs and overlays
    * Skip navigation links and bypass blocks
    * Keyboard interaction patterns for custom widgets
    * Roving tabindex and arrow key navigation
<!-- chapter: perceivable-content, duration: 2h -->
* Perceivable Content
    * Color contrast requirements and tools for checking ratios
    * Text resizing and responsive text considerations
    * Meaningful alternative text for images and decorative image handling
    * Accessible SVG graphics and icon implementations
    * Media accessibility: captions for video, transcripts for audio
    * Audio descriptions and accessible media players
    * Content that avoids seizure-inducing patterns
    * Adaptable content and multiple presentation modes
<!-- chapter: accessible-forms-and-interactive-elements, duration: 2h -->
* Accessible Forms and Interactive Elements
    * Associating labels with form controls
    * Grouping related fields with `<fieldset>` and `<legend>`
    * Error identification and descriptive error messages
    * Required fields and input validation feedback
    * Accessible date pickers, autocomplete, and custom select elements
    * `File` upload accessibility considerations
    * Accessible tables: headers, scope, and captions
    * Summary attributes and complex table structures
<!-- chapter: testing-for-accessibility, duration: 2h -->
* Testing for Accessibility
    * Manual testing techniques and screen reader basics
    * Testing with NVDA on `Windows`
    * Testing with VoiceOver on `macOS` and `iOS`
    * Automated testing with axe-core and browser extensions
    * Lighthouse accessibility audits in `Chrome DevTools`
    * Integrating accessibility checks into `CI/CD` pipelines
    * Writing automated accessibility tests with `jest`-axe and `cypress`-axe
    * Creating accessibility test plans and checklists
<!-- chapter: legal-requirements-and-compliance, duration: 1h -->
* Legal Requirements and Compliance
    * `Americans with Disabilities Act` (ADA) and web accessibility
    * `Section 508` of the `Rehabilitation Act`
    * `European Accessibility Act` (EAA) and `EN 301 549`
    * VPAT (Voluntary Product Accessibility Template) documentation
    * Conformance reporting and accessibility statements
    * Managing accessibility debt and remediation priorities
<!-- chapter: accessibility-in-modern-frameworks, duration: 2h -->
* Accessibility in Modern Frameworks
    * Accessibility considerations in `React`: JSX semantics, fragments, refs for focus
    * Accessible `React` component patterns and libraries
    * Accessibility in Vue: template semantics, v-focus, and vue-a11y utilities
    * Accessibility in `Angular`: CDK a11y module, live announcer, focus trap
    * Component library accessibility evaluation
    * Establishing accessibility guidelines for development teams

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
