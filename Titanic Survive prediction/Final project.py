'''
Name : Rohit kumar
College : Rashtrakavi Ramdhari Singh Dinkar college of Engineering, Begusarai
Final Project : Titanic survival prediction
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
print(train)
print(test)

combined = pd.concat([ train, test ])
print(combined)

print(combined.describe())

x = sns.heatmap(combined.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show(x)

style =sns.set_style('whitegrid')
x1 = sns.countplot(x='Survived', data=combined, palette='RdBu_r')
plt.show(style)

sns.set_style('whitegrid')
plt.show(sns.countplot(x='Survived', hue='Sex', data=combined, palette='RdBu_r'))

sns.set_style('whitegrid')
plt.show(sns.countplot(x='Survived', hue='Pclass', data=combined, palette='rainbow'))

plt.show(sns.distplot(combined['Age'].dropna(), kde=False, color='darkred', bins=30))

plt.show(sns.countplot(x='SibSp',data=combined))

plt.show(combined['Fare'].hist(color='green',bins=40,figsize=(8,4)))

plt.show(sns.countplot(x='Embarked',data=combined))

plt.figure(figsize=(12, 7))
plt.show(sns.boxplot(x='Pclass',y='Age',data=combined,palette='winter'))


def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]

    if pd.isnull(Age):

        if Pclass == 1:
            return np.mean(combined[combined['Pclass'] == 1]['Age'])

        elif Pclass == 2:
            return np.mean(combined[combined['Pclass'] == 2]['Age'])

        else:
            return np.mean(combined[combined['Pclass'] == 3]['Age'])

    else:
        return Age

combined['Age'] = combined[['Age','Pclass']].apply(impute_age, axis=1)

combined.drop('Cabin', axis=1, inplace=True)

combined.fillna(value={'Embarked': 'S', 'Fare': np.mean(combined['Fare'])}, inplace=True)

print(combined.info())

sex = pd.get_dummies(combined['Sex'], drop_first=True)
embark = pd.get_dummies(combined['Embarked'], drop_first=True)
print(sex)
print(embark)

combined.drop(['Sex','Embarked','Name','Ticket'], axis=1, inplace=True)
combined = pd.concat([combined,sex,embark], axis=1)
print(combined)
print(combined.head())

cnull = sns.heatmap(combined.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show(cnull)

from sklearn.model_selection import train_test_split
train = combined[combined['Survived'].notnull()]
test = combined[combined['Survived'].isnull()]
test = test.drop('Survived', axis=1)

X_train, X_test, y_train, y_test = train_test_split(train.drop(['Survived', 'PassengerId'],axis=1),
                                                    train['Survived'], test_size=0.30)
from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
model = logmodel.fit(X_train,y_train)
print(model)

predictions = logmodel.predict(X_test).astype(int)
print(predictions)

from sklearn.metrics import classification_report
print(classification_report(y_test,predictions))