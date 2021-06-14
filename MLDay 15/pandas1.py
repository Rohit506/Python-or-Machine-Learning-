'''
working on 'Series' one of Data Structure of pandas
'Series' is used for 1D data
'''

import pandas as pd
import numpy as np
print(pd.__version__)
arr1 = np.array([1, 2, 3, 4,5])
x1 = pd.Series(arr1)        # 'S' is capital of Series data structure of pandas
print(x1)

arr2 = np.array([1, 2, 3.5, 5, 4, 5])       # if one element is in float then it print all data in flotting
x2 = pd.Series(arr2)
print(x2)

arr3 = np.array(['Anish', 'Rohit', 'Uttam', 'Lalit', 'Vivek'])
x3 = pd.Series(arr3)
print(x3)

arr4 = np.array(['Anish', 'Rohit', 'Uttam', 'Lalit', 'Vivek'])
x4 = pd.Series(arr3, index=np.arange(100, 105))     # modify index of data
print(x4)

arr5 = np.array(['Anish', 'Rohit', 'Uttam', 'Lalit', 'Vivek'])
x5 = pd.Series(arr3, index=np.array(['rank1', 'rank2', 'rank3', 'rank4', 'rank5']))     # modify index of data
print(x5)

dict = {1001: 'Rohit', 1002: 'Uttam', 1003: 'Anish', 1004: 'Lalit'}
x6 = pd.Series(dict)
print(x6)

x8 = pd.Series(50, index=['a', 'b', 'c'])
print(x8)

x7 = pd.Series([100, 200, 300, 400, 500], index=['a', 'b', 'c', 'd', 'e'])
print(x7)
print('x7[0]: ', x7[0])
print('x7[ :3] :', x7[:3])
print('x7[-3: ] :\n', x7[-3:])
print(x7['b'])

print(x7.mean())
print(x7.max())
print(x7.min())
print(x7.median())