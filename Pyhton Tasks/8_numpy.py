

# task  :1  
"""
output  : [[13,14], 
            [19,20]]
"""

# print(a[2:4,0:2])

# task  :2 
"""
output  : [[2,9,16,23,30]]
# """
# for i in range(5):
#     print(a[ 0 + i , 1 + i ],end=" ")

import numpy as np

"""
task  :1 
[
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1]]

output  :
[
[1,1,1,1,1],
[1,0,0,0,1],
[1,0,9,0,1],
[1,0,0,0,1],
[1,1,1,1,1]]

"""
'''
a = np.array([
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1]]
)

a[1:4,1:4] = 0
a[2,2] = 9
print(a)'''


# Sort Random Vector of Size 10

# Write a NumPy program to create a random vector of size 10 and sort it.

# Expected Output:
# Original array:
# [ 0.73123073 0.67714015 0.95615347 0.4759837 0.88789818 0.6910404 2
# 0.59996415 0.26144489 0.51618644 0.89943882]
# Sorted array:
# [ 0.26144489 0.4759837 0.51618644 0.59996415 0.67714015 0.6910404 2
# 0.73123073 0.88789818 0.89943882 0.95615347]


# import numpy as np
# arr = np.random.rand(10)
# print("array:")
# print(arr)
# arr.sort()
# print("Sorted array:")
# print(arr)


'''Write a NumPy program to create a 3x3x3 array with random values.'''

# import numpy as np
# arr = np.random.random((3,3,3))
# print(arr)

'''Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

Update sixth value to 11
[ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]'''

# arr = np.zeros(10)
# print(arr)
# arr[5] = 11
# print(arr)

'''Write a NumPy program to convert a list and tuple into arrays.

List to array:
[1 2 3 4 5 6 7 8]

Tuple to array:
[[8 4 6]
[1 2 3]]'''

# l1 = [1,2,3,4,5,6,7,8]
# t1 = ( (8,4,6) , (1,2,3) )
# arr1 = np.array(l1)
# arr2 = np.array(t1)
# print(arr1)
# print(arr2)


'''
Write a NumPy program to test whether each element of a 1-D array is also present in a second array. 
Array1:  [ 0 10 20 40 60]                                              
Array2:  [0, 40]                                                       
Compare each element of array1 and array2                              
[ True False False  True False]'''


# array1 = np.array([0,10,20,40,60])
# array2 = np.array([0,40])
# result = np.isin(array1, array2)
# print(result)

'''Create Array of Zeros, Ones, Fives

Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives. 
An array of 10 zeros:
[ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
An array of 10 ones:
[ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]
An array of 10 fives:
[ 5.  5.  5.  5.  5.  5.  5.  5.  5.  5.]'''

# zeros = np.zeros(10)
# ones = np.ones(10)
# fives = np.ones(10) * 5
# print(zeros)
# print(ones)
# print(fives)

'''Write a NumPy program to create a 3x3 identity matrix.'''

matrix = np.zeros(9).reshape(3,3)
matrix[0,0] = 1
matrix[1,1] = 1
matrix[2,2] = 1

print(matrix)