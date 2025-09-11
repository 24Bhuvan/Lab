#Demonstration of Splitting numpy ndarrays
import numpy as np

# Original array
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

print("Original array:\n", a)

# 1. Split into 2 parts along rows (axis=0)
split_rows = np.array_split(a, 2, axis=0)
print("\nSplit into 2 along rows:")
for i, part in enumerate(split_rows):
    print(f"Part {i}:\n{part}")

# 2. Split into 2 parts along columns (axis=1)
split_cols = np.array_split(a, 2, axis=1)
print("\nSplit into 2 along columns:")
for i, part in enumerate(split_cols):
    print(f"Part {i}:\n{part}")

# 3. hsplit (horizontal split, splits columns)
hsplit_array = np.hsplit(a, 2)
print("\nhsplit (split columns):")
for i, part in enumerate(hsplit_array):
    print(f"Part {i}:\n{part}")

# 4. vsplit (vertical split, splits rows)
vsplit_array = np.vsplit(a, 3)
print("\nvsplit (split rows):")
for i, part in enumerate(vsplit_array):
    print(f"Part {i}:\n{part}")
