#!/usr/bin/python2

import sqlite3

mydatabase = "/home/bal/Proiect/NutryPy/products.sqlite"
connection = sqlite3.connect(mydatabase)
cursor = connection.cursor()
cursor.execute('SELECT * FROM products WHERE id=1')
entries = cursor.fetchall()

#print entries

cursor.close()
quit()
