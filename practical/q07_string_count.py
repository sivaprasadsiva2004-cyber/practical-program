# ============================================================
# Q7. Count vowels, consonants, digits, and
#     special characters in a string.
# ============================================================

def analyse_string(text: str) -> dict:
    """
    Analyse the given string and return counts of:
    vowels, consonants, digits, whitespace, special characters.
    """
    VOWELS = set("aeiouAEIOU")

    counts = {
        "vowels"    : 0,
        "consonants": 0,
        "digits"    : 0,
        "whitespace": 0,
        "special"   : 0,
    }

    vowel_found     = []
    consonant_found = []
    digit_found     = []
    special_found   = []

    for ch in text:
        if ch in VOWELS:
            counts["vowels"] += 1
            vowel_found.append(ch)
        elif ch.isalpha():
            counts["consonants"] += 1
            consonant_found.append(ch)
        elif ch.isdigit():
            counts["digits"] += 1
            digit_found.append(ch)
        elif ch.isspace():
            counts["whitespace"] += 1
        else:
            counts["special"] += 1
            special_found.append(ch)

    counts["_details"] = {
        "vowels"    : vowel_found,
        "consonants": consonant_found,
        "digits"    : digit_found,
        "special"   : special_found,
    }
    return counts


# ── Main ─────────────────────────────────────────────────────
print("=" * 60)
print("   String Character Analyser")
print("=" * 60)

text = input("  Enter a string: ")
result = analyse_string(text)

print(f"\n  Input String  : '{text}'")
print(f"  Total Length  : {len(text)}")
print("─" * 60)
print(f"  Vowels       ({result['vowels']:3d})  : "
      f"{result['_details']['vowels']}")
print(f"  Consonants   ({result['consonants']:3d})  : "
      f"{result['_details']['consonants']}")
print(f"  Digits       ({result['digits']:3d})  : "
      f"{result['_details']['digits']}")
print(f"  Whitespace   ({result['whitespace']:3d})")
print(f"  Special Chars({result['special']:3d})  : "
      f"{result['_details']['special']}")
print("─" * 60)
total = sum(v for k, v in result.items() if k != "_details")
print(f"  Total counted : {total}")
print("=" * 60)