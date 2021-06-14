import pandas as pd
import numpy as np

student_data = {'Name': ['Suraj', 'Uttam', 'Anish', 'Rohit', 'Lalit', 'Shivam', 'Srikant', 'Aryan'],
                'Roll': [101, 102, 103, 104, 105, 106, 107, 108],
                'Marks': [56.5, 62.5, 68.8, 63.3, 65.5, 78.9, 80.9, 68.7],
                'Age': [30, 31, 34, 28, 19, 28, 31, 20],
                'Passing_Year': [2015, 2014, 2016, 2014, 2018, 2017, 2017, 2015],
                'Branch': ['CS', 'IT', 'IT', 'IT', 'CS', 'CS', 'IT', 'CS']
                }
df = pd.DataFrame(student_data)
print(df)

print(df.groupby('Passing_Year').groups)
print('='*50)
group1 = df.groupby('Passing_Year')
for name, data in group1:
    print(name)
    print(data)
print('='*50)

group2 = df.groupby('Branch')
for x, y in group2:
    print(x)
    print(y)
print('='*50)

data1 = {
    'Roll': [101, 102, 103, 104, 105, 106, 107, 108],
    'Name': ['Suraj', 'Uttam', 'Anish', 'Rohit', 'Lalit', 'Shivam', 'Srikant', 'Aryan'],
}
data2 = {
    'Roll': [101, 102, 103, 104, 105, 106, 107, 108],
    'Marks': [56.5, 62.5, 68.8, 63.3, 65.5, 78.9, 80.9, 68.7],
}
df3 = pd.DataFrame(data1)
df4 = pd.DataFrame(data2)
print(df3)
print(df4)
print('='*50)

df5 = df3.merge(df4, on='Roll')
print(df5)
df6 = df3.merge(df4, on='Roll', how='left')
print(df6)
df7 = df3.merge(df4, on='Roll', how='right')
print(df7)
df8 = df3.merge(df4, on='Roll', how='outer')
print(df8)

print(df8.isna())       # it returns 'True' or 'False' for nan value exist or not
print(df8['Name'].isna())
print(df8.fillna(0))
print(df8.fillna(method='ffill'))
print(df8.dropna())
print(df8.dropna(axis=1))
print(df8.isna().sum())