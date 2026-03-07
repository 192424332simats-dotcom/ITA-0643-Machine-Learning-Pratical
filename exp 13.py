from sklearn.linear_model import LinearRegression

X=[[1],[2],[3]]
y=[20000,30000,40000]

model=LinearRegression()
model.fit(X,y)

print(model.predict([[4]]))
