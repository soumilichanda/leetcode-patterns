"""
LeetCode 714: Best Time to Buy and Sell Stock with Transaction Fee
Difficulty: Medium
Pattern: Cluster 44 — Dynamic Programming (2-State Rolling Profit Transition)

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0

        cash = 0
        hold = -prices[0]

        for price in prices[1:]:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)

        return cash


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([1, 3, 2, 8, 4, 9], 2) == 8
    assert sol.maxProfit([1, 3, 7, 5, 10, 3], 3) == 6
    print("LC 714 verified successfully!")
