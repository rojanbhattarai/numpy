import numpy as np 

array=np.array([10,20])
array2=np.array([30,40])

arr=np.vstack((array,array2))
arr1=np.hstack((array,array2))
print(arr)
print(arr1)