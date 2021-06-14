import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

primeminister = ["J.L.Nehru", "L.B.Shastri", "M.Singh", "N.Modi"]
working_year = [15, 1, 10, 6]
y_pos = np.arange(len(primeminister))
ax.barh(y_pos, working_year)
plt.show()