# ============================================================
# Q3. Demonstrate all operators:
#     arithmetic, relational, logical, bitwise, assignment.
# ============================================================

a, b = 15, 4

print("=" * 50)
print("  ARITHMETIC OPERATORS  (a=15, b=4)")
print("=" * 50)
print(f"  a + b  = {a + b}   (Addition)")
print(f"  a - b  = {a - b}   (Subtraction)")
print(f"  a * b  = {a * b}   (Multiplication)")
print(f"  a / b  = {a / b}  (Division - float)")
print(f"  a // b = {a // b}   (Floor Division)")
print(f"  a % b  = {a % b}    (Modulus)")
print(f"  a ** b = {a ** b} (Exponentiation)")

print("\n" + "=" * 50)
print("  RELATIONAL (COMPARISON) OPERATORS")
print("=" * 50)
print(f"  a == b  → {a == b}")
print(f"  a != b  → {a != b}")
print(f"  a >  b  → {a > b}")
print(f"  a <  b  → {a < b}")
print(f"  a >= b  → {a >= b}")
print(f"  a <= b  → {a <= b}")

print("\n" + "=" * 50)
print("  LOGICAL OPERATORS  (True, False)")
print("=" * 50)
x, y = True, False
print(f"  x = {x},  y = {y}")
print(f"  x and y → {x and y}")
print(f"  x or  y → {x or y}")
print(f"  not x   → {not x}")

print("\n" + "=" * 50)
print("  BITWISE OPERATORS  (a=15, b=4)")
print("=" * 50)
print(f"  a & b  = {a & b}   (AND)   15={bin(a)}, 4={bin(b)}")
print(f"  a | b  = {a | b}  (OR)")
print(f"  a ^ b  = {a ^ b}  (XOR)")
print(f"  ~a     = {~a}  (NOT / complement)")
print(f"  a << 1 = {a << 1}  (Left Shift)")
print(f"  a >> 1 = {a >> 1}   (Right Shift)")

print("\n" + "=" * 50)
print("  ASSIGNMENT OPERATORS")
print("=" * 50)
n = 10
print(f"  n = 10  → n = {n}")
n += 5;  print(f"  n += 5  → n = {n}")
n -= 3;  print(f"  n -= 3  → n = {n}")
n *= 2;  print(f"  n *= 2  → n = {n}")
n //= 4; print(f"  n //= 4 → n = {n}")
n **= 3; print(f"  n **= 3 → n = {n}")
n %= 5;  print(f"  n %= 5  → n = {n}")
n &= 3;  print(f"  n &= 3  → n = {n}")
n |= 8;  print(f"  n |= 8  → n = {n}")
n ^= 2;  print(f"  n ^= 2  → n = {n}")

print("\n" + "=" * 50)
print("  IDENTITY & MEMBERSHIP OPERATORS")
print("=" * 50)
lst = [1, 2, 3]
print(f"  1 in  [1,2,3]  → {1 in lst}")
print(f"  9 not in [1,2,3] → {9 not in lst}")
p = q = [1, 2, 3]
r = [1, 2, 3]
print(f"  p is q  → {p is q}  (same object)")
print(f"  p is r  → {p is r}  (different object)")
print("=" * 50)