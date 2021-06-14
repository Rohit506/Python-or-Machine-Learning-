import numpy as np
y = np.arange(24)
y1 = y.reshape((6,4))       # multiply should be equal to given number
print(y1)
print("*"*30)
'''
y2 = y.reshape((2,3))
print(y2)          # it will print error
'''
y2 = y.reshape((-1,3))
print(y2)
print("*"*30)

y3 = y.reshape(3, -1)
print(y3)
print("*"*30)

y3 = np.resize(y,(4, 6))
print(y3)
print("*"*30)

y3 = np.resize(y,(5, 5))        # it repeate the element
print(y3)
print("*"*30)

y3 = np.resize(y,(5, 7))
print(y3)
print("*"*30)

x = np.array([[5, 8, 9, 5], [2, 4, 9, 4], [8, 3, 6, 4]])
print(x)
print(x.reshape((4, 3)))
print(np.resize(x, (5, 5)))