Run the full Obsidian CLI QA harness. Tests run directly against the registered test vault so
the Obsidian CLI can operate against it. Results are snapshotted into a timestamped report dir
at the end, then the fixture is restored via git.

Run only after the latest skill version is installed.

---

## Setup

```bash
TIMESTAMP=$(date +%Y-%m-%d-%H%M)
REPORT_DIR="$(pwd)/qa/reports/qa-$TIMESTAMP"
mkdir -p "$REPORT_DIR"
VAULT_PATH="$(pwd)/qa/fixtures/test_vault"
CONFIG_PATH="$(pwd)/qa/fixtures/config.yaml"
SKILL_VERSION=$(grep '"version"' ~/.claude/plugins/marketplaces/obsidian-cli-skill/plugins/obsidian-cli/.claude-plugin/plugin.json 2>/dev/null | head -1 | grep -o '"[^"]*"' | tail -1 | tr -d '"' || echo "unknown")
```

Copy the example config and set `vault_path` to the test vault:

```bash
cp plugins/obsidian-cli/config.yaml.example "$CONFIG_PATH"
# Set vault_path to VAULT_PATH in config.yaml
```

**The fixture vault at `qa/fixtures/test_vault` is registered with Obsidian**, so CLI commands
will actually persist to disk. All tests modify this vault directly. After the run, the fixture
is restored.

---

## Phase 1 — Parallel Tests

Launch all of the following in parallel using the Task tool with `general-purpose` subagents.
Each subagent invokes the obsidian-cli skill, auto-approves any proposals, and returns a
completion marker with a brief summary.

These tests touch different parts of the vault and can safely run at the same time.

### T1 — Enrich Inbox

Invoke the obsidian-cli skill:

> "Set frontmatter on everything in my Inbox folder — assign type and topic based on each note's
> content. My config is at `<CONFIG_PATH>`"

Auto-approve the proposal. If any CLI command fails, do not write files directly — report the
exact CLI error and return `[T1_FAIL]`. Return `[T1_COMPLETE]` only if all changes were applied
via the Obsidian CLI, with each file and the type/topic assigned.

### T2 — Create Daily Template

Invoke the obsidian-cli skill:

> "Create a daily note template with date, tags, and a section for notes of the day. My vault
> is at `<VAULT_PATH>`"

Auto-approve the proposal. If the CLI command fails, do not write the file directly — report the
exact CLI error and return `[T2_FAIL]`. Return `[T2_COMPLETE]` only if the file was created via
the Obsidian CLI, with the filename.

### T3 — Search

Invoke the obsidian-cli skill:

> "Search my vault for notes mentioning kubernetes. My vault is at `<VAULT_PATH>`"

If the CLI search command fails, report the exact error and return `[T3_FAIL]`. Return
`[T3_COMPLETE]` with the list of matching files.

### T4 — Reference Audit

Launch the `qa-reference-auditor` agent. Return its full output.

---

## Phase 2 — Sequential Tests

Run after Phase 1. These touch Notes/ and Bases/ so they run in order.

### T5 — Migrate & Enrich Unsorted (batch-executor test)

The primary integration test. 8 files triggers the skill's batch delegation path — the
`batch-executor` agent should be launched after approval.

Invoke the obsidian-cli skill:

> "Migrate all the notes in my Unsorted folder to Notes with proper frontmatter. Analyze each
> note's content, assign type, context, and topic, rename files to kebab-case, then move them
> to Notes. My config is at `<CONFIG_PATH>`"

Auto-approve the proposal. If any CLI command fails, do not fall back to direct file writes —
report the exact CLI error and return `[T5_FAIL]`. **Record whether `batch-executor` was
launched** — its output is `[N/total] ✓ ...` lines ending with `**Done** — N succeeded, N
failed`. If absent, the skill executed inline (fallback path).

After completion, verify:

```bash
UNSORTED_EMPTY=$( [ -z "$(ls -A "$VAULT_PATH/Unsorted/" 2>/dev/null)" ] && echo "PASS" || echo "FAIL" )
NOTES_COUNT=$(find "$VAULT_PATH/Notes/" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
KEBAB_FAIL=$(find "$VAULT_PATH/Notes/" -name "*.md" 2>/dev/null | xargs -I{} basename {} | grep -E '[A-Z _]' || true)
KEBAB_CHECK=$( [ -z "$KEBAB_FAIL" ] && echo "PASS" || echo "FAIL" )
```

Read frontmatter from each migrated file and record: original filename, new filename, type,
context, topic.

### T6 — Update Base

Invoke the obsidian-cli skill:

> "Update the Base at Bases/test base.base to show all notes from the Notes folder with type,
> context, and topic columns, sorted by type. My config is at `<CONFIG_PATH>`"

Auto-approve. If the CLI command fails, do not write the file directly — report the exact CLI
error and return `[T6_FAIL]`. After completion, verify:

```bash
BASE_SOURCE=$(grep -q "source:" "$VAULT_PATH/Bases/test base.base" 2>/dev/null && echo "PASS" || echo "FAIL")
BASE_COLUMNS=$(grep -qE "type|context|topic" "$VAULT_PATH/Bases/test base.base" 2>/dev/null && echo "PASS" || echo "FAIL")
```

---

## Snapshot & Restore

After all tests complete:

```bash
# Snapshot the post-test vault state into the report dir
cp -r "$VAULT_PATH/" "$REPORT_DIR/vault/"

# Restore the fixture to its committed state
git restore qa/fixtures/test_vault/
git clean -fd qa/fixtures/test_vault/
```

Do not commit any changes to `qa/fixtures/test_vault/`. The report dir holds the result snapshot.

---

## Report

Write `$REPORT_DIR/summary.md`:

```markdown
# Obsidian CLI QA Report — <TIMESTAMP>

**Skill version:** obsidian-cli <SKILL_VERSION>
**Model:** <your model name and ID>

---

## T1 — Enrich Inbox

| File | Type | Context | Topic | Status |
|---|---|---|---|---|
| Article-to-read.md | ... | ... | ... | PASS/FAIL |
| Quick-thought.md | ... | ... | ... | PASS/FAIL |
| Welcome.md | ... | ... | ... | PASS/FAIL |

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
| Unsorted/ empty after migration | PASS/FAIL |
| All new files kebab-case | PASS/FAIL |
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

- Tests run against `qa/fixtures/test_vault/` directly — do not copy first
- Always restore the fixture at the end: `git restore qa/fixtures/test_vault/ && git clean -fd qa/fixtures/test_vault/`
- Never commit changes to `qa/fixtures/test_vault/`
- batch-executor not launching on T5 is a warning, not a hard failure
- Any test where the skill is not invoked = hard FAIL
- Any test where vault state doesn't match expected = hard FAIL
- **All vault changes must go through the Obsidian CLI.** If a subagent falls back to writing
  files directly instead of using `obsidian` CLI commands, that is a hard FAIL — do not accept
  it as equivalent. Report the CLI error that caused the fallback.
