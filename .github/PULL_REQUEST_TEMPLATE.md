## Summary

<!-- 1-3 sentences describing the change -->

## Type of Change

- [ ] New agent
- [ ] New command
- [ ] New skill
- [ ] Bug fix
- [ ] Documentation
- [ ] Refactor

## Component Counts

Run after changes:

```bash
find agents -name '*.md' | wc -l
find commands -name '*.md' | wc -l
find skills -mindepth 1 -maxdepth 1 -type d | wc -l
```

| Component | Before | After |
|-----------|--------|-------|
| Agents |  |  |
| Commands |  |  |
| Skills |  |  |

## Checklist

- [ ] README.md updated with new component
- [ ] AGENT.md updated if structure changed
- [ ] No personal references or secrets in added files
- [ ] Frontmatter `name` field matches filename (agents)
