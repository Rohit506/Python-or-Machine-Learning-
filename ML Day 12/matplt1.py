
import matplotlib.pyplot as plt
import numpy as np
angle = np.arange(0, 800, 5)
sin_value = np.sin(np.radians(angle))
plt.plot(angle, sin_value, color='r')
plt.title("Sin curve")
plt.xlabel("sin angle")
plt.ylabel("sin value")
plt.show()