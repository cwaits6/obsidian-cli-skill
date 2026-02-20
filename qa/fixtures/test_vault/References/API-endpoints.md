---
type: reference
context: work
topic: api
created: 2024-01-28
---

# API Endpoints

Documentation for the internal API used by the [[Projects/Automation|automation project]].

## Authentication

All endpoints require Bearer token in Authorization header.

## Endpoints

### GET /api/notes

List all notes in the vault.

**Parameters:**
- `folder` (optional) — filter by folder path
- `limit` (optional) — max results, default 100

### GET /api/notes/:path

Read a specific note by path.

**Returns:** note content, properties, and link metadata.

### PUT /api/notes/:path/properties

Update properties on a note.

**Body:**
```json
{
  "type": "reference",
  "topic": "api"
}
```

### GET /api/search

Full-text search across the vault.

**Parameters:**
- `q` (required) — search query
- `folder` (optional) — scope to folder
