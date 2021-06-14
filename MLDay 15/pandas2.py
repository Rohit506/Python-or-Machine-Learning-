'''
Working on 'DataFrame'
Which is used for 2D data
It print 'index' or 'column' of data by default
'''

import pandas as pd
import numpy as np
df1 = pd.DataFrame()
print(df1)
print(type(df1))

df2 = pd.DataFrame([1, 2, 3, 4, 5])
print(df2)
print('*'*50)

cricket_data = [['Virat Kohli', 13000], ['Rohit Sharma', 9500], ['Sachine Tendulkar', 18500], ['Yuvraj Singh', 10500], ['M S Dhoni', 12000]]
df3 = pd.DataFrame(cricket_data)
print(pd.DataFrame(cricket_data))
print('*'*50)

df4 = pd.DataFrame(cricket_data, columns=['BATSMAN', 'ODI RUNS'])       # modify columns name
print(df4)
print('*'*50)

student_data = {'Name': ['Suraj', 'Uttam', 'Anish', 'Rohit', 'Lalit'],
                'Roll': [101, 102, 103, 104, 105],
                'Marks': [56.5, 62.5, 68.8, 63.3, 65.5],
                'Age': [30, 31, 34, 28, 19]
                }
df5 = pd.DataFrame(student_data)
print(df5)
print('*'*50)
df6 = pd.DataFrame(student_data, index=['rank1', 'rank2', 'rank3', 'rank4', 'rank5'])
print(df6)
print('*'*50)

data = {'Mark1': pd.Series([60, 70, 80], index=['Suraj', 'Uttam', 'Anish']),
        'Mark2': pd.Series([60, 70, 80, 65], index=['Suraj', 'Uttam', 'Lalit', 'Anish'])
        }
df7 = pd.DataFrame(data)
print(df7)

df7['Mark3'] = pd.Series([50, 60, 60, 55], index=['Suraj', 'Uttam', 'Lalit', 'Anish'])
print(df7)

df7['Total'] = df7['Mark1']+ df7['Mark2']+df7['Mark3']
print(df7)
print('='*50)

print(df7['Mark1'])

#del df7['Mark1']
#print('After Deletion Mark1 Column :')
#print(df7)
'''
if we write index name then use 'loc' method
when we erite numeric index then use 'iloc' method
'''

print(df7.loc['Lalit'])
print(df7.iloc[1])
print('='*50)
print(df7.iloc[1:3])

df8 = pd.DataFrame([[40, 50, 60, 120], [50, 45, 35, 130], [60, 58, 62, 180]],
                   columns=['Mark1', 'Mark2', 'Mark3', 'Total'],
                   index=['Deepak', 'Alok', 'Anup'])
print(df8)
print(df7)

df7 = df7.append(df8)
print(df7)

# Column Deletion
#del df7['Mark1']        # Ther is two way to delete column, using 'del' or 'df7.pop('Mark1')'
#print("After Deletion :")
#print(df7)

# Row Deletion
#df7 = df7.drop('Lalit')
#print(df7)

# Slicing
print(df7.loc[:, :])        # It prints all rows and all columns
print('='*50)
print(df7.loc[['Anish', 'Lalit'], : ])

print(df7.loc['Lalit':'Alok', : ])
print('='*50)
print(df7.loc['Lalit':'Alok', 'Mark1':'Mark3'])
print('='*50)

# Here we can do the sam thing using 'iloc'
print(df7.iloc[:, :])       # iloc take index number as values
print(df7.iloc[2:7,2:4 ])
print(df7.iloc[:, -1:])
print('='*50)

print(df7.at['Alok', 'Mark1'])

