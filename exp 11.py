from sklearn.tree import DecisionTreeClassifier

X=[[25,50000],[40,60000]]
y=[0,1]

model=DecisionTreeClassifier()
model.fit(X,y)

print(model.predict([[30,55000]]))
