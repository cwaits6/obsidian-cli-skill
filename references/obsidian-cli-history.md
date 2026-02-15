# File History & Recovery Operations

Commands for viewing and recovering file versions using Obsidian Sync.

## history - List file history versions

```bash
obsidian history [file=<name>] [path=<path>]
```

**Parameters:**
- `file=<name>` - Target filename (include path)
- `path=<path>` - Target path (alternative)

**Examples:**
```bash
obsidian history file="Tech/K8s/Helm.md"

obsidian history file="my-note.md" path="My-Notes"
```

## history:list - List files with history

```bash
obsidian history:list
```

**Examples:**
```bash
# Show all files with version history
obsidian history:list
```

## history:read - Read a file history version

```bash
obsidian history:read [file=<name>] [path=<path>] [version=<n>]
```

**Parameters:**
- `file=<name>` - Target filename
- `path=<path>` - Target path
- `version=<n>` - Version number to read

**Examples:**
```bash
obsidian history:read file="my-note.md" version=1

obsidian history:read file="my-note.md" path="My-Notes" version=5
```

## history:restore - Restore a file history version

```bash
obsidian history:restore [file=<name>] [path=<path>] version=<n>
```

**Parameters:**
- `file=<name>` - Target filename
- `path=<path>` - Target path
- `version=<n>` (required) - Version to restore

**Examples:**
```bash
# Restore specific version
obsidian history:restore file="my-note.md" version=3

# Restore with path
obsidian history:restore file="my-note.md" path="My-Notes" version=2
```

## history:open - Open file recovery view

```bash
obsidian history:open [file=<name>] [path=<path>]
```

**Parameters:**
- `file=<name>` - Target filename
- `path=<path>` - Target path

**Examples:**
```bash
obsidian history:open file="my-note.md"

# Open recovery UI
obsidian history:open
```

## Common Patterns

### Find recoverable versions
```bash
obsidian history file="my-important-note.md"
```

### Recover accidental deletion
```bash
obsidian history:list
obsidian history:restore file="deleted-note.md" version=1
```
