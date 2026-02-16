# Output Format Standard

All user-facing output must follow these formats. The primary goal is **compactness** — users work in a terminal and should never need to scroll more than one screen to see a complete proposal or summary.

## General Rules

- **Minimize vertical space.** Prefer single-line bullets over multi-line blocks. Never use blank lines between list items.
- **State shared values once.** If all notes share a property value (e.g., context: work), say it once in the header, not per item.
- **Omit obvious details.** Don't repeat the operation type on every line. Don't show unchanged properties.
- **Use tables only for summaries of ≤10 items.** For larger sets, use grouped counts with expandable details only if the user asks.
- **No headers for single-section output.** If there's only one group, skip the group label and just list items.

## Proposal Format

Used when presenting any operation that needs user approval.

```
**<Operation> Proposal** — <N> files <shared context if any>

**<Group>:** <file.md> → <changes> · <file2.md> → <changes>
**<Group>:** <file.md> → <changes>

⚠ <Anything needing user input: ambiguous decisions, empty files>
```

For operations where each item has multiple property changes, use one bullet per file:

```
**<Operation> Proposal** — <N> files, all context: work

**Snippets:** file.md → topic: [aws] · other.md → topic: [linux]
**How-to:** guide.md → topic: [aws, terraform]
**Troubleshooting:** bug.md → topic: [k8s, helm], resolved: true

⚠ Empty files: note.md, draft.md — include or skip?
```

**Rules:**
- Bold label per group on the same line as items — no `###` headers
- Use ` · ` (middle dot) to separate multiple items on one line when they share the same changes pattern
- One line per group if items fit; wrap to bullets only if a single line would exceed ~120 chars
- Flag decisions needing user input with ⚠ at the end

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
