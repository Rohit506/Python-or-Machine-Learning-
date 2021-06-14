# Contour Graph
import matplotlib.pyplot as plt
import numpy as np
xlist = [1, 2, 3, 4, 5]
ylist = [3, 4, 2, 1, 6]

x, y = np.meshgrid(xlist, ylist)        # meshgrid converts array into square matrix
print(x)
print(y)
z = np.sqrt(x**2 + y**2)
a = plt.contourf(x, y, z)
plt.colorbar(a)
plt.show()