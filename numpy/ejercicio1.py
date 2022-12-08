#Crear funcion pares que devuelva un arreglo de numeros pares entre dos valores pasados como parametros
import numpy as np

def pares(numero1, numero2):
    if(numero1 % 2 == 0):
        array = np.arange(numero1, numero2,2)
    else:
        numero1 = numero1 + 1
        array = np.arange(numero1, numero2, 2)
    return array

print(pares(2,40))
