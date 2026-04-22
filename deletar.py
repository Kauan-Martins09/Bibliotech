import sqlite3
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE usuarios")

conn.commit()