
import pandas as pd
pd.set_option("display.max_columns", 15, "display.width", 1000)
from sklearn.datasets import load_boston
boston = load_boston()
x = boston.data
y = boston.target
print(x)
print(y)
columns = boston.feature_names
print(columns)
'''
CRIM--> per capita crime rate by town
ZN--> proportion of residential land zoned for lots over 25,000 sq.ft.
INDUS--> proportion of non-retail business acres per town
CHAS--> Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
NOX--> nitric oxides concentration (parts per 10 million)
RM--> average number of rooms per dwelling
AGE--> proportion of owner-occupied units built prior to 1940
DIS--> weighted distances to five Boston employment centres
RAD--> index of accessibility to radial highways
TAX--> full-value property-tax rate per $10,000
PTRATIO--> pupil-teacher ratio by town
B--> 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
LSTAT--> % lower status of the population
MEDV--> Median value of owner-occupied homes in $1000's
'''
boston_df =pd.DataFrame(boston.data)
print(boston_df.head())
boston_df.columns = boston.feature_names
print(boston_df.head())
import matplotlib.pyplot as plt
plt.boxplot(boston_df['CRIM'])
plt.show()