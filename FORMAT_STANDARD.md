# Obsidian CLI Reference Format Standard

All reference files follow this standardized structure for consistency and progressive disclosure.

## File Structure

```
# Category Title
Brief description of what these commands do.

## command:name - Short description

```bash
obsidian command:name [param=<value>] [flag]
```

**Parameters:**
- `param=<value>` (required/optional) - Description
- `flag` - Description

**Examples:**
```bash
# Example 1
obsidian command:name param=value

# Example 2 with explanation
obsidian command:name param=value flag
```

## Common Patterns

### Pattern description
```bash
obsidian command:name param=value
```
```

## Key Rules

1. **Parameter Format:**
   - Required parameters: `param=<value>` (required)
   - Optional parameters: `[param=<value>]`
   - Flags (no value): `[flag]` (optional flags)
   - Flags in descriptions: `Flag: description of what it does`

2. **Command Syntax Block:**
   - Always wrapped in triple backticks with `bash` language tag
   - Use square brackets `[]` for optional parameters
   - Use angle brackets `<>` for parameter placeholders
   - Space-separated parameters (not comma-separated)

3. **Examples:**
   - Minimum 2 examples per command
   - Include comments explaining what each does
   - Show both basic and advanced usage
   - Use relative paths and realistic file names

4. **Common Patterns:**
   - Include at end of file
   - Group related workflows together
   - Show real-world use cases

5. **Consistency:**
   - Use "Flag:" prefix in parameter descriptions for boolean flags
   - Use consistent phrasing (e.g., "Target file", "Target folder")
   - All file paths relative to vault root
   - All property/parameter names consistent across files

## Parameter Type Descriptions

When documenting parameters, use these consistent phrases:

- **Required parameters:** `param=<name>` (required) - Description
- **Optional parameters:** `param=<value>` - Description  
- **Flag parameters:** `flag` - Flag: description
- **Choice parameters:** `param=option1|option2` - Choose from: option1, option2

## File Naming

All reference files follow pattern: `obsidian-cli-<category>.md`

Categories:
- `obsidian-cli-files.md` - File operations
- `obsidian-cli-properties.md` - Property operations
- `obsidian-cli-vault.md` - Vault operations
- `obsidian-cli-search.md` - Search operations
- `obsidian-cli-tags-aliases.md` - Tags and aliases
- `obsidian-cli-tasks.md` - Task operations
- `obsidian-cli-bookmarks.md` - Bookmark operations
- `obsidian-cli-history.md` - History operations
- `obsidian-cli-sync.md` - Sync operations
- `obsidian-cli-workspace.md` - Workspace operations
- `obsidian-cli-themes.md` - Theme operations
- `obsidian-cli-snippets.md` - Snippet operations
- `obsidian-cli-commands.md` - Command operations
- `obsidian-cli-utilities.md` - Utility operations
- `obsidian-cli-dev.md` - Developer tools
- `obsidian-cli-plugins.md` - Plugin operations
- `obsidian-cli-outline.md` - Outline operations
- `obsidian-cli-bases.md` - Base operations
- `obsidian-cli-templates.md` - Template operations
- `obsidian-cli-daily.md` - Daily note operations
- `obsidian-cli-publish.md` - Publish operations
- `obsidian-cli-web-unique.md` - Web viewer and unique note operations
