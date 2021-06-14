import numpy as np
a = np.array([1, 2, 3, 4, 5])
print("arr1 =", a, type(a))
print("data type =", a.dtype)       # Integer of 32 bit or 4 byte

a = np.array([1, 2, 3, 4, 5], dtype='int8')
print(a, a.dtype)

arr2 = np.array([1.2, 3.4, 5, 6])
print(arr2, arr2.dtype)

arr2 = np.array([1.2, 3.4, 5, 6], dtype='int8')
print(arr2)

arr2 = np.array([129.2, 258.4, 5, 6], dtype='int8')     # result because of range of 8bit int is -128 to 127
print(arr2)

arr2 = np.array([129.2, 258.4, 5, 6], dtype='i1')       # i1 is sort form of int8
print(arr2)

# User Define Data type
student = np.dtype([('name', 'U16'), ('age', 'i1'), ('mark', 'f4')])    # U16 = u cand take 16 character and f4 = float of 32 bit
arr3 = np. array([('Rohit', 21, 322), ('Uttam', 23, 350), ('Anish', 20, 378)], dtype=student)
print(arr3)
print(arr3['name'])
print(arr3['age'])
print(arr3['mark'])