#Demonstration of various NumPy shape and reshaping operations
import numpy as np
# Original array
a = np.arange(12)  # Creates a 1D array with values from 0 to 11
print("Original array:", a) # [ 0  1  2  3  4  5  6  7  8  9 10 11]         
print("Shape:", a.shape)     # (12,)
# 1. Reshape to 3x4 array
b = a.reshape(3, 4) # Reshapes to 3 rows and 4 columns
print("Reshaped to 3x4:\n", b)
# 2. Reshape to 2x2x3 array (3D)
c = a.reshape(2, 2, 3) # Reshapes to 2 blocks of 2x3
print("Reshaped to 2x2x3:\n", c)