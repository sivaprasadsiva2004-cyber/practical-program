# ============================================================
# Q14. Menu-driven program using if-elif and loops.
#      (Simple Calculator + Utilities)
# ============================================================

def add(a, b):        return a + b
def subtract(a, b):   return a - b
def multiply(a, b):   return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def power(a, b):      return a ** b
def modulus(a, b):    return a % b


def factorial(n: int) -> int:
    """Iterative factorial."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> list:
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ✗ Invalid number. Try again.")


def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  ✗ Invalid integer. Try again.")


# ── Main menu loop ────────────────────────────────────────────
def main():
    while True:
        print("\n" + "=" * 45)
        print("       MAIN MENU")
        print("─" * 45)
        print("  1. Arithmetic Calculator")
        print("  2. Factorial")
        print("  3. Prime Number Check")
        print("  4. Fibonacci Series")
        print("  5. Temperature Converter")
        print("  0. Exit")
        print("─" * 45)
        choice = input("  Enter your choice: ").strip()

        # ── 1. Calculator ────────────────────────────────────
        if choice == "1":
            print("\n  --- Calculator ---")
            a = get_number("  Enter first number : ")
            b = get_number("  Enter second number: ")
            print("\n  Operations:")
            print("   a. Add       b. Subtract")
            print("   c. Multiply  d. Divide")
            print("   e. Power     f. Modulus")
            op = input("  Choose (a-f): ").strip().lower()

            try:
                if   op == "a": print(f"\n  Result: {add(a, b)}")
                elif op == "b": print(f"\n  Result: {subtract(a, b)}")
                elif op == "c": print(f"\n  Result: {multiply(a, b)}")
                elif op == "d": print(f"\n  Result: {divide(a, b):.4f}")
                elif op == "e": print(f"\n  Result: {power(a, b)}")
                elif op == "f": print(f"\n  Result: {modulus(a, b)}")
                else:           print("  ✗ Invalid operation.")
            except (ZeroDivisionError, ValueError) as e:
                print(f"  ✗ Error: {e}")

        # ── 2. Factorial ──────────────────────────────────────
        elif choice == "2":
            n = get_int("\n  Enter a non-negative integer: ")
            try:
                print(f"\n  {n}! = {factorial(n)}")
            except ValueError as e:
                print(f"  ✗ {e}")

        # ── 3. Prime check ────────────────────────────────────
        elif choice == "3":
            n = get_int("\n  Enter an integer: ")
            result = "PRIME ✓" if is_prime(n) else "NOT prime ✗"
            print(f"\n  {n} is {result}")

        # ── 4. Fibonacci ──────────────────────────────────────
        elif choice == "4":
            n = get_int("\n  How many Fibonacci terms? ")
            seq = fibonacci(n)
            print(f"\n  Fibonacci ({n} terms): {seq}")

        # ── 5. Temperature converter ──────────────────────────
        elif choice == "5":
            print("\n  Conversions:")
            print("  a. Celsius → Fahrenheit")
            print("  b. Fahrenheit → Celsius")
            print("  c. Celsius → Kelvin")
            sub = input("  Choose (a-c): ").strip().lower()
            temp = get_number("  Enter temperature: ")

            if   sub == "a":
                print(f"\n  {temp}°C = {temp * 9/5 + 32:.2f}°F")
            elif sub == "b":
                print(f"\n  {temp}°F = {(temp - 32) * 5/9:.2f}°C")
            elif sub == "c":
                print(f"\n  {temp}°C = {temp + 273.15:.2f} K")
            else:
                print("  ✗ Invalid choice.")

        # ── 0. Exit ───────────────────────────────────────────
        elif choice == "0":
            print("\n  Goodbye! 👋")
            break

        else:
            print("\n  ✗ Invalid choice. Please enter 0–5.")


if __name__ == "__main__":
    main()