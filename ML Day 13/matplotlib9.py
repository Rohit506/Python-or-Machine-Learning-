import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
activity = ['Sleep', 'Play', 'Study', 'Social Network', 'Others']
hrs = [6, 2, 2, 10, 4]
ax.pie(hrs, labels=activity, autopct='%2.2f%%', colors=['b', 'g', 'y', 'm', 'r'], counterclock= False)
plt.show()