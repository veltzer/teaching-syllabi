---
tags:
  - languages:javascript
  - concepts:web-development
  - networking:web
  - networking:http
  - practices:performance
level: intermediate
category: language
duration_hours: 16
audience:
  - audiences:developers
  - audiences:performance-engineers
---
<!-- course: web_performance_optimization -->
# Web Performance Optimization

## Description
This course provides a comprehensive guide to measuring, analyzing, and improving web application performance. Participants will learn how to optimize Core Web Vitals, leverage browser rendering efficiently, implement lazy loading and code splitting, optimize assets, and establish performance budgets. The course covers both the theory behind web performance and practical tools and techniques for achieving fast, responsive web experiences.

## Duration
16 hours / 2 days

## Intended Audience
* Web developers seeking to build high-performance applications.
* Performance engineers responsible for monitoring and improving site speed.

## Prerequisites
* Several years of web development experience.
* Understanding of browser rendering and `HTTP` fundamentals.

## Required Knowledge
* `HTML` `CSS` `JavaScript` Fundamentals

## Objectives
* Measure and interpret Core Web Vitals (LCP, FID, CLS).
* Analyze performance using Lighthouse and `PageSpeed Insights`.
* Optimize the critical rendering path for faster page loads.
* Implement lazy loading, code splitting, and tree shaking.
* Apply image and font optimization techniques.
* Configure caching, CDN, and resource hints for optimal delivery.
* Establish and enforce performance budgets.

## Outline
<!-- chapter: core-web-vitals, duration: 1h -->
* Core Web Vitals
    * Largest Contentful Paint (LCP)
    * First Input Delay (FID) and Interaction to Next Paint (INP)
    * Cumulative Layout Shift (CLS)
    * Measuring Core Web Vitals in the field and lab
    * Impact on SEO and user experience
<!-- chapter: performance-measurement-tools, duration: 1h -->
* Performance Measurement Tools
    * Lighthouse audits and scoring
    * `PageSpeed Insights` analysis
    * `Chrome DevTools` Performance panel
    * WebPageTest and synthetic monitoring
    * Real User Monitoring (RUM)
<!-- chapter: critical-rendering-path, duration: 1h -->
* Critical Rendering Path
    * How browsers render pages
    * Render-blocking resources
    * Critical `CSS` extraction
    * Optimizing DOM and CSSOM construction
    * `JavaScript` execution and its impact on rendering
<!-- chapter: lazy-loading, duration: 1h -->
* Lazy Loading
    * Native lazy loading for images and iframes
    * Component-level lazy loading in `React`, Vue, and `Angular`
    * Intersection Observer `API`
    * Loading priorities and strategies
<!-- chapter: code-splitting-and-tree-shaking, duration: 2h -->
* Code Splitting and Tree Shaking
    * Webpack code splitting strategies
    * Dynamic imports
    * Route-based and component-based splitting
    * Tree shaking and dead code elimination
    * Bundle analysis and optimization
<!-- chapter: image-optimization, duration: 2h -->
* Image Optimization
    * Modern formats (WebP, AVIF)
    * Responsive images with srcset and sizes
    * Image compression techniques
    * Image CDNs and on-the-fly transformation
    * SVG optimization
<!-- chapter: font-loading-strategies, duration: 2h -->
* Font Loading Strategies
    * font-display property
    * Font subsetting
    * Preloading fonts
    * Variable fonts
    * Reducing layout shift from font loading
<!-- chapter: cdn-and-delivery-optimization, duration: 2h -->
* CDN and Delivery Optimization
    * CDN architecture and benefits
    * Edge caching strategies
    * `HTTP`/2 features (multiplexing, server push, header compression)
    * `HTTP`/3 and QUIC benefits
    * Connection optimization
<!-- chapter: resource-hints-and-caching, duration: 2h -->
* Resource Hints and Caching
    * preload, prefetch, preconnect, `dns`-prefetch
    * Cache-Control and caching headers
    * Service worker caching strategies
    * ETags and conditional requests
    * Immutable assets and cache busting
<!-- chapter: performance-budgets, duration: 2h -->
* Performance Budgets
    * Defining performance budgets
    * Budget metrics (size, timing, count)
    * Enforcing budgets in `CI/CD`
    * Monitoring and alerting on budget violations
    * Performance culture and team practices

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
