"""
concatenate method:
- numpy provide the functinality to cancatenate the more than one array.
- the main diffrence btween concatenate and stack method is:
    - the stack method every time create a new dimension but the concatenate method works with existing dimension.
- the concatenate method evry time return a new array that can not change the existing array.
"""

# example :

import numpy as np

# concatenate() for 1-D array:

arr = np.array([1,2,3])
print(f"the first array is: {arr}")

arr2 = np.array([4,5,6])
print(f"the second array is: {arr2}")

arr3 = np.array([5,6,7,8,9])
print(f"the third array is: {arr3}")

merge = np.concatenate((arr,arr2,arr3))
print(f"after concatenate two array:\n {merge}")


# cancatenate() method for multi-dimensional array :

first = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"the first array is:\n {first}")

second = np.full((3,3),7)
print(f"the second array is:\n {second}")

third = np.eye(3)
print(f"the third array is:\n {third}")

fourth = np.zeros((3,3))
print(f"the fourth array is:\n {fourth}")

fifth = np.ones((3,3))
print(f"the fifth array is:\n {fifth}")

after_merge = np.concatenate((first,second,third,fourth,fifth))
print(f"after merging array is:\n {after_merge}")

column_wise_after_merge = np.concatenate((first,second,third,fourth,fifth),axis=1)
print(f"after rmerging colmn wise:\n {column_wise_after_merge}")