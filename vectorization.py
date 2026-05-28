"""
vectorization :
- vectorization is the process to perform mathamtical operation with array with out used python loop.
"""
# example :

import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"the original array is:\n {arr}")

result = arr * 5        #the numpy implicitly multiply the all element of array with 5
print(f"array after multiply with 5:\n {result}")

add_result = arr + 5
print(f"after add 5 the new array is:\n {add_result}")