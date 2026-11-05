"""
LeetCode 188: Best Time to Buy and Sell Stock IV
Difficulty: Hard
Pattern: Cluster 33 — DP General k-Transactions

Time Complexity: O(k * n)
Space Complexity: O(k)
"""

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0

        n = len(prices)
        # Infinite transaction optimization if k >= n // 2
        if k >= n // 2:
            return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, n))

        # buy[j] is the max balance after buying the j-th stock
        # sell[j] is the max profit after selling the j-th stock
        buy = [-float("inf")] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j - 1] - price)
                sell[j] = max(sell[j], buy[j] + price)

        return sell[k]


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit(2, [2, 4, 1]) == 2
    assert sol.maxProfit(2, [3, 2, 6, 5, 0, 3]) == 7
    print("LC 188 verified successfully!")
