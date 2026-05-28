"""
Q - How to declare the numpy array?
    - numpy provide the multiple ways to created array.
    - generally, numpy array is created with the help of .array() method.
"""

import numpy as np 

#with the help of list :
with_lst = np.array([1,2,3,4,6])   # one - dimensional array
print(f"with the help of python list : {with_lst}")

# created zeros array :
zeros = np.zeros((2,3))   #pass the shape in the form of tuple
print(f"with the help of zeros method :\n {zeros}") 

# created ones array :
ones = np.ones((3,3))   #pass the shape in the form of tuple
print(f"with the help of ones method:\n {ones}")

#created specific numbers :
specific = np.full((3,3),7)
print(f"with the help of full method:\n {specific}")

#crated identity matrix :
identity = np.eye(3)
print(f"with the help of eye method:\n {identity}")

                    #or

# from numpy import array as np
# from numpy import zeros as z
# from numpy import ones as o
# from numpy import eye as e
# from numpy import full as f

# arr = np([[1,2,3],[5,6,7]])
# print(arr)

# zero = z((2,3))
# print(zero)

# one = o((3,4))
# print(one)

# ident = e(4)
# print(ident)

# full = f((3,4),7)
# print(full)


#multi dimensional array  or tensor

multi_dim = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[21,22,23],[24,25,26],[27,28,29]]])
print(multi_dim)
print(multi_dim.shape)
print(multi_dim.ndim)
print(multi_dim.size)