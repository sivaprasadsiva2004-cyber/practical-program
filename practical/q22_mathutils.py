# ============================================================
# q22_mathutils.py  –  Reusable module
#
# Contains:
#   factorial(n)   – iterative factorial
#   is_prime(n)    – primality test
#   prime_factors(n) – prime factorisation
#   primes_upto(n) – Sieve of Eratosthenes
#
# This file acts as the MODULE.
# Run it directly to see a self-test demo.
# Import it from other scripts:
#   from q22_mathutils import factorial, is_prime
# ============================================================


def factorial(n: int) -> int:
    """
    Return n! (n factorial) iteratively.
    Raises ValueError for negative n.
    """
    if not isinstance(n, int):
        raise TypeError(f"factorial requires int, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"factorial not defined for negative numbers ({n})")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """
    Return True if n is a prime number, False otherwise.
    Uses trial division up to √n – O(√n) time.
    """
    if not isinstance(n, int):
        raise TypeError(f"is_prime requires int, got {type(n).__name__}")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def prime_factors(n: int) -> list:
    """
    Return the prime factorisation of n as a list.
    Example: prime_factors(36) → [2, 2, 3, 3]
    """
    if n < 2:
        return []
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def primes_upto(limit: int) -> list:
    """
    Return all primes up to (and including) `limit`
    using the Sieve of Eratosthenes.
    """
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i, flag in enumerate(sieve) if flag]


# ── Self-test / demo when run directly ───────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  q22_mathutils  –  Module Self-Test")
    print("=" * 55)

    # Factorial
    print("\n  factorial(n):")
    for n in [0, 1, 5, 10, 15, 20]:
        print(f"    {n:2d}! = {factorial(n)}")

    # is_prime
    print("\n  is_prime(n):")
    test_nums = [0, 1, 2, 3, 4, 17, 18, 97, 100, 101]
    for n in test_nums:
        mark = "✓ prime" if is_prime(n) else "✗ not prime"
        print(f"    {n:4d}  →  {mark}")

    # prime_factors
    print("\n  prime_factors(n):")
    for n in [1, 12, 36, 100, 97, 360]:
        print(f"    {n:4d}  →  {prime_factors(n)}")

    # primes_upto
    print("\n  primes_upto(50):")
    print(f"    {primes_upto(50)}")

    print("\n" + "=" * 55)
    print("  Importing this module from another script:")
    print("    from q22_mathutils import factorial, is_prime")
    print("=" * 55)