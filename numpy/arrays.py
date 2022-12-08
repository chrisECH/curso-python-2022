import numpy as np


#Creado arrays
np.zeros(4)


np.ones(5)

print(np.arange(5))

lista1 = [1,2,3,4]
array1 = np.array(lista1)
print(array1)

lista2 = [5,6,7,8]
lista_doble = (lista1, lista2)

array_doble=np.array(lista_doble)
print(array_doble)
print(array_doble.shape)
