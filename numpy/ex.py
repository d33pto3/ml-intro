# -- Numpy (Numerical Python) - A Python library used for working with arrays.

# -- 1. Create a numpy array

# -- Numpy array-
# a. Optimized for numerical operations (homogenous data types)
# b. Store elements of same data type
# c. Supports vectorized operations, which are faster

# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

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
arr3 = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
print(arr3)

# -- Check Number of Dimensions
print('number of dimensions: ',arr3.ndim)