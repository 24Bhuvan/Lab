#Demonstration of copy and view in numpy ndarrays
import numpy as np
# Original array
a = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array:\n", a)
# Creating a copy of the array
b = a.copy()
# Creating a view of the array
c = a.view()
# Modifying the copy
b[0, 0] = 99
print("\nAfter modifying the copy (b):")
print("Copy (b):\n", b)  # b is modified
print("Original array (a):\n", a)  # a remains unchanged
# Modifying the view
c[0, 0] = 88
print("\nAfter modifying the view (c):")
print("View (c):\n", c)  # c is modified
print("Original array (a):\n", a)  # a is also modified
