import numpy as np

arr = np.array([
    [1, 2],
    [3, 4]
])

newarr1=np.insert(arr,2,[5,6],axis=None)
newarr2=np.insert(arr,2,[5,6],axis=0)
newarr3=np.insert(arr,2,[5,6],axis=1)
print(newarr1)
print(newarr2)
print(newarr3)
