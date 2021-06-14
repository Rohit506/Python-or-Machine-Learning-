import matplotlib.pyplot as plt
import numpy as np
x = np.arange(10)
y = x**2
y2 = x**3
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.4, 0.4])
ax2 = fig.add_axes([0.5, 0.5, 0.4, 0.4])

ax1.set_title('SQUARE CURVE')
ax1.set_xlabel('Number')
ax1.set_ylabel('Square')

ax2.set_title('CUBE CURVE')
ax2.set_xlabel('Number')
ax2.set_ylabel('Cube')

ax1.plot(x, y)
ax2.plot(x, y2)
plt.show()