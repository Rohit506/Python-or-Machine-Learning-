

import pandas as pd
df = pd.read_csv("50_Startups.csv")
print(df)

print("#"*100)

from sklearn.preprocessing import LabelEncoder
labelEncoder = LabelEncoder()
df2 = df
df2.State = labelEncoder.fit_transform(df2.State)
print(df2)

print("#"*100)

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder()
df3 = pd.DataFrame(ohe.fit_transform(df2[['State']]).toarray())
print(df3)

print("#"*100)

merge_data = pd.concat([df2, df3], axis=1)
print(merge_data)
print("#"*100)
merge_data.pop('State')
merge_data.pop(2)
print(merge_data)
print("#"*100)
df = merge_data.rename(columns={0: 'California', 1: 'Florida'})
print(df)
print("#"*100)
x = df.iloc[:, [0, 1, 2, 4, 5]].values
y = df.iloc[:, 3].values
print("Feature Data:\n", x)
print("#"*100)
print("Profit Data:\n", y)
print("#"*100)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=8)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
print("Values of b0, b1, b2, b4, b5:\n", model.coef_)
print("#"*100)
print("y intercept:\n", model.intercept_)
y_pred = model.predict(X_test)
#print(y_pred)
from sklearn.metrics import mean_absolute_error
print("Absolute Mean Error: ", mean_absolute_error(y_test, y_pred))
print("Accuracy %: ", model.score(x, y)*1100)
