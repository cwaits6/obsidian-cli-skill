# Workspace & Tab Operations

Commands for managing workspace and tab layout.

## workspace - Show workspace tree

```bash
obsidian workspace [ids]
```

**Parameters:**
- `ids` - Flag: show tab IDs

**Examples:**
```bash
# Show workspace structure
obsidian workspace

# Show with IDs
obsidian workspace ids
```

## tabs - List open tabs

```bash
obsidian tabs [ids]
```

**Parameters:**
- `ids` - Flag: show tab IDs

**Examples:**
```bash
# List all open tabs
obsidian tabs

# Show with IDs
obsidian tabs ids
```

## tab:open - Open a new tab

```bash
obsidian tab:open [group=<id>] [file=<path>] [view=<type>]
```

**Parameters:**
- `group=<id>` - Tab group ID
- `file=<path>` - File to open in tab
- `view=<type>` - View type (e.g., markdown, kanban)

**Examples:**
```bash
# Open new tab
obsidian tab:open

# Open file in new tab
obsidian tab:open file="Tech/K8s/Helm.md"

# Open with specific view type
obsidian tab:open file="my-base.base" view=table
```

## Common Patterns

### Get workspace layout
```bash
obsidian workspace ids
```

### Manage tabs
```bash
obsidian tabs
obsidian tab:open file="my-note.md"
```
