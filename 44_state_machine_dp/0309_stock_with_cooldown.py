"""
LeetCode 309: Best Time to Buy and Sell Stock with Cooldown
Difficulty: Medium
Pattern: Cluster 44 — Dynamic Programming (3-State Finite State Machine)

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        held = -prices[0]
        sold = 0
        rest = 0

        for price in prices[1:]:
            prev_held = held
            prev_sold = sold
            prev_rest = rest

            held = max(prev_held, prev_rest - price)
            sold = prev_held + price
            rest = max(prev_rest, prev_sold)

        return max(sold, rest)


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([1, 2, 3, 0, 2]) == 3
    assert sol.maxProfit([1]) == 0
    print("LC 309 verified successfully!")
