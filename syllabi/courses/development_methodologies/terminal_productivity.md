---
tags:
  - practices:tools
  - practices:productivity
  - practices:command-line
level: beginner
category: methodology
duration_hours: 16
audience:
  - audiences:developers
---
<!-- course: terminal_productivity -->
# Terminal Productivity

## Description
This course teaches developers how to become highly productive in the terminal by mastering modern command-line tools, shell customization, and terminal workflows. Participants will learn to configure their shell environment, use tmux for multiplexing, replace traditional `Unix` tools with modern alternatives, manage dotfiles, and build personal automation scripts. The course emphasizes practical, immediately applicable techniques that compound into significant productivity gains.

## Duration
16 hours / 1 day

## Intended Audience
* Developers who spend significant time working in the terminal
* Engineers looking to modernize their command-line tooling
* Developers setting up new development environments
* Anyone seeking to improve their day-to-day terminal workflow

## Prerequisites
* Basic familiarity with the command line and shell usage
* Experience navigating the `file` system and running commands in a terminal
* No advanced shell scripting experience required

## Objectives
* Customize shell environments using `bash`, `zsh`, or `fish` with modern prompt frameworks
* Use tmux effectively for session management, window splitting, and persistent workflows
* Replace traditional command-line tools with modern alternatives (`fzf`, `ripgrep`, `fd`, `bat`, `eza`)
* Manage dotfiles using version control and configuration management tools
* Set up efficient `SSH` configurations for managing multiple remote systems
* Build personal automation scripts and workflows for common development tasks

## Outline
<!-- chapter: shell-customization, duration: 1h -->
* Shell Customization
    * Comparing `bash`, `zsh`, and `fish`
    * Shell configuration files and load order
    * Prompt customization and information display
    * `Oh My Zsh` framework and plugins
    * Starship cross-shell prompt
    * Shell options and useful defaults
<!-- chapter: tmux, duration: 2h -->
* tmux
    * Sessions, `windows`, and panes
    * Key bindings and prefix key
    * Splitting and navigating panes
    * Session management and persistence
    * tmux configuration (.tmux.conf)
    * Copy mode and clipboard integration
    * tmux plugin manager (`tpm`)
    * Status bar customization
<!-- chapter: terminal-multiplexing-workflows, duration: 1h -->
* Terminal Multiplexing Workflows
    * Project-specific tmux sessions
    * Scripted session setup
    * tmuxinator and tmux-sessionizer patterns
    * Working with multiple projects simultaneously
    * Remote pairing with tmux
<!-- chapter: shell-aliases-and-functions, duration: 1h -->
* Shell Aliases and Functions
    * Creating and organizing aliases
    * Writing shell functions for complex operations
    * Conditional aliases and platform-specific configuration
    * Abbreviations in `fish` and `zsh`
<!-- chapter: dotfiles-management, duration: 1h -->
* Dotfiles Management
    * Why and how to version control dotfiles
    * `chezmoi` for cross-machine dotfile management
    * `GNU Stow` for symlink-based management
    * Bootstrapping a new machine from dotfiles
    * Secrets management in dotfiles
<!-- chapter: fzf-fuzzy-finder, duration: 1h -->
* `fzf` (Fuzzy Finder)
    * Interactive fuzzy searching
    * `File` and directory fuzzy finding
    * History search with `fzf`
    * `fzf` integration with `Vim`/`Neovim`
    * Custom `fzf` commands and key bindings
    * Preview `windows` and advanced configuration
<!-- chapter: modern-cli-tools, duration: 2h -->
* Modern `CLI` Tools
    * `ripgrep` (rg): fast code searching
    * `fd`: user-friendly `file` finding
    * `bat`: syntax-highlighted `file` viewing
    * `eza` (formerly exa): modern ls replacement
    * z/zoxide: intelligent directory jumping
    * `delta`: improved `git diff` output
    * `jq` and yq for structured data processing
    * httpie and curlie for `HTTP` requests
<!-- chapter: shell-history, duration: 1h -->
* Shell History
    * atuin: shell history database and sync
    * Searching and filtering history effectively
    * History across multiple machines
    * Contextual history (per directory, per project)
<!-- chapter: git-integrations, duration: 1h -->
* `Git` Integrations
    * lazygit: terminal UI for `git`
    * tig: text-mode interface for `git`
    * `git` aliases for common workflows
    * Interactive staging and commit workflows
    * `git` log visualization in the terminal
<!-- chapter: ssh-configuration-and-management, duration: 1h -->
* `SSH` Configuration and Management
    * `SSH` config `file` and host aliases
    * Key management and `ssh`-agent
    * ProxyJump and bastion host configuration
    * Multiplexing `SSH` connections
    * `SSH` tunneling and port forwarding
<!-- chapter: clipboard-integration, duration: 1h -->
* Clipboard Integration
    * Terminal clipboard tools (pbcopy/pbpaste, xclip, wl-copy)
    * tmux clipboard integration
    * Cross-platform clipboard handling
    * Piping output to and from the clipboard
<!-- chapter: terminal-emulators, duration: 1h -->
* Terminal Emulators
    * Alacritty: `GPU`-accelerated terminal
    * Kitty: feature-rich `GPU` terminal
    * WezTerm: `Lua`-configurable terminal
    * Configuration and customization
    * Font selection and rendering
    * Choosing the right terminal emulator
<!-- chapter: scripting-for-automation, duration: 1h -->
* Scripting for Automation
    * Writing reusable shell scripts
    * PATH management and script organization
    * Error handling in shell scripts
    * Combining tools into automation pipelines
    * Task runners and `make` for developer workflows
<!-- chapter: personal-productivity-workflows, duration: 1h -->
* Personal Productivity Workflows
    * Building a daily development workflow
    * Quick-switching between projects
    * Note-taking and task management from the terminal
    * Integrating terminal tools into the development cycle
    * Measuring and improving your own productivity

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
