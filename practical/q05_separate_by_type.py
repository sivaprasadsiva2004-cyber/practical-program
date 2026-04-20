# ============================================================
# Q5. Given a mixed list, separate elements
#     based on their datatype.
# ============================================================

# Sample mixed list with various types
mixed_list = [
    42, 3.14, "hello", True, None, 2 + 3j,
    "world", 100, 0.001, False, [1, 2], {"key": "val"},
    (7, 8), {9, 10}, "Python", 999
]

# ── Separate elements into type-keyed buckets ────────────────
buckets = {}

for element in mixed_list:
    # Use the class name as the bucket key
    type_name = type(element).__name__
    buckets.setdefault(type_name, []).append(element)

# ── Display results ──────────────────────────────────────────
print("=" * 55)
print("  Original Mixed List:")
print(f"  {mixed_list}")
print("=" * 55)
print("\n  Elements separated by datatype:\n")

for type_name, items in buckets.items():
    print(f"  {type_name:10s} ({len(items)} item{'s' if len(items)>1 else ''}):")
    for item in items:
        print(f"    • {repr(item)}")
    print()

# ── Summary statistics ────────────────────────────────────────
print("=" * 55)
print("  Summary")
print("─" * 55)
print(f"  Total elements  : {len(mixed_list)}")
print(f"  Distinct types  : {len(buckets)}")
for t, items in buckets.items():
    print(f"    {t:10s} → {len(items)} element(s)")
print("=" * 55)