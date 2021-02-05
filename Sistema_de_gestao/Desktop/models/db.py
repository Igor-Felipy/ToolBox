import sqlite3


def create_table():
    conn = sqlite3.connect('products.db')

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE stock (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        qtt INTEGER NOT NULL,
        kind TEXT,
        price INTEGER,
        created_in TEXT NOT NULL,
        last_movimentation TEXT,
    );
    """)

    print('table created!!!')

    conn.close()