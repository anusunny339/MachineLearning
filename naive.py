import pandas as pd
import sklearn as sl

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import  accuracy_score
from sklearn.naive_bayes import GaussianNB

data=pd.read_csv("iris.csv")
x=data.iloc[:,:-1].values
y=data.iloc[:,4].values

data.head(5)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)
print(x)
print(y)

sc=StandardScaler()

x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

classifier=GaussianNB()
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)
print(y_pred)
cm=confusion_matrix(y_test,y_pred)

print("accuracy",accuracy_score(y_test,y_pred))
print("array",cm)

df=pd.DataFrame({'real':y_test,'pred':y_pred})
print(df)
