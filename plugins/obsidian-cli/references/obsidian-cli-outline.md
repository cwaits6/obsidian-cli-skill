# Document Structure & Outline Operations

Commands for exploring document structure and content analysis.

## outline - Show headings for the current file

```bash
obsidian outline [file=<name>] [path=<path>] [format=tree|md] [total]
```

**Parameters:**
- `file=<name>` - Target filename (include path relative to vault root)
- `path=<path>` - Target path (alternative to file)
- `format=tree|md` - Output format
  - `tree` - Tree structure (default)
  - `md` - Markdown list
- `total` - Flag: show heading count

**Examples:**
```bash
# Show file outline
obsidian outline file="Tech/K8s/Helm.md"

# Markdown format
obsidian outline file="my-guide.md" format=md

# With count
obsidian outline file="large-document.md" total
```

## Common Patterns

### Analyze document structure
```bash
obsidian outline file="my-note.md" total
```

### Export outline as markdown
```bash
obsidian outline file="my-guide.md" format=md
```

### Explore large documents
```bash
obsidian outline file="long-guide.md" format=tree
```
