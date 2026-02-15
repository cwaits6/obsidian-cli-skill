# Property Operations Commands

Commands for setting, reading, and removing properties (frontmatter) on notes.

## property:set - Set a property on a file

```bash
obsidian property:set name=<name> value=<value> [type=text|list|number|checkbox|date|datetime] [file=<name>] [path=<path>]
```

**Parameters:**
- `name=<name>` (required) - Property name
- `value=<value>` (required) - Property value
- `type=` (optional) - Property type; inferred if not specified
  - `text` - Text value
  - `number` - Numeric value
  - `checkbox` - Boolean/checkbox value
  - `date` - Date value
  - `datetime` - Date and time value
  - `list` - Array of values
- `file=<name>` - Target filename (with path relative to vault root)
- `path=<path>` - Target path/folder (alternative to file parameter)

**Examples:**
```bash
# Set basic property
obsidian property:set name=type value=how-to file="My-Notes/my-guide.md"

# Set with explicit type
obsidian property:set name=resolved value=true type=checkbox file="My-Notes/bug.md"

# Set list property (use comma-separated values in brackets)
obsidian property:set name=topic value="[kubernetes, aws]" type=list file="My-Notes/note.md"

# Set date property
obsidian property:set name=due-date value=2025-12-31 type=date file="My-Notes/task.md"

# Using path parameter with file name
obsidian property:set name=context value=work file="note.md" path="My-Notes"
```

## property:read - Read a specific property

```bash
obsidian property:read name=<name> [file=<name>] [path=<path>]
```

**Parameters:**
- `name=<name>` (required) - Property name to read
- `file=<name>` - Target filename (with path relative to vault root)
- `path=<path>` - Target path/folder (alternative to file parameter)

**Examples:**
```bash
obsidian property:read name=context file="My-Notes/my-note.md"

# Using path parameter
obsidian property:read name=type file="my-note.md" path="My-Notes"
```

## property:remove - Remove a property

```bash
obsidian property:remove name=<name> [file=<name>] [path=<path>]
```

**Parameters:**
- `name=<name>` (required) - Property name to remove
- `file=<name>` - Target filename (with path relative to vault root)
- `path=<path>` - Target path/folder (alternative to file parameter)

**Example:**
```bash
obsidian property:remove name=old-property file="My-Notes/note.md"
```

## properties - List all properties

```bash
obsidian properties [all] [file=<name>] [path=<path>] [name=<name>] [total] [sort=count] [counts] [format=yaml|tsv]
```

**Parameters:**
- `all` - Include all properties including empty ones
- `file=<name>` - Show properties for specific file
- `path=<path>` - Show properties for files in folder
- `name=<name>` - Filter by property name
- `total` - Show count of properties
- `sort=count` - Sort by usage count
- `counts` - Show property usage counts
- `format=yaml|tsv` - Output format (yaml or tsv)

**Examples:**
```bash
# List all properties in vault with counts
obsidian properties counts

# List properties for a specific file
obsidian properties file="My-Notes/my-note.md"

# Show all properties in YAML format
obsidian properties format=yaml all
```

## Common Patterns

### Set multiple properties at once
```bash
obsidian property:set name=type value=reference file="note.md"
obsidian property:set name=context value=work file="note.md"
obsidian property:set name=topic value="[kubernetes]" type=list file="note.md"
obsidian property:set name=project value=platform-upgrade file="note.md"
```

### Bulk set property on multiple files
```bash
obsidian files folder="My-Notes" | while read file; do
  obsidian property:set name=context value=work file="$file"
done
```

### Set conditional property (e.g., resolved for troubleshooting)
```bash
# For troubleshooting notes, add resolved property
obsidian property:set name=resolved value=true type=checkbox file="Troubleshooting/bug.md"
```

### Verify property was set
```bash
obsidian property:read name=type file="My-Notes/my-note.md"
```

## Tips

- **Type inference:** If you don't specify `type=`, Obsidian CLI infers it from the value
  - `true`/`false` → checkbox
  - Numbers → number
  - Dates in ISO format → date
  - Values in brackets → list

- **List values:** Use comma-separated format in brackets: `[value1, value2, value3]`

- **File parameter:** Include full path relative to vault root: `file="Folder/Subfolder/note.md"`

- **Path parameter:** Use folder path: `path="Folder/Subfolder"`

- **Property names:** Use consistent naming (kebab-case recommended to match file naming)

- **Validate:** Always verify properties are set correctly by reading them back with `property:read`
