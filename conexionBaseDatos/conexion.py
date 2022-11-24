import sqlite3

# Crea una base de datos de sqlite en la carpeta con el nombre que le indiquemos
conexion = sqlite3.connect("basedatos1.db")

cursor = conexion.cursor()
cursor.execute("CREATE TABLE PERSONAS (nombre TEXT, apellido1 TEXT, apellido2 TEXT, edad INTEGER)")
conexion.commit()
conexion.close()
