'''
.ravel()->  views
.flatten()-> copy no change in original value
'''
import numpy as np

# Creating a 2D array
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arrravel= arr.ravel()

print(arr.flatten())
print(arrravel)

