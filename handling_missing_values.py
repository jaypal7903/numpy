"""
handling missing values:
- the numpy provide the functionality to handle the missing values in a dataset.
- the numpy provide the three functions to handle the missing values.
    1) np.isnan(array)
    2) np.isinf(array)
    3) np.nan_to_num(array,nan or inf, number)

- 1) np.isnan(array) :
    - the nan stands for not a number.
    - this function is return the boolean array.
    - if a given array has any nan value then function return the True otherwise Flase of this this position.

- 2) np.isinf(array) :
    - the inf stands for infinity.
    - this function is return the boolean array.
    - if a given array has any inf value then the function return the True otherwise Flase of this position.

- 3)np.nan_to_num(array,nan or inf , number) :
    - this function is used to replace the value with number.
    - the default value of this function is zero.
"""

# example :

import numpy as np

#np.isnan() method

arr = np.array([1,3,5,np.nan,9,np.nan])
print(f"the original array is: {arr}")

#check the arr has any contain not a number values.
after_check = np.isnan(arr)
print(f"after checking the result is: {after_check}")

replace_arr = np.nan_to_num(arr,np.nan,5)
print(f"after replace with mean value: {replace_arr}")


# np.isinf() method

# arr = np.array([1,2,3,np.inf,5,-np.inf])
# print(f"the original array is: {arr}")

# #check the function has any inf values
# check = np.isinf(arr)
# print(f"after checking: {check}")

# #replace the inf value with any number:
# replace = np.nan_to_num(arr,posinf=5,neginf=1)
# print(f"after replace the value: {replace}")