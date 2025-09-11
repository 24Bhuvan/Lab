#Demonstration of Search, Sorted Seach, Sort, Filter Functions in ndarrys
import numpy as np

# Original array
a = np.array([1, 3, 5, 7, 9])
print("Original array:", a)

# 1. searchsorted: Find indices where elements should be inserted to maintain order
indices = np.searchsorted(a, [2, 6, 8])
print("\nsearchsorted for [2,6,8]:", indices)
# Output: [1 3 4] → positions where 2,6,8 can be inserted

# 2. sort: Return a sorted copy of the array
unsorted = np.array([10, 2, 5, 7, 1])
sorted_array = np.sort(unsorted)
print("\nOriginal unsorted array:", unsorted)
print("Sorted array:", sorted_array)

# 3. Filtering: Get elements satisfying a condition
arr = np.array([1, 4, 6, 8, 3, 7])
filtered = arr[arr > 5]  # Elements greater than 5
print("\nOriginal array:", arr)
print("Filtered (arr > 5):", filtered)