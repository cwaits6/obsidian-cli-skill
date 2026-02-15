# CSS Snippet Operations

Commands for managing CSS snippets.

## snippets - List installed CSS snippets

```bash
obsidian snippets
```

**Examples:**
```bash
obsidian snippets
```

## snippets:enabled - List enabled CSS snippets

```bash
obsidian snippets:enabled
```

**Examples:**
```bash
obsidian snippets:enabled
```

## snippet:enable - Enable a CSS snippet

```bash
obsidian snippet:enable name=<name>
```

**Parameters:**
- `name=<name>` (required) - Snippet name

**Examples:**
```bash
obsidian snippet:enable name="my-custom-styles"
```

## snippet:disable - Disable a CSS snippet

```bash
obsidian snippet:disable name=<name>
```

**Parameters:**
- `name=<name>` (required) - Snippet name

**Examples:**
```bash
obsidian snippet:disable name="my-custom-styles"
```

## Common Patterns

### Manage snippets
```bash
obsidian snippets
obsidian snippet:enable name="snippet-name"
obsidian snippets:enabled
```
