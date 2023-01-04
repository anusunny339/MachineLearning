import pandas as pd
import  sklearn as sl
import matplotlib.pyplot as plt

data=pd.read_csv("iris.csv")
points=data.iloc[:,3:5].values
x=points[:,0]
y=points[:,-1]

plt.scatter(x,y,s=50,alpha=0.7)
plt.xlabel("annula")
plt.ylabel("spend")
#plt.show()

from sklearn.cluster import KMeans

kmeans=KMeans(n_clusters=6,random_state=0)
kmeans.fit(points)

pred_clu=kmeans.predict(points)

plt.scatter(x,y,c=pred_clu,s=50,alpha=0.7,cmap='viridis')
centers=kmeans.cluster_centers_
plt.scatter(centers[:0],centers[:,0],centers[:,1],s=100,c='red')
plt.show()



