"""
indexing :
- indexing means access the one element based ob index.
- in python, numpy provide the concept of indexing.
- every element frist index is zero.

slicing :
- slicing means access the more than one element in array.
"""

# example :

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,0])
print(arr)

# indexing :

print(arr[0])    #output -> 1
print(arr[1])    #output -> 2

arr[2] = 20     #change is apply the original array

print("used of loop")
for i in range(0,10,1) :
    print(arr[i],end=" ")

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])  #in two dim array access the element used aarray_name[row][column] 
print("\n",arr2) 
print(arr2[0][2])       #output  -> 3
print(arr2[1][1])       #output  -> 5
print(arr2[2][0])       #output  -> 7


# slicing : [start:stop:step]  start is inclusive but stop is exclusive

print(arr[1 : 11 : 2])       #output :  2 4 6 8 0
print(arr[::-1])            #output : 0 9 8 7 6 5 4 3 2 1  (if we not pass the start and stop then python automatically take entire array)
print(arr[3:8])            #output : 4 5 6 7 8  (the step is optinal if we not not than by default take 1)