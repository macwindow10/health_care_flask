import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (fname, mname, lname, email, password, postal_code) VALUES (?, ?, ?, ?, ?, ?)",
            ('John', 'W', 'Doe', 'john.doe@yahoo.com', '123456', '45763')
            )

connection.commit()
connection.close()
