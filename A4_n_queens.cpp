/**
 * Practical A4: n-Queens with First Queen Placed (Backtracking)
 * Group A: Algorithms (DAA)
 *
 * Description:
 * Places n non-attacking queens on an n×n chessboard such that no two queens
 * share the same row, column, or diagonal. The first queen is placed at a
 * fixed user-specified column in row 0, and backtracking is used to safely
 * place the remaining n-1 queens in rows 1 to n-1.
 *
 * Backtracking Principle:
 * Construct solution incrementally row-by-row. If placing a queen in column c
 * of row r leads to conflicts or dead-ends down the tree, backtrack by resetting
 * board[r][c] = 0 and trying the next available column.
 *
 * Diagonal Conflict Formula (Common Viva Question):
 * Two queens at (r1, c1) and (r2, c2) share a diagonal if and only if:
 *   abs(r1 - r2) == abs(c1 - c2)
 *
 * Complexity Analysis:
 * - Time Complexity:  O(n!) in worst case; backtracking prunes non-promising branches early.
 * - Space Complexity: O(n^2) for board representation + O(n) recursive stack depth.
 *
 * Compilation & Execution:
 *   g++ -O2 A4_n_queens.cpp -o A4_n_queens
 *   ./A4_n_queens
 */

#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;

int n = 8;
vector<vector<int>> board;

// Checks if position (r, c) is safe from previously placed queens above
bool safe(int r, int c) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j]) {
                // Check column conflict (j == c) and diagonal conflict (|i - r| == |j - c|)
                if (j == c || abs(i - r) == abs(j - c)) {
                    return false;
                }
            }
        }
    }
    return true;
}

// Backtracking function to place queens from row r to n-1
bool solve(int r) {
    if (r == n) return true; // All queens successfully placed

    for (int c = 0; c < n; c++) {
        if (safe(r, c)) {
            board[r][c] = 1; // Place queen
            if (solve(r + 1)) return true; // Recurse to next row
            board[r][c] = 0; // Backtrack: remove queen and try next column
        }
    }
    return false; // No safe column in row r
}

int main() {
    int firstCol = 0;
    cout << "Practical A4: n-Queens with First Queen Placed (n = " << n << ")\n";
    cout << "Enter column (0 to " << n - 1 << ") for the first queen in row 0: ";
    if (!(cin >> firstCol)) {
        firstCol = 0; // default fallback
    }

    if (firstCol < 0 || firstCol >= n) {
        cout << "Invalid column! Must be between 0 and " << n - 1 << ".\n";
        return 1;
    }

    board.assign(n, vector<int>(n, 0));
    board[0][firstCol] = 1; // Fix the first queen in row 0

    if (solve(1)) { // Begin backtracking from row 1
        cout << "\nSolution Matrix (Q = Queen, . = Empty):\n";
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << (board[i][j] ? "Q " : ". ");
            }
            cout << "\n";
        }
    } else {
        cout << "\nNo solution exists for this first queen position.\n";
    }

    return 0;
}
