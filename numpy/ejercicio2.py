#1- crear una lista con números del 10 al 19
#2- Crear una lista con números del 50 al 59
# 3- Crear una matriz 2x10 con las listas anteriores
# 4- Crear otra matriz que cuyos valores sean iguales a la matriz anterior multiplicado por 2
import numpy as np

lista = np.arange(10, 20)
lista2 = np.arange(50,60)

lista_doble = (lista, lista2)
array_doble = np.array(lista_doble).reshape((2,10))
print(array_doble)

multiplicado = array_doble * 2
print(multiplicado)