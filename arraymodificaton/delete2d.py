import numpy as np

arr = np.array([
    [1, 2],
    [3, 4]
])

newarr=np.delete(arr,1,axis=0)
newarr1=np.delete(arr,1,axis=1)
print(newarr)
print(newarr1)