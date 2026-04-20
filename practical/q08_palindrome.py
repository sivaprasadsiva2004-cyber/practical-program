# ============================================================
# Q8. Check whether a string is a palindrome
#     (a) with slicing  (b) without slicing.
# ============================================================

def clean(text: str) -> str:
    """
    Remove non-alphanumeric chars and convert to lowercase
    so 'A man, a plan, a canal: Panama' is treated as palindrome.
    """
    return "".join(ch.lower() for ch in text if ch.isalnum())


# ── Method 1: Using Slicing ──────────────────────────────────
def is_palindrome_slicing(text: str) -> bool:
    """Reverse the cleaned string with [::-1] and compare."""
    s = clean(text)
    return s == s[::-1]


# ── Method 2: Without Slicing (two-pointer approach) ─────────
def is_palindrome_no_slicing(text: str) -> bool:
    """
    Use two pointers (left and right) that move towards the centre.
    If any mismatch is found, it's not a palindrome.
    """
    s = clean(text)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left  += 1
        right -= 1
    return True


# ── Test cases ───────────────────────────────────────────────
test_cases = [
    "racecar",
    "hello",
    "Madam",
    "A man, a plan, a canal: Panama",
    "Was it a car or a cat I saw?",
    "Python",
    "No lemon, no melon",
    "12321",
    "12345",
]

print("=" * 65)
print(f"  {'String':<38}  {'Slicing':<10}  {'No-Slicing'}")
print("─" * 65)

for s in test_cases:
    r1 = is_palindrome_slicing(s)
    r2 = is_palindrome_no_slicing(s)
    mark1 = "✓ Yes" if r1 else "✗ No "
    mark2 = "✓ Yes" if r2 else "✗ No "
    print(f"  {s:<38}  {mark1:<10}  {mark2}")

print("=" * 65)

# ── Interactive check ────────────────────────────────────────
print()
user_str = input("  Enter your own string to check: ")
r = is_palindrome_slicing(user_str)
print(f"\n  '{user_str}' is {'a PALINDROME ✓' if r else 'NOT a palindrome ✗'}")
print("=" * 65)