"""Writes the funniest warning label for a time machine to /output/entry.txt."""
import os

TEXT = "WARNING: This time machine goes backwards. Your mistakes go with it. So do the consequences."

# Rule: the warning label must be a single line of 1 to 120 characters.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 120, f"entry must be one line, 1-120 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
