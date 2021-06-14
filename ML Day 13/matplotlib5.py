import matplotlib.pyplot as plt
import numpy as np

overs = ["0-10", "10-20", "20-30", "30-40", "40-50"]
indrun = [64, 48, 90, 110, 40]
ausrun = [20, 80, 70, 50, 90]
x = np.arange(5)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.bar(x-0.15, indrun, width=0.30, color="r", label="IND")
ax.bar(x+0.15, ausrun, width=0.30, color="y", label="AUS")
ax.set_title("IND vs AUS")
ax.set_xlabel("Overs------>")
ax.set_ylabel("Runs------->")
ax.set_xticks(x)
ax.set_yticks(np.arange(0, 121, 5))
ax.grid(True)
ax.set_xticklabels(overs)
plt.legend()
plt.show()
