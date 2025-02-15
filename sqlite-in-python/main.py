"""
DB-API 2.0 interface for SQLite databases documentation
https://docs.python.org/3/library/sqlite3.html
"""

import sqlite3

database_filename = "example.db"


# Using a context manager to connect to the database
# automatically close the connection
with sqlite3.connect(database_filename) as conn:
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

    print("Table created!")


# Inserting Data
with sqlite3.connect(database_filename) as conn:
    cur = conn.cursor()

    # Insert data into the users table
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))

    print("Data inserted!")


# Retrieving Data
with sqlite3.connect(database_filename) as conn:
    cur = conn.cursor()

    # Fetch and display all rows from the users table
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

    for row in rows:
        print(row)


# Updating and Deleting Data
with sqlite3.connect() as conn:
    cur = conn.cursor(database_filename)

    # Update Alice's age
    cur.execute("UPDATE users SET age = ? WHERE name = ?", (26, "Alice"))

    # Delete Bob from the table
    cur.execute("DELETE FROM users WHERE name = ?", ("Bob",))

    print("Data updated and deleted!")
