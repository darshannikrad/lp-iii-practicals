"""
Practical B2: Spam Email Classification (KNN and SVM)
Group B: Machine Learning (ML)

Problem Statement:
Classify emails as spam (1) or not spam (0) using K-Nearest Neighbors (KNN)
and Support Vector Machine (SVM with linear kernel), and evaluate their classification performance.

Key Concepts & Viva Points:
- KNN: Instance-based "lazy learner". Does not learn an explicit model during training;
  classifies test instances based on majority vote of the k nearest neighbors.
- Curse of Dimensionality: In high dimensions (thousands of word counts), Euclidean distance
  becomes less discriminative, degrading KNN performance.
- SVM: Finds the optimal maximum-margin separating hyperplane between classes. Points closest
  to the hyperplane boundary are "support vectors".
- Linear Kernel: Suitable for text data because high-dimensional word feature spaces are often
  linearly or near-linearly separable.
- Confusion Matrix:
  - TP: Spam correctly identified.
  - TN: Legitimate mail correctly kept.
  - FP: Legitimate mail mistakenly labeled as spam (costliest error for users).
  - FN: Spam that slipped past the filter into inbox.

Execution:
  python3 B2_spam_classification.py
"""

import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# --- 1. Load Data (Fallback to synthetic word-count data if emails.csv is absent) ---
csv_path = "emails.csv"
if os.path.exists(csv_path):
    print(f"Loading '{csv_path}'...")
    df = pd.read_csv(csv_path)
else:
    print(f"'{csv_path}' not found. Generating sample word-count dataset for demonstration...")
    np.random.seed(42)
    n_samples, n_words = 600, 100
    word_cols = [f"word_{i}" for i in range(n_words)]
    X_synthetic = np.random.poisson(lam=1.5, size=(n_samples, n_words))
    # Synthetic label: high counts in certain words trigger spam
    y_synthetic = ((X_synthetic[:, :5].sum(axis=1) > 10)).astype(int)

    df = pd.DataFrame(X_synthetic, columns=word_cols)
    df.insert(0, "Email No.", [f"Email {i}" for i in range(n_samples)])
    df["Prediction"] = y_synthetic

# --- 2. Separate Features and Target ---
X = df.drop(columns=["Email No.", "Prediction"], errors="ignore")
y = df["Prediction"]

# --- 3. Split Dataset into 80% Train and 20% Test ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training samples: {X_train.shape[0]} | Testing samples: {X_test.shape[0]} | Features: {X_train.shape[1]}")

# --- 4. Train & Evaluate KNN and SVM ---
models = [
    ("K-Nearest Neighbors (k=5)", KNeighborsClassifier(n_neighbors=5)),
    ("Support Vector Machine (Linear SVM)", SVC(kernel="linear", random_state=42))
]

for name, model in models:
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    print("\n" + "=" * 60)
    print(f"Model: {name}")
    print("=" * 60)
    print(f"Accuracy: {accuracy_score(y_test, pred):.4f}")
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, pred))
    print("\nClassification Report:")
    print(classification_report(y_test, pred, target_names=["Not Spam (0)", "Spam (1)"]))

# Optional: evaluating different k values for KNN
print("\nOptional: Tuning k in KNN [1, 3, 5, 7, 9]:")
for k in [1, 3, 5, 7, 9]:
    m = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
    score = accuracy_score(y_test, m.predict(X_test))
    print(f"  k = {k}: Accuracy = {score:.4f}")

print("\nConclusion: Linear SVM typically outperforms KNN on high-dimensional text data,")
print("both in classification accuracy/F1-score and inference speed.")
