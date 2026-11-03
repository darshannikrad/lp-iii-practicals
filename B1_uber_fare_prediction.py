"""
Practical B1: Uber Ride Fare Prediction
Group B: Machine Learning (ML)

Problem Statement:
Predict Uber ride fares by:
1. Preprocessing raw trip data and extracting temporal features (hour, day of week).
2. Calculating distance from coordinates using the Haversine formula.
3. Identifying and filtering outliers using the Interquartile Range (IQR) method.
4. Analyzing feature correlations with target 'fare_amount'.
5. Training and evaluating Linear Regression and Random Forest Regressor models using R^2 and RMSE.

Key Concepts & Viva Points:
- Haversine Formula: Computes the great-circle distance between two geographic coordinates on a sphere.
- IQR Outlier Filtering: Outliers fall outside [Q1 - 1.5 * IQR, Q3 + 1.5 * IQR].
- R^2 Score: Coefficient of determination; fraction of target variance explained by model (closer to 1.0 is better).
- RMSE: Root Mean Squared Error; average error in fare dollars (lower is better, penalizes large mistakes).
- Why Random Forest wins: Captures non-linear relationships, traffic/time surges, and feature interactions.

Execution:
  python3 B1_uber_fare_prediction.py
"""

import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# --- 1. Load Data (Fallback to synthetic data if uber.csv is not present) ---
csv_path = "uber.csv"
if os.path.exists(csv_path):
    print(f"Loading '{csv_path}'...")
    df = pd.read_csv(csv_path)
else:
    print(f"'{csv_path}' not found. Generating sample Uber dataset for demonstration...")
    np.random.seed(42)
    n_samples = 1000
    df = pd.DataFrame({
        "Unnamed: 0": range(n_samples),
        "key": [f"key_{i}" for i in range(n_samples)],
        "pickup_datetime": pd.date_range("2015-01-01", periods=n_samples, freq="h"),
        "pickup_longitude": np.random.uniform(-74.01, -73.95, n_samples),
        "pickup_latitude": np.random.uniform(40.70, 40.80, n_samples),
        "dropoff_longitude": np.random.uniform(-74.01, -73.95, n_samples),
        "dropoff_latitude": np.random.uniform(40.70, 40.80, n_samples),
        "passenger_count": np.random.randint(1, 6, n_samples),
    })
    # Synthetic fare roughly correlated with distance
    dx = (df["dropoff_longitude"] - df["pickup_longitude"]) * 111
    dy = (df["dropoff_latitude"] - df["pickup_latitude"]) * 111
    dist_approx = np.sqrt(dx**2 + dy**2)
    df["fare_amount"] = 3.5 + 2.5 * dist_approx + np.random.normal(0, 1.5, n_samples)

# --- 2. Preprocess & Feature Engineering ---
# Drop useless identifier columns
df = df.drop(columns=["Unnamed: 0", "key"], errors="ignore")
df = df.dropna()

# Extract datetime attributes (rush hours, day of week)
df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
df["hour"] = df["pickup_datetime"].dt.hour
df["day"] = df["pickup_datetime"].dt.dayofweek
df = df.drop(columns=["pickup_datetime"])

# Distance from geographic coordinates via Haversine Formula (Earth radius = 6371 km)
lat1, lon1 = np.radians(df["pickup_latitude"]), np.radians(df["pickup_longitude"])
lat2, lon2 = np.radians(df["dropoff_latitude"]), np.radians(df["dropoff_longitude"])
a = (np.sin((lat2 - lat1) / 2) ** 2
     + np.cos(lat1) * np.cos(lat2) * np.sin((lon2 - lon1) / 2) ** 2)
df["distance"] = 6371 * 2 * np.arcsin(np.sqrt(a))

# --- 3. Outlier Removal via IQR Method ---
for col in ["fare_amount", "distance"]:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    df = df[(df[col] >= q1 - 1.5 * iqr) & (df[col] <= q3 + 1.5 * iqr)]

# Filter non-positive fares and distances
df = df[(df["fare_amount"] > 0) & (df["distance"] > 0)]

# --- 4. Correlation Analysis ---
print("\nFeature Correlation with target (fare_amount):")
print(df.corr(numeric_only=True)["fare_amount"])

# --- 5. Train & Evaluate Models ---
X = df[["distance", "passenger_count", "hour", "day"]]
y = df["fare_amount"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nTraining set size: {len(X_train)} | Testing set size: {len(X_test)}")
print("=" * 60)

for name, model in [
    ("Linear Regression", LinearRegression()),
    ("Random Forest", RandomForestRegressor(n_estimators=50, random_state=42))
]:
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    r2 = r2_score(y_test, pred)
    rmse = np.sqrt(mean_squared_error(y_test, pred))
    print(f"[{name}]")
    print(f"  R^2 Score: {r2:.4f}")
    print(f"  RMSE:      ${rmse:.4f}")
    print("-" * 60)

print("\nConclusion: Random Forest usually yields higher R^2 and lower RMSE because it")
print("captures non-linear dependencies between distance, time-of-day, and fare surges.")
