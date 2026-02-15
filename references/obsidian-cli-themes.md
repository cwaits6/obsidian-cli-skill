# Theme Operations

Commands for managing and installing themes.

## theme - Show theme information

```bash
obsidian theme [name=<name>]
```

**Parameters:**
- `name=<name>` - Get info about specific theme

**Examples:**
```bash
# Show active theme
obsidian theme

# Get theme info
obsidian theme name="Minimal"
```

## theme:set - Set active theme

```bash
obsidian theme:set name=<name>
```

**Parameters:**
- `name=<name>` (required) - Theme name to activate

**Examples:**
```bash
obsidian theme:set name="Minimal"

obsidian theme:set name="Things"
```

## themes - List installed themes

```bash
obsidian themes [versions]
```

**Parameters:**
- `versions` - Flag: show version information

**Examples:**
```bash
# List themes
obsidian themes

# With versions
obsidian themes versions
```

## theme:install - Install a community theme

```bash
obsidian theme:install name=<name> [enable]
```

**Parameters:**
- `name=<name>` (required) - Theme name from community
- `enable` - Flag: enable after install

**Examples:**
```bash
obsidian theme:install name="Minimal"

obsidian theme:install name="Things" enable
```

## theme:uninstall - Uninstall a theme

```bash
obsidian theme:uninstall name=<name>
```

**Parameters:**
- `name=<name>` (required) - Theme to uninstall

**Examples:**
```bash
obsidian theme:uninstall name="Minimal"
```

## Common Patterns

### Change theme
```bash
obsidian theme:set name="Your-Theme"
```

### Find and install theme
```bash
obsidian themes
obsidian theme:install name="Theme-Name" enable
```
