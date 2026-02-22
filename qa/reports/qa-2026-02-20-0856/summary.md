# Obsidian CLI QA Report — 2026-02-20-0856

**Skill version:** obsidian-cli 1.2.0
**Model:** Claude Sonnet 4.6 (claude-sonnet-4-6)

---

## My Assessment

This automated test created via Claude Code to test the viability of this skill had some good tests and some that I think did not fully test the skill, however I still wanted to leave this generated report in here for informational purposes. I believe that doing manual testing might be more indicative of the actual capability of this plugin/skill so I can see personally how it reacts.

## Overall Result

**FAIL**

**Hard failures:**
- T3: No results — "kubernetes" not in any fixture file content (fixture gap, not a skill bug)
- T4: 3 reference files use singular `Example:` instead of `Examples:`

**Warnings:**
- T5: batch-executor agent not launched — skill executed 36 CLI commands inline (fallback path)
- T1: `topic` values written as strings (`"[productivity, knowledge-management]"`) instead of YAML lists

---

## Key Finding: Vault Name vs Path

The Obsidian CLI requires `vault="test_vault"` (the registered name) — not the full filesystem
path. Using the full path returns "Vault not found." This must be reflected in all skill prompts
that reference a test vault.

---

## T1 — Enrich Inbox

**Skill invoked:** YES
**Execution path:** Obsidian CLI (`obsidian property:set vault="test_vault" ...`)

| File | Type | Context | Topic | Status |
|---|---|---|---|---|
| Article-to-read.md | reference | personal | [productivity, knowledge-management] | PASS |
| Quick-thought.md | inbox | personal | [automation, api] | PASS |
| Welcome.md | note | personal | [obsidian, knowledge-management] | PASS |

**Note:** Topic values were written as quoted strings (`"[productivity, knowledge-management]"`)
rather than YAML list syntax. Obsidian renders these correctly but it is not clean YAML.

---

## T2 — Create Daily Template

**Skill invoked:** YES
**Execution path:** Obsidian CLI (`obsidian create` + `obsidian append`)

| Check | Status |
|---|---|
| New file created: Templates/daily-note-v2.md | PASS |
| Contains Templater date syntax | PASS |

**Note:** Skill created `daily-note-v2.md` to avoid overwriting the existing `daily-note.md`
fixture. Correct behavior.

---

## T3 — Search

**Skill invoked:** YES
**CLI executed:** `obsidian vault="test_vault" search query="kubernetes"`

| Check | Status |
|---|---|
| CLI search command ran successfully | PASS |
| Results returned for "kubernetes" | FAIL |

**Root cause:** No fixture file contains the word "kubernetes" — the Unsorted files reference
"K8s", "EKS", and "Kubernetes" (capital K) but not lowercase "kubernetes". The CLI search
returned "No matches found" which is accurate. This is a fixture gap, not a skill bug.

**Fix:** Add "kubernetes" (lowercase) to `K8s Pod Stuck Pending.md` fixture content.

---

## T4 — Reference Audit

**Status:** FAIL

**Hard failures (3):**
- `obsidian-cli-files.md:96` — `append` uses `Example:` (singular)
- `obsidian-cli-files.md:140` — `open` uses `Example:` (singular)
- `obsidian-cli-properties.md:72` — `property:remove` uses `Example:` (singular)

**Warnings (19):** Commands with fewer than 2 examples — snippets (4), sync (3), utilities (3),
plugins (2), dev (2), files (2), history (1), themes (1).

**Passes:** All 22 files use `param=value` syntax, have syntax blocks, Parameters sections, and
Common Patterns sections. No GNU-style `--flag` drift detected.

---

## T5 — Migrate & Enrich Unsorted

**Skill invoked:** YES
**Execution path:** Obsidian CLI (36 commands — 28 `property:set` + 8 `move`)
**batch-executor launched:** NO (inline fallback — see warning)

| Original File | New File | Type | Context | Topic | Status |
|---|---|---|---|---|---|
| API Rate Limiting.md | api-rate-limiting.md | reference | work | [api, backend] | PASS |
| EKS IRSA setup.md | eks-irsa-setup.md | how-to | work | [aws, eks, kubernetes] | PASS |
| GitLab CI Caching.md | gitlab-ci-caching.md | how-to | work | [gitlab, ci-cd] | PASS |
| helmValuesOverride.md | helm-values-override.md | snippet | work | [helm, kubernetes] | PASS |
| K8s Pod Stuck Pending.md | k8s-pod-stuck-pending.md | troubleshooting | work | [kubernetes] | PASS |
| remember to check.md | remember-to-check.md | inbox | work | [engineering] | PASS |
| Standup Feb 12.md | standup-feb-12.md | meeting | work | [engineering, team] | PASS |
| terraform_module_patterns.md | terraform-module-patterns.md | reference | work | [terraform, infrastructure] | PASS |

| Check | Status |
|---|---|
| All 8 files migrated via CLI | PASS |
| Unsorted/ empty after migration | PASS |
| All migrated files kebab-case | PASS |
| Files in Notes/ after migration | 20 (12 pre-existing + 8 migrated) |
| CLI failures | 0 |

**Warning — batch-executor not launched:** The skill ran all 36 CLI commands inline in the
planning model rather than delegating to the batch-executor agent. The SKILL.md specifies
delegation for batches >5 files. The fallback path was used instead.

---

## T6 — Update Base

**Skill invoked:** YES
**Execution path:** Obsidian CLI (`obsidian create ... overwrite`)

| Check | Status |
|---|---|
| test base.base written via CLI | PASS |
| Source points to Notes/ | PASS |
| Has type, context, topic columns | PASS |
| Sort by type ascending | PASS |

**Note:** Skill correctly used `name="test base.base"` with explicit extension to avoid the CLI
creating a `.md` file by default.

---

## Next Fixes

1. **T3 fixture** — Add "kubernetes" (lowercase) to `K8s Pod Stuck Pending.md` content
2. **T4 hard failures** — Fix `Example:` → `Examples:` in `files.md:96`, `files.md:140`, `properties.md:72`
3. **T4 warnings** — Add a second example to commands in snippets, sync, utilities, plugins, dev, files, history, themes
4. **batch-executor delegation** — Investigate why the planning model executes inline instead of delegating for large batches; may need stronger instruction in SKILL.md
5. **Topic YAML format** — Property values are being set as quoted strings rather than proper YAML list syntax; investigate whether this is a CLI limitation or a command construction issue
