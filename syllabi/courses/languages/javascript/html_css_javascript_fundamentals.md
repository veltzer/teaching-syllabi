---
tags:
  - languages:javascript
  - concepts:web-development
  - concepts:programming
level: beginner
category: language
duration_hours: 40
audience:
  - audiences:developers
---
<!-- course: html_css_javascript_fundamentals -->
<!-- Track gaps: TCP/IP fundamentals, HTTP protocol details, web server vs web client architecture, analysis of a connection -->
# `HTML`, `CSS`, and `JavaScript` Fundamentals

## Description
This course provides a `solid` foundation in the three core technologies of the web: `HTML`, `CSS`, and `JavaScript`. Students will learn to structure web pages with semantic HTML5, style them with modern CSS3 including Flexbox and Grid, and add interactivity with `JavaScript`. The course covers `ES6`+ features, DOM manipulation, event handling, asynchronous programming, and essential tooling to prepare students for modern frontend development.

## Duration
40 hours / 5 days

## Intended Audience
* Beginners who want to learn web development from the ground up
* Software developers from other platforms transitioning to web development
* Backend developers who need to understand frontend fundamentals
* Quality assurance engineers who need to understand web technologies
* Anyone interested in building websites and web applications

## Prerequisites
* Basic computer literacy and familiarity with using a web browser
* Ability to work with a text editor or IDE
* No prior programming experience is required, though basic programming concepts are helpful

## Objectives
* Structure web pages using semantic HTML5 elements, forms, and media
* Style web pages with CSS3 including Flexbox, Grid, responsive design, and animations
* Write `JavaScript` programs using variables, types, operators, control flow, functions, arrays, and objects
* Manipulate the DOM and handle user events with `JavaScript`
* Use the fetch `API` to communicate with `web services`
* Apply `ES6`+ features including let/const, arrow functions, template literals, destructuring, spread/`rest`, modules, promises, and async/await
* Use browser developer tools to debug and inspect web applications
* Store data in the browser using `Web Storage`
* Understand modern web development tooling with `npm` and bundlers

## Outline
<!-- chapter: introduction-to-the-web-and-html-basics, duration: 2h -->
* Introduction to the Web and `HTML` Basics
    * How the web works: browsers, servers, `HTTP`, and URLs
    * Setting up a development environment and editor
    * `HTML` document structure: DOCTYPE, `html`, head, body
    * Text elements: headings, paragraphs, lists, and links
    * Images, attributes, and paths
    * Comments and `HTML` validation
<!-- chapter: semantic-html5-and-document-structure, duration: 2h -->
* Semantic HTML5 and Document Structure
    * Semantic elements: header, nav, main, section, article, aside, footer
    * Tables for tabular data
    * The div and span elements
    * Block-level vs inline elements
    * Character entities and special characters
    * `HTML` best practices and document outlining
<!-- chapter: html-forms-and-media, duration: 2h -->
* `HTML` Forms and Media
    * Form elements: input, textarea, select, button
    * Input types: text, email, password, number, date, range, color, file
    * Form attributes: action, method, name, placeholder, required
    * Labels, fieldsets, and form accessibility
    * Audio and video elements
    * Embedding content with iframe
<!-- chapter: accessibility-fundamentals, duration: 2h -->
* Accessibility Fundamentals
    * Why accessibility matters
    * ARIA roles, states, and properties
    * Keyboard navigation and focus management
    * Alt text, labels, and screen reader considerations
    * Semantic markup for accessibility
<!-- chapter: css-fundamentals, duration: 3h -->
* `CSS` Fundamentals
    * Adding `CSS`: inline, internal, and external stylesheets
    * Selectors: element, class, `ID`, attribute, and pseudo selectors
    * The cascade, specificity, and inheritance
    * Colors, backgrounds, and opacity
    * Typography: fonts, text properties, and `Google Fonts`
    * The box model: margin, border, padding, content
    * Units: px, em, rem, %, vw, vh
<!-- chapter: css-layout-with-flexbox-and-grid, duration: 3h -->
* `CSS` Layout with Flexbox and Grid
    * Display property and positioning: static, relative, absolute, fixed, sticky
    * Float and clear (legacy layout)
    * Flexbox: flex container, flex items, alignment, and ordering
    * `CSS Grid`: grid container, grid items, template areas, and gap
    * `When` to use Flexbox vs Grid
    * Building common layouts with Flexbox and Grid
<!-- chapter: responsive-design-and-media-queries, duration: 3h -->
* Responsive Design and Media Queries
    * The viewport meta tag
    * Media queries and breakpoints
    * Mobile-first vs desktop-first approach
    * Responsive images and fluid layouts
    * Responsive typography
    * Testing across devices and screen sizes
<!-- chapter: css-transitions-and-animations, duration: 2h -->
* `CSS` Transitions and Animations
    * `CSS` transitions: property, duration, timing, delay
    * Transform: translate, rotate, scale, skew
    * `CSS` keyframe animations
    * Hover effects and interactive styling
    * Performance considerations for animations
<!-- chapter: javascript-fundamentals, duration: 3h -->
* `JavaScript` Fundamentals
    * Adding `JavaScript` to a web page
    * Variables: var, let, and const
    * Data types: strings, numbers, booleans, null, undefined, symbols
    * Operators: arithmetic, comparison, logical, assignment
    * Type coercion and type checking
    * Control flow: if/else, switch, ternary operator
    * Loops: for, while, do...`while-loop`, `for-loop`...of, for...in
<!-- chapter: functions-arrays-and-objects, duration: 3h -->
* Functions, Arrays, and Objects
    * `Function-declarations` and expressions
    * Arrow functions and concise syntax
    * Parameters, default values, and `return-values`
    * Scope and closures
    * Arrays: creation, access, iteration, and common methods
    * Objects: creation, properties, methods, and object destructuring
    * `Array` destructuring and the spread/`rest` operators
    * Template literals and tagged templates
<!-- chapter: dom-manipulation-and-events, duration: 3h -->
* DOM Manipulation and Events
    * What is the DOM and the document tree
    * Selecting elements: getElementById, querySelector, querySelectorAll
    * Modifying elements: text content, `HTML`, attributes, and classes
    * Creating, appending, and removing elements
    * Event listeners and event types
    * Event propagation: bubbling and capturing
    * Event delegation and handling dynamic content
    * Form events and input handling
<!-- chapter: asynchronous-javascript-and-the-fetch-api, duration: 3h -->
* Asynchronous `JavaScript` and the Fetch `API`
    * Introduction to asynchronous programming
    * Callbacks and callback patterns
    * Promises: creation, chaining, and error handling
    * async/await syntax
    * The fetch `API` for making `HTTP` requests
    * Working with `JSON` data
    * Handling errors and loading states
    * Consuming public `REST APIs`
<!-- chapter: es6-modules-and-modern-features, duration: 3h -->
* `ES6`+ Modules and Modern Features
    * ES modules: import and export
    * Named exports and default exports
    * Map, Set, and other data structures
    * Optional chaining and nullish coalescing
    * `Array` methods: map, filter, reduce, find, some, every
    * String and number methods
    * Iterators and the Symbol type
<!-- chapter: browser-developer-tools-and-web-storage, duration: 3h -->
* Browser Developer Tools and Web Storage
    * Using browser developer tools: Elements, Console, Network, Sources
    * Debugging `JavaScript` with breakpoints and the debugger statement
    * Inspecting `CSS` and layout issues
    * Network tab for monitoring requests
    * localStorage and sessionStorage
    * Reading and writing data in `Web Storage`
    * `JSON` serialization for storage
<!-- chapter: introduction-to-web-development-tooling, duration: 3h -->
* Introduction to Web Development Tooling
    * What is `npm` and the `Node.js` ecosystem
    * Initializing a project with package.`json`
    * Installing and using packages
    * Overview of bundlers: Webpack, Vite, Parcel
    * Introduction to code linting with ESLint
    * Code formatting with Prettier
    * Version control basics with `Git`

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
