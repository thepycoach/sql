import sqlite3

# create a connection
conn = sqlite3.connect('students.db')

c = conn.cursor()  # cursor

# create a table
#
c.execute("""CREATE TABLE students (
            name TEXT,
            age INTEGER,
            height REAL
    )""")

# insert data into a table
c.execute("INSERT INTO students VALUES ('mark', 20, 1.9)")

all_students = [
    ('john', 21, 1.8),
    ('david', 35, 1.7),
    ('michael', 19, 1.83),
]
c.executemany("INSERT INTO students VALUES (?, ?, ?)", all_students)

# select data
c.execute("SELECT * FROM students")
print(c.fetchall())

# commit
conn.commit()

# close the connection
conn.close()
