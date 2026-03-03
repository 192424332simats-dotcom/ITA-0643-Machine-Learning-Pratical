# Linear Regression Implementation

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample Dataset
# X = Years of Experience
# y = Salary
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([30000, 35000, 40000, 45000, 50000, 55000])

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Model parameters
print("Intercept (b0):", model.intercept_)
print("Slope (b1):", model.coef_[0])

# Evaluation
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("Mean Squared Error:", mse)
print("R2 Score:", r2)

# Plot the results
plt.scatter(X, y, color='blue', label="Actual Data")
plt.plot(X, y_pred, color='red', label="Regression Line")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression")
plt.legend()
plt.show()
