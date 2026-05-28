"""
stacking :
- stacking is the process to merge multiple array.
- the numpy provide the to type of stacking method:
    - 1)vstack (verticly merge the array).
    - 2)hstack (horigontaly merge the array).

- the no. of dimensional are must be same.
     
Note : [the stacking method not change the original array that return a new array.]
"""

# example :

import numpy as np

# stacking method for 1-D array

# arr = np.array([1,2,3])
# print(f"the first array is: {arr}")

# arr2 = np.array([4,5,6])
# print(f"the second array is: {arr2}")

# arr3 = np.arange(1,10,3)
# print(f"the third array is: {arr3}")

# vstack_arr = np.vstack((arr,arr2,arr3))
# print(f"after joining new array is:\n {vstack_arr}")

# hstack_arr = np.hstack((arr,arr2,arr3))
# print(f"after joinng horizontaly the new array is:\n {hstack_arr}")

# print(f"the shape of hstack_arr is: {vstack_arr.shape}")
# print(f"the size of hstack_arr is: {vstack_arr.size}")
# print(f"the no. of dimensional of hstack_arr is: {vstack_arr.ndim}")
# print(f"the datatype of hstack_arr is: {vstack_arr.dtype}")

# stacking method for multi-dimensional array:

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"the first array:\n {arr}")

arr2 = np.full((3,3),5)
print(f"the second array:\n {arr2}")

arr3 = np.ones((3,3))
print(f"the third array is:\n {arr3}")

arr4 = np.zeros((3,3))
print(f"the fourth array is:\n {arr4}")

arr5 = np.eye(3)
print(f"the fifth array is:\n {arr5}")

#vstack() method :

vstack_arr = np.vstack((arr,arr2,arr3,arr4,arr5))
print(f"after use vstack method the new array is:\n {vstack_arr}")

#hstack() method :

hstack_arr = np.hstack((arr,arr2,arr3,arr4,arr5))
print(f"the use of hstack methof the new array is:\n {hstack_arr}")

# stack() method:  the stack method create a new dimension every time.
"""
if we apply axis = 1 then the new array take the first row of first array and seocnd row of second array's first row as well as entire program.
if we apply axis = 0 then the new array take first array and after take a second array as well as entire program.
"""
stack = np.stack((arr,arr2,arr3,arr4,arr5),axis=0)
print(f"after used satacking method:\n {stack}")