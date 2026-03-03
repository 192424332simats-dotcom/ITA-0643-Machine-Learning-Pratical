# Implementation of K-Nearest Neighbours (KNN)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

# Create KNN model (k = 3)
knn = KNeighborsClassifier(n_neighbors=3)

# Train the model
knn.fit(X_train, y_train)

# Predict test data
y_pred = knn.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy of KNN:", accuracy)

# Predict a new sample
new_sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = knn.predict(new_sample)

print("New Sample Prediction:", iris.target_names[prediction][0])
