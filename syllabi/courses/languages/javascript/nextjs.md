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
  - audiences:architects
---
<!-- course: nextjs -->
# Next.js Development

## Description
This course provides a thorough guide to building modern web applications with Next.js and the App Router architecture. Students will learn `React` Server Components, advanced routing patterns, data fetching strategies, rendering techniques (SSR, SSG, ISR, streaming), authentication, styling, and deployment. The course emphasizes building production-grade applications with optimal performance and developer experience.

## Duration
24 hours / 3 days

## Intended Audience
* `React` developers looking to build full-stack, production-grade applications
* Frontend developers who want to leverage server-side rendering and static generation
* Full-stack `JavaScript` or `TypeScript` developers building modern web platforms
* Software engineers transitioning from client-side `React` to server-rendered architectures
* Backend developers looking to understand modern frontend deployment patterns

## Prerequisites
* `Solid` understanding of `React` fundamentals (components, hooks, state, props)
* Proficiency in `JavaScript` (`ES6`+) and basic `TypeScript` knowledge
* Familiarity with `npm` or `yarn` package managers
* Understanding of `HTTP` protocol, `REST APIs`, and web fundamentals
* Basic knowledge of `HTML`, `CSS`, and responsive design
* Experience with command-line tools and `Git`

## Required Knowledge
* `HTML` `CSS` `JavaScript` Fundamentals (or equivalent experience)
* `React` (or equivalent experience)
* `TypeScript` Programming (or equivalent experience)

## Objectives
* Understand the Next.js App Router architecture and `React` Server Components
* Implement `file`-based, dynamic, parallel, and intercepting routes
* Apply rendering strategies including SSR, SSG, ISR, and streaming
* Fetch data using server actions, the fetch `API`, caching, and revalidation
* Distinguish between server and client components and use each appropriately
* Implement authentication with NextAuth.js
* Style applications using `CSS Modules` and `Tailwind CSS`
* Optimize images, fonts, and metadata for performance and SEO
* Deploy Next.js applications to `Vercel` and self-hosted environments
* Write tests for Next.js applications

## Outline
<!-- chapter: introduction-to-next-js-and-the-app-router, duration: 2h -->
* Introduction to Next.js and the App Router
    * Overview of Next.js and its evolution
    * The App Router architecture and directory conventions
    * Creating a Next.js project and project structure
    * `React` Server Components vs client components
    * The `"use client"` and `"use server"` directives
    * Development server, hot reloading, and Turbopack
    * `TypeScript` configuration and support
<!-- chapter: routing-fundamentals, duration: 3h -->
* Routing Fundamentals
    * `File`-based routing and route segments
    * Dynamic routes and catch-all segments
    * Route groups and layout organization
    * Parallel routes and slot-based layouts
    * Intercepting routes and modal patterns
    * Loading, error, and not-found pages
    * Route handlers for `API` endpoints
    * Middleware and request interception
<!-- chapter: layouts-pages-and-navigation, duration: 2h -->
* Layouts, Pages, and Navigation
    * Root layout and nested layouts
    * Template components and layout persistence
    * The Link component and client-side navigation
    * Programmatic navigation with useRouter
    * Active link styling and navigation state
    * Metadata `API` and SEO optimization
    * generateMetadata and dynamic metadata
<!-- chapter: data-fetching-and-caching, duration: 3h -->
* Data Fetching and Caching
    * Server-side data fetching in server components
    * The extended fetch `API` and caching behavior
    * Request memoization and data deduplication
    * Revalidation strategies: time-based and on-demand
    * Server actions for mutations and form handling
    * useFormStatus and useOptimistic hooks
    * Streaming and Suspense for progressive rendering
    * Error handling in data fetching
<!-- chapter: rendering-strategies, duration: 2h -->
* Rendering Strategies
    * Static rendering and build-time generation
    * Dynamic rendering and runtime server-side rendering
    * Incremental Static Regeneration (ISR)
    * Streaming with `React Suspense` boundaries
    * Partial prerendering concepts
    * generateStaticParams for static path generation
    * Understanding the rendering lifecycle
<!-- chapter: authentication-and-authorization, duration: 3h -->
* Authentication and Authorization
    * Authentication patterns in Next.js
    * Setting up NextAuth.js (Auth.js)
    * Credential-based and `OAuth` provider authentication
    * Session management and protected routes
    * Middleware-based route protection
    * Role-based access control
    * Server-side authentication checks
<!-- chapter: styling-and-optimization, duration: 3h -->
* Styling and Optimization
    * `CSS Modules` and component-scoped styles
    * `Tailwind CSS` integration and configuration
    * Global styles and `CSS`-in-JS considerations
    * Image optimization with the Image component
    * Font optimization with next/font
    * Script optimization with next/script
    * Bundle analysis and code splitting
<!-- chapter: testing-and-internationalization, duration: 3h -->
* Testing and Internationalization
    * Testing strategies for Next.js applications
    * Unit testing components with `Jest` and `React Testing Library`
    * Testing server components and server actions
    * End-to-end testing with `Playwright`
    * Internationalization and locale routing
    * Content translation and locale detection
    * Middleware-based locale handling
<!-- chapter: deployment-and-production, duration: 3h -->
* Deployment and Production
    * Deploying to `Vercel`: configuration and previews
    * Self-hosted deployment with `Node.js`
    * `Docker` containerization for Next.js
    * Static export for CDN deployment
    * Environment variables and runtime configuration
    * Monitoring, logging, and error tracking
    * Performance monitoring and Core Web Vitals

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
