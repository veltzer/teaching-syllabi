---
tags:
  - languages:javascript
  - languages:typescript
  - concepts:web-development
level: intermediate
category: language
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: svelte -->
# Svelte and SvelteKit Development

## Description
Svelte is a modern front-end framework that shifts work from the browser to the compile step, producing highly optimized vanilla `JavaScript` with no virtual DOM overhead. Combined with SvelteKit, its full-stack application framework, developers can build fast, server-rendered, and statically generated web applications. This course covers Svelte fundamentals through advanced patterns and full-stack development with SvelteKit.

## Duration
24 hours / 3 days

## Intended Audience
* Front-end developers looking to adopt a modern, compiler-based framework
* React or Vue developers exploring alternative approaches to reactivity
* Full-stack developers building server-rendered web applications
* `TypeScript` developers seeking a framework with first-class `TypeScript` support
* Web developers interested in performance-optimized applications

## Prerequisites
* `Solid` understanding of `HTML`, `CSS`, and modern `JavaScript` (`ES6`+)
* Familiarity with component-based architecture concepts
* Basic knowledge of `Node.js` and `npm`/pnpm package management
* Experience with at least one front-end framework (React, Vue, or Angular) is helpful
* Understanding of `HTTP` protocol and client-server communication
* Basic familiarity with `TypeScript` syntax

## Required Knowledge
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)
* React (or equivalent experience)
* Angular (or equivalent experience)
* `TypeScript` Programming (or equivalent experience)
* `Node.js` Backend Development (or equivalent experience)

## Objectives
* Build reactive user interfaces using Svelte components and template syntax
* Implement state management with Svelte stores and reactive declarations
* Create smooth transitions, animations, and motion effects
* Develop full-stack applications with SvelteKit routing, SSR, and SSG
* Handle server-side logic, form actions, and hooks in SvelteKit
* Integrate `TypeScript` into Svelte and SvelteKit projects
* Test Svelte components and SvelteKit applications
* Deploy SvelteKit applications to various hosting platforms

## Outline
<!-- chapter: introduction-to-svelte, duration: 2h -->
* Introduction to Svelte
    * What is Svelte and how it differs from React and Vue
    * The compiler-based approach and its performance benefits
    * Setting up a Svelte development environment
    * Project structure and configuration
    * Creating your first Svelte component
    * Understanding the Svelte compilation process
<!-- chapter: svelte-fundamentals-and-reactivity, duration: 2h -->
* Svelte Fundamentals and Reactivity
    * Reactive declarations and statements
    * Reactive assignments and the $: syntax
    * Component props and default values
    * Event handling and dispatching custom events
    * Two-way data binding with `bind`:
    * Reactive stores: writable, readable, and derived
    * The $ store auto-subscription syntax
<!-- chapter: template-syntax-and-control-flow, duration: 2h -->
* Template Syntax and Control Flow
    * Expression rendering and `HTML` injection
    * `{#if}`, `{:else if}`, and `{:else}` blocks
    * `{#each}` blocks with keyed iteration
    * `{#await}` blocks for promise handling
    * `{@html}` for raw `HTML` rendering
    * `{@const}` for local constants in templates
    * Slot-based content composition and named slots
<!-- chapter: component-patterns-and-lifecycle, duration: 3h -->
* Component Patterns and Lifecycle
    * Component lifecycle functions: onMount, onDestroy, beforeUpdate, afterUpdate
    * Component composition and slot forwarding
    * Context `API` with setContext and getContext
    * Spread props and `rest` props
    * Dynamic components with `<svelte:component>`
    * Special elements: `<svelte:window>`, `<svelte:body>`, `<svelte:head>`
    * Component bindings and this-references
<!-- chapter: styling-transitions-and-animations, duration: 3h -->
* Styling, Transitions, and Animations
    * Scoped `CSS` in Svelte components
    * Global styles and the `:global()` modifier
    * `CSS` custom properties and theming
    * Built-in transitions: fade, fly, slide, scale, draw
    * Custom transition functions
    * The animate: directive for list reordering
    * Motion with tweened and `spring` stores
    * Transition events and deferred transitions
<!-- chapter: advanced-state-management, duration: 2h -->
* Advanced State Management
    * Custom store implementations
    * Store composition patterns
    * Sharing state across components
    * Managing complex application state
    * Immutable data patterns in Svelte
    * Integration with external state management libraries
<!-- chapter: introduction-to-sveltekit, duration: 2h -->
* Introduction to SvelteKit
    * SvelteKit architecture and project structure
    * `File`-based routing and route parameters
    * Layout components and nested layouts
    * Page load functions and data fetching
    * Server-side rendering (SSR) and static site generation (SSG)
    * Understanding the SvelteKit request lifecycle
<!-- chapter: sveltekit-server-side-logic, duration: 3h -->
* SvelteKit Server-Side Logic
    * Server routes and `API` endpoints (+server.js)
    * Page server load functions (+page.server.js)
    * Form actions for handling form submissions
    * Progressive enhancement and use:enhance
    * Hooks: handle, handleFetch, handleError
    * Server-only modules and environment variables
    * Error and redirect handling
<!-- chapter: typescript-integration, duration: 2h -->
* `TypeScript` Integration
    * Setting up `TypeScript` in Svelte and SvelteKit projects
    * Typing component props, events, and slots
    * Type-safe load functions and form actions
    * Generated types and the ./$types module
    * Using `TypeScript` in Svelte template blocks
<!-- chapter: testing-and-deployment, duration: 3h -->
* Testing and Deployment
    * Unit testing Svelte components with Vitest and Testing Library
    * End-to-end testing with `Playwright`
    * Testing SvelteKit routes and server logic
    * SvelteKit adapters for different deployment targets
    * Deploying to `Vercel`, `Netlify`, and `Node.js` servers
    * Performance optimization and preloading strategies
    * Building for production and bundle analysis

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
