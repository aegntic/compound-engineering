# XML Tag Structure Best Practices & Guidelines

This reference document outlines the standards and conventions for using XML-like tags to structure prompts, LLM outputs, and multi-agent communication.

---

## 1. System Prompting Structure

Using XML tags to partition different parts of a system prompt or user input is one of the most effective ways to guide LLM behavior, prevent instruction drift, and mitigate prompt injection.

### Standard Template Structure

```xml
<system_instructions>
Define the core role, constraints, and operational protocols of the agent.
</system_instructions>

<context>
Provide background information, environment metadata, or project state.
</context>

<examples>
  <example>
    <input>Example input here</input>
    <output>Example output here</output>
  </example>
</examples>

<user_input>
The actual user query or task.
</user_input>
```

### Key Rules

- Use unique tag names to avoid collisions.
- Maintain a flat hierarchy where possible to reduce nesting complexity.
- Capitalization: Use lowercase with underscores (`snake_case`) or hyphens (`kebab-case`) for tag names.

---

## 2. LLM Output Structuring

When designing tasks where the LLM must return structured data, XML tags are often superior to JSON because:

1. They are easier for the model to generate incrementally (streaming).
2. They do not suffer from escaping issues as severely as JSON (e.g., double quotes, backslashes, newlines).
3. They tolerate parser errors and truncations much better.

### Designing Output Tags

Define clear start and end boundaries for the model to output:

```
I will analyze the file and output my thoughts.

<analysis>
This is where the detailed reasoning and analysis goes.
</analysis>

<result>
Final output or structured data here.
</result>
```

### Handling Nested Content & Special Characters (CDATA)

If the content inside a tag contains code (HTML, JS, XML examples) or special symbols, instruct the LLM to wrap the content in a CDATA section to avoid parsing conflicts:

```xml
<code_block>
<![CDATA[
def parse_xml(data):
    if "<tag>" in data:
        return True
]]>
</code_block>
```

---

## 3. Parsing & Error Tolerance

LLM outputs are not guaranteed to be strictly valid XML. Common issues include:

- **Truncation**: The output cuts off before the closing tag is printed (e.g., `<thought>some text...` with no `</thought>`).
- **Unescaped characters**: Using `<` or `&` directly inside text.
- **Missing root tag**: Multiple sibling elements without a single enclosing parent.

### Robust Parsing Workflow

1. **Do not use strict XML parsers directly** (e.g., standard `xml.etree.ElementTree`) on raw LLM text. They will throw exceptions on malformed markup.
2. **Use regex extraction**: Extract contents using a non-greedy regex for closed tags first.
3. **Handle unclosed tags**: If a closing tag is missing, find the last opening tag and extract all text from it to the end of the string. This correctly handles repeated same-name tags where only the final instance is truncated.
4. **Use BeautifulSoup / lxml**: If available, use parser features that auto-close tags and tolerate malformed markup.

### Canonical Parsing Function

The parsing logic is maintained in `scripts/parse_xml.py`. Import or call that script directly rather than duplicating the regex. The key logic:

```python
import re

def extract_tags(text: str, tag: str, error_tolerant: bool = True) -> list:
    # Match standard closed tags
    closed_pattern = rf"<{tag}(?:\s+[^>]*)?>(.*?)</{tag}>"
    matches = list(re.finditer(closed_pattern, text, re.DOTALL))
    results = [m.group(1).strip() for m in matches]

    if error_tolerant:
        # Fallback: find the LAST opening tag with no closing tag after it
        open_pattern = rf"<{tag}(?:\s+[^>]*)?>"
        open_matches = list(re.finditer(open_pattern, text, re.DOTALL))
        for om in reversed(open_matches):
            remaining = text[om.end():]
            if not re.search(rf"</{tag}>", remaining, re.DOTALL):
                already_captured = any(m.start() == om.start() for m in matches)
                if not already_captured:
                    results.append(remaining.strip())
                break

    return results
```

> **Note:** Always use the `scripts/parse_xml.py` script as the source of truth for parsing behavior. The snippet above is for reference only and may lag behind the script.

---

## 4. Streaming / Chunked Parsing

**Out of scope.** This guide covers parsing complete or truncated finished outputs only. Streaming parsing (processing partial chunks as they arrive over SSE) requires a stateful accumulator and is not covered here.

---

## 5. Security Considerations

- **Never render extracted tag contents as raw HTML** without sanitization. LLM output may contain `<script>` tags or other injection vectors.
- **Validate extracted content** before passing it to template engines, eval-like functions, or shell commands.
- **Beware of CDATA termination**: `]]>` inside user-controlled content can prematurely close a CDATA section. Sanitize or escape `]]>` sequences within content.
