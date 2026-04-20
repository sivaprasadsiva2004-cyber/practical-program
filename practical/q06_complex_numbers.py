# ============================================================
# Q6. Perform arithmetic operations on complex numbers.
# ============================================================

import cmath

def display_complex(label, value):
    """Pretty-print a complex number with its magnitude and phase."""
    mag   = abs(value)
    phase = cmath.phase(value)
    print(f"  {label:25s} = {value}")
    print(f"  {'':25s}   |z| = {mag:.4f},  phase = {phase:.4f} rad")

# ── Define two complex numbers ───────────────────────────────
z1 = complex(4, 3)   # 4 + 3j
z2 = complex(1, -2)  # 1 - 2j

print("=" * 55)
print("  Complex Number Arithmetic")
print("=" * 55)
display_complex("z1", z1)
print()
display_complex("z2", z2)
print("─" * 55)

# Arithmetic operations
print()
display_complex("Addition      z1 + z2", z1 + z2)
print()
display_complex("Subtraction   z1 - z2", z1 - z2)
print()
display_complex("Multiplication z1 * z2", z1 * z2)
print()
display_complex("Division      z1 / z2", z1 / z2)

print("─" * 55)
print("\n  Additional complex properties / functions:\n")
print(f"  z1.real          = {z1.real}")
print(f"  z1.imag          = {z1.imag}")
print(f"  z1.conjugate()   = {z1.conjugate()}")
print(f"  abs(z1)          = {abs(z1):.4f}  (magnitude)")
print(f"  cmath.sqrt(z1)   = {cmath.sqrt(z1):.4f}")
print(f"  cmath.exp(z1)    = {cmath.exp(z1):.4f}")
print(f"  cmath.log(z1)    = {cmath.log(z1):.4f}")
print(f"  cmath.polar(z1)  = {cmath.polar(z1)}")   # (r, θ)
r, theta = cmath.polar(z1)
print(f"  cmath.rect(r,θ)  = {cmath.rect(r, theta):.4f}")  # back to rectangular
print("=" * 55)