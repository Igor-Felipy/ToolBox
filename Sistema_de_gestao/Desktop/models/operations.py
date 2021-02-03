import sqlite3
from db import create_table

try:
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
except:
    create_table()
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

def insertProduct(name,qtd):
    try:
        cursor.execute("""
        INSERT INTO products (name, qtd)
        VALUES (?,?)
        """,(name,qtd))
        conn.commit()
        return("Product created!")
    except:
        return("error")

def updateQtd(id,qtd):
    try:
        cursor.execute("""
        UPDATE products
        SET qtd = ?
        WHERE id=?
        """,(qtd,id))
        conn.commit()
        return("quantity updated")
    except:
        return("error")


def updateName(id,name):
    try:
        cursor.execute("""
        UPDATE products
        SET name = ?
        WHERE id=?
        """, (name,id))
        conn.commit()
        return("name updated")
    except:
        return("error")


def deleteProduct(id):
    try:
        cursor.execute("""
        DELETE FROM products
        WHERE id=?
        """,(id))
        conn.commit()
        return("product deleted")
    except:
        return("error")