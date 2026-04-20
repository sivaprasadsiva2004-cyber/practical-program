# ============================================================
# Q27. Retrieve and display records from a MySQL table.
#
# Run AFTER q26_mysql_create_insert.py has populated the DB.
# Update DB_CONFIG with your MySQL credentials.
# ============================================================

import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host"    : "localhost",
    "user"    : "root",
    "password": "your_password",   # ← change this
    "database": "college_db",
}


def fetch_all(cur) -> tuple:
    """Return (rows, column_names) from the last executed query."""
    return cur.fetchall(), [d[0] for d in cur.description]


def print_table(rows: list, columns: list, title: str = ""):
    """Pretty-print query results as a formatted table."""
    if title:
        print(f"\n  {title}")

    widths = [max(len(str(col)),
                  max((len(str(row[i])) for row in rows), default=0))
              for i, col in enumerate(columns)]

    sep    = "  +" + "+".join("-" * (w + 2) for w in widths) + "+"
    header = "  |" + "|".join(f" {col:<{widths[i]}} " for i, col in enumerate(columns)) + "|"

    print(sep)
    print(header)
    print(sep)
    for row in rows:
        line = "  |" + "|".join(f" {str(v):<{widths[i]}} " for i, v in enumerate(row)) + "|"
        print(line)
    print(sep)
    print(f"  {len(rows)} row(s)\n")


# ── Main ─────────────────────────────────────────────────────
print("=" * 65)
print("  Q27 – MySQL: Retrieve & Display Records")
print("=" * 65)

try:
    conn = mysql.connector.connect(**DB_CONFIG)
    cur  = conn.cursor()

    # 1. Fetch ALL records
    cur.execute("SELECT * FROM students")
    rows, cols = fetch_all(cur)
    print_table(rows, cols, "All Students")

    # 2. Fetch records with condition – CGPA > 8.5
    cur.execute("SELECT name, branch, cgpa FROM students WHERE cgpa > 8.5")
    rows, cols = fetch_all(cur)
    print_table(rows, cols, "Students with CGPA > 8.5")

    # 3. Fetch sorted by CGPA descending
    cur.execute("SELECT name, cgpa FROM students ORDER BY cgpa DESC")
    rows, cols = fetch_all(cur)
    print_table(rows, cols, "Sorted by CGPA (Descending)")

    # 4. Aggregate queries
    cur.execute("""
        SELECT
            COUNT(*)            AS total_students,
            ROUND(AVG(cgpa),2)  AS avg_cgpa,
            MAX(cgpa)           AS highest_cgpa,
            MIN(cgpa)           AS lowest_cgpa
        FROM students
    """)
    rows, cols = fetch_all(cur)
    print_table(rows, cols, "Aggregate Statistics")

    # 5. Group by branch
    cur.execute("""
        SELECT branch,
               COUNT(*)           AS count,
               ROUND(AVG(cgpa),2) AS avg_cgpa
        FROM students
        GROUP BY branch
        ORDER BY avg_cgpa DESC
    """)
    rows, cols = fetch_all(cur)
    print_table(rows, cols, "Branch-wise Summary")

    # 6. fetchone and fetchmany examples
    print("  fetchone() example:")
    cur.execute("SELECT * FROM students LIMIT 1")
    row = cur.fetchone()
    print(f"  First row: {row}\n")

    print("  fetchmany(3) example:")
    cur.execute("SELECT name, cgpa FROM students")
    chunk = cur.fetchmany(3)
    for r in chunk:
        print(f"    {r}")

except Error as e:
    print(f"\n  ✗ MySQL Error: {e}")
    print("  Ensure q26_mysql_create_insert.py has been run first.")

finally:
    if 'conn' in dir() and conn.is_connected():
        cur.close()
        conn.close()
        print("\n  ✓ Connection closed.")

print("=" * 65)