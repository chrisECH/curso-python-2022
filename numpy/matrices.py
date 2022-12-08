# Array o matrices transpuestas
import numpy as np

array = np.arange(15).reshape((3,5))
print(array)


print(array[0][1])


#trasnpuesta 
array_trans = array.transpose()
print(array_trans)