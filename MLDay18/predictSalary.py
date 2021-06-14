'''
    Predict Salary According t0 their year Experience
    Mthod Using linear-Regression
'''
import pandas as pd

dataset = pd.read_csv("Salary_Data.csv")
print(dataset)
print(dataset.isna().sum())
print(dataset.describe())
x = dataset.iloc[ : , : -1].values
y = dataset.iloc[:, -1].values
print("Feature Data:",x)
print("Target Data:",y)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=1)
print("X_train: \n", X_train)
print("Y_train: \n", Y_train)
print("X_test: \n", X_test)
print("Y_test: \n", Y_test)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, Y_train)
predicted_y = model.predict(X_test)
print("y_intercept : ", model.intercept_)
print("Slope: ", model.coef_)
print("Accuracy: ", model.score(X_test, Y_test))

import matplotlib.pyplot as plt
plt.title("Predict Salary according to year experience")
plt.scatter(X_train, Y_train, color="g", marker="*", label="Training")
plt.scatter(X_test, Y_test, color="r", marker="o", label="Actual Data")
#plt.scatter(X_test, predicted_y, color="g", marker="x", label="Predicted Data")
#plt.scatter(x, y, color="y", marker="+", label="Original Data")
plt.plot(x, model.predict(x), label="Best Fit line")

plt.xlabel("Year of experiences")
plt.ylabel("Salary")
plt.legend()
plt.show()

a = eval(input("Enter a year of experience: "))
predicted_value = model.predict([[a]])
print("Predicted value for ", a, "year is ", predicted_value)
