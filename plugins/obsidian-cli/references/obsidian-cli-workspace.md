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

## workspaces - List saved workspaces

```bash
obsidian workspaces [total]
```

**Parameters:**
- `total` - Flag: show workspace count

**Examples:**
```bash
# List saved workspaces
obsidian workspaces

# Show workspace count
obsidian workspaces total
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

## workspace:save - Save current layout as workspace

```bash
obsidian workspace:save [name=<name>]
```

**Parameters:**
- `name=<name>` - Workspace name

**Examples:**
```bash
# Save with generated name
obsidian workspace:save

# Save with explicit name
obsidian workspace:save name="Research Layout"
```

## workspace:load - Load a saved workspace

```bash
obsidian workspace:load name=<name>
```

**Parameters:**
- `name=<name>` (required) - Workspace name

**Examples:**
```bash
obsidian workspace:load name="Research Layout"

obsidian workspace:load name="Writing Focus"
```

## workspace:delete - Delete a saved workspace

```bash
obsidian workspace:delete name=<name>
```

**Parameters:**
- `name=<name>` (required) - Workspace name

**Examples:**
```bash
obsidian workspace:delete name="Old Layout"

obsidian workspace:delete name="Scratch"
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

### Save and restore layouts
```bash
obsidian workspace:save name="Review"
obsidian workspace:load name="Review"
```
