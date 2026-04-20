# ============================================================
# Q20. Write functions to implement map(), filter(),
#      and reduce() manually.
# ============================================================

from functools import reduce as builtin_reduce   # for verification


# ── Manual map ───────────────────────────────────────────────
def my_map(func, iterable):
    """
    Apply `func` to every element of `iterable`
    and return a list of results.

    Equivalent to: list(map(func, iterable))
    """
    result = []
    for item in iterable:
        result.append(func(item))
    return result


# ── Manual filter ────────────────────────────────────────────
def my_filter(func, iterable):
    """
    Return a list containing only the elements of `iterable`
    for which `func(element)` is truthy.

    Equivalent to: list(filter(func, iterable))
    """
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result


# ── Manual reduce ────────────────────────────────────────────
def my_reduce(func, iterable, initializer=None):
    """
    Cumulatively apply `func` of two arguments (left to right)
    to reduce `iterable` to a single value.

    Equivalent to: functools.reduce(func, iterable, initializer)
    """
    it = iter(iterable)

    if initializer is None:
        try:
            accumulator = next(it)
        except StopIteration:
            raise TypeError("my_reduce() of empty sequence with no initial value")
    else:
        accumulator = initializer

    for item in it:
        accumulator = func(accumulator, item)

    return accumulator


# ── Demonstration ─────────────────────────────────────────────
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("=" * 60)
print(f"  Data: {numbers}")
print("=" * 60)

# ── MAP examples ──────────────────────────────────────────────
print("\n  ── MAP ──────────────────────────────────────────────")

squared = my_map(lambda x: x ** 2, numbers)
print(f"  Square each    : {squared}")

doubled = my_map(lambda x: x * 2, numbers)
print(f"  Double each    : {doubled}")

to_str  = my_map(str, numbers)
print(f"  Convert to str : {to_str}")

words   = ["hello", "world", "python"]
upper   = my_map(str.upper, words)
print(f"  Upper words    : {upper}")

# Verify against built-in
assert squared == list(map(lambda x: x ** 2, numbers)), "map mismatch!"
print("  ✓ Matches built-in map()")


# ── FILTER examples ───────────────────────────────────────────
print("\n  ── FILTER ───────────────────────────────────────────")

evens    = my_filter(lambda x: x % 2 == 0, numbers)
print(f"  Even numbers   : {evens}")

odds     = my_filter(lambda x: x % 2 != 0, numbers)
print(f"  Odd numbers    : {odds}")

gt_five  = my_filter(lambda x: x > 5, numbers)
print(f"  Greater than 5 : {gt_five}")

non_empty = my_filter(None, ["", "hello", 0, "world", None, 42])
print(f"  Truthy values  : {non_empty}")   # filter(None,...) keeps truthy

# Verify against built-in
assert evens == list(filter(lambda x: x % 2 == 0, numbers)), "filter mismatch!"
print("  ✓ Matches built-in filter()")


# ── REDUCE examples ───────────────────────────────────────────
print("\n  ── REDUCE ───────────────────────────────────────────")

total    = my_reduce(lambda acc, x: acc + x, numbers)
print(f"  Sum            : {total}")

product  = my_reduce(lambda acc, x: acc * x, numbers)
print(f"  Product        : {product}")

maximum  = my_reduce(lambda a, b: a if a > b else b, numbers)
print(f"  Maximum        : {maximum}")

minimum  = my_reduce(lambda a, b: a if a < b else b, numbers)
print(f"  Minimum        : {minimum}")

# Concatenate strings
sentence = my_reduce(lambda a, b: a + " " + b, ["Python", "is", "awesome"])
print(f"  Join words     : '{sentence}'")

# With initializer
with_init = my_reduce(lambda acc, x: acc + x, numbers, initializer=100)
print(f"  Sum + init 100 : {with_init}")

# Verify against built-in
assert total == builtin_reduce(lambda a, b: a + b, numbers), "reduce mismatch!"
print("  ✓ Matches functools.reduce()")


# ── Chaining map + filter + reduce ────────────────────────────
print("\n" + "=" * 60)
print("  Chained example: sum of squares of even numbers")
print("─" * 60)
evens_sq_sum = my_reduce(
    lambda a, b: a + b,
    my_map(lambda x: x ** 2,
           my_filter(lambda x: x % 2 == 0, numbers))
)
print(f"  Data         : {numbers}")
print(f"  Step 1 filter: {my_filter(lambda x: x % 2 == 0, numbers)}")
print(f"  Step 2 map   : {my_map(lambda x: x**2, my_filter(lambda x: x%2==0, numbers))}")
print(f"  Step 3 reduce: {evens_sq_sum}")
print("=" * 60)