import numpy as np 
array= np.array([10,np.nan,30,40,np.nan,60])

print(np.nan_to_num(array,nan=100))