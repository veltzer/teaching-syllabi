# Testing Bootcamp

## Credits
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com)

## Description
This course is a practical course and is intended for people just entering the IT industry
with no hands on experience with how testing and integration is done in the real world.

At first the course introduces the participants to theoretical ideas of testing.
Second the course moves on to larger systems and introduces git the most used tool
in the industry for source code management
The course then goes on to introducing agile and `CI/CD` and agile/scrum as the most widely
used method for managing code change and application delivery.

The course then introduces `Python` as an invaluable tool for writing tests.

The course then proceeds to web testing and introduces the participants to web architecture
basics and to HTML, CSS and `JavaScript`. The course then delves into `Python` and `Selenium`
as a testing framework for professional web testing.

The course then introduces `Linux` fundamentals and `Linux` programming for people doing testing
on native platforms.

## Duration
304 hours / 38 days

## Intended Audience
* IT Beginners who wish to better understand `CI/CD` and IT workflow and `Selenium` in particular.
* Non beginners who would like to better grasp testing fundamentals

## Prerequisites
* Tech affinity.
* Programming in some language is an advantage.
* Knowledge in web fundamentals is an advantage.
* `Python` is an advantage.

## Objectives
* Understand the fundamentals of software testing.
* Understand basic `CI/CD` concepts.
* Understand agile principles.
* Understand the scrum cycle and methodology.
* Have a basic understanding of how git works.
* Be able to use git basic commands.
* Be able to describe the basics of the web architecture.
* Be able to write HTML, CSS, and `JavaScript` code at a basic level.
* Understand the basic concepts behind `Selenium`.
* Be able to write tests for web applications using `Selenium`.
* Be able to write basic `Linux` native code and test it.

## Outline
* Testing theory (20 hours)
    * Introduction to testing
        * Software testing life-cycle
        * V-model
    * Static techniques
        * Review Process Inspection
    * Control Flow Testing
        * Statement Coverage
        * Branch Coverage
        * Path Coverage
    * Data-Flow Testing
        * Data-Flow graph
        * Data-Flow Coverage
    * Mutation testing
    * Levels of testing
        * Unit testing
            * Dynamic Unit Testing
        * System testing
        * Function level
        * Module level
        * Sub system level
        * End to end
        * Acceptance testing
    * Using aids
        * Stubs
        * Mocks
        * Recordings
    * Measuring software quality
        * Various methods
        * Combining methods
* Agile and Scrum methodologies (40 hours)
    * Agile Principles & Scrum Overview
        * Agile Principles
        * Lean Principles
        * Process control models
        * Incremental and Iterative product development
        * Shifting the focus on product management
        * Overview of the Scrum process
    * The Team
        * Dedicated cross functional teams
        * Conditions for Self-Organization
        * T-shaped people
    * Product Backlog and User Stories
        * Product backlog characteristics
        * User Stories
        * Getting your first backlog
    * Estimation
        * Why comparative estimation works
        * Planning Poker
    * Product Backlog Items
        * Getting backlog items Ready
        * Slicing User stories
    * Sprint Planning
        * Team capacity
        * Facilitating the sprint planning meeting
        * The Sprint backlog
        * Sprint Burndown chart
    * The Sprint
        * Definition of Done
        * How the team should work in a sprint
        * Tools for the ScrumMaster
        * Sustainable Pace
    * Scrum Roles and Responsibilities
        * The Team and building effective teams
        * Scrum Master Responsibilities
        * Product Owner Responsibilities
        * The Scrum Project Community
        * What happens to traditional roles in Scrum?
    * Scrum Meetings
        * Reviews
        * Retrospectives
    * Release Planning
        * Velocity
        * Release Planning
        * Tracking release progress
    * Scaling Scrum
        * Scrum of Scrums
        * Scaling the product backlog
        * Scaling across a program and business areas
        * Distributed Teams
* CD/CD introduction (20 hours)
    * Introduction to `DevOps`
        * What is `DevOps`?
        * What isn't `DevOps`?
        * `DevOps` over traditional development
        * Managing the `DevOps` cultural shift
    * `DevOps` Philosophy
        * CALMS model
        * `DevOps` goals
        * `DevOps` and roles
        * `DevOps` Life-cycle
    * DevSecOps
        * What is it?
        * Thinking like a hacker
        * Threat maps
        * Prevention
    * Continuous Integration
        * What is it?
        * Benefits
        * Workflows
    * Continuous Deployment
        * What is it and why?
        * Continuous development v. Continuous delivery
        * Benefits Workflows
* `Git` (24 hours)
    * Introduction to `Git`
        * History of `Git`
        * Who is using `Git`
        * Adopting `Git`
    * `Git` basics
        * Setting up a local repository
        * Setting up a client to a repository
            * Local
            * Remote
        * The staging area
        * `git add` and `git stage`
        * `git status`
        * `git diff`
        * `git commit`
        * `git log`
        * `git rm`
        * `git mv`
        * `git grep`
    * Configuring `Git`
        * Local and global config files
        * Configuring `Git` commands
        * Configuring signing
        * Adding aliases
        * Ignoring files
    * Undoing things
        * Undoing things in the Staging area
        * `git reset --hard`
        * `git revert`
        * `git rebase`
        * `git restore`
        * `git cherry-pick` and `git-cherry`
        * `git commit --amend`
        * using `git rebase` to split past changes
    * Remote repositories
        * Working with a remote repository
        * Setting up / publishing a repository
        * Understanding the repository structure
        * Working with Multiple remotes
        * Working with GitHub
    * Branches
        * Theory: the many reasons we want local branches
        * Theory: the many reasons we want branches
        * Creating branches
        * Working on branches
        * Committing on branches
        * Moving between branches
        * Visualizing branching activity
        * Pruning local/remote branches
        * `git reflog`
    * Merging changes
        * `git fetch`
        * `git pull`
        * `git rebase`
        * Fast forwarding?
        * Cherry picking
        * Handling conflicts
            * basics
            * using merge tools
    * Merge vs Rebase
        * Which should you choose? (Rebase)
        * Why?
    * Workflows
        * `Git` does not force a workflow
        * Feature branches
        * Development vs production
        * Back porting changes
        * Examples of workflows
            * Working with your own workflow
            * `Jenkins`
            * Working with pull requests
            * `Gerrit`
    * Showing `Git` data
        * `git log`
        * `git show`
        * `git show-branch`
        * `git blame` and `git annotate`
        * `git whatchanged`
        * Visual tools
            * Gitk
            * SourceTree
            * `Git` Kraken
            * `Git` Cola
            * Many more
    * Under the hood
        * Digital signatures overview
        * Core ideas
            * Always on a branch
            * SHA includes all history
            * SHA is unique in the world
        * Core concepts
            * The three core structures: commit, tree, blob
            * Commits point to previous commit
            * Commits point to trees
            * Trees point to blobs (never store anything twice)
        * .git:
            * The `Git` object store and how it works
            * What branch am I on?
            * What commit am I on?
            * Where are the tags?
            * Where are the heads?
            * Where are the remotes?
        * What happens when you
            * add to staging area (the index)
            * commit
            * create a branch
            * create an annotated tag
    * Worktrees
        * Why are they needed?
        * Creating a worktree
        * Working with worktrees
        * Pruning worktrees
    * Tagging
        * Why tag?
        * Difference between annotated and non annotated tags
        * Pushing and pulling tags
        * Using tags in other `Git` commands
    * Rewriting History
        * Why you should never do it
        * How to do it anyway
    * Understanding revisions (git revisions)
        * Various things git understands
            * \<branch\>
            * \<object\>
            * \<commit\>
            * \<commit-ish\>
            * \<tree\>
            * \<tree-ish\>
            * \<pathspec\>
        * Commit-ish vs Tree-ish
        * git rev-parse
    * Stashing
        * Why would you want stashing?
        * Creating and naming stashes
        * Apply a specific stash
        * Delete stashes
    * `Git` hooks
        * How to set up hooks?
        * What guarantees do you get?
    * Build in tools
        * `git instaweb`
        * `git daemon`
        * `git http-backend`
        * `git shell`
        * `git export`
        * `git bisect`
        * `git describe`
        * `git archive`
        * `git bundle`
        * `git submodule`
        * `git notes`
    * `Git` tools
        * `Git` and programming languages: GitPython
        * `Git` and development platforms: GitHub, BitBucket, Gitlab
        * `Git` and `IDEs`: `PyCharm`, `Eclipse`, Spyder
        * `Git` and CICD tools: `Jenkins`, Bamboo
* `Python` (40 hours)
    * Introduction to `Python`
        * History of `Python`
        * Why `Python`?
        * `Python` is an `OO` language
        * `Python` is a dynamic language (what does that mean?)
        * Basic `OO` principles (for those who need them)
        * Comparison of `Python` with other programming languages
    * Your first `Python` program
        * How to install the `Python` programming environment
        * Your first script
        * Running your script
        * `IDEs` and tools for `Python`
    * Types and operators
        * Why do we need basic types
        * Numbers
        * Strings
        * Lists
        * Dictionaries
        * Tuples
        * Files
        * Object properties
    * Basic statements
        * Assignments
        * Expressions
        * Print
        * Conditionals
        * Loops (while, for)
    * Functions
        * Why do we need functions
        * Basics
        * Scoping
        * Argument passing
    * Modules
        * Why do we need modules
        * Basics
        * Namespaces
        * Importing modules
        * Reloading modules
    * Classes
        * Why do we need classes
        * Basics
        * The class statement
        * Using class methods
        * Inheritance in `Python`
        * Operator overloading
        * Namespace lookup rules
        * Design using classes
    * Exceptions
        * Why do we need exceptions
        * Basics
        * How are exceptions used
        * Catching modes
    * Systems programming in `Python`
        * IO
        * processes
        * threads
        * pipes
        * signals
    * Using third party modules and packaging modules
        * Built in `Python` modules
        * Downloading, installing and using modules off the net
        * Writing your own module and uploading it
* Web fundamentals (40 hours)
    * Web architecture
        * `TCP`/IP
        * Server and clients
        * An analysis of a connection
        * `HTTP`: the protocol
        * Web servers and web clients
    * Introduction to Web Programming (HTML)
        * Understanding How Websites Work
        * Understanding How web pages are Structured
        * Understanding How HTML Pages Fit into that Context
    * Creating a Proper HTML Document Structure
        * Basics of Creating a HTML Document
        * Role of HTML, CSS, and `JavaScript`
        * Understanding HTML Elements
        * Common Elements
        * Classes
        * IDs
        * Entities
    * An Introduction to CSS
        * Understanding Basic CSS Concepts
        * Adding Inline CSS
        * Linking to External Stylesheets
        * Understanding Font, Color, and Other CSS Property Changes
    * `JavaScript`
        * Why do we need it?
        * Basic type system
        * Writing functions
        * The DOM
        * Manipulating the DOM
        * Object oriented `JavaScript`
* Introduction to `Selenium` (40 hours)
    * An Overview of `Selenium`
        * Web Testing
        * Web Testing Automation
        * A History of `Selenium`
    * Automated Web Testing Goals
        * Assertion/Verify
        * Locating Elements
        * Matching
        * Waiting
        * Storing
        * `JavaScript`
        * Multi-Window support
        * Debugging
        * Test Suites
    * `Selenium` `IDE`
        * Installation and Setup
        * Building Tests
        * Running Tests
    * `Selenium` Commands
        * Building Tests with `Selenium` `IDE`
        * Running Tests with `Selenium` `IDE`
    * `Selenium` Web Driver
        * What is it?
        * Setup
        * Underlying behavior
        * Language choices
        * Writing tests with Web-Driver
        * Running tests with Web-Driver
        * Waits
        * Browser Startup
        * Remoting
    * `Selenium` Remote Control
        * What is it?
        * How is it different from Web Driver?
        * Why would you use it?
        * Setup
        * Language choices
        * Writing tests with RC
        * Running tests with RC
        * Using Client Libraries
        * Reporting
    * Techniques For Testing
        * What Tests?
        * When?
        * Best Practices for Testing Your Apps
        * Best Practices And Patterns
        * Toolbox
    * `Selenium` Grid
        * What is it?
        * Why would you do it?
        * How do you set it up?
        * Configuration
        * Common Errors.
    * `Selenium` In Real Life
        * Issues
        * Continuous Integration
    * `Selenium` 2.0
        * Key Features
* `Linux` fundamentals (40 hours)
    * Introduction to `UNIX`
        * What is `UNIX`
        * History of `UNIX`
        * Operating system core structure
        * The process tree
            * Why is it important?
            * Adoption by init
            * Zombies
        * What are system calls?
        * Basic security
            * file system security
            * processes as separate boxes
        * The root user
            * Not different from regular user
            * System calls do not get refused
    * The basics
        * Logging in/out
        * Changing your password
        * Command structure
        * Simple commands
        * Control characters
    * File system
        * Basic structure
        * Paths (relative and absolute)
        * Home directories
        * Moving around commands (cd, `PWD`, `pushd`, `popd`
    * Shells
        * Why a shell?
        * The two main families of shells (csh/tcsh, sh/ksh/bash)
        * defining shell variables (csh/tcsh and sh/ksh/bash).
        * exporting as environment variables (csh/tcsh and sh/ksh/bash).
        * command line substitution (csh/tcsh and sh/ksh/bash).
        * glob patterns on the command line (csh/tcsh and sh/ksh/bash).
        * redirection of input, output and errors. (csh/tcsh and sh/ksh/bash).
        * aliases (csh/tcsh and sh/ksh/bash).
        * pipes (csh/tcsh and sh/ksh/bash).
        * command history (csh/tcsh and sh/ksh/bash).
        * session initialization files (csh/tcsh and sh/ksh/bash)
    * Manipulating files, folders, and whole disks
        * `ls`
        * `cat, more`
        * `head, tail`
        * `tee`
        * `wc, diff`
        * `touch`
        * `mkdir, rmdir`
        * `mv, cp`
        * `df, du`
        * `tr, cut`
        * `uniq, sort`
        * `xargs, find`
        * `grep`
        * `sed, awk`
        * What are power tools good for?
        * Exercise with power tools.
    * Files in details
        * File types in `UNIX` (all 7 types).
        * The INODE concept
        * ls and INODES
        * Symbolic links (ln -s)
        * Hard links (ln)
    * Security in practice
        * `UNIX` accounts.
        * The `/etc/passwd` and `/etc/shadow` files.
        * File ownership.
        * Directory and file access modes.
        * How File and Directory access is determined.
        * Changing modes and ownership (`chmod`, `chown`) in symbolic and octal forms.
        * `umask`
    The `vi` text editor
        * Introduction to `vi`
        * The `vi` command
        * `vi` modes
        * insert mode
        * moving around
        * command mode
        * command commands
        * search and replace
    * Process management
        * The ps command
        * Finding the pid of a process
        * Sending a signal to a process (kill).
        * Monitoring processes with top.
        * Dealing with zombies in practice.
        * The shell and jobs.
    * Networking basics
        * The client/server model.
        * `ifconfig`, `ifup`, `ifdown`
        * `telnet`, `rlogin`, `rcp`, `rsh`, `trust`
    * Shell scripting introduction (in sh/ksh/bash family of shells)
        * Writing your first shell script
        * Variables
        * Command line arguments
        * Mathematical operations
        * Exit status and error handling
        * Expressions, operators and conditions
        * Flow control (test, if, elif, case)
        * Loops (for while until)
    * The `Linux` boot system (`systemd`)
        How the `Linux` system boots
        * old `SysV` init system
        * new `systemd`
        * `rc.local` and adding your own initialization code
        * writing your own `/etc/init.d` script
* `Bash` programming (40 hours)
    * Theory
        * What is a shell ?
        * Why do we need a shell?
        * How is a shell better than a GUI?
        * The shell as a game.
        * Shell families.
        * The history of ksh and bash.
    * Shell basics
        * Single command and arguments
        * Semi colons
        * Escaping the shell
    * Environment and shell variables
        * Defining
        * Deleting
        * Demoting and promoting
        * Checking if they exist
    * Redirection
        * Redirecting standard output
        * Redirecting standard error
        * Redirecting standard input
        * Doing other tricks with redirection
    * Globbing
        * asterisk
        * question mark
        * characters classes
        * negation
        * several options
    * Expansion
        * curly braces and comma
        * several options
    * The return code
        * return code on the command line
        * return code if a script
    * Writing you first script
        * editors
        * shbang line
        * chmodding and why
        * extensions for scripts
        * failure in a script
        * prohibiting failure in a script
        * return code of an entire script
        * exiting early with code
        * using wrong variable names
        * using strict variable names
        * debugging your script
    * Syntax
        * Conditionals.
            * no brace
            * left straight brace
            * two left straight braces
        * `while` loops
    * Pipes
        * How to use them
        * How do they work
    * IO
        * reading from a file
        * writing to a file
        * writing data to process
        * reading data from process
    * Redirection in scripts
        * Redirecting for entire scripts
        * Restoring from redirection
    * Multi processing
        * launching sub processes
        * getting their return code
        * launching more than one sub process and collecting their codes
    * Writing bash functions
        * return code of functions
        * passing parameters to functions
        * passing parameters by reference
    * Using variable types
        * strings
        * arrays
        * associative arrays
    * Doing arithmetic
        * integer arithmetic
        * floating point arithmetic
    * Timing
    * Exception handling
    * Object oriented programming
    * Test harnesses
    * Aliases
