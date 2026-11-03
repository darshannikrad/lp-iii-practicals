/**
 * Practical A5: Quick Sort (Deterministic vs Randomized)
 * Group A: Algorithms (DAA)
 *
 * Description:
 * Implements and compares the empirical and theoretical performance of
 * Deterministic Quick Sort (fixed pivot, here the last element) versus
 * Randomized Quick Sort (random pivot chosen uniformly from the subarray).
 * Uses high-resolution timers to demonstrate how sorted input degrades
 * deterministic Quick Sort into its worst-case O(n^2), while randomized Quick Sort
 * sustains expected O(n log n) runtime.
 *
 * Divide and Conquer Approach:
 * 1. Choose pivot (Deterministic: a[high], Randomized: swap random a[r] with a[high]).
 * 2. Partition: reorder elements so <= pivot move left, > pivot move right.
 * 3. Recursively sort the left and right partitions.
 *
 * Complexity Analysis:
 * - Deterministic Quick Sort:
 *   - Best & Average Case: O(n log n)
 *   - Worst Case:          O(n^2) when pivot is persistently minimum or maximum (e.g. sorted array).
 * - Randomized Quick Sort:
 *   - Expected Case:       O(n log n) regardless of input ordering.
 *   - Space Complexity:    O(log n) average recursion stack, O(n) worst-case recursion stack.
 *
 * Compilation & Execution:
 *   g++ -O2 A5_quick_sort.cpp -o A5_quick_sort
 *   ./A5_quick_sort
 */

#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <chrono>
using namespace std;

// Lomuto partition scheme
int partition(vector<int>& a, int low, int high) {
    int pivot = a[high]; // Last element as pivot
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (a[j] <= pivot) {
            swap(a[++i], a[j]);
        }
    }
    swap(a[i + 1], a[high]);
    return i + 1;
}

// QuickSort function supporting deterministic and randomized variants
void quickSort(vector<int>& a, int low, int high, bool randomized) {
    if (low < high) {
        if (randomized) {
            // Select uniform random index in [low, high] and swap with last element
            int r = low + rand() % (high - low + 1);
            swap(a[r], a[high]);
        }
        int p = partition(a, low, high);
        quickSort(a, low, p - 1, randomized);
        quickSort(a, p + 1, high, randomized);
    }
}

int main() {
    srand(static_cast<unsigned int>(time(0)));
    int n = 10000;

    cout << "Practical A5: Quick Sort (Deterministic vs Randomized)\n";
    cout << "Comparing runtimes on sorted input of size n = " << n << " (worst case for deterministic)\n";
    cout << "-------------------------------------------------------------------------\n";

    // Create an already-sorted array
    vector<int> sorted(n);
    for (int i = 0; i < n; i++) sorted[i] = i;

    vector<int> d = sorted; // copy for deterministic
    vector<int> r = sorted; // copy for randomized

    // Measure deterministic Quick Sort
    auto t1 = chrono::high_resolution_clock::now();
    quickSort(d, 0, n - 1, false);
    auto t2 = chrono::high_resolution_clock::now();

    // Measure randomized Quick Sort
    quickSort(r, 0, n - 1, true);
    auto t3 = chrono::high_resolution_clock::now();

    cout << "Deterministic time: "
         << chrono::duration<double, milli>(t2 - t1).count() << " ms\n";
    cout << "Randomized time:    "
         << chrono::duration<double, milli>(t3 - t2).count() << " ms\n";

    // Small correctness verification
    vector<int> sample = {5, 2, 9, 1, 7};
    quickSort(sample, 0, sample.size() - 1, true);
    cout << "\nCorrectness test on sample {5, 2, 9, 1, 7}:\nSorted sample: ";
    for (int x : sample) cout << x << " ";
    cout << "\n";

    return 0;
}
