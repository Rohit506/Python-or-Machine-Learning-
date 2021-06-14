'''
Plot Scatter values
'''
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
boys_marks = np.array([56, 58, 62, 76, 89, 65, 64, 73, 98, 51])
girls_marks = np.array([96, 99, 82, 76, 51, 76, 61, 76, 93, 88])
x = np.arange(10)
ax.scatter(x, boys_marks, color='g', marker='D', label='B_Marks')
ax.scatter(x, girls_marks, color='y', marker='*', label='G_Marks')
ax.set_xlabel("Roll Number")
ax.set_ylabel("Marks")
ax.legend(loc='upper center')
plt.show()
