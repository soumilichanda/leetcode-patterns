# Cluster 7: Tries & Prefix Search Invariants

| Problem | Key Invariant | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **LC 208 (Implement Trie)** | 26-ary child dictionary mapping with explicit boolean terminal markers. | $O(L)$ per op | $O(N \cdot L)$ |
| **LC 211 (Add & Search Words)** | Trie traversal with recursive DFS branching across `.children.values()` on wildcard `.`. | $O(L)$ normal / $O(26^L)$ wildcard | $O(N \cdot L)$ |
