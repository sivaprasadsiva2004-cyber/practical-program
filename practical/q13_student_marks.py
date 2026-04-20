# ============================================================
# Q13. Create a dictionary of student names and marks.
#      Find topper, average, and sort by marks.
# ============================================================

# ── Student data ──────────────────────────────────────────────
students = {
    "Alice"   : 88,
    "Bob"     : 73,
    "Charlie" : 95,
    "Diana"   : 91,
    "Eve"     : 67,
    "Frank"   : 82,
    "Grace"   : 95,
    "Hank"    : 58,
}

# ── Display original dictionary ───────────────────────────────
print("=" * 45)
print("  Student Marks Report")
print("=" * 45)
print(f"  {'Name':<12} {'Marks':>6}  {'Grade'}")
print("─" * 45)

def get_grade(marks: int) -> str:
    """Return letter grade based on marks."""
    if marks >= 90: return "A+"
    if marks >= 80: return "A"
    if marks >= 70: return "B"
    if marks >= 60: return "C"
    return "F"

for name, marks in students.items():
    print(f"  {name:<12} {marks:>6}  {get_grade(marks)}")

# ── Topper ────────────────────────────────────────────────────
highest_marks = max(students.values())
toppers = [n for n, m in students.items() if m == highest_marks]

# ── Lowest scorer ─────────────────────────────────────────────
lowest_marks = min(students.values())
lowest = [n for n, m in students.items() if m == lowest_marks]

# ── Average ───────────────────────────────────────────────────
average = sum(students.values()) / len(students)

# ── Above / below average ─────────────────────────────────────
above_avg = {n: m for n, m in students.items() if m >= average}
below_avg = {n: m for n, m in students.items() if m < average}

# ── Sort by marks (descending) ────────────────────────────────
sorted_desc = dict(sorted(students.items(), key=lambda x: x[1], reverse=True))
sorted_asc  = dict(sorted(students.items(), key=lambda x: x[1]))

print("\n" + "=" * 45)
print("  Statistics")
print("─" * 45)
print(f"  Topper        : {', '.join(toppers)} ({highest_marks})")
print(f"  Lowest Scorer : {', '.join(lowest)} ({lowest_marks})")
print(f"  Class Average : {average:.2f}")
print(f"  Total Students: {len(students)}")

print("\n  Students above average:")
for n, m in above_avg.items():
    print(f"    {n:<12} {m}")

print("\n  Students below average:")
for n, m in below_avg.items():
    print(f"    {n:<12} {m}")

print("\n  Sorted by Marks (Descending):")
rank = 1
for n, m in sorted_desc.items():
    print(f"    Rank {rank}: {n:<12} {m}  {get_grade(m)}")
    rank += 1

print("\n  Sorted by Marks (Ascending):")
for n, m in sorted_asc.items():
    print(f"    {n:<12} {m}")

print("=" * 45)