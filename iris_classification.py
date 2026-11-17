"""
AI Project 2: Data Classification Using AI
Dataset: Iris (150 samples, 4 features, 3 classes)
Algorithm: K-Nearest Neighbors (KNN), k=5
"""

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score, confusion_matrix, ConfusionMatrixDisplay,
    classification_report, f1_score
)

# 1. Load and understand the dataset
iris = load_iris()
X = iris.data
y = iris.target

print("DATASET INFORMATION")
print("-------------------")
print("Number of samples:", X.shape[0])
print("Number of features:", X.shape[1])
print("Classes:", list(iris.target_names))
print("Feature names:", list(iris.feature_names))
print("First five rows:\n", X[:5])

# 2. Split data into training and testing sets (80% / 20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42,
    stratify=y,
    shuffle=True
)

print("\nDATA SPLIT")
print("----------")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# 3. Feature scaling
# Fit the scaler only on training data to avoid data leakage.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Create and train the KNN classification model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)

# 5. Make predictions on unseen test data
y_pred = model.predict(X_test_scaled)

# 6. Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
macro_f1 = f1_score(y_test, y_pred, average="macro")
cm = confusion_matrix(y_test, y_pred)

print("\nMODEL EVALUATION")
print("----------------")
print(f"Accuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)")
print(f"Macro F1 Score: {macro_f1:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
print("Confusion Matrix:")
print(cm)

# 7. Save a confusion matrix image for project evidence
display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)
display.plot(cmap="Blues", values_format="d")
plt.title("Iris Classification - KNN Confusion Matrix")
plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=200)
plt.show()

# 8. Predict the class of a new flower sample
# Order: sepal length, sepal width, petal length, petal width (cm)
new_flower = [[5.1, 3.5, 1.4, 0.2]]
new_flower_scaled = scaler.transform(new_flower)
prediction = model.predict(new_flower_scaled)[0]
print("\nNEW FLOWER PREDICTION")
print("---------------------")
print("Input measurements:", new_flower[0])
print("Predicted Iris class:", iris.target_names[prediction])
