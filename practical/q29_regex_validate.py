# ============================================================
# Q29. Use regular expressions to validate
#      email address and phone number.
# ============================================================

import re


# ── Email validation ─────────────────────────────────────────
EMAIL_PATTERN = re.compile(
    r"""
    ^                       # start of string
    [a-zA-Z0-9]             # first char: letter or digit
    [a-zA-Z0-9._%+\-]*      # local part: letters, digits, . _ % + -
    @                       # literal @
    [a-zA-Z0-9]             # domain first char
    [a-zA-Z0-9\-]*          # domain chars (no consecutive dots)
    (?:\.[a-zA-Z0-9\-]+)*   # optional subdomains
    \.[a-zA-Z]{2,}          # TLD – at least 2 alpha chars
    $                       # end of string
    """,
    re.VERBOSE,
)

def validate_email(email: str) -> bool:
    """Return True if `email` is a valid email address."""
    return bool(EMAIL_PATTERN.match(email.strip()))


# ── Phone number validation ───────────────────────────────────
# Patterns accepted:
#   Indian mobile  : 9876543210  /  +919876543210  /  09876543210
#   US format      : (212) 555-0100  /  212-555-0100  /  2125550100
#   International  : +44 20 1234 5678

PHONE_PATTERN = re.compile(
    r"""
    ^
    (?:
        # Indian mobile: optional +91 or 0, then 10 digits starting with 6-9
        (?:\+91|0)?[6-9]\d{9}
        |
        # US: optional (xxx) or xxx-, then xxx-xxxx
        (?:\(\d{3}\)[\s\-]?|\d{3}[\s\-]?)\d{3}[\s\-]?\d{4}
        |
        # Generic international: +[1-3 digit country code] [6-14 digits / spaces]
        \+\d{1,3}[\s\-]?\d[\d\s\-]{6,14}\d
    )
    $
    """,
    re.VERBOSE,
)

def validate_phone(phone: str) -> bool:
    """Return True if `phone` matches a supported phone format."""
    # Strip common separators for length check but validate original pattern
    return bool(PHONE_PATTERN.match(phone.strip()))


# ── Extract emails and phones from a bulk text ────────────────
def extract_emails(text: str) -> list:
    """Extract all email addresses from raw text."""
    pattern = r'[a-zA-Z0-9][a-zA-Z0-9._%+\-]*@[a-zA-Z0-9\-]+(?:\.[a-zA-Z0-9\-]+)*\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

def extract_phones(text: str) -> list:
    """Extract phone-like patterns from raw text."""
    pattern = r'(?:\+\d{1,3}[\s\-]?)?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4}'
    return re.findall(pattern, text)


# ── Test data ─────────────────────────────────────────────────
test_emails = [
    ("alice@example.com",          True),
    ("user.name+tag@domain.co.in", True),
    ("user_123@sub.domain.org",    True),
    ("admin@company.io",           True),
    ("@nodomain.com",              False),
    ("missing_at_sign.com",        False),
    ("double@@at.com",             False),
    ("no_tld@domain",              False),
    ("spaces in@email.com",        False),
    ("trailing.dot.@test.com",     False),
]

test_phones = [
    ("9876543210",       True),   # Indian mobile
    ("+919876543210",    True),   # Indian with country code
    ("09876543210",      True),   # Indian with leading 0
    ("(212) 555-0100",   True),   # US format
    ("212-555-0100",     True),   # US format
    ("+44 20 1234 5678", True),   # UK
    ("1234",             False),  # too short
    ("abcdefghij",       False),  # not digits
    ("123-456-789",      False),  # wrong format
    ("0000000000",       False),  # Indian: must start 6-9
]

# ── Display results ───────────────────────────────────────────
print("=" * 60)
print("  EMAIL VALIDATION")
print(f"  {'Email':<38} {'Expected':<10} {'Result':<10} {'Status'}")
print("─" * 60)
all_pass = True
for email, expected in test_emails:
    result = validate_email(email)
    status = "✓ PASS" if result == expected else "✗ FAIL"
    if result != expected: all_pass = False
    print(f"  {email:<38} {str(expected):<10} {str(result):<10} {status}")
print(f"\n  All tests passed: {'✓ Yes' if all_pass else '✗ No'}")

print("\n" + "=" * 60)
print("  PHONE VALIDATION")
print(f"  {'Phone':<25} {'Expected':<10} {'Result':<10} {'Status'}")
print("─" * 60)
all_pass = True
for phone, expected in test_phones:
    result = validate_phone(phone)
    status = "✓ PASS" if result == expected else "✗ FAIL"
    if result != expected: all_pass = False
    print(f"  {phone:<25} {str(expected):<10} {str(result):<10} {status}")
print(f"\n  All tests passed: {'✓ Yes' if all_pass else '✗ No'}")

# ── Extraction demo ───────────────────────────────────────────
print("\n" + "=" * 60)
print("  EXTRACT FROM BULK TEXT")
print("─" * 60)
sample_text = """
Contact our team:
  Sales  : sales@company.com    Phone: 9876543210
  Support: help@support.org     Phone: (212) 555-0100
  Info   : info@example.co.in   Phone: +919812345678
Invalid ones: @@bad.com  123-abc  missing@
"""
print(f"  Emails found : {extract_emails(sample_text)}")
print(f"  Phones found : {extract_phones(sample_text)}")

# ── Interactive ──────────────────────────────────────────────
print("\n" + "=" * 60)
e = input("  Enter an email to validate : ").strip()
p = input("  Enter a phone to validate  : ").strip()
print(f"\n  Email '{e}' → {'✓ Valid' if validate_email(e) else '✗ Invalid'}")
print(f"  Phone '{p}' → {'✓ Valid' if validate_phone(p) else '✗ Invalid'}")
print("=" * 60)