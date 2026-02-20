Run the full Obsidian CLI QA harness. Tests are executed against a copy of the test vault —
the original fixture is never modified.

Run only after the latest skill version is installed.

---

## Setup

```bash
TIMESTAMP=$(date +%Y-%m-%d-%H%M)
REPORT_DIR="$(pwd)/qa/reports/qa-$TIMESTAMP"
mkdir -p "$REPORT_DIR"
cp -r qa/fixtures/test_vault/ "$REPORT_DIR/vault/"
cp plugins/obsidian-cli/config.yaml.example "$REPORT_DIR/config.yaml"
SKILL_VERSION=$(grep '"version"' ~/.claude/plugins/marketplaces/obsidian-cli-skill/plugins/obsidian-cli/.claude-plugin/plugin.json 2>/dev/null | head -1 | grep -o '"[^"]*"' | tail -1 | tr -d '"' || echo "unknown")
```

Set `vault_path` in `$REPORT_DIR/config.yaml` to the absolute path of `$REPORT_DIR/vault`.

---

## Phase 1 — Parallel Tests

Launch all of the following in parallel using the Task tool with `general-purpose` subagents.
Each subagent should invoke the obsidian-cli skill with its prompt, auto-approve any proposals,
and return a completion marker with a brief summary of what was done.

These tests do not touch overlapping parts of the vault and can safely run at the same time.

### T1 — Enrich Inbox

Invoke the obsidian-cli skill:

> "Set frontmatter on everything in my Inbox folder — assign type and topic based on each note's
> content. My config is at `<CONFIG_PATH>`"

Auto-approve the proposal. Return `[T1_COMPLETE]` with a list of files and their assigned
properties when done.

### T2 — Create Daily Template

Invoke the obsidian-cli skill:

> "Create a daily note template with date, tags, and a section for notes of the day."

Auto-approve the proposal. Return `[T2_COMPLETE]` with the filename of the created template.

### T3 — Search

Invoke the obsidian-cli skill:

> "Search my vault for notes mentioning kubernetes. My vault is at `<VAULT_PATH>`"

Return `[T3_COMPLETE]` with the list of matching files returned by the skill.

### T4 — Reference Audit

Launch the `qa-reference-auditor` agent. Return its full output.

---

## Phase 2 — Sequential Tests

Run these after Phase 1 completes. They share the Notes/ and Bases/ areas so they run in order.

### T5 — Migrate & Enrich Unsorted (batch-executor test)

This is the primary integration test. The migration involves 8 files, which should trigger the
skill to delegate execution to the `batch-executor` agent after approval.

Invoke the obsidian-cli skill:

> "Migrate all the notes in my Unsorted folder to Notes with proper frontmatter. Analyze each
> note's content, assign type, context, and topic, rename files to kebab-case, then move them to
> Notes. My config is at `<CONFIG_PATH>`"

Auto-approve the proposal. **Observe and record whether the `batch-executor` agent was launched**
— its output has the format `[N/total] ✓ ...` with a final `**Done** — N succeeded, N failed`
line. If you see that output, batch-executor ran. If not, the skill executed directly.

After completion, verify:

```bash
UNSORTED_EMPTY=$( [ -z "$(ls -A "$REPORT_DIR/vault/Unsorted/" 2>/dev/null)" ] && echo "PASS" || echo "FAIL" )
NOTES_COUNT=$(find "$REPORT_DIR/vault/Notes/" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
KEBAB_FAIL=$(find "$REPORT_DIR/vault/Notes/" -name "*.md" 2>/dev/null | xargs -I{} basename {} | grep -E '[A-Z _]' || true)
KEBAB_CHECK=$( [ -z "$KEBAB_FAIL" ] && echo "PASS" || echo "FAIL" )
```

Read frontmatter from each migrated file and record: original filename, new filename, type,
context, topic.

### T6 — Update Base

Invoke the obsidian-cli skill:

> "Update the Base at Bases/test base.base to show all notes from the Notes folder with type,
> context, and topic columns, sorted by type. My config is at `<CONFIG_PATH>`"

Auto-approve the proposal. After completion, verify:

```bash
BASE_SOURCE=$(grep -q "source:" "$REPORT_DIR/vault/Bases/test base.base" 2>/dev/null && echo "PASS" || echo "FAIL")
BASE_COLUMNS=$(grep -qE "type|context|topic" "$REPORT_DIR/vault/Bases/test base.base" 2>/dev/null && echo "PASS" || echo "FAIL")
```

---

## Report

Write `$REPORT_DIR/summary.md`:

```markdown
# Obsidian CLI QA Report — <TIMESTAMP>

**Skill version:** obsidian-cli <SKILL_VERSION>
**Model:** <your model name and ID>

---

## T1 — Enrich Inbox

| File | Type | Topic | Status |
|---|---|---|---|
| Article-to-read.md | ... | ... | PASS/FAIL |
| Quick-thought.md | ... | ... | PASS/FAIL |
| Welcome.md | ... | ... | PASS/FAIL |

---

## T2 — Create Daily Template

| Check | Status |
|---|---|
| New file created in Templates/ | PASS/FAIL |
| Contains Templater date syntax | PASS/FAIL |

---

## T3 — Search

| Check | Status |
|---|---|
| Results returned for "kubernetes" | PASS/FAIL |
| Matching files | <list> |

---

## T4 — Reference Audit

<paste full qa-reference-auditor output>

---

## T5 — Migrate & Enrich Unsorted

**batch-executor launched:** YES / NO

| Original File | New File | Type | Context | Topic | Status |
|---|---|---|---|---|---|
| K8s Pod Stuck Pending.md | ... | ... | ... | ... | PASS/FAIL |
| terraform_module_patterns.md | ... | ... | ... | ... | PASS/FAIL |
| GitLab CI Caching.md | ... | ... | ... | ... | PASS/FAIL |
| EKS IRSA setup.md | ... | ... | ... | ... | PASS/FAIL |
| helmValuesOverride.md | ... | ... | ... | ... | PASS/FAIL |
| Standup Feb 12.md | ... | ... | ... | ... | PASS/FAIL |
| API Rate Limiting.md | ... | ... | ... | ... | PASS/FAIL |
| remember to check.md | ... | ... | ... | ... | PASS/FAIL |

| Check | Status |
|---|---|
| Unsorted/ empty | PASS/FAIL |
| All kebab-case | PASS/FAIL |
| Files in Notes/ after migration | <N> |

---

## T6 — Update Base

| Check | Status |
|---|---|
| test base.base updated | PASS/FAIL |
| Source points to Notes/ | PASS/FAIL |
| Has type, context, topic columns | PASS/FAIL |

---

## Overall Result

**<PASS or FAIL>**

Hard failures: <list or "none">
Warnings: <list or "none">
```

---

## Rules

- Do NOT modify `qa/fixtures/test_vault/` — it is the immutable baseline
- All changes go to `$REPORT_DIR/vault/` only
- batch-executor not launching on T5 is a warning, not a hard failure (skill may fall back to
  direct execution)
- Any test where the skill is not invoked at all = hard FAIL
- Any test where vault state doesn't match expected = hard FAIL
