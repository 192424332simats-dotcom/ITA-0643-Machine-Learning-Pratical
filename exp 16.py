from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

data=load_iris()

knn=KNeighborsClassifier().fit(data.data,data.target)
dt=DecisionTreeClassifier().fit(data.data,data.target)

print(knn.score(data.data,data.target))
print(dt.score(data.data,data.target))
