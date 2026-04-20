# ============================================================
# Q17. Copy contents of one file to another
#      after removing all digits (0–9).
# ============================================================

import os
import re


def copy_remove_digits(source_path: str, dest_path: str) -> dict:
    """
    Read source_path, strip every digit character, and write
    the cleaned content to dest_path.

    Returns a stats dictionary with counts of removed digits
    and total characters processed.
    """
    digit_count = 0
    total_chars = 0
    lines_read  = 0

    with open(source_path, "r", encoding="utf-8") as src, \
         open(dest_path,   "w", encoding="utf-8") as dst:

        for line in src:
            lines_read  += 1
            total_chars += len(line)

            # Count digits in this line
            digit_count += sum(1 for ch in line if ch.isdigit())

            # Remove all digit characters
            cleaned_line = re.sub(r"\d", "", line)
            dst.write(cleaned_line)

    return {
        "lines_read"    : lines_read,
        "total_chars"   : total_chars,
        "digits_removed": digit_count,
        "chars_written" : total_chars - digit_count,
    }


def create_sample_file(path: str):
    """Create a sample file containing digits for testing."""
    content = """\
Hello World123!
Python 3.11 was released in 2022.
My phone number is 9876543210.
The year 2024 is a leap year.
Pi approximation: 3.14159265
I have 5 cats and 2 dogs at home.
Today is the 18th day of the 4th month.
Rank 1: Alice (95 marks), Rank 2: Bob (88 marks).
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# ── Main ─────────────────────────────────────────────────────
SOURCE = "digits_source.txt"
DEST   = "digits_cleaned.txt"

# Create demo source file
if not os.path.exists(SOURCE):
    create_sample_file(SOURCE)
    print(f"  ✓ Created source file: '{SOURCE}'")

print("=" * 60)
print("  Copy File — Remove Digits")
print("=" * 60)

src  = input(f"  Source file (Enter for '{SOURCE}'): ").strip() or SOURCE
dest = input(f"  Dest   file (Enter for '{DEST}'  ): ").strip() or DEST

try:
    stats = copy_remove_digits(src, dest)

    print(f"\n  ✓ Done!")
    print(f"  Source        : {src}")
    print(f"  Destination   : {dest}")
    print("─" * 60)
    print(f"  Lines read    : {stats['lines_read']}")
    print(f"  Total chars   : {stats['total_chars']}")
    print(f"  Digits removed: {stats['digits_removed']}")
    print(f"  Chars written : {stats['chars_written']}")

    # ── Preview ──────────────────────────────────────────────
    print("\n  Preview of cleaned file:")
    print("─" * 60)
    with open(dest, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            print(f"  {i:2}│ {line}", end="")
            if i >= 10:
                print(f"\n  … (showing first 10 of {stats['lines_read']} lines)")
                break
    print("\n" + "=" * 60)

except FileNotFoundError:
    print(f"  ✗ Source file '{src}' not found.")
except PermissionError:
    print(f"  ✗ Permission error accessing files.")