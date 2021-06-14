import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
def random_generator(n, start, end) :
    return (end-start)*np.random.rand(n) + start

fig = plt.figure()
ax = fig.gca(projection='3d')
xs = random_generator(20, 10, 20)
ys = random_generator(20, 20, 30)
#zs = random_generator(100, -4, 4)
z = 10
ax.bar(xs, ys, z)

xs1 = random_generator(20, 0, 10)
ys1 = random_generator(20, 100, 20)
#zs1 = random_generator(100, -8, 8)
z = 20
ax.bar(xs1, ys1, z)

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
plt.show()