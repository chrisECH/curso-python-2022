

try:
    numero1 = 5
    numero2 = 2
    division = numero1 / numero2
    print(division)
except ZeroDivisionError:
    print("Error: Division entre cero")
except:
    print("Ha habido un error")
else:
    print("La division funciono correctamente")
finally:
    print("Esta prueba ha terminado")
