# Compound Engineering

Portable AI-powered development tools for any coding agent. 29 specialized agents, 32 commands, and 24 skills for Claude Code, GitHub Copilot, and OpenCode.

**Philosophy:** Each unit of engineering work should make subsequent units of work easier — not harder.

## Install

```bash
# Claude Code
claude install-plugin https://github.com/aegntic/compound-engineering

# Or clone directly
git clone https://github.com/aegntic/compound-engineering.git ~/.claude/skills/compound-engineering
```

## Structure

```
compound-engineering/
├── agents/           # 29 specialized AI agents
│   ├── design/       # 3 agents (design review, iteration, Figma sync)
│   ├── research/     # 8 agents (best practices, docs, git history, issues)
│   ├── review/       # 17 agents (code review, security, architecture, language-specific)
│   └── workflow/     # 3 agents (bug reproduction, PR comments, spec analysis)
├── commands/         # 32 slash commands
│   └── workflows/    # Core workflows (compound, plan, review, work, brainstorm, ideate)
├── skills/           # 24 skills
├── platforms/        # Platform-specific hooks
└── plugin.yaml       # Plugin metadata
```

## Agents

### Design (3)

| Agent | Purpose |
|-------|---------|
| `design-implementation-reviewer` | Compare live UI against Figma designs |
| `design-iterator` | Iterative UI refinement through screenshot-analyze-improve cycles |
| `figma-design-sync` | Detect and fix visual differences between implementation and Figma |

### Research (8)

| Agent | Purpose |
|-------|---------|
| `best-practices-researcher` | Research external best practices and documentation |
| `framework-docs-researcher` | Gather framework/library documentation and examples |
| `git-history-analyzer` | Archaeological analysis of git history |
| `issue-intelligence-analyst` | Analyze GitHub issues for recurring patterns |
| `learnings-researcher` | Search past solutions in `docs/solutions/` |
| `repo-research-analyst` | Research repository structure and conventions |

### Review (17)

| Agent | Purpose |
|-------|---------|
| `agent-native-reviewer` | Ensure agent-native action parity |
| `architecture-strategist` | SOLID compliance and clean architecture review |
| `code-simplicity-reviewer` | Complexity elimination and readability |
| `data-integrity-guardian` | Database migration and data model safety |
| `data-migration-expert` | Validate data migrations against reality |
| `deployment-verification-agent` | Go/No-Go deployment checklists |
| `frontend-race-conditions-reviewer` | Async UI race conditions and stale state |
| `laravel-reviewer` | Laravel 11+ / PHP 8.3+ best practices |
| `nestjs-reviewer` | NestJS simplicity, performance, security |
| `pattern-recognition-specialist` | Design patterns and anti-patterns |
| `performance-oracle` | Performance bottlenecks and algorithmic complexity |
| `python-reviewer` | Pythonic patterns, type safety, security |
| `rust-reviewer` | Ownership correctness, unsafe discipline, zero-cost abstractions |
| `schema-drift-detector` | Schema snapshot and artifact drift detection |
| `security-sentinel` | OWASP Top 10 security audit |
| `typescript-reviewer` | Type safety, modern patterns, maintainability |
| `vue-reviewer` | Vue.js/Nuxt best practices and performance |

### Workflow (3)

| Agent | Purpose |
|-------|---------|
| `bug-reproduction-validator` | Systematically reproduce and validate bug reports |
| `pr-comment-resolver` | Address PR review comments with requested changes |
| `spec-flow-analyzer` | Analyze specs for user flow completeness |

## Key Commands

| Command | Description |
|---------|-------------|
| `/workflows:compound` | Document solved problems to compound team knowledge |
| `/workflows:plan` | Structured implementation planning |
| `/workflows:review` | Multi-agent code review |
| `/workflows:work` | Execute a planned work session |
| `/workflows:brainstorm` | Structured brainstorming |
| `/workflows:ideate` | Generate and evaluate improvement ideas |
| `/workflows:architecture` | Architecture review and improvement |
| `/workflows:constitution` | Define project engineering principles |
| `/lfg` | Start accelerated development |
| `/ralph-loop` | Automated improvement loop |
| `/triage` | Triage GitHub issues |
| `/reproduce-bug` | Systematic bug reproduction |
| `/resolve_parallel` | Resolve PR comments in parallel |
| `/test-browser` | Browser-based testing |
| `/changelog` | Generate changelog |
| `/deepen-plan` | Deepen an existing plan |

## Skills

| Skill | Purpose |
|-------|---------|
| `agent-browser` | Browser automation via Vercel agent-browser CLI |
| `agent-native-architecture` | Build applications where agents are first-class citizens |
| `agent-native-audit` | Scored audit of agent-native architecture principles |
| `brainstorming` | Explore user intent before implementing |
| `caveman` | Ultra-compressed communication (~75% token reduction) |
| `compound-docs` | Capture solved problems as searchable documentation |
| `compound-refresh` | Refresh stale learnings against current codebase |
| `create-agent-skills` | Expert guidance for authoring Claude Code skills |
| `document-review` | Refine brainstorm/plan documents |
| `file-todos` | File-based todo tracking system |
| `finishing-branch` | Verify quality and clean up feature branches |
| `frontend-design` | Production-grade frontend interfaces |
| `gemini-imagegen` | Image generation via Gemini API |
| `git-worktree` | Git worktree management for parallel development |
| `grill-me` | Relentlessly interview user about a plan or design |
| `ideate` | Generate and evaluate grounded improvement ideas |
| `laravel-conventions` | Modern Laravel 11+ / PHP 8.3+ coding standards |
| `orchestrating-swarms` | Multi-agent swarm orchestration |
| `rclone` | Cloud storage file management via rclone |
| `resolve-pr-parallel` | Resolve PR comments using parallel processing |
| `setup` | Configure review agents for your stack |
| `skill-creator` | Guide for creating effective skills |
| `systematic-debugging` | Structured 4-phase debugging methodology |
| `ubiquitous-language` | DDD-style ubiquitous language glossary extraction |

## Docs Convention

Workflows write output to `{project_root}/docs/`:

```
docs/
├── ideation/              # Ideation artifacts
├── plans/                 # Implementation plans
├── brainstorms/           # Brainstorm documents
├── solutions/             # Compounded learnings (keep in git)
└── execution-sessions/    # Work session logs
```

## MCP Server

Includes Context7 MCP server integration for enhanced documentation lookup.

## License

MIT
