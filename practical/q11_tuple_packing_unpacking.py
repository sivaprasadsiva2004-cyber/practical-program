# ============================================================
# Q11. Demonstrate tuple packing and unpacking
#      with nested tuples.
# ============================================================

print("=" * 55)
print("  1.  TUPLE PACKING")
print("─" * 55)

# Packing – multiple values assigned to a single tuple variable
student = ("Alice", 21, "Computer Science", 9.1)
print(f"  Packed tuple: {student}")
print(f"  Type        : {type(student)}")

# ── Basic Unpacking ───────────────────────────────────────────
print("\n" + "=" * 55)
print("  2.  BASIC TUPLE UNPACKING")
print("─" * 55)

name, age, branch, cgpa = student
print(f"  name   = {name}")
print(f"  age    = {age}")
print(f"  branch = {branch}")
print(f"  cgpa   = {cgpa}")

# ── Extended Unpacking with * ─────────────────────────────────
print("\n" + "=" * 55)
print("  3.  EXTENDED UNPACKING  (using *)")
print("─" * 55)

first, *middle, last = (10, 20, 30, 40, 50)
print(f"  Tuple  : (10, 20, 30, 40, 50)")
print(f"  first  = {first}")
print(f"  middle = {middle}  ← captured as list")
print(f"  last   = {last}")

# ── Swapping with tuples ──────────────────────────────────────
print("\n" + "=" * 55)
print("  4.  SWAPPING VIA TUPLE PACKING/UNPACKING")
print("─" * 55)

x, y = 100, 200
print(f"  Before swap: x = {x}, y = {y}")
x, y = y, x          # Python creates a temporary tuple (y, x)
print(f"  After swap : x = {x}, y = {y}")

# ── Nested Tuples ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("  5.  NESTED TUPLES")
print("─" * 55)

# Address nested inside a person tuple
person = ("Bob", 25, ("Mumbai", "Maharashtra", 400001))
print(f"  person = {person}")

# Unpack all levels including the nested tuple
p_name, p_age, (city, state, pin) = person
print(f"\n  Unpacked:")
print(f"  name   = {p_name}")
print(f"  age    = {p_age}")
print(f"  city   = {city}")
print(f"  state  = {state}")
print(f"  pin    = {pin}")

# ── Deeply nested tuple ───────────────────────────────────────
print("\n" + "=" * 55)
print("  6.  DEEPLY NESTED TUPLE UNPACKING")
print("─" * 55)

matrix_row = ((1, 2), (3, 4), (5, 6))
print(f"  matrix_row = {matrix_row}")

for (a, b) in matrix_row:
    print(f"  Pair → a={a}, b={b}, sum={a+b}")

# ── Tuple as function return ──────────────────────────────────
print("\n" + "=" * 55)
print("  7.  FUNCTION RETURNING A TUPLE")
print("─" * 55)

def min_max_avg(numbers):
    """Return (minimum, maximum, average) as a packed tuple."""
    total = sum(numbers)
    return min(numbers), max(numbers), total / len(numbers)

data = [4, 7, 2, 9, 1, 5]
minimum, maximum, average = min_max_avg(data)
print(f"  Data    : {data}")
print(f"  Minimum : {minimum}")
print(f"  Maximum : {maximum}")
print(f"  Average : {average:.2f}")
print("=" * 55)