import sqlite3


conn = sqlite3.connect('data/instruments.db')
cursor = conn.cursor()

CREATE_TABLE = '''
CREATE TABLE IF NOT EXISTS instruments (
    id INTEGER PRIMARY KEY, AUTOINCREMENT,
    name TEXT,
    brand TEXT,
    Category TEXT,
    condition TEXT,
    price REAL
)
'''

cursor.execute(CREATE_TABLE)


def add(name, brand, category, condition, price):
    pass

def get_all():
    pass

def delete():
    pass

def update():
    pass

conn.commit()

conn.close()