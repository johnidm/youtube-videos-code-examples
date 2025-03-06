## Video Script 

Welcome to our 5-minute guide on how to use SQLite with Python! If you're looking for a fast, easy-to-use database without all the overhead, SQLite is a great choice. And the best part? It’s built right into Python, so no extra installations are needed! In this video, we’ll cover the basics of setting up an SQLite database, performing CRUD operations, and share some tips for getting the most out of it.

---

#### What is SQLite?

SQLite is a lightweight, serverless database engine that’s ideal for small to medium-sized applications. Unlike other databases, it doesn't require a separate server process—everything is stored in a simple file on your system.

#### Connecting to SQLite in Python

Let’s jump right into the code! First, let’s learn how to connect to an SQLite database.


Here, we import sqlite3, which is Python’s built-in library for working with SQLite databases. We then create a connection to a file called example.db. If the file doesn’t exist, it will automatically be created. After that, we create a cursor object, which lets us execute SQL commands.

#### Creating a Table

Now, let’s create a table to store some data.

In this example, we’re creating a simple users table with three fields: id, name, and age. The id is the primary key, which uniquely identifies each row. We wrap everything inside a transaction and commit the changes to the database.

#### Inserting Data

Let’s add some users to our database.

Using the INSERT INTO SQL statement, we add rows for Alice and Bob. After inserting the data, remember to commit the transaction to save the changes.

#### Retrieving Data

Now, let’s retrieve the data we just inserted!

We use SELECT * FROM users to get all the rows from our users table. Then we use fetchall() to retrieve the results and loop through them to display each user.

#### Updating and Deleting Data

Let’s update Alice’s age and then delete Bob from the table

Here, we update Alice’s age using the UPDATE statement and remove Bob with the DELETE statement. Simple and easy!

#### Wrap-up

To recap, we covered how to:

Connect to an SQLite database
1) Create tables
2) Insert, retrieve, update, and delete data

SQLite is a fantastic tool for small projects or when you need a lightweight solution. Thanks for watching, and don’t forget to like and subscribe for more quick programming tips!