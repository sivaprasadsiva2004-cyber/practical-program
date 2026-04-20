# ============================================================
# Q26. Connect to a MySQL database, create a table,
#      and insert records.
#
# Prerequisites:
#   pip install mysql-connector-python
#
# Update DB_CONFIG below with your MySQL credentials.
# ============================================================

import mysql.connector
from mysql.connector import Error

# ── Database configuration – update these values ─────────────
DB_CONFIG = {
    "host"    : "localhost",
    "user"    : "root",
    "password": "your_password",   # ← change this
    "database": "college_db",      # will be created if absent
}

# ── Sample data to insert ─────────────────────────────────────
STUDENTS = [
    ("Alice",   21, "Computer Science", 9.1),
    ("Bob",     22, "Electronics",      7.8),
    ("Charlie", 20, "Data Science",     8.5),
    ("Diana",   23, "AI & Big Data",    9.4),
    ("Eve",     21, "Computer Science", 8.0),
]


def get_connection(without_db: bool = False):
    """
    Return a MySQL connection.
    If without_db=True, connect without selecting a database
    (used for CREATE DATABASE).
    """
    config = dict(DB_CONFIG)
    if without_db:
        config.pop("database", None)
    return mysql.connector.connect(**config)


def setup_database():
    """Create the database if it doesn't already exist."""
    conn = get_connection(without_db=True)
    cur  = conn.cursor()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
    print(f"  ✓ Database '{DB_CONFIG['database']}' ready.")
    cur.close()
    conn.close()


def create_table(conn):
    """Drop (if exists) and create the students table."""
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS students")

    create_sql = """
        CREATE TABLE students (
            id         INT          AUTO_INCREMENT PRIMARY KEY,
            name       VARCHAR(50)  NOT NULL,
            age        INT          NOT NULL,
            branch     VARCHAR(100) NOT NULL,
            cgpa       FLOAT        NOT NULL,
            created_at TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
        )
    """
    cur.execute(create_sql)
    conn.commit()
    print("  ✓ Table 'students' created.")
    cur.close()


def insert_records(conn, records: list):
    """Insert multiple student records using executemany()."""
    cur = conn.cursor()

    insert_sql = """
        INSERT INTO students (name, age, branch, cgpa)
        VALUES (%s, %s, %s, %s)
    """
    cur.executemany(insert_sql, records)
    conn.commit()
    print(f"  ✓ {cur.rowcount} records inserted successfully.")
    cur.close()


def display_table(conn, table: str = "students"):
    """Fetch and display all rows from a table."""
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows    = cur.fetchall()
    columns = [desc[0] for desc in cur.description]

    print(f"\n  Table: {table}")
    print("─" * 65)
    header = "  " + "  ".join(f"{col:<12}" for col in columns)
    print(header)
    print("─" * 65)
    for row in rows:
        print("  " + "  ".join(f"{str(v):<12}" for v in row))
    print("─" * 65)
    print(f"  {len(rows)} row(s) returned.")
    cur.close()


# ── Main ─────────────────────────────────────────────────────
print("=" * 65)
print("  Q26 – MySQL: Connect → Create Table → Insert Records")
print("=" * 65)

try:
    # Step 1: ensure database exists
    setup_database()

    # Step 2: connect to the database
    conn = get_connection()
    print(f"  ✓ Connected to MySQL server (v{conn.get_server_info()})")

    # Step 3: create table
    create_table(conn)

    # Step 4: insert records
    insert_records(conn, STUDENTS)

    # Step 5: display
    display_table(conn)

except Error as e:
    print(f"\n  ✗ MySQL Error: {e}")
    print("\n  NOTE: This program requires a running MySQL server.")
    print("  Update DB_CONFIG at the top of the file with your credentials.")

finally:
    if 'conn' in dir() and conn.is_connected():
        conn.close()
        print("\n  ✓ Connection closed.")

print("=" * 65)