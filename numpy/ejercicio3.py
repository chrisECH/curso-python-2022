# Crear lista con valores del 0 al 30
# Crear otra lista con los primeros 10 valores de la lista inicial
# Crear una lista con los últimos 10 valores de la lista inicial
# Crear un bucle que recorra esta última lista de valores finales


import numpy as np

array1 = np.arange(0,31)
print(array1)

array2 = array1[0:10]
print(array2)

array3 = array1[-10:]
print(array3)

for i in array3:
    print(i)