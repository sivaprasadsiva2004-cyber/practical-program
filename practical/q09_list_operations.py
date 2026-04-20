# ============================================================
# Q9. Perform all list operations:
#     insert, append, extend, remove, pop, sort, reverse.
# ============================================================

def show(label: str, lst: list):
    print(f"  {label:<35} → {lst}")


# ── Starting list ─────────────────────────────────────────────
my_list = [30, 10, 50, 20, 40]

print("=" * 60)
print("  All List Operations Demo")
print("=" * 60)
show("Initial list", my_list)

# 1. append – add element at the end
my_list.append(60)
show("After append(60)", my_list)

# 2. insert – insert at a specific index
my_list.insert(2, 99)
show("After insert(2, 99)", my_list)

# 3. extend – add multiple elements from an iterable
my_list.extend([70, 80])
show("After extend([70, 80])", my_list)

# 4. remove – remove first occurrence of a value
my_list.remove(99)
show("After remove(99)", my_list)

# 5. pop (no arg) – remove and return last element
popped = my_list.pop()
show(f"After pop() [removed {popped}]", my_list)

# 6. pop (with index) – remove and return element at index
popped_idx = my_list.pop(1)
show(f"After pop(1) [removed {popped_idx}]", my_list)

# 7. sort – sort in ascending order (in-place)
my_list.sort()
show("After sort() [ascending]", my_list)

# 8. sort with reverse=True – descending
my_list.sort(reverse=True)
show("After sort(reverse=True)", my_list)

# 9. reverse – reverse in-place
my_list.reverse()
show("After reverse()", my_list)

# 10. index – find position of first occurrence
val = 50
show(f"index({val})", [f"position = {my_list.index(val)}"])

# 11. count – count occurrences
my_list.append(10)
show(f"After append(10), count(10)", [f"{my_list.count(10)} time(s)"])
show("List now", my_list)

# 12. copy – shallow copy
copy_list = my_list.copy()
show("Shallow copy (copy())", copy_list)

# 13. clear – remove all elements
temp = [1, 2, 3]
temp.clear()
show("After clear() on [1,2,3]", temp)

# 14. List slicing
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
show("\nFruits list", fruits)
show("fruits[1:4]  (slice)", fruits[1:4])
show("fruits[::-1] (reversed copy)", fruits[::-1])
show("fruits[::2]  (every other)", fruits[::2])

print("\n" + "=" * 60)
print("  len / min / max / sum / sorted")
print("─" * 60)
nums = [5, 2, 8, 1, 9, 3]
print(f"  nums = {nums}")
print(f"  len(nums)    = {len(nums)}")
print(f"  min(nums)    = {min(nums)}")
print(f"  max(nums)    = {max(nums)}")
print(f"  sum(nums)    = {sum(nums)}")
print(f"  sorted(nums) = {sorted(nums)}   (original unchanged)")
print("=" * 60)