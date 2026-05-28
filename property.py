"""
property of numpy array :
- the numpy provide the some property of numpy array.
"""

# example :

import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,0]])
print(arr)

shape = arr.shape           # arr.shape  -> is return the shape of the array in the form of tuple 
print(f"the shape of array is: {shape}")

size = arr.size             # arr.size  -> is return total number of element present in array
print(f"the size of the array is: {size}")

dim = arr.ndim              # arr.ndim  -> is return the number of dimension in the array
print(f"the number of demensional is: {dim}")

data_type = arr.dtype       #arr.dtype  -> is return the data type of the arrays's elemrnt
print(f"the data type of the array's element is: {data_type}")

arr_converted = arr.astype(str)
print(f"after convert the type array is:\n {arr_converted}")