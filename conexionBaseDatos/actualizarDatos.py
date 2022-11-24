import sqlite3

conexion = sqlite3.connect("basedatos1.db")

cursor = conexion.cursor()

cursor.execute("UPDATE PERSONAS SET edad = 25 WHERE nombre = 'Maria'")
conexion.commit()
personas =cursor.execute("SELECT * FROM PERSONAS")

for persona in personas:
    print(persona)

conexion.close()