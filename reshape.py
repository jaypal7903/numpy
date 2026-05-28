"""
reshaping :
- numpy provide the functinality to convert the multi-dimensional array into a 1-D array.
- also convert the 1-D array into multi-dimensional array.
"""

# example :

import numpy as np

# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(f"the shape of array before converting: {arr.shape} \n array is:\n {arr}")

# # converting into 1-D array :

# # with the help of ravel method 
# new_arr = arr.ravel()           #the ravel() method return the new array thay can't convert existing array
# print(f"after converting new array is: {new_arr}")
# print(f"the orginal array is:\n {arr}")

# flatten_arr = arr.flatten()     #the flatten array is create a view of the array.
# print(f"with the help of flatten method:\n {flatten_arr}")
# print(f"the original array is:\n {arr}")


"""
coverting 1-D into multi-dimensional.
"""

arr = np.array([1,2,3,4,5,6,7,8,9])
print(f"the original array is:\n {arr}")

#converting with the help of reshape() method

converted_arr = arr.reshape((3,3))      #in the reshape((row,colmn)) pass the new shape in the form of tuple.
print(f"after converting:\n {converted_arr}")  #every time return a new array