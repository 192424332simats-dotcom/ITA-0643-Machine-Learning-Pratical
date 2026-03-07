from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

data=load_iris()

model=GaussianNB()
model.fit(data.data,data.target)

print(model.predict([data.data[1]]))
