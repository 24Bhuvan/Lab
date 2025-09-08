# Demonstration of various NumPy ufunc arithmetic operations
import numpy as np

x = np.array([10, 20, 30])
y = np.array([1, 2, 3])

# 1. np.add → element-wise addition
print("add:", np.add(x, y))       # [11 22 33]

# 2. np.subtract → element-wise subtraction
print("subtract:", np.subtract(x, y))  # [ 9 18 27]

# 3. np.multiply → element-wise multiplication
print("multiply:", np.multiply(x, y))  # [10 40 90]

# 4. np.divide → element-wise division (float result)
print("divide:", np.divide(x, y))  # [10. 10. 10.]

# 5. np.mod → element-wise remainder
print("mod:", np.mod(x, y))        # [0 0 0]

# 6. np.power → element-wise power (x^y)
print("power:", np.power(x, y))    # [  10  400 27000]

# 7. np.reciprocal → reciprocal (1/x)
z = np.array([1, 2, 0.5])
print("reciprocal:", np.reciprocal(z))  # [1.  0.5 2.]
