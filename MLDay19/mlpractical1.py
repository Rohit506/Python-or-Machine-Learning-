

import numpy as np
import matplotlib.pyplot as plt
ran = np.random.RandomState(7)
x= 10* ran.randn(50)
print(x)
print("="*80)
y = 2*x+3 + ran.randn(50)
print(y)
y[10] = 150          # here are some outliers
y[5] = 110           # if outliers in the linearRegression
y[15] = 105          # then prediction is not accurate

plt.figure(1)
plt.boxplot(y)      # boxplot is used to find outliers
plt.figure(2)


plt.scatter(x, y)
plt.xlabel("x-values--------->>>")
plt.ylabel("y-values------->>>>")
#plt.show()

X = x.reshape(-1, 1)
Y = y.reshape(-1, 1)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, Y)
print("B0: ", model.intercept_)
print("B1: ", model.coef_)
y_pred = model.predict(X)

plt.plot(X, y_pred, color="r")
plt.show()