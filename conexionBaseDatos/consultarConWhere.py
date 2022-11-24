import sqlite3

conexion = sqlite3.connect("basedatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS WHERE edad >= 25")

personas = cursor.fetchall()

for persona in personas:
    print(persona)

conexion.close()