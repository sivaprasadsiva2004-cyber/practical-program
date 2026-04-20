# ============================================================
# Q19. Demonstrate the use of iterators in Python.
#      An iterator is an object implementing __iter__() and __next__().
# ============================================================


# ── 1. Built-in iterators ─────────────────────────────────────
print("=" * 55)
print("  1. Built-in Iterator (iter() + next())")
print("─" * 55)

my_list = [10, 20, 30, 40, 50]
it = iter(my_list)          # get iterator object from list

print(f"  List          : {my_list}")
print(f"  Iterator type : {type(it)}")
print(f"  next(it) calls:")
for _ in range(len(my_list)):
    print(f"    → {next(it)}")

# StopIteration when exhausted
try:
    next(it)
except StopIteration:
    print("  ✓ StopIteration raised – iterator exhausted")


# ── 2. Iterating over different iterables ─────────────────────
print("\n" + "=" * 55)
print("  2. Iterating Different Iterables")
print("─" * 55)

for item in iter("Python"):        # string iterator
    print(f"  char → {item}")

print()
for k, v in iter({"a": 1, "b": 2}.items()):   # dict iterator
    print(f"  key={k}, val={v}")


# ── 3. Custom Iterator class ──────────────────────────────────
print("\n" + "=" * 55)
print("  3. Custom Iterator – CountDown")
print("─" * 55)

class CountDown:
    """
    Custom iterator that counts down from `start` to 1.
    Implements __iter__ and __next__ dunder methods.
    """
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Return the next value or raise StopIteration."""
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


countdown = CountDown(7)
print("  Countdown from 7:")
for num in countdown:
    print(f"    {num}", end="  ")
print()


# ── 4. Custom Iterator – Fibonacci ───────────────────────────
print("\n" + "=" * 55)
print("  4. Custom Iterator – Fibonacci (first 10 terms)")
print("─" * 55)

class FibonacciIterator:
    """Yields Fibonacci numbers up to `limit` terms."""
    def __init__(self, limit: int):
        self.limit = limit
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        value    = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return value


fibs = list(FibonacciIterator(10))
print(f"  First 10 Fibonacci: {fibs}")


# ── 5. Infinite iterator with manual break ────────────────────
print("\n" + "=" * 55)
print("  5. Infinite Iterator – EvenNumbers (stopped at 20)")
print("─" * 55)

class EvenNumbers:
    """Infinite iterator yielding even numbers starting from 0."""
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        val = self.num
        self.num += 2
        return val


evens = EvenNumbers()
result = []
for e in evens:
    if e > 20:
        break
    result.append(e)
print(f"  Even numbers ≤ 20: {result}")


# ── 6. Using itertools ────────────────────────────────────────
import itertools

print("\n" + "=" * 55)
print("  6. itertools examples")
print("─" * 55)

# islice – take first n items from any iterable/iterator
squares = (x ** 2 for x in itertools.count(1))   # infinite generator
print(f"  First 8 perfect squares : {list(itertools.islice(squares, 8))}")

# cycle – repeat a sequence endlessly
colors = itertools.cycle(["Red", "Green", "Blue"])
print(f"  cycle 7 items           : {[next(colors) for _ in range(7)]}")

# chain – concatenate iterables
chained = list(itertools.chain([1, 2], [3, 4], [5]))
print(f"  chain([1,2],[3,4],[5])  : {chained}")

print("=" * 55)