#!/usr/bin/env python3
"""
XML Tag Extractor for LLM Outputs

Extracts content from specified XML-like tags, even if the markup is malformed
(e.g., unclosed tags at the end of a response due to context truncation).
"""

import sys
import re
import argparse
from typing import List


def extract_tags(text: str, tag: str, error_tolerant: bool = True) -> List[str]:
    """
    Extracts contents of the specified XML-like tag from the text.
    Handles multiple tags, attributes, and optionally unclosed tags at the end.

    The unclosed-tag fallback finds the LAST opening tag that has no matching
    closing tag. This handles the common case where repeated tags appear and
    only the final one is truncated.
    """
    # Match standard closed tags: <tag>...</tag> or <tag attr="val">...</tag>
    closed_pattern = rf"<{tag}(?:\s+[^>]*)?>(.*?)</{tag}>"
    matches = list(re.finditer(closed_pattern, text, re.DOTALL))

    results = [m.group(1).strip() for m in matches]

    if error_tolerant:
        # Fallback: find the last opening tag that has no closing tag after it.
        # This correctly handles cases where earlier same-name tags are properly
        # closed but a later one is truncated.
        open_pattern = rf"<{tag}(?:\s+[^>]*)?>"
        open_matches = list(re.finditer(open_pattern, text, re.DOTALL))

        for om in reversed(open_matches):
            start_pos = om.end()
            # Check if there's a closing tag after this opening tag
            remaining = text[start_pos:]
            close_pattern = rf"</{tag}>"
            if not re.search(close_pattern, remaining, re.DOTALL):
                # Avoid duplicating content already captured by a closed match
                # that starts at the same position
                already_captured = any(
                    m.start() == om.start() for m in matches
                )
                if not already_captured:
                    results.append(remaining.strip())
                break

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Extract content from XML tags in LLM outputs, tolerating malformed tags."
    )
    parser.add_argument("tag", help="The XML tag name to extract (without brackets).")
    parser.add_argument(
        "--file", "-f", help="Path to the file to parse. If not specified, reads from stdin."
    )
    parser.add_argument(
        "--strict", "-s", action="store_true", help="Disable error-tolerant parsing for unclosed tags."
    )
    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            print(f"Error reading file {args.file}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        text = sys.stdin.read()

    results = extract_tags(text, args.tag, error_tolerant=not args.strict)

    for match in results:
        print(match)


if __name__ == "__main__":
    main()
