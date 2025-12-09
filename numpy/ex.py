# -- Numpy (Numerical Python) - A Python library used for working with arrays.

# -- 1. Create a numpy array

# -- Numpy array-
# a. Optimized for numerical operations (homogenous data types)
# b. Store elements of same data type
# c. Supports vectorized operations, which are faster

# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# print(arr)

# -- ndarray
# print(type(arr))

# -- numpy version
# print(np.__version__)

# -- 0-D Arrays
# arr1 = np.array(45)
# print(arr1)

# -- 1-D Arrays [arr itself]

# -- 2-D Arrays
# arr2 = np.array([[1,2,3], [4,5,6]])
# print(arr2)

# -- 3-D Arrays
# arr3 = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
# print(arr3)

# -- Check Number of Dimensions
# print('number of dimensions: ',arr3.ndim)

# -- Array indexing
# arr3 = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11, 12]]])
# print(arr3[0, 1, 2])

# -- Array slicing
# arr = np.array([1,2,3,4,5,6,7])
# print(arr[::2])

# Slicing 2D array

# arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr2[0:2, 1:4:2])

# -- Data Type
 
# Checking Data type of an array
# arr = np.array([1,2,3,4,5])
# print(arr.dtype) 

# arr2 = np.array(['apple', 'banana', 'cherry'])
# print(arr2.dtype)

# arr3 = np.array([1, 2])
# print(arr3.dtype)

# Creating array with defined data type
# arr4 = np.array([12,22,33,4455], dtype= 'S')
# print(arr4.dtype)

# -- Converting Data Type on Existing Arrays
# arr = np.array([1.1, 2.1, 3.7])
# newArr = arr.astype('i') # (int32)
# newArr2 = arr.astype(int) # (int64)

# print(newArr)
# print(newArr2)
# print(newArr.dtype)
# print(newArr2.dtype)

# int to boolean
# newArr3 = arr.astype(bool)
# print(newArr3)
# print(newArr3.dtype)

# -- copy vs view (one has base, one doesn't have)
# copy is a separate array from the main array
# view is the same array it cloned from just a view of that

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# y = arr.view()

# print(x.base)
# print(y.base)

# x[0] = 41
# print(x, arr)

# y[0] = 30
# print(y, arr)

# -- Array Shape
# The shape of an array is the number of elements 
# arr = np.array([[1,2,3,4],[5,6,7,8]])
# print(arr.shape) # returns (2, 4) - means the array has 2 dimensions, where the first dimension has 2 elements and the second has 4

# arr2 = np.array([1,2,3,4], ndmin=5) # creating a 5 dimension array from this
# print(arr2)
# print(arr2.shape)

# -- Array Reshape (changing the shape of an array)
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# # newarr = arr.reshape(4,3) # Create 4 arrays with 3 elements in each array (4 * 3 = 12) 
# # print(newarr)

# newarr = arr.reshape(2, 3, 2) # 2 * 3 * 2 = 12
# print(newarr)

# print(newarr.base) # returns the main array, so its a view

# arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# newarr2 = arr2.reshape(2, 2, -1) # we can have one unknow dimension (-1), which will be calculated auto

# print(newarr2)

# important: flattening the arrays:
# arr3 = np.array([[1,2,3],[4,5,6]])
# newarr3 = arr3.reshape(-1)
# print(newarr3)

# -- array iterating
arr = np.array([1,2,3])

for x in arr: 
    print(x)
    
arr2 = np.array([[1,2,3], [4,5,6]])

for x in arr2:
    for y in x:
        print(y)
        
# Iterating arrays using nditer 