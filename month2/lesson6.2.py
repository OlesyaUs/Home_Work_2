import sqlite3
connection = sqlite3.connect("db.sqlite3")

cursor = connection.cursor()
cursor.execute("CREATE TABLE students (name TEXT, age INTEGER, weight INTEGER, height INTEGER")

connection.close()