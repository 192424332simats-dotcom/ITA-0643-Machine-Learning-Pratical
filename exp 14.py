from sklearn.linear_model import LinearRegression

X=[[1000],[1500],[2000]]
y=[3,4,5]

model=LinearRegression()
model.fit(X,y)

print(model.predict([[1800]]))
