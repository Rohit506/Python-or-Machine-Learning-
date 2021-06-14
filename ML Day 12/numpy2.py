# Work on 3D Array

import numpy as np
x = np.arange(10)

print(x[::2])
print(x[2:7:2])

print("="*30)

x1 = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
'''
        11  12  13
        21  22  23
        31  32  33
'''

print(x1[0])
print(x1[1:])
print(x1[::2])

print("="*30)

print(x1[... , 1])      #for all row print the ement of column 1
print(x1[..., -1])      # here -1 means last column of an array
print(x1[1, ...])       # print column element of row 1
print(x1[:, 1:])        # for all rows print column 1 and 2's element
print("="*30)

y = np.arange(24).reshape(4, 2, 3)      # it means 4 matrix of 2x3
'''
    [[[ 0  1  2]
      [ 3  4  5]]
    
     [[ 6  7  8]
      [ 9 10 11]]
    
     [[12 13 14]
      [15 16 17]]
    
     [[18 19 20]
      [21 22 23]]]
  '''
print(y)
print()
print(y[0])
print("="*30)

print(y[1: 4, ..., 1])      # here 1:4 means matrix of index 1 to 3    or , for all rows print col. 1 element
