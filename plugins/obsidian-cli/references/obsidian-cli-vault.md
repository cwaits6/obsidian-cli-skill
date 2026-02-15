# Vault & Folder Operations

Commands for managing vault structure, exploring files and folders.

## vault - Show vault information

```bash
obsidian vault [info=name|path|files|folders|size]
```

**Parameters:**
- `info=name|path|files|folders|size` - Information to display
  - `name` - Vault name
  - `path` - Vault file system path
  - `files` - Total file count
  - `folders` - Total folder count
  - `size` - Vault size

**Examples:**
```bash
# Show all vault info
obsidian vault

# Show specific info
obsidian vault info=name
obsidian vault info=path
obsidian vault info=files
```

## vaults - List all known vaults

```bash
obsidian vaults [total] [verbose]
```

**Parameters:**
- `total` - Flag: show count
- `verbose` - Flag: detailed information

**Examples:**
```bash
obsidian vaults

obsidian vaults total verbose
```

## files - List files in vault

```bash
obsidian files [folder=<path>] [ext=<extension>] [total]
```

**Parameters:**
- `folder=<path>` - Target folder (defaults to vault root)
- `ext=<extension>` - Filter by file extension (e.g., ".md", ".yaml")
- `total` - Flag: show file count

**Examples:**
```bash
# List all files in vault root
obsidian files

# List files in specific folder
obsidian files folder="Tech"

# Filter by extension
obsidian files ext=".md" total

# Markdown files in subfolder
obsidian files folder="02-Work/00-Notes" ext=".md"
```

## file - Show file information

```bash
obsidian file [file=<name>] [path=<path>]
```

**Parameters:**
- `file=<name>` - Target filename (include path relative to vault root)
- `path=<path>` - Target path (alternative to file)

**Examples:**
```bash
obsidian file file="Tech/K8s/Helm.md"

obsidian file file="my-note.md" path="My-Notes"
```

## folders - List folders in vault

```bash
obsidian folders [folder=<path>] [total]
```

**Parameters:**
- `folder=<path>` - Parent folder to list (defaults to vault root)
- `total` - Flag: show folder count

**Examples:**
```bash
# List top-level folders
obsidian folders

# List folders in subfolder
obsidian folders folder="Tech"

# Show count
obsidian folders total
```

## folder - Show folder information

```bash
obsidian folder path=<path> [info=files|folders|size]
```

**Parameters:**
- `path=<path>` (required) - Folder path
- `info=files|folders|size` - Information type
  - `files` - File count in folder
  - `folders` - Subfolder count
  - `size` - Folder size

**Examples:**
```bash
# Folder details
obsidian folder path="Tech"

# Specific info
obsidian folder path="Tech/K8s" info=files
obsidian folder path="02-Work/00-Notes" info=size
```

## diff - Compare local/sync versions

```bash
obsidian diff [file=<name>] [path=<path>] [from=<n>] [to=<n>] [filter=local|sync]
```

**Parameters:**
- `file=<name>` - Target filename
- `path=<path>` - Target path
- `from=<n>` - Start version
- `to=<n>` - End version
- `filter=local|sync` - Filter by version type

**Examples:**
```bash
obsidian diff file="my-note.md" filter=local

obsidian diff file="my-note.md" from=1 to=3
```

## Common Patterns

### List all markdown notes
```bash
obsidian files ext=".md"
```

### Find all files in a project folder
```bash
obsidian files folder="Projects/MyProject"
```

### Analyze folder structure
```bash
obsidian folder path="Tech" info=files
obsidian folders total
```

### Get vault statistics
```bash
obsidian vault info=files
obsidian vault info=folders
```
