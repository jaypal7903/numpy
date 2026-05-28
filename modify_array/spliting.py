"""
spliting :
- spliting is the technic to divide the one array to multiple array.
- the numpy provide the three method to perform spliting operation.
    1) split()
    2) vsplit()
    3) hsplit()
"""

# example :

import numpy as np

# split() method for 1-D array
"""
arr = np.array([1,2,3,4,5,6,7,8,9])
print(f"the original array is: {arr}")

divided_arr = np.split(arr,3)
print(f"after spliting:\n {divided_arr}")
"""

# split() method for multi - dim array
"""
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"the original multi-dimensional array:\n {arr2}")

row_wise_divided = np.split(arr2,3,axis=0)
print(f"after spliting multi-dim array:\n {row_wise_divided}")

col_wise_divided = np.split(arr2,3,axis=1)
print(f"after column wise divided array is:\n {col_wise_divided}")
"""

#hsplit() method r 1-D array:
"""
arr = np.array([1,2,3,4,5,6,7,8,9])
print(f"the original array is: {arr}")

hsplit_arr = np.hsplit(arr,3)
print(f"after used hsplit method:\n {hsplit_arr}")"""

# hsplit for multi - dim array :
"""
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"the original multi - dim array:\n {arr2}")

multi_divided_arr = np.hsplit(arr2,3)
print(f"after divided multi-dim array is:\n {multi_divided_arr}")
"""
# Note: vsplit() method only works with 2 or multi-dim array

# vsplit() method for mullti-Dim array :

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"the original mullti-dim array is:\n {arr}")

vsplit_arr = np.vsplit(arr,3)
print(f"after used vsplit method:\n {vsplit_arr}")