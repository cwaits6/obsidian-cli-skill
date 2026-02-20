---
type: project
context: work
topic: tooling
status: active
priority: high
created: 2024-01-08
---

# Automation Project

Build CLI tooling to automate repetitive vault operations: bulk property assignment, file migration, and template generation.

## Objectives

- [ ] Bulk assign properties based on folder and content analysis
- [ ] Migrate notes between folders with automatic re-linking
- [ ] Generate Templater templates from schema definitions
- [x] Set up obsidian CLI integration

## Architecture

The CLI reads vault files directly and applies transformations. No database — the filesystem is the source of truth.

## Log

- **2024-01-08** — Project kickoff
- **2024-01-15** — CLI integration working, see [[Notes/Meeting-2024-01-15]]
- **2024-02-01** — Bulk property assignment prototype complete

## Related

- [[References/CLI-cheat-sheet]]
- [[References/API-endpoints]]
- [[Notes/Quarterly-goals-q1]]
