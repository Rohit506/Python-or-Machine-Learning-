import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
def random_generator(n, start, end) :
    return (end-start)*np.random.rand(n) + start

fig = plt.figure()
ax = fig.gca(projection='3d')
xs = random_generator(100, 10, 20)
ys = random_generator(100, 20, 30)
zs = random_generator(100, -4, 4)
ax.bar(xs, ys, zs)

xs1 = random_generator(100, 0, 10)
ys1 = random_generator(100, 100, 20)
zs1 = random_generator(100, -8, 8)
ax.bar(xs1, ys1, zs1)

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
plt.show()