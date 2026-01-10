import numpy as np 

array = np.array([
    [1, 2],
    [3, 4]
])

print(np.split(array,2,axis=0))
print(np.hsplit(array,2))
print(np.vsplit(array,2))
