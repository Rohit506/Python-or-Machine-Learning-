# numpy attributes
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])    # 2D array
print(a)
print('a.shape =', a.shape)             # it shows the no. of rows and column
print('a.ndim =', a.ndim)               # it print number of dimension
print('a.dtype =', a.dtype)
print('a.itemsize =', a.itemsize)       # it shows size of element in byte form
print('a.size =', a.size)               # it print number of element in array
print("*"*50)

b = np.array([[1, 2, 3],[4, 5]])
print(b, type(b))
print('b.shape =', b.shape)             # it will print number of rows in tuples form
print('b.ndim =', b.ndim)               # it print number of dimension
print('b.dtype =', b.dtype)
print('b.itemsize =', b.itemsize)       # it shows size of element in byte form
print('b.size =', b.size)
