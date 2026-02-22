# File Operations Commands

Commands for creating, reading, moving, and deleting files. Obsidian CLI automatically updates all vault links when files are moved or renamed.

## create - Create a new file

```bash
obsidian create [name=<name>] [path=<path>] [content=<text>] [template=<name>] [overwrite] [open] [newtab]
```

**Parameters:**
- `name=<name>` (required) - Filename without extension
- `path=<path>` - Destination folder (relative to vault root)
- `content=<text>` - Initial file content
- `template=<name>` - Template to use for file content
- `overwrite` - Flag: overwrite if file already exists
- `open` - Flag: open file after creating (CLI is silent by default)
- `newtab` - Flag: open in new tab

**Examples:**
```bash
# Create note in My-Notes folder
obsidian create name="my-note" path="My-Notes"

# Create with initial content
obsidian create name="meeting-notes" path="My-Notes" content="## Attendees\n\n## Discussion"

# Create from template
obsidian create name="how-to-guide" path="How-Tos" template="how-to-template"
```

## read - Read file contents

```bash
obsidian read [file=<name>] [path=<path>]
```

**Parameters:**
- `file=<name>` - Target filename (include path relative to vault root)
- `path=<path>` - Target path (alternative to file parameter)

**Examples:**
```bash
obsidian read file="My-Notes/my-note.md"

# Using path parameter
obsidian read file="my-note.md" path="My-Notes"
```

## move - Move or rename file (auto-updates links)

```bash
obsidian move [file=<name>] [path=<path>] to=<path>
```

**Parameters:**
- `file=<name>` - Current file name (include path relative to vault root)
- `path=<path>` - Alternative way to specify current path/folder
- `to=<path>` (required) - New file path (includes new filename, relative to vault root)

**Use cases:**
- **Rename:** Same folder, different name: `obsidian move file="Folder/old-name.md" to="Folder/new-name.md"`
- **Move:** Different folder, same name: `obsidian move file="Old-Folder/file.md" to="New-Folder/file.md"`
- **Move + rename:** Different folder and name: `obsidian move file="Old/old-name.md" to="New/new-name.md"`

**Important:** All vault links are automatically updated to match the new path.

**Examples:**
```bash
# Rename file to kebab-case
obsidian move file="My-Notes/My Meeting Notes.md" to="My-Notes/my-meeting-notes.md"

# Move file to different folder
obsidian move file="Captures/random-note.md" to="My-Notes/organized-note.md"

# Batch rename with loop
obsidian files folder="Captures" | while read file; do
  normalized=$(echo "$file" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
  obsidian move file="$file" to="$normalized"
done
```

## append - Add content to end of file

```bash
obsidian append [file=<name>] [path=<path>] content=<text> [inline]
```

**Parameters:**
- `file=<name>` - Target filename (include path relative to vault root)
- `path=<path>` - Target path (alternative to file parameter)
- `content=<text>` (required) - Content to append
- `inline` - Flag: don't add newline before content

**Example:**
```bash
obsidian append file="My-Notes/meeting.md" content="## Follow-up Items"
```

## prepend - Add content to start of file

```bash
obsidian prepend [file=<name>] [path=<path>] content=<text> [inline]
```

**Same parameters as append**, but adds to beginning of file (after frontmatter).

## rename - Rename a file in place

```bash
obsidian rename [file=<name>] [path=<path>] name=<new-name>
```

**Parameters:**
- `file=<name>` - Current filename (include path relative to vault root)
- `path=<path>` - Target path (alternative to file parameter)
- `name=<new-name>` (required) - New filename (without path)

**Note:** Renames the file within its current folder. To move to a different folder, use `move` instead. All vault links are automatically updated.

**Examples:**
```bash
# Rename to kebab-case
obsidian rename file="Notes/My Meeting Notes.md" name="my-meeting-notes.md"

# Rename using path parameter
obsidian rename path="Notes/helmValuesOverride.md" name="helm-values-override.md"
```

## delete - Delete file

```bash
obsidian delete [file=<name>] [path=<path>] [permanent]
```

**Parameters:**
- `file=<name>` - File to delete (include path relative to vault root)
- `path=<path>` - Target path (alternative to file parameter)
- `permanent` - Flag: skip trash, permanently delete

**Examples:**
```bash
# Move to trash
obsidian delete file="Captures/old-note.md"

# Permanently delete
obsidian delete file="Captures/old-note.md" permanent
```

## open - Open file in Obsidian

```bash
obsidian open [file=<name>] [path=<path>] [newtab]
```

**Parameters:**
- `file=<name>` - File to open (include path relative to vault root)
- `path=<path>` - Target path (alternative to file parameter)
- `newtab` - Flag: open in new tab instead of current pane

**Example:**
```bash
obsidian open file="My-Notes/my-note.md" newtab
```

## files - List files

```bash
obsidian files [folder=<path>] [ext=<extension>] [total]
```

**Parameters:**
- `folder=<path>` - Folder to list (optional, defaults to vault root)
- `ext=<extension>` - Filter by extension (e.g., ".md", ".yaml")
- `total` - Flag: show file count

**Examples:**
```bash
# List all files in My-Notes
obsidian files folder="My-Notes"

# List only YAML files
obsidian files ext=".yaml"

# List and count files in folder
obsidian files folder="Captures" total
```

## Common Patterns

### Normalize filenames in a folder to kebab-case
```bash
obsidian files folder="Captures" | while read file; do
  normalized=$(basename "$file" | tr '[:upper:]' '[:lower:]' | tr ' _' '-' | tr -s '-')
  obsidian move file="$file" to="$normalized"
done
```

### Batch move files from one folder to another with rename
```bash
obsidian files folder="Source-Folder" | while read file; do
  obsidian move file="$file" to="Dest-Folder/$file"
done
```

### Create multiple notes from a list
```bash
for note_name in "note-1" "note-2" "note-3"; do
  obsidian create name="$note_name" path="My-Notes" content="# $note_name"
done
```
