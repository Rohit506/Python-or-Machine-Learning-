import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
x = np.array([2, 4, 6, 1, 5, 6, 3, 5, 6, 4, 5, 7, 4, 9])
y = np.array([5, 5, 1, 8, 5, 1, 7, 6, 8, 2, 1, 5, 3, 4])
z = np.array([8, 3, 7, 5, 6, 3, 7, 5, 7, 3, 5, 6, 4, 7])
ax.scatter(x, y, z)
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
plt.show()
