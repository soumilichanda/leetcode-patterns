# LeetCode Patterns & Algorithmic Problem Solving 🧠

Curated solutions to LeetCode problems organized by algorithmic patterns, focusing on strict time/space complexity invariants.

[![Solved Patterns](https://img.shields.io/badge/Solved-27%20Patterns-brightgreen.svg)](#pattern-progress-tracker)
[![Clusters Completed](https://img.shields.io/badge/Clusters-10%2F10%20Completed-brightgreen.svg)](#pattern-progress-tracker)
[![Auxiliary Space Complexity](https://img.shields.io/badge/Complexity-O(1)%20Auxiliary%20Space-dodgerblue.svg)](#pattern-progress-tracker)

---

## 📊 Pattern Progress Tracker

| # | Problem | Difficulty | Pattern | Invariant / Technique | Time | Space | Solution |
| :---: | :--- | :---: | :--- | :--- | :---: | :---: | :---: |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Arrays & Hashing | Hash map complement lookup | `O(n)` | `O(n)` | [Code](01_arrays_and_hashing/0001_two_sum.py) |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | Two Pointers | Inward-converging two pointers | `O(n)` | `O(1)` | [Code](02_two_pointers/0125_valid_palindrome.py) |
| 167 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium | Two Pointers | Monotonic sorted sum convergence | `O(n)` | `O(1)` | [Code](02_two_pointers/0167_two_sum_ii_sorted.py) |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | Two Pointers | Inward scan greedy bottleneck shift | `O(n)` | `O(1)` | [Code](02_two_pointers/0011_container_with_most_water.py) |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | Sliding Window | Monotonic minimum anchor | `O(n)` | `O(1)` | [Code](03_sliding_window/0121_best_time_to_buy_and_sell_stock.py) |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | Sliding Window | Dynamic hash map index jump | `O(n)` | `O(min(n, m))` | [Code](03_sliding_window/0003_longest_substring_without_repeating_characters.py) |
| 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | Sliding Window | Frequency count valid window expansion | `O(n)` | `O(1)` | [Code](03_sliding_window/0424_longest_repeating_character_replacement.py) |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | Stack | LIFO hash map bracket matching | `O(n)` | `O(n)` | [Code](04_stack/0020_valid_parentheses.py) |
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/) | Medium | Stack | Value-delta tracking auxiliary stack | `O(1)` | `O(n)` | [Code](04_stack/0155_min_stack.py) |
| 739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | Stack | Monotonic decreasing stack indices | `O(n)` | `O(n)` | [Code](04_stack/0739_daily_temperatures.py) |
| 704 | [Binary Search](https://leetcode.com/problems/binary-search/) | Easy | Binary Search | Monotonic interval halving `[L, R]` | `O(log n)` | `O(1)` | [Code](05_binary_search/0704_binary_search.py) |
| 74 | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Medium | Binary Search | Virtualized row/column 1D coordinate flattening | `O(log(m * n))` | `O(1)` | [Code](05_binary_search/0074_search_a_2d_matrix.py) |
| 875 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | Binary Search | Binary search on monotone answer space | `O(n log m)` | `O(1)` | [Code](05_binary_search/0875_koko_eating_bananas.py) |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | Linked List | Three-pointer iterative link flip | `O(n)` | `O(1)` | [Code](06_linked_list/0206_reverse_linked_list.py) |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | Linked List | Sentinel dummy head splice | `O(n + m)` | `O(1)` | [Code](06_linked_list/0021_merge_two_sorted_lists.py) |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | Linked List | Floyd's fast/slow pointer collision | `O(n)` | `O(1)` | [Code](06_linked_list/0141_linked_list_cycle.py) |
| 19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | Linked List | Fixed sentinel window gap `(n + 1)` | `O(n)` | `O(1)` | [Code](06_linked_list/0019_remove_nth_node_from_end_of_list.py) |
| 143 | [Reorder List](https://leetcode.com/problems/reorder-list/) | Medium | Linked List | Midpoint split + reverse + alternating splice | `O(n)` | `O(1)` | [Code](06_linked_list/0143_reorder_list.py) |
| 226 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Easy | Trees | Recursive post-order child pointer swap | `O(n)` | `O(h)` | [Code](07_trees/0226_invert_binary_tree.py) |
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | Trees | Divide-and-conquer subtree depth reduction | `O(n)` | `O(h)` | [Code](07_trees/0104_maximum_depth_of_binary_tree.py) |
| 102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | Trees | BFS level-size queue snapshot iteration | `O(n)` | `O(w)` | [Code](07_trees/0102_binary_tree_level_order_traversal.py) |
| 208 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | Tries | 26-ary child dict with end-of-word boolean marker | `O(L)` | `O(N * L)` | [Code](08_tries/0208_implement_trie.py) |
| 211 | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Medium | Tries | Prefix tree combined with backtracking DFS wildcard matching | `O(L)` / `O(26^L)` | `O(N * L)` | [Code](08_tries/0211_design_add_and_search_words_data_structure.py) |
| 215 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | Heaps | Bounded size-k min-heap invariant | `O(n log k)` | `O(k)` | [Code](09_heaps/0215_kth_largest_element.py) |
| 973 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium | Heaps | Max-heap over squared Euclidean coordinates | `O(n log k)` | `O(k)` | [Code](09_heaps/0973_k_closest_points_to_origin.py) |
| 200 | [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | Graphs | 2D grid BFS traversal with in-place sinking | `O(m * n)` | `O(min(m, n))` | [Code](10_graphs/0200_number_of_islands.py) |
| 207 | [207. Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | Graphs | Kahn algorithm topological sort with in-degrees | `O(V + E)` | `O(V + E)` | [Code](10_graphs/0207_course_schedule.py) |
---

## 🧪 Automated Testing & Verification

Each algorithmic cluster contains unit tests and invariant validation:

```bash
pytest -v 08_tries/test_tries.py
python 08_tries/benchmark_trie.py
python 09_heaps/0215_kth_largest_element.py
python 09_heaps/0973_k_closest_points_to_origin.py
