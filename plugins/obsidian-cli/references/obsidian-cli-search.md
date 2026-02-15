# Search & Link Operations

Commands for searching vault content and analyzing link structure.

## search - Search vault for text

```bash
obsidian search query=<text> [path=<folder>] [limit=<n>] [total] [matches] [case] [format=text|json]
```

**Parameters:**
- `query=<text>` (required) - Search query text
- `path=<folder>` - Limit search to folder
- `limit=<n>` - Maximum number of results
- `total` - Flag: show result count
- `matches` - Flag: show match details
- `case` - Flag: case-sensitive search
- `format=text|json` - Output format

**Examples:**
```bash
# Basic search
obsidian search query="kubernetes"

# Search in specific folder with limit
obsidian search query="config" path="Tech/K8s" limit=10

# Search with JSON output
obsidian search query="error" format=json
```

## search:open - Open search view

```bash
obsidian search:open [query=<text>]
```

**Parameters:**
- `query=<text>` - Pre-populate search query

**Examples:**
```bash
obsidian search:open

# Open search with query
obsidian search:open query="helm"
```

## links - List outgoing links from a file

```bash
obsidian links [file=<name>] [path=<path>] [total]
```

**Parameters:**
- `file=<name>` - Target filename (include path relative to vault root)
- `path=<path>` - Target path (alternative to file)
- `total` - Flag: show count

**Examples:**
```bash
obsidian links file="Tech/K8s/Helm.md"

obsidian links file="my-note.md" path="My-Notes" total
```

## backlinks - List backlinks to a file

```bash
obsidian backlinks [file=<name>] [path=<path>] [counts] [total]
```

**Parameters:**
- `file=<name>` - Target filename (include path relative to vault root)
- `path=<path>` - Target path (alternative to file)
- `counts` - Flag: show usage counts
- `total` - Flag: show total count

**Examples:**
```bash
# Find all notes linking to this file
obsidian backlinks file="Tech/Platform/Platform Application Onboarding.md"

# With counts
obsidian backlinks file="my-note.md" counts total
```

## unresolved - List unresolved links in vault

```bash
obsidian unresolved [total] [counts] [verbose]
```

**Parameters:**
- `total` - Flag: show count of unresolved links
- `counts` - Flag: show frequency counts
- `verbose` - Flag: show detailed information

**Examples:**
```bash
# Find all broken/unresolved links
obsidian unresolved total

# With frequency counts
obsidian unresolved counts
```

## deadends - List files with no outgoing links

```bash
obsidian deadends [total] [all]
```

**Parameters:**
- `total` - Flag: show count
- `all` - Flag: include system files

**Examples:**
```bash
obsidian deadends

obsidian deadends total all
```

## orphans - List files with no incoming links

```bash
obsidian orphans [total] [all]
```

**Parameters:**
- `total` - Flag: show count
- `all` - Flag: include system files

**Examples:**
```bash
obsidian orphans

# Find unlinked notes
obsidian orphans total
```

## Common Patterns

### Find all notes referencing a topic
```bash
obsidian backlinks file="Topics/kubernetes.md" counts
```

### Identify unused files
```bash
obsidian orphans all
```

### Find broken links
```bash
obsidian unresolved verbose
```

### Search and filter results
```bash
obsidian search query="AWS" path="Tech" limit=50 format=json
```
