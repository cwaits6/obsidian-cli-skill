# Migration Workflow: Migrate and Enrich Notes

Reorganize notes into a new folder while intelligently assigning properties. Two phases, each proposed and approved separately.

Before starting, read:
- The user's `config.yaml` for property schema, naming conventions, and batch settings
- [property-extraction-guide.md](property-extraction-guide.md) for content analysis rules
- [output-format-standard.md](output-format-standard.md) for formatting rules (compactness is critical)

## Phase 1: Property Assignment

1. Read all notes from the source folder
2. Analyze each note's content using the property extraction guide
3. Present a **Property Proposal** for review
4. On approval, set all properties via `obsidian property:set`

### Property Proposal Format

Use the proposal format from the output format standard. Group notes by assigned `type` using bold labels — never use `###` headers per type. One line per file.

```
**Property Proposal** — 12 files, all context: work

**Snippets:**
- file.md → topic: [aws]
- other.md → topic: [linux]
- script.md → topic: [bash]
**How-to:**
- guide.md → topic: [aws, terraform]
- setup.md → topic: [kubernetes]
**Troubleshooting:**
- bug.md → topic: [k8s, helm], resolved: true
**Reference:**
- concepts.md → topic: [kubernetes], tags: [kubernetes]
**Inbox:**
- draft.md → topic: [kubernetes]

⚠ Empty files: note.md, other.md — include or skip?
⚠ bug.md classified as troubleshooting (has problem/solution structure) — confirm?
```

### Proposal Rules

- Group by type, not by source folder
- One line per file — each file gets its own line with its assigned properties
- State shared values once in the header (e.g., context, destination) — never repeat per item
- If multiple files in the same group have identical properties, collapse with ` · `: `file.md · other.md → topic: [aws]`
- Call out conditional properties (e.g., `resolved`) inline with the item
- Flag empty files and ambiguous type decisions with ⚠

## Phase 2: Rename and Move

After properties are set:

1. Present a **Rename & Move Proposal**
2. New filenames follow `naming_conventions.file_format` from config.yaml
3. On approval, move all files via `obsidian move`

```
**Rename & Move Proposal** — 12 files → Notes/, convention: lowercase-kebab-case

- file.md → aws-cli-snippets.md
- other.md → linux-disk-cleanup.md
- guide.md → terraform-vpc-setup.md
- setup.md → k8s-cluster-init.md
- bug.md → helm-chart-timeout-fix.md
- concepts.md → k8s-networking-overview.md
- draft.md → k8s-notes.md
```

One line per file. No per-item headers, no extra vertical space.

## Approval Behavior

Controlled by `batch_settings.approval_mode` in config.yaml:

- **`batch`** — Present the entire phase as one proposal. Once approved, execute all operations without pausing to re-confirm between items.
- **`single`** — Present each note individually within each phase, getting approval before proceeding to the next.

## Batch Splitting

If notes exceed `batch_settings.max_batch_size`, split into multiple batches within each phase. Propose and get approval for each batch before executing it. Use the same compact format for each batch, adding a batch indicator: `**Batch 1/3** —`.
