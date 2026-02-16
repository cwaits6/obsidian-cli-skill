# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Claude Code plugin** (not a traditional application) that provides Obsidian CLI automation capabilities. It packages 95+ documented Obsidian CLI commands as reference documentation that Claude Code consumes at runtime to automate vault operations. The plugin can include skills, agents, hooks, MCP servers, and other components.

There is no build step, no test suite, and no application code — the project is entirely documentation and configuration files.

## Repository Structure

```
.claude-plugin/marketplace.json    # Plugin marketplace metadata
plugins/obsidian-cli/
  .claude-plugin/plugin.json       # Plugin manifest (version managed by semantic-release)
  config.yaml.example              # User configuration template (property schema, batch settings)
  skills/obsidian-cli/SKILL.md     # Main skill prompt — defines Claude's behavior and workflows
  agents/                          # Subagent definitions (auto-discovered by Claude Code)
  references/                      # CLI command documentation (one file per category)
docs/                              # Local reference docs (gitignored, not distributed)
```

**Key files:**
- `SKILL.md` is the entry point — it defines workflows (migrate, enrich, create bases, generate templates) and instructs Claude to always read reference files before constructing commands.
- `references/FORMAT_STANDARD.md` defines the documentation format all reference files must follow.
- `references/output-format-standard.md` defines how all user-facing output must be formatted (proposals, progress, summaries, errors).
- `config.yaml.example` defines the user's property schema, naming conventions, and batch settings. Users copy this to `config.yaml` (gitignored) for personalization.

## Versioning and Releases

- Automated via **semantic-release** on push to `main` (GitHub Actions)
- Version in `plugins/obsidian-cli/.claude-plugin/plugin.json` is updated automatically during release
- Uses conventional commits: `feat:` → minor, `fix:` → patch, `docs:` for documentation changes
- Commit message format from CONTRIBUTING.md: `docs(reference): improve obsidian-cli-files examples`

## Working with Reference Files

All reference files in `plugins/obsidian-cli/references/` follow the format in `FORMAT_STANDARD.md`:
- File naming: `obsidian-cli-<category>.md`
- Commands use `param=value` format (not `--flag` format)
- Each command needs: syntax block, parameters section, minimum 2 examples
- Include Common Patterns section at end of file

## Important Conventions

- `config.yaml` is gitignored — never commit user configuration
- All file paths in examples should be relative to vault root
- The skill requires Obsidian 1.12.1+ with CLI enabled
- Changes to reference files should be verified against actual `obsidian help` output

## Design References (in docs/, gitignored)

When optimizing skills, creating agents, or restructuring the plugin, consult these local references:

- `docs/skill-design-guide.md` — Anthropic's complete guide to building skills (converted from PDF). Covers frontmatter design, progressive disclosure, trigger phrases, testing, and distribution.
- `docs/claude-code-plugins-reference.md` — Claude Code plugin system reference. Covers the full plugin manifest schema, component types (skills, agents, hooks, MCP servers, LSP servers), directory structure, caching, and CLI commands.
- `docs/claude-code-subagents-reference.md` — Subagent configuration reference. Covers agent frontmatter schema (name, description, model, tools, permissions, hooks, memory, skills), scope/priority, and built-in agents.

These files are gitignored and not distributed with the plugin. They exist as working references for development.
