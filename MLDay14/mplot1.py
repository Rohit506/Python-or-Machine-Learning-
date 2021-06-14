import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])     # standard fig ploting place
x = np.arange(10)
boys_marks = np.array([56, 58, 62, 76, 89, 65, 64, 73, 98, 51])
girls_marks = np.array([96, 99, 82, 76, 51, 76, 61, 76, 93, 88])
ax.scatter(x, boys_marks, color ='y', marker ='D')
ax.scatter(x, girls_marks, color ='r', marker = '*')
ax.set_xlabel("Roll Number")
ax.set_ylabel("Marks")
plt.show()