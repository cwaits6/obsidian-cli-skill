---
name: obsidian-cli
description: "Comprehensive Obsidian vault automation via CLI. Use for: (1) Migrating and reorganizing notes with intelligent property assignment, (2) Creating and managing Obsidian Bases (.base files) for Bases views, (3) Generating Templater templates with dynamic syntax, (4) Batch operations on notes. Prioritizes Obsidian CLI when available; provides native Obsidian workflows as fallback. Claude asks for explicit approval before any edits to your vault."
---

# Obsidian CLI Skill

**Version: 1.12.1 (Obsidian App 1.12.1, CLI Installer 1.5.8)**
**Last Updated: February 14, 2026**
**Status: Fully Documented - All 95+ Commands Covered**

## Overview

This skill enables batch automation of your Obsidian vault using the Obsidian CLI. It intelligently analyzes your notes, assigns properties based on content, and orchestrates migrations, base creation, template generation, and other vault operations.

**Core principle: Claude asks for explicit approval before modifying any of your notes.**

## CRITICAL: Instructions for Claude Models

IMPORTANT: Claude models must ALWAYS follow these rules when using this skill:

1. **ALWAYS consult reference files**: Before proposing ANY obsidian command, ALWAYS read the corresponding reference file from the references/ directory. This is not optional.

2. **NEVER guess command syntax**: Do NOT attempt to construct obsidian commands from memory or general knowledge. Command syntax has been vetted and verified. Reference the documentation.

3. **Reference file structure**: Use this mapping to find the right documentation:
   - File operations → obsidian-cli-files.md
   - Property operations → obsidian-cli-properties.md
   - Search/links → obsidian-cli-search.md
   - Plugin management → obsidian-cli-plugins.md
   - Any other operation → Check the reference list below

4. **Parameter format**: All commands use `param=value` format (NOT --flag format). Always verify exact parameter names in reference files.

5. **Examples provided**: Never construct examples yourself. Always use the pattern from the reference files as a template.

6. **When in doubt**: If you cannot find a command in the reference files, the command may not exist or may require native Obsidian workflows instead.

**Failure to follow these rules will result in command execution failures and vault modification errors.**

## Workflow

All operations follow this pattern:

1. **Analyze** - Claude reads notes/requirements
2. **Propose** - Claude shows you the changes (properties, structure, commands, etc.)
3. **Approve** - You review and approve before any files are modified
4. **Execute** - Obsidian CLI commands make the approved changes

## Obsidian CLI Command Categories

When you need to work with your vault, Claude will:
1. Determine which command category is needed (see below)
2. Read the corresponding reference file for detailed commands
3. Propose the specific CLI commands to run
4. Get your approval
5. Execute via Bash

### File Operations
Moving, renaming, creating, reading, deleting files. Obsidian CLI automatically updates all vault links.
- **See:** [obsidian-cli-files.md](../../references/obsidian-cli-files.md)
- **When to use:** Organizing notes, bulk migrations, file cleanup
- **Key command:** `obsidian move file=<path> to=<newpath>` (handles renaming and moving with auto-link updates)

### Property Operations
Setting, reading, removing properties/frontmatter on notes.
- **See:** [obsidian-cli-properties.md](../../references/obsidian-cli-properties.md)
- **When to use:** Assigning type, context, topic, tags, and other metadata
- **Key commands:** `obsidian property:set name=<prop> value=<val> file=<path>`, `obsidian property:read name=<prop> file=<path>`

### Base Operations
Creating and querying Obsidian Bases (.base files) for creating Bases with structured data.
- **See:** [obsidian-cli-bases.md](../../references/obsidian-cli-bases.md)
- **When to use:** Setting up views to query notes by properties, creating dashboards
- **Key commands:** `obsidian bases`, `obsidian base:query`, `obsidian base:create`

### Template Operations
Creating, reading, and inserting Templater templates.
- **See:** [obsidian-cli-templates.md](../../references/obsidian-cli-templates.md)
- **When to use:** Automating note creation, inserting dynamic content
- **Key commands:** `obsidian templates`, `obsidian template:read`, `obsidian template:insert`

### Search Operations
Searching vault content and links.
- **See:** [obsidian-cli-search.md](../../references/obsidian-cli-search.md)
- **When to use:** Finding notes by content, analyzing link structure
- **Key commands:** `obsidian search`, `obsidian links`, `obsidian backlinks`

### Plugin Operations
Enabling, disabling, managing plugins.
- **See:** [obsidian-cli-plugins.md](../../references/obsidian-cli-plugins.md)
- **When to use:** Automating plugin setup, running plugin commands via CLI
- **Key commands:** `obsidian plugin:enable`, `obsidian plugin:disable`, `obsidian command`

## Common Workflows

### Migrate and Enrich Notes

Reorganize notes to a new folder while intelligently assigning properties:

1. Claude reads your notes from the source folder
2. Using the [property extraction guide](../../references/property-extraction-guide.md), Claude analyzes each note's content
3. Claude proposes properties (type, context, topic, tags, etc.) based on the content
4. You review and approve the proposed properties
5. Claude rewrites each note with the assigned YAML frontmatter (using `obsidian property:set`)
6. Claude moves enriched notes to the destination folder (using `obsidian move`)

**Approval step is mandatory** - Claude will show you the property assignments for each note before applying them.

### Create Obsidian Bases

Generate `.base` files to define Base structures:

1. You describe what data you want to query (e.g., "all how-to notes organized by topic")
2. Claude references your [config.yaml.example](../../config.yaml.example) to understand your property schema
3. Claude proposes the `.base` file structure and view configuration
4. You approve the structure
5. Claude creates the `.base` file using Obsidian CLI
6. Open it in Obsidian to create Base views

### Generate Templater Templates

Create new Templater templates for automating note creation:

1. You describe what the template should do
2. Claude proposes the template content with dynamic Templater syntax
3. You review and approve
4. Claude creates the template file in your Templates folder

## Reference Materials

### Configuration & Schema
- **[config.yaml.example](../../config.yaml.example)** - Template for your property schema (copy to config.yaml)
- **[property-schema.md](../../references/property-schema.md)** - Your universal and conditional properties
- **[property-extraction-guide.md](../../references/property-extraction-guide.md)** - How Claude analyzes content to assign properties

### Vault Understanding
- **[obsidian-bases.md](../../references/obsidian-bases.md)** - How to create and structure `.base` files
- **[templater-plugin.md](../../references/templater-plugin.md)** - Templater syntax and template patterns
- **[native-workflows.md](../../references/native-workflows.md)** - Fallback native Obsidian approaches

### Obsidian CLI Commands (by category)

**Core Operations**
- **[obsidian-cli-files.md](../../references/obsidian-cli-files.md)** - File operations (create, read, move, delete, append, prepend, open)
- **[obsidian-cli-properties.md](../../references/obsidian-cli-properties.md)** - Property/frontmatter management (set, read, remove)
- **[obsidian-cli-vault.md](../../references/obsidian-cli-vault.md)** - Vault and folder operations (info, list files, folders, diff)

**Advanced Features**
- **[obsidian-cli-bases.md](../../references/obsidian-cli-bases.md)** - Base operations (query, create, views)
- **[obsidian-cli-templates.md](../../references/obsidian-cli-templates.md)** - Template operations (list, read, insert)
- **[obsidian-cli-plugins.md](../../references/obsidian-cli-plugins.md)** - Plugin management (enable, disable, install, uninstall)

**Search & Analysis**
- **[obsidian-cli-search.md](../../references/obsidian-cli-search.md)** - Search, links, backlinks, unresolved links, orphans, deadends
- **[obsidian-cli-tags-aliases.md](../../references/obsidian-cli-tags-aliases.md)** - Tag and alias operations
- **[obsidian-cli-outline.md](../../references/obsidian-cli-outline.md)** - Document structure and outline (when created)

**Data Management**
- **[obsidian-cli-tasks.md](../../references/obsidian-cli-tasks.md)** - Task and checkbox operations
- **[obsidian-cli-bookmarks.md](../../references/obsidian-cli-bookmarks.md)** - Bookmark management
- **[obsidian-cli-history.md](../../references/obsidian-cli-history.md)** - File history and recovery (local versions)
- **[obsidian-cli-sync.md](../../references/obsidian-cli-sync.md)** - Sync operations and version control

**UI & Workspace**
- **[obsidian-cli-workspace.md](../../references/obsidian-cli-workspace.md)** - Workspace and tab management
- **[obsidian-cli-themes.md](../../references/obsidian-cli-themes.md)** - Theme installation and management
- **[obsidian-cli-snippets.md](../../references/obsidian-cli-snippets.md)** - CSS snippet management
- **[obsidian-cli-commands.md](../../references/obsidian-cli-commands.md)** - Command execution and hotkey lookup

**Utilities & Development**
- **[obsidian-cli-utilities.md](../../references/obsidian-cli-utilities.md)** - General utilities (version, reload, wordcount, outline, recents)
- **[obsidian-cli-dev.md](../../references/obsidian-cli-dev.md)** - Developer tools (devtools, debugging, inspection, screenshots)

## Important Notes

- **Approval required:** Claude will always show you the commands and ask for approval before executing
- **Direct CLI calls:** Claude calls Obsidian CLI commands directly via Bash (no wrapper scripts)
- **Auto-link updates:** When moving/renaming files, Obsidian CLI automatically updates all vault links
- **File naming:** Normalized automatically to lowercase kebab-case where needed
- **Schema customization:** Always customize [config.yaml.example](../../config.yaml.example) to match your vault
- **CLI limitations:** If a task can't be done via CLI, detailed native Obsidian instructions will be provided
- **Nested operations:** For complex workflows (e.g., migrate + enrich + query), operations happen in sequence with approval at each step
