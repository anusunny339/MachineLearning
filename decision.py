import pandas as pd
import sklearn as sl

from sklearn.model_selection import train_test_split
from sklearn import metrics,tree
from sklearn.metrics import confusion_matrix
from sklearn.metrics import  accuracy_score

data=pd.read_csv('iris.csv',names=['Virginica','Versicolor','Setosa','class'])

print(data.head())
data.info()

data['class'],class_names=pd.factorize(data['class'])
print(class_names)
print(data['class'].unique())

data['Virginica'],_=pd.factorize(data['Virginica'])
data['Versicolor'],_=pd.factorize(data['Versicolor'])
data['Setosa'],_=pd.factorize(data['Setosa'])

print(data.head())

x=data.iloc[:,:-1]
y=data.iloc[:,-1]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=0)
dtree=tree.DecisionTreeClassifier(criterion='entropy',max_depth=3,random_state=0)

dtree.fit(x_train,y_train)


y_pred=dtree.predict(x_test)

count_miss=(y_test!=y_pred).sum()
print("miss{}".format(count_miss))

print("accu",accuracy_score(y_test,y_pred))