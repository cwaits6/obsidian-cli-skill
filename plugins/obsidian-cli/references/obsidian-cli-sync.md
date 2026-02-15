# Sync Operations

Commands for managing Obsidian Sync functionality.

## sync - Pause or resume sync

```bash
obsidian sync [on] [off]
```

**Parameters:**
- `on` - Flag: enable sync
- `off` - Flag: disable sync

**Examples:**
```bash
# Check sync status
obsidian sync

# Enable sync
obsidian sync on

# Disable sync
obsidian sync off
```

## sync:status - Show sync status

```bash
obsidian sync:status
```

**Examples:**
```bash
# Check current sync status
obsidian sync:status
```

## sync:deleted - List deleted files in sync

```bash
obsidian sync:deleted [total]
```

**Parameters:**
- `total` - Flag: show count

**Examples:**
```bash
obsidian sync:deleted

obsidian sync:deleted total
```

## sync:history - List sync version history for a file

```bash
obsidian sync:history [file=<name>] [path=<path>] [total]
```

**Parameters:**
- `file=<name>` - Target filename
- `path=<path>` - Target path
- `total` - Flag: show count

**Examples:**
```bash
obsidian sync:history file="my-note.md"

obsidian sync:history file="my-note.md" total
```

## sync:read - Read a sync version

```bash
obsidian sync:read [file=<name>] [path=<path>] version=<n>
```

**Parameters:**
- `file=<name>` - Target filename
- `path=<path>` - Target path
- `version=<n>` (required) - Version number

**Examples:**
```bash
obsidian sync:read file="my-note.md" version=2
```

## sync:restore - Restore a sync version

```bash
obsidian sync:restore [file=<name>] [path=<path>] version=<n>
```

**Parameters:**
- `file=<name>` - Target filename
- `path=<path>` - Target path
- `version=<n>` (required) - Version to restore

**Examples:**
```bash
obsidian sync:restore file="my-note.md" version=1
```

## sync:open - Open sync history view

```bash
obsidian sync:open [file=<name>] [path=<path>]
```

**Parameters:**
- `file=<name>` - Target filename
- `path=<path>` - Target path

**Examples:**
```bash
obsidian sync:open

obsidian sync:open file="my-note.md"
```

## Common Patterns

### Check sync health
```bash
obsidian sync:status
obsidian sync:deleted total
```

### Recover from sync
```bash
obsidian sync:history file="affected-note.md"
obsidian sync:restore file="affected-note.md" version=1
```
