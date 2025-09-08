# Demonstration of various NumPy random number generation functions
import numpy as np

# 1. np.random.rand(d0, d1, …, dn)
# Generates random numbers in [0,1) with a uniform distribution
a = np.random.rand(2, 3)  
print("rand:\n", a)

# 2. np.random.randn(d0, d1, …, dn)
# Generates random numbers from a standard normal distribution (mean=0, std=1)
b = np.random.randn(2, 3)  
print("randn:\n", b)

# 3. np.random.ranf(size)
# Generates random floats in [0,1) (same as np.random.random)
c = np.random.ranf(5)  
print("ranf:\n", c)

# 4. np.random.randint(low, high=None, size=None, dtype=int)
# Generates random integers from low (inclusive) to high (exclusive)
d = np.random.randint(1, 10, size=(2, 3))  
print("randint:\n", d)
