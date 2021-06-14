'''
  Plot multiple plot on plotting area
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(10)
y = x**2
y2 = x**3
plt.subplot(211, facecolor='r')
plt.plot(x, y)
plt.subplot(212, facecolor='y')
plt.plot(x, y2)
plt.show()