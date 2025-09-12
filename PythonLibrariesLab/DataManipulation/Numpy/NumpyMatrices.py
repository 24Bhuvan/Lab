# Demonstration of Numpy Matrix
# Creation
# Operations
# Matrix Multiplication
# Flatten (to array)
# Conversion to ndarray

import numpy as np

# -------------------------
# 1. Matrix Creation
print("\n1. Matrix Creation:")
m = np.matrix([[1, 2, 3],
               [4, 5, 6]])
print("Matrix m:\n", m)
print("Type:", type(m))

# -------------------------
# 2. Basic Operations
print("\n2. Basic Operations:")
print("m + m:\n", m + m)       # element-wise addition
print("m * 2:\n", m * 2)       # scalar multiplication
print("m.T (transpose):\n", m.T)

# -------------------------
# 3. Matrix Multiplication (* operator is matrix mult for np.matrix)
print("\n3. Matrix Multiplication:")
m2 = np.matrix([[1, 0],
                [0, 1],
                [1, 1]])
print("Matrix m2:\n", m2)
print("m * m2:\n", m * m2)

# -------------------------
# 4. Flatten (to 1D array)
print("\n4. Flatten:")
print("Flattened (to ndarray):", np.array(m).flatten())

# -------------------------
# 5. Conversion to ndarray
print("\n5. Conversion to ndarray:")
arr = np.asarray(m)
print("Converted ndarray:\n", arr)
print("Type:", type(arr))
