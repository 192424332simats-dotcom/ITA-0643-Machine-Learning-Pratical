from sklearn.neural_network import MLPClassifier

X=[[0,0],[0,1],[1,0],[1,1]]
y=[0,1,1,0]

model=MLPClassifier(max_iter=1000)
model.fit(X,y)

print(model.predict([[1,0]]))
