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
df.to_csv("Student.csv")
df.to_csv('Student2.csv', index=None)
print("Data Converted in csv sucessfully!")