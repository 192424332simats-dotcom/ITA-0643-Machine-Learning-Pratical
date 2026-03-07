from sklearn.linear_model import LinearRegression

X=[[1],[2],[3]]
y=[2,4,6]

model=LinearRegression()
model.fit(X,y)

print(model.predict([[4]]))
