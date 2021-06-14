'''
50_startup_data.csv
Predict Profit using Multiple linearRegression
working on this
'''
import pandas as pd
pd.set_option('display.max_column', 10, 'display.width', 1000)
df = pd.read_csv("50_Startups.csv")
print(df)
dummies_data = pd.get_dummies(df.State)
print(dummies_data)

merge_data = pd.concat([df, dummies_data], axis=1)
print(merge_data)

merge_data.pop('State')
print(merge_data)
merge_data.pop('New York')
print(merge_data)

x = merge_data.iloc[:,:-3]
print(x)