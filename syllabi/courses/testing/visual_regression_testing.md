---
tags:
  - concepts:testing
  - concepts:test-quality
  - concepts:web-development
  - concepts:best-practices
level: intermediate
category: testing
duration_hours: 16
audience:
  - audiences:senior-developers
  - audiences:qa-engineers
  - audiences:developers
  - audiences:frontend-developers
---
<!-- course: visual_regression_testing -->
# Visual Regression Testing

## Description
Visual regression testing — taking a screenshot of a page or component and comparing it to a stored
baseline — has matured from a brittle hobby into a reliable engineering practice. The catalog has
`Playwright`, `Advanced Playwright`, `Cypress`, `Selenium`, `Jest`, and `End-to-End Testing Strategy`,
but does not have a focused course on the visual-regression specialty. Visual tests catch what unit
tests and end-to-end tests cannot: a `CSS` change that broke the header, a font swap that shifted
layout, a third-party widget that started rendering differently, a dark-mode regression, an
accessibility-contrast regression, and a responsive-breakpoint failure.

This two day course covers visual regression testing as practiced today. It covers what visual tests
catch (and what they do not), the screenshot-comparison technologies (`pixel-diff`, `perceptual-diff`,
`AI`-based comparators), the canonical tools (`Percy`, `Chromatic`, `Applitools`, `Loki`,
`Playwright`'s `toHaveScreenshot`, `BackstopJS`), the integration with `Storybook` for component-level
visual tests, the integration with `Playwright` and `Cypress` for end-to-end visual tests, the
flakiness sources (fonts, animations, dates, network), the baseline-management workflow, the review
flow (`Percy` and `Chromatic`'s `PR`-based flow), the cost shape, the visual-test pyramid (component,
page, full-flow), and the patterns that `make` visual tests succeed. Examples include real production
visual-test setups. Participants leave able to introduce visual regression testing into a project
without making the test suite hostile.

## Duration
16 hours / 2 days

## Intended Audience
* senior developers wanting to catch visual regressions
* `QA` engineers extending automation to visual coverage
* frontend developers maintaining a design system
* developers adopting `Storybook` or component-driven development

## Prerequisites
* working experience with at least one of `Playwright`, `Cypress`, or `Selenium`
* familiarity with frontend development
* exposure to `Storybook` is helpful but not required
* basic `CI/CD` knowledge

## Objectives
* explain what visual tests catch and what they do not
* deploy at least one visual-test platform
* integrate visual tests into a `CI` pipeline
* manage baselines and the review flow
* eliminate the canonical sources of flakiness
* design the visual-test pyramid
* recognize `when` visual tests are the wrong tool

## Outline
<!-- chapter: what-visual-tests-catch, duration: 1h -->
* What visual tests catch
    * the `CSS` regression
    * the font-swap shift
    * the dark-mode regression
    * the third-party-widget change
    * what unit and `E2E` tests miss
    * the canonical "the page looked broken and nothing alerted"
<!-- chapter: what-visual-tests-do-not-catch, duration: 1h -->
* What visual tests do not catch
    * the functional regression
    * the data-driven content regression
    * the keyboard-navigation regression
    * the screen-reader regression
    * cross-reference to the Web Accessibility course
<!-- chapter: pixel-diff-vs-perceptual-diff, duration: 1h -->
* Pixel-diff vs perceptual-diff
    * exact-pixel comparison
    * perceptual diff and human-tolerance
    * `AI`-based comparators
    * the trade-off
    * the "we got 1000 false positives from anti-aliasing" experience
<!-- chapter: percy-and-chromatic, duration: 2h -->
* `Percy` and `Chromatic`
    * `Percy` overview and `BrowserStack` integration
    * `Chromatic` and the `Storybook` integration
    * the `PR`-based review flow
    * the cost model
    * picking
<!-- chapter: applitools-and-the-ai-approach, duration: 1h -->
* `Applitools` and the `AI` approach
    * the `Visual AI` model
    * the layout-aware comparison
    * the cross-browser story
    * the cost shape
    * `when` `Applitools` wins
<!-- chapter: open-source-tools, duration: 1h -->
* Open-source tools
    * `BackstopJS`
    * `Loki` for `Storybook`
    * `Playwright`'s `toHaveScreenshot`
    * `Cypress` plugins
    * picking
<!-- chapter: storybook-component-tests, duration: 2h -->
* `Storybook` component tests
    * the per-story snapshot
    * the `Chromatic` integration
    * the design-system regression case
    * the per-prop variation
    * worked example
<!-- chapter: end-to-end-visual-tests, duration: 1h -->
* End-to-end visual tests
    * the per-page snapshot
    * the per-flow-step snapshot
    * cross-reference to the Advanced `Playwright` course
    * the maintenance cost
    * picking the pages to cover
<!-- chapter: eliminating-flakiness, duration: 2h -->
* Eliminating flakiness
    * the font-loading wait
    * the animation-disable trick
    * the date-and-time freeze
    * the network-interception
    * the per-platform pixel difference (`Linux` vs `macOS` vs `Windows`)
    * the canonical "tests pass on `CI` and fail locally" reality
<!-- chapter: baseline-management, duration: 1h -->
* Baseline management
    * the per-branch baseline
    * the auto-approve workflow
    * the "we accepted everything for two weeks and missed regressions" failure
    * the bulk-update tool
    * the human-review gate
<!-- chapter: review-flow-in-practice, duration: 1h -->
* Review flow in practice
    * the `PR`-side panel
    * the per-component approval
    * the team norm: who approves
    * the "the visual diff was approved without being looked at" failure
    * the integration with required reviews
<!-- chapter: cross-browser-and-cross-device, duration: 1h -->
* Cross-browser and cross-device
    * `Chrome`, `Firefox`, `Safari`
    * mobile viewports
    * the per-browser baseline cost
    * the "we tested only `Chrome`" gap
    * picking the matrix
<!-- chapter: cost-shape-and-budget, duration: 1h -->
* Cost shape and budget
    * the per-snapshot pricing
    * the `CI`-time cost
    * the storage cost
    * the false-positive triage cost
    * the "we cancelled the contract because it was too expensive" outcome

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
