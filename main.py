import sqlite3
from sqlite3 import Error

conn = None
try:
    conn = sqlite3.connect('cnab-transactions.db')
    print('Conected')
except Error as e:
    print(e)
    

conn.execute("CREATE TABLE IF NOT EXISTS transactions (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, trade VARCHAR(500) NOT NULL);")

print('Table created!')

with open('CNAB.txt') as file:
    lines = file.readlines()
    for line in lines:
        conn.execute(f"INSERT INTO transactions (trade) VALUES ('{line}')")

conn.commit()
conn.close()
