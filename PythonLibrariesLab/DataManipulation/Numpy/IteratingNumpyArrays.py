#Demonstration of iterating through numpy arrays using nditer and ndenumerate
import numpy as np     
# Original array
a = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array:\n", a)
# 1. Using nditer to iterate through each element
print("Iterating using nditer:")
for x in np.nditer(a):
    print(x, end=' ')  # Output: 1 2 3 4 5 6   
print()  # For newline
# 2. Using ndenumerate to get both index and value  
print("Iterating using ndenumerate:")
for index, x in np.ndenumerate(a):
    print(f"Index: {index}, Value: {x}")  # Output: Index: (0, 0), Value: 1 ... Index: (1, 2), Value: 6