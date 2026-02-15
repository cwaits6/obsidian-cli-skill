# Obsidian CLI Skill

[![GitHub Release](https://img.shields.io/github/v/release/cwaits6/obsidian-cli-skill?style=flat-square)](https://github.com/cwaits6/obsidian-cli-skill/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Comprehensive Obsidian CLI automation skill for Claude Code. Features 95+ fully documented CLI commands organized by category with complete syntax reference, real-world examples, and common patterns.

## Features

- Migrate and enrich notes with intelligent property assignment
- Create and query Obsidian Bases (database views and structured data)
- Bulk file operations (move, rename, delete with auto-link updates)
- Generate Templater templates for note automation
- Comprehensive search and link analysis
- Full sync and version control support
- Plugin management and command execution
- 95+ commands fully documented with examples

## Installation

In Claude Code terminal:

```bash
/plugin install cwaits6/obsidian-cli-skill
```

## Quick Start

Once installed, use the skill directly in Claude Code:

```bash
# Migrate and enrich notes with properties
I want to migrate all my notes from the Research folder to my Notes folder with automatic property assignment based on content

# Create a Base to view your notes organized by properties
Set up an Obsidian Base to view all how-to notes organized by topic

# Analyze your vault structure
Find all unresolved links and orphaned notes in my vault

# Bulk update properties
Add type: reference and context: work properties to all files in my research folder

# Search and discover
Show me all notes linking to my kubernetes reference with usage counts
```

## Documentation

Complete command documentation organized by category in `references/`:

**Core Operations**
- [obsidian-cli-files.md](references/obsidian-cli-files.md) - File operations
- [obsidian-cli-properties.md](references/obsidian-cli-properties.md) - Property management
- [obsidian-cli-vault.md](references/obsidian-cli-vault.md) - Vault operations

**Advanced Features**
- [obsidian-cli-bases.md](references/obsidian-cli-bases.md) - Base operations
- [obsidian-cli-templates.md](references/obsidian-cli-templates.md) - Template generation
- [obsidian-cli-plugins.md](references/obsidian-cli-plugins.md) - Plugin management

**Search & Analysis**
- [obsidian-cli-search.md](references/obsidian-cli-search.md) - Search and links
- [obsidian-cli-tags-aliases.md](references/obsidian-cli-tags-aliases.md) - Tags and aliases
- [obsidian-cli-tasks.md](references/obsidian-cli-tasks.md) - Task management

**Data Management**
- [obsidian-cli-bookmarks.md](references/obsidian-cli-bookmarks.md) - Bookmarks
- [obsidian-cli-history.md](references/obsidian-cli-history.md) - Version history
- [obsidian-cli-sync.md](references/obsidian-cli-sync.md) - Sync operations

**UI & Workspace**
- [obsidian-cli-workspace.md](references/obsidian-cli-workspace.md) - Workspace management
- [obsidian-cli-themes.md](references/obsidian-cli-themes.md) - Theme management
- [obsidian-cli-snippets.md](references/obsidian-cli-snippets.md) - CSS snippets
- [obsidian-cli-commands.md](references/obsidian-cli-commands.md) - Command execution

**Utilities**
- [obsidian-cli-utilities.md](references/obsidian-cli-utilities.md) - General utilities
- [obsidian-cli-dev.md](references/obsidian-cli-dev.md) - Developer tools

## Configuration

Copy `config.yaml.example` to your Claude skills directory and customize for your vault:

```bash
cp config.yaml.example ~/.claude/skills/obsidian-cli/config.yaml
```

Edit with your vault settings, property types, and naming conventions.

## How It Works

All operations follow an approval-first workflow:

1. **Analyze** - Claude reads your vault or requirements
2. **Propose** - Claude shows the exact commands that will run
3. **Approve** - You review and approve before any changes
4. **Execute** - Commands are run via Obsidian CLI

This ensures you maintain full control over your vault modifications.

## Requirements

- Obsidian 1.12.1 or later
- Obsidian CLI enabled
- Claude Code with plugin support

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

## License

MIT License - See [LICENSE](LICENSE) for details.
