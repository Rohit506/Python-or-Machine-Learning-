import matplotlib.pyplot as plt
import numpy as np

overs = np.arange(11)
indrun = np.array([0, 5, 13, 20, 30, 38, 50, 63, 72, 86, 102])
ausrun = np.array([0, 10, 23, 30, 40, 58, 60, 63, 68, 74, 80])

fig = plt.figure()
plt.plot(overs, indrun, "b", linewidth=3, label="IND")
plt.plot(overs, ausrun, "y", linewidth=3, label="AUS")
plt.title("IND vs AUS T-20 MATCH")
plt.xlabel("Overs")
plt.ylabel("Runs")
plt.xticks(overs)
plt.yticks(np.arange(0,111,10))
plt.legend(loc = "best")
plt.show()

