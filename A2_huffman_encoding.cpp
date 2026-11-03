/**
 * Practical A2: Huffman Encoding (Greedy Strategy)
 * Group A: Algorithms (DAA)
 *
 * Description:
 * Implements Huffman Coding for lossless data compression using a greedy algorithm.
 * Frequent characters receive shorter binary codes, while rarer characters receive
 * longer codes. A min-heap (priority queue) is used to repeatedly merge the two
 * lowest-frequency nodes into a parent node until a single root remains.
 *
 * Key Properties:
 * - Prefix-free code: No codeword is a prefix of another, allowing unambiguous decoding.
 * - Optimal: Produces the minimum weighted average codeword length among prefix codes.
 * - Lossless: The exact original text is preserved without data loss.
 *
 * Complexity Analysis:
 * - Time Complexity:  O(n log n), where n is the number of distinct characters
 *                     (n-1 merges, each priority queue pop/push takes O(log n)).
 * - Space Complexity: O(n) to store tree nodes and frequency/code maps.
 *
 * Compilation & Execution:
 *   g++ -O2 A2_huffman_encoding.cpp -o A2_huffman_encoding
 *   ./A2_huffman_encoding
 */

#include <iostream>
#include <string>
#include <queue>
#include <map>
#include <vector>
using namespace std;

// Tree Node for Huffman Tree
struct Node {
    char ch;
    int freq;
    Node *left, *right;
    Node(char c, int f, Node* l = nullptr, Node* r = nullptr)
        : ch(c), freq(f), left(l), right(r) {}
};

// Comparator to configure std::priority_queue as a min-heap
struct Compare {
    bool operator()(Node* a, Node* b) {
        return a->freq > b->freq;
    }
};

// Recursive function to traverse Huffman tree and generate prefix codes
void getCodes(Node* node, string code, map<char, string>& codes) {
    if (!node) return;
    // Leaf node contains character
    if (!node->left && !node->right) {
        codes[node->ch] = code.empty() ? "0" : code;
        return;
    }
    getCodes(node->left, code + "0", codes);
    getCodes(node->right, code + "1", codes);
}

int main() {
    string text = "huffman coding";
    cout << "Practical A2: Huffman Encoding\n";
    cout << "Input text: \"" << text << "\"\n";
    cout << "---------------------------------------------\n";

    // Step 1: Count character frequencies
    map<char, int> freq;
    for (char c : text) freq[c]++;

    // Step 2: Build min-heap of nodes
    priority_queue<Node*, vector<Node*>, Compare> pq;
    for (auto& p : freq) {
        pq.push(new Node(p.first, p.second));
    }

    // Step 3: Repeatedly merge two lowest frequency nodes (Greedy step)
    while (pq.size() > 1) {
        Node* a = pq.top(); pq.pop();
        Node* b = pq.top(); pq.pop();
        pq.push(new Node('\0', a->freq + b->freq, a, b));
    }

    // Step 4: Generate prefix codes
    map<char, string> codes;
    if (!pq.empty()) {
        getCodes(pq.top(), "", codes);
    }

    // Display generated codes
    cout << "Huffman Codes:\n";
    for (auto& p : codes) {
        cout << "  '" << p.first << "' : " << p.second << "\n";
    }

    // Display encoded bitstream
    cout << "\nEncoded Bitstream: ";
    for (char c : text) {
        cout << codes[c];
    }
    cout << "\n";

    return 0;
}
