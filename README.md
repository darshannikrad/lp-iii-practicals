# LP-III Laboratory Practicals + Viva Guide

This repository contains the complete set of **12 unique practical assignments** for **Laboratory Practice III (LP-III)**, covering **Algorithms (DAA)**, **Machine Learning (ML)**, and **Blockchain (Solidity)**.

Each file includes clean, fully documented, and ready-to-run source code with theoretical explanations, time and space complexity analysis, and frequently asked viva questions.

---

## 📋 Table of Practicals

| # | File | Group | Language | Title / Problem Statement | Time Complexity | Space Complexity |
|---|---|---|---|---|---|---|
| **A1** | [`A1_fibonacci.cpp`](A1_fibonacci.cpp) | Algorithms | C++ | Recursive and Non-Recursive Fibonacci Numbers | Rec: $O(2^n)$<br>Iter: $O(n)$ | Rec: $O(n)$<br>Iter: $O(1)$ |
| **A2** | [`A2_huffman_encoding.cpp`](A2_huffman_encoding.cpp) | Algorithms | C++ | Huffman Encoding using Greedy Strategy | $O(n \log n)$ | $O(n)$ |
| **A3** | [`A3_knapsack_01.cpp`](A3_knapsack_01.cpp) | Algorithms | C++ | 0-1 Knapsack using Dynamic Programming | $O(n \times W)$ | 2D: $O(n \times W)$<br>1D: $O(W)$ |
| **A4** | [`A4_n_queens.cpp`](A4_n_queens.cpp) | Algorithms | C++ | N-Queens with First Queen Placed (Backtracking) | $O(n!)$ | Board: $O(n^2)$<br>Stack: $O(n)$ |
| **A5** | [`A5_quick_sort.cpp`](A5_quick_sort.cpp) | Algorithms | C++ | Quick Sort: Deterministic vs Randomized | Avg: $O(n \log n)$<br>Worst: $O(n^2)$ | Avg: $O(\log n)$<br>Worst: $O(n)$ |
| **B1** | [`B1_uber_fare_prediction.py`](B1_uber_fare_prediction.py) | Machine Learning | Python | Uber Ride Fare Prediction (Linear Regression & Random Forest) | Model fitting | $O(N \times D)$ |
| **B2** | [`B2_spam_classification.py`](B2_spam_classification.py) | Machine Learning | Python | Spam Email Classification (KNN vs SVM) | Model fitting | $O(N \times D)$ |
| **B3** | [`B3_churn_neural_network.py`](B3_churn_neural_network.py) | Machine Learning | Python | Bank Customer Churn with Multilayer Perceptron ANN | Iterative epochs | Network weights |
| **B4** | [`B4_gradient_descent.py`](B4_gradient_descent.py) | Machine Learning | Python | Gradient Descent for $y = (x + 3)^2$ starting at $x = 2$ | $O(\text{iterations})$ | $O(1)$ |
| **B5** | [`B5_kmeans_clustering.py`](B5_kmeans_clustering.py) | Machine Learning | Python | Customer/Sales Clustering with K-Means & Elbow Method | $O(n \cdot k \cdot d \cdot i)$ | $O(n \cdot d + k \cdot d)$ |
| **C1** | [`C1_bank_account.sol`](C1_bank_account.sol) | Blockchain | Solidity | Bank Account Smart Contract (Deposit, Withdraw, Balance) | Gas-based | EVM Storage |
| **C2** | [`C2_student_data.sol`](C2_student_data.sol) | Blockchain | Solidity | Student Data Smart Contract (Structs, Arrays, Gas Observation) | Gas-based | EVM Storage |

---

## 🛠️ Prerequisites & Setup

### 1. C++ (Group A: A1 - A5)
Requires any modern C++ compiler (`g++` or `clang++` supporting C++17 or newer):
```bash
# Compile and run any algorithm:
g++ -O2 -std=c++17 A1_fibonacci.cpp -o A1 && ./A1
g++ -O2 -std=c++17 A2_huffman_encoding.cpp -o A2 && ./A2
g++ -O2 -std=c++17 A3_knapsack_01.cpp -o A3 && ./A3
g++ -O2 -std=c++17 A4_n_queens.cpp -o A4 && ./A4
g++ -O2 -std=c++17 A5_quick_sort.cpp -o A5 && ./A5
```

### 2. Python (Group B: B1 - B5)
Install required dependencies:
```bash
pip install numpy pandas scikit-learn matplotlib
```
Or run individual scripts with `python3`:
```bash
python3 B1_uber_fare_prediction.py
python3 B2_spam_classification.py
python3 B3_churn_neural_network.py
python3 B4_gradient_descent.py
python3 B5_kmeans_clustering.py
```
> **Note:** The Python scripts automatically check for their respective CSV datasets (`uber.csv`, `emails.csv`, `Churn_Modelling.csv`, `sales_data_sample.csv`). If a CSV is not found, realistic synthetic data is generated on the fly so the scripts run out-of-the-box.

### 3. Solidity (Group C: C1 - C2)
1. Open [Remix IDE](https://remix.ethereum.org).
2. Create `Bank.sol` or `StudentData.sol` and paste the respective file code.
3. In the **Solidity Compiler** tab, select compiler version `0.8.x` and click **Compile**.
4. In the **Deploy & Run Transactions** tab:
   - Environment: Select **Remix VM** (for local testing without gas cost) or **Injected Provider - MetaMask** (for Sepolia testnet).
   - Click **Deploy** and interact with the deployed contract functions.

---

## 📖 Practical Summaries

### Practical A1: Fibonacci Numbers
- **Concept:** Computes $F(n) = F(n-1) + F(n-2)$ with $F(0)=0, F(1)=1$.
- **Recursive:** Makes two calls per node; time is $O(2^n)$ (precisely $O(\phi^n)$, $\phi \approx 1.618$), stack depth is $O(n)$.
- **Iterative:** Keeps two variables sliding forward; time is $O(n)$, space is $O(1)$.
- **Viva Key:** Iteration avoids call stack overhead and duplicate state recomputation. For $O(\log n)$ runtime, matrix exponentiation or fast doubling can be used.

### Practical A2: Huffman Encoding
- **Concept:** Greedy compression assigning short binary codes to frequent characters and longer codes to rare characters.
- **Data Structure:** Min-heap (`std::priority_queue`) to repeatedly extract and merge the two lowest frequency nodes.
- **Viva Key:** Huffman produces an optimal, prefix-free, lossless code where no codeword is a prefix of another.

### Practical A3: 0-1 Knapsack
- **Concept:** Selects subset of $n$ indivisible items with weights $wt[i]$ and values $val[i]$ to maximize total value within capacity $W$.
- **Recurrence:** $dp[i][w] = \max(dp[i-1][w], val[i-1] + dp[i-1][w - wt[i-1]])$.
- **Viva Key:** 0-1 Knapsack cannot be solved with a simple greedy heuristic (value/weight ratio) because items are indivisible; it requires Dynamic Programming ($O(n \times W)$ pseudo-polynomial). Fractional Knapsack can be solved greedily in $O(n \log n)$.

### Practical A4: N-Queens with First Queen Placed
- **Concept:** Places $n$ queens on an $n \times n$ board such that no two queens attack each other (no shared row, column, or diagonal).
- **Backtracking:** The first queen is placed in row 0 at the user-specified column. Rows $1$ through $n-1$ are filled recursively. If a placement reaches a dead end, it backtracks by resetting `board[r][c] = 0`.
- **Diagonal Check:** Two queens at $(r_1, c_1)$ and $(r_2, c_2)$ conflict if $|r_1 - r_2| == |c_1 - c_2|$.

### Practical A5: Quick Sort (Deterministic vs Randomized)
- **Concept:** Divide-and-conquer sorting by choosing a pivot and partitioning elements into smaller and larger subarrays.
- **Deterministic:** Chooses a fixed pivot (e.g. last element). On already-sorted or reverse-sorted input, partition splits are unbalanced ($0$ and $n-1$), degrading performance to $O(n^2)$.
- **Randomized:** Swaps a uniformly random element with the last element before partitioning. Eliminates worst-case bias and maintains expected $O(n \log n)$ runtime across all inputs.

### Practical B1: Uber Ride Fare Prediction
- **Pipeline:** Load data $\to$ drop identifiers (`Unnamed: 0`, `key`) $\to$ parse `pickup_datetime` to extract `hour` and `day` $\to$ compute Haversine distance from coordinates $\to$ filter outliers via IQR $\to$ train Linear Regression and Random Forest Regressor $\to$ evaluate $R^2$ and RMSE.
- **Viva Key:** Random Forest Regressor typically achieves higher $R^2$ and lower RMSE because it models non-linear relationships, peak-hour surges, and geographic interactions.

### Practical B2: Spam Email Classification (KNN vs SVM)
- **Pipeline:** Word-count feature matrix $\to$ 80/20 train/test split $\to$ train `KNeighborsClassifier(n_neighbors=5)` and `SVC(kernel="linear")` $\to$ evaluate accuracy, confusion matrix, precision, recall, and F1-score.
- **Viva Key:** SVM with a linear kernel substantially outperforms KNN on text datasets due to the *curse of dimensionality*. In high dimensions, Euclidean distances between points converge, hindering KNN's distance metric.

### Practical B3: Bank Customer Churn (Artificial Neural Network)
- **Pipeline:** Drop irrelevant identifiers $\to$ one-hot encode `Geography` and `Gender` with `drop_first=True` (avoids dummy variable trap) $\to$ split train/test $\to$ scale features using `StandardScaler` (fit on train only to prevent data leakage) $\to$ train Multilayer Perceptron (`MLPClassifier`).
- **Viva Key:** Churn data is imbalanced (~80% stay vs ~20% churn). Accuracy alone is misleading; false negatives (failing to detect a churner) are especially costly for retention.

### Practical B4: Gradient Descent for $y = (x + 3)^2$
- **Objective:** Minimize $y = (x + 3)^2$ starting at $x = 2$.
- **Derivative:** $dy/dx = 2(x + 3)$.
- **Update Rule:** $x \leftarrow x - \text{lr} \times \text{gradient}$.
- **Viva Key:** Subtracting the gradient moves opposite to steepest ascent. For $\text{lr} = 0.1$, the error decays geometrically by a factor of $(1 - 2 \cdot 0.1) = 0.8$ each step, converging smoothly to the global minimum at $x = -3$, $y = 0$.

### Practical B5: K-Means Clustering (Elbow Method)
- **Concept:** Unsupervised grouping of sales records based on numeric attributes (`QUANTITYORDERED`, `PRICEEACH`, `SALES`).
- **Elbow Method:** Fits K-Means for $k = 1$ to $10$, records inertia (Within-Cluster Sum of Squares, WCSS), and identifies the bend/elbow in the plot where rate of decrease diminishes (typically $k=3$ or $k=4$).
- **Viva Key:** Features must be standardized (`StandardScaler`) prior to clustering because K-Means relies on Euclidean distance, which would otherwise be overwhelmed by larger numerical features.

### Practical C1: Bank Account Smart Contract
- **State & Logic:** Unsigned integer `balance`, state-modifying functions `deposit(amount)` and `withdraw(amount)` with `require(balance >= amount, "...")`, and read-only `showBalance()` view function.
- **Viva Key:** Calls to `view` functions do not create an on-chain transaction and cost zero gas. State-modifying operations cost gas and must be confirmed by miners/validators.

### Practical C2: Student Data Smart Contract
- **State & Logic:** `struct Student` with dynamic storage array `Student[] public students`. Includes `addStudent(...)`, `getStudent(index)`, and `totalStudents()`.
- **Gas Observation:** Storage write operations (`push` to storage) cost significant gas because every node in the Ethereum network stores the state permanently. Memory allocations are transient and inexpensive.

---

## ⚡ Quick Viva Cheat Sheet

| Topic | One-Line Exam Answer |
|---|---|
| **Greedy (Huffman)** | Makes the locally optimal choice at each step; never backtracks or reconsiders. |
| **Dynamic Programming (Knapsack)** | Decomposes problem into overlapping subproblems and stores results in a table to eliminate recomputation. |
| **Backtracking (N-Queens)** | Builds candidate solution incrementally and undoes the last choice upon encountering a conflict or dead end. |
| **Divide & Conquer (Quick Sort)** | Partitions elements around a chosen pivot and recursively sorts the subarrays. |
| **Outlier Detection** | Points lying outside $[Q1 - 1.5 \times IQR, Q3 + 1.5 \times IQR]$ are removed to prevent distortion of linear estimators. |
| **$R^2$ vs RMSE** | $R^2$ measures fraction of variance explained (closer to 1 is better); RMSE measures average error in target units (lower is better). |
| **KNN vs SVM** | KNN is a lazy distance-based voter; SVM finds the maximum-margin hyperplane separating classes. |
| **Feature Scaling** | Normalizes variables onto a common scale so high-magnitude features do not dominate distance calculations or gradients. |
| **Learning Rate** | Step size in gradient descent. Too small converges slowly; too large oscillates or diverges. |
| **Elbow Method** | Plots inertia against $k$ and selects the point of inflection (elbow) where marginal returns decrease. |
| **Gas on Ethereum** | Unit of computational effort. Transaction fee $= \text{Gas Used} \times \text{Gas Price}$ (in Gwei). |

---

## 📜 License
This repository is released under the [MIT License](LICENSE).
