# ============================================================
# Q21. Write recursive and iterative functions for Fibonacci
#      and compare their execution time.
# ============================================================

import time
import sys

# Increase recursion limit for large n
sys.setrecursionlimit(10000)


# ── 1. Recursive Fibonacci (naive – exponential time) ────────
def fib_recursive(n: int) -> int:
    """
    Classic recursive approach.
    Time  : O(2^n) – very slow for large n
    Space : O(n)   – call-stack depth
    """
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# ── 2. Recursive with Memoisation (top-down DP) ──────────────
_memo = {}

def fib_memo(n: int) -> int:
    """
    Recursive + memoisation.
    Time  : O(n)
    Space : O(n) for the memo cache
    """
    if n in _memo:
        return _memo[n]
    if n <= 1:
        return n
    _memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return _memo[n]


# ── 3. Iterative Fibonacci ────────────────────────────────────
def fib_iterative(n: int) -> int:
    """
    Iterative approach using two variables.
    Time  : O(n)
    Space : O(1)  ← most efficient
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# ── 4. Iterative – return full series ────────────────────────
def fib_series(n: int) -> list:
    """Return the first n Fibonacci numbers as a list."""
    if n <= 0: return []
    if n == 1: return [0]
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series


# ── Correctness check ─────────────────────────────────────────
print("=" * 60)
print("  Fibonacci – Correctness Check (first 15 terms)")
print("─" * 60)
expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
series   = fib_series(15)
print(f"  Series   : {series}")
print(f"  Expected : {expected}")
print(f"  Match    : {'✓ Yes' if series == expected else '✗ No'}")


# ── Timing comparison ─────────────────────────────────────────
def time_it(func, n: int, label: str) -> float:
    start  = time.perf_counter()
    result = func(n)
    end    = time.perf_counter()
    elapsed = (end - start) * 1000   # convert to ms
    print(f"  {label:<35} fib({n:2d}) = {result:>10}  [{elapsed:.4f} ms]")
    return elapsed


print("\n" + "=" * 60)
print("  Execution Time Comparison")
print("─" * 60)

# Small n – all three approaches
for n in [10, 20, 30]:
    print(f"\n  n = {n}:")
    t1 = time_it(fib_recursive, n, "Recursive (naive)")
    t2 = time_it(fib_memo,      n, "Recursive + Memoisation")
    t3 = time_it(fib_iterative, n, "Iterative")

# Large n – only memo and iterative (naive is too slow)
print(f"\n  n = 100  (naive skipped – too slow):")
t2 = time_it(fib_memo,      100, "Recursive + Memoisation")
t3 = time_it(fib_iterative, 100, "Iterative")

print(f"\n  n = 1000  (naive skipped – too slow):")
_memo.clear()   # reset memo for fresh timing
t2 = time_it(fib_memo,      1000, "Recursive + Memoisation")
t3 = time_it(fib_iterative, 1000, "Iterative")

print("\n" + "=" * 60)
print("  Summary")
print("─" * 60)
print("  Naive Recursive  : O(2^n) time, O(n) space – slow!")
print("  Memo Recursive   : O(n) time,   O(n) space – fast, uses memory")
print("  Iterative        : O(n) time,   O(1) space – fastest & most efficient")
print("=" * 60)