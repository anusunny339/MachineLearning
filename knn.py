import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sl

data=pd.read_csv("iris.csv")
x=data.iloc[:,:-1].values
y=data.iloc[:,4].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)
print("x:",x)
print("\ny:",y)

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)

from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
print("matrix",confusion_matrix(y_test,y_pred))
print("\n Classification Report",classification_report(y_test,y_pred))
print("\naccuracy:",accuracy_score(y_test,y_pred))

