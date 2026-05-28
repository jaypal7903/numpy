"""
Aggerigation function :
- Aggrigation function means take more than one value and retuen only one value.
- numpy provide the some aggregation function :
    - 1) sum()  [add the all element of array and return single value].
    - 2) max()  [find the maximam element of given array].
    - 3) min()  [find the minimum element of given array].
    - 4) std()  [find the standatrd divation of given array].
    - 5) var()  [find the variance of the given array].
    - 6) prod() [multiply the all element of given array].
    - 7) mean() [find the average of all element of given array].
    - 8) median() [find the middle value of numpy array].
"""

#example :

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

# perform sum method
print(f"the addition of all element of numpy array is: {np.sum(arr)}")

# perform max method
print(f"the maximum element in numpy array is: {np.max(arr)}")

# perform min method
print(f"the minimum element in numpy array is: {np.min(arr)}")

#find the standard divatian with the help of std() method
print(f"the stadard divation of numpy array is: {np.std(arr)}")

#find the variance with the help of var() method
print(f"the variance of numpy array is: {np.var(arr)}")

# find the product of numpy array with the help of prod() method
print(f"the product of numpy array is: {np.prod(arr)}")

# find the average value of numpy array with the help of mean() method
print(f"the mean value of numpy array is: {np.mean(arr)}")

# find the median value of numpy array with the help of median() method
print(f"the median value of numpy array is: {np.median(arr)}")