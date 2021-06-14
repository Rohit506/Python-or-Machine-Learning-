import numpy as np
a = np.empty([3, 2], dtype='int32')
print(a)
x1 = np.zeros(5)
print(x1)
x2 = np.zeros(5, dtype='int8')
print('x2 =',x2)

x3 = np.zeros((3, 3), dtype='int8')
print('x3 =','\n', x3)

x3 = np.ones((3, 3), dtype='int8')
print('x3 =', '\n', x3)

x4 = np.full((3, 3), 5)
print('x4 =', '\n', x4)
print("*"*30)

x = np.eye(4)       # eye or identity are same
print(x)
print("*"*30)

x = np.identity(4)      # eye or identity are same
print(x)
print("*"*30)

x = np.eye(4, k=2)
print(x)
print("*"*30)

x = np.eye(4, k=3)
print(x)
print("*"*30)

x = np.eye(4, k=-2)
print(x)
print("*"*30)

x7 = np.diag([1, 2, 3, 4])
print(x7)