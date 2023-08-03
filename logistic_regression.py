# -*- coding: utf-8 -*-
"""Logistic Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O8dj_qCZgB3ixXyVJUbHRMX0FCixx-Y7
"""

#Binary Classification (YES/NO)
from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
from matplotlib import pyplot as plt
# %matplotlib inline

df=pd.read_csv('/content/drive/MyDrive/ML Projects/insurance_data.csv')
df.head()

plt.scatter(df.age,df.bought_insurance,marker='*',color='red')
#connection graph -> sigmoid function

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test=train_test_split(df[['age']],df.bought_insurance,test_size=0.1)

x_test

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(x_train,y_train)

model.predict(x_test)

model.score(x_test,y_test)
#efficiency of our code
#We have considered small data set so accuracy is 100%
#might fall some point if case of large data ser

model.predict_proba(x_test)
#probablitiy that person will buy insurance or not

model.predict([[56]])