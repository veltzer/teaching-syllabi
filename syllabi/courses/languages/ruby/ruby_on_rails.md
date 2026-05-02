---
tags:
  - languages:ruby
  - concepts:web-development
  - networking:web
  - concepts:design-patterns
level: intermediate
category: language
duration_hours: 24
audience:
  - audiences:developers
---
<!-- course: ruby_on_rails -->
# `Ruby on Rails`

## Description
`Ruby on Rails` is a full-stack web application framework built on the Ruby programming language, following convention over configuration and the MVC architectural pattern. This course covers the essential components of Rails development from routing and controllers through ActiveRecord `ORM`, views, testing, and deployment. Students will learn to build robust, maintainable web applications using modern Rails practices.

## Duration
24 hours / 3 days

## Intended Audience
* Developers building web applications with `Ruby on Rails`
* Backend developers learning a full-stack framework
* Developers migrating from other web frameworks to Rails

## Prerequisites
* Basic Ruby programming knowledge
* Familiarity with `HTML`, `CSS`, and `HTTP`
* Basic understanding of relational databases and `SQL`

## Objectives
* Understand the MVC architecture in Rails
* Build data models with ActiveRecord and migrations
* Create RESTful routes, controllers, and views
* Implement authentication and authorization
* Write tests with `RSpec` and Capybara
* Deploy Rails applications to production

## Outline
<!-- chapter: introduction-to-ruby-on-rails, duration: 2h -->
* Introduction to `Ruby on Rails`
    * Rails philosophy (convention over configuration, DRY)
    * MVC architecture overview
    * Installing Ruby and Rails
    * Project structure and directory layout
    * Rails generators
    * The Rails console
    * Bundler and Gemfile
<!-- chapter: routing, duration: 2h -->
* Routing
    * RESTful routes and resources
    * Route helpers
    * Nested routes
    * Member and collection routes
    * Namespaced routes
    * Route constraints
<!-- chapter: controllers, duration: 2h -->
* Controllers
    * Controller actions and the request cycle
    * Parameters (params, strong parameters)
    * Filters (before_action, after_action, around_action)
    * Rendering and redirecting
    * Flash messages
    * Session and cookies
    * Respond to different formats (`HTML`, `JSON`)
<!-- chapter: activerecord-orm, duration: 2h -->
* ActiveRecord `ORM`
    * Models and database tables
    * Migrations (creating, modifying, rolling back)
    * `CRUD` operations
    * Query interface (where, order, limit, joins, includes)
    * Scopes
    * Callbacks
    * Transactions
<!-- chapter: associations, duration: 2h -->
* Associations
    * belongs_to and has_many
    * has_many :through
    * has_one
    * Polymorphic associations
    * Self-referential associations
    * Eager loading and N+1 query prevention
<!-- chapter: views-and-templates, duration: 2h -->
* Views and Templates
    * ERB templates
    * Layouts
    * Partials and rendering collections
    * View helpers
    * Form helpers and form builders
    * Asset pipeline and Webpacker
    * Turbo and Stimulus (Hotwire)
<!-- chapter: validations-and-forms, duration: 2h -->
* Validations and Forms
    * Model validations (presence, uniqueness, format, custom)
    * Error messages and display
    * Form objects
    * Nested forms (accepts_nested_attributes_for)
    * `File` uploads with Active Storage
<!-- chapter: authentication-with-devise, duration: 2h -->
* Authentication with Devise
    * Installing and configuring Devise
    * User registration and login
    * Password recovery
    * Confirmable and lockable modules
    * OmniAuth integration
    * Authorization patterns
<!-- chapter: testing-with-rspec-and-capybara, duration: 2h -->
* Testing with `RSpec` and Capybara
    * `RSpec` setup and configuration
    * Model specs
    * Request specs
    * System tests with Capybara
    * Factories with FactoryBot
    * Mocking and stubbing
    * Test coverage
<!-- chapter: action-cable-websockets, duration: 2h -->
* `Action Cable` (WebSockets)
    * Real-time features overview
    * Channels and subscriptions
    * Broadcasting messages
    * Client-side `JavaScript`
    * Connection authentication
<!-- chapter: active-job, duration: 2h -->
* `Active Job`
    * Background job processing
    * Job queues and adapters (Sidekiq, Delayed Job)
    * Mailers with Action Mailer
    * Scheduled jobs
    * Error handling and retries
<!-- chapter: deployment, duration: 2h -->
* Deployment
    * Production environment configuration
    * Database setup for production
    * Asset precompilation
    * Deploying to cloud platforms
    * Puma configuration
    * Logging and monitoring
    * Security best practices

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
