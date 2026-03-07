from sklearn.tree import DecisionTreeClassifier

X=[[4,64],[6,128],[8,256]]
y=[1,2,3]

model=DecisionTreeClassifier()
model.fit(X,y)

print(model.predict([[6,128]]))
