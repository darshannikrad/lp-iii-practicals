/**
 * Practical A1: Fibonacci Numbers (Recursive and Non-Recursive)
 * Group A: Algorithms (DAA)
 *
 * Description:
 * Computes Fibonacci numbers using both recursive and non-recursive (iterative)
 * approaches. In Fibonacci, each number is the sum of the previous two:
 * F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1.
 *
 * Complexity Analysis:
 * - Recursive:
 *   Time Complexity:  O(2^n) - more accurately O(phi^n) where phi ≈ 1.618.
 *                     Recomputes overlapping subproblems repeatedly.
 *   Space Complexity: O(n) due to recursive call stack depth.
 * - Non-Recursive (Iterative):
 *   Time Complexity:  O(n) - single linear loop sliding two variables.
 *   Space Complexity: O(1) - only maintains two variables (a, b).
 * - Memoized (Top-Down DP):
 *   Time Complexity:  O(n)
 *   Space Complexity: O(n)
 *
 * Compilation & Execution:
 *   g++ -O2 A1_fibonacci.cpp -o A1_fibonacci
 *   ./A1_fibonacci
 */

#include <iostream>
#include <vector>
using namespace std;

// Recursive Fibonacci (Exponential Time)
long long fibRec(int n) {
    if (n <= 1) return n; // base case
    return fibRec(n - 1) + fibRec(n - 2); // two recursive calls
}

// Non-recursive (Iterative) Fibonacci (Linear Time, O(1) Space)
long long fibIter(int n) {
    long long a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        long long next = a + b;
        a = b;
        b = next;
    }
    return a;
}

// Memoized Fibonacci (Top-down DP)
long long memo[100] = {0};
long long fibMemo(int n) {
    if (n <= 1) return n;
    if (memo[n] != 0) return memo[n];
    return memo[n] = fibMemo(n - 1) + fibMemo(n - 2);
}

int main() {
    int n = 10;
    cout << "Practical A1: Fibonacci Numbers (n = " << n << ")\n";
    cout << "---------------------------------------------\n";

    cout << "Recursive:     ";
    for (int i = 0; i < n; i++) cout << fibRec(i) << " ";
    cout << "\n";

    cout << "Non-recursive: ";
    for (int i = 0; i < n; i++) cout << fibIter(i) << " ";
    cout << "\n";

    cout << "Memoized DP:   ";
    for (int i = 0; i < n; i++) cout << fibMemo(i) << " ";
    cout << "\n";

    cout << "\nConclusion: The non-recursive version is far more efficient in both time and space.\n";
    return 0;
}
