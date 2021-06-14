# Boxplot to find outliers

import matplotlib.pyplot as plt
import numpy as np
data1 = np.array([-5, 4, 5, 3, 2.3, 4.1, 5.4, -6, 3.6, 5.6, 12, 4.3, 4, 2, 5.1, 10])
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.boxplot(data1)
plt.show()