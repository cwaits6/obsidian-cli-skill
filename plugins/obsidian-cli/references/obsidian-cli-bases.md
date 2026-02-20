# Base Operations Commands

Commands for working with Obsidian Bases (.base files) and Base views.

## bases - List all .base files

```bash
obsidian bases
```

**Output:** Lists all `.base` files in your vault.

## base:query - Query a base

```bash
obsidian base:query [file=<name>] [path=<path>] [view=<name>] [format=json|csv|tsv|md|paths]
```

**Parameters:**
- `file=<name>` - Base filename (wikilink resolution)
- `path=<path>` - Exact path to `.base` file relative to vault root
- `view=<name>` - View name to query
- `format=json|csv|tsv|md|paths` - Output format
  - `json` - JSON format
  - `csv` - Comma-separated values
  - `tsv` - Tab-separated values
  - `md` - Markdown table
  - `paths` - File paths only

**Examples:**
```bash
# Query base as markdown table
obsidian base:query path="Bases/my-base.base" format=md

# Get results as JSON
obsidian base:query path="Bases/work-notes.base" format=json

# Query a specific view
obsidian base:query path="Bases/work-notes.base" view="by-topic" format=paths
```

## base:create - Create item in base

```bash
obsidian base:create [name=<name>] [content=<text>] [silent] [newtab]
```

**Parameters:**
- `name=<name>` - Name for the new item
- `content=<text>` - Initial content for the new item
- `silent` - Flag: create without opening
- `newtab` - Flag: open in new tab

**Examples:**
```bash
# Create item with default name/content
obsidian base:create

# Create named item and open in new tab
obsidian base:create name="New Work Note" content="# Draft" newtab
```

## base:views - List views in the current base file

```bash
obsidian base:views
```

**Examples:**
```bash
# List all views in active base
obsidian base:views

# Open a base file, then inspect its views
obsidian open path="Bases/work-by-topic.base"
obsidian base:views
```

## Creating .base Files

To create a `.base` file, create a YAML file with the following structure:

```yaml
id: unique-id-here
name: Database Name
type: database
properties:
  type:
    type: string
  context:
    type: string
  topic:
    type: list
  project:
    type: string
views:
  table-view:
    type: table
    sourceType: folder
    source: My-Notes
    properties:
      - type
      - context
      - topic
      - project
```

Then create the file via CLI:
```bash
obsidian create name="my-base" path="Bases" content="id: my-base\nname: My Base\ntype: database"
```

## Common Patterns

### Create a base to view all work notes by topic
```yaml
id: work-by-topic
name: Work Notes by Topic
type: database
properties:
  type:
    type: string
  context:
    type: string
  topic:
    type: list
  project:
    type: string
views:
  by-topic:
    type: table
    sourceType: folder
    source: My-Notes
    properties:
      - type
      - context
      - topic
      - project
```

### Query base and display results
```bash
obsidian base:query path="Bases/work-by-topic.base" format=md
```

## See Also

- [obsidian-bases.md](obsidian-bases.md) for detailed `.base` file structure and configuration
- [property-schema.md](property-schema.md) for your property definitions
