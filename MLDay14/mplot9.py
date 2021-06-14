import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
angle = np.arange(0, 800, 4)
angle_in_radian = np.radians(angle)
z = np.linspace(-3, 3, 200)
a = z**2+1
x = a*np.sin(angle_in_radian)
y = a*np.cos(angle_in_radian)
ax.plot(x, y, z)
plt.show()