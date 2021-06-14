'''
Plot Horizontal bar
changing x-axis labels to y-axis labels
'''

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_axes([0.15, 0.1, 0.8, 0.8])

primeminister = ["J.L.Nehru", "L.B.Shastri", "M.Singh", "N.Modi"]
working_year = [15, 1, 10, 6]
y_pos = np.arange(len(primeminister))
ax.barh(y_pos, working_year, color='m')
ax.set_yticks(y_pos)
ax.invert_yaxis()       # invert the data of y-axis
ax.set_yticklabels(primeminister)
plt.show()