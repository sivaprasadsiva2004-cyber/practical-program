# ============================================================
# Q18. Accept command-line arguments and perform
#      arithmetic operations.
#
# Usage examples:
#   python q18_command_line_args.py 10 5
#   python q18_command_line_args.py 10 5 add
#   python q18_command_line_args.py 10 5 all
# ============================================================

import sys


def perform_operation(a: float, b: float, operation: str) -> None:
    """Dispatch to the requested arithmetic operation."""
    op = operation.lower()

    operations = {
        "add"      : ("Addition"      , lambda x, y: x + y),
        "sub"      : ("Subtraction"   , lambda x, y: x - y),
        "mul"      : ("Multiplication", lambda x, y: x * y),
        "div"      : ("Division"      , lambda x, y: x / y if y != 0
                                                     else "undefined (÷0)"),
        "floordiv" : ("Floor Division", lambda x, y: x // y if y != 0
                                                     else "undefined (÷0)"),
        "mod"      : ("Modulus"       , lambda x, y: x % y if y != 0
                                                     else "undefined (÷0)"),
        "pow"      : ("Power"         , lambda x, y: x ** y),
    }

    if op == "all":
        print(f"\n  All operations on {a} and {b}:")
        print("─" * 40)
        for key, (name, fn) in operations.items():
            result = fn(a, b)
            if isinstance(result, float):
                print(f"  {name:<18}: {result:.4f}")
            else:
                print(f"  {name:<18}: {result}")
    elif op in operations:
        name, fn = operations[op]
        result = fn(a, b)
        if isinstance(result, float):
            print(f"\n  {name}: {a} OP {b} = {result:.4f}")
        else:
            print(f"\n  {name}: {a} OP {b} = {result}")
    else:
        print(f"\n  ✗ Unknown operation '{operation}'.")
        print("  Available: add, sub, mul, div, floordiv, mod, pow, all")


def print_usage():
    print("\n  Usage:")
    print("    python q18_command_line_args.py <num1> <num2> [operation]")
    print("\n  Operations: add | sub | mul | div | floordiv | mod | pow | all")
    print("  (Default: all)\n")


# ── Main ─────────────────────────────────────────────────────
print("=" * 55)
print("  Command-Line Arithmetic")
print("=" * 55)
print(f"  sys.argv : {sys.argv}")

args = sys.argv[1:]   # exclude the script name itself

if len(args) < 2:
    print("\n  ℹ  No command-line arguments provided.")
    print("  Running in interactive mode instead.\n")
    try:
        a   = float(input("  Enter first number : "))
        b   = float(input("  Enter second number: "))
        ops = ("add", "sub", "mul", "div",
               "floordiv", "mod", "pow", "all")
        print(f"  Operations: {', '.join(ops)}")
        op  = input("  Choose operation   : ").strip() or "all"
    except ValueError:
        print("  ✗ Invalid number entered.")
        sys.exit(1)
else:
    try:
        a  = float(args[0])
        b  = float(args[1])
        op = args[2] if len(args) >= 3 else "all"
    except ValueError:
        print(f"\n  ✗ '{args[0]}' or '{args[1]}' is not a valid number.")
        print_usage()
        sys.exit(1)

perform_operation(a, b, op)
print("=" * 55)