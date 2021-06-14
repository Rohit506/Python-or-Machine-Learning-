# Statical Function

import numpy as np
x = np.array([1, 4, 5, 6, 2, 4, 6])
print(x.max())
print(x.min())
print(x.mean())
print(np.median(x))
print(x.std())
print("="*30)

angle = np.array([0, 30, 45, 60, 90])
angle_in_radian = np.radians(angle)     # Broadcasting rules
print(angle_in_radian)
print(np.sin(angle_in_radian))
print(np.cos(angle_in_radian))