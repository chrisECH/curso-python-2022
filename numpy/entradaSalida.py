#Entrada y salida de arrays
import numpy as np

array1 = np.arange(6)
print(array1)

np.save("array1s", array1)
np.load("array1s.npy")

array1 = np.arange(6)
print(array1)
array2 = np.arange(8)
print(array2)

np.savez("arrays", x=array1, y=array2)
array_recuperado = np.load("arrays.npz")
print(array_recuperado)
print(array_recuperado['x'])

np.savetxt("miFicheroArray.txt",array2,delimiter=",")
np.loadtxt("miFicheroArray.txt",delimiter=",")