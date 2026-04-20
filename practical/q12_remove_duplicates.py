# ============================================================
# Q12. Remove duplicates from a list while maintaining order.
# ============================================================

# ── Method 1: Using a set as a "seen" tracker ─────────────────
def remove_duplicates_set(lst: list) -> list:
    """
    O(n) average time.  Uses a set to track already-seen elements.
    Preserves the first occurrence of each element.
    """
    seen   = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# ── Method 2: Using dict.fromkeys() (Python 3.7+ ordered dict) ──
def remove_duplicates_dict(lst: list) -> list:
    """
    dict.fromkeys preserves insertion order and auto-deduplicates keys.
    Very concise one-liner equivalent.
    """
    return list(dict.fromkeys(lst))


# ── Method 3: Manual nested loop (no extra data structure) ───
def remove_duplicates_manual(lst: list) -> list:
    """
    O(n²) – illustrative / for environments without sets/dicts.
    """
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


# ── Test cases ───────────────────────────────────────────────
test_lists = [
    [1, 2, 3, 2, 1, 4, 3, 5],
    ["apple", "banana", "apple", "cherry", "banana"],
    [True, 1, False, 0, True, 2],    # bool/int overlap
    [3, 3, 3, 3],
    [],
    [42],
    [1, "one", 1.0, "one", 2, 2],
]

print("=" * 65)
print(f"  {'Original List':<38}  {'Deduplicated'}")
print("─" * 65)

for lst in test_lists:
    result = remove_duplicates_set(lst)
    print(f"  {str(lst):<38}  {result}")

print("=" * 65)

# ── Compare all three methods on a common list ───────────────
sample = [5, 1, 3, 1, 5, 2, 3, 4, 2]
print(f"\n  Comparing all methods on: {sample}\n")
print(f"  Method 1 (set tracker)   : {remove_duplicates_set(sample)}")
print(f"  Method 2 (dict.fromkeys) : {remove_duplicates_dict(sample)}")
print(f"  Method 3 (manual loop)   : {remove_duplicates_manual(sample)}")

# ── Interactive ──────────────────────────────────────────────
print("\n" + "=" * 65)
raw = input("  Enter a list of items (space-separated): ").strip().split()
print(f"  Deduplicated (order preserved): {remove_duplicates_set(raw)}")
print("=" * 65)