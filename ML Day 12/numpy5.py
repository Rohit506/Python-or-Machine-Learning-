
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 7], [10, 11, 12]])
print(a)
print()

b = np.array([[10, 20, 6], [14, 45, 16], [1, 2, 3]])
print(b)
print()
print(np.linalg.det(b))
print()
print(np.matmul(a, b))

x1 = np.linalg.inv(a)
print(x1)
print()
print(np.dot(a, x1))
print()

# Solve equations
a1 = np.array([[1, 2], [2, 3]])
a2 = np.array([5, 8])
res = np.linalg.solve(a1, a2)
print(res)
print()

a1 = np.array([[1, 2, 1], [2, 3, 2], [1, 1, 2]])
a2 = np.array([8, 14, 9])
res = np.linalg.solve(a1, a2)
print(res)

a = np.array([[1, 2, 3], [4, 5, 7], [10, 11, 12]])
print(a)
print(a.T)
print()
print(a)
print(np.fliplr(a))
print(np.flipud(a))
print(np.flip(a))