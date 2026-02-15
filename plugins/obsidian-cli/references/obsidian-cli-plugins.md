# Plugin & Command Operations

Commands for managing plugins and executing Obsidian commands via CLI.

## plugins - List installed plugins

```bash
obsidian plugins [filter=core|community] [versions]
```

**Parameters:**
- `filter=core|community` - Filter by plugin type (core or community)
- `versions` - Flag: show version information

**Examples:**
```bash
# List all plugins
obsidian plugins

# List community plugins
obsidian plugins filter=community

# Show with versions
obsidian plugins versions
```

## plugins:enabled - List enabled plugins

```bash
obsidian plugins:enabled [filter=core|community] [versions]
```

**Parameters:**
- `filter=core|community` - Filter by plugin type
- `versions` - Flag: show version information

**Examples:**
```bash
obsidian plugins:enabled

obsidian plugins:enabled filter=community versions
```

## plugin - Get plugin information

```bash
obsidian plugin id=<plugin-id>
```

**Parameters:**
- `id=<plugin-id>` (required) - Plugin ID (folder name in `.obsidian/plugins/` or community ID)

**Examples:**
```bash
obsidian plugin id=templater-obsidian

obsidian plugin id=obsidian-dataview
```

## plugin:enable - Enable a plugin

```bash
obsidian plugin:enable id=<id> [filter=core|community]
```

**Parameters:**
- `id=<id>` (required) - Plugin ID
- `filter=core|community` - Filter by plugin type

**Examples:**
```bash
obsidian plugin:enable id=templater-obsidian

obsidian plugin:enable id=dataview filter=community
```

## plugin:disable - Disable a plugin

```bash
obsidian plugin:disable id=<id> [filter=core|community]
```

**Parameters:**
- `id=<id>` (required) - Plugin ID
- `filter=core|community` - Filter by plugin type

**Examples:**
```bash
obsidian plugin:disable id=old-plugin

obsidian plugin:disable id=unused filter=community
```

## plugin:reload - Reload a plugin (for developers)

```bash
obsidian plugin:reload id=<id>
```

**Parameters:**
- `id=<id>` (required) - Plugin ID

**Examples:**
```bash
obsidian plugin:reload id=my-custom-plugin
```

## plugin:install - Install a community plugin

```bash
obsidian plugin:install id=<id> [enable]
```

**Parameters:**
- `id=<id>` (required) - Plugin ID from community
- `enable` - Flag: enable plugin after install

**Examples:**
```bash
obsidian plugin:install id=templater-obsidian

obsidian plugin:install id=obsidian-dataview enable
```

## plugin:uninstall - Uninstall a community plugin

```bash
obsidian plugin:uninstall id=<id>
```

**Parameters:**
- `id=<id>` (required) - Plugin ID to uninstall

**Examples:**
```bash
obsidian plugin:uninstall id=unused-plugin
```

## plugins:restrict - Toggle or check restricted mode

```bash
obsidian plugins:restrict [on] [off]
```

**Parameters:**
- `on` - Flag: enable restricted mode (disable community plugins)
- `off` - Flag: disable restricted mode

**Examples:**
```bash
# Check current state
obsidian plugins:restrict

# Enable restricted mode
obsidian plugins:restrict on

# Disable restricted mode
obsidian plugins:restrict off
```

## Common Patterns

### Check plugin status
```bash
obsidian plugin id=templater-obsidian
```

### Enable a plugin
```bash
obsidian plugin:enable id=templater-obsidian
```

### Find all enabled community plugins
```bash
obsidian plugins:enabled filter=community
```

### Install and enable a plugin
```bash
obsidian plugin:install id=dataview enable
```

### Reload plugin after changes
```bash
obsidian plugin:reload id=my-plugin
```

### List all plugins with versions
```bash
obsidian plugins versions
```

## Plugin IDs Reference

Common plugin IDs:
- `templater-obsidian` - Templater
- `obsidian-dataview` - Dataview
- `obsidian-git` - Obsidian Git
- `db-folder` - Database Folder
- `quickadd` - QuickAdd
- `omnisearch` - Omnisearch

Find exact ID in `.obsidian/plugins/` directory (folder name is the ID)

## Tips

- **Discover plugin IDs:** Check `.obsidian/plugins/` directory
- **List all plugins:** `obsidian plugins versions` to see IDs and versions
- **Enable before commands:** Ensure plugin is enabled before running plugin-specific commands
- **Restricted mode:** Use to disable community plugins temporarily for troubleshooting

