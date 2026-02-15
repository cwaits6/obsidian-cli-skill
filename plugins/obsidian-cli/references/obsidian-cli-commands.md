# Command & Hotkey Operations

Commands for executing Obsidian commands and managing hotkeys.

## command - Execute an Obsidian command

```bash
obsidian command id=<command-id>
```

**Parameters:**
- `id=<command-id>` (required) - Command ID to execute

**Examples:**
```bash
# Open settings
obsidian command id=app:open-settings

# Toggle sidebar
obsidian command id=app:toggle-left-sidebar

# Open command palette
obsidian command id=command-palette:open
```

## commands - List available command IDs

```bash
obsidian commands [filter=<prefix>]
```

**Parameters:**
- `filter=<prefix>` - Filter commands by prefix

**Examples:**
```bash
# List all commands
obsidian commands

# Filter by prefix
obsidian commands filter=app

obsidian commands filter=editor
```

## hotkey - Get hotkey for a command

```bash
obsidian hotkey id=<command-id> [verbose]
```

**Parameters:**
- `id=<command-id>` (required) - Command ID
- `verbose` - Flag: detailed information

**Examples:**
```bash
obsidian hotkey id=app:open-settings

obsidian hotkey id=editor:toggle-bold verbose
```

## hotkeys - List all hotkeys

```bash
obsidian hotkeys [total] [all] [verbose]
```

**Parameters:**
- `total` - Flag: show count
- `all` - Flag: include all hotkeys
- `verbose` - Flag: detailed information

**Examples:**
```bash
# List configured hotkeys
obsidian hotkeys

# Show all with details
obsidian hotkeys all verbose total
```

## Common Patterns

### Execute common commands
```bash
obsidian command id=app:open-vault-settings
obsidian command id=app:open-settings
obsidian command id=obsidian-sync:start-sync
```

### Find hotkeys
```bash
obsidian hotkeys verbose
obsidian hotkey id=editor:toggle-bold
```

### Discover available commands
```bash
obsidian commands filter=editor
```
