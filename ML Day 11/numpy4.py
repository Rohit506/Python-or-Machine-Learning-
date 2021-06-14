import numpy as np
a = np.array([[1, 2, 3],[5, 6, 7], [10, 11, 12]])
print(a)
print(a.flatten())      # it covert in 1D array
print(a.flatten(order='F'))     # it prints matrix in column bias
# order = c (print array in row bias by default)
# order = f (print array in column bias not by default)
print (a)
y = np.ravel(a)
print(y)
x1 = np.ravel(a, order='F')     # flatten or ravel are same only syntax are differ
print(x1)

x = np.arange(8)
print(x)
x1 = x.reshape((2, 4))
print(x1)

x1 = x.reshape((2, 4), order='F')
print(x1)
x1 = x.reshape((4, 2))
print(x1)

x1 = x.reshape((2, 2, 2))       # 3D matrix (2 matrix of 2x2)
print(x1)


