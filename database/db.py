import sqlite3

def connect():
    return sqlite3.connect('data/instruments.db')

CREATE_TABLE = '''
CREATE TABLE IF NOT EXISTS instruments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    brand TEXT,
    category TEXT,
    condition TEXT,
    price REAL
)
'''

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(CREATE_TABLE)
    conn.commit()
    conn.close()

def add(name, brand, category, condition, price):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO instruments (name, brand, category, condition, price) VALUES (?, ?, ?, ?, ?)',
                   (name, brand, category, condition, price))
    conn.commit()
    conn.close()

def get_all():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM instruments')
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM instruments WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def update(name, brand, category, condition, price):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('UPDATE instruments SET brand = ?, category = ?, condition = ?, price = ? WHERE name = ?',
                   (brand, category, condition, price, name))
    conn.commit()
    conn.close()
