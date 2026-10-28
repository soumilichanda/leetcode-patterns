# LeetCode Patterns & Algorithmic Problem Solving 🧠

Curated solutions to LeetCode problems organized by algorithmic patterns, focusing on strict time/space complexity invariants.

[![Solved Patterns](https://img.shields.io/badge/Solved-58%20Patterns-brightgreen.svg)](#-pattern-progress-tracker)
[![Clusters Completed](https://img.shields.io/badge/Clusters-25%2F25%20Completed-brightgreen.svg)](#-pattern-progress-tracker)
[![Auxiliary Space Complexity](https://img.shields.io/badge/Complexity-O(1)%20Auxiliary%20Space-dodgerblue.svg)](#-pattern-progress-tracker)

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
| 208 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | Tries | 26-ary child dict with end-of-word boolean marker | `O(L)` | `O(N * L)` | [Code](08_tries/0208_implement_trie_prefix_tree.py) |
| 211 | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Medium | Tries | Prefix tree combined with backtracking DFS wildcard matching | `O(L)` / `O(26^L)` | `O(N * L)` | [Code](08_tries/0211_design_add_and_search_words_data_structure.py) |
| 215 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | Heaps | Bounded size-k min-heap invariant | `O(n log k)` | `O(k)` | [Code](09_heaps/0215_kth_largest_element.py) |
| 973 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium | Heaps | Max-heap over squared Euclidean coordinates | `O(n log k)` | `O(k)` | [Code](09_heaps/0973_k_closest_points_to_origin.py) |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | Graphs | 2D grid BFS traversal with in-place sinking | `O(m * n)` | `O(min(m, n))` | [Code](10_graphs/0200_number_of_islands.py) |
| 207 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | Graphs | Kahn algorithm topological sort with in-degrees | `O(V + E)` | `O(V + E)` | [Code](10_graphs/0207_course_schedule.py) |
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | 1D DP | Space-optimized Fibonacci recurrence | `O(n)` | `O(1)` | [Code](11_dynamic_programming/0070_climbing_stairs.py) |
| 198 | [House Robber](https://leetcode.com/problems/house-robber/) | Medium | 1D DP | Non-adjacent state transition optimization | `O(n)` | `O(1)` | [Code](11_dynamic_programming/0198_house_robber.py) |
| 62 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | Medium | 2D DP | Rolling row combinatorial grid transition | `O(m * n)` | `O(n)` | [Code](12_dynamic_programming_2d/0062_unique_paths.py) |
| 1143 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | 2D DP | Dual-sequence matrix state recurrence | `O(m * n)` | `O(m * n)` | [Code](12_dynamic_programming_2d/1143_longest_common_subsequence.py) |
| 300 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | 1D / Subsequence DP | Patience sorting via binary search (`bisect_left`) on tails array | `O(n log n)` | `O(n)` | [Code](13_dynamic_programming_subsequences/0300_longest_increasing_subsequence.py) |
| 416 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Medium | 0/1 Knapsack DP | Reverse 1D boolean array tabulation towards sum/2 | `O(n * target)` | `O(target)` | [Code](13_dynamic_programming_subsequences/0416_partition_equal_subset_sum.py) |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium | Greedy | Kadane’s O(n) greedy prefix scan discarding negative baggage | O(n) | O(1) | [Python](14_greedy/0053_maximum_subarray.py) |
| 55 | [Jump Game](https://leetcode.com/problems/jump-game/) | Medium | Greedy | Furthest horizon reachability expansion with early exit | O(n) | O(1) | [Python](14_greedy/0055_jump_game.py) |
| 78 | [Subsets](https://leetcode.com/problems/subsets/) | Medium | Backtracking | Binary decision tree state space exploration | O(n * 2^n) | O(n) | [Code](15_backtracking/0078_subsets.py) |
| 39 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium | Backtracking | Target prune recursion with unbounded candidate reuse | O(2^t) | O(t) | [Code](15_backtracking/0039_combination_sum.py) |
| 46 | [Permutations](https://leetcode.com/problems/permutations/) | Medium | Backtracking | In-place element swap state-space recursion | O(n * n!) | O(n) | [Code](16_grid_backtracking/0046_permutations.py) |
| 79 | [Word Search](https://leetcode.com/problems/word-search/) | Medium | Backtracking | In-place 2D grid boundary DFS masking | O(M * N * 4^L) | O(L) | [Code](16_grid_backtracking/0079_word_search.py) |
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | Intervals | Sort by start boundary and absorb overlapping spans | O(n log n) | O(n) | [Python](17_intervals/0056_merge_intervals.py) |
| 57 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | Intervals | Three-stage linear sweep: before, overlap merge, and after | O(n) | O(n) | [Python](17_intervals/0057_insert_interval.py) |
| 435 | [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | Greedy Intervals | Earliest finish-time sort to minimize overlap collisions | O(n log n) | O(1) | [Python](19_greedy_intervals/0435_non_overlapping_intervals.py) |
| 763 | [763. Partition Labels](https://leetcode.com/problems/partition-labels/) | Medium | Greedy Intervals | Last-occurrence boundary expansion window | O(n) | O(1) | [Python](19_greedy_intervals/0763_partition_labels.py) |
| 208 | [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | Tries | 26-ary retrieval tree with end-of-word boolean marker | `O(L)` | `O(N * L)` | [Python](08_tries/0208_implement_trie.py) |
| 211 | [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Medium | Tries | Prefix tree combined with backtracking DFS wildcard matching | `O(L)` / `O(26^L)` | `O(N * L)` | [Python](08_tries/0211_design_add_and_search_words.py) |
| 212 | [212. Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard | Tries | Prefix Trie pruning with 2D matrix DFS backtracking | `O(M * N * 4 * 3^(L-1))` | `O(K * L)` | [Python](20_tries/0212_word_search_ii.py) |
| 215 | [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | Heaps | Bounded size-k min-heap invariant | `O(n log k)` | `O(k)` | [Python](21_heaps/0215_kth_largest_element.py) |
| 295 | [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | Heaps | Dual balanced max/min heaps partition | `O(log n)` | `O(n)` | [Python](21_heaps/0295_find_median_from_data_stream.py) |
| 127 | [127. Word Ladder](https://leetcode.com/problems/word-ladder/) | Hard | Graph BFS | Bidirectional frontier BFS with wildcard bucketing | `O(M^2 * N)` | `O(M^2 * N)` | [Python](23_graph_bfs/0127_word_ladder.py) |
| 207 | [207. Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | Graph BFS | Kahn's algorithm in-degree topological sort | `O(V + E)` | `O(V + E)` | [Python](23_graph_bfs/0207_course_schedule.py) |
| 684 | [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Medium | Graph DSU | Disjoint Set Union with path compression cycle detection | `O(E * alpha(V))` | `O(V)` | [Python](24_mst_union_find/0684_redundant_connection.py) |
| 1584 | [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | Graph MST | Kruskal algorithm with Manhattan edge greedy sort | `O(N^2 log N)` | `O(N^2)` | [Python](24_mst_union_find/1584_min_cost_to_connect_all_points.py) |



## 🧪 Automated Testing & Verification

Each algorithmic cluster contains unit tests and invariant validation:

```bash
pytest -v 08_tries/test_tries.py
pytest -v 11_dynamic_programming/test_dp.py
pytest -v 12_dynamic_programming_2d/test_dp_2d.py
pytest -v 20_tries/test_tries.py
pytest -v 21_heaps/test_heaps.py
pytest -v 24_mst_union_find/test_mst_union_find.py
| 743 | [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | Graph Shortest Path | Dijkstra min-heap greedy relaxation | O((V + E) log V) | O(V + E) | [Python](25_graph_shortest_path/0743_network_delay_time.py) |
| 787 | [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium | Graph Shortest Path | Snapshot Bellman-Ford relaxation bounded by K stops | O(K * E) | O(V) | [Python](25_graph_shortest_path/0787_cheapest_flights_k_stops.py) |
