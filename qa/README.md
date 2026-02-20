# Local Obsidian QA

This directory contains local-only validation assets for the Obsidian CLI skill. It is intentionally stored at repository root and is not bundled in the published plugin package.

## Commands

### `/obsidian-qa` — Trigger & Reference Validation

Validates skill quality by testing actual trigger behavior and reference compliance.

1. **Skill trigger tests** — launches one haiku agent per prompt in `qa/trigger-tests.md`, checks whether the `obsidian-cli` skill correctly triggers (or stays silent). Generates a timestamped report in `qa/reports/`.
2. **Reference audit** — checks all reference files for format compliance, syntax violations, and command coverage against `obsidian help`.

### `/obsidian-smoke` — Functional Smoke Test

Runs the skill end-to-end against a copied test vault to verify it can analyze, enrich, rename, and migrate notes.

1. Copies `qa/fixtures/test_vault/` into a timestamped report directory
2. Invokes the skill to enrich and migrate 8 raw notes from `Unsorted/` to `Notes/`
3. Validates that files are renamed to `lowercase-kebab-case`, frontmatter is added, and `Unsorted/` is empty
4. Writes a `summary.md` with results

**What it tests:**
- Content analysis and property assignment (type, context, topic)
- File renaming from messy names to kebab-case
- Migration from `Unsorted/` to `Notes/`
- Multiple note types: troubleshooting, how-to, reference, snippet, meeting, inbox

## Test Matrix

`qa/trigger-tests.md` defines three categories:
- **Should Trigger** — prompts that reference vault/Obsidian context
- **Should Not Trigger** — prompts that share vocabulary (notes, frontmatter, markdown) but lack Obsidian context
- **Borderline** — ambiguous prompts that should NOT trigger without clarification

## Test Notes

`qa/fixtures/test_vault/Unsorted/` contains 8 raw notes with no frontmatter and intentionally messy filenames (mixed casing, spaces, underscores, camelCase). These serve as input for `/obsidian-smoke`.

## Reports

Each QA run generates a markdown report in `qa/reports/` with:
- Pass/fail per prompt (trigger tests)
- Results table and diff command (smoke tests)
- Overall verdict

These reports serve as proof that the skill was tested before release.

## Severity Model

- Hard failure:
  - skill triggers when it should NOT (false positive)
  - skill does NOT trigger when it should (false negative)
  - command syntax violations in references
- Warning:
  - borderline prompt mismatches
  - description drift in references
  - missing examples
