# Output Format Standard

All user-facing output must follow these formats. The goal is **clean, scannable output** — each item should take one line, shared values should not be repeated, and the user should be able to review a proposal without excessive scrolling.

## General Rules

- **One line per item.** Each file gets one line with its changes. Never use multi-line blocks or sub-bullets per file.
- **State shared values once.** If all notes share a property value (e.g., context: work), say it once in the header, not per item.
- **Omit obvious details.** Don't repeat the operation type on every line. Don't show unchanged properties.
- **Group by logical category.** Use bold labels (not `###` headers) to group items — the label and first item share the same line.
- **Use tables only for summaries of ≤10 items.** For larger sets, use grouped counts.

## Proposal Format

Used when presenting any operation that needs user approval.

Default format — one line per file, grouped by category:

```
**<Operation> Proposal** — <N> files, all context: <shared value>

**<Group>:**
- file.md → topic: [aws], tags: [cli]
- other.md → topic: [linux]
**<Group>:**
- guide.md → topic: [aws, terraform]
- setup.md → topic: [kubernetes]

⚠ Empty files: note.md, draft.md — include or skip?
```

When multiple files in the same group have **identical changes**, collapse them onto one line with ` · ` (middle dot):

```
**Snippets:** file.md · other.md · script.md → topic: [aws]
```

Only use ` · ` when the changes are truly the same. If each file has different properties, list them separately.

## Progress Format

Used during batch execution. **Do not print a line for every file.** Show progress in batches.

For ≤10 files, show a single completion summary after all operations finish (skip per-item progress entirely).

For >10 files, show a progress line every 5 files:

```
[5/20] ✓ 5 properties set...
[10/20] ✓ 10 properties set...
[15/20] ✓ 14 set, 1 failed (broken.md: file not found)
[20/20] Done — 19 succeeded, 1 failed
```

**Rules:**
- Never print a line per file during execution — this floods the terminal
- Batch progress at intervals of 5 or 10 depending on total count
- Include failure details inline when they occur
- Final line states totals

## Summary Format

Used after an operation completes.

For ≤10 files:
```
**Done** — <N> succeeded, <N> failed, <N> skipped

| File | Status | Details |
|------|--------|---------|
| file.md | ✓ | type: snippet, topic: [aws] |
| broken.md | ✗ | file not found |
```

For >10 files, use counts only (no per-file table):
```
**Done** — 14 succeeded, 1 failed

Failed: broken.md (file not found)
```

Only list failures and skips individually. Successes are the default — don't enumerate them for large batches.

## Error Format

Used when an individual operation fails during execution.

```
✗ <file.md> — `<command that failed>` → <error message>. Fix: <suggestion>
```

Single line. Include the command, error, and fix inline. Only expand to multi-line if the error message itself is long.

## Search Results Format

```
**"<query>"** — <N> matches in <M> files

**folder/** file.md:12 ...snippet... · other.md:45 ...snippet...
**folder2/** note.md:3 ...snippet...
```

**Rules:**
- Bold folder path, then file:line pairs with snippets on the same line
- Separate entries with ` · ` when they fit on one line
- Bold the matching term in snippets
- State totals in header, not at the bottom

## Base Preview Format

Used when proposing a `.base` file for approval before creating it.

```
**Base Proposal** — <name>.base in <path>

Query: type = "how-to"
Group by: topic
Columns: Name, topic, context, tags
Sort: topic (ascending)

Filter formula:
(property("type") = "how-to")
```

Show the human-readable intent first (query, grouping, columns), then the actual filter formula. Keep it to one block — don't split across multiple sections.

## Template Preview Format

Used when proposing a Templater template for approval before creating it.

```
**Template Proposal** — <name>.md in <templates path>

---
type: <% tp.system.prompt("Type") %>
context: <% tp.system.prompt("Context") %>
topic: []
---

# <% tp.file.title %>

<template body>
```

Show the complete template content as it will appear in the file. No separate "explanation" section — the template should be self-explanatory with Templater syntax visible.

## Info / List Format

Used for read-only queries (vault structure, property listing, file listing) that don't modify anything.

```
**<Query Description>** — <N> results

- item one
- item two
- item three
```

For property reads across multiple files:

```
**Properties on 5 files in Docs/**

| File | type | context | topic |
|------|------|---------|-------|
| file.md | reference | work | [aws] |
| other.md | how-to | work | [k8s] |
```

Use a table when showing the same properties across multiple files. Use a simple list for single-dimension results (file names, folder names, plugin names).

## Multi-Phase Summary

Used after a workflow with multiple phases completes (e.g., migration = property assignment + rename/move).

```
**Migration Complete** — <N> files

Phase 1 (properties): <N> set, <N> failed
Phase 2 (rename/move): <N> moved, <N> failed

Failed: broken.md (file not found in phase 2)
```

One line per phase with counts. Only list individual failures at the end. Do not repeat the per-phase summaries that were already shown during execution.
