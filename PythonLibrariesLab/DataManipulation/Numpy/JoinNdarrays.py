# Demonstration of joining numpy ndarrays using concatenate and stack
import numpy as np

# Original arrays
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

print("Array a:\n", a)
print("Array b:\n", b)

# 1. Concatenate
concat_axis0 = np.concatenate((a, b), axis=0)  # along rows
concat_axis1 = np.concatenate((a, b), axis=1)  # along columns
print("\nConcatenate along axis 0:\n", concat_axis0)
print("\nConcatenate along axis 1:\n", concat_axis1)

# 2. Stack
stacked0 = np.stack((a, b))          # new axis 0
stacked1 = np.stack((a, b), axis=1)  # new axis 1
stacked2 = np.stack((a, b), axis=2)  # new axis 2
print("\nStack along new axis 0:\n", stacked0)
print("\nStack along axis 1:\n", stacked1)
print("\nStack along axis 2:\n", stacked2)

# 3. hstack (horizontal stack, axis=1)
hstacked = np.hstack((a, b))
print("\nhstack (horizontal stack):\n", hstacked)

# 4. vstack (vertical stack, axis=0)
vstacked = np.vstack((a, b))
print("\nvstack (vertical stack):\n", vstacked)

# 5. dstack (depth stack, axis=2)
dstacked = np.dstack((a, b))
print("\ndstack (depth stack):\n", dstacked)