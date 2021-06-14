import matplotlib.pyplot as plt
import numpy as np
batch = ["ML", "Java", "Python", "C", "C++"]
no_of_student = [92, 360, 300, 150, 50]

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

ax.set_yticks(np.arange(0, 401, 20))
plt.bar(batch, no_of_student, color="r")
plt.show()