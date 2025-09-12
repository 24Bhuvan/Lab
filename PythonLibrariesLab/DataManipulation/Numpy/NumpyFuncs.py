# Demonstration of important numpy functions
# Shuffle
# Unique
# Resize
# Flatten
# Ravel

import numpy as np

# Sample array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Original array:\n", arr)

# -------------------------
# 1. Shuffle (randomly permutes elements along an axis)
print("\n1. Shuffle:")
arr_copy = arr.copy()
np.random.shuffle(arr_copy)   # shuffles rows in-place
print(arr_copy)

# -------------------------
# 2. Unique (get unique elements)
print("\n2. Unique:")
arr2 = np.array([1, 2, 2, 3, 4, 4, 5])
print("Array:", arr2)
print("Unique elements:", np.unique(arr2))

# -------------------------
# 3. Resize (repeat/truncate to fit new shape)
print("\n3. Resize:")
print("Original:", arr2)
print("Resize to (3,3):\n", np.resize(arr2, (3, 3)))

# -------------------------
# 4. Flatten (convert to 1D copy)
print("\n4. Flatten:")
print("Flattened:", arr.flatten())

# -------------------------
# 5. Ravel (convert to 1D view if possible)
print("\n5. Ravel:")
r = arr.ravel()
print("Raveled:", r)
r[0] = 99   # since it's a view, it modifies original if contiguous
print("Modified ravel:", r)
print("Original after ravel modification:\n", arr)
