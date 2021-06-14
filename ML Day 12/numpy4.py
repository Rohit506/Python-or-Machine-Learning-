
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [10, 11, 12]])
print(a)
print()

b = np.array([[10, 20, 30], [14, 15, 16], [1, 2, 3]])
print(b)
print()

print(a+b)
print()

print(a-b)
print()

print(a*b)      # it only multiply two element of array not a matrix multipication
print()

print(a.sum())
print()

print(a.sum(axis=0))        # print sum of column bias
print(a.sum(axis=1))        # print sum of row bias
print()

arr = np.array([10, 8, 9, 15, 12, 19, 13])
print(np.sort(arr))       # it will sort the element in increasing order
print(arr.argsort())    # it will print the index of sorted element
x = np.argsort(arr)
print()
print("largest element :", arr[x[len(x)-1]])
print("smallest element :", arr[x[0]])