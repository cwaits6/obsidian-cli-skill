# Migration Workflow: Migrate and Enrich Notes

Reorganize notes into a new folder while intelligently assigning properties. This workflow has two phases, each presented and approved separately.

Before starting, read:
- The user's `config.yaml` for property schema, naming conventions, and batch settings
- [property-extraction-guide.md](property-extraction-guide.md) for how to analyze note content
- [output-format-standard.md](output-format-standard.md) for how to format proposals and results

## Phase 1: Property Assignment

1. Read all notes from the source folder
2. Analyze each note's content using the property extraction guide
3. Present a **Property Proposal** grouped by type for review
4. On approval, set all properties via `obsidian property:set`

### Property Proposal Format

Group notes by their assigned `type` under category headers. Follow the output format standard for structure.

```
## Property Proposal

I'll organize your <N> notes with the following property assignments (all context: "<context>"):

### Snippets (reusable commands)
- Source/File.md → type: snippet, topic: [aws]
- Source/Other.md → type: snippet, topic: [linux]

### Troubleshooting (problem + solution)
- Source/Bug.md → type: troubleshooting, topic: [kubernetes, helm], resolved: true

### How-to (step-by-step procedures)
- Source/Guide.md → type: how-to, topic: [aws, terraform]

### Reference (documents what something is/how it works)
- Source/Concepts.md → type: reference, topic: [kubernetes], tags: [kubernetes]

### Inbox (unstructured captures)
- Source/Draft.md → type: inbox, topic: [kubernetes]

### Additional Notes
- Troubleshooting notes with resolved solutions: Bug.md, Fix.md
- Empty files: Note.md, Other.md — include or skip?
- Type decision rationale for any ambiguous notes
```

### Proposal Rules

- Group by type, not by source folder
- Only show properties that differ from defaults (e.g., if all share the same context, state it once at the top)
- Call out conditional properties (e.g., `resolved`) separately
- Flag empty files and ambiguous type decisions for user input

## Phase 2: Rename and Move

After properties are set:

1. Present a **Rename & Move Proposal** showing old filenames → new filenames + destination
2. New filenames follow the `naming_conventions.file_format` specified in config.yaml
3. On approval, move all files via `obsidian move`

```
## Rename & Move Proposal

All files will be moved to: <destination_path>
File naming convention: <file_format from config.yaml>

- Source/Folder/File.md → new-filename.md
- Source/Folder/Other File.md → other-filename.md
- ...
```

## Approval Behavior

Controlled by `batch_settings.approval_mode` in config.yaml:

- **`batch`** — Each phase is presented as a complete summary. Once approved, all operations in that phase execute without further prompts. Do not pause between operations to re-confirm.
- **`single`** — Claude presents each note individually within each phase, getting approval before proceeding to the next note.

## Batch Splitting

If the number of notes exceeds `batch_settings.max_batch_size` in config.yaml, split notes into multiple batches within each phase — propose and get approval for each batch before executing it.
