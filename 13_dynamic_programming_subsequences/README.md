# Cluster 13: Subsequences & Partition Dynamic Programming

| Problem | Algorithmic Pattern | State Invariant & Recurrence | Time | Space |
| :--- | :--- | :--- | :---: | :---: |
| **LC 300 (LIS)** | Patience Sorting / Binary Search | `tails[k]` stores smallest tail of increasing subsequences of length $k+1$. Bisection via `bisect_left`. | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n)$ |
| **LC 416 (Partition Equal Subset Sum)** | 0/1 Knapsack Decision | Target sum $W = \frac{\sum nums}{2}$. Reverse iteration: $dp[w] = dp[w] \lor dp[w - num]$ to prevent duplicate element reuse. | $\mathcal{O}(n \cdot W)$ | $\mathcal{O}(W)$ |
