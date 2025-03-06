"""
DB-API 2.0 interface for SQLite databases documentation
https://docs.python.org/3/library/sqlite3.html
"""

import sqlite3

database_filename = "example.db" # Using in-memory SQLite database :memory:
"""
To use SQLite in-memory database, you just need to use ":memory:" as the database name instead of a file name. 
This creates a temporary database that exists only in memory and will be deleted when the connection is closed.

The in-memory SQLite database is useful for:

- Testing
- Temporary data processing
- Cases where you don't need to persist the data
- Performance-critical applications (since memory operations are faster than disk operations)
Keep in mind that:

1. All data will be lost when the connection is closed
2. Each connection creates its own separate in-memory database
3. If you need to share data between different connections, you'll need to use a file-based database instead
The rest of your code will work exactly the same way, just with the in-memory database instead of a file-based one.

"""

# Using a context manager to connect to the database
# automatically close the connection
with sqlite3.connect(database_filename, timeout=10.0,) as conn:
    # Create a cursor object
    cur = conn.cursor()

print("Connected to SQLite!")


# Creating a Table
with sqlite3.connect(database_filename) as conn:
    cur = conn.cursor()

    # Create a table called 'users'
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER
                  )""")

    conn.commit()
    print("Table created!")


# Inserting Data
with sqlite3.connect(database_filename) as conn:
    cur = conn.cursor()

    # Insert data into the users table
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))

    print("Data inserted!")
    conn.commit()


# Retrieving Data
with sqlite3.connect(database_filename) as conn:
    cur = conn.cursor()

    # Fetch and display all rows from the users table
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

    for row in rows:
        print(row)


# Updating and Deleting Data
with sqlite3.connect(database_filename) as conn:
    cur = conn.cursor()

    # Update Alice's age
    cur.execute("UPDATE users SET age = ? WHERE name = ?", (26, "Alice"))

    # Delete Bob from the table
    cur.execute("DELETE FROM users WHERE name = ?", ("Bob",))
    conn.commit()
    print("Data updated and deleted!")
