# Developer Tools

Commands for debugging and development purposes.

## devtools - Toggle Electron dev tools

```bash
obsidian devtools
```

**Examples:**
```bash
obsidian devtools
```

## dev:debug - Attach/detach Chrome DevTools Protocol debugger

```bash
obsidian dev:debug [on] [off]
```

**Parameters:**
- `on` - Flag: enable debugger
- `off` - Flag: disable debugger

**Examples:**
```bash
obsidian dev:debug on

obsidian dev:debug off
```

## dev:console - Show captured console messages

```bash
obsidian dev:console [clear] [limit=<n>] [level=log|warn|error|info|debug]
```

**Parameters:**
- `clear` - Flag: clear console history
- `limit=<n>` - Maximum messages to show
- `level=log|warn|error|info|debug` - Filter by level

**Examples:**
```bash
obsidian dev:console

obsidian dev:console level=error limit=10
```

## dev:errors - Show captured errors

```bash
obsidian dev:errors [clear]
```

**Parameters:**
- `clear` - Flag: clear error history

**Examples:**
```bash
obsidian dev:errors

obsidian dev:errors clear
```

## dev:dom - Query DOM elements

```bash
obsidian dev:dom selector=<css> [total] [text] [inner] [all] [attr=<name>] [css=<prop>]
```

**Parameters:**
- `selector=<css>` (required) - CSS selector
- `total` - Flag: show count
- `text` - Flag: show text content
- `inner` - Flag: show inner HTML
- `all` - Flag: include all matches
- `attr=<name>` - Get attribute value
- `css=<prop>` - Get CSS property value

**Examples:**
```bash
obsidian dev:dom selector=".heading-collapse-indicator"

obsidian dev:dom selector="[data-type='note']" all total
```

## dev:css - Inspect CSS with source locations

```bash
obsidian dev:css selector=<css> [prop=<name>]
```

**Parameters:**
- `selector=<css>` (required) - CSS selector
- `prop=<name>` - Specific property to inspect

**Examples:**
```bash
obsidian dev:css selector=".markdown-rendered"

obsidian dev:css selector="h1" prop="font-size"
```

## dev:screenshot - Take a screenshot

```bash
obsidian dev:screenshot [path=<filename>]
```

**Parameters:**
- `path=<filename>` - Output file path

**Examples:**
```bash
obsidian dev:screenshot

obsidian dev:screenshot path="screenshot.png"
```

## dev:mobile - Toggle mobile emulation

```bash
obsidian dev:mobile [on] [off]
```

**Parameters:**
- `on` - Flag: enable mobile mode
- `off` - Flag: disable mobile mode

**Examples:**
```bash
obsidian dev:mobile on

obsidian dev:mobile off
```

## dev:cdp - Run a Chrome DevTools Protocol command

```bash
obsidian dev:cdp method=<CDP.method> [params=<json>]
```

**Parameters:**
- `method=<CDP.method>` (required) - CDP method name
- `params=<json>` - JSON parameters

**Examples:**
```bash
obsidian dev:cdp method=Runtime.evaluate params='{"expression":"console.log(\"test\")"}'
```

## eval - Execute JavaScript and return result

```bash
obsidian eval code=<javascript>
```

**Parameters:**
- `code=<javascript>` (required) - JavaScript code

**Examples:**
```bash
obsidian eval code="app.vault.getFiles().length"

obsidian eval code="moment().format('YYYY-MM-DD')"
```

## Common Patterns

### Debug plugins
```bash
obsidian devtools
obsidian dev:console level=error
```

### Inspect elements
```bash
obsidian dev:dom selector=".editor-container" all
obsidian dev:css selector=".editor-container"
```

### Take screenshots
```bash
obsidian dev:screenshot path="vault-state.png"
```
