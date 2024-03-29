import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title,content) VALUES (?,?)",
            ('First post','Content for first post')
            )

cur.execute("INSERT INTO posts (title,content) VALUES (?,?)",
            ('2nd post','Content for 2nd post')
            )

connection.commit()
connection.close()
