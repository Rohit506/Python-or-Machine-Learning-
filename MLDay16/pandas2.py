import pandas as pd
import numpy as np

student_data = {'Name': ['Suraj', 'Uttam', 'Anish', 'Rohit', 'Lalit'],
                'Roll': [101, 102, 103, 104, 105],
                'Marks': [56.5, 62.5, 68.8, 63.3, 65.5],
                'Age': [30, 31, 34, 28, 19]
                }
df1 = pd.DataFrame(student_data)
print(df1)

#df2 = df1.rename(columns={'Name':'Student_Name', 'Marks':'Percentage'},
                 #index={'rank1':0, 'rank2':1, 'rank3':3})
df2 = df1.rename(columns={'Name':'Student_Name', 'Marks':'Percentage'},
                 index={0:'rank1', 1:'rank2', 2:'rank3'})
print(df2)
print(df1)

df3 = df1.reindex(index=[0, 2, 4], columns=['Age', 'Roll', 'Name'])
print(df3)

df4 = pd.DataFrame(np.random.randn(7, 3), columns=['Col-1', 'Col-2', 'Col-3'])
print(df4)

df5 = pd.DataFrame(np.random.randn(10, 3), columns=['Col-1', 'Col-2', 'Col-3'])
print(df5)

df6 = df4.reindex_like(df5)
print(df6)