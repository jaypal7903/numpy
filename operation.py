"""
mathamatical operation on numpy array:
- we can perform the various mathamatical operation on numpy array.
    - 1) + [add the constant number with all element of numpy array].
    - 2) - [subtract the constant number with all element of numpy array].
    - 3) * [multiply the constant number with all element of numpy array].
    - 4) / [divide the constant number with all element of numpy array].
    - 5) % [give the remainder of all element of numpy array].
    - 6) // [divide the constant number with all element of numpy array and return the floor value].
    - 7) ** [perform the power operation with all element of numpy array].
"""

# example :

import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"original array :\n {arr}")

# add with constant number
print(f"after add constant number:\n {arr +5}")

#subtract wth constant number
print(f"after subtract constant number:\n {arr - 5}")

#multiply with constant number
print(f"after multiply with constant number:\n {arr * 5}")

#divide with constant number
divided_arr = arr / 5
print(f"after division with constant number:\n {divided_arr}")

# convert into int
after_converted = divided_arr.astype(int)
print(f"after convert into int:\n {after_converted}")

#modulo operation with constant
print(f"after perform modulo operation:\n {arr % 5}")

# floor division operation with constant number 
print(f"after perform floor division operation:\n {arr // 3}")

print(f"after perform power operation with constant number:\n {arr ** 3}")