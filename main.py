#!/usr/bin/env python3
"""Cat Reviews Its Human — a one-star review written by a house cat.

The entry is a single line, under 200 characters. The program writes it to
/output/entry.txt, where the sealed scorer reads it, and prints it.
"""

import os

LINE = "One star. The red dot escaped under the sofa again and the human just stood there holding the thing that makes it. Coward."

# Validate the entry: one line, at most 200 characters, no stray whitespace.
assert "\n" not in LINE, "entry must be a single line"
assert len(LINE) <= 200, f"entry too long: {len(LINE)} chars"
assert LINE == LINE.strip(), "entry must not have leading or trailing whitespace"

output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    f.write(LINE)

# Read it back and confirm the file holds exactly the line we wrote.
with open(output_path, encoding="utf-8") as f:
    assert f.read() == LINE, "round-trip mismatch: file content differs from LINE"

print(LINE)
