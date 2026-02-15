# Bookmarks Operations

Commands for managing and organizing bookmarks in your vault.

## bookmarks - List all bookmarks

```bash
obsidian bookmarks [total] [verbose]
```

**Parameters:**
- `total` - Flag: show bookmark count
- `verbose` - Flag: detailed information

**Examples:**
```bash
obsidian bookmarks

obsidian bookmarks total verbose
```

## bookmark - Add a bookmark

```bash
obsidian bookmark [file=<path>] [subpath=<subpath>] [folder=<path>] [search=<query>] [url=<url>] [title=<title>]
```

**Parameters:**
- `file=<path>` - File to bookmark
- `subpath=<subpath>` - Heading subpath within file
- `folder=<path>` - Folder to bookmark
- `search=<query>` - Saved search to bookmark
- `url=<url>` - External URL to bookmark
- `title=<title>` - Bookmark title

**Examples:**
```bash
# Bookmark a file
obsidian bookmark file="Tech/K8s/Helm.md"

# Bookmark a folder
obsidian bookmark folder="02-Work/00-Notes"

# Bookmark a heading
obsidian bookmark file="Tech/K8s/Helm.md" subpath="Error when pulling helm chart" title="Helm Chart Error"

# Bookmark a search
obsidian bookmark search="tag:troubleshooting" title="All Troubleshooting"

# Bookmark external URL
obsidian bookmark url="https://kubernetes.io" title="Kubernetes Docs"
```

## Common Patterns

### View all saved bookmarks
```bash
obsidian bookmarks verbose
```

### Get bookmark statistics
```bash
obsidian bookmarks total
```
