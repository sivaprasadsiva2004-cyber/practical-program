# ============================================================
# Q16. Read a file and count number of lines,
#      words, and characters.
# ============================================================

import os


def analyse_file(filepath: str) -> dict:
    """
    Open and read a text file, then return a dictionary with:
      - line_count
      - word_count
      - char_count        (including spaces & newlines)
      - char_no_spaces    (excluding whitespace)
      - blank_lines
      - longest_line      (text and length)
      - shortest_line     (text and length, non-blank)
    """
    line_count       = 0
    word_count       = 0
    char_count       = 0
    char_no_spaces   = 0
    blank_lines      = 0
    longest_line     = ("", 0)
    shortest_line    = (None, float("inf"))

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line_count += 1
            char_count += len(line)

            stripped = line.strip()
            words    = stripped.split()

            word_count     += len(words)
            char_no_spaces += len(stripped.replace(" ", ""))

            if stripped == "":
                blank_lines += 1
            else:
                if len(stripped) > longest_line[1]:
                    longest_line = (stripped, len(stripped))
                if len(stripped) < shortest_line[1]:
                    shortest_line = (stripped, len(stripped))

    if shortest_line[0] is None:
        shortest_line = ("(no non-blank lines)", 0)

    return {
        "line_count"    : line_count,
        "word_count"    : word_count,
        "char_count"    : char_count,
        "char_no_spaces": char_no_spaces,
        "blank_lines"   : blank_lines,
        "longest_line"  : longest_line,
        "shortest_line" : shortest_line,
    }


def create_sample_file(path: str):
    """Create a sample text file for demonstration."""
    content = """\
Python is a high-level, interpreted programming language.
It emphasizes code readability and simplicity.

Python supports multiple programming paradigms including:
object-oriented, procedural, and functional programming.

Guido van Rossum created Python in the late 1980s.
The first version was released in 1991.

Python is widely used in:
  - Web development (Django, Flask)
  - Data Science & Machine Learning (NumPy, Pandas, TensorFlow)
  - Automation and scripting
  - Scientific computing

"Simple is better than complex." — The Zen of Python
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# ── Main ─────────────────────────────────────────────────────
SAMPLE_PATH = "sample_input.txt"

# Create sample file if it doesn't exist
if not os.path.exists(SAMPLE_PATH):
    create_sample_file(SAMPLE_PATH)
    print(f"  ✓ Created sample file: '{SAMPLE_PATH}'")

print("=" * 60)
print("  File Analyser")
print("=" * 60)

filepath = input(f"  Enter filename (press Enter for '{SAMPLE_PATH}'): ").strip()
if not filepath:
    filepath = SAMPLE_PATH

try:
    stats = analyse_file(filepath)

    print(f"\n  File           : {filepath}")
    print(f"  Size           : {os.path.getsize(filepath):,} bytes")
    print("─" * 60)
    print(f"  Lines (total)  : {stats['line_count']}")
    print(f"  Blank lines    : {stats['blank_lines']}")
    print(f"  Non-blank lines: {stats['line_count'] - stats['blank_lines']}")
    print(f"  Words          : {stats['word_count']}")
    print(f"  Characters     : {stats['char_count']} (incl. whitespace)")
    print(f"  Characters     : {stats['char_no_spaces']} (excl. whitespace)")
    print("─" * 60)
    lng = stats['longest_line']
    srt = stats['shortest_line']
    print(f"  Longest line   ({lng[1]} chars): '{lng[0][:50]}{'…' if len(lng[0])>50 else ''}'")
    print(f"  Shortest line  ({srt[1]} chars): '{srt[0][:50]}'")
    print("=" * 60)

except FileNotFoundError:
    print(f"  ✗ File '{filepath}' not found.")
except PermissionError:
    print(f"  ✗ Permission denied: '{filepath}'.")