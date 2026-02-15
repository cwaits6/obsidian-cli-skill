# Utility & Information Commands

General utility commands for vault management and information.

## version - Show Obsidian version

```bash
obsidian version
```

**Examples:**
```bash
obsidian version
```

## reload - Reload the vault

```bash
obsidian reload
```

**Examples:**
```bash
obsidian reload
```

## restart - Restart the app

```bash
obsidian restart
```

**Examples:**
```bash
obsidian restart
```

## random - Open a random note

```bash
obsidian random [folder=<path>] [newtab] [silent]
```

**Parameters:**
- `folder=<path>` - Limit to specific folder
- `newtab` - Flag: open in new tab
- `silent` - Flag: don't show notification

**Examples:**
```bash
# Open random note
obsidian random

# Random note from folder
obsidian random folder="Tech"

# Open in new tab silently
obsidian random folder="02-Work/00-Notes" newtab silent
```

## random:read - Read a random note

```bash
obsidian random:read [folder=<path>]
```

**Parameters:**
- `folder=<path>` - Limit to specific folder

**Examples:**
```bash
obsidian random:read

obsidian random:read folder="My-Notes"
```

## recents - List recently opened files

```bash
obsidian recents [total]
```

**Parameters:**
- `total` - Flag: show count

**Examples:**
```bash
obsidian recents

obsidian recents total
```

## outline - Show headings for a file

```bash
obsidian outline [file=<name>] [path=<path>] [format=tree|md] [total]
```

**Parameters:**
- `file=<name>` - Target filename
- `path=<path>` - Target path
- `format=tree|md` - Output format (tree or markdown)
- `total` - Flag: show heading count

**Examples:**
```bash
# Show file outline
obsidian outline file="Tech/K8s/Helm.md"

# Markdown format
obsidian outline file="my-note.md" format=md total
```

## wordcount - Count words and characters

```bash
obsidian wordcount [file=<name>] [path=<path>] [words] [characters]
```

**Parameters:**
- `file=<name>` - Target filename
- `path=<path>` - Target path
- `words` - Flag: show word count
- `characters` - Flag: show character count

**Examples:**
```bash
obsidian wordcount file="my-note.md"

obsidian wordcount file="article.md" words characters
```

## Common Patterns

### Get vault information
```bash
obsidian version
obsidian vault info=files
```

### Explore files
```bash
obsidian random folder="My-Notes"
obsidian recents total
```

### Analyze document
```bash
obsidian outline file="my-note.md" total
obsidian wordcount file="my-note.md" words characters
```
