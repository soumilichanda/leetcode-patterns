"""
LeetCode 123: Best Time to Buy and Sell Stock III
Difficulty: Hard
Pattern: Cluster 32 — Multidimensional DP / Sequential Stage Transduction

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        buy1, buy2 = -float("inf"), -float("inf")
        sell1, sell2 = 0, 0

        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)

        return sell2


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert sol.maxProfit([1, 2, 3, 4, 5]) == 4
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    print("LC 123 verified successfully!")
