import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import numpy as np
import sklearn as sl
data=pd.read_csv("iris.csv")
x=data.iloc[:,:-1]
y=data.iloc[:,-1]

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
print(x)

from sklearn import metrics
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)
print(regressor.intercept_)
print(regressor.coef_)

y_pred=regressor.predict(x_test)

for (i,j) in zip(y_test,y_pred):
    if i!=j:
        print("act",i,"pred",j)
print("missmact",(y_test!=y_pred).sum())
print("mean ab err",metrics.mean_absolute_error(y_test,y_pred))
print("'mean sq",metrics.mean_squared_error(y_test,y_pred))
print("roor",np.sqrt(metrics.mean_squared_error(y_test,y_pred)))