---
name: xml-tag-structure
description: Guide for structuring, parsing, and validating XML-like tags in LLM inputs, system prompts, outputs, and agent-to-agent communication. Use this skill when designing prompt templates, parsing structured content from text, or handling nested tag boundaries.
---

# XML Tag Structure

## Overview

This skill provides guidelines and tools for utilizing XML-like tags to structure prompts, format LLM output payloads, and robustly parse structured text data. It helps maintain clear delimiters for instruction blocks and data boundaries, even when dealing with malformed or truncated text.

## File Tree

```
xml-tag-structure/
├── SKILL.md                     # This file. Skill definition and workflow guide.
├── references/
│   └── xml-guidelines.md        # Comprehensive best-practices reference for XML tags.
└── scripts/
    └── parse_xml.py             # CLI tool for extracting tag contents from text.
```

## Workflow Decision Tree

To handle XML tags in LLM workflows, follow this process:

1. **Structuring Prompts**: Wrap instructions, context, input variables, and output schemas in clean, snake_case XML tags.
2. **Structuring Outputs**: Define specific tags for the model to output, using CDATA sections for nested code or raw markup blocks.
3. **Parsing Output Payloads**: Run robust parsing logic to extract tags, handling potentially truncated responses and malformed markup.

---

## 1. Structuring Prompts

When designing system prompts, wrap different types of information in explicit tags. This helps the LLM distinguish instruction from context or user input, preventing prompt injection and instructions leakage.

### Standard Tag Categories

- `<system_instructions>`: Define the agent's identity, rules, and core directives.
- `<context>`: Provide background information, schemas, file contexts, or system state.
- `<examples>`: Enclose few-shot examples (each inside `<example>`).
- `<user_input>`: Enclose the current input or request to process.

### Rules for Prompt Tags

- Use snake_case or kebab-case for tag names (e.g., `<file_content>` or `<file-content>`).
- Keep tag names descriptive and singular/plural consistent (e.g., `<item>` inside `<items>`).
- Avoid mixing tags with standard markup or styling unless explicitly wrapping inline values.

---

## 2. Formatting LLM Output Payloads

Instruct the LLM to output structured data wrapped in specific XML tags. This approach avoids JSON escaping issues and is easier for the model to stream.

### Output XML Guidelines

- Request unique tag wrappers for each output section (e.g., `<thought>`, `<reasoning>`, `<code_changes>`, `<final_answer>`).
- Wrap any code or characters that look like XML tags in CDATA blocks: `<![CDATA[ ... ]]>`.
- Ensure all block tags are placed on their own lines to ease regex-based line splitting and parsing.

---

## 3. Parsing and Handling Malformed Tags

LLM outputs are occasionally malformed or truncated due to context limits. Do not use strict parser APIs directly on raw output. Instead, use robust regex extraction.

### Using the Bundled Extractor Script

Use the bundled script `scripts/parse_xml.py` to extract tag contents from text files or standard input.

#### Syntax

```bash
python3 scripts/parse_xml.py <tag_name> [-f <file_path>] [--strict]
```

#### Examples

Extract the content of the `<thought>` tag from a saved file:

```bash
python3 scripts/parse_xml.py thought -f response.txt
```

Extract the content of the `<response>` tag from standard input:

```bash
cat response.txt | python3 scripts/parse_xml.py response
```

Use the `--strict` flag to disable fallback parsing for unclosed/truncated tags (strict parsing matches closed tags only):

```bash
python3 scripts/parse_xml.py result -f response.txt --strict
```

---

## 4. Streaming / Chunked Parsing

**Status: Out of scope for this skill.**

Streaming and chunked parsing (processing partial LLM output as it arrives over SSE or chunked transfer) introduces distinct challenges: detecting partial opening tags, buffering incomplete content, and deciding when to emit extracted results. This skill focuses on parsing complete or truncated *finished* outputs. For streaming use cases, consider building a stateful streaming parser that accumulates chunks and applies the extraction logic from `scripts/parse_xml.py` once the stream closes or a boundary is detected.

---

## References

For detailed standards and examples, see:

- `references/xml-guidelines.md` — Comprehensive guide on XML tags in prompts and outputs.
