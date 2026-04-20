# ============================================================
# Q10. Find second largest and second smallest elements
#      in a list WITHOUT using built-in functions
#      (no min(), max(), sort(), sorted()).
# ============================================================

def find_second_largest(lst: list):
    """
    Single-pass O(n) approach.
    Tracks the largest and second-largest seen so far.
    Returns None if the list has fewer than 2 distinct values.
    """
    if len(lst) < 2:
        return None

    largest        = lst[0]
    second_largest = None

    for num in lst[1:]:
        if num > largest:
            second_largest = largest
            largest        = num
        elif num != largest:
            if second_largest is None or num > second_largest:
                second_largest = num

    return second_largest


def find_second_smallest(lst: list):
    """
    Single-pass O(n) approach.
    Tracks the smallest and second-smallest seen so far.
    """
    if len(lst) < 2:
        return None

    smallest        = lst[0]
    second_smallest = None

    for num in lst[1:]:
        if num < smallest:
            second_smallest = smallest
            smallest        = num
        elif num != smallest:
            if second_smallest is None or num < second_smallest:
                second_smallest = num

    return second_smallest


# ── Test cases ───────────────────────────────────────────────
test_lists = [
    [12, 35, 1, 10, 34, 1],
    [10, 5, 10],
    [100],
    [7, 7, 7],
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
    [-5, -1, -3, -2, -4],
    [42, 17],
]

print("=" * 60)
print(f"  {'List':<38} {'2nd Min':>8} {'2nd Max':>8}")
print("─" * 60)

for lst in test_lists:
    sl  = find_second_largest(lst)
    ss  = find_second_smallest(lst)
    sl_str = str(sl) if sl is not None else "N/A"
    ss_str = str(ss) if ss is not None else "N/A"
    print(f"  {str(lst):<38} {ss_str:>8} {sl_str:>8}")

print("=" * 60)

# ── Interactive ──────────────────────────────────────────────
print("\n  Enter your own list (space-separated integers):")
try:
    user_input = input("  → ").strip().split()
    user_list  = [int(x) for x in user_input]
    print(f"\n  List           : {user_list}")
    print(f"  Second Smallest: {find_second_smallest(user_list)}")
    print(f"  Second Largest : {find_second_largest(user_list)}")
except ValueError:
    print("  ✗ Invalid input. Please enter integers only.")
print("=" * 60)