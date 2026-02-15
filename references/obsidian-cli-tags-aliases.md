# Tags & Aliases Operations

Commands for managing and querying tags and aliases in your vault.

## tags - List tags in vault or file

```bash
obsidian tags [all] [file=<name>] [path=<path>] [total] [counts] [sort=count]
```

**Parameters:**
- `all` - Flag: include all tags
- `file=<name>` - Limit to specific file
- `path=<path>` - Limit to folder
- `total` - Flag: show tag count
- `counts` - Flag: show usage count for each tag
- `sort=count` - Sort by usage frequency

**Examples:**
```bash
# List all tags in vault
obsidian tags

# Tags in specific file
obsidian tags file="Tech/K8s/Helm.md"

# Tags with usage counts
obsidian tags counts sort=count

# Tags in folder
obsidian tags path="Tech" total
```

## tag - Get tag information

```bash
obsidian tag name=<tag> [total] [verbose]
```

**Parameters:**
- `name=<tag>` (required) - Tag name
- `total` - Flag: show count
- `verbose` - Flag: detailed information

**Examples:**
```bash
obsidian tag name="kubernetes"

obsidian tag name="troubleshooting" total verbose
```

## aliases - List aliases in vault or file

```bash
obsidian aliases [all] [file=<name>] [path=<path>] [total] [verbose]
```

**Parameters:**
- `all` - Flag: include all aliases
- `file=<name>` - Limit to specific file
- `path=<path>` - Limit to folder
- `total` - Flag: show count
- `verbose` - Flag: detailed information

**Examples:**
```bash
# List all aliases
obsidian aliases

# Aliases in specific file
obsidian aliases file="Tech/K8s/Helm.md"

# Aliases with details
obsidian aliases all verbose total
```

## Common Patterns

### Find most used tags
```bash
obsidian tags counts sort=count
```

### List all aliases
```bash
obsidian aliases all
```

### Get tag statistics
```bash
obsidian tag name="kubernetes" total
```

### Explore file metadata
```bash
obsidian aliases file="my-note.md"
obsidian tags file="my-note.md"
```
