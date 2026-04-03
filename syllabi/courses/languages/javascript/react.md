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
  - audiences:architects
---
<!-- course: react -->
# `React` Development

## Description
This course provides a comprehensive guide to building modern web applications with `React`. Starting from core fundamentals like JSX, components, props, and state, the course progresses through hooks, advanced component patterns, routing, state management, data fetching, styling strategies, testing, and performance optimization. Students will also learn how to use `TypeScript` with `React` and get an introduction to Next.js for production-grade applications.

## Duration
32 hours / 4 days

## Intended Audience
* Frontend developers looking to master `React` for building modern web applications
* Full-stack developers who want to strengthen their frontend skills with `React`
* `JavaScript` or `TypeScript` developers transitioning to component-based UI development
* Backend developers seeking to understand modern frontend architecture
* Software engineers working on single-page applications and progressive web apps

## Prerequisites
* `Solid` understanding of `HTML`, `CSS`, and `JavaScript` (`ES6`+ features)
* Familiarity with `npm` or `yarn` package managers
* Basic understanding of the DOM and browser developer tools
* Experience with `JavaScript` modules, arrow functions, destructuring, and promises
* Familiarity with `TypeScript` basics is helpful but not required

## Required Knowledge
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)
* `TypeScript` Programming (or equivalent experience)

## Objectives
* Build interactive user interfaces using `React` components, JSX, props, and state
* Implement and compose `React` hooks including useState, useEffect, useContext, useReducer, useMemo, useCallback, and custom hooks
* Apply common component patterns for reusable and maintainable code
* Build forms with controlled components and handle user input effectively
* Implement client-side routing using `React Router`
* Manage application state with `Context API`, `Redux Toolkit`, and Zustand
* Fetch and cache server data using fetch and `TanStack Query`
* Style `React` applications using `CSS Modules`, styled-components, and `Tailwind CSS`
* Write reliable tests with `React Testing Library` and `Jest`
* Optimize `React` application performance using `React`.memo, `React`.lazy, and Suspense
* Integrate `TypeScript` into `React` projects for type-safe development
* Build server-rendered applications with Next.js

## Outline
<!-- chapter: react-fundamentals, duration: 3h -->
* `React` Fundamentals
    * What is `React` and why use it
    * Setting up a project with Vite and `Create React App`
    * Understanding JSX syntax and expressions
    * Components: function components and component composition
    * Props: passing data to components and prop types
    * State: managing component state and reactivity
    * Rendering lists and handling conditional rendering
    * Event handling in `React`
<!-- chapter: react-hooks, duration: 3h -->
* `React` Hooks
    * Introduction to hooks and rules of hooks
    * useState for local state management
    * useEffect for side effects and lifecycle management
    * useContext for consuming context values
    * useReducer for complex state logic
    * useMemo and useCallback for memoization
    * useRef for DOM references and mutable values
    * Building custom hooks for reusable logic
<!-- chapter: component-patterns-and-architecture, duration: 2h -->
* Component Patterns and Architecture
    * Container and presentational components
    * Compound components pattern
    * Render props and higher-order components
    * Controlled vs uncontrolled components
    * Component composition and children patterns
    * Error boundaries for graceful error handling
<!-- chapter: forms-and-controlled-components, duration: 2h -->
* Forms and Controlled Components
    * Handling form inputs and controlled components
    * Form validation strategies
    * Working with `React Hook Form`
    * `File` inputs and complex form fields
    * Multi-step forms and dynamic form generation
<!-- chapter: routing-with-react-router, duration: 3h -->
* Routing with `React Router`
    * Setting up `React Router` in a project
    * Route definitions, path parameters, and nested routes
    * Programmatic navigation and redirects
    * Route guards and protected routes
    * Lazy loading routes with code splitting
    * Search parameters and location state
<!-- chapter: state-management, duration: 3h -->
* State Management
    * Local state vs global state considerations
    * `Context API` for sharing state across components
    * Introduction to `Redux Toolkit` and the `Redux` store
    * Slices, reducers, and actions with `Redux Toolkit`
    * `Async` logic with `Redux Toolkit` createAsyncThunk
    * Zustand as a lightweight state management alternative
    * Choosing the right state management approach
<!-- chapter: fetching-data, duration: 3h -->
* Fetching Data
    * Using the fetch `API` for `HTTP` requests
    * Handling loading states, errors, and caching
    * Introduction to `TanStack Query` (`React Query`)
    * Query keys, caching, and background refetching
    * Mutations and optimistic updates
    * Pagination and infinite scrolling
<!-- chapter: styling-react-applications, duration: 2h -->
* Styling `React` Applications
    * `CSS Modules` for scoped styling
    * styled-components and `CSS`-in-JS approach
    * Utility-first styling with `Tailwind CSS`
    * Theming and design tokens
    * Responsive design in `React` applications
<!-- chapter: testing-react-applications, duration: 3h -->
* Testing `React` Applications
    * Setting up `Jest` and `React Testing Library`
    * Rendering components and querying the DOM
    * Simulating user interactions and events
    * Testing hooks and `async` behavior
    * Mocking modules, `API` calls, and context providers
    * Snapshot testing and `when` to use it
<!-- chapter: performance-optimization, duration: 3h -->
* Performance Optimization
    * Understanding `React` rendering and reconciliation
    * `React`.memo for preventing unnecessary re-renders
    * `React`.lazy and Suspense for code splitting
    * Profiling with `React DevTools`
    * Virtualized lists for large datasets
    * Bundle analysis and optimization strategies
<!-- chapter: typescript-with-react, duration: 2h -->
* `TypeScript` with `React`
    * Typing props, state, and events
    * Typing hooks: useState, useRef, useReducer, useContext
    * Generic components and utility types
    * Typing third-party libraries and declaration files
    * Best practices for `TypeScript` in `React` projects
<!-- chapter: introduction-to-next-js-and-deployment, duration: 3h -->
* Introduction to Next.js and Deployment
    * What is Next.js and server-side rendering
    * Pages, layouts, and the `App Router`
    * Static site generation and server components
    * `API` routes in Next.js
    * Deployment options: `Vercel`, `Netlify`, `Docker` containers
    * Environment variables and production configuration

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
