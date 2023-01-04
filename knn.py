import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn as sl

dataset=pd.read_csv("iris.csv")

X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,4].values


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20)

#from sklearn.model_selection import train_test_split
#X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20)
print(X)
print(y)

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=3)

#from sklearn.neighbors import KNeighborsClassifier
#classifier=KNeighborsClassifier(n_neighbors=3)

#classifier.fit(X_train,y_train)
#y_pred=classifier.predict(X_test)

classifier.fit(X_train, y_train)
y_pred=classifier.predict(X_test)


#from sklearn.metrics import confusion_matrix,classification_report

#print(classification_report(y_test,y_pred))


from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,y_pred))


