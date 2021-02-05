import sqlite3
from db import create_table
from datetime import datetime

try:
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
except:
    create_table()
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()


def uniqueConsult(id):
    try:
        data = cursor.execute("""
        SELECT * 
        FROM  products
        WHERE id = ?
        """,(id))
        conn.commit()
        return(data)
    except:
        return("error")

def consult():
    try:
        data = cursor.execute("""
        SELECT * 
        FROM  products
        ORDER BY id
        """)
        conn.commit()
        return(data)
    except:
        return("error")


def insertProduct(name,qtt,):
    try:
        date = str(datetime.now().strftime('%d-%m-%Y %H:%M'))
        cursor.execute("""
        INSERT INTO products (name, qtt, created_in)
        VALUES (?,?,?)
        """,(name,qtt,date))
        conn.commit()
        return("Product created!")
    except:
        return("error")

def updateQtt(id,qtt):
    try:
        cursor.execute("""
        UPDATE products
        SET qtt = ?
        WHERE id=?
        """,(qtt,id))
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


def quantityPlus(id):
    try:
        qtt = cursor.execute("""
        SELECT qtt 
        FROM  products
        WHERE id = ?
        """,(id))

        qtt = qtt + 1

        cursor.execute("""
        UPDATE products
        SET qtt = ?
        WHERE id=?
        """,(qtt,id))

        conn.commit()
        return("product deleted")
    except:
        return("error")

def quantityLess(id):
    try:
        qtt = cursor.execute("""
        SELECT qtt 
        FROM  products
        WHERE id = ?
        """,(id))

        qtt = qtt - 1

        cursor.execute("""
        UPDATE products
        SET qtt = ?
        WHERE id=?
        """,(qtt,id))

        conn.commit()
        return("product deleted")
    except:
        return("error")