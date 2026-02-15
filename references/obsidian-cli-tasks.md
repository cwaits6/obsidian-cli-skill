# Task Operations

Commands for viewing and managing tasks and checkboxes in your vault.

## tasks - List tasks in vault or file

```bash
obsidian tasks [all] [daily] [file=<name>] [path=<path>] [total] [done] [todo] [status="<char>"] [verbose]
```

**Parameters:**
- `all` - Flag: include all task types
- `daily` - Flag: only daily recurring tasks
- `file=<name>` - Limit to specific file
- `path=<path>` - Limit to folder
- `total` - Flag: show count
- `done` - Flag: only completed tasks
- `todo` - Flag: only incomplete tasks
- `status="<char>"` - Filter by status character
- `verbose` - Flag: detailed information

**Examples:**
```bash
# List all tasks
obsidian tasks

# Only incomplete tasks
obsidian tasks todo

# Completed tasks
obsidian tasks done

# Tasks in specific file
obsidian tasks file="MyProject/todo.md" total

# Daily recurring tasks
obsidian tasks daily verbose
```

## task - Show or update a task

```bash
obsidian task [ref=<path:line>] [file=<name>] [path=<path>] [line=<n>] [toggle] [done] [todo] [daily] [status="<char>"]
```

**Parameters:**
- `ref=<path:line>` - Reference to task (file:line)
- `file=<name>` - Target filename
- `path=<path>` - Target path
- `line=<n>` - Line number of task
- `toggle` - Flag: toggle task state
- `done` - Flag: mark as done
- `todo` - Flag: mark as todo
- `daily` - Flag: mark as daily recurring
- `status="<char>"` - Set custom status character

**Examples:**
```bash
# View task at specific line
obsidian task file="todo.md" line=5

# Toggle task state
obsidian task file="todo.md" line=5 toggle

# Mark as done
obsidian task ref="MyProject/todo.md:10" done

# Set custom status
obsidian task file="todo.md" line=3 status="!"
```

## Common Patterns

### Get task summary
```bash
obsidian tasks total done
obsidian tasks total todo
```

### Find daily recurring tasks
```bash
obsidian tasks daily verbose
```

### Explore task structure
```bash
obsidian tasks file="MyProject/roadmap.md" verbose
```
