"""
Practical B5: Customer/Sales Data Clustering with K-Means (Elbow Method)
Group B: Machine Learning (ML)

Problem Statement:
Apply K-Means clustering to sales data (sales_data_sample.csv).
Determine the optimal number of clusters using the Elbow Method (Within-Cluster Sum of Squares / Inertia).

Key Concepts & Viva Points:
- Unsupervised Learning: Discovering inherent groupings without predefined class labels.
- K-Means Algorithm:
  1. Initialize k centroids randomly (or via K-Means++).
  2. Assign each observation to the nearest centroid (Euclidean distance).
  3. Recompute centroid as the mean of assigned points.
  4. Repeat until centroid coordinates converge or maximum iterations are met.
- Inertia / WCSS: Sum of squared distances of samples to their closest cluster center.
- Elbow Method: Plot inertia vs number of clusters k. As k increases, inertia strictly decreases.
  The "elbow" point is where the rate of decrease abruptly slows down (diminishing returns).
- Feature Standardization: Crucial because K-Means computes Euclidean distance; unscaled 'SALES'
  (thousands of dollars) would completely drown out 'QUANTITYORDERED' (tens of items).
- Encoding Latin1: sales_data_sample.csv typically contains European character encodings;
  pd.read_csv(..., encoding='latin1') prevents UnicodeDecodeError.

Installation (run once):
  python -m pip install numpy pandas scikit-learn matplotlib

Execution:
  python3 B5_kmeans_clustering.py
  python3 B5_kmeans_clustering.py --plot
"""

import os
import sys
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# --- 1. Load Data (Fallback to synthetic dataset if sales_data_sample.csv is absent) ---
csv_path = "sales_data_sample.csv"
if os.path.exists(csv_path):
    print(f"Loading '{csv_path}' with latin1 encoding...")
    df = pd.read_csv(csv_path, encoding="latin1")
else:
    print(f"'{csv_path}' not found. Generating sample sales dataset for demonstration...")
    np.random.seed(42)
    n = 1000
    # Simulate 3 natural customer segments: Bulk Low-Cost, Standard Retail, High-End Luxury
    segment = np.random.choice([0, 1, 2], p=[0.4, 0.4, 0.2], size=n)
    quantities = np.where(segment == 0, np.random.normal(50, 10, n),
                 np.where(segment == 1, np.random.normal(30, 8, n), np.random.normal(15, 5, n)))
    prices = np.where(segment == 0, np.random.normal(35, 5, n),
             np.where(segment == 1, np.random.normal(70, 10, n), np.random.normal(140, 15, n)))
    quantities = np.clip(quantities, 5, 100)
    prices = np.clip(prices, 10, 200)
    sales = quantities * prices

    df = pd.DataFrame({
        "ORDERNUMBER": range(10000, 10000 + n),
        "QUANTITYORDERED": quantities,
        "PRICEEACH": prices,
        "SALES": sales
    })

# --- 2. Feature Selection & Preprocessing ---
selected_features = ["QUANTITYORDERED", "PRICEEACH", "SALES"]
data = df[selected_features].dropna()

# Standardize features so each has mean=0, std=1
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# --- 3. Elbow Method: Compute Inertia across k = 1 to 10 ---
print("\n" + "=" * 60)
print("Evaluating Inertia (WCSS) for k = 1 to 10:")
print("=" * 60)
inertias = []
k_range = range(1, 11)

for k in k_range:
    km = KMeans(n_clusters=k, init="k-means++", n_init=10, random_state=42)
    km.fit(scaled_data)
    inertias.append(km.inertia_)
    print(f"  k = {k:2d} | Inertia (WCSS): {km.inertia_:12.2f}")

# --- 4. Fit K-Means with Optimal k (Elbow Point, usually k=3 or 4) ---
optimal_k = 3
print(f"\nFitting final model with optimal k = {optimal_k} (selected at the elbow)...")
final_kmeans = KMeans(n_clusters=optimal_k, init="k-means++", n_init=10, random_state=42)
cluster_labels = final_kmeans.fit_predict(scaled_data)

# Cluster summary statistics
cluster_sizes = pd.Series(cluster_labels).value_counts().to_dict()
print(f"Cluster sizes distribution: {cluster_sizes}")

data_with_clusters = data.copy()
data_with_clusters["Cluster"] = cluster_labels
print("\nMean feature values by cluster:")
print(data_with_clusters.groupby("Cluster").mean().round(2))

# --- 5. Optional simple plots: elbow curve and cluster scatter plot ---
def show_plots():
    try:
        import matplotlib.pyplot as plt

        plt.plot(list(k_range), inertias, marker="o")
        plt.xlabel("Number of clusters (k)")
        plt.ylabel("Inertia")
        plt.title("Elbow Method")
        plt.show()

        plt.scatter(scaled_data[:, 0], scaled_data[:, 2], c=cluster_labels, cmap="viridis")
        plt.xlabel("Quantity Ordered (standardized)")
        plt.ylabel("Sales (standardized)")
        plt.title("K-Means Customer Clusters")
        plt.show()
    except ImportError:
        print("Install matplotlib to display plots: python -m pip install matplotlib")

if "--plot" in sys.argv:
    show_plots()
