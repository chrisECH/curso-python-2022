import sqlite3

# Crea una base de datos de sqlite en la carpeta con el nombre que le indiquemos
conexion = sqlite3.connect("basedatos1.db")

cursor = conexion.cursor()

cursor.execute("INSERT INTO PERSONAS VALUES('Christian', 'Camarena', 'Hernandez', 25)")

conexion.commit()
conexion.close()