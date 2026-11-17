"""
LeetCode 188: Best Time to Buy and Sell Stock IV
Difficulty: Hard
Pattern: Cluster 45 — Dynamic Programming (Generalized 2k-State Rolling Profit Vector)

Time Complexity: O(n * min(k, n // 2))
Space Complexity: O(k)
"""

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2 or k <= 0:
            return 0

        # When k >= n // 2, transactions are effectively unbounded (greedy peak-valley capture)
        if k >= n // 2:
            return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, n))

        buy = [-prices[0]] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices[1:]:
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j - 1] - price)
                sell[j] = max(sell[j], buy[j] + price)

        return sell[k]


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit(2, [2, 4, 1]) == 2
    assert sol.maxProfit(2, [3, 2, 6, 5, 0, 3]) == 7
    print("LC 188 verified successfully!")
