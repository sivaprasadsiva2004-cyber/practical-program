# ============================================================
# Q15. Count frequency of each word in a text
#      using a dictionary.
# ============================================================

import string
from collections import Counter   # also shown as a comparison


def word_frequency_manual(text: str) -> dict:
    """
    Manual approach using a plain dictionary.
    Steps:
      1. Convert to lowercase.
      2. Remove punctuation.
      3. Split into words.
      4. Build frequency dictionary.
    """
    # Lowercase and strip punctuation
    translator = str.maketrans("", "", string.punctuation)
    cleaned    = text.lower().translate(translator)

    words = cleaned.split()

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1   # increment or start at 1

    return freq


def display_frequency(freq: dict, title: str = "Word Frequency"):
    """Display sorted frequency table."""
    # Sort by frequency (desc), then alphabetically for ties
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    print(f"\n  {title}")
    print(f"  {'Word':<20} {'Count':>5}  {'Bar'}")
    print("─" * 45)
    for word, count in sorted_freq:
        bar = "█" * count
        print(f"  {word:<20} {count:>5}  {bar}")


# ── Sample text ───────────────────────────────────────────────
sample_text = """
To be, or not to be, that is the question.
Whether 'tis nobler in the mind to suffer
the slings and arrows of outrageous fortune,
or to take arms against a sea of troubles
and by opposing end them. To die, to sleep,
no more; and by a sleep to say we end
the heartache and the thousand natural shocks
that flesh is heir to.
"""

print("=" * 55)
print("  Word Frequency Counter")
print("=" * 55)
print(f"\n  Text:\n  {sample_text.strip()}\n")

# ── Manual approach ───────────────────────────────────────────
freq_manual = word_frequency_manual(sample_text)
display_frequency(freq_manual, "Manual Dictionary Approach")

# ── Built-in Counter approach ─────────────────────────────────
translator = str.maketrans("", "", string.punctuation)
cleaned    = sample_text.lower().translate(translator)
freq_counter = dict(Counter(cleaned.split()))
print(f"\n  Using collections.Counter: same result = "
      f"{freq_manual == freq_counter}")

# ── Statistics ────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  Statistics")
print("─" * 55)
print(f"  Total words   : {sum(freq_manual.values())}")
print(f"  Unique words  : {len(freq_manual)}")
most_common = max(freq_manual, key=freq_manual.get)
print(f"  Most frequent : '{most_common}' ({freq_manual[most_common]} times)")

# ── Interactive ──────────────────────────────────────────────
print("\n" + "=" * 55)
user_text = input("  Enter your own text (single line): ").strip()
if user_text:
    uf = word_frequency_manual(user_text)
    display_frequency(uf, "Your Text – Word Frequency")
print("=" * 55)