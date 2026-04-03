---
tags:
  - tools:junit5
  - languages:java
  - practices:testing
  - concepts:tdd
level: intermediate
category: testing
duration_hours: 16
audience:
  - audiences:developers
  - audiences:java-developers
---
<!-- course: junit5 -->
# `JUnit 5`

## Description
This course provides a comprehensive introduction to `JUnit 5`, the modern testing framework for `Java` applications, covering its modular architecture and powerful new features. Students will learn to write expressive tests using the `JUnit Jupiter` `API`, apply parameterized and lifecycle-aware testing, and extend the framework through its extension model. Integration with `Mockito` for mocking and best practices for integration testing patterns are also covered. The course closes with a practical guide to migrating existing `JUnit 4` test suites to the new platform.

## Duration
16 hours / 2 days

## Intended Audience
* `Java` developers who are new to `JUnit 5` or still using `JUnit 4`
* Backend engineers who want to write more expressive and maintainable tests
* Team leads responsible for establishing `Java` testing standards

## Prerequisites
* `Solid` experience writing `Java` applications
* Familiarity with basic unit testing concepts
* Experience with `Maven` or `Gradle` build tools
* Some exposure to `JUnit 4` or another `Java` testing framework is helpful

## Objectives
* Understand the modular architecture of the `JUnit 5` platform
* Write clear tests using `JUnit Jupiter` annotations and lifecycle hooks
* Use assertion and assumption APIs for precise, readable test conditions
* Create parameterized tests from a variety of data sources
* Extend `JUnit 5` behaviour with the `Extension` `API`
* Control test execution order and enable conditional test execution
* Mock dependencies with `Mockito` alongside `JUnit 5`
* Design integration tests using common `Java` persistence and web patterns
* Migrate a `JUnit 4` test suite to `JUnit 5` systematically

## Outline
<!-- chapter: junit5-architecture-overview, duration: 1h -->
* `JUnit 5` Architecture Overview
    * The three sub-projects: `JUnit Platform`, `JUnit Jupiter`, `JUnit Vintage`
    * Test engine and launcher concepts
    * Integrating `JUnit 5` with `Maven` and `Gradle`
    * IDE support in `IntelliJ IDEA` and `Eclipse`
    * Running tests from the command line with the `ConsoleLauncher`
    * Key differences from `JUnit 4`
<!-- chapter: writing-tests-with-junit-jupiter, duration: 2h -->
* Writing Tests with `JUnit Jupiter`
    * `@Test`, `@DisplayName`, and test method visibility rules
    * `@BeforeEach`, `@AfterEach`, `@BeforeAll`, `@AfterAll` lifecycle annotations
    * Nested test classes with `@Nested`
    * Grouping related tests and expressing structure
    * `@Tag` for categorising and filtering tests
    * Disabling tests with `@Disabled`
<!-- chapter: assertions-and-assumptions, duration: 2h -->
* Assertions and Assumptions
    * Core assertions in `org.junit.jupiter.api.Assertions`
    * Grouped assertions with `assertAll`
    * Exception testing with `assertThrows` and `assertDoesNotThrow`
    * Timeout assertions with `assertTimeout` and `assertTimeoutPreemptively`
    * Using third-party assertion libraries: `AssertJ` and `Hamcrest`
    * Assumptions: `assumeTrue`, `assumeFalse`, `assumingThat`
<!-- chapter: parameterized-tests, duration: 2h -->
* Parameterized Tests
    * Introduction to `@ParameterizedTest`
    * Value sources: `@ValueSource`, `@EnumSource`, `@NullSource`, `@EmptySource`
    * `@CsvSource` and `@CsvFileSource` for tabular data
    * `@MethodSource` for complex argument types
    * `@ArgumentsSource` and custom argument providers
    * Argument converters and aggregators
    * Naming parameterized test cases
<!-- chapter: test-lifecycle-and-extensions, duration: 2h -->
* Test Lifecycle and Extensions
    * Test instance lifecycle: per-method vs per-class
    * The `Extension` `API` and `ExtensionContext`
    * Implementing `BeforeEachCallback` and `AfterEachCallback`
    * Parameter resolution with `ParameterResolver`
    * Conditional execution with `ExecutionCondition`
    * Exception handling extensions
    * Registering extensions: declarative and programmatic approaches
    * `@ExtendWith` vs `@RegisterExtension`
<!-- chapter: test-ordering-and-conditions, duration: 1h -->
* Test Ordering and Conditions
    * Default test method ordering behaviour
    * `@TestMethodOrder` with `MethodOrderer` implementations
    * `@TestClassOrder` for nested test classes
    * Built-in conditional annotations: `@EnabledOnOs`, `@EnabledOnJre`, `@EnabledIfSystemProperty`
    * `@EnabledIfEnvironmentVariable` for CI-aware test skipping
    * Writing custom condition implementations
<!-- chapter: mocking-with-mockito, duration: 3h -->
* Mocking with `Mockito`
    * `Mockito` in the `JUnit 5` ecosystem: `MockitoExtension`
    * `@Mock`, `@InjectMocks`, and `@Spy` annotations
    * Stubbing with `when`/`thenReturn` and `doReturn`/`when`
    * Argument matchers: `any()`, `eq()`, `argThat()`
    * Verifying interactions with `verify` and `verifyNoMoreInteractions`
    * Capturing arguments with `ArgumentCaptor`
    * Mocking `static-methods` with `mockStatic`
    * Mocking constructors and `final-classes`
<!-- chapter: integration-testing-patterns, duration: 2h -->
* Integration Testing Patterns
    * Distinguishing unit tests from integration tests
    * Testing persistence layers with `@DataJpaTest` and `Spring Boot Test`
    * In-memory databases vs containerised databases in tests
    * Testing `REST` APIs with `MockMvc` and `WebTestClient`
    * Transaction management in integration tests
    * Test slices and context caching in `Spring Boot`
    * Organising integration tests separately from unit tests
<!-- chapter: migration-from-junit4, duration: 1h -->
* Migration from `JUnit 4`
    * Running `JUnit 4` tests on the `JUnit 5` platform with `junit-vintage-engine`
    * Annotation mapping: `@Before`→`@BeforeEach`, `@RunWith`→`@ExtendWith`
    * Migrating `@Rule` and `@ClassRule` to extensions
    * Replacing Hamcrest and `@Test(expected=...)` patterns
    * Incremental migration strategies for large codebases
    * Common pitfalls and how to avoid them

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
