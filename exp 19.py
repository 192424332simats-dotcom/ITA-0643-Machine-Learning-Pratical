from sklearn.naive_bayes import GaussianNB

X=[[25,30000],[40,50000]]
y=[0,1]

model=GaussianNB()
model.fit(X,y)

print(model.predict([[30,40000]]))
