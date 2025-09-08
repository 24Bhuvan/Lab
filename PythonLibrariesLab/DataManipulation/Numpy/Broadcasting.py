#Demonstratiosn of various NumPy broadcasting operations
import numpy as np
#Broadcasting means performing operations on arrays of different shapes

# Original arrays
a = np.array([[1, 2, 3], [4, 5, 6]])  # Shape (2, 3)
b = np.array([10, 20, 30])              # Shape (3,)
print("Array a:\n", a)
print("Array b:\n", b)  
# Broadcasting b to match the shape of a
c = a + b  # b is broadcasted to shape (2, 3)   
print("Broadcasted addition (a + b):\n", c)
# Original arrays
d = np.array([[1], [2], [3]])  # Shape (3, 1)
e = np.array([10, 20, 30])     # Shape (3,)
print("Array d:\n", d)
print("Array e:\n", e)
# Broadcasting e to match the shape of d
f = d + e  # e is broadcasted to shape (3, 3)
print("Broadcasted addition (d + e):\n", f)