#Demostration of various NumPy indexing and slicing techniques for ndarrays
import numpy as np 
# Original array
a = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Original array:\n", a)
# 1. Accessing a single element (row 1, column 2)   
elem = a[1, 2]  # Accessing element at 2nd row, 3rd column
print("Element at (1, 2):", elem)  # 60 
# 2. Accessing a full row (row 0)
row = a[0, :]  # Accessing the entire first row
print("First row:", row)  # [10 20 30]
# 3. Accessing a full column (column 1) 
col = a[:, 1]  # Accessing the entire second column
print("Second column:", col)  # [20 50 80]
# 4. Slicing a sub-array (rows 0-1, columns 1-2)
sub_array = a[0:2, 1:3]  # Slicing rows 0-1 and columns 1-2
print("Sub-array (0:2, 1:3):\n", sub_array)  # [[20 30] [50 60]]
# 5. Boolean indexing (elements greater than 50)    
bool_idx = a > 50  # Create a boolean mask
filtered_elems = a[bool_idx]  # Apply the mask to get elements > 50
print("Elements greater than 50:", filtered_elems)  # [60 70 80 90]
# 6. Fancy indexing (specific rows and columns)
rows = np.array([0, 2])  # Row indices  
cols = np.array([1, 2])  # Column indices
fancy_elems = a[rows[:, np.newaxis], cols]  # Fancy indexing
print("Fancy indexed elements:\n", fancy_elems)  # [[20 30] [80 90]]
# 7. Modifying elements (set elements in row 1 to 0)
a[1, :] = 0  # Set all elements in the second row to 0
print("Array after modifying row 1:\n", a)  # [[10 20 30] [ 0  0  0] [70 80 90]]