# Demonstration of numpy functions:
# Insert
# Append
# Delete

import numpy as np

# Sample array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Original array:\n", arr)

# -------------------------
# 1. Insert (add elements at specific positions)
print("\n1. Insert:")
# Insert 99 at index 1 (row-wise flattening by default)
inserted = np.insert(arr, 1, 99)
print("Insert 99 at index 1:", inserted)

# Insert along axis (e.g., insert column at position 1)
inserted_axis = np.insert(arr, 1, [9, 9], axis=1)
print("Insert column [9,9] at column index 1:\n", inserted_axis)

# -------------------------
# 2. Append (add elements at the end)
print("\n2. Append:")
appended = np.append(arr, [7, 8, 9])
print("Append [7,8,9]:", appended)

# Append row to 2D array
appended_row = np.append(arr, [[7, 8, 9]], axis=0)
print("Append row [7,8,9]:\n", appended_row)

# -------------------------
# 3. Delete (remove elements by index)
print("\n3. Delete:")
deleted = np.delete(arr, 1)  # delete element at index 1 (flattened)
print("Delete element at index 1:", deleted)

# Delete row
deleted_row = np.delete(arr, 0, axis=0)
print("Delete row 0:\n", deleted_row)

# Delete column
deleted_col = np.delete(arr, 1, axis=1)
print("Delete column 1:\n", deleted_col)
