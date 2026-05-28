"""
brodcasting :
- broadcasting is the process to convert small array into big array.
- the numpy implicitly perform broadcasting.
"""

# example :

import numpy as np

arr = np.array([1,2,3])
print(f"the small 1-D array is: {arr}")

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"the large array is:\n {arr2}")

result = arr + arr2        #internally the change of shape of arr into the (3,3)
print(f"the resultant array is:\n {result}")

#numpy change the shape of arr and perform operation with new array. the new array is [[1,2,3],[1,2,3],[1,2,3]]
mul_result = arr * arr2     
print(f"after multiply the arr and arr2:\n {mul_result}")