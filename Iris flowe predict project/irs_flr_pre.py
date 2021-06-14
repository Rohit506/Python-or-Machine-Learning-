import numpy as np
import pandas as pd

# Load Dataset
dataset = pd.read_csv("Iris.csv")
dataset.pop("Id")
print(dataset)
print(dataset.shape)
print(dataset.head(20))
print(dataset.describe())
print(dataset.groupby('Species').size())

import matplotlib.pyplot as plt
dataset.hist()
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


all_inputs = dataset[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values
all_classes = dataset['Species'].values

(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=1)

dtc = DecisionTreeClassifier()
print(dtc.fit(train_inputs, train_classes))
print(dtc.score(test_inputs, test_classes))