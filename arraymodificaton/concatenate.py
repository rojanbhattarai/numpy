import numpy as np 

array=np.array([10,20])
array2=np.array([30,40])

conc_array=np.concatenate((array,array2),axis=0)
print(conc_array)