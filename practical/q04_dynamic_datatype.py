# ============================================================
# Q4. Take user input and dynamically determine
#     and convert its datatype.
# ============================================================

def detect_and_convert(value: str):
    """
    Try to convert the raw string input into the most
    appropriate Python type, in priority order:
    int → float → complex → bool-like → str.
    Returns (converted_value, detected_type_name).
    """
    # Boolean-like strings
    if value.strip().lower() in ("true", "false"):
        converted = value.strip().lower() == "true"
        return converted, "bool"

    # Integer
    try:
        converted = int(value)
        return converted, "int"
    except ValueError:
        pass

    # Float
    try:
        converted = float(value)
        return converted, "float"
    except ValueError:
        pass

    # Complex  e.g. "3+4j"
    try:
        converted = complex(value)
        return converted, "complex"
    except ValueError:
        pass

    # Default: keep as string
    return value, "str"


def show_conversions(value):
    """Display all possible explicit type conversions."""
    print(f"\n  Possible explicit conversions for: '{value}'")
    conversions = {
        "int"    : lambda v: int(float(v)),   # float first handles "3.9"
        "float"  : float,
        "str"    : str,
        "bool"   : bool,
        "complex": complex,
    }
    for type_name, converter in conversions.items():
        try:
            result = converter(value)
            print(f"    → {type_name:8s} : {result}")
        except (ValueError, TypeError):
            print(f"    → {type_name:8s} : ✗ (conversion not possible)")


# ── Main ─────────────────────────────────────────────────────
print("=" * 55)
print("   Dynamic Datatype Detection & Conversion")
print("=" * 55)

user_input = input("\n  Enter a value: ").strip()

detected_value, detected_type = detect_and_convert(user_input)

print(f"\n  Raw Input    : '{user_input}'  (type: str)")
print(f"  Detected as  : {detected_type}")
print(f"  Converted Val: {detected_value}")
print(f"  Python type(): {type(detected_value)}")

show_conversions(user_input)
print("=" * 55)