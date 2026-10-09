# LeetCode Patterns & Algorithmic Problem Solving 🧠

Curated solutions to LeetCode problems organized by algorithmic patterns, focusing on strict time/space complexity invariants.

![LeetCode Patterns Solved](https://img.shields.io/badge/Solved-25%20Patterns-brightgreen)
![Clusters Completed](https://img.shields.io/badge/Clusters-9%2F9%20Completed-brightgreen)
![Complexity](https://img.shields.io/badge/Complexity-O(1)%20Auxiliary%20Space-blue)
---

### 📊 Pattern Progress Tracker

| # | Problem | Difficulty | Pattern | Invariant / Technique | Time | Space | Solution |
| :---: | :--- | :---: | :---: | :--- | :---: | :---: | :---: |
| 1 | Two Sum | Easy | Arrays & Hashing | Hash map complement lookup | $O`O(n)` | $O`O(n)` | [Code](01_arrays_and_hashing/0001_two_sum.py) |
| 125 | Valid Palindrome | Easy | Two Pointers | Inward-converging two pointers | $O`O(n)` | `O(1)` | [Code](02_two_pointers/0125_valid_palindrome.py) |
| 167 | Two Sum II - Input Array Is Sorted | Medium | Two Pointers | Monotonic sorted sum convergence | $O`O(n)` | `O(1)` | [Code](02_two_pointers/0167_two_sum_ii_sorted.py) |
| 11 | Container With Most Water | Medium | Two Pointers | Inward scan greedy bottleneck shift | $O`O(n)` | `O(1)` | [Code](02_two_pointers/0011_container_with_most_water.py) |
| 121 | Best Time to Buy and Sell Stock | Easy | Sliding Window | Monotonic minimum anchor | $O`O(n)` | `O(1)` | [Code](03_sliding_window/0121_best_time_to_buy_and_sell_stock.py) |
| 3 | Longest Substring Without Repeating Characters | Medium | Sliding Window | Dynamic hash map index jump | $O`O(n)` | `O(\min(n, m))` | [Code](03_sliding_window/0003_longest_substring_without_repeating_characters.py) |
| 424 | Longest Repeating Character Replacement | Medium | Sliding Window | Frequency count valid window expansion | $O`O(n)` | `O(1)` | [Code](03_sliding_window/0424_longest_repeating_character_replacement.py) |
| 20 | Valid Parentheses | Easy | Stack | LIFO hash map bracket matching | $O`O(n)` | $O`O(n)` | [Code](04_stack/0020_valid_parentheses.py) |
| 155 | Min Stack | Medium | Stack | Synchronized tuple minimum tracking | `O(1)` ops | $O`O(n)` | [Code](04_stack/0155_min_stack.py) |
| 739 | Daily Temperatures | Medium | Stack | Monotonic decreasing index stack | $O`O(n)` | $O`O(n)` | [Code](04_stack/0739_daily_temperatures.py) |
| 704 | Binary Search | Easy | Binary Search | Monotonic window bisection | `O(\log n)` | `O(1)` | [Code](05_binary_search/0704_binary_search.py) |
| 74 | Search a 2D Matrix | Medium | Binary Search | Virtual 1D-to-2D row/col coordinate projection | `O(\log(m \cdot n))` | `O(1)` | [Code](05_binary_search/0074_search_a_2d_matrix.py) |
| 875 | Koko Eating Bananas | Medium | Binary Search | Monotonic answer space feasibility search | `O(n \log(\max(P)))` | `O(1)` | [Code](05_binary_search/0875_koko_eating_bananas.py) |
| 206 | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | Linked List | Three-pointer in-place traversal reversal | $O`O(n)` | `O(1)` | [Python](06_linked_list/0206_reverse_linked_list.py) |
| 21 | [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | Linked List | Sentinel dummy head splice merge | `O(n + m)` | `O(1)` | [Python](06_linked_list/0021_merge_two_sorted_lists.py) |
| 141 | [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | Linked List | Floyd's fast & slow pointer collision | $O`O(n)` | `O(1)` | [Python](06_linked_list/0141_linked_list_cycle.py) |
| 19 | [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | Linked List | Fixed sentinel window gap $(n+1)$ | $O`O(n)` | `O(1)` | [Python](06_linked_list/0019_remove_nth_node_from_end_of_list.py) |
| 143 | [143. Reorder List](https://leetcode.com/problems/reorder-list/) | Medium | Linked List | Midpoint split + reverse + alternating splice | $O`O(n)` | `O(1)` | [Python](06_linked_list/0143_reorder_list.py) |
| 226 | [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Easy | Trees | Recursive post-order child pointer swap | \(n) | \(h) | [Python](07_trees/0226_invert_binary_tree.py) |
| 104 | [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | Trees | Divide-and-conquer subtree depth reduction | \(n) | \(h) | [Python](07_trees/0104_maximum_depth_of_binary_tree.py) |
| 102 | [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | Trees | BFS level-size queue snapshot iteration | \(n) | \(w) | [Python](07_trees/0102_binary_tree_level_order_traversal.py) |
| 208 | [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | Tries | 26-ary child dict with end-of-word boolean marker | \(L) | \(N \cdot L) | [Python](08_tries/0208_implement_trie.py) |
| 211 | [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Medium | Tries | Prefix tree combined with backtracking DFS wildcard matching | \(L) / \(26^L) | \(N \cdot L) | [Python](08_tries/0211_design_add_and_search_words.py) |
Medium | Heaps | Bounded size-k min-heap invariant | `O(n log k)` | `O(k)` | [Python](09_heaps/0215_kth_largest_element.py) |
| 973 | [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium | Heaps | Max-heap over squared Euclidean coordinates | `O(n log k)` | `O(k)` | [Python](09_heaps/0973_k_closest_points_to_origin.py) |

---

## 🧪 Automated Testing & Verification

Each algorithmic cluster contains unit tests and invariant validation:

```bash
pytest -v 08_tries/test_tries.py
python 08_tries/benchmark_trie.py
python 09_heaps/0215_kth_largest_element.py
python 09_heaps/0973_k_closest_points_to_origin.py
```
