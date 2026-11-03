/**
 * Practical A3: 0-1 Knapsack Problem (Dynamic Programming)
 * Group A: Algorithms (DAA)
 *
 * Description:
 * Given n items, each with a given weight and value, and a knapsack of capacity W,
 * determines the maximum total value that can be put in the knapsack. Each item can
 * either be taken as a whole or left (0-1 decision, no fractions allowed).
 *
 * DP State Formulation:
 * - dp[i][w] = maximum value achievable using a subset of the first i items
 *              with capacity limit w.
 * - Transitions:
 *   - Skip item: dp[i][w] = dp[i-1][w]
 *   - Take item (if wt[i-1] <= w): dp[i][w] = max(dp[i-1][w], val[i-1] + dp[i-1][w - wt[i-1]])
 *
 * Complexity Analysis:
 * - Time Complexity:  O(n * W), where n is the number of items and W is bag capacity.
 *                     Each state in the DP table is computed in O(1) time.
 *                     Note: This is pseudo-polynomial because W depends on numeric magnitude.
 * - Space Complexity: O(n * W) for 2D DP table; reducible to O(W) using 1D backwards loop.
 *
 * 0-1 vs Fractional Knapsack (Common Viva Point):
 * - 0-1 Knapsack items are indivisible -> Solved using Dynamic Programming / Branch & Bound.
 * - Fractional Knapsack items can be divided -> Solved greedily by sorting value/weight ratio in O(n log n).
 *
 * Compilation & Execution:
 *   g++ -O2 A3_knapsack_01.cpp -o A3_knapsack_01
 *   ./A3_knapsack_01
 */

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 2D Dynamic Programming solution
int knapsack2D(const vector<int>& wt, const vector<int>& val, int W) {
    int n = wt.size();
    vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            dp[i][w] = dp[i - 1][w]; // Skip item
            if (wt[i - 1] <= w) {    // Take item
                dp[i][w] = max(dp[i][w], val[i - 1] + dp[i - 1][w - wt[i - 1]]);
            }
        }
    }

    // Backtracking to find which items were selected
    cout << "Selected item indices (0-based): ";
    int curW = W;
    for (int i = n; i > 0; i--) {
        if (dp[i][curW] != dp[i - 1][curW]) {
            cout << (i - 1) << " ";
            curW -= wt[i - 1];
        }
    }
    cout << "\n";

    return dp[n][W];
}

// Space-optimized 1D DP solution (O(W) space)
int knapsack1D(const vector<int>& wt, const vector<int>& val, int W) {
    int n = wt.size();
    vector<int> dp(W + 1, 0);

    for (int i = 0; i < n; i++) {
        // Iterate backwards so each item is included at most once (0-1 knapsack)
        for (int w = W; w >= wt[i]; w--) {
            dp[w] = max(dp[w], val[i] + dp[w - wt[i]]);
        }
    }
    return dp[W];
}

int main() {
    vector<int> weights = {10, 20, 30};
    vector<int> values  = {60, 100, 120};
    int capacity = 50;

    cout << "Practical A3: 0-1 Knapsack (Dynamic Programming)\n";
    cout << "---------------------------------------------\n";
    cout << "Knapsack Capacity: " << capacity << "\n";
    cout << "Items (Weight, Value):\n";
    for (size_t i = 0; i < weights.size(); i++) {
        cout << "  Item " << i << ": (" << weights[i] << " kg, Rs. " << values[i] << ")\n";
    }

    int maxVal2D = knapsack2D(weights, values, capacity);
    cout << "Maximum value (2D DP): " << maxVal2D << "\n";

    int maxVal1D = knapsack1D(weights, values, capacity);
    cout << "Maximum value (1D DP): " << maxVal1D << "\n";

    return 0;
}
