# Boxplot to find outliers

import matplotlib.pyplot as plt
import numpy as np
col1 = np.array([-5, 4, 5, 3, 2.3, 4.1, 5.4, -6, 3.6, 5.6, 12, 4.3, 4, 2, 5.1, 10])
col2 = np.array([-5, 4, 5, 13, 12.3, 14.1, 15.4, -6, 13.6, 15.6, 12, 14.3, 14, 12, 15.1, 30])
age = np.array([22, 21, 23, 25, 25, 21, -5, 33, 32, 70, 21, -1, 22, 23, 24])
data = [col1, col2, age]
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.boxplot(data)        # red line in boxplot is 'mean' of data
plt.show()