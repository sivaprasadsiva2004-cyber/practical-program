# ============================================================
# Q1. Demonstrate all built-in data types,
#     display their type and memory location (id).
# ============================================================

import sys

# ── Integer ──────────────────────────────────────────────────
num_int = 42
print("─" * 55)
print(f"  Integer  : {num_int}")
print(f"  Type     : {type(num_int)}")
print(f"  Memory   : {id(num_int)}")
print(f"  Size     : {sys.getsizeof(num_int)} bytes")

# ── Float ────────────────────────────────────────────────────
num_float = 3.14159
print("\n─" * 56)
print(f"  Float    : {num_float}")
print(f"  Type     : {type(num_float)}")
print(f"  Memory   : {id(num_float)}")
print(f"  Size     : {sys.getsizeof(num_float)} bytes")

# ── Complex ──────────────────────────────────────────────────
num_complex = 2 + 3j
print("\n─" * 56)
print(f"  Complex  : {num_complex}")
print(f"  Type     : {type(num_complex)}")
print(f"  Memory   : {id(num_complex)}")
print(f"  Size     : {sys.getsizeof(num_complex)} bytes")

# ── Boolean ──────────────────────────────────────────────────
flag = True
print("\n─" * 56)
print(f"  Boolean  : {flag}")
print(f"  Type     : {type(flag)}")
print(f"  Memory   : {id(flag)}")
print(f"  Size     : {sys.getsizeof(flag)} bytes")

# ── String ───────────────────────────────────────────────────
text = "Hello, Python!"
print("\n─" * 56)
print(f"  String   : {text}")
print(f"  Type     : {type(text)}")
print(f"  Memory   : {id(text)}")
print(f"  Size     : {sys.getsizeof(text)} bytes")

# ── List ─────────────────────────────────────────────────────
my_list = [1, "two", 3.0, True]
print("\n─" * 56)
print(f"  List     : {my_list}")
print(f"  Type     : {type(my_list)}")
print(f"  Memory   : {id(my_list)}")
print(f"  Size     : {sys.getsizeof(my_list)} bytes")

# ── Tuple ────────────────────────────────────────────────────
my_tuple = (10, 20, 30)
print("\n─" * 56)
print(f"  Tuple    : {my_tuple}")
print(f"  Type     : {type(my_tuple)}")
print(f"  Memory   : {id(my_tuple)}")
print(f"  Size     : {sys.getsizeof(my_tuple)} bytes")

# ── Set ──────────────────────────────────────────────────────
my_set = {1, 2, 3, 4, 5}
print("\n─" * 56)
print(f"  Set      : {my_set}")
print(f"  Type     : {type(my_set)}")
print(f"  Memory   : {id(my_set)}")
print(f"  Size     : {sys.getsizeof(my_set)} bytes")

# ── Dictionary ───────────────────────────────────────────────
my_dict = {"name": "Alice", "age": 22}
print("\n─" * 56)
print(f"  Dict     : {my_dict}")
print(f"  Type     : {type(my_dict)}")
print(f"  Memory   : {id(my_dict)}")
print(f"  Size     : {sys.getsizeof(my_dict)} bytes")

# ── NoneType ─────────────────────────────────────────────────
nothing = None
print("\n─" * 56)
print(f"  NoneType : {nothing}")
print(f"  Type     : {type(nothing)}")
print(f"  Memory   : {id(nothing)}")
print(f"  Size     : {sys.getsizeof(nothing)} bytes")
print("─" * 55)