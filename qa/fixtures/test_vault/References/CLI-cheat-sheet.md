---
type: reference
context: tooling
topic: obsidian
created: 2024-01-11
---

# CLI Cheat Sheet

Quick reference for commonly used obsidian CLI commands.

## File Operations

| Command | Description |
|---------|-------------|
| `obsidian files` | List all files |
| `obsidian read path="note.md"` | Read a note |
| `obsidian search query="term"` | Search vault |
| `obsidian folders` | List all folders |

## Property Operations

| Command | Description |
|---------|-------------|
| `obsidian properties path="note.md"` | Read properties |
| `obsidian property:set path="note.md" key=type value=reference` | Set a property |
| `obsidian property:remove path="note.md" key=draft` | Remove a property |

## Link Analysis

| Command | Description |
|---------|-------------|
| `obsidian links path="note.md"` | Outgoing links |
| `obsidian backlinks path="note.md"` | Incoming links |
| `obsidian links:unresolved` | Find broken links |

## Related

- [[Projects/Automation]]
- [[Notes/Getting-started-with-obsidian]]
