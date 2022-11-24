import sqlite3

# Crea una base de datos de sqlite en la carpeta con el nombre que le indiquemos
conexion = sqlite3.connect("basedatos1.db")

cursor = conexion.cursor()

list_personas = [('Pedro','Vega','Estrada',24), ('Maria','Aguilar','Patinio',26), ('Ulises','Perez','Monzalvo',23)]

cursor.executemany("INSERT INTO PERSONAS VALUES(?,?,?,?)",list_personas)
conexion.commit()
conexion.close()