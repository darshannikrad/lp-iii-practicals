"""
Practical B3: Bank Customer Churn Prediction with an Artificial Neural Network
Group B: Machine Learning (ML)

Problem Statement:
Build an Artificial Neural Network (ANN) classifier to predict whether a bank customer
will churn (leave the bank within six months).
Tasks:
1. Load and clean dataset (drop identifiers: RowNumber, CustomerId, Surname).
2. One-hot encode categorical features (Geography, Gender) with drop_first=True.
3. Split into 80% train and 20% test sets.
4. Normalize features using StandardScaler (fit on train, transform on test to prevent data leakage).
5. Train a Multilayer Perceptron (MLP) neural network.
6. Evaluate accuracy, confusion matrix, and classification report.

Key Concepts & Viva Points:
- Dummy Variable Trap: When one-hot encoding columns, keeping all levels introduces collinearity.
  drop_first=True prevents this redundancy.
- Data Leakage: Scaler must be fit ONLY on training data, then applied to test data.
- StandardScaler: Shifts mean to 0 and scaling variance to 1, ensuring high-magnitude features
  (e.g., Balance up to $250,000) do not dominate smaller features (e.g., Age 18-90).
- Activation Functions:
  - ReLU (Rectified Linear Unit): f(x) = max(0, x), used in hidden layers to introduce non-linearity
    and prevent vanishing gradients.
  - Sigmoid: f(x) = 1 / (1 + e^-x), used at output to yield probability in [0, 1].
- Class Imbalance: Churn datasets are typically ~80% stay and ~20% churn; accuracy alone can be
  misleading, so confusion matrix, precision, and recall are critical.

Execution:
  python3 B3_churn_neural_network.py
"""

import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# --- 1. Load Data (Fallback to synthetic dataset if Churn_Modelling.csv is absent) ---
csv_path = "Churn_Modelling.csv"
if os.path.exists(csv_path):
    print(f"Loading '{csv_path}'...")
    df = pd.read_csv(csv_path)
else:
    print(f"'{csv_path}' not found. Generating sample churn dataset for demonstration...")
    np.random.seed(42)
    n = 1000
    df = pd.DataFrame({
        "RowNumber": range(1, n + 1),
        "CustomerId": np.random.randint(15000000, 16000000, n),
        "Surname": [f"User_{i}" for i in range(n)],
        "CreditScore": np.random.randint(350, 850, n),
        "Geography": np.random.choice(["France", "Spain", "Germany"], n),
        "Gender": np.random.choice(["Male", "Female"], n),
        "Age": np.random.randint(18, 75, n),
        "Tenure": np.random.randint(0, 11, n),
        "Balance": np.random.uniform(0, 200000, n),
        "NumOfProducts": np.random.randint(1, 5, n),
        "HasCrCard": np.random.choice([0, 1], n),
        "IsActiveMember": np.random.choice([0, 1], n),
        "EstimatedSalary": np.random.uniform(20000, 180000, n),
    })
    # Realistic churn correlation: higher age, lower active status increases churn probability
    prob = 0.2 + (df["Age"] > 45) * 0.3 - (df["IsActiveMember"] == 1) * 0.15
    prob = np.clip(prob, 0.05, 0.95)
    df["Exited"] = (np.random.rand(n) < prob).astype(int)

# --- 2. Preprocessing & Feature Engineering ---
# Drop identifier columns with no predictive power
df = df.drop(columns=["RowNumber", "CustomerId", "Surname"], errors="ignore")

# One-hot encode categorical features (drop_first=True avoids dummy variable trap)
df = pd.get_dummies(df, columns=["Geography", "Gender"], drop_first=True)

# Separate features (X) and target (y)
X = df.drop(columns=["Exited"])
y = df["Exited"]

# --- 3. Train-Test Split (80% / 20%) ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- 4. Feature Scaling (StandardScaler) ---
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# --- 5. Train Neural Network (MLPClassifier) ---
# Architecture: Input (features) -> Hidden 1 (16 neurons, ReLU) -> Hidden 2 (8 neurons, ReLU) -> Output
model = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation="relu",
    solver="adam",
    max_iter=300,
    random_state=42
)
model.fit(X_train, y_train)

# --- 6. Prediction and Evaluation ---
pred = model.predict(X_test)

print("\n" + "=" * 60)
print("Artificial Neural Network Evaluation")
print("=" * 60)
print(f"Accuracy: {accuracy_score(y_test, pred):.4f}")
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, pred))
print("\nClassification Report:")
print(classification_report(y_test, pred, target_names=["Stayed (0)", "Exited (1)"]))

print("\nConclusion: Feature normalization and multi-layer perceptron training allow the model")
print("to capture non-linear relationships across demographic and financial indicators.")

# --- Bonus: Equivalent Keras / TensorFlow Code Snippet ---
"""
# If your lab requires TensorFlow/Keras instead of scikit-learn:
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

keras_model = Sequential([
    Dense(16, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])
keras_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
keras_model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=1)
keras_pred = (keras_model.predict(X_test) > 0.5).astype(int)
"""
