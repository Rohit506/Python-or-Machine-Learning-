import matplotlib.pyplot as plt
import numpy as np

overs = np.arange(11)
indrun = np.array([0, 5, 13, 20, 30, 38, 50, 63, 72, 86, 102])
ausrun = np.array([0, 10, 23, 30, 40, 58, 60, 63, 68, 74, 80])

fig = plt.figure()

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])     # this is standard location of plotting
# define location for plot figure by changing their variables

ax.plot(overs, indrun, "b", linewidth=3, label="IND")
ax.plot(overs, ausrun, "y", linewidth=3, label="AUS")
ax.set_title("IND vs AUS T-20 MATCH")
ax.set_xlabel("Overs")
ax.set_ylabel("Runs")
ax.set_xticks(overs)
ax.set_yticks(np.arange(0,111,10))
ax.legend()
plt.show()