# ordinary Square formula using sklearn
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([4, 7, 9, 10, 13, 16, 17, 20, 21, 23])

print(x.shape, x.ndim)
x = x.reshape(-1, 1)  # -1 means numer of rows according to array data, and 1 means only one column
print(x)
y = y.reshape(-1, 1)
print(y)

from sklearn.linear_model import LinearRegression

model = LinearRegression()      # it isthe model or function
model.fit(x, y)
b0 = model.intercept_
b1 = model.coef_
print("B0 :", b0)
print("B1 :", b1)
y_pred = model.predict(x)
print("Predicted y :", y_pred)

# plot graph

plt.xticks(np.arange(1,11))
plt.yticks(np.arange(1,27))
plt.xlabel("x- values")
plt.ylabel("y-values")
plt.title("Predict with Sklearn")
plt.plot(x,y, marker="*", color="g", label="Actual y")
plt.plot(x,y_pred, marker="o", color="r", label="Predicted y")
plt.legend()            # legend is used to show the label on graph
plt.grid(True)
plt.show()

# if we want to predict custom

a = eval(input("Enter a unknown number: "))
predict_y = model.predict([[a]])
print("Predicted by Machine : ", predict_y)