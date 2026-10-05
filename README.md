# LeetCode Patterns & Algorithmic Problem Solving 🧠

Curated solutions to LeetCode problems organized by algorithmic patterns, focusing on strict time/space complexity invariants.

![LeetCode Patterns Solved](https://img.shields.io/badge/Solved-15%20Patterns-brightgreen)
![Clusters Completed](https://img.shields.io/badge/Clusters-5%2F5%20Active-blue)
![Complexity](https://img.shields.io/badge/Complexity-O(1)%20Auxiliary%20Space-blue)
---

### 📊 Pattern Progress Tracker

| # | Problem | Difficulty | Pattern | Invariant / Technique | Time | Space | Solution |
| :---: | :--- | :---: | :---: | :--- | :---: | :---: | :---: |
| 1 | Two Sum | Easy | Arrays & Hashing | Hash map complement lookup | $O(n)$ | $O(n)$ | [Code](01_arrays_and_hashing/0001_two_sum.py) |
| 125 | Valid Palindrome | Easy | Two Pointers | Inward-converging two pointers | $O(n)$ | $O(1)$ | [Code](02_two_pointers/0125_valid_palindrome.py) |
| 167 | Two Sum II - Input Array Is Sorted | Medium | Two Pointers | Monotonic sorted sum convergence | $O(n)$ | $O(1)$ | [Code](02_two_pointers/0167_two_sum_ii_sorted.py) |
| 11 | Container With Most Water | Medium | Two Pointers | Inward scan greedy bottleneck shift | $O(n)$ | $O(1)$ | [Code](02_two_pointers/0011_container_with_most_water.py) |
| 121 | Best Time to Buy and Sell Stock | Easy | Sliding Window | Monotonic minimum anchor | $O(n)$ | $O(1)$ | [Code](03_sliding_window/0121_best_time_to_buy_and_sell_stock.py) |
| 3 | Longest Substring Without Repeating Characters | Medium | Sliding Window | Dynamic hash map index jump | $O(n)$ | $O(\min(n, m))$ | [Code](03_sliding_window/0003_longest_substring_without_repeating_characters.py) |
| 424 | Longest Repeating Character Replacement | Medium | Sliding Window | Frequency count valid window expansion | $O(n)$ | $O(1)$ | [Code](03_sliding_window/0424_longest_repeating_character_replacement.py) |
| 20 | Valid Parentheses | Easy | Stack | LIFO hash map bracket matching | $O(n)$ | $O(n)$ | [Code](04_stack/0020_valid_parentheses.py) |
| 155 | Min Stack | Medium | Stack | Synchronized tuple minimum tracking | $O(1)$ ops | $O(n)$ | [Code](04_stack/0155_min_stack.py) |
| 739 | Daily Temperatures | Medium | Stack | Monotonic decreasing index stack | $O(n)$ | $O(n)$ | [Code](04_stack/0739_daily_temperatures.py) |
| 704 | Binary Search | Easy | Binary Search | Monotonic window bisection | $O(\log n)$ | $O(1)$ | [Code](05_binary_search/0704_binary_search.py) |
| 74 | Search a 2D Matrix | Medium | Binary Search | Virtual 1D-to-2D row/col coordinate projection | $O(\log(m \cdot n))$ | $O(1)$ | [Code](05_binary_search/0074_search_a_2d_matrix.py) |
| 875 | Koko Eating Bananas | Medium | Binary Search | Monotonic answer space feasibility search | $O(n \log(\max(P)))$ | $O(1)$ | [Code](05_binary_search/0875_koko_eating_bananas.py) |
| 206 | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | Linked List | Three-pointer in-place traversal reversal | $O(n)$ | $O(1)$ | [Python](06_linked_list/0206_reverse_linked_list.py) |
| 21 | [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | Linked List | Sentinel dummy head splice merge | $O(n + m)$ | $O(1)$ | [Python](06_linked_list/0021_merge_two_sorted_lists.py) |