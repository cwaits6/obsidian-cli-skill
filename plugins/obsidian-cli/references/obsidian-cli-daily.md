# Daily Note Operations

Commands for opening and editing daily notes.

## daily - Open daily note

```bash
obsidian daily [paneType=tab|split|window]
```

**Parameters:**
- `paneType=tab|split|window` - Pane type for opening the daily note

**Examples:**
```bash
# Open today's daily note
obsidian daily

# Open in a new tab
obsidian daily paneType=tab
```

## daily:read - Read daily note contents

```bash
obsidian daily:read
```

**Examples:**
```bash
obsidian daily:read

obsidian vault="Work" daily:read
```

## daily:append - Append content to daily note

```bash
obsidian daily:append content=<text> [paneType=tab|split|window] [inline]
```

**Parameters:**
- `content=<text>` (required) - Content to append
- `paneType=tab|split|window` - Pane type for opening
- `inline` - Flag: append without newline

**Examples:**
```bash
# Append task to today's daily note
obsidian daily:append content="- [ ] Follow up with team"

# Append inline
obsidian daily:append content=" #focus" inline
```

## daily:prepend - Prepend content to daily note

```bash
obsidian daily:prepend content=<text> [paneType=tab|split|window] [inline]
```

**Parameters:**
- `content=<text>` (required) - Content to prepend
- `paneType=tab|split|window` - Pane type for opening
- `inline` - Flag: prepend without newline

**Examples:**
```bash
# Prepend title marker
obsidian daily:prepend content="# Standup"

# Prepend inline
obsidian daily:prepend content="[DRAFT] " inline
```

## Common Patterns

### Capture a quick daily task
```bash
obsidian daily:append content="- [ ] Review pull request"
```

### Pull daily content into automation
```bash
obsidian daily:read
```
