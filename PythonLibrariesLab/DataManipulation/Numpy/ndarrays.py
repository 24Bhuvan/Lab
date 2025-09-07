# Creating and Dimensions of ND Arraysimport numpy as np 
import numpy as np # Import NumPy

# 1D Array
arr1 = np.array([1, 2, 3])
print("1D:", arr1, "Dim:", arr1.ndim, "Shape:", arr1.shape)

# 2D Array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D:\n", arr2, "Dim:", arr2.ndim, "Shape:", arr2.shape)

# 3D Array
arr3 = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
print("3D:\n", arr3, "Dim:", arr3.ndim, "Shape:", arr3.shape)

# 2D Array with ndmin
arr_nd2 = np.array([1, 2, 3], ndmin=2)
print("2D ndmin=2:\n", arr_nd2, "Dim:", arr_nd2.ndim, "Shape:", arr_nd2.shape)

# 5D Array with ndmin
arr_nd5 = np.array([1, 2, 3, 4], ndmin=5)
print("5D ndmin=5:\n", arr_nd5, "Dim:", arr_nd5.ndim, "Shape:", arr_nd5.shape)