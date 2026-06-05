# Compound Engineering

Portable AI-powered development tools. 29 agents, 32 commands, 24 skills.

## Philosophy

Each unit of engineering work should make subsequent units of work easier — not harder.

## Structure

- `agents/` — Specialized AI agents (design, research, review, workflow)
- `commands/` — Slash commands including workflow orchestrations
- `skills/` — Reusable skill definitions with references and templates
- `platforms/` — Platform-specific hooks (Claude Code)
- `plugin.yaml` — Plugin metadata

## Adding Components

### New Agent

1. Create `agents/{category}/{name}.md` with frontmatter (`name`, `description`, `model`)
2. Update README.md agent table

### New Command

1. Create `commands/{name}.md` with frontmatter (`name`, `description`)
2. Update README.md command table

### New Skill

1. Create `skills/{name}/SKILL.md` with frontmatter (`name`, `description`)
2. Add `references/`, `scripts/`, or `templates/` subdirectories as needed
3. Update README.md skill table

## Docs Output

Workflows write to `docs/`:
- `docs/solutions/` — Compounded learnings (keep in git)
- `docs/ideation/`, `docs/plans/`, `docs/brainstorms/`, `docs/execution-sessions/` — Ephemeral (gitignore)

## Count Verification

```bash
find agents -name '*.md' | wc -l     # Should match README count
find commands -name '*.md' | wc -l    # Should match README count
find skills -mindepth 1 -maxdepth 1 -type d | wc -l  # Should match README count
```
