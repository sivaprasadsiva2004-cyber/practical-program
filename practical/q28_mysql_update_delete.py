# ============================================================
# Q28. Update and delete records in a MySQL table.
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


def show_table(cur, title: str = "Current table state"):
    """Fetch and display the students table."""
    cur.execute("SELECT id, name, age, branch, cgpa FROM students")
    rows = cur.fetchall()
    print(f"\n  ── {title} ──")
    print(f"  {'ID':<4} {'Name':<12} {'Age':<5} {'Branch':<22} {'CGPA'}")
    print("  " + "-" * 55)
    for r in rows:
        print(f"  {r[0]:<4} {r[1]:<12} {r[2]:<5} {r[3]:<22} {r[4]}")
    print(f"  ({len(rows)} rows)\n")


# ── Main ─────────────────────────────────────────────────────
print("=" * 65)
print("  Q28 – MySQL: Update & Delete Records")
print("=" * 65)

try:
    conn = mysql.connector.connect(**DB_CONFIG)
    cur  = conn.cursor()

    show_table(cur, "BEFORE any changes")

    # ── UPDATE: single row by name ────────────────────────────
    print("  1. UPDATE – Set Bob's CGPA to 8.2")
    cur.execute("UPDATE students SET cgpa = 8.2 WHERE name = 'Bob'")
    conn.commit()
    print(f"     Rows affected: {cur.rowcount}")

    # ── UPDATE: multiple rows (bulk) ──────────────────────────
    print("\n  2. UPDATE – Increment age by 1 for CS branch")
    cur.execute("""
        UPDATE students
        SET age = age + 1
        WHERE branch = 'Computer Science'
    """)
    conn.commit()
    print(f"     Rows affected: {cur.rowcount}")

    # ── UPDATE with parameterised query (safe, avoids SQL injection) ──
    print("\n  3. UPDATE – Change Alice's branch (parameterised)")
    cur.execute(
        "UPDATE students SET branch = %s WHERE name = %s",
        ("Artificial Intelligence", "Alice")
    )
    conn.commit()
    print(f"     Rows affected: {cur.rowcount}")

    show_table(cur, "AFTER UPDATES")

    # ── DELETE: single row ────────────────────────────────────
    print("  4. DELETE – Remove student named 'Eve'")
    cur.execute("DELETE FROM students WHERE name = 'Eve'")
    conn.commit()
    print(f"     Rows deleted: {cur.rowcount}")

    # ── DELETE with condition ─────────────────────────────────
    print("\n  5. DELETE – Remove students with CGPA < 8.0")
    cur.execute("DELETE FROM students WHERE cgpa < 8.0")
    conn.commit()
    print(f"     Rows deleted: {cur.rowcount}")

    show_table(cur, "AFTER DELETES")

    # ── Restore sample data ───────────────────────────────────
    print("  6. Inserting fresh records to restore table...")
    cur.execute("""
        INSERT INTO students (name, age, branch, cgpa) VALUES
        ('Frank', 22, 'Electronics', 7.5),
        ('Grace', 21, 'Computer Science', 9.2)
    """)
    conn.commit()
    print(f"     Rows inserted: {cur.rowcount}")

    show_table(cur, "FINAL state")

except Error as e:
    print(f"\n  ✗ MySQL Error: {e}")
    print("  Ensure q26_mysql_create_insert.py has been run first.")

finally:
    if 'conn' in dir() and conn.is_connected():
        cur.close()
        conn.close()
        print("  ✓ Connection closed.")

print("=" * 65)