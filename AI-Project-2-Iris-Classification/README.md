# AI Project 2: Data Classification Using AI

## Description
This project uses the Iris dataset to classify flowers into three species:
- Setosa
- Versicolor
- Virginica

It uses a **K-Nearest Neighbors (KNN)** machine learning model with `k=5`.
The data is split into 80% training data and 20% testing data. The project
scales the features and evaluates the model using accuracy, a confusion
matrix, precision, recall, and F1 score.

The program also predicts the species of a new flower sample.

## How to Run

### 1. Install the required packages
Open Command Prompt or the VS Code terminal in the project folder and run:

```bash
py -m pip install scikit-learn matplotlib
```

### 2. Run the Python program

```bash
py iris_classification.py
```

The program prints the dataset information, evaluation results, and a
prediction for a new flower sample. It also saves the confusion matrix as
`confusion_matrix.png` in the project folder.

## Dataset
The Iris dataset is included in scikit-learn. A separate dataset download
is not required.

## Model Details
- Algorithm: K-Nearest Neighbors (KNN)
- Number of neighbors: 5
- Training/testing split: 80% / 20%
- Evaluation: Accuracy, precision, recall, F1 score, and confusion matrix
