import sqlite3


def create_table():
    conn = sqlite3.connect('products.db')

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE stock (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        qtd INTEGER NOT NULL
    );
    """)

    print('table created!!!')

    conn.close()