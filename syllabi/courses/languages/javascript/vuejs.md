---
tags:
  - languages:javascript
  - languages:typescript
  - concepts:web-development
level: intermediate
category: language
duration_hours: 32
audience:
  - audiences:developers
---
<!-- course: vuejs -->
# `Vue.js` Development

## Description
This course provides a comprehensive guide to building modern web applications with `Vue 3`. Starting from core fundamentals like the Composition `API`, reactivity, and component architecture, the course progresses through routing, state management with Pinia, form handling, `HTTP` integration, `TypeScript` support, testing, and server-side rendering with Nuxt.js. Students will gain the skills to build scalable, maintainable single-page applications.

## Duration
32 hours / 4 days

## Intended Audience
* Frontend developers looking to master `Vue.js` for building modern web applications
* Full-stack developers who want to add `Vue.js` to their frontend toolkit
* `JavaScript` or `TypeScript` developers transitioning to component-based UI development
* `React` or `Angular` developers exploring `Vue.js` as an alternative framework
* Software engineers building single-page applications and progressive web apps

## Prerequisites
* `Solid` understanding of `JavaScript` (`ES6`+ features: arrow functions, destructuring, modules, promises)
* Basic knowledge of `HTML` and `CSS`
* Familiarity with `npm` or `yarn` package managers
* Understanding of component-based UI development concepts
* Basic experience with command-line tools and development servers
* Familiarity with `TypeScript` is helpful but not required

## Required Knowledge
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)
* `TypeScript` Programming (or equivalent experience)

## Objectives
* Build reactive user interfaces using the `Vue 3` Composition `API`
* Create reusable components with props, events, slots, and provide/inject
* Implement client-side routing with `Vue Router` including nested and dynamic routes
* Manage application state using Pinia stores
* Integrate `TypeScript` into Vue applications for type safety
* Handle forms, validation, and `HTTP` requests with Axios
* Write unit and component tests with Vitest and `Vue Test Utils`
* Set up build tooling with Vite and deploy Vue applications
* Understand server-side rendering concepts with Nuxt.js

## Outline
<!-- chapter: vue-3-fundamentals, duration: 4h -->
* `Vue 3` Fundamentals
    * Introduction to `Vue.js` and the `Vue 3` ecosystem
    * Creating a Vue application with Vite
    * Template syntax: interpolation, directives, and event handling
    * The Composition `API`: setup, `ref`, reactive
    * Computed properties and watchers
    * Conditional rendering and list rendering
    * Class and style bindings
    * Understanding the reactivity system
<!-- chapter: components-in-depth, duration: 3h -->
* Components in Depth
    * Component creation and registration
    * Props: declaration, validation, and type checking
    * Custom events and the emit pattern
    * Slots: default, named, and scoped slots
    * Provide and inject for dependency passing
    * Dynamic and `async` components
    * Component `design patterns` and composition
<!-- chapter: directives-and-lifecycle-hooks, duration: 3h -->
* Directives and Lifecycle Hooks
    * Built-in directives: v-model, v-show, v-if, v-for, v-`bind`, v-on
    * Custom directives: creation and use cases
    * Lifecycle hooks in the Composition `API`
    * Template refs and DOM access
    * nextTick and the rendering cycle
<!-- chapter: routing-with-vue-router, duration: 3h -->
* Routing with `Vue Router`
    * Setting up `Vue Router` and defining routes
    * Dynamic route matching and route parameters
    * Nested routes and named views
    * Programmatic navigation and route guards
    * Navigation guards: global, per-route, and in-component
    * Lazy loading routes and code splitting
    * Route transitions and scroll behavior
<!-- chapter: state-management-with-pinia, duration: 3h -->
* State Management with Pinia
    * Introduction to Pinia and store concepts
    * Defining stores: state, getters, and actions
    * Using stores in components
    * Store composition and shared state
    * Plugins and store subscriptions
    * Persisting state and hydration
    * Migrating from `Vuex` to Pinia
<!-- chapter: forms-validation-and-http-requests, duration: 3h -->
* Forms, Validation, and `HTTP` Requests
    * Form input bindings with v-model
    * Form handling patterns and multi-step forms
    * Validation strategies and validation libraries
    * Making `HTTP` requests with Axios
    * Interceptors, error handling, and loading states
    * Composables for reusable data fetching logic
<!-- chapter: transitions-animations-and-styling, duration: 3h -->
* Transitions, Animations, and Styling
    * The Transition and TransitionGroup components
    * `CSS` transitions and animations in Vue
    * `JavaScript`-based animations
    * List move transitions
    * Third-party animation library integration
<!-- chapter: typescript-with-vue, duration: 3h -->
* `TypeScript` with Vue
    * Setting up `TypeScript` in a Vue project
    * Typing component props, emits, and refs
    * Typing the Composition `API`: `ref`, reactive, computed
    * Type-safe stores with Pinia
    * Using `TypeScript` with `Vue Router`
    * Generics and utility types in Vue components
<!-- chapter: testing-and-build-tooling, duration: 4h -->
* Testing and Build Tooling
    * Unit testing with Vitest
    * Component testing with `Vue Test Utils`
    * Testing composables and stores
    * Mocking dependencies and `API` calls
    * Vite configuration and plugins
    * Environment variables and build modes
    * Code splitting and bundle optimization
<!-- chapter: server-side-rendering-and-deployment, duration: 3h -->
* Server-Side Rendering and Deployment
    * Introduction to Nuxt.js and SSR concepts
    * Nuxt project structure and conventions
    * Data fetching in Nuxt: useFetch and useAsyncData
    * Static site generation with Nuxt
    * Deployment strategies for Vue applications
    * Performance optimization and lazy loading

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
