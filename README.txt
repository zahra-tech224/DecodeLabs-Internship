AI PROJECT 2 — DATA CLASSIFICATION USING AI

WHAT THIS PROJECT DOES
- Loads the Iris dataset (150 samples, 4 measurements, 3 flower classes).
- Randomly shuffles and splits data into 80% training and 20% testing.
- Scales the features with StandardScaler.
- Trains a K-Nearest Neighbors (KNN) classifier with k=5.
- Evaluates predictions using accuracy, confusion matrix, precision, recall and F1 score.
- Predicts the class of one new flower sample.

HOW TO RUN (Windows)
1. Install Python 3 if it is not already installed.
2. Open Command Prompt in this folder.
3. Install required packages:
   py -m pip install scikit-learn matplotlib
4. Run:
   py iris_classification.py

The program prints the results and creates confusion_matrix.png in the same folder.
The Iris dataset is built into scikit-learn, so no separate CSV download is required.

EXPECTED RESULT FOR THE INCLUDED RANDOM SEED
- Training samples: 120
- Testing samples: 30
- Accuracy: 93.33%
- Macro F1 score: approximately 0.9327
Small differences can occur if you change the random seed or split.
