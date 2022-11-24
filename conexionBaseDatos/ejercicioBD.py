import sqlite3

conexion = sqlite3.connect("basededatos.db")

cursor = conexion.cursor()
cursor.execute("DROP TABLE PRODUCTOS")
conexion.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTOS (id INTEGER, nombre TEXT, precio INTEGER) ")
conexion.commit()

lista_productos = [(1,'Impresora', 300), (2,'Raton',20), (3,'Ordenador', 600)]

cursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", lista_productos)
conexion.commit()

productos = cursor.execute("SELECT * FROM PRODUCTOS")

for producto in productos:
    print(producto)

conexion.close()