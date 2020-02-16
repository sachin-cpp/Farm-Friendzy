# -*- coding: utf-8 -*-

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
plt.style.use('seaborn')

dataset=pd.read_csv('datasets/arcanut.csv')
dataset_2=pd.read_csv('datasets/complete.csv')
dataset_3=pd.read_csv('datasets/data.csv')

df = pd.DataFrame(dataset_2)
def fun(x):
    if x == 'Bajra':
        return 1
    if x == 'Banana':
        return 2

    if x == 'Bean':
        return 3
    if x == 'Black pepper':
        return 4
    if x == 'Blackgram':
        return 5
    if x == 'Brinjal':
        return 6
    if x == 'Cabbage':
        return 7
    if x == 'Cardamom':
        return 8
    if x == 'Carrot':
        return 9
   
df['fun'] = df['Crop'].apply(fun) 
df
    
    



X = dataset_2.iloc[:,[0,1,2,4]].values
Y = dataset_2.iloc[:,5].values
Z = dataset_3.iloc[:,:]

# Feature Scaling
#"""from sklearn.preprocessing import StandardScaler
#sc_X = StandardScaler()
#X_train = sc_X.fit_transform(X_train)
#X_test = sc_X.transform(X_test)
#sc_y = StandardScaler()
#y_train = sc_y.fit_transform(y_train.reshape(-1,1))"""


#regressor = LinearRegression()
#regressor.fit(X, Y)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, random_state = 0)

regressor = LinearRegression()

regressor.fit(X_train, Y_train)
#predecting test set results

Y_pred = regressor.predict(X_test)
# Visualising the Training set results
from sklearn.datasets import make_blobs
X, y = make_blobs(n_samples=300, centers=4,
                  random_state=0, cluster_std=1.0)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='rainbow');

y_pred_1 = dataset_2.iloc[:,3]

