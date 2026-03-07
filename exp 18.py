from sklearn.linear_model import Perceptron
from sklearn.datasets import load_iris

data=load_iris()

model=Perceptron()
model.fit(data.data,data.target)

print(model.predict([data.data[0]]))
