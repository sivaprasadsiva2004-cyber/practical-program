# ============================================================
# Q2. Illustrate mutable and immutable objects with examples.
# ============================================================

print("=" * 55)
print("        IMMUTABLE OBJECTS")
print("=" * 55)

# ── Integer (immutable) ──────────────────────────────────────
a = 10
print(f"\n[Integer]")
print(f"  a = {a},  id(a) = {id(a)}")
a = 20                      # rebinding creates a new object
print(f"  After a = 20  → id(a) = {id(a)}  (new object!)")

# ── String (immutable) ───────────────────────────────────────
s = "hello"
print(f"\n[String]")
print(f"  s = '{s}',  id(s) = {id(s)}")
s = s + " world"            # creates a brand-new string
print(f"  After s += ' world' → s = '{s}'")
print(f"  id(s) = {id(s)}  (new object!)")

# ── Tuple (immutable) ────────────────────────────────────────
t = (1, 2, 3)
print(f"\n[Tuple]")
print(f"  t = {t},  id(t) = {id(t)}")
try:
    t[0] = 99               # this will raise TypeError
except TypeError as e:
    print(f"  Trying t[0] = 99  →  Error: {e}")

print("\n" + "=" * 55)
print("        MUTABLE OBJECTS")
print("=" * 55)

# ── List (mutable) ───────────────────────────────────────────
lst = [1, 2, 3]
print(f"\n[List]")
print(f"  lst = {lst},  id(lst) = {id(lst)}")
lst.append(4)               # modifies the same object in place
print(f"  After lst.append(4) → lst = {lst}")
print(f"  id(lst) = {id(lst)}  (SAME object!)")

# ── Dictionary (mutable) ─────────────────────────────────────
d = {"x": 1, "y": 2}
print(f"\n[Dictionary]")
print(f"  d = {d},  id(d) = {id(d)}")
d["z"] = 3
print(f"  After d['z'] = 3 → d = {d}")
print(f"  id(d) = {id(d)}  (SAME object!)")

# ── Set (mutable) ────────────────────────────────────────────
st = {10, 20, 30}
print(f"\n[Set]")
print(f"  st = {st},  id(st) = {id(st)}")
st.add(40)
print(f"  After st.add(40) → st = {st}")
print(f"  id(st) = {id(st)}  (SAME object!)")

print("\n" + "=" * 55)
print("  Summary: Immutable → new object on change")
print("           Mutable   → same object, value changes")
print("=" * 55)