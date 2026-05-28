"""
insert the element in array:
- numpy provide the insert() method to insert the element in specific position in array.
- numpy provide the append() method to add the element in last position of numpy array.

Note : the insert() and append() method every time return a new array, that can not modify the existing array.

syntax:

-insert() :
    np.insert(arr,index,elemet,axis)
        where, np = numpy
               arr = array
               index = index number to be inserted new element
               element = data to be inserted in array
               axis = it possible three value (None or 0 or 1)   by default value is 0
                        None = flatten array
                        0 = row-wise inserted data
                        1 = colum-wise inserted data
"""

# example :

import numpy as np

# arr = np.array([1,2,3])
# print(f"original array:\n {arr}")

# #insert() method :
# new_arr = np.insert(arr,1,5,axis=None)
# print(f"after inserting new array: {new_arr}")

# print(np.insert(new_arr,2,12))

# # insert() for multi-dimensional array :
# arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(f"2-D original array:\n {arr2}")

# row_wise = np.insert(arr2,1,[11,23,34],axis=0)
# print(f"after inserting new array:\n {row_wise}")

# col_wise = np.insert(arr2,0,[44,56,67],axis=1)
# print(f"after inserting new array:\n {col_wise}")

# print(f"after inserting in row_wise colmn wise add new data:\n {np.insert(row_wise,2,[89,90,92,99],axis=1)}")

"""
append() :
    np.append(arr,element,axis)
        where, np = numpy
               arr = array
               element = data to be inserted
               axis = it possible three value (None or 0 or 1)   by default value is 0
                        None = flatten array
                        0 = row-wise inserted data
                        1 = colum-wise inserted data
"""

# example :

arr = np.array([1,3,4])
print(f"original array:\n {arr}")

# append() metod :

new_arr = np.append(arr,5,axis=None)
print(f"after inserting new array:\n {new_arr}")

print(f"after add second value:\n {np.append(arr,7)}")

#append() method for multi-dimensional array

arr2 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

# Append row-wise (axis=0)
result = np.append(arr2,[[10, 11, 12]], axis=0)

print("After appending a row:\n", result)

#append() method colmn-wise (axis=1)

col_wise = np.append(arr2,[[12],[22],[33]], axis=1)
print(f"after appending a colmn:\n {col_wise}")

print(f"add a new colmn of result array that all-ready contains inserted row:\n {np.append(result,[[45],[67],[99],[92]],axis=1)}")