# Demonstration of various NumPy data types
import numpy as np

# 1. 'i' → signed integer
a = np.array([1, -2, 3], dtype='i')
print("int (i):", a, a.dtype)

# 2. 'b' → boolean
b = np.array([True, False, 1, 0], dtype='b')
print("bool (b):", b, b.dtype)

# 3. 'u' → unsigned integer (only positive)
c = np.array([1, 2, 3], dtype='u1')  # 'u1' = unsigned int 8-bit
print("unsigned int (u):", c, c.dtype)

# 4. 'f' → float
d = np.array([1.2, 3.4, 5.6], dtype='f')
print("float (f):", d, d.dtype)

# 5. 'c' → complex float
e = np.array([1+2j, 3+4j], dtype='c')
print("complex (c):", e, e.dtype)

# 6. 'm' → timedelta (time difference)
f = np.array([1, 2, 3], dtype='m8[D]')  # days
print("timedelta (m):", f, f.dtype)

# 7. 'M' → datetime
g = np.array(['2025-09-08', '2025-09-09'], dtype='M8[D]')
print("datetime (M):", g, g.dtype)

# 8. 'O' → object (generic Python objects)
h = np.array([{"a": 1}, [1,2,3], "hello"], dtype='O')
print("object (O):", h, h.dtype)

# 9. 'S' → string (ASCII, fixed-length)
i = np.array([b"hi", b"hello"], dtype='S5')
print("string (S):", i, i.dtype)

# 10. 'U' → Unicode string (fixed-length)
j = np.array(["hi", "hello"], dtype='U5')
print("unicode string (U):", j, j.dtype)

# 11. 'V' → void (raw data, custom byte records)
k = np.array([(1, 2.0)], dtype='V16')  # raw 16-byte record
print("void (V):", k, k.dtype)
