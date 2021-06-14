import matplotlib.pyplot as plt
import numpy as np
x = np.arange(10)
y = x**2
y2 = x**3
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax2 = fig.add_axes([0.4, 0.4, 0.5, 0.5])
ax1.plot(x, y)
ax2.plot(x, y2)
plt.show()