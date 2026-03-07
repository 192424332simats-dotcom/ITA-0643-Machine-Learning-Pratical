from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

data=load_iris()

model=KNeighborsClassifier()
model.fit(data.data,data.target)

print(model.predict([data.data[0]]))
