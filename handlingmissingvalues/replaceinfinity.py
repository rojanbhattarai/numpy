import numpy as np 
array= np.array([10,np.inf,30,-np.inf,50,60])
print(f"this is the original array   {array}")

cleaned_arr=np.nan_to_num(array,posinf=10000,neginf=-10000)
print(f"this is the cleaned array   {cleaned_arr}")