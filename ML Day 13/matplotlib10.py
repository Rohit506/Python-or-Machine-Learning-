# plotting histogram

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
marks = np.array([24, 33, 35, 36, 44, 48, 56, 57, 58, 67, 67, 56, 74, 72, 71, 59, 63, 80, 82, 87, 90])
bin = np.array([0, 25, 50, 75, 100])
ax.hist(marks, bin)
ax.set_xticks(bin)
ax.set_xlabel('Marks')
ax.set_ylabel('Students')
plt.show()