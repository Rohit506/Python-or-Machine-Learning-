# Data VIsualization
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(10)
y = x*x
print(x)
print(y)
plt.plot(x,y)
plt.title("My First graph")
plt.xlabel("Number")
plt.ylabel("square of Number")
plt.show()