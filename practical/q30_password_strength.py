# ============================================================
# Q30. Write a regex program to check password strength.
#
# Strength criteria:
#   WEAK   – fails multiple rules
#   FAIR   – meets 3 out of 5 rules
#   STRONG – meets 4 out of 5 rules
#   VERY STRONG – meets all 5 rules
# ============================================================

import re
from getpass import getpass   # hides input (optional)


# ── Individual regex checks ───────────────────────────────────
RULES = [
    {
        "id"     : 1,
        "label"  : "Minimum 8 characters",
        "pattern": re.compile(r".{8,}"),
        "tip"    : "Use at least 8 characters.",
    },
    {
        "id"     : 2,
        "label"  : "At least one UPPERCASE letter (A-Z)",
        "pattern": re.compile(r"[A-Z]"),
        "tip"    : "Add at least one uppercase letter.",
    },
    {
        "id"     : 3,
        "label"  : "At least one lowercase letter (a-z)",
        "pattern": re.compile(r"[a-z]"),
        "tip"    : "Add at least one lowercase letter.",
    },
    {
        "id"     : 4,
        "label"  : "At least one digit (0-9)",
        "pattern": re.compile(r"\d"),
        "tip"    : "Add at least one number.",
    },
    {
        "id"     : 5,
        "label"  : "At least one special character (!@#$%^&*...)",
        "pattern": re.compile(r"[!@#$%^&*()\-_=+\[\]{};:'\",.<>?/\\|`~]"),
        "tip"    : "Add a special character like @, #, $, etc.",
    },
]

# Bonus rules
EXTRA_RULES = [
    {
        "label"  : "No repeated characters (aaa, 111)",
        "pattern": re.compile(r"(.)\1{2,}"),   # match = bad
        "inverted": True,
        "tip"    : "Avoid repeating the same character 3+ times.",
    },
    {
        "label"  : "No common sequences (123, abc, qwerty)",
        "pattern": re.compile(
            r"(012|123|234|345|456|567|678|789|890"
            r"|abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno"
            r"|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz"
            r"|qwerty|asdf|zxcv|password|admin|login)",
            re.IGNORECASE
        ),
        "inverted": True,
        "tip"    : "Avoid keyboard sequences like '123' or 'qwerty'.",
    },
]


def evaluate_password(password: str) -> dict:
    """
    Evaluate a password against all rules.
    Returns a report dictionary with pass/fail per rule,
    overall score, and strength label.
    """
    results   = []
    score     = 0
    tips      = []

    for rule in RULES:
        passed = bool(rule["pattern"].search(password))
        if passed:
            score += 1
        else:
            tips.append(rule["tip"])
        results.append({"label": rule["label"], "passed": passed})

    # Extra checks
    extra_results = []
    for rule in EXTRA_RULES:
        match   = bool(rule["pattern"].search(password))
        passed  = not match   # inverted: match means FAIL
        extra_results.append({"label": rule["label"], "passed": passed})
        if not passed:
            tips.append(rule["tip"])

    # Strength label
    if score == 5:
        strength = "VERY STRONG 🔒"
        color    = "✅"
    elif score == 4:
        strength = "STRONG"
        color    = "🟢"
    elif score == 3:
        strength = "FAIR"
        color    = "🟡"
    else:
        strength = "WEAK"
        color    = "🔴"

    return {
        "password"     : password,
        "score"        : score,
        "max_score"    : len(RULES),
        "strength"     : strength,
        "icon"         : color,
        "rule_results" : results,
        "extra_results": extra_results,
        "tips"         : tips,
    }


def display_report(report: dict):
    """Print a formatted password strength report."""
    print("\n" + "=" * 55)
    print("  Password Strength Report")
    print("─" * 55)
    hidden = "*" * len(report["password"])
    print(f"  Password : {hidden}  ({len(report['password'])} chars)")
    print(f"  Score    : {report['score']} / {report['max_score']}")
    print(f"  Strength : {report['icon']}  {report['strength']}")
    print("─" * 55)
    print("  Core Rules:")
    for r in report["rule_results"]:
        mark = "  ✓" if r["passed"] else "  ✗"
        print(f"  {mark}  {r['label']}")
    print("\n  Extra Rules:")
    for r in report["extra_results"]:
        mark = "  ✓" if r["passed"] else "  ✗"
        print(f"  {mark}  {r['label']}")
    if report["tips"]:
        print("\n  Suggestions:")
        for tip in report["tips"]:
            print(f"    → {tip}")
    print("=" * 55)


# ── Test passwords ────────────────────────────────────────────
test_passwords = [
    "abc",
    "password",
    "Password1",
    "P@ssw0rd",
    "Tr0ub4dor&3",
    "MyS3cur3P@ss!",
    "aaaaaaaA1!",
    "qwerty123",
]

print("=" * 55)
print("  Password Strength Checker – Batch Test")
print("─" * 55)
print(f"  {'Password':<20} {'Score':<8} {'Strength'}")
print("─" * 55)
for pwd in test_passwords:
    r = evaluate_password(pwd)
    print(f"  {pwd:<20} {r['score']}/{r['max_score']}    {r['icon']} {r['strength']}")

# ── Interactive check ─────────────────────────────────────────
print("\n" + "=" * 55)
print("  Check your own password")
print("─" * 55)
try:
    pwd = getpass("  Enter password (hidden): ")
except Exception:
    pwd = input("  Enter password: ")

report = evaluate_password(pwd)
display_report(report)