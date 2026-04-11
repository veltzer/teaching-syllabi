---
tags:
  - practices:tools
  - practices:productivity
level: beginner
category: methodology
duration_hours: 16
audience:
  - audiences:developers
---
<!-- course: vim_and_neovim -->
# `Vim` and `Neovim`

## Description
This course introduces `Vim` and `Neovim` as powerful, efficient text editors built around the philosophy of modal editing. Participants will learn core `Vim` navigation and editing commands, progress to advanced features such as macros and registers, and then explore `Neovim`-specific enhancements including `Lua`-based configuration, modern plugin management, and LSP integration. By the end of the course, participants will be able to use `Neovim` as a full-featured development environment.

## Duration
16 hours / 2 day

## Intended Audience
* Developers looking to improve their text editing efficiency
* Engineers who frequently work in terminal-based environments
* Developers interested in using `Neovim` as their primary IDE
* Anyone who wants to leverage `Vim` motions in their existing editor

## Prerequisites
* Basic familiarity with using a terminal and command line
* Experience with at least one programming language
* No prior `Vim` experience required

## Objectives
* Understand `Vim`'s modal editing philosophy and its benefits
* Navigate and edit text efficiently using motions, text objects, and operators
* Use registers, macros, and advanced editing techniques for repetitive tasks
* Configure `Neovim` using init.`lua` and `Lua`-based configuration
* Set up a modern `Neovim` environment with plugins for code completion, navigation, and debugging
* Apply `Vim` motions in other editors such as `VS Code` and `JetBrains` `IDEs`

## Outline
<!-- chapter: vim-philosophy, duration: 1h -->
* `Vim` Philosophy
    * Why modal editing
    * The composability of `Vim` commands
    * Thinking in terms of operators and motions
    * Efficiency through text objects
    * The learning curve and how to approach it
<!-- chapter: modes, duration: 1h -->
* Modes
    * Normal mode: the home mode
    * Insert mode: entering text
    * Visual mode: selecting text (character, line, block)
    * Command-line mode: executing commands
    * Replace mode
    * Switching between modes efficiently
<!-- chapter: navigation, duration: 1h -->
* Navigation
    * Character, word, and line motions
    * Sentence and paragraph motions
    * Searching within a line (f, t, `;`, `,`)
    * Search and n/N navigation
    * Jumping to marks and positions
    * Text objects (iw, aw, `ip`, `i"`, it, etc.)
    * Navigating by matching brackets and tags
<!-- chapter: editing-commands, duration: 1h -->
* Editing Commands
    * Delete (d), change (`c`), yank (y), and put (p)
    * Combining operators with motions and text objects
    * Undo and redo
    * Repeat with .
    * Indentation and formatting
    * Join lines, substitution, and text manipulation
<!-- chapter: searching-and-replacing, duration: 1h -->
* Searching and Replacing
    * / and ? search patterns
    * Regular expressions in `Vim`
    * Substitution with :s and :%s
    * Global command (:g)
    * Search and replace across files
<!-- chapter: buffers-windows-and-tabs, duration: 1h -->
* Buffers, `Windows`, and Tabs
    * Buffer management and the buffer list
    * Splitting `windows` horizontally and vertically
    * Navigating between `windows`
    * Tab pages and `when` to use them
    * Argument list and quickfix list
<!-- chapter: registers, duration: 1h -->
* Registers
    * Named registers (a-z)
    * The unnamed register and numbered registers
    * The system clipboard registers (+, *)
    * The expression register (`=`)
    * Read-only registers
    * Recording and replaying with registers
<!-- chapter: macros, duration: 1h -->
* Macros
    * Recording macros
    * Playing back macros
    * Recursive macros
    * Editing macros via registers
    * Practical macro patterns for code editing
<!-- chapter: configuration, duration: 1h -->
* Configuration
    * .vimrc for `Vim`
    * init.`lua` for `Neovim`
    * Setting options
    * Key mappings (nnoremap, inoremap, etc.)
    * Autocommands
    * `Lua`-based configuration patterns for `Neovim`
<!-- chapter: neovim-differences-and-advantages, duration: 1h -->
* `Neovim` Differences and Advantages
    * `Neovim` vs `Vim`: architecture and goals
    * Built-in LSP client
    * Built-in Treesitter support
    * `Lua` as a first-class configuration language
    * `Async` job control and improved terminal integration
    * `Neovim` ecosystem and community
<!-- chapter: plugin-management, duration: 1h -->
* Plugin Management
    * lazy.nvim plugin manager
    * Installing and configuring plugins
    * Lazy loading for fast startup
    * Plugin dependencies and ordering
    * Managing plugin updates
<!-- chapter: essential-plugins, duration: 1h -->
* Essential Plugins
    * telescope.nvim: fuzzy finding files, buffers, and symbols
    * nvim-treesitter: syntax highlighting and code navigation
    * nvim-lspconfig: Language Server Protocol integration
    * nvim-cmp: autocompletion framework
    * `File` explorer plugins (neo-tree, oil.nvim)
    * Status line and UI enhancements
<!-- chapter: neovim-as-ide, duration: 1h -->
* `Neovim` as IDE
    * Language Server Protocol setup and configuration
    * Code completion, diagnostics, and code actions
    * `Go`-to-definition, references, and hover documentation
    * Debugging with nvim-dap
    * Snippet management
    * `Git` integration (gitsigns, fugitive, diffview)
<!-- chapter: custom-key-mappings, duration: 1h -->
* Custom Key Mappings
    * Leader key patterns
    * Building a personal keymap system
    * Which-key for discoverability
    * Common mapping patterns for productivity
<!-- chapter: terminal-integration, duration: 1h -->
* Terminal Integration
    * `Neovim` built-in terminal
    * Terminal mode and key mappings
    * Toggling terminal `windows`
    * Running build and test commands from `Neovim`
<!-- chapter: vim-motions-in-other-editors, duration: 1h -->
* `Vim` Motions in Other Editors
    * `Vim` extension for `VS Code`
    * IdeaVim for `JetBrains` `IDEs`
    * Capabilities and limitations of `Vim` emulation layers
    * Sharing configuration across editors
    * `When` to use `Vim` motions vs a full `Neovim` setup

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
