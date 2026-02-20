# Publish Operations

Commands for Obsidian Publish sites and published files.

## publish:site - Show publish site information

```bash
obsidian publish:site
```

**Examples:**
```bash
obsidian publish:site

obsidian vault="Docs" publish:site
```

## publish:list - List published files

```bash
obsidian publish:list [total]
```

**Parameters:**
- `total` - Flag: show published file count

**Examples:**
```bash
obsidian publish:list

obsidian publish:list total
```

## publish:status - List publish changes

```bash
obsidian publish:status [total] [new] [changed] [deleted]
```

**Parameters:**
- `total` - Flag: show change count
- `new` - Flag: show new files only
- `changed` - Flag: show changed files only
- `deleted` - Flag: show deleted files only

**Examples:**
```bash
obsidian publish:status

obsidian publish:status changed total
```

## publish:add - Publish a file or changed files

```bash
obsidian publish:add [file=<name>] [path=<path>] [changed]
```

**Parameters:**
- `file=<name>` - File name
- `path=<path>` - Exact file path from vault root
- `changed` - Flag: publish all changed files

**Examples:**
```bash
# Publish active file
obsidian publish:add

# Publish all changed files
obsidian publish:add changed
```

## publish:remove - Unpublish a file

```bash
obsidian publish:remove [file=<name>] [path=<path>]
```

**Parameters:**
- `file=<name>` - File name
- `path=<path>` - Exact file path from vault root

**Examples:**
```bash
obsidian publish:remove file="Draft"

obsidian publish:remove path="Notes/Old Page.md"
```

## publish:open - Open file on published site

```bash
obsidian publish:open [file=<name>] [path=<path>]
```

**Parameters:**
- `file=<name>` - File name
- `path=<path>` - Exact file path from vault root

**Examples:**
```bash
obsidian publish:open file="Public Home"

obsidian publish:open path="Docs/API.md"
```

## Common Patterns

### Review pending publish changes
```bash
obsidian publish:status total
```

### Publish everything changed
```bash
obsidian publish:add changed
```
