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

## Common Patterns

### Open docs in the web viewer
```bash
obsidian web url="https://help.obsidian.md/cli" newtab
```
