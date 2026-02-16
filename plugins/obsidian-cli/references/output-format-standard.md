# Output Format Standard

All user-facing output from this skill must follow these formats for consistency and scannability.

## Proposal Format

Used when presenting any operation that needs user approval before execution.

```
## <Operation Type> Proposal

<Brief summary: what will happen, how many files, shared values stated once>

### <Group Label>
- path/to/file.md → <changes>
- path/to/other.md → <changes>

### <Group Label>
- path/to/another.md → <changes>

### Notes
- <Anything requiring user input: ambiguous decisions, empty files, edge cases>
```

**Rules:**
- Header states the operation type and count
- Group by logical category (type for properties, folder for moves, etc.)
- Shared values (e.g., all notes share the same context) stated once at the top, not repeated per item
- Compact bullet format: `- path → changes`
- Flag decisions that need user input in a Notes section

## Progress Format

Used during execution to show inline status.

```
[1/15] ✓ path/to/file.md — property set
[2/15] ✓ path/to/other.md — property set
[3/15] ✗ path/to/broken.md — error: file not found
```

**Rules:**
- Running count: `[n/total]`
- Checkmark (✓) for success, cross (✗) for failure
- Brief status after the dash

## Summary Format

Used after an operation completes to show final results.

```
## Summary

| File | Status | Details |
|------|--------|---------|
| file.md | ✓ | type: snippet, topic: [aws] |
| other.md | ✓ | moved to Notes/other-file.md |
| broken.md | ✗ | file not found |

**Results:** 13 succeeded, 1 failed, 1 skipped
```

**Rules:**
- Table with columns: File, Status, Details
- Total counts at the bottom: succeeded, failed, skipped
- Only include the Details column content that's relevant to the operation

## Error Format

Used when an individual operation fails.

```
**Error:** `obsidian property:set name=type value=snippet file="path/to/file.md"`
**Output:** <error message from CLI>
**Fix:** <suggested resolution>
```

**Rules:**
- Show the exact command that failed
- Include the CLI error output
- Suggest a fix or next step

## Search Results Format

Used when presenting search or analysis results.

```
## Search Results: "<query>"

Found <N> matches across <M> files.

### folder/
- **file.md** (line 12): ...matching snippet with **highlighted** term...
- **other.md** (line 45): ...matching snippet with **highlighted** term...

### another-folder/
- **note.md** (line 3): ...matching snippet with **highlighted** term...
```

**Rules:**
- Group by folder for spatial context
- Show file path, line number, and a snippet with the match bolded
- State total counts in the header
