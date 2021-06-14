'''
  Plot multiple plot on plotting area
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(10)
y = x           # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y2 = x*2        # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
y3 = x**2       # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
y4 = x**3
plt.subplot(221, facecolor='r')     # 221 means 2 rows , 2 col, 1st graph
plt.plot(x, y)

plt.subplot(222)     # 222 means 2 rows , 2 col, 2nd graph
plt.plot(x, y2)

plt.subplot(223)
plt.plot(x, y3)

plt.subplot(224, facecolor='y')
plt.scatter(x, y4)
plt.show()