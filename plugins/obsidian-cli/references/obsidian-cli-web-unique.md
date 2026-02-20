# Web Viewer and Unique Note Operations

Commands for the Web viewer and Unique note creator features.

## web - Open URL in web viewer

```bash
obsidian web url=<url> [newtab]
```

**Parameters:**
- `url=<url>` (required) - URL to open
- `newtab` - Flag: open in new tab

**Examples:**
```bash
obsidian web url="https://help.obsidian.md/cli"

obsidian web url="https://obsidian.md" newtab
```

## unique - Create unique note

```bash
obsidian unique [name=<text>] [content=<text>] [paneType=tab|split|window] [silent]
```

**Parameters:**
- `name=<text>` - Note name
- `content=<text>` - Initial content
- `paneType=tab|split|window` - Pane type for opening
- `silent` - Flag: create without opening

**Examples:**
```bash
# Create unique note with generated name
obsidian unique

# Create unique note with content
obsidian unique name="Meeting Capture" content="# Notes" silent
```

## Common Patterns

### Open docs in the web viewer
```bash
obsidian web url="https://help.obsidian.md/cli" newtab
```

### Create quick scratch notes
```bash
obsidian unique name="Scratch" content="- idea"
```
