import pandas as pd
import numpy as np

student_data = {'Name': ['Suraj', 'Uttam', 'Anish', 'Rohit', 'Lalit'],
                'Roll': [101, 102, 103, 104, 105],
                'Marks': [56.5, 62.5, 68.8, 63.3, 65.5],
                'Age': [30, 31, 34, 28, 19]
                }
df1 = pd.DataFrame(student_data)
print(df1)
print(df1.sort_index(ascending=False))
print(df1.sort_values(by='Name'))
#print(df1.sort_values(by='Mark', ascending=False), iloc[0])
#print(df1.sort_values(by=['Mark', 'Age']))
print(df1.sort_values(by='Marks', ascending=False).iloc[0].Name)