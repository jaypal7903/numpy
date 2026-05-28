"""
delete() method :
- the method used to delete the element of the numpy array.
- the delete method every time return a new array that can not change in exsting array.

syntax :

np.delete(arr,index,axis)
    where, np = numpy
           arr = array name
           index = index number that deleted element
           axis = it possible three values(None,0,1)
                    None = it used to 1-D array [by default value is 0]
                    0 = it used to row wise delete the element of the array
                    1 = it used to colum wise delete the element of the array
"""

# exaple :

import numpy as np

# 1 - D array :
arr = np.array([10,20,30,40,50,60])
print(f"the original array is: {arr}")

delete_arr = np.delete(arr,2,axis=None)
print(f"after deleting element the new array is:\n {delete_arr}")

# multi - D array :

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"the original array is:\n {arr2}")

row_wise = np.delete(arr2,1,axis=0)
print(f"after deleting:\n {row_wise}")

col_wise = np.delete(arr2,1,axis=1)
print(f"after deleting colmn wise:\n {col_wise}")