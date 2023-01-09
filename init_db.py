import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (role, fname, mname, lname, email, password, postal_code) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('Patient', 'John', 'W', 'Doe', 'john.doe@yahoo.com', '123456', '45763')
            )

cur.execute("INSERT INTO users (role, fname, mname, lname, email, password, postal_code, qualification, expertise) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Doctor', 'David', 'A', 'Runner', 'david.runner@yahoo.com', '123456', '45763', 'MBBS, FCPS', 'MedicalSpecialist')
            )

connection.commit()
connection.close()
