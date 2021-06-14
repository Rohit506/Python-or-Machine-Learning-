import numpy as np
import matplotlib.pyplot as plt

x= np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([4, 7, 9, 10, 13, 16, 17, 20, 21, 23])
n = len(x)
x_square = x*x          # Print the values of x square
xy = x*y                # Print the vaalues of x multiply y
print('x_square :', x_square)
print('xy :', xy)
sum_of_x = np.sum(x)        # sum of all x
sum_of_y = np.sum(y)        # sum of all y
sum_of_x_square = np.sum(x_square)      # sum of all x square values
sum_of_xy = np.sum(xy)                  # sum of all x*y
print('sum_of_x :', sum_of_x)
print('sum_of_y:', sum_of_y)
print('sum_of_x_square:', sum_of_x_square)
print('sum_of_xy:', sum_of_xy)

# Write Ordinary Square Formula
b0 = (sum_of_y*sum_of_x_square - sum_of_x*sum_of_xy)/(n*sum_of_x_square - sum_of_x*sum_of_x)
print('B0 :', b0)
b1 = (n*sum_of_xy - sum_of_x*sum_of_y)/(n*sum_of_x_square - sum_of_x*sum_of_x)
print('B1 :', b1)

# plot Graph
y_pred = b0 + b1*x
print('Predicted y:', y_pred)
plt.xlabel('Values of x')
plt.ylabel('values of y')
plt.xticks(np.arange(1, 11))
plt.yticks(np.arange(1, 27, 2))
plt.plot(x, y, marker='o', color='r')
plt.plot(x, y_pred, "g--")
plt.grid(True)
plt.show()

a = eval(input("Enter a nuber to predict :"))
predicted_y = b0 - b1*a
print("Predicted Values :", predicted_y)